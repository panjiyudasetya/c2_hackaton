"""
Jira ticket readiness reviewer — scores a single ticket against a fixed
rubric (problem/behaviour/acceptance-criteria/edge-cases/API/dependencies/
permissions/designs/data/non-functional) using only the ticket's own
collected content and whatever its `explicit_links` point to.

Unlike DecisionAgent (which searches the whole vector index for a
free-form question), this targets exactly one ticket -- no semantic search
involved, so it works even before `decision-intel index` has ever been run;
it only needs the ticket itself to have been collected (`decision-intel
jira`), and benefits from `enrich`/`graph` having run so `explicit_links`
actually points at linked artifacts.

This module never writes to Jira itself -- it only reads and reports. The
one place this project *does* write back to Jira is posting the rendered
report as a comment (JiraCollector.post_comment, called explicitly by the
caller, e.g. the frontend's "Post to Jira" button -- never automatically).
Editing ticket fields or transitioning status is deliberately out of scope:
the reviewer's own system prompt says "do not invent missing requirements"
and "do not rewrite the ticket unless asked" -- it has no source for what
the *correct* missing content is, so writing it into real fields would mean
fabricating requirements, not identifying gaps in them.
"""

from __future__ import annotations

import json
import re
import time
from pathlib import Path
from typing import Any, Iterator

import anthropic

_MODEL = "claude-opus-5"

# Verbatim from the product spec -- do not paraphrase or "improve" this;
# the exact wording controls the scoring rubric and output structure.
_SYSTEM = """\
You are a Jira ticket readiness reviewer.

Your job is to determine whether a Jira card contains enough information for a developer to start implementation without needing significant clarification.

Analyze ONLY information available in the Jira card and its attached/linked artifacts. Do not invent missing requirements.

Evaluate these criteria:

1. User problem is clearly described
2. Expected outcome/behaviour is clearly described
3. Acceptance criteria are explicit and testable
4. Edge cases and error scenarios are defined
5. API/input/output behaviour is sufficiently specified
6. Dependencies and integrations are identified and described
7. User permissions/roles are defined where relevant
8. UI/UX designs or relevant technical specifications are available where relevant
9. Data requirements/validation rules are clear
10. Non-functional requirements are defined where relevant

For each criterion, assign:
- PASS = 1
- PARTIAL = 0.5
- FAIL = 0
- N/A = exclude from scoring

Calculate:

Readiness % =
(sum of applicable criterion scores / number of applicable criteria) × 100

Then classify:
- READY: >= 80%, with no critical criterion failing
- NEEDS CLARIFICATION: 50-79%
- NOT READY: < 50%

Critical criteria are:
- Expected behaviour
- Acceptance criteria
- Dependencies/integrations
- API behaviour, when the ticket involves an API
- Permissions, when the ticket involves restricted functionality

Important:
- Do not assume that missing information is acceptable.
- Do not penalize N/A criteria.
- Distinguish between "not mentioned" and "explicitly defined".
- For every PASS/PARTIAL/FAIL, provide concise evidence from the Jira card.
- Identify the exact missing information required to move the ticket toward READY.
- Do not rewrite the ticket unless asked.

Return exactly this structure:

Readiness: XX% — READY / NEEDS CLARIFICATION / NOT READY

| Criterion | Result | Evidence |
|---|---|---|
| User problem | PASS/PARTIAL/FAIL/N/A | ... |
| Expected behaviour | PASS/PARTIAL/FAIL/N/A | ... |
| Acceptance criteria | PASS/PARTIAL/FAIL/N/A | ... |
| Edge cases | PASS/PARTIAL/FAIL/N/A | ... |
| API behaviour | PASS/PARTIAL/FAIL/N/A | ... |
| Dependencies | PASS/PARTIAL/FAIL/N/A | ... |
| Permissions | PASS/PARTIAL/FAIL/N/A | ... |
| Designs/specifications | PASS/PARTIAL/FAIL/N/A | ... |
| Data/validation | PASS/PARTIAL/FAIL/N/A | ... |
| Non-functional requirements | PASS/PARTIAL/FAIL/N/A | ... |

Blocking issues:
- ...

Recommended questions for the Product Owner:
1. ...
2. ...
3. ...
"""


def _locate_ticket_file(output_dir: Path, key: str) -> Path | None:
    """Find the collected .md file for a Jira key like ``PTO-123``."""
    project = key.split("-")[0] if "-" in key else key
    candidate = output_dir / "jira" / project / f"{key}.md"
    if candidate.exists():
        return candidate
    matches = list((output_dir / "jira").rglob(f"{key}.md")) if (output_dir / "jira").exists() else []
    return matches[0] if matches else None


def _build_ticket_context(output_dir: Path, key: str, max_linked: int = 5) -> tuple[str, str]:
    """Return (title, context_markdown) for *key* plus content from whatever
    its explicit_links point to (Confluence pages, related tickets, PRs)."""
    from ..collectors.base import parse_frontmatter

    ticket_path = _locate_ticket_file(output_dir, key)
    if not ticket_path:
        raise ValueError(
            f"Jira ticket {key} not found under {output_dir}/jira -- "
            f"run `decision-intel jira --project {key.split('-')[0]}` (or --board) to collect it first."
        )

    content = ticket_path.read_text(encoding="utf-8")
    meta, _ = parse_frontmatter(content)
    title = meta.get("title", key)

    lines = [f"## Jira Ticket: {key}", "", content.strip(), ""]

    linked_ids = meta.get("explicit_links") or []
    seen_paths = {str(ticket_path.resolve())}
    added = 0

    if linked_ids:
        from ..graph import get_document_file_path

        for doc_id in linked_ids:
            if added >= max_linked:
                break
            file_path = get_document_file_path(doc_id, output_dir)
            if not file_path or str(Path(file_path).resolve()) in seen_paths:
                continue
            seen_paths.add(str(Path(file_path).resolve()))
            try:
                linked_content = Path(file_path).read_text(encoding="utf-8")
            except OSError:
                continue
            lines += [f"## Linked artifact: {doc_id}", "", linked_content.strip()[:4000], ""]
            added += 1

    return title, "\n".join(lines)


# ── history / re-check diffing ────────────────────────────────────────────────
# Lets a second run on the same ticket answer "did readiness actually improve,
# and what's still blocking" instead of just producing a fresh, disconnected
# report each time.

_HEADER_RE = re.compile(
    r"Readiness:\s*([\d.]+)\s*%.*?(READY|NEEDS CLARIFICATION|NOT READY)", re.IGNORECASE
)
_ROW_RE = re.compile(r"^\|\s*([^|]+?)\s*\|\s*(PASS|PARTIAL|FAIL|N/A)\s*\|", re.MULTILINE | re.IGNORECASE)


def parse_report(report: str) -> dict[str, Any]:
    """Pull the headline score and per-criterion results out of a rendered
    report -- both follow a fixed structure mandated by the reviewer's
    system prompt, so this is a plain regex, not another LLM call."""
    header = _HEADER_RE.search(report)
    criteria: dict[str, str] = {}
    for m in _ROW_RE.finditer(report):
        name = m.group(1).strip()
        if name.lower() == "criterion":  # the table's own header row
            continue
        criteria[name] = m.group(2).upper()

    return {
        "percentage": float(header.group(1)) if header else None,
        "classification": header.group(2).upper() if header else None,
        "criteria": criteria,
    }


def _history_path(output_dir: Path, issue_key: str) -> Path:
    return output_dir / ".readiness_history" / f"{issue_key}.json"


def _load_history(output_dir: Path, issue_key: str) -> list[dict[str, Any]]:
    path = _history_path(output_dir, issue_key)
    if not path.exists():
        return []
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []


def save_and_diff(output_dir: Path, issue_key: str, report: str, max_history: int = 20) -> dict[str, Any] | None:
    """Record *report* in this ticket's local history and, if a previous
    review exists, return what changed. Returns None on a ticket's first
    ever review (nothing to compare against yet)."""
    history = _load_history(output_dir, issue_key)
    previous = history[-1] if history else None

    parsed = parse_report(report)
    history.append({"timestamp": time.time(), **parsed})
    history = history[-max_history:]

    path = _history_path(output_dir, issue_key)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(history, indent=2), encoding="utf-8")

    if not previous:
        return None

    changed = {
        name: {"from": previous.get("criteria", {}).get(name), "to": result}
        for name, result in parsed["criteria"].items()
        if previous.get("criteria", {}).get(name) not in (None, result)
    }

    return {
        "previous_percentage": previous.get("percentage"),
        "previous_classification": previous.get("classification"),
        "previous_timestamp": previous.get("timestamp"),
        "new_percentage": parsed["percentage"],
        "new_classification": parsed["classification"],
        "changed_criteria": changed,
    }


class TicketReadinessReviewer:
    """Scores one Jira ticket's implementation readiness via the Anthropic SDK."""

    def __init__(self, output_dir: Path) -> None:
        self.output_dir = output_dir

    def review_stream(self, issue_key: str) -> Iterator[str]:
        """Yield the readiness report as it streams in. Raises ValueError
        if the ticket hasn't been collected."""
        title, context = _build_ticket_context(self.output_dir, issue_key)
        prompt = (
            f"# Ticket to review: {issue_key} — {title}\n\n"
            f"{context}\n\n"
            "Evaluate this ticket's implementation readiness per your instructions."
        )

        client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env

        with client.messages.stream(
            model=_MODEL,
            max_tokens=4096,
            system=_SYSTEM,
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            yield from stream.text_stream

    def review(self, issue_key: str) -> str:
        """Stream the report to stdout token-by-token and return the full text."""
        chunks: list[str] = []
        for text in self.review_stream(issue_key):
            print(text, end="", flush=True)
            chunks.append(text)

        print()
        return "".join(chunks)

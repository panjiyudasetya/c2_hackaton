"""Renders a Document as markdown with a YAML frontmatter "tag" block, in
the same style already used for GitHub docs in this project, e.g.:

    ---
    id: github:teqplay/dataflow_dag_core:pr:726
    source: github
    type: pull_request
    repo: teqplay/dataflow_dag_core
    number: 726
    title: PTO-2839 Promotes `visit_id` as primary key in `ods_port_visit`
    author: panjiyudasetya
    state: closed
    date: '2026-07-17'
    merged_at: '2026-07-22'
    base_branch: develop
    head_branch: chore/set-visit-id-as-pk
    url: https://github.com/teqplay/dataflow_dag_core/pull/726
    labels: []
    linked_issues: []
    explicit_links: []
    ---

Key order is: id, source, type, then every key in ``doc.extra`` in the order
the collector inserted them (this is how source-specific fields like Jira's
``board``/``assignee`` or Confluence's ``space`` slot in), then title,
author, status, date, url, and finally explicit_links.

This intentionally hand-rolls the YAML instead of depending on PyYAML, so
formatting stays exactly predictable (date-like strings quoted, empty lists
rendered as ``[]``, no surprise type coercion when the file is re-parsed).
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from .models import Document

_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_RESERVED_WORDS = {"true", "false", "null", "yes", "no", "on", "off", "~"}
_LEADING_INDICATORS = set("-?:,[]{}#&*!|>'\"%@`")


def _looks_numeric(text: str) -> bool:
    try:
        float(text)
        return True
    except ValueError:
        return False


def _needs_quote(text: str) -> bool:
    if text == "" or text != text.strip():
        return True
    if text.lower() in _RESERVED_WORDS or _looks_numeric(text):
        return True
    if text[0] in _LEADING_INDICATORS:
        return True
    if ": " in text or text.endswith(":") or " #" in text:
        return True
    return False


def _scalar(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value)
    if _DATE_RE.match(text) or _needs_quote(text):
        return "'" + text.replace("'", "''") + "'"
    return text


def _dump(fm: dict[str, Any]) -> str:
    lines: list[str] = []
    for key, value in fm.items():
        if isinstance(value, (list, tuple)):
            if not value:
                lines.append(f"{key}: []")
            else:
                lines.append(f"{key}:")
                lines.extend(f"  - {_scalar(item)}" for item in value)
        else:
            lines.append(f"{key}: {_scalar(value)}")
    return "\n".join(lines)


def build_frontmatter(doc: Document) -> dict[str, Any]:
    """Assemble the ordered tag dict for a Document (exposed separately from
    ``to_markdown`` so callers/tests can inspect the tags without parsing
    YAML back out)."""
    fm: dict[str, Any] = {
        "id": doc.doc_id,
        "source": doc.source,
        "type": doc.type,
    }
    for key, value in (doc.extra or {}).items():
        fm[key] = value
    fm["title"] = doc.title
    if doc.author:
        fm["author"] = doc.author
    if doc.status:
        fm["status"] = doc.status
    if doc.date:
        fm["date"] = doc.date
    fm["url"] = doc.url
    fm["explicit_links"] = list(doc.explicit_links or [])
    return fm


def to_markdown(doc: Document) -> str:
    fm = build_frontmatter(doc)
    body = (doc.body or "").strip("\n")
    return f"---\n{_dump(fm)}\n---\n\n{body}\n"


def write_document(path: str, doc: Document) -> str:
    """Write ``doc`` as tagged markdown to ``path``, creating parent dirs as
    needed. Returns the path (as str) for convenience, matching how the
    collectors already call this."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(to_markdown(doc), encoding="utf-8")
    return str(p)

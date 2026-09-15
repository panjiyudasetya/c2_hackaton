"""
Phase 5 — AI agent using the Anthropic SDK with streaming.

Evidence is gathered locally (vector search + graph), then sent to Claude
in a single prompt.  Tokens stream to stdout as they arrive so the user
sees the answer building up in real time.
"""

from __future__ import annotations

from pathlib import Path

import anthropic

_MODEL = "claude-opus-5"

_SYSTEM = """\
You are a decision-intelligence assistant for an engineering team. Your job is to explain
WHY technical decisions were made by analysing evidence collected from GitHub, JIRA,
Confluence, and Notion.

The user's question and all relevant evidence have already been collected for you below.
Answer solely from the provided evidence — do not make up facts not present in it.

When answering:
1. Cite every claim with the document id (e.g. github:org/repo:pr:42).
2. Be explicit about gaps — where the evidence is missing or ambiguous, say so.

Structure your final answer with:
- Summary (2-3 sentences)
- Decisions made (bullet list: decision → reason)
- Rationale (paragraph explaining the "why" behind the decisions)
- Supporting evidence (list of doc ids with one-line description)
- Gaps (what information is missing or unclear)
"""


def _build_context(output_dir: Path, question: str, top_k: int = 15) -> str:
    """
    Run semantic search + graph traversal locally; return a formatted evidence block.
    """
    from decision_intel.graph import get_document_file_path, get_linked_documents
    from decision_intel.indexer import search_documents

    results = search_documents(query=question, output_dir=output_dir, top_k=top_k)
    if not results:
        return "No relevant documents found in the index."

    lines: list[str] = ["## Search Results", ""]
    seen_files: set[str] = set()

    for r in results:
        file_path: str = r.metadata.get("file_path", "")
        lines.append(f"### {r.doc_id}  (score: {r.score:.3f})")
        if file_path:
            lines.append(f"**File:** {file_path}")
        lines.append("")
        lines.append(r.text[:2000])
        lines.append("")
        if file_path:
            seen_files.add(file_path)

    # Follow graph links from the top-3 results
    linked_lines: list[str] = []
    for r in results[:3]:
        try:
            linked = get_linked_documents(
                doc_id=r.doc_id,
                output_dir=output_dir,
                min_confidence=0.5,
                depth=2,
            )
            for lnk in linked:
                lnk_path = get_document_file_path(lnk.doc_id, output_dir) or ""
                if not lnk_path or lnk_path in seen_files:
                    continue
                seen_files.add(lnk_path)
                linked_lines.append(f"### {lnk.doc_id}  (linked, confidence: {lnk.confidence:.3f})")
                linked_lines.append(f"**File:** {lnk_path}")
                linked_lines.append("")
                try:
                    content = Path(lnk_path).read_text(encoding="utf-8")
                    linked_lines.append(content[:2000])
                except OSError:
                    linked_lines.append("_(could not read file)_")
                linked_lines.append("")
        except Exception:
            pass

    if linked_lines:
        lines += ["## Linked Documents (via metadata graph)", ""] + linked_lines

    return "\n".join(lines)


class DecisionAgent:
    """Answers decision-reasoning questions with streaming output via the Anthropic SDK."""

    def __init__(self, output_dir: Path) -> None:
        self.output_dir = output_dir

    def ask(self, question: str) -> str:
        """
        Stream the answer to stdout token-by-token and return the full text.

        Reads ANTHROPIC_API_KEY from the environment (set in .env or shell).
        """
        context = _build_context(self.output_dir, question)
        prompt = (
            f"## Question\n\n{question}\n\n"
            f"{context}\n\n"
            "Please answer the question using only the evidence above."
        )

        client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env

        chunks: list[str] = []
        with client.messages.stream(
            model=_MODEL,
            max_tokens=8192,
            system=_SYSTEM,
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            for text in stream.text_stream:
                print(text, end="", flush=True)
                chunks.append(text)

        print()  # final newline after streaming finishes
        return "".join(chunks)

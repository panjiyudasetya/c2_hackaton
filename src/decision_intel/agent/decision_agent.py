"""
Phase 5 — AI agent using the Claude Code SDK.

Runs under your existing Claude Code session credentials — no separate
Anthropic API key required.

Strategy: search and graph calls are made locally in Python first, then the
collected evidence is embedded into a single prompt sent to Claude with no
tool calls.  This avoids the multi-turn tool loop that triggers rate-limit
events before a text answer is produced.
"""

from __future__ import annotations

import asyncio
import os
from pathlib import Path

from claude_code_sdk import ClaudeCodeOptions, query
from claude_code_sdk._errors import MessageParseError
from claude_code_sdk.types import AssistantMessage, ResultMessage, TextBlock

_SYSTEM = """\
You are a decision-intelligence assistant for an engineering team. Your job is to explain
WHY technical decisions were made by analysing evidence collected from GitHub, JIRA,
Confluence, and Notion.

The user's question and all relevant evidence have already been collected for you below.
Do NOT call any external tools — answer solely from the provided evidence.

When answering:
1. Cite every claim with the document id (e.g. github:org/repo:pr:42).
2. Be explicit about gaps — where the evidence is missing or ambiguous, say so.

Structure your final answer with:
- Summary (2–3 sentences)
- Decisions made (bullet list: decision → reason)
- Rationale (paragraph explaining the "why" behind the decisions)
- Supporting evidence (list of doc ids with one-line description)
- Gaps (what information is missing or unclear)
"""


def _build_context(output_dir: Path, question: str, top_k: int = 15) -> str:
    """Search + graph locally; return a formatted evidence block."""
    from ..indexer import search_documents
    from ..graph import get_linked_documents

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
    db_path = output_dir / ".graph.db"
    _db_conn = None
    if db_path.exists():
        import sqlite3
        _db_conn = sqlite3.connect(str(db_path))
        _db_conn.row_factory = sqlite3.Row

    for r in results[:3]:
        try:
            linked = get_linked_documents(
                doc_id=r.doc_id,
                output_dir=output_dir,
                min_confidence=0.5,
                depth=2,
            )
            for lnk in linked:
                lnk_path = ""
                if _db_conn:
                    row = _db_conn.execute(
                        "SELECT file_path FROM documents WHERE id = ?", (lnk.doc_id,)
                    ).fetchone()
                    lnk_path = row["file_path"] if row and row["file_path"] else ""
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

    if _db_conn:
        _db_conn.close()

    if linked_lines:
        lines += ["## Linked Documents (via metadata graph)", ""] + linked_lines

    return "\n".join(lines)


class DecisionAgent:
    """Answers decision-reasoning questions using the Claude Code SDK."""

    def __init__(self, output_dir: Path) -> None:
        self.output_dir = output_dir

    def ask(self, question: str) -> str:
        """Run the agent and return the final answer as markdown."""
        return asyncio.run(self._ask_async(question))

    async def _ask_async(self, question: str) -> str:
        # ANTHROPIC_API_KEY (loaded from .env) takes precedence over the
        # Claude.ai OAuth session that claude-code-sdk needs. Remove it for
        # the duration of this call, then restore it afterwards.
        removed: dict[str, str] = {}
        for key in ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN"):
            val = os.environ.pop(key, None)
            if val:
                removed[key] = val

        # Gather evidence locally — no tool calls needed.
        context = _build_context(self.output_dir, question)

        prompt = (
            f"## Question\n\n{question}\n\n"
            f"{context}\n\n"
            "Please answer the question using only the evidence above."
        )

        options = ClaudeCodeOptions(
            allowed_tools=[],          # no tools — single-turn answer
            append_system_prompt=_SYSTEM,
            cwd=str(self.output_dir.parent),
            max_turns=1,
        )

        last_text = ""
        try:
            aiter = query(prompt=prompt, options=options).__aiter__()
            while True:
                try:
                    message = await aiter.__anext__()
                except StopAsyncIteration:
                    break
                except MessageParseError:
                    continue

                if isinstance(message, ResultMessage):
                    if message.result:
                        return message.result
                elif isinstance(message, AssistantMessage):
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            last_text = block.text
        finally:
            os.environ.update(removed)

        return last_text or "No answer produced."

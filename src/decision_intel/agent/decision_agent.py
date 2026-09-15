"""
Phase 5 — AI agent using the Anthropic Tool Runner.

The SDK drives the tool-use loop; this module only defines the three tools
and extracts the final text answer from the last runner message.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import anthropic
from anthropic import beta_tool

from ..graph import get_linked_documents
from ..indexer import search_documents

_MODEL = "claude-opus-5"

_SYSTEM = """\
You are a decision-intelligence assistant for an engineering team. Your job is to explain
WHY technical decisions were made by analysing evidence collected from GitHub, JIRA,
Confluence, and Notion.

When answering:
1. Use search_documents_tool first to find relevant context for the user's question.
2. Use get_linked_documents_tool to follow cross-source chains (e.g. a JIRA ticket that
   links to a design doc that links to a PR).
3. Use read_document when you need the full content of a specific file.
4. Cite every claim with the document id (e.g. github:org/repo:pr:42).
5. Be explicit about gaps — where the evidence is missing or ambiguous, say so.

Structure your final answer with:
- Summary (2–3 sentences)
- Decisions made (bullet list: decision → reason)
- Rationale (paragraph explaining the "why" behind the decisions)
- Supporting evidence (list of doc ids with one-line description)
- Gaps (what information is missing or unclear)
"""


class DecisionAgent:
    """Answers decision-reasoning questions using collected documents."""

    def __init__(self, output_dir: Path) -> None:
        self.output_dir = output_dir
        self.client = anthropic.Anthropic()
        self._tools = self._build_tools()

    # ── tool definitions ───────────────────────────────────────────────────────

    def _build_tools(self) -> list:
        """Create @beta_tool-decorated functions closed over self.output_dir."""
        output_dir = self.output_dir

        @beta_tool
        def search_documents_tool(
            query: str,
            top_k: int = 10,
            source: Optional[str] = None,
            since: Optional[str] = None,
        ) -> str:
            """Semantic search over all collected documents.

            Use this first to find documents relevant to the user's question.
            Returns the top matching chunks with their source metadata.

            Args:
                query: Natural-language search query.
                top_k: Number of results to return (default 10).
                source: Filter to this source only — github, jira, notion, or confluence.
                since: Only include documents updated on or after this date (YYYY-MM-DD).
            """
            results = search_documents(
                query=query,
                output_dir=output_dir,
                top_k=top_k,
                source=source,
                since=since,
            )
            if not results:
                return "No results found."
            return json.dumps([r.to_dict() for r in results], indent=2)

        @beta_tool
        def get_linked_documents_tool(
            doc_id: str,
            min_confidence: float = 0.5,
            depth: int = 2,
        ) -> str:
            """Follow cross-source links from a document through the metadata graph.

            Use this after finding a document via search to discover what it links to
            (e.g. the JIRA ticket that motivated a PR, the Confluence page that designed it).

            Args:
                doc_id: Document ID to start from, e.g. 'github:org/repo:pr:42' or 'jira:OFI-123'.
                min_confidence: Minimum link confidence to include, 0 to 1 (default 0.5).
                depth: Number of hops to traverse (default 2).
            """
            results = get_linked_documents(
                doc_id=doc_id,
                output_dir=output_dir,
                min_confidence=min_confidence,
                depth=depth,
            )
            if not results:
                return "No linked documents found."
            return json.dumps([r.to_dict() for r in results], indent=2)

        @beta_tool
        def read_document(file_path: str) -> str:
            """Read the full markdown content of a specific collected document.

            Use this when a search result or linked document needs to be read in full.

            Args:
                file_path: Absolute or relative path to the .md file.
            """
            path = Path(file_path)
            if not path.exists():
                return f"File not found: {file_path}"
            content = path.read_text(encoding="utf-8")
            if len(content) > 20_000:
                content = content[:20_000] + "\n\n_[content truncated]_"
            return content

        return [search_documents_tool, get_linked_documents_tool, read_document]

    # ── agent loop ─────────────────────────────────────────────────────────────

    def ask(self, question: str) -> str:
        """Run the Tool Runner loop and return the final answer as markdown."""
        runner = self.client.beta.messages.tool_runner(
            model=_MODEL,
            max_tokens=16_000,
            thinking={"type": "adaptive"},
            system=_SYSTEM,
            tools=self._tools,
            messages=[{"role": "user", "content": question}],
        )

        last = None
        for message in runner:
            last = message

        if last is None:
            return "No response."

        for block in last.content:
            if hasattr(block, "type") and block.type == "text":
                return block.text

        return ""

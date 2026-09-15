"""
Phase 5 — AI agent that answers decision questions using tool use.

Tools available to the agent:
- search_documents   → semantic search via ChromaDB
- get_linked_documents → graph traversal via SQLite
- read_document      → return full markdown content of one file
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import anthropic

from ..graph import get_linked_documents
from ..indexer import search_documents

_MODEL = "claude-opus-5"

_SYSTEM = """\
You are a decision-intelligence assistant for an engineering team. Your job is to explain
WHY technical decisions were made by analysing evidence collected from GitHub, JIRA,
Confluence, and Notion.

When answering:
1. Use search_documents first to find relevant context for the user's question.
2. Use get_linked_documents to follow cross-source chains (e.g. a JIRA ticket that
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

_TOOLS: list[dict[str, Any]] = [
    {
        "name": "search_documents",
        "description": (
            "Semantic search over all collected documents (GitHub issues, PRs, JIRA tickets, "
            "Notion pages, Confluence pages). Use this first to find documents relevant to the "
            "user's question. Returns the top matching chunks with their source metadata."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Natural-language search query.",
                },
                "top_k": {
                    "type": "integer",
                    "description": "Number of results to return (default 10).",
                    "default": 10,
                },
                "source": {
                    "type": "string",
                    "enum": ["github", "jira", "notion", "confluence"],
                    "description": "Filter results to this source only (optional).",
                },
                "since": {
                    "type": "string",
                    "description": "Filter to documents updated on or after this date YYYY-MM-DD (optional).",
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "get_linked_documents",
        "description": (
            "Follow cross-source links from a known document ID through the metadata graph. "
            "Use this after finding a document via search to discover what it links to "
            "(e.g. the JIRA ticket that motivated a PR, the Confluence page that designed it)."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "doc_id": {
                    "type": "string",
                    "description": "Document ID to start from, e.g. 'github:org/repo:pr:42' or 'jira:OFI-123'.",
                },
                "min_confidence": {
                    "type": "number",
                    "description": "Minimum link confidence to include (0–1, default 0.5).",
                    "default": 0.5,
                },
                "depth": {
                    "type": "integer",
                    "description": "Number of hops to traverse (default 2).",
                    "default": 2,
                },
            },
            "required": ["doc_id"],
        },
    },
    {
        "name": "read_document",
        "description": (
            "Read the full markdown content of a specific collected document by its file path. "
            "Use this when a search result or linked document needs to be read in full."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Absolute or relative path to the .md file.",
                },
            },
            "required": ["file_path"],
        },
    },
]


class DecisionAgent:
    """Answers decision-reasoning questions using collected documents."""

    def __init__(self, output_dir: Path) -> None:
        self.output_dir = output_dir
        self.client = anthropic.Anthropic()

    # ── tool execution ─────────────────────────────────────────────────────────

    def _exec_tool(self, name: str, inputs: dict[str, Any]) -> str:
        if name == "search_documents":
            results = search_documents(
                query=inputs["query"],
                output_dir=self.output_dir,
                top_k=inputs.get("top_k", 10),
                source=inputs.get("source"),
                since=inputs.get("since"),
            )
            if not results:
                return "No results found."
            return json.dumps([r.to_dict() for r in results], indent=2)

        if name == "get_linked_documents":
            results = get_linked_documents(
                doc_id=inputs["doc_id"],
                output_dir=self.output_dir,
                min_confidence=inputs.get("min_confidence", 0.5),
                depth=inputs.get("depth", 2),
            )
            if not results:
                return "No linked documents found."
            return json.dumps([r.to_dict() for r in results], indent=2)

        if name == "read_document":
            path = Path(inputs["file_path"])
            if not path.exists():
                return f"File not found: {path}"
            content = path.read_text(encoding="utf-8")
            # Cap at 20 000 chars to fit comfortably in context
            if len(content) > 20_000:
                content = content[:20_000] + "\n\n_[content truncated]_"
            return content

        return f"Unknown tool: {name}"

    # ── agent loop ─────────────────────────────────────────────────────────────

    def ask(self, question: str) -> str:
        """
        Run the agent loop and return the final answer as a markdown string.

        The agent decides which tools to call and in what order.
        """
        messages: list[dict[str, Any]] = [{"role": "user", "content": question}]

        while True:
            response = self.client.messages.create(
                model=_MODEL,
                max_tokens=16_000,
                thinking={"type": "adaptive"},
                system=_SYSTEM,
                tools=_TOOLS,
                messages=messages,
            )

            # Accumulate the assistant turn
            messages.append({"role": "assistant", "content": response.content})

            if response.stop_reason == "end_turn":
                # Extract the final text answer
                for block in response.content:
                    if hasattr(block, "type") and block.type == "text":
                        return block.text
                return ""

            if response.stop_reason == "tool_use":
                tool_results: list[dict[str, Any]] = []
                for block in response.content:
                    if not (hasattr(block, "type") and block.type == "tool_use"):
                        continue
                    result_text = self._exec_tool(block.name, block.input)
                    tool_results.append({
                        "type":        "tool_result",
                        "tool_use_id": block.id,
                        "content":     result_text,
                    })
                messages.append({"role": "user", "content": tool_results})
                continue

            # Unexpected stop reason — surface what we have
            break

        return "Agent stopped unexpectedly."

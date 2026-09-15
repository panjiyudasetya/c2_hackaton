"""
Phase 5 — AI agent using the Claude Code SDK.

Runs under your existing Claude Code session credentials — no separate
Anthropic API key required.  The agent uses the built-in Bash tool to
call three decision-intel CLI subcommands:
  decision-intel search "query"
  decision-intel links  "doc_id"
  decision-intel read-doc "file_path"
"""

from __future__ import annotations

import asyncio
import shutil
from pathlib import Path

from claude_code_sdk import ClaudeCodeOptions, query
from claude_code_sdk.types import AssistantMessage, ResultMessage, TextBlock

_SYSTEM = """\
You are a decision-intelligence assistant for an engineering team. Your job is to explain
WHY technical decisions were made by analysing evidence collected from GitHub, JIRA,
Confluence, and Notion.

You have three bash commands available (always run them from the project directory):

  decision-intel search "QUERY" [--top-k N] [--source github|jira|notion|confluence] [--since YYYY-MM-DD]
      Semantic search over all collected documents. Returns JSON with doc_id, text, score, file_path.

  decision-intel links "DOC_ID" [--min-confidence 0.5] [--depth 2]
      Follow cross-source links from a document through the metadata graph.
      Returns JSON list of linked documents with confidence scores.

  decision-intel read-doc "FILE_PATH"
      Read the full markdown content of a specific collected document.

When answering:
1. Use `decision-intel search` first to find relevant context.
2. Use `decision-intel links` to follow cross-source chains (JIRA → Confluence → PR).
3. Use `decision-intel read-doc` when you need the full content of a specific file.
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
    """Answers decision-reasoning questions using the Claude Code SDK."""

    def __init__(self, output_dir: Path) -> None:
        self.output_dir = output_dir
        cli_path = shutil.which("decision-intel") or "decision-intel"
        self._system = _SYSTEM + f"\nThe decision-intel command is at: {cli_path}\n"

    def ask(self, question: str) -> str:
        """Run the agent and return the final answer as markdown."""
        return asyncio.run(self._ask_async(question))

    async def _ask_async(self, question: str) -> str:
        options = ClaudeCodeOptions(
            allowed_tools=["Bash"],
            append_system_prompt=self._system,
            cwd=str(self.output_dir.parent),
            max_turns=20,
        )

        last_text = ""
        async for message in query(prompt=question, options=options):
            if isinstance(message, ResultMessage):
                # ResultMessage.result holds the final plain-text answer
                if message.result:
                    return message.result
            elif isinstance(message, AssistantMessage):
                # Accumulate text blocks in case ResultMessage has no result
                for block in message.content:
                    if isinstance(block, TextBlock):
                        last_text = block.text

        return last_text or "No answer produced."

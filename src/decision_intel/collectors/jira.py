"""
JIRA collector — fetches issues (and their comments) and writes one markdown file each.
"""

from __future__ import annotations

import os
import re
from pathlib import Path

from .base import BaseCollector


def _safe_filename(text: str) -> str:
    return re.sub(r"[^\w\-]", "_", text).strip("_")[:80]


def _md_escape(text: str | None) -> str:
    return (text or "").replace("|", "\\|")


class JiraCollector(BaseCollector):
    """
    Collects JIRA issues matching a JQL query and writes them as markdown.
    """

    def __init__(self, output_dir: Path) -> None:
        super().__init__(output_dir / "jira")

    def is_configured(self) -> bool:
        return all(
            os.environ.get(k) for k in ("JIRA_URL", "JIRA_USER", "JIRA_API_TOKEN")
        )

    def _client(self):
        from atlassian import Jira  # lazy import — not installed until needed

        return Jira(
            url=os.environ["JIRA_URL"],
            username=os.environ["JIRA_USER"],
            password=os.environ["JIRA_API_TOKEN"],
            cloud=True,
        )

    def collect(self, jql: str = "", max_results: int = 50, **kwargs) -> list[Path]:
        """
        Fetch issues matching *jql* and write one .md file per issue.

        Args:
            jql: JQL filter string, e.g. ``project = OFI AND sprint in openSprints()``.
                 Defaults to all issues updated in the last 30 days.
            max_results: Maximum number of issues to fetch.
        """
        if not jql:
            jql = "order by updated DESC"

        jira = self._client()
        issues = jira.jql(jql, limit=max_results).get("issues", [])

        created: list[Path] = []
        for raw in issues:
            path = self._write_issue(jira, raw)
            created.append(path)
        return created

    def _write_issue(self, jira, raw: dict) -> Path:
        key = raw["key"]
        fields = raw.get("fields", {})

        title = fields.get("summary", "")
        description = fields.get("description") or ""
        issue_type = (fields.get("issuetype") or {}).get("name", "")
        status = (fields.get("status") or {}).get("name", "")
        priority = (fields.get("priority") or {}).get("name", "")
        reporter = ((fields.get("reporter") or {}).get("displayName") or
                    (fields.get("reporter") or {}).get("emailAddress", ""))
        assignee = ((fields.get("assignee") or {}).get("displayName") or
                    (fields.get("assignee") or {}).get("emailAddress") or "Unassigned")
        labels = fields.get("labels") or []
        components = [c.get("name", "") for c in (fields.get("components") or [])]
        created_at = (fields.get("created") or "")[:10]
        updated_at = (fields.get("updated") or "")[:10]
        url = f"{os.environ['JIRA_URL']}/browse/{key}"

        # Fetch comments
        comments_data = jira.issue(key, fields="comment").get("fields", {}).get("comment", {})
        raw_comments = comments_data.get("comments", [])

        lines: list[str] = [
            f"# [{key}] {title}",
            "",
            f"**URL:** {url}  ",
            f"**Type:** {issue_type} | **Status:** {status} | **Priority:** {priority}  ",
            f"**Reporter:** {reporter} | **Assignee:** {assignee}  ",
            f"**Created:** {created_at} | **Updated:** {updated_at}  ",
        ]

        if labels:
            lines.append(f"**Labels:** {', '.join(labels)}  ")
        if components:
            lines.append(f"**Components:** {', '.join(components)}  ")

        lines += ["", "## Description", "", description or "_No description._", ""]

        if raw_comments:
            lines += ["## Comments", ""]
            for c in raw_comments:
                author = (c.get("author") or {}).get("displayName", "Unknown")
                created = (c.get("created") or "")[:10]
                body = (c.get("body") or "").strip()
                lines += [f"### {author} — {created}", "", body, ""]

        filename = f"{_safe_filename(key)}.md"
        return self._write(filename, "\n".join(lines))

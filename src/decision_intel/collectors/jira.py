"""
JIRA collector — fetches issues (and their comments) and writes one markdown
file each, tagged with YAML frontmatter (id/source/type/.../explicit_links)
so Phase 2/3/4 (enrich/index/graph) can pick them up the same way they
already do for GitHub docs — see collectors/base.py's render_frontmatter.
"""

from __future__ import annotations

import os
from pathlib import Path

from .base import BaseCollector, render_frontmatter, safe_filename


def _adf_to_text(node) -> str:
    """Extract plain text from an Atlassian Document Format (ADF) node or plain string."""
    if isinstance(node, str):
        return node
    if not isinstance(node, dict):
        return ""
    if node.get("type") == "text":
        return node.get("text", "")
    parts = [_adf_to_text(child) for child in node.get("content", [])]
    sep = "\n" if node.get("type") in ("doc", "paragraph", "heading", "listItem",
                                        "bulletList", "orderedList", "blockquote",
                                        "codeBlock", "rule", "panel") else ""
    return sep.join(parts)


def _issue_links(fields: dict) -> list[tuple[str, str, str]]:
    """
    Return (related_key, related_summary, relation_label) for every issuelink on a raw fields dict.
    """
    out = []
    for link in fields.get("issuelinks", []) or []:
        if "inwardIssue" in link:
            issue = link["inwardIssue"]
            label = link["type"]["inward"]
        elif "outwardIssue" in link:
            issue = link["outwardIssue"]
            label = link["type"]["outward"]
        else:
            continue
        out.append((issue["key"], issue["fields"].get("summary", ""), label))
    return out


class JiraCollector(BaseCollector):
    """
    Collects JIRA issues matching a JQL query and writes them as markdown.
    """

    _required_env_vars = ["JIRA_URL", "JIRA_USER", "JIRA_API_TOKEN"]

    def __init__(self, output_dir: Path) -> None:
        super().__init__(output_dir / "jira")

    def _client(self):
        from atlassian import Jira  # lazy import — not installed until needed

        return Jira(
            url=os.environ["JIRA_URL"],
            username=os.environ["JIRA_USER"],
            password=os.environ["JIRA_API_TOKEN"],
            cloud=True,
        )

    def post_comment(self, issue_key: str, comment: str) -> str:
        """Post *comment* onto *issue_key* and return the ticket's URL.

        This is the one write operation this project performs against Jira --
        deliberately not status transitions or field edits (see
        agent/readiness_reviewer.py's module docstring for why). Uses the
        same credentials as collection, which already have whatever
        read/write scope the configured account has in Jira itself.
        """
        jira = self._client()
        jira.issue_add_comment(issue_key, comment)
        return f"{os.environ['JIRA_URL'].rstrip('/')}/browse/{issue_key}"

    def collect(self, jql: str = "", max_results: int = 50, **kwargs) -> list[Path]:
        """
        Fetch issues matching *jql* and write one .md file per issue.

        Args:
            jql: JQL filter string, e.g. ``project = OFI AND sprint in openSprints()``.
                 Defaults to issues updated in the last 30 days, newest first.
            max_results: Maximum number of issues to fetch.
        """
        if not jql.strip():
            jql = "updated >= -30d ORDER BY updated DESC"

        jira = self._client()
        result = jira.jql(jql, limit=max_results)
        issues = result.get("issues", [])
        total = min(result.get("total", len(issues)), max_results)

        created: list[Path] = []
        for n, raw in enumerate(issues, start=1):
            path = self._write_issue(jira, raw)
            created.append(path)
            self._report(n, total, "Cards")
        return created

    def collect_boards(self, board_names: list[str], max_results_per_board: int = 1000) -> list[Path]:
        """
        Fetch every card (and its subtasks) from Jira Agile boards whose name
        matches any of *board_names* (case-insensitive substring), via the
        Agile board view rather than a JQL filter — mirrors what the board
        actually shows, as opposed to `collect()`'s search-based selection.

        Args:
            board_names: Board name substrings to match, e.g. ``["PTO", "TCC"]``.
            max_results_per_board: Max cards to fetch per matching board.
        """
        jira = self._client()
        boards = self._find_boards(jira, board_names)

        created: list[Path] = []
        for board in boards:
            board_id = board["id"]
            board_name = board["name"]

            raw_issues = self._board_issues(jira, board_id, max_results_per_board)
            parents = [i for i in raw_issues if not i["fields"]["issuetype"]["subtask"]]

            for n, issue in enumerate(parents, start=1):
                created.append(self._write_issue(jira, issue, board_name=board_name))
                self._report(n, len(parents), f"{board_name} cards")

                for sub_ref in issue["fields"].get("subtasks") or []:
                    try:
                        sub_issue = jira.issue(sub_ref["key"])
                    except Exception:  # noqa: BLE001 — keep collecting other issues
                        continue
                    created.append(self._write_issue(jira, sub_issue, board_name=board_name))

        return created

    def list_all_boards(self, max_boards: int = 200) -> list[dict]:
        """Return every Agile board the credentials can see, as
        [{"id", "name", "type"}, ...] -- used by the web UI's board picker."""
        jira = self._client()
        boards: list[dict] = []
        start = 0
        while len(boards) < max_boards:
            page = jira.get_all_agile_boards(start=start, limit=50) or {}
            values = page.get("values", [])
            if not values:
                break
            boards.extend(
                {"id": b.get("id"), "name": b.get("name", "Unnamed"), "type": b.get("type", "")}
                for b in values
            )
            if page.get("isLast", True):
                break
            start += 50
        return boards[:max_boards]

    def _find_boards(self, jira, target_names: list[str]) -> list[dict]:
        """Return every Agile board whose name contains any of *target_names*."""
        boards: list[dict] = []
        start = 0
        while True:
            page = jira.get_all_agile_boards(start=start, limit=50) or {}
            values = page.get("values", [])
            if not values:
                break
            for board in values:
                name = board.get("name", "")
                if any(t.lower() in name.lower() for t in target_names):
                    boards.append(board)
            if page.get("isLast", True):
                break
            start += 50
        return boards

    def _board_issues(self, jira, board_id, max_results: int) -> list[dict]:
        """Return every card on *board_id* (parents and subtasks, unfiltered)."""
        issues: list[dict] = []
        start = 0
        while len(issues) < max_results:
            page = jira.get_issues_for_board(
                board_id, jql="", start=start, limit=min(50, max_results - len(issues))
            ) or {}
            batch = page.get("issues", [])
            if not batch:
                break
            issues.extend(batch)
            start += len(batch)
        return issues

    def _write_issue(self, jira, raw: dict, board_name: str | None = None) -> Path:
        key = raw["key"]
        fields = raw.get("fields", {})

        title = fields.get("summary", "")
        description = _adf_to_text(fields.get("description") or "")
        issuetype_fields = fields.get("issuetype") or {}
        issue_type = issuetype_fields.get("name", "")
        is_subtask = bool(issuetype_fields.get("subtask"))
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

        links = _issue_links(fields)
        explicit_links = [f"jira:{k}" for k, _, _ in links]
        parent = fields.get("parent")
        if parent:
            explicit_links.append(f"jira:{parent['key']}")

        project_key = key.split("-")[0] if "-" in key else "unknown"

        meta = {
            "id":             f"jira:{key}",
            "source":         "jira",
            "type":           "subtask" if is_subtask else "issue",
            "key":            key,
            "project":        project_key,
            "board":          board_name,
            "issuetype":      issue_type,
            "priority":       priority,
            "assignee":       assignee,
            "labels":         labels,
            "components":     components,
            "title":          title,
            "author":         reporter,
            "status":         status,
            "date":           created_at,
            "url":            url,
            "explicit_links": explicit_links,
        }

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

        if board_name:
            lines.append(f"**Board:** {board_name}  ")
        if labels:
            lines.append(f"**Labels:** {', '.join(labels)}  ")
        if components:
            lines.append(f"**Components:** {', '.join(components)}  ")
        if parent:
            lines.append(f"**Parent:** [{parent['key']}] {parent['fields'].get('summary', '')}  ")

        lines += ["", "## Description", "", description or "_No description._", ""]

        if links:
            lines += ["## Linked issues", ""]
            for rel_key, rel_summary, label in links:
                lines.append(f"- {label}: [{rel_key}] {rel_summary}")
            lines.append("")

        subtasks = fields.get("subtasks") or []
        if subtasks:
            lines += ["## Subtasks", ""]
            for sub in subtasks:
                sub_fields = sub.get("fields", {})
                sub_status = sub_fields.get("status", {}).get("name", "Unknown")
                lines.append(f"- [{sub['key']}] {sub_fields.get('summary', '')} ({sub_status})")
            lines.append("")

        if raw_comments:
            lines += ["## Comments", ""]
            for c in raw_comments:
                author = (c.get("author") or {}).get("displayName", "Unknown")
                c_created = (c.get("created") or "")[:10]
                body = _adf_to_text(c.get("body") or "").strip()
                lines += [f"### {author} — {c_created}", "", body, ""]

        filename = f"{project_key}/{safe_filename(key)}.md"
        return self._write(filename, render_frontmatter(meta, "\n".join(lines)))

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

        if raw_comments:
            lines += ["## Comments", ""]
            for c in raw_comments:
                author = (c.get("author") or {}).get("displayName", "Unknown")
                c_created = (c.get("created") or "")[:10]
                body = (c.get("body") or "").strip()
                lines += [f"### {author} — {c_created}", "", body, ""]

        filename = f"{project_key}/{safe_filename(key)}.md"
        return self._write(filename, render_frontmatter(meta, "\n".join(lines)))

"""
Confluence collector — fetches every page in a set of spaces and writes one
markdown file each, tagged with YAML frontmatter (id/source/type/.../
explicit_links), matching the convention already used for GitHub/JIRA docs —
see collectors/base.py's render_frontmatter.

Credentials are read from environment variables only - never hardcode a
token in this file or paste one into a chat:

    CONFLUENCE_URL         e.g. https://your-org.atlassian.net/wiki
    CONFLUENCE_USER        your Atlassian account email
    CONFLUENCE_API_TOKEN   an Atlassian API token (can reuse the JIRA one —
                            Jira and Confluence share Atlassian Cloud auth)
"""

from __future__ import annotations

import os
from pathlib import Path

from .base import BaseCollector, render_frontmatter, safe_filename

PAGE_SIZE = 50


class ConfluenceCollector(BaseCollector):
    """
    Collects every page in the given Confluence spaces and writes them as markdown.
    """

    _required_env_vars = ["CONFLUENCE_URL", "CONFLUENCE_USER", "CONFLUENCE_API_TOKEN"]

    def __init__(self, output_dir: Path) -> None:
        super().__init__(output_dir / "confluence")

    def _client(self):
        from atlassian import Confluence  # lazy import — not installed until needed

        return Confluence(
            url=os.environ["CONFLUENCE_URL"],
            username=os.environ["CONFLUENCE_USER"],
            password=os.environ["CONFLUENCE_API_TOKEN"],
            cloud=True,
        )

    def collect(self, space_keys: list[str], max_pages: int = 100, **kwargs) -> list[Path]:
        """
        Fetch every page in each of *space_keys* and write one .md file per page.

        Args:
            space_keys: Confluence space keys, e.g. ``["TC", "PTO"]``.
            max_pages: Max pages to fetch per space.
        """
        confluence = self._client()

        created: list[Path] = []
        for space_key in space_keys:
            for page in self._iter_pages(confluence, space_key, max_pages):
                created.append(self._write_page(confluence, page, space_key))
        return created

    def _iter_pages(self, confluence, space_key: str, max_pages: int) -> list[dict]:
        pages: list[dict] = []
        start = 0
        while len(pages) < max_pages:
            batch = confluence.get_all_pages_from_space(
                space_key,
                start=start,
                limit=min(PAGE_SIZE, max_pages - len(pages)),
                expand="body.storage,version,history",
            )
            if not batch:
                break
            pages.extend(batch)
            start += PAGE_SIZE
        return pages

    def _write_page(self, confluence, page: dict, space_key: str) -> Path:
        from markdownify import markdownify as md

        page_id = page["id"]
        title = page.get("title", "Untitled")
        base_url = confluence.url.rstrip("/")
        url = f"{base_url}/spaces/{space_key}/pages/{page_id}"

        html_content = page.get("body", {}).get("storage", {}).get("value", "")
        body = md(html_content, heading_style="ATX").strip()

        version = page.get("version") or {}
        author = ((version.get("by") or {}).get("displayName") or
                  (page.get("history", {}).get("createdBy", {}).get("displayName", "")))
        date = version.get("when") or page.get("history", {}).get("createdDate", "")

        meta = {
            "id":             f"confluence:{page_id}",
            "source":         "confluence",
            "type":           "page",
            "space":          space_key,
            "title":          title,
            "author":         author,
            "date":           date[:10] if date else "",
            "url":            url,
            "explicit_links": [],
        }

        lines = [
            f"# {title}",
            "",
            f"**Space:** {space_key}  ",
            f"**URL:** {url}  ",
            "",
            "## Content",
            "",
            body,
        ]

        filename = f"{space_key}/{page_id}_{safe_filename(title)}.md"
        return self._write(filename, render_frontmatter(meta, "\n".join(lines)))

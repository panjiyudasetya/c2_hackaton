"""
Confluence collector — fetches every page in a set of spaces and writes one
markdown file each, tagged with YAML frontmatter (id/source/type/.../
explicit_links), matching the convention already used for GitHub/JIRA docs —
see collectors/base.py's render_frontmatter.

Credentials are read from environment variables only - never hardcode a
token in this file or paste one into a chat:

    CONFLUENCE_URL         e.g. https://your-org.atlassian.net  (no /wiki suffix)
    CONFLUENCE_USER        your Atlassian account email
    CONFLUENCE_API_TOKEN   an Atlassian API token (can reuse the JIRA one —
                            Jira and Confluence share Atlassian Cloud auth)
"""

from __future__ import annotations

import os
from pathlib import Path

from .base import BaseCollector, render_frontmatter, safe_filename


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
            # List page IDs quickly (no body), then fetch body per page so
            # progress updates after each page rather than after the whole batch.
            page_stubs = self._list_pages(confluence, space_key, max_pages)
            for n, stub in enumerate(page_stubs, start=1):
                created.append(self._write_page(confluence, stub, space_key))
                self._report(n, len(page_stubs), "Pages")
        return created

    def _list_pages(self, confluence, space_key: str, max_pages: int) -> list[dict]:
        """Return page stubs (id, title, version, history) via the v1 REST API.

        Using the v1 content endpoint with spaceKey directly — the v2 API
        requires a numeric space ID, which would need an extra lookup.
        """
        pages: list[dict] = []
        start = 0
        batch_size = 50
        while len(pages) < max_pages:
            result = confluence.get(
                "wiki/rest/api/content",
                params={
                    "spaceKey": space_key,
                    "type": "page",
                    "start": start,
                    "limit": min(batch_size, max_pages - len(pages)),
                    "expand": "version,history",
                },
            )
            batch = result.get("results", []) if isinstance(result, dict) else []
            if not batch:
                break
            pages.extend(batch)
            if len(batch) < batch_size:
                break
            start += len(batch)
        return pages

    def _write_page(self, confluence, stub: dict, space_key: str) -> Path:
        from markdownify import markdownify as md

        page_id = stub["id"]
        title = stub.get("title", "Untitled")
        # Use the env var as base — confluence.url may already have /wiki appended.
        base_url = os.environ["CONFLUENCE_URL"].rstrip("/")
        url = f"{base_url}/wiki/spaces/{space_key}/pages/{page_id}"

        # Fetch body separately — keeps listing fast and progress responsive.
        full = confluence.get(
            f"wiki/rest/api/content/{page_id}",
            params={"expand": "body.storage"},
        )
        html_content = (full.get("body") or {}).get("storage", {}).get("value", "")
        body = md(html_content, heading_style="ATX").strip() if html_content else ""

        version = stub.get("version") or {}
        author = ((version.get("by") or {}).get("displayName") or
                  (stub.get("history", {}).get("createdBy", {}).get("displayName", "")))
        date = version.get("when") or stub.get("history", {}).get("createdDate", "")

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

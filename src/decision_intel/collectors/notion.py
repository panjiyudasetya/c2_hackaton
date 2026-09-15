"""
Notion collector — fetches pages from a database or page tree and writes
them as markdown, tagged with YAML frontmatter (id/source/type/.../
explicit_links), matching the convention already used for GitHub/JIRA/
Confluence docs — see collectors/base.py's render_frontmatter.
"""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any

from .base import BaseCollector, render_frontmatter


def _safe_filename(text: str) -> str:
    return re.sub(r"[^\w\-]", "_", text).strip("_")[:80]


def _extract_rich_text(rich_texts: list[dict]) -> str:
    return "".join(rt.get("plain_text", "") for rt in (rich_texts or []))


def _page_title(page: dict) -> str:
    """
    Extract the title from a page's properties.
    """
    props = page.get("properties", {})
    for prop in props.values():
        if prop.get("type") == "title":
            return _extract_rich_text(prop.get("title", []))
    return page.get("id", "untitled")


def _blocks_to_markdown(blocks: list[dict]) -> str:
    """
    Convert a flat list of Notion blocks to markdown text.
    """
    lines: list[str] = []
    for block in blocks:
        btype = block.get("type", "")
        data = block.get(btype, {})

        if btype in ("paragraph", "quote"):
            text = _extract_rich_text(data.get("rich_text", []))
            prefix = "> " if btype == "quote" else ""
            lines.append(f"{prefix}{text}")

        elif btype in ("heading_1", "heading_2", "heading_3"):
            level = int(btype[-1])
            text = _extract_rich_text(data.get("rich_text", []))
            lines.append(f"{'#' * level} {text}")

        elif btype == "bulleted_list_item":
            text = _extract_rich_text(data.get("rich_text", []))
            lines.append(f"- {text}")

        elif btype == "numbered_list_item":
            text = _extract_rich_text(data.get("rich_text", []))
            lines.append(f"1. {text}")

        elif btype == "to_do":
            done = data.get("checked", False)
            text = _extract_rich_text(data.get("rich_text", []))
            lines.append(f"- [{'x' if done else ' '}] {text}")

        elif btype == "code":
            lang = data.get("language", "")
            text = _extract_rich_text(data.get("rich_text", []))
            lines += [f"```{lang}", text, "```"]

        elif btype == "divider":
            lines.append("---")

        elif btype == "callout":
            text = _extract_rich_text(data.get("rich_text", []))
            lines.append(f"> **Note:** {text}")

        elif btype == "table_of_contents":
            pass  # skip ToC blocks

        else:
            # fallback: try to extract any rich_text present
            text = _extract_rich_text(data.get("rich_text", []))
            if text:
                lines.append(text)

        lines.append("")  # blank line after each block

    return "\n".join(lines)


def _prop_to_str(prop: dict) -> str:
    """
    Convert a Notion property value to a plain string.
    """
    ptype = prop.get("type", "")
    val = prop.get(ptype, None)

    if val is None:
        return ""
    if ptype == "title":
        return _extract_rich_text(val)
    if ptype == "rich_text":
        return _extract_rich_text(val)
    if ptype == "number":
        return str(val) if val is not None else ""
    if ptype == "select":
        return (val or {}).get("name", "")
    if ptype == "multi_select":
        return ", ".join(o.get("name", "") for o in (val or []))
    if ptype == "status":
        return (val or {}).get("name", "")
    if ptype == "date":
        start = (val or {}).get("start", "")
        end = (val or {}).get("end", "")
        return f"{start} → {end}" if end else start
    if ptype == "checkbox":
        return "Yes" if val else "No"
    if ptype == "url":
        return val or ""
    if ptype == "email":
        return val or ""
    if ptype == "phone_number":
        return val or ""
    if ptype == "people":
        return ", ".join(
            p.get("name") or p.get("id", "") for p in (val or [])
        )
    if ptype == "relation":
        return ", ".join(r.get("id", "") for r in (val or []))
    if ptype == "formula":
        inner = val or {}
        ftype = inner.get("type", "")
        return str(inner.get(ftype, ""))
    if ptype in ("created_time", "last_edited_time"):
        return str(val)[:10] if val else ""
    if ptype in ("created_by", "last_edited_by"):
        return (val or {}).get("name") or (val or {}).get("id", "")
    return str(val)


class NotionCollector(BaseCollector):
    """Collects Notion pages from one or more database IDs and writes them as markdown."""

    def __init__(self, output_dir: Path) -> None:
        super().__init__(output_dir / "notion")

    def is_configured(self) -> bool:
        return bool(os.environ.get("NOTION_TOKEN"))

    def _client(self):
        from notion_client import Client  # lazy import

        return Client(auth=os.environ["NOTION_TOKEN"])

    def collect(
        self,
        database_ids: list[str] | None = None,
        page_ids: list[str] | None = None,
        max_pages: int = 50,
        **kwargs,
    ) -> list[Path]:
        """
        Fetch pages from Notion databases and/or standalone pages.

        Args:
            database_ids: List of Notion database IDs to query.
            page_ids: List of standalone page IDs to fetch directly.
            max_pages: Max pages to fetch per database.
        """
        notion = self._client()
        created: list[Path] = []

        for db_id in (database_ids or []):
            db_dir = self.output_dir / _safe_filename(db_id)
            db_dir.mkdir(parents=True, exist_ok=True)
            pages = self._query_database(notion, db_id, max_pages)
            for page in pages:
                path = self._write_page(notion, page, db_dir, database_id=db_id)
                created.append(path)

        for page_id in (page_ids or []):
            page = notion.pages.retrieve(page_id=page_id)
            path = self._write_page(notion, page, self.output_dir)
            created.append(path)

        return created

    def _query_database(self, notion, database_id: str, max_pages: int) -> list[dict]:
        results: list[dict] = []
        cursor: str | None = None

        while len(results) < max_pages:
            params: dict[str, Any] = {
                "database_id": database_id,
                "page_size": min(100, max_pages - len(results)),
            }
            if cursor:
                params["start_cursor"] = cursor

            resp = notion.databases.query(**params)
            results.extend(resp.get("results", []))

            if not resp.get("has_more"):
                break
            cursor = resp.get("next_cursor")

        return results

    def _fetch_blocks(self, notion, block_id: str) -> list[dict]:
        """
        Fetch all top-level blocks for a page (no recursion into nested children).
        """
        blocks: list[dict] = []
        cursor: str | None = None

        while True:
            params: dict[str, Any] = {"block_id": block_id, "page_size": 100}
            if cursor:
                params["start_cursor"] = cursor

            resp = notion.blocks.children.list(**params)
            blocks.extend(resp.get("results", []))

            if not resp.get("has_more"):
                break
            cursor = resp.get("next_cursor")

        return blocks

    def _write_page(self, notion, page: dict, out_dir: Path, database_id: str | None = None) -> Path:
        page_id = page["id"]
        title = _page_title(page)
        url = page.get("url", "")
        created_at = (page.get("created_time") or "")[:10]
        updated_at = (page.get("last_edited_time") or "")[:10]
        props = page.get("properties", {})

        # No "author" field: the Notion API only exposes a `created_by` user
        # id on the page object, not a display name, without an extra
        # per-user API call.
        meta = {
            "id":             f"notion:{page_id}",
            "source":         "notion",
            "type":           "page",
            "database_id":    database_id,
            "title":          title,
            "date":           created_at,
            "updated_at":     updated_at,
            "url":            url,
            "explicit_links": [],
        }

        lines: list[str] = [
            f"# {title}",
            "",
            f"**URL:** {url}  ",
            f"**Created:** {created_at} | **Last edited:** {updated_at}  ",
            "",
        ]

        # Properties table (skip title — already in heading)
        non_title = {k: v for k, v in props.items() if v.get("type") != "title"}
        if non_title:
            lines += ["## Properties", "", "| Property | Value |", "| --- | --- |"]
            for name, prop in non_title.items():
                value = _prop_to_str(prop)
                if value:
                    lines.append(f"| {name} | {value} |")
            lines.append("")

        # Page content
        try:
            blocks = self._fetch_blocks(notion, page_id)
            if blocks:
                lines += ["## Content", "", _blocks_to_markdown(blocks)]
        except Exception:
            lines.append("_Content could not be fetched._\n")

        filename = f"{_safe_filename(title or page_id)}.md"
        path = out_dir / filename
        path.write_text(render_frontmatter(meta, "\n".join(lines)), encoding="utf-8")
        return path

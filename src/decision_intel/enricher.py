"""
Phase 2 — Link extraction and frontmatter enrichment.

Scans every collected markdown file for cross-source references
(JIRA keys, GitHub URLs, Confluence URLs, Notion URLs) and writes
them into the ``explicit_links`` frontmatter field.
"""

from __future__ import annotations

import re
from pathlib import Path

from .collectors.base import parse_frontmatter, render_frontmatter

# ── patterns ──────────────────────────────────────────────────────────────────

_JIRA_KEY   = re.compile(r"\b([A-Z]{2,10}-\d+)\b")
_GH_PR      = re.compile(r"github\.com/([\w\-\.]+/[\w\-\.]+)/pull/(\d+)")
_GH_ISSUE   = re.compile(r"github\.com/([\w\-\.]+/[\w\-\.]+)/issues/(\d+)")
_CONFLUENCE = re.compile(
    r"https?://[\w\-]+\.atlassian\.net/wiki/spaces/[\w/\-\+\.%]+"
    r"(?:/pages/(\d+))?[^\s\)\"\'<>]*"
)
_NOTION = re.compile(
    r"https?://(?:www\.)?notion\.so/"
    r"(?:[\w\-]+/)?"                  # optional workspace slug
    r"([a-f0-9]{32}|[a-f0-9\-]{36})" # page id
    r"[^\s\)\"\'<>]*"
)


def extract_links(text: str) -> list[str]:
    """Return deduplicated list of cross-source reference IDs found in *text*."""
    links: list[str] = []

    for m in _JIRA_KEY.finditer(text):
        links.append(f"jira:{m.group(1)}")

    for m in _GH_PR.finditer(text):
        links.append(f"github:{m.group(1)}:pr:{m.group(2)}")

    for m in _GH_ISSUE.finditer(text):
        links.append(f"github:{m.group(1)}:issue:{m.group(2)}")

    for m in _CONFLUENCE.finditer(text):
        page_id = m.group(1)
        ref = f"confluence:{page_id}" if page_id else f"confluence:{m.group(0).rstrip('.,;:')}"
        links.append(ref)

    for m in _NOTION.finditer(text):
        links.append(f"notion:{m.group(1)}")

    return list(dict.fromkeys(links))  # deduplicate, preserve order


# ── per-file enrichment ────────────────────────────────────────────────────────

def enrich_file(path: Path) -> int:
    """
    Re-read *path*, extract cross-source links, update ``explicit_links``
    in the frontmatter, and write the file back in place.

    Returns the number of new links added.
    """
    content = path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(content)

    if not meta:
        # File has no frontmatter — assign a fallback id and skip link enrichment
        meta = {
            "id": f"file:{path.stem}",
            "source": "unknown",
            "explicit_links": [],
        }
        path.write_text(render_frontmatter(meta, body), encoding="utf-8")
        return 0

    existing: list[str] = meta.get("explicit_links") or []
    # Also consider links already in linked_issues (set by github.py)
    existing += meta.get("linked_issues") or []

    found = extract_links(body)

    # Exclude self-references
    own_id: str = meta.get("id", "")
    found = [lnk for lnk in found if lnk != own_id and lnk not in existing]

    if found:
        meta["explicit_links"] = existing + found
        path.write_text(render_frontmatter(meta, body), encoding="utf-8")

    return len(found)


# ── bulk enrichment ────────────────────────────────────────────────────────────

def enrich_all(output_dir: Path) -> dict[str, int]:
    """
    Walk all ``.md`` files under *output_dir* and enrich each one.

    Returns a dict mapping file path → number of new links added.
    """
    results: dict[str, int] = {}
    for md_file in sorted(output_dir.rglob("*.md")):
        new_links = enrich_file(md_file)
        results[str(md_file)] = new_links
    return results

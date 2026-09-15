"""Phase 1 collector: pull every page from a Confluence space into
frontmatter-tagged markdown files (one file per page), so Phase 2/3/4 can
build the link graph and vector index on top of them.

Credentials are read from environment variables only - never hardcode a
token in this file or paste one into a chat:

    CONFLUENCE_DOMAIN     e.g. https://ofiniti.atlassian.net
    CONFLUENCE_EMAIL      your Atlassian account email
    CONFLUENCE_API_TOKEN  an Atlassian API token (id.atlassian.com/manage-profile/security/api-tokens)

Usage:
    python -m decision_intel.cli collect-confluence --space TC --out output/confluence
"""
from __future__ import annotations

import os
from typing import Iterator

import requests
from markdownify import markdownify as md
from requests.auth import HTTPBasicAuth

from ..models import Document
from ..frontmatter_utils import write_document
from .common import safe_filename, require_env

PAGE_SIZE = 50


def _client():
    domain = require_env("CONFLUENCE_DOMAIN").rstrip("/")
    email = require_env("CONFLUENCE_EMAIL")
    token = require_env("CONFLUENCE_API_TOKEN")
    auth = HTTPBasicAuth(email, token)
    headers = {"Accept": "application/json"}
    return domain, auth, headers


def _iter_pages(space_key: str) -> Iterator[dict]:
    """Yield every page in a space, following pagination (the original
    script only ever fetched the first 50 results)."""
    domain, auth, headers = _client()
    url = f"{domain}/wiki/rest/api/content/search"
    params = {
        "cql": f'space="{space_key}" and type="page"',
        "expand": "body.storage,history,version",
        "limit": PAGE_SIZE,
        "start": 0,
    }

    while True:
        response = requests.get(url, headers=headers, auth=auth, params=params, timeout=30)
        if response.status_code != 200:
            raise RuntimeError(
                f"Confluence API error {response.status_code}: {response.text}"
            )
        data = response.json()
        results = data.get("results", [])
        if not results:
            return
        yield from results

        # cursor-based `_links.next` when present, else fall back to start offset
        next_link = data.get("_links", {}).get("next")
        if next_link:
            params = None
            url = domain + next_link if next_link.startswith("/") else next_link
        else:
            size = data.get("size", len(results))
            if size < PAGE_SIZE:
                return
            params["start"] += PAGE_SIZE


def collect(space_key: str, out_dir: str) -> list[str]:
    """Fetch every page in `space_key`, write one .md file per page under
    `out_dir`, return the list of file paths written."""
    domain, _, _ = _client()
    written: list[str] = []

    print(f"Mencari halaman di Space: {space_key}...")
    count = 0
    for page in _iter_pages(space_key):
        count += 1
        page_id = page.get("id")
        title = page.get("title", "Untitled")
        page_url = f"{domain}/wiki/spaces/{space_key}/pages/{page_id}"

        html_content = page.get("body", {}).get("storage", {}).get("value", "")
        body = md(html_content, heading_style="ATX").strip()

        version = page.get("version", {}) or {}
        author = (version.get("by") or {}).get("displayName", "") or (
            page.get("history", {}).get("createdBy", {}).get("displayName", "")
        )
        date = version.get("when", "") or page.get("history", {}).get("createdDate", "")

        doc = Document(
            doc_id=f"confluence:{page_id}",
            source="confluence",
            type="page",
            title=title,
            url=page_url,
            author=author,
            date=date[:10] if date else "",
            status="",
            explicit_links=[],
            extra={"space": space_key},
            body=body,
        )
        filename = f"{page_id}_{safe_filename(title)}.md"
        path = os.path.join(out_dir, filename)
        write_document(path, doc)
        written.append(path)
        print(f"OK: {path}")

    if count == 0:
        print("Tidak ada halaman ditemukan - cek Space Key.")
    else:
        print(f"Selesai. {count} halaman disimpan di '{out_dir}'.")
    return written

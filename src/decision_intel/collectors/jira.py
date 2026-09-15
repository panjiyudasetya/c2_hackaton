"""Phase 1 collector: pull every card (and its subtasks) from a set of Jira
boards into frontmatter-tagged markdown files - one file per issue - so
Phase 2/3/4 can build the link graph and vector index on top of them.

Credentials are read from environment variables only - never hardcode a
token in this file or paste one into a chat:

    JIRA_SERVER      e.g. https://ofiniti.atlassian.net
    JIRA_EMAIL       your Atlassian account email
    JIRA_API_TOKEN   an Atlassian API token

Usage:
    python -m decision_intel.cli collect-jira --boards PTO TCC --out output/jira
"""
from __future__ import annotations

import os
from typing import Any

from jira import JIRA

from ..models import Document
from ..frontmatter_utils import write_document
from .common import safe_filename, require_env


def _client() -> JIRA:
    server = require_env("JIRA_SERVER").rstrip("/")
    email = require_env("JIRA_EMAIL")
    token = require_env("JIRA_API_TOKEN")
    return JIRA(options={"server": server}, basic_auth=(email, token))


def _issue_links(fields: dict) -> list[tuple[str, str, str]]:
    """Return (related_key, related_summary, relation_label) for every
    issuelink on a raw fields dict."""
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


def _find_boards(jira: JIRA, target_names: list[str]) -> list[Any]:
    boards, start_at = [], 0
    while True:
        page = jira.boards(startAt=start_at, maxResults=50)
        if not page:
            break
        for board in page:
            name = getattr(board, "name", board.raw.get("name", "Unnamed"))
            if any(t.lower() in name.lower() for t in target_names):
                boards.append(board)
        start_at += 50
    return boards


def _board_issues(jira: JIRA, board_id: int) -> list[dict]:
    server = jira._options["server"]
    issues, start_at = [], 0
    while True:
        url = f"{server}/rest/agile/1.0/board/{board_id}/issue?startAt={start_at}&maxResults=50"
        response = jira._session.get(url)
        if response.status_code != 200:
            print(f"  gagal menarik issue board {board_id}: status {response.status_code}")
            break
        page = response.json().get("issues", [])
        if not page:
            break
        issues.extend(page)
        start_at += 50
    return issues


def _issue_to_document(key: str, fields: dict, board_name: str) -> Document:
    server = os.environ["JIRA_SERVER"].rstrip("/")
    summary = fields.get("summary", "Tanpa Judul")
    status = fields.get("status", {}).get("name", "Unknown")
    assignee = (fields.get("assignee") or {}).get("displayName", "Unassigned")
    reporter = (fields.get("reporter") or {}).get("displayName", assignee)
    issuetype = fields.get("issuetype", {}).get("name", "Unknown")
    is_subtask = bool(fields.get("issuetype", {}).get("subtask"))
    created = (fields.get("created") or "")[:10]
    description = fields.get("description") or ""
    if isinstance(description, dict):
        # Jira Cloud can return Atlassian Document Format; keep it simple for
        # a hackathon build and just note that richer ADF rendering is a
        # follow-up rather than silently dropping the field.
        description = "*(rich-text description - render via ADF if needed)*"

    links = _issue_links(fields)
    explicit_links = [f"jira:{k}" for k, _, _ in links]

    parent = fields.get("parent")
    if parent:
        explicit_links.append(f"jira:{parent['key']}")

    body_lines = [f"# [{key}] {summary}", ""]
    body_lines.append(f"- Tipe: {issuetype}")
    body_lines.append(f"- Status: {status}")
    body_lines.append(f"- Assignee: {assignee}")
    body_lines.append(f"- Reporter: {reporter}")
    body_lines.append(f"- Board: {board_name}")
    if parent:
        body_lines.append(f"- Parent: [{parent['key']}] {parent['fields'].get('summary', '')}")
    body_lines.append("")
    if description:
        body_lines.append("## Description")
        body_lines.append(description)
        body_lines.append("")

    if links:
        body_lines.append("## Terhubung dengan card lain")
        for rel_key, rel_summary, label in links:
            body_lines.append(f"- {label}: [{rel_key}] {rel_summary}")
        body_lines.append("")

    subtasks = fields.get("subtasks") or []
    if subtasks:
        body_lines.append("## Subtasks")
        for sub in subtasks:
            sub_fields = sub.get("fields", {})
            body_lines.append(
                f"- [{sub['key']}] {sub_fields.get('summary', '')} "
                f"({sub_fields.get('status', {}).get('name', 'Unknown')})"
            )
        body_lines.append("")

    return Document(
        doc_id=f"jira:{key}",
        source="jira",
        type="subtask" if is_subtask else "issue",
        title=summary,
        url=f"{server}/browse/{key}",
        author=reporter,
        date=created,
        status=status,
        explicit_links=explicit_links,
        extra={"board": board_name, "assignee": assignee, "issuetype": issuetype},
        body="\n".join(body_lines),
    )


def collect(board_names: list[str], out_dir: str) -> list[str]:
    print("Menghubungkan ke Jira...")
    jira = _client()
    written: list[str] = []

    print(f"Mencari board target: {board_names}...")
    boards = _find_boards(jira, board_names)
    print(f"Ditemukan {len(boards)} board.\n")

    for board in boards:
        board_id = getattr(board, "id", board.raw.get("id"))
        board_name = getattr(board, "name", board.raw.get("name", "Unnamed"))
        print(f"Memproses board: {board_name} (ID: {board_id})...")

        raw_issues = _board_issues(jira, board_id)
        parents = [i for i in raw_issues if not i["fields"]["issuetype"]["subtask"]]

        for issue in parents:
            key = issue["key"]
            fields = issue["fields"]
            doc = _issue_to_document(key, fields, board_name)
            path = os.path.join(out_dir, f"{safe_filename(key)}.md")
            write_document(path, doc)
            written.append(path)
            print(f"  OK: {path}")

            for sub_ref in fields.get("subtasks") or []:
                sub_key = sub_ref["key"]
                try:
                    sub_issue = jira.issue(sub_key)
                    sub_fields = sub_issue.raw.get("fields", {})
                except Exception as exc:  # noqa: BLE001 - keep collecting other issues
                    print(f"  gagal memuat subtask {sub_key}: {exc}")
                    continue
                sub_doc = _issue_to_document(sub_key, sub_fields, board_name)
                sub_path = os.path.join(out_dir, f"{safe_filename(sub_key)}.md")
                write_document(sub_path, sub_doc)
                written.append(sub_path)
                print(f"  OK: {sub_path}")

    print(f"\nSelesai. {len(written)} file disimpan di '{out_dir}'.")
    return written

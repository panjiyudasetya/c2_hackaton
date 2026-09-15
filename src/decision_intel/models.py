"""Shared document model used by the "Phase 1" collectors.

Every collector that wants frontmatter-tagged markdown output (Confluence,
Jira, and — going forward — GitHub) normalizes what it fetches into one of
these, then hands it to ``frontmatter_utils.write_document``. That keeps the
tag block on every generated .md file consistent across sources, e.g.:

    ---
    id: github:teqplay/dataflow_dag_core:pr:726
    source: github
    type: pull_request
    repo: teqplay/dataflow_dag_core
    number: 726
    title: PTO-2839 Promotes `visit_id` as primary key in `ods_port_visit`
    author: panjiyudasetya
    state: closed
    date: '2026-07-17'
    merged_at: '2026-07-22'
    base_branch: develop
    head_branch: chore/set-visit-id-as-pk
    url: https://github.com/teqplay/dataflow_dag_core/pull/726
    labels: []
    linked_issues: []
    explicit_links: []
    ---

See ``frontmatter_utils.py`` for how a Document turns into that block.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Document:
    doc_id: str
    """Globally unique tag id, e.g. ``confluence:98339`` or ``jira:PTO-3028``."""

    source: str
    """Where this came from: ``confluence`` | ``jira`` | ``github`` | ``notion``."""

    type: str
    """What kind of thing this is: ``page`` | ``issue`` | ``subtask`` |
    ``pull_request`` | ``issue_ticket`` ..."""

    title: str
    url: str

    author: str = ""
    date: str = ""
    status: str = ""

    explicit_links: list[str] = field(default_factory=list)
    """Other doc_ids this document explicitly references (parent issues,
    linked issues, etc.) — used later to build the cross-source link graph."""

    extra: dict[str, Any] = field(default_factory=dict)
    """Source-specific tag fields (e.g. ``space`` for Confluence, or
    ``board``/``assignee``/``issuetype`` for Jira). Flattened straight into
    the frontmatter block, right after id/source/type."""

    body: str = ""
    """Markdown body written below the frontmatter block."""

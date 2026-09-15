---
id: github:teqplay/dataflow_dag_core:pr:741
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 741
title: Chore - Clean up `CLAUDE.md` and remove unused `.augment` rule files
author: panjiyudasetya
state: closed
date: '2026-08-18'
merged_at: '2026-08-18'
base_branch: develop
head_branch: chore/add-dataplatform-domain
url: https://github.com/teqplay/dataflow_dag_core/pull/741
labels: []
linked_issues: []
explicit_links: []
---
# PR #741: Chore - Clean up `CLAUDE.md` and remove unused `.augment` rule files

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/741  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `develop` ← `chore/add-dataplatform-domain`  
**Created:** 2026-08-18  
**Merged:** 2026-08-18  

## Description

### Description
- Removed all 7 unused `.augment/rules/*.md` files — legacy config from the Augment AI tool, now fully superseded by `CLAUDE.md` as the single source of coding conventions for this repo.
- Updated `CLAUDE.md`: added a `conventions-review domain: data` tag, and expanded the SQL formatting rule to explicitly spell out keyword casing (uppercase `SELECT`, `FROM`, etc.) vs. identifier/literal/type casing (lowercase snake_case, `true`/`false`/`null`, `integer`/`text`/etc.).

### Why
Two separate AI-assistant configs (`.augment/` and `CLAUDE.md`) were coexisting and had drifted — the `.augment` rules were stale duplicates. Consolidating onto `CLAUDE.md` avoids conflicting guidance for anyone (human or AI) working in this repo.

### Changes
| File | Change |
|---|---|
| `.augment/rules/*.md` (7 files) | Deleted — 1,733 lines removed |
| `CLAUDE.md` | +5/-2 — domain tag added, SQL casing rule clarified with examples |

### Impact
Documentation-only change; no code, DAG, or SQL template behavior affected.

### Test plan
- [ ] N/A — no runtime code touched.


## Commits

- `4600ee65` **Panji Y. Wiwaha** (2026-08-18): docs: clarify SQL formatting rules and add domain tag
  Adds conventions-review domain tag and expands SQL keyword/identifier
  casing rule with concrete examples for keywords, literals, and types.
- `9e8a7f0f` **Panji Y. Wiwaha** (2026-08-18): chore: remove leftover .augment rule files
  These were leftover config from the Augment AI tool, superseded by
  CLAUDE.md as the single source of guidance for this repo.

## Reviews

### augmentcode[bot] — COMMENTED (2026-08-18)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### ryan-kharisma — APPROVED (2026-08-18)

LGTM

## Comments

---
id: github:teqplay/dataflow_dag_core:pr:757
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 757
title: 'fix(sof): Remove %(...)s patterns from SQL comments to prevent psycopg2 KeyError'
author: panjiyudasetya
state: closed
date: '2026-09-04'
merged_at: '2026-09-04'
base_branch: develop
head_branch: fix/streaming-ods
url: https://github.com/teqplay/dataflow_dag_core/pull/757
labels: []
linked_issues: []
explicit_links: []
---
# PR #757: fix(sof): Remove %(...)s patterns from SQL comments to prevent psycopg2 KeyError

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/757  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `develop` ← `fix/streaming-ods`  
**Created:** 2026-09-04  
**Merged:** 2026-09-04  

## Description

### Description
`psycopg2` scans the entire SQL string for %(key)s placeholders, including inside -- comments. `%(requires_*)s` and `%(name)s` were not in the params dict passed to validate_metadata, causing `KeyError` at runtime.

## Commits

- `5e50f2c1` **Panji Y. Wiwaha** (2026-09-04): fix(sof): remove %(...)s patterns from SQL comments to prevent psycopg2 KeyError
  psycopg2 scans the entire SQL string for %(key)s placeholders, including
  inside -- comments. %(requires_*)s and %(name)s were not in the params dict
  passed to validate_metadata, causing KeyError at runtime.

## Reviews

### augmentcode[bot] — COMMENTED (2026-09-04)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-04)

### 🟢 Approval recommended

The change is limited to comment text and directly addresses the reported `psycopg2` placeholder-scanning failure without affecting query behavior.

<details>
<summary>Pull request overview</summary>

This PR updates the SOF metadata validation SQL template to avoid `psycopg2` interpreting placeholder-like patterns inside `--` comments as real `%(key)s` parameters, which previously caused runtime `KeyError` when those keys were not present in the params dict.

**Changes:**
- Removed `%(requires_*)s` placeholder-like text from a comment to prevent `psycopg2` placeholder scanning from tripping on a non-existent key.
- Removed `%(name)s::boolean` placeholder-like text from a comment while retaining the explanatory note about `::boolean` casts and sqlfluff parsing.
</details>

<details>
<summary>File summaries</summary>

| File | Description |
| ---- | ----------- |
| teqplay/templates/sql/dml/processing_queue/sof_validate_metadata.sql | Rewords SQL comments to remove placeholder-like `%(...)s` patterns that can be mistakenly parsed by `psycopg2`. |
</details>

<details>
<summary>Review details</summary>

- **Files reviewed:** 1/1 changed files
- **Comments generated:** 0
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/dataflow_dag_core/new/develop?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

### ryan-kharisma — APPROVED (2026-09-04)

LGTM

## Comments

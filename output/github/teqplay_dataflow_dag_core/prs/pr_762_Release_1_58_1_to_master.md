---
id: github:teqplay/dataflow_dag_core:pr:762
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 762
title: Release 1.58.1 to master
author: panjiyudasetya
state: closed
date: '2026-09-07'
merged_at: '2026-09-07'
base_branch: master
head_branch: hotfix/1.58.1
url: https://github.com/teqplay/dataflow_dag_core/pull/762
labels: []
linked_issues: []
explicit_links: []
---
# PR #762: Release 1.58.1 to master

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/762  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `master` ← `hotfix/1.58.1`  
**Created:** 2026-09-07  
**Merged:** 2026-09-07  

## Description


## [1.58.1] - 2026-09-07
### Fixed
- Fix RabbitMQ connection resets on `staging_sof` stream DAGs (#758)

## Commits

- `bba36fd8` **Panji Y. Wiwaha** (2026-09-07): Bump version 1.58.1

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-07)

### 🟢 Approval recommended

The changes are limited to a version bump and a correctly formatted changelog entry consistent with the stated release contents.

<details>
<summary>Pull request overview</summary>

Prepares the `master` branch for the 1.58.1 release by bumping the package version and documenting the included fix (RabbitMQ connection reset mitigation for `staging_sof` stream DAGs, per #758).

**Changes:**
- Bump `teqplay` package version from `1.58.0` to `1.58.1`.
- Add a `1.58.1` changelog entry dated `2026-09-07` noting the RabbitMQ connection reset fix for `staging_sof` stream DAGs (#758).
</details>

<details>
<summary>File summaries</summary>

| File | Description |
| ---- | ----------- |
| `teqplay/__init__.py` | Updates the published package version constant to `1.58.1`. |
| `CHANGELOG.md` | Adds the `1.58.1` release notes entry documenting the fix shipped in this release. |
</details>

<details>
<summary>Review details</summary>

- **Files reviewed:** 2/2 changed files
- **Comments generated:** 0
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/dataflow_dag_core/new/master?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

### ryan-kharisma — APPROVED (2026-09-07)

LGTM

### augmentcode[bot] — COMMENTED (2026-09-07)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

## Comments

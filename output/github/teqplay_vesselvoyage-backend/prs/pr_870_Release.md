---
id: github:teqplay/vesselvoyage-backend:pr:870
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 870
title: Release
author: TeqJoostD
state: closed
date: '2026-09-03'
merged_at: '2026-09-03'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/870
labels: []
linked_issues: []
explicit_links: []
---
# PR #870: Release

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/870  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `master` ← `develop`  
**Created:** 2026-09-03  
**Merged:** 2026-09-03  

## Description

_No description._

## Commits

- `29f250d8` **Jamie de Leest** (2026-09-02): ci: add id-token/contents permissions for reusable workflow jobs
- `89c6a427` **Jamie de Leest** (2026-09-02): ci: add id-token/contents permissions for reusable workflow jobs
- `cbff7598` **Joost Dambrink** (2026-09-03): Merge pull request #869 from teqplay/add-reusable-workflow-permissions
  ci: add id-token/contents permissions for reusable workflow jobs

## Reviews

### michel-teqplay — APPROVED (2026-09-03)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-03)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-03)

### 🟢 Approval recommended

The change is minimal and correctly scopes GitHub Actions permissions to enable OIDC while keeping repository access read-only.

<details>
<summary>Pull request overview</summary>

This PR updates the repository’s GitHub Actions workflows to explicitly set job-level `GITHUB_TOKEN` permissions, enabling OIDC token issuance (via `id-token: write`) while keeping repository content access read-only.

**Changes:**
- Add `permissions: id-token: write` and `contents: read` to the `main` workflow job.
- Add the same explicit permissions to the `coverage` workflow job.
</details>

<details>
<summary>File summaries</summary>

| File | Description |
| ---- | ----------- |
| .github/workflows/main.yml | Adds explicit job permissions to support OIDC-based auth while limiting repo access. |
| .github/workflows/coverage.yml | Adds explicit job permissions for the coverage workflow to support OIDC-based auth while limiting repo access. |
</details>

<details>
<summary>Review details</summary>

- **Files reviewed:** 2/2 changed files
- **Comments generated:** 0
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/vesselvoyage-backend/new/master?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

## Comments

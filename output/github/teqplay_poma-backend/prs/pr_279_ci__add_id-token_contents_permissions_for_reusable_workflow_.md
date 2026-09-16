---
id: github:teqplay/poma-backend:pr:279
source: github
type: pull_request
repo: teqplay/poma-backend
number: 279
title: 'ci: add id-token/contents permissions for reusable workflow jobs'
author: Jamie-de-Leest
state: closed
date: '2026-09-02'
merged_at: '2026-09-09'
base_branch: develop
head_branch: add-reusable-workflow-permissions
url: https://github.com/teqplay/poma-backend/pull/279
labels: []
linked_issues: []
explicit_links: []
---
# PR #279: ci: add id-token/contents permissions for reusable workflow jobs

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/279  
**State:** closed | **Author:** Jamie-de-Leest  
**Base ← Head:** `develop` ← `add-reusable-workflow-permissions`  
**Created:** 2026-09-02  
**Merged:** 2026-09-09  

## Description

Adds

```yaml
permissions:
  id-token: write
  contents: read
```

to jobs that call a reusable workflow from `teqplay/actions`.

## Commits

- `34638b5d` **Jamie de Leest** (2026-09-02): ci: add id-token/contents permissions for reusable workflow jobs

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-02)

### 🟢 Approval recommended

The change is minimal, scoped to CI permissions, and is correctly applied at the job level for a reusable-workflow invocation.

<details>
<summary>Pull request overview</summary>

Adds explicit `GITHUB_TOKEN` permissions to the reusable-workflow caller job so it can request an OIDC token (`id-token: write`) and read repository contents (`contents: read`) when invoking `teqplay/actions/.github/workflows/backend-poma.yml`.

**Changes:**
- Add job-level `permissions` for `id-token: write` and `contents: read` to the `main` reusable-workflow job.
</details>

<details>
<summary>File summaries</summary>

| File | Description |
| ---- | ----------- |
| .github/workflows/main.yml | Adds `permissions` to the reusable-workflow caller job to enable OIDC token minting and read-only repo access. |
</details>

<details>
<summary>Review details</summary>

- **Files reviewed:** 1/1 changed files
- **Comments generated:** 0
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/poma-backend/new/develop?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

### augmentcode[bot] — COMMENTED (2026-09-02)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### michel-teqplay — APPROVED (2026-09-09)

_No comment._

## Comments

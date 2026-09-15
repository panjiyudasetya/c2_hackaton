---
id: github:teqplay/dataflow_dag_core:pr:753
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 753
title: 'ci: add id-token/contents permissions for reusable workflow jobs'
author: Jamie-de-Leest
state: closed
date: '2026-09-02'
merged_at: '2026-09-03'
base_branch: develop
head_branch: add-reusable-workflow-permissions
url: https://github.com/teqplay/dataflow_dag_core/pull/753
labels: []
linked_issues: []
explicit_links: []
---
# PR #753: ci: add id-token/contents permissions for reusable workflow jobs

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/753  
**State:** closed | **Author:** Jamie-de-Leest  
**Base ← Head:** `develop` ← `add-reusable-workflow-permissions`  
**Created:** 2026-09-02  
**Merged:** 2026-09-03  

## Description

Adds

```yaml
permissions:
  id-token: write
  contents: read
```

to jobs that call a reusable workflow from `teqplay/actions`.

## Commits

- `a4dbf117` **Jamie de Leest** (2026-09-02): ci: add id-token/contents permissions for reusable workflow jobs

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-02)

### 🟢 Approval recommended

The permissions change is correctly scoped to the reusable-workflow caller job and is syntactically valid with no apparent side effects.

<details>
<summary>Pull request overview</summary>

This PR updates the GitHub Actions workflow that uploads the project SBOM so that the job invoking the reusable workflow from `teqplay/actions` has the explicit token permissions required for OIDC-based authentication and repository read access.

**Changes:**
- Adds job-level `permissions` (`id-token: write`, `contents: read`) to the reusable-workflow caller job in the SBOM upload workflow.
</details>

<details>
<summary>File summaries</summary>

| File | Description |
| ---- | ----------- |
| `.github/workflows/SBOM upload.yml` | Adds explicit `permissions` to the reusable-workflow job to enable OIDC token minting and read-only repo access. |
</details>

<details>
<summary>Review details</summary>

- **Files reviewed:** 1/1 changed files
- **Comments generated:** 0
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/dataflow_dag_core/new/develop?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

### augmentcode[bot] — COMMENTED (2026-09-02)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — APPROVED (2026-09-03)

_No comment._

## Comments

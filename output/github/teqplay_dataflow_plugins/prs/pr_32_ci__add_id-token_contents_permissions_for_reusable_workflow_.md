---
id: github:teqplay/dataflow_plugins:pr:32
source: github
type: pull_request
repo: teqplay/dataflow_plugins
number: 32
title: 'ci: add id-token/contents permissions for reusable workflow jobs'
author: Jamie-de-Leest
state: closed
date: '2026-09-02'
merged_at: '2026-09-03'
base_branch: develop
head_branch: add-reusable-workflow-permissions
url: https://github.com/teqplay/dataflow_plugins/pull/32
labels: []
linked_issues: []
explicit_links: []
---
# PR #32: ci: add id-token/contents permissions for reusable workflow jobs

**Repo:** teqplay/dataflow_plugins  
**URL:** https://github.com/teqplay/dataflow_plugins/pull/32  
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

- `0f351093` **Jamie de Leest** (2026-09-02): ci: add id-token/contents permissions for reusable workflow jobs

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-02)

### 🟢 Approval recommended

The change is minimal, correctly scoped to the calling job, and matches the stated intent to support reusable workflow execution with OIDC.

<details>
<summary>Pull request overview</summary>

Updates the SBOM upload GitHub Actions workflow to explicitly grant the minimal permissions required for jobs that invoke a reusable workflow (OIDC token minting and repository read access).

**Changes:**
- Add job-level `permissions` for the reusable-workflow caller job.
- Grant `id-token: write` and `contents: read` to support OIDC-based authentication and read-only repo access.
</details>

<details>
<summary>File summaries</summary>

| File | Description |
| ---- | ----------- |
| .github/workflows/SBOM upload.yml | Adds explicit job permissions needed to call the `teqplay/actions` reusable SBOM upload workflow. |
</details>

<details>
<summary>Review details</summary>

- **Files reviewed:** 1/1 changed files
- **Comments generated:** 0
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/dataflow_plugins/new/develop?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

### augmentcode[bot] — COMMENTED (2026-09-02)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — APPROVED (2026-09-03)

_No comment._

## Comments

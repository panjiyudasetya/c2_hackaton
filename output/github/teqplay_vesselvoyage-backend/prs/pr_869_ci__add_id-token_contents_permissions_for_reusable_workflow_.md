---
id: github:teqplay/vesselvoyage-backend:pr:869
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 869
title: 'ci: add id-token/contents permissions for reusable workflow jobs'
author: Jamie-de-Leest
state: closed
date: '2026-09-02'
merged_at: '2026-09-03'
base_branch: develop
head_branch: add-reusable-workflow-permissions
url: https://github.com/teqplay/vesselvoyage-backend/pull/869
labels: []
linked_issues: []
explicit_links: []
---
# PR #869: ci: add id-token/contents permissions for reusable workflow jobs

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/869  
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

- `29f250d8` **Jamie de Leest** (2026-09-02): ci: add id-token/contents permissions for reusable workflow jobs
- `89c6a427` **Jamie de Leest** (2026-09-02): ci: add id-token/contents permissions for reusable workflow jobs

## Reviews

### augmentcode[bot] — COMMENTED (2026-09-02)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F869%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-02)

### 🟢 Approval recommended

The change is minimal, correctly scoped to the reusable-workflow job, and introduces no functional or security regressions based on the workflow structure.

<details>
<summary>Pull request overview</summary>

Updates the repository’s CI configuration to explicitly grant OIDC token and read-only repository contents permissions to the reusable-workflow caller job, aligning with GitHub Actions permission scoping for jobs that `uses:` workflows from `teqplay/actions`.

**Changes:**
- Adds `permissions: { id-token: write, contents: read }` to the `coverage` job that invokes the reusable workflow.
</details>

<details>
<summary>File summaries</summary>

| File | Description |
| ---- | ----------- |
| .github/workflows/coverage.yml | Grants `id-token` and `contents` permissions to the reusable workflow caller job for OIDC/authenticated access while keeping contents read-only. |
</details>

<details>
<summary>Review details</summary>

- **Files reviewed:** 1/1 changed files
- **Comments generated:** 0
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/vesselvoyage-backend/new/develop?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

### TeqJoostD — APPROVED (2026-09-03)

_No comment._

## Review Comments

## Comments

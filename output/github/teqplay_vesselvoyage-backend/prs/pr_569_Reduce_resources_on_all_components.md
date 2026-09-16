---
id: github:teqplay/vesselvoyage-backend:pr:569
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 569
title: Reduce resources on all components
author: Darius-Wattimena
state: closed
date: '2025-07-15'
merged_at: '2025-07-15'
base_branch: develop
head_branch: resources
url: https://github.com/teqplay/vesselvoyage-backend/pull/569
labels: []
linked_issues: []
explicit_links: []
---
# PR #569: Reduce resources on all components

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/569  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `resources`  
**Created:** 2025-07-15  
**Merged:** 2025-07-15  

## Description

_No description._

## Commits

- `d4eef49a` **Darius Wattimena** (2025-07-15): Reduce resources on all components

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-15)

## Pull Request Overview

This PR reduces memory allocations across various Helm value files to lower resource usage.

- Removed the global default resource block
- Halved MongoDB memory in `values.yaml`
- Updated memory requests and limits for processing and API environments in their respective values files

### Reviewed Changes

Copilot reviewed 6 out of 6 changed files in this pull request and generated no comments.

<details>
<summary>Show a summary per file</summary>

| File                          | Description                                          |
| ----------------------------- | ---------------------------------------------------- |
| helm/values.yaml              | Removed global resource defaults and cut MongoDB memory from 8Gi to 4Gi |
| helm/values.processing-prod.yaml | Reduced memory from 10Gi to 6Gi for processing-prod |
| helm/values.processing-dev.yaml  | Reduced memory from 10Gi to 6Gi for processing-dev  |
| helm/values.processing-data.yaml | Added resource block and set memory to 4Gi         |
| helm/values.api-prod.yaml        | Added resource block and set memory to 2Gi         |
| helm/values.api-dev.yaml         | Added resource block and set memory to 2Gi         |
</details>



<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**helm/values.processing-prod.yaml:14**
* The resource definition for `memory: 6Gi` is duplicated across multiple values files; consider using a shared YAML anchor or a global default to centralize these settings and reduce duplication.
```
    memory: 6Gi
```
</details>

### TeqJoostD — APPROVED (2025-07-15)

_No comment._

---
id: github:teqplay/vesselvoyage-backend:pr:601
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 601
title: Fix last filtering
author: Darius-Wattimena
state: closed
date: '2025-09-03'
merged_at: '2025-09-03'
base_branch: develop
head_branch: fix-last-filtering
url: https://github.com/teqplay/vesselvoyage-backend/pull/601
labels: []
linked_issues: []
explicit_links: []
---
# PR #601: Fix last filtering

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/601  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `fix-last-filtering`  
**Created:** 2025-09-03  
**Merged:** 2025-09-03  

## Description

_No description._

## Commits

- `940e5019` **Darius Wattimena** (2025-09-02): Fix filtering not working correctly when doing a descending filter where the code expects ascending filtering
- `0653e233` **Darius Wattimena** (2025-09-02): ktlint
- `e45e8bbd` **Darius Wattimena** (2025-09-03): Made the list reversed to avoid an extra iteration

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-09-03)

## Pull Request Overview

This PR fixes last filtering functionality by introducing sorting awareness and proper handling of multiple ongoing visits. The changes ensure that when filtering visits/voyages, the system correctly identifies the "last" ongoing item based on chronological order rather than just position in the list.

Key changes:
- Modified base controller to return sort direction information alongside filtered data
- Updated filtering logic to sort by start time before applying last-item filtering
- Added conditional sorting to maintain proper order based on query type

### Reviewed Changes

Copilot reviewed 4 out of 4 changed files in this pull request and generated 3 comments.

| File | Description |
| ---- | ----------- |
| BaseApiV2Controller.kt | Changed return type to include sort direction flag and restructured control flow |
| ApiVoyageV2Controller.kt | Enhanced mapToApi method with sorting awareness and filtering controls |
| ApiVisitV2Controller.kt | Applied same filtering and sorting improvements as voyage controller |
| ApiStatementOfFactsV2Controller.kt | Updated filtering method to handle sort direction for statement of facts |

### TeqJoostD — APPROVED (2025-09-03)

_No comment._

## Review Comments

### Copilot — 2025-09-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/BaseApiV2Controller.kt`

The return statement at line 40 uses an awkward `true to if (end != null)` construct that creates a Pair with conditional logic embedded in the second element. This reduces readability and makes the code harder to maintain. Consider extracting the conditional logic into a separate variable before creating the Pair.

### Copilot — 2025-09-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageV2Controller.kt`

The list is sorted by start time on every call to mapToApi, which could be inefficient for large datasets. Consider if the data can be pre-sorted at the service layer or if sorting is only needed when filterMultipleOngoing is true.

### Copilot — 2025-09-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageV2Controller.kt`

When sortedAscending is false, the filteredData is sorted again by descending order, which creates an additional O(n log n) operation. Since the data was already sorted ascending at line 245, you could reverse the list instead of re-sorting for better performance.
```suggestion
                .asReversed()
```

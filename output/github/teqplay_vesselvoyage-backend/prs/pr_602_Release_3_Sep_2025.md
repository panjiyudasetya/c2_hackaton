---
id: github:teqplay/vesselvoyage-backend:pr:602
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 602
title: Release 3 Sep 2025
author: Darius-Wattimena
state: closed
date: '2025-09-03'
merged_at: '2025-09-03'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/602
labels: []
linked_issues: []
explicit_links: []
---
# PR #602: Release 3 Sep 2025

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/602  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2025-09-03  
**Merged:** 2025-09-03  

## Description

_No description._

## Commits

- `940e5019` **Darius Wattimena** (2025-09-02): Fix filtering not working correctly when doing a descending filter where the code expects ascending filtering
- `0653e233` **Darius Wattimena** (2025-09-02): ktlint
- `e45e8bbd` **Darius Wattimena** (2025-09-03): Made the list reversed to avoid an extra iteration
- `5769e2fc` **Darius Wattimena** (2025-09-03): Merge pull request #601 from teqplay/fix-last-filtering
  Fix last filtering

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-09-03)

## Pull Request Overview

This PR implements sorting functionality for vessel voyage and visit data endpoints. The changes modify the return type of the base API method to include sort direction information and update the filtering logic across multiple controllers to handle ascending and descending sort orders consistently.

- Modified base controller to return sort direction alongside data
- Updated filtering logic to handle both ascending and descending sort orders
- Applied consistent sorting behavior across voyage, visit, and statement of facts controllers

### Reviewed Changes

Copilot reviewed 4 out of 4 changed files in this pull request and generated 2 comments.

| File | Description |
| ---- | ----------- |
| BaseApiV2Controller.kt | Changed return type to include sort direction (Pair<Boolean, List<I>>) |
| ApiVoyageV2Controller.kt | Updated mapToApi method to support filtering and sorting parameters |
| ApiVisitV2Controller.kt | Updated mapToApi method with filtering and sorting capabilities |
| ApiStatementOfFactsV2Controller.kt | Modified filterIfMultipleOngoing to support sort direction parameter |

## Review Comments

### Copilot — 2025-09-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageV2Controller.kt`

The mapping operation is duplicated in both branches. Extract the mapping to avoid redundant code and improve maintainability by applying the sort operation before mapping once.
```suggestion
        val sorted = if (sortedAscending) {
            filteredData.sortedBy { visit -> visit.start.time }
        } else {
            filteredData.sortedByDescending { visit -> visit.start.time }
        }
        return sorted.map { mapper.toApi(it) }
```

### Copilot — 2025-09-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVisitV2Controller.kt`

The sorting logic is inconsistent between ApiVoyageV2Controller and ApiVisitV2Controller. ApiVoyageV2Controller sorts by start time before mapping, while ApiVisitV2Controller maps first then reverses. This inconsistency could lead to different behavior and makes the codebase harder to maintain.

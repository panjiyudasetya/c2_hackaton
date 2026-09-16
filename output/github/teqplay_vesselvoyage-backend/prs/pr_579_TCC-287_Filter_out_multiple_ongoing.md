---
id: github:teqplay/vesselvoyage-backend:pr:579
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 579
title: TCC-287 Filter out multiple ongoing
author: Darius-Wattimena
state: closed
date: '2025-07-28'
merged_at: '2025-07-28'
base_branch: develop
head_branch: TCC-287-fix-broken-visits
url: https://github.com/teqplay/vesselvoyage-backend/pull/579
labels: []
linked_issues: []
explicit_links: []
---
# PR #579: TCC-287 Filter out multiple ongoing

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/579  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-287-fix-broken-visits`  
**Created:** 2025-07-28  
**Merged:** 2025-07-28  

## Description

_No description._

## Commits

- `5538ffc5` **Darius Wattimena** (2025-07-28): Filter out multiple ongoing
- `622b0d91` **Darius Wattimena** (2025-07-28): Remove unneeded code

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-28)

## Pull Request Overview

This PR implements filtering logic to handle multiple ongoing entries by ensuring only the last ongoing item is included in API responses. The change addresses ticket TCC-287 and prevents multiple ongoing items from being returned through various API endpoints.

- Adds filtering logic to exclude multiple ongoing entries, keeping only the last one
- Updates mapping functions across multiple controllers to include explicit return types
- Implements consistent filtering behavior for voyages, visits, entries, and statement of facts

### Reviewed Changes

Copilot reviewed 4 out of 4 changed files in this pull request and generated 6 comments.

| File | Description |
| ---- | ----------- |
| ApiVoyageV2Controller.kt | Updates mapToApi functions with explicit return types and filtering logic for ongoing voyages |
| ApiVisitV2Controller.kt | Adds filtering logic to mapToApi function for ongoing visits |
| ApiStatementOfFactsV2Controller.kt | Introduces filterIfMultipleOngoing helper function and applies it to service calls |
| ApiEntryV2Controller.kt | Adds import for Entry model and implements filtering logic in mapToApi function |

### TeqJoostD — APPROVED (2025-07-28)

_No comment._

## Review Comments

### Copilot — 2025-07-28 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageV2Controller.kt`

Converting to mutable list and then calling dropLast(1).toList() is inefficient. Use this.dropLast(1) directly instead.
```suggestion
        val leftOverItems = this.dropLast(1)
```

### Copilot — 2025-07-28 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVisitV2Controller.kt`

Converting to mutable list and then calling dropLast(1).toList() is inefficient. Use this.dropLast(1) directly instead.
```suggestion
        val leftOverItems = this
            // Drop the last item we just took
            .dropLast(1)
```

### Copilot — 2025-07-28 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiStatementOfFactsV2Controller.kt`

Converting to mutable list and then calling dropLast(1).toList() is inefficient. Use this.dropLast(1) directly instead.
```suggestion
        val leftOverItems = this.dropLast(1)
```

### Copilot — 2025-07-28 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiEntryV2Controller.kt`

Converting to mutable list and then calling dropLast(1).toList() is inefficient. Use this.dropLast(1) directly instead.
```suggestion
        val leftOverItems = this
            // Drop the last item we just took
            .dropLast(1)
```

### Copilot — 2025-07-28 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageV2Controller.kt`

The filtering logic is duplicated across multiple controllers. Consider extracting this to a shared utility function to improve maintainability and reduce code duplication.

### Copilot — 2025-07-28 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiStatementOfFactsV2Controller.kt`

The function name 'filterIfMultipleOngoing' is misleading as it always filters, not just when there are multiple ongoing items. Consider renaming to 'filterOngoingExceptLast' or 'keepOnlyLastOngoing' for clarity.

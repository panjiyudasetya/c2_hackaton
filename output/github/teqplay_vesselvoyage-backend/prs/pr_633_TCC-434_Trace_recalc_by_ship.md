---
id: github:teqplay/vesselvoyage-backend:pr:633
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 633
title: TCC-434 Trace recalc by ship
author: Darius-Wattimena
state: closed
date: '2025-10-13'
merged_at: '2025-10-13'
base_branch: develop
head_branch: TCC-434-trace-recalc-by-ship
url: https://github.com/teqplay/vesselvoyage-backend/pull/633
labels: []
linked_issues: []
explicit_links: []
---
# PR #633: TCC-434 Trace recalc by ship

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/633  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-434-trace-recalc-by-ship`  
**Created:** 2025-10-13  
**Merged:** 2025-10-13  

## Description

Replaces the existing full recalc endpoint by one that can be called per IMO so things don't explode

## Commits

- `72215a14` **Darius Wattimena** (2025-10-08): Made it so we schedule trace recalculation per imo instead of all in 1 go

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-13)

## Pull Request Overview

This PR refactors the full trace recalculation functionality to operate on a per-IMO basis rather than processing all entries at once, preventing system overload during large-scale recalculation operations.

- Modified the trace recalculation endpoint to accept a set of IMO numbers instead of processing all entries
- Added asynchronous processing with progress logging for better monitoring of long-running operations
- Updated data access methods to filter by IMO for more targeted recalculation

### Reviewed Changes

Copilot reviewed 4 out of 4 changed files in this pull request and generated 2 comments.

| File | Description |
| ---- | ----------- |
| EntryV2Service.kt | Updated method to find finished entries filtered by IMO instead of all entries |
| PostProcessingService.kt | Added asynchronous processing and IMO-based filtering with progress logging |
| NewEntryDataSource.kt | Modified database query to filter by IMO and end date |
| ProcessingPostProcessingController.kt | Updated endpoint to accept IMO set as request body |

### michel-teqplay — APPROVED (2025-10-13)

_No comment._

## Review Comments

### Copilot — 2025-10-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt`

Using `thread` for background processing can lead to uncontrolled thread creation and potential resource exhaustion. Consider using a proper thread pool or Spring's `@Async` annotation with a configured executor to manage thread lifecycle and resource usage.
```suggestion
        executor.execute {
```

### Copilot — 2025-10-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingPostProcessingController.kt`

The endpoint accepts an empty set without validation. Consider adding validation to ensure the IMO set is not empty and contains valid IMO numbers to prevent unnecessary processing.

---
id: github:teqplay/vesselvoyage-backend:pr:634
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 634
title: Release 13 Oct 2025
author: Darius-Wattimena
state: closed
date: '2025-10-13'
merged_at: '2025-10-13'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/634
labels: []
linked_issues: []
explicit_links: []
---
# PR #634: Release 13 Oct 2025

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/634  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2025-10-13  
**Merged:** 2025-10-13  

## Description

_No description._

## Commits

- `72215a14` **Darius Wattimena** (2025-10-08): Made it so we schedule trace recalculation per imo instead of all in 1 go
- `03bc604a` **Jamie de Leest** (2025-10-09): feat: update ETA predictor models
- `4d7d585c` **jamie-teqplay** (2025-10-10): Merge pull request #631 from teqplay/TCC-474-Update-ETA-predictor-models
  feat: update ETA predictor models
- `ee020504` **Darius Wattimena** (2025-10-13): Implement batched post-processing so we always keep up-to-date with real-time entries
- `fdcace27` **Darius Wattimena** (2025-10-13): Update src/main/kotlin/nl/teqplay/vesselvoyage/datasource/PostProcessableDataSource.kt
  Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com>
- `82591baa` **Darius Wattimena** (2025-10-13): First sort before limiting
- `18ac9a34` **Darius Wattimena** (2025-10-13): Merge remote-tracking branch 'origin/TCC-434-batched-post-processing' into TCC-434-batched-post-processing
- `96cbb0e6` **Darius Wattimena** (2025-10-13): Merge pull request #632 from teqplay/TCC-434-batched-post-processing
  TCC-434 batched post-processing
- `fbe90a44` **Darius Wattimena** (2025-10-13): Merge pull request #633 from teqplay/TCC-434-trace-recalc-by-ship
  TCC-434 Trace recalc by ship

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-13)

## Pull Request Overview

This PR implements performance optimizations for post-processing operations by adding batch processing and IMO-specific filtering capabilities. The changes aim to improve system responsiveness by limiting the scope of operations and processing entries in manageable batches.

- Added batch processing with a maximum limit of 1000 entries per cycle to prevent system overload
- Modified trace recalculation to work with specific IMO sets instead of all entries
- Enhanced data source methods to support IMO-based filtering for finished entries

### Reviewed Changes

Copilot reviewed 5 out of 6 changed files in this pull request and generated 3 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| EntryV2Service.kt | Updated method to find finished IDs by specific IMO instead of all entries |
| PostProcessingService.kt | Added batch processing limits and IMO-specific trace recalculation with threading |
| PostProcessableDataSource.kt | Implemented batch retrieval with sorting and indexing optimizations |
| NewEntryDataSource.kt | Modified to filter finished entries by IMO in database queries |
| ProcessingPostProcessingController.kt | Updated API endpoint to accept IMO sets as request body |
</details>

## Review Comments

### Copilot — 2025-10-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt`

Using `kotlin.concurrent.thread` for background processing is not recommended in Spring applications. Consider using Spring's `@Async` annotation with a proper thread pool executor or injecting `TaskExecutor` for better resource management and monitoring.
```suggestion

```

### Copilot — 2025-10-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt`

The thread created here is not managed by Spring's application context and could lead to resource leaks or uncontrolled thread creation. Use Spring's async capabilities or a managed executor service instead.
```suggestion
        // Execute in a managed thread as this can take a while
        executor.execute {
```

### Copilot — 2025-10-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/PostProcessableDataSource.kt`

Creating indexes during application startup can impact startup time. Consider creating this index during database migration or initialization scripts instead of at runtime.
```suggestion

```

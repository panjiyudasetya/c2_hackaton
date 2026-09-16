---
id: github:teqplay/vesselvoyage-backend:pr:613
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 613
title: Release 22 Sep 2025
author: Darius-Wattimena
state: closed
date: '2025-09-22'
merged_at: '2025-09-22'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/613
labels: []
linked_issues: []
explicit_links: []
---
# PR #613: Release 22 Sep 2025

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/613  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2025-09-22  
**Merged:** 2025-09-22  

## Description

_No description._

## Commits

- `33b6c579` **Darius Wattimena** (2025-09-22): Add test for merging duplicate visits into a single visit
- `b8074ef1` **Darius Wattimena** (2025-09-22): Implement duplicate entry pruning in EntriesMergeService
- `9a28ce02` **Darius Wattimena** (2025-09-22): Merge pull request #612 from teqplay/fix-duplicate-entries
  Fix duplicate entries

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-09-22)

## Pull Request Overview

This PR adds deduplication functionality to the entries merge service to handle duplicate entries with identical start and end times during the merge process.

- Adds a new `pruneDuplicateNewEntries` function that removes duplicate entries based on start/end time pairs
- Integrates the deduplication logic into the main merge flow by calling it early in the process
- Includes comprehensive test coverage for the duplicate handling scenario

### Reviewed Changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated 2 comments.

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/merge/EntriesMergeService.kt | Adds deduplication logic with new function and integration into merge flow |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/merge/EntriesMergeV2ServiceTest.kt | Adds test case to verify duplicate entries are properly merged into a single visit |

## Review Comments

### Copilot — 2025-09-22 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/merge/EntriesMergeService.kt`

The function modifies the input parameter directly without indicating this in the function name or documentation. Consider renaming to `removeDuplicateNewEntries` or making it return a new list to follow immutable design patterns.
```suggestion
     * Returns a new list with duplicate entries removed from newEntries based on identical start and end times.
     * Only the first occurrence of each unique (start, end) pair is kept.
     */
    fun pruneDuplicateNewEntries(newEntries: List<Entry>): List<Entry> {
        val seenTimes = mutableSetOf<Pair<Instant, Instant?>>()
        return newEntries.filter { entry ->
            val timePair = entry.getStartTime() to entry.getEndTime()
            seenTimes.add(timePair)
```

### Copilot — 2025-09-22 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/merge/EntriesMergeService.kt`

[nitpick] Using a generic Pair for time comparison makes the code less readable. Consider creating a data class like `TimeRange(val start: Instant, val end: Instant?)` to improve code clarity and type safety.

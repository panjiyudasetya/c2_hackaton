---
id: github:teqplay/vesselvoyage-backend:pr:681
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 681
title: Release 10 Dec 2025
author: Darius-Wattimena
state: closed
date: '2025-12-09'
merged_at: '2025-12-10'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/681
labels: []
linked_issues: []
explicit_links: []
---
# PR #681: Release 10 Dec 2025

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/681  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2025-12-09  
**Merged:** 2025-12-10  

## Description

_No description._

## Commits

- `8ca94b91` **Darius Wattimena** (2025-12-09): Fix an issue where the port area activity would be filtered out in waters where a lot of EOSPs overlap
- `9e9d51ec` **Darius Wattimena** (2025-12-09): ktlint
- `a9904789` **Darius Wattimena** (2025-12-09): Fix so we don't put the Port ATA to an older time when we entered the port after the EOSP ATA
- `e5c0e270` **Darius Wattimena** (2025-12-09): Add test for updating port area activity start time on new confirmed visit
- `ed2b94bc` **Darius Wattimena** (2025-12-09): Cleaned up code and added some better comments why the changes need to be made
- `708d9574` **Darius Wattimena** (2025-12-09): Clarify comment on port activity time adjustment logic for overlapping EOSPs
- `a93199e9` **Darius Wattimena** (2025-12-09): Merge pull request #680 from teqplay/TCC-581-fix-special-case
  TCC-581 fix missing port ata
- `198e604e` **Darius Wattimena** (2025-12-09): Fix an issue where it was still possible to have a port ata outside of the visit time
- `254ad638` **Darius Wattimena** (2025-12-09): Update existing test to match new behaviour
- `8fc0e9ca` **Darius Wattimena** (2025-12-09): Refactor port area activity time correction logic so it is reused by both components
- `ebb9a485` **Darius Wattimena** (2025-12-09): Merge pull request #682 from teqplay/TCC-581-eosp-leaving-edge-case
  TCC-581 Fix EOSP leaving edge case

## Reviews

### michel-teqplay — APPROVED (2025-12-09)

_No comment._

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-12-09)

## Pull request overview

This release adds logic to synchronize port area activity start times with visit start times when switching between overlapping EOSP (End of Sea Passage) activities and confirming visits. The change ensures data consistency when a vessel's visit is reassigned to a different port that was entered earlier.

- Updates `StopBaseProcessor` to adjust port area activity start times when switching to a new confirmed visit
- Adds comprehensive test coverage for the new port area activity synchronization logic

### Reviewed changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated 1 comment.

| File | Description |
| ---- | ----------- |
| `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopBaseProcessor.kt` | Implements logic to find and update matching port area activities when switching visits, ensuring start times align with the new visit start time |
| `src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/EventProcessingServiceTest.kt` | Adds test case validating that port area activities are correctly reassigned and updated when switching to a new confirmed visit with overlapping EOSPs |

### github-actions[bot] — COMMENTED (2025-12-09)

Review completed. No suggestions at this time.

## Review Comments

### Copilot — 2025-12-09 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopBaseProcessor.kt`

The null check for `updatedPortActivity` is redundant. Since `updatedPortActivity` is defined as `matchingPortActivity?.copy(start = newVisitStart)`, if `matchingPortActivity` is not null, `updatedPortActivity` will also be not null (`.copy()` always returns a non-null value for non-null objects).

The condition can be simplified to:
```kotlin
portAreaActivities = if (matchingPortActivity != null) {
    currentVisit.portAreaActivities - matchingPortActivity + updatedPortActivity!!
} else {
    currentVisit.portAreaActivities
}
```

Or even better, use `let`:
```kotlin
portAreaActivities = matchingPortActivity?.let { matching ->
    currentVisit.portAreaActivities - matching + updatedPortActivity!!
} ?: currentVisit.portAreaActivities
```
```suggestion
                    portAreaActivities = matchingPortActivity?.let { matching ->
                        currentVisit.portAreaActivities - matching + updatedPortActivity!!
                    } ?: currentVisit.portAreaActivities,
```

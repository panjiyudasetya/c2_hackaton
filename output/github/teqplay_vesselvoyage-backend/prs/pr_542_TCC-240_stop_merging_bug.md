---
id: github:teqplay/vesselvoyage-backend:pr:542
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 542
title: TCC-240 stop merging bug
author: Darius-Wattimena
state: closed
date: '2025-06-24'
merged_at: '2025-06-25'
base_branch: develop
head_branch: TCC-240-splitting-error
url: https://github.com/teqplay/vesselvoyage-backend/pull/542
labels: []
linked_issues: []
explicit_links: []
---
# PR #542: TCC-240 stop merging bug

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/542  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-240-splitting-error`  
**Created:** 2025-06-24  
**Merged:** 2025-06-25  

## Description

_No description._

## Commits

- `426e13ce` **Darius Wattimena** (2025-06-24): Added extra test cases which ensure that the visits and voyages get correctly resumed and stops are correctly merged
- `9df68e8f` **Darius Wattimena** (2025-06-24): Adjusted logic to match correct behaviour
- `2d8d807b` **Darius Wattimena** (2025-06-24): Added endpoint to processing backend which can be used to fix broken stops
- `c16a417e` **Darius Wattimena** (2025-06-24): Added a way to track progression and put the call in a background thread

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-06-24)

## Pull Request Overview

This PR addresses the "TCC-240 stop merging bug" by updating the stop merging logic and adding comprehensive tests along with new processing service endpoints.  
- Replaces simple list concatenation for stops with the mergeStops function to correctly merge split stops.  
- Introduces new tests for resuming visits and voyages along with DSL helpers.  
- Adds a new ProcessingStopService and API endpoint to fix broken stops in batches.

### Reviewed Changes

Copilot reviewed 6 out of 6 changed files in this pull request and generated no comments.

<details>
<summary>Show a summary per file</summary>

| File                                                                 | Description                                                                    |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------|
| src/test/kotlin/nl/teqplay/vesselvoyage/util/EntryUtilsTest.kt       | Added tests for resumeVisit and resumeVoyage to validate merged stop behavior. |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/dsl/EntriesBuilder.kt | Added DSL infix function defaultWithTime for generating default LocationTime.    |
| src/main/kotlin/nl/teqplay/vesselvoyage/util/entryUtils.kt           | Replaced stop merging logic with mergeStops and introduced the mergeStops function. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/ProcessingStopService.kt | Introduced a service to log and fix broken stops.                             |
| src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt | Added batch processing for fixing stops using mergeStops.                      |
| src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingStopV2Controller.kt | Created API endpoint for triggering broken stops fix.                         |
</details>



<details>
<summary>Comments suppressed due to low confidence (2)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/util/entryUtils.kt:814**
* Consider adding inline documentation in mergeStops to clarify the assumptions behind grouping by startEventId and merging stops based on the first and last elements. This will help future maintainers understand why this approach is sufficient for restoring split stops.
```
        .groupBy { stop -> stop.startEventId }
```
**src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt:266**
* [nitpick] Consider clarifying the purpose of passing an empty list as currentStops to mergeStops in a code comment. This will make it clear that the intention is to only process and sort the existing stops when there are no new ones.
```
                val newStops = mergeStops(entry.stops, emptyList())
```
</details>

### TeqJoostD — DISMISSED (2025-06-24)

added 1 question, otherwise LGTM

### TeqJoostD — APPROVED (2025-06-25)

_No comment._

## Comments

### TeqJoostD — 2025-06-24

How long does this operation take? Is it usefull adding a progress counter? Or not needed

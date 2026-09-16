---
id: github:teqplay/vesselvoyage-backend:pr:526
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 526
title: TCC-147 remove in memory state
author: Darius-Wattimena
state: closed
date: '2025-06-04'
merged_at: '2025-06-11'
base_branch: develop
head_branch: TCC-147-remove-in-memory-state
url: https://github.com/teqplay/vesselvoyage-backend/pull/526
labels: []
linked_issues: []
explicit_links: []
---
# PR #526: TCC-147 remove in memory state

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/526  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-147-remove-in-memory-state`  
**Created:** 2025-06-04  
**Merged:** 2025-06-11  

## Description

_No description._

## Commits

- `c5b30412` **Darius Wattimena** (2025-06-04): Remove in-memory state management for V2 and deprecate V1 methods
- `f4b81302` **Darius Wattimena** (2025-06-04): ktlint

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-06-04)

## Pull Request Overview

This PR removes in-memory state management (and related metrics) across recalculation and ship status services and updates tests to match the new behavior.

- Eliminated `shipStatusService.removeStatus(…)` calls from both recalculation services
- Stripped out meter registry dependencies and metrics from `ProcessingShipStatusService`
- Adjusted tests to remove expectations on `removeStatus`, updated stubbed calls and verification counts

### Reviewed Changes

Copilot reviewed 10 out of 10 changed files in this pull request and generated 1 comment.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| ReventsRecalculationServiceTest.kt | Removed verification of `removeStatus` |
| ManualRecalculationServiceTest.kt | Dropped `removeStatus` calls and meter registry, added stubbing for `findLastByImo` |
| ShipStatusServiceTest.kt | Removed meter registry injection in setup |
| EntryServiceTest.kt | Removed meter registry from service instantiation |
| ReventsRecalculationService.kt | Deleted in-memory status removal after processing |
| ManualRecalculationService.kt | Deleted in-memory status removal before persist |
| ShipStatusService.kt | Deprecated and removed V1 in-memory methods, cleaned up API |
| ProcessingShipStatusService.kt | Removed metrics and deprecated state‐cache methods |
| EntryService.kt | Removed `getCurrentShipEntries` reliance on in-memory state |
| ApiShipStatusService.kt | Deprecated V1 overrides for state mutation methods |
</details>



<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/service/ShipStatusService.kt:2**
* [nitpick] This import appears unused after removing the old in-memory methods—consider deleting it to keep imports tidy.
```
import java.util.Collections
```
</details>

### TeqJoostD — DISMISSED (2025-06-04)

![image](https://github.com/user-attachments/assets/542a5938-26e4-43dd-80a4-b10b49d06255)

### leonjoosse — APPROVED (2025-06-10)

_No comment._

## Review Comments

### Copilot — 2025-06-04 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/ShipStatusService.kt`

Add a `replaceWith` in the `@Deprecated` annotation to guide callers toward the new API, e.g. `@Deprecated("Use getStatus(Int)", ReplaceWith("getStatus(imo.toInt())"))`.

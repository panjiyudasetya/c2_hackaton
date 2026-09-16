---
id: github:teqplay/vesselvoyage-backend:pr:510
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 510
title: SPV-2633 add support for revents merge-back system
author: TeqJoostD
state: closed
date: '2025-05-21'
merged_at: '2025-06-03'
base_branch: develop
head_branch: SPV-2633
url: https://github.com/teqplay/vesselvoyage-backend/pull/510
labels: []
linked_issues: []
explicit_links: []
---
# PR #510: SPV-2633 add support for revents merge-back system

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/510  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `SPV-2633`  
**Created:** 2025-05-21  
**Merged:** 2025-06-03  

## Description

_No description._

## Commits

- `b8ecc165` **TeqJoostD** (2025-05-21): feat: add support for revents merge-back system
- `28916705` **Joost Dambrink** (2025-05-22): Update src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationService.kt
  Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com>
- `183d70db` **TeqJoostD** (2025-05-22): feat: add unit-tests
  fix: remove unnecessary field in merge result
- `bf8ac450` **TeqJoostD** (2025-05-22): Merge remote-tracking branch 'origin/SPV-2633' into SPV-2633
- `e5eedfe9` **Joost Dambrink** (2025-05-26): Merge branch 'develop' into SPV-2633
- `4d681154` **TeqJoostD** (2025-05-26): Merge branch 'develop' into SPV-2633
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationService.kt
- `9fddf75b` **TeqJoostD** (2025-05-26): format
- `3f833ccb` **TeqJoostD** (2025-05-26): Trigger new workflow
- `575ca0d4` **TeqJoostD** (2025-05-26): fix: make sure multiple ship results are also included in merge search recalculation
  fix: add missing json subtype
- `ebff1e12` **TeqJoostD** (2025-05-26): fix: remove breaking annotation for ReventsRecalculationStatus
- `b6dca3d4` **TeqJoostD** (2025-05-26): fix: update merge status
- `5bc89500` **TeqJoostD** (2025-05-27): add error handling
- `8b3cd373` **TeqJoostD** (2025-05-27): fix tests
- `9a02c5bd` **TeqJoostD** (2025-05-27): fix tests
- `d0be9887` **TeqJoostD** (2025-05-27): fix tests
- `c44a31f8` **Darius Wattimena** (2025-05-27): Merge branch 'develop' into SPV-2633
- `7f71d3da` **TeqJoostD** (2025-05-27): Align status id with revents id
- `5ecac41f` **TeqJoostD** (2025-05-27): fix test
- `4e0d33c9` **TeqJoostD** (2025-05-27): fix formatting :) :(

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-05-21)

## Pull Request Overview

Adds support for a merge-back workflow for recalculation results (“merge” scenarios) by:
- Introducing new merge scenario handling in ReventsRecalculationService
- Extending data source with queries to retrieve recent scenarios by IMO
- Adding controller endpoints and models to drive merge operations

### Reviewed Changes

Copilot reviewed 5 out of 5 changed files in this pull request and generated 2 comments.

| File | Description |
| ---- | ----------- |
| ReventsRecalculationService.kt | Implements merge scenario detection, per-IMO merge logic, retry handling, and status updates |
| ReventsRecalculationsDataSource.kt | Adds `firstScenarioIdByImo` and `findMostRecentResultsByImos` to look up recent scenarios per IMO |
| ProcessingRecalculateV2Controller.kt | Exposes three new POST endpoints for ship, batch, and full-scenario merges |
| RecalculationResult.kt | Introduces `RecalculationMode`, adds `mode` property to all results, and defines `RecalculationMergeResult` model and `MERGE_SUFFIX` |


<details>
<summary>Comments suppressed due to low confidence (3)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationService.kt:364**
* [nitpick] This service class has grown significantly with both core recalculation and merge logic; consider extracting merge-specific methods into a dedicated MergeService to improve separation of concerns and testability.
```
class ReventsRecalculationService(
```
**src/main/kotlin/nl/teqplay/vesselvoyage/datasource/ReventsRecalculationsDataSource.kt:65**
* [nitpick] These new data source methods contain important date filtering and query logic; please add unit tests to cover both successful lookups and edge cases (e.g., no result or out-of-range dates).
```
fun firstScenarioIdByImo(imo: Int): String? {
```
**api/src/main/kotlin/nl/teqplay/vesselvoyage/model/RecalculationResult.kt:33**
* Adding a new mandatory `mode` property to the public interface is a breaking change for clients; ensure downstream consumers are updated or provide a deprecation path.
```
val mode: RecalculationMode
```
</details>

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-05-22)

## Pull Request Overview

This PR adds support for the revents merge-back system in the recalculation workflow.  
- Introduces new mergeShipRecalculation methods in the service for single IMO, batch IMOs, and scenario-based recalculations.  
- Adds corresponding API endpoints in the controller and updates the model with a new RecalculationMergeResult type and a mode property.  
- Extends test coverage for merge scenarios within the service and model tests.

### Reviewed Changes

Copilot reviewed 6 out of 6 changed files in this pull request and generated 1 comment.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationServiceTest.kt | Added tests for the different mergeShipRecalculation overloads |
| src/test/kotlin/nl/teqplay/vesselvoyage/model/RecalculationMergeResultTest.kt | Added tests to validate RecalculationMergeResult creation |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationService.kt | Introduced merge-back logic including merge scenario handling and V2 data merging |
| src/main/kotlin/nl/teqplay/vesselvoyage/datasource/ReventsRecalculationsDataSource.kt | Added helper functions to fetch scenario IDs and recent merge results |
| src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingRecalculateV2Controller.kt | Exposed new merge endpoints for ship and scenario-based merging |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/model/RecalculationResult.kt | Updated result models with mode support and introduced RecalculationMergeResult |
</details>



<details>
<summary>Comments suppressed due to low confidence (2)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationService.kt:665**
* Ensure that the ERROR constant used for comparing error levels is properly imported or defined, as its origin is not immediately clear from the diff.
```
errors.any { it.level == ERROR } -> STOPPED
```
**api/src/main/kotlin/nl/teqplay/vesselvoyage/model/RecalculationResult.kt:102**
* [nitpick] Document the purpose and format of the _id field in RecalculationMergeResult, particularly the rationale for appending MERGE_SUFFIX, to aid future maintainability.
```
data class RecalculationMergeResult(... override val _id: String = UUID.randomUUID().toString() + MERGE_SUFFIX, ...)
```
</details>

### TeqJoostD — COMMENTED (2025-05-22)

_No comment._

### Darius-Wattimena — DISMISSED (2025-05-23)

_No comment._

### Darius-Wattimena — DISMISSED (2025-05-27)

_No comment._

### Darius-Wattimena — APPROVED (2025-06-03)

_No comment._

## Review Comments

### Copilot — 2025-05-21 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/model/RecalculationResult.kt`

[nitpick] The `RecalculationMergeResult` class defines both `status` and `revents` fields of the same type, which is redundant and could cause confusion; consider consolidating to a single property.
```suggestion
    
```

### Copilot — 2025-05-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationService.kt`

[nitpick] This newly added public method lacks KDoc explaining its purpose, parameters, and side effects; adding documentation will help maintain consistency and readability.
```suggestion
     * Merges V2 data for a single IMO from a specific scenario.
     *
     * This method processes the merging of V2 data for a given IMO and scenario ID.
     * It delegates the merging logic to `processImoForMergingV2` and updates the provided
     * `errors` list with any issues encountered during the process.
     *
     * @param imo The IMO number of the vessel to process.
     * @param scenarioId The ID of the scenario associated with the merging process.
     * @param errors A mutable list to collect errors encountered during the merging process.
```

### Copilot — 2025-05-22 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationService.kt`

Consider documenting the rationale for returning the IMO for retry in processImoForMergingV2. If the returned value is not used downstream, clarify its intent or remove it to simplify the flow.
```suggestion

```

### TeqJoostD — 2025-05-22 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationService.kt`

It is used...

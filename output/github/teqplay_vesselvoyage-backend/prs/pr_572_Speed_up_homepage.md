---
id: github:teqplay/vesselvoyage-backend:pr:572
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 572
title: Speed up homepage
author: Darius-Wattimena
state: closed
date: '2025-07-15'
merged_at: '2025-07-15'
base_branch: develop
head_branch: speed-up-home-page
url: https://github.com/teqplay/vesselvoyage-backend/pull/572
labels: []
linked_issues: []
explicit_links: []
---
# PR #572: Speed up homepage

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/572  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `speed-up-home-page`  
**Created:** 2025-07-15  
**Merged:** 2025-07-15  

## Description

_No description._

## Commits

- `cc5e74ea` **Darius Wattimena** (2025-07-15): Rewritten the home page endpoint for the frontend to instead do a look-up in memory instead of getting the same data out of the database
- `3e493e3a` **Darius Wattimena** (2025-07-15): Added some extra comments
- `1ace1ed1` **Darius Wattimena** (2025-07-15): Do some code cleanup

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-15)

## Pull Request Overview

This PR rewrites the home page endpoint to use in-memory ship statuses instead of querying the database, removing legacy minimal query paths and models while consolidating the lookup logic into a single service method.

- Removed minimal voyage/visit query methods and associated internal models.
- Added `getAll()` in `ProcessingShipStatusService` and replaced parallel DB calls with in-memory iteration in `ProcessingFrontendViewV2Service`.
- Updated controller documentation to reflect the in-memory data source and response semantics.

### Reviewed Changes

Copilot reviewed 9 out of 9 changed files in this pull request and generated 2 comments.

<details>
<summary>Show a summary per file</summary>

| File                                                         | Description                                                             |
| ------------------------------------------------------------ | ----------------------------------------------------------------------- |
| src/main/kotlin/.../VoyageV2Service.kt                       | Removed deprecated minimal voyage lookup methods and import.           |
| src/main/kotlin/.../VisitV2Service.kt                        | Removed deprecated minimal visit lookup method and import.             |
| src/main/kotlin/.../ProcessingShipStatusService.kt           | Added `getAll()` to expose in-memory ship status map.                  |
| src/main/kotlin/.../ProcessingFrontendViewV2Service.kt       | Replaced DB queries with in-memory filtering loop over ship statuses.  |
| src/main/kotlin/.../MinimalNewVoyage.kt                       | Deleted internal minimal voyage model.                                 |
| src/main/kotlin/.../MinimalNewVisit.kt                        | Deleted internal minimal visit model.                                  |
| src/main/kotlin/.../NewVoyageDataSource.kt                    | Removed minimal voyage query methods and imports.                      |
| src/main/kotlin/.../NewVisitDataSource.kt                     | Removed minimal visit query method and imports.                        |
| src/main/kotlin/.../ProcessingFrontendViewV2Controller.kt     | Updated Javadoc to clarify in-memory response behavior.                |
</details>



<details>
<summary>Comments suppressed due to low confidence (2)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/service/ProcessingShipStatusService.kt:93**
* Add a KDoc comment describing the purpose and behavior of `getAll()`, so consumers understand that it returns a snapshot of all ship statuses.
```
    fun getAll(): Map<Int, NewShipStatus> {
```
**src/main/kotlin/nl/teqplay/vesselvoyage/service/ProcessingFrontendViewV2Service.kt:24**
* This new in-memory filtering logic should be covered by unit tests to validate each branch (visiting, just left, sailing towards) and boundary conditions.
```
    fun createPortsPageResponse(request: PortsPageRequest): PortsResponse {
```
</details>

### TeqJoostD — APPROVED (2025-07-15)

_No comment._

## Review Comments

### Copilot — 2025-07-15 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/ProcessingFrontendViewV2Service.kt`

Extract the suffix ".eosp" into a constant or utility method to avoid a magic string and ensure consistency across the codebase.

### Copilot — 2025-07-15 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/ProcessingFrontendViewV2Service.kt`

The nested loop and when blocks increase complexity; consider extracting the filtering logic into smaller, well-named functions to reduce nesting and improve readability.

---
id: github:teqplay/vesselvoyage-backend:pr:696
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 696
title: TCC-650 ship search barges
author: Darius-Wattimena
state: closed
date: '2026-01-16'
merged_at: '2026-01-19'
base_branch: develop
head_branch: TCC-650-ship-search-barges
url: https://github.com/teqplay/vesselvoyage-backend/pull/696
labels: []
linked_issues: []
explicit_links: []
---
# PR #696: TCC-650 ship search barges

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/696  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-650-ship-search-barges`  
**Created:** 2026-01-16  
**Merged:** 2026-01-19  

## Description

To simplify some of the changes I adjusted V1 related endpoints to not do anything and return empty responses so the imo based filtering isn't used anymore.
The endpoints already returned no data anyhow, so should be no issue.

## Commits

- `20b7873f` **Darius Wattimena** (2026-01-16): Adjust ship search to work with barges and refactor qualifying IMOs to qualifying ship IDs across controllers and services
- `85ab2010` **Darius Wattimena** (2026-01-16): Adjusted existing test to reflect changes in ship cache

## Reviews

### github-actions[bot] — COMMENTED (2026-01-16)

Review completed. No suggestions at this time.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-01-16)

## Pull request overview

This PR refactors the ship search and filtering logic to use ship IDs instead of IMO numbers, and deprecates V1 endpoints by making them return empty responses. The changes align with transitioning from IMO-based to ID-based ship identification, which supports vessels without IMO numbers (e.g., barges).

**Changes:**
- Migrated ship lookup/filtering from IMO-based to ship ID-based throughout V2 services and data sources
- Removed IMO-based filtering functionality including `applyFilter`, `getShipsByCategory`, and related methods from `StaticShipInfoService`
- Simplified V1 endpoints (`VoyageService`, `VisitService`) to return empty responses
- Enhanced ship search to include ship ID matching in addition to name, IMO, and MMSI

### Reviewed changes

Copilot reviewed 24 out of 24 changed files in this pull request and generated 2 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| StaticShipInfoServiceTest.kt | Removed tests for deprecated IMO-based filtering and renamed test methods |
| ShipCacheServiceTest.kt | Removed tests for IMO-based category lookup and full cache access |
| ApiVoyageV2ControllerTest.kt | Updated mock to use ship ID-based category lookup |
| ApiVisitV2ControllerTest.kt | Updated mock to use ship ID-based category lookup |
| ApiStatementOfFactsV2ControllerTest.kt | Updated mock to use ship ID-based category lookup |
| VoyageV2Service.kt | Renamed parameter from `qualifyingImos` to `qualifyingShipIds` |
| VisitV2Service.kt | Renamed parameter from `qualifyingImos` to `qualifyingShipIds` |
| BaseApiV2Service.kt | Renamed parameters from `imos` to `shipIds` |
| VoyageService.kt | Simplified V1 methods to return empty lists |
| VisitService.kt | Simplified V1 methods to return empty lists |
| StaticShipInfoService.kt | Removed IMO-based filter methods, added ship ID category lookup, enhanced search with ID matching |
| ShipCacheService.kt | Migrated category mapping from IMO-based to ship ID-based |
| ProcessingFrontendViewV2Service.kt | Updated to use ship IDs instead of IMOs for filtering |
| LimitedShipService.kt | Changed from IMO-based to ship ID-based filtering |
| NewVoyageDataSource.kt | Updated query filters to use `shipId` instead of `imo` |
| NewVisitDataSource.kt | Updated query filters to use `shipId` instead of `imo` |
| NewEntryDataSource.kt | Updated limited entry filtering to use `shipId` instead of `imo` |
| BaseApiDataSource.kt | Changed interface signatures from `imos` to `shipIds` |
| ProcessingVoyageController.kt | Removed redundant `.toList()` call |
| BaseApiV2Controller.kt | Renamed method and updated to use ship IDs, removed unused imports |
| ApiVoyageV2Controller.kt | Renamed variable from `qualifyingImos` to `qualifyingShipIds` |
| ApiVoyageController.kt | Removed redundant `.toList()` call |
| ApiVisitV2Controller.kt | Renamed variable from `qualifyingImos` to `qualifyingShipIds` |
| ApiStatementOfFactsV2Controller.kt | Renamed variable from `qualifyingImos` to `qualifyingShipIds` |
</details>

### github-actions[bot] — COMMENTED (2026-01-16)

Review completed. The migration from IMO-based to ship ID-based filtering looks structurally sound. One potential concern identified regarding null shipId handling in database queries during the migration period.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2026-01-16)

Review completed. No suggestions at this time.

### michel-teqplay — APPROVED (2026-01-19)

_No comment._

## Review Comments

### Copilot — 2026-01-16 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/StaticShipInfoService.kt`

The `query` parameter is already lowercased at line 232, but `nameMatches` is lowercasing it again. Remove the redundant `query.lowercase()` call and use `query` directly since it's already been lowercased.
```suggestion
        return this.name?.lowercase()?.contains(query) ?: false
```

### Copilot — 2026-01-16 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/StaticShipInfoService.kt`

The comment incorrectly says 'trailing whitespaces' but `trim()` removes both leading and trailing whitespace. Should be 'leading and trailing whitespace'.
```suggestion
            .trim() // Trim leading and trailing whitespace
```

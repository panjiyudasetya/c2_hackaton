---
id: github:teqplay/vesselvoyage-backend:pr:694
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 694
title: TCC-643 api adjustments for `byPort` endpoints
author: Darius-Wattimena
state: closed
date: '2026-01-12'
merged_at: '2026-01-13'
base_branch: develop
head_branch: TCC-643-api-adjustments
url: https://github.com/teqplay/vesselvoyage-backend/pull/694
labels: []
linked_issues: []
explicit_links: []
---
# PR #694: TCC-643 api adjustments for `byPort` endpoints

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/694  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-643-api-adjustments`  
**Created:** 2026-01-12  
**Merged:** 2026-01-13  

## Description

Based on the discussion the PTO team, JoostD and me had on this topic.
Jira card includes full description of the changes -> https://teqplaybv.atlassian.net/browse/TCC-643

## Commits

- `657d3232` **Darius Wattimena** (2026-01-12): Introduce VesselType enum and update endpoints to filter by vessel type when requesting by port
- `370339fa` **Darius Wattimena** (2026-01-12): Updated client to support the new vesselType parameter
- `1f7a5395` **Darius Wattimena** (2026-01-12): Made the vesselType field non-nullable to make things easier
- `71cea704` **Darius Wattimena** (2026-01-12): Update client to reflect non-nullable changes
- `0620da90` **Darius Wattimena** (2026-01-12): PR feedback

## Reviews

### github-actions[bot] — COMMENTED (2026-01-12)

Review completed. The implementation looks solid overall with proper propagation of the vesselType parameter through all layers. One potential issue identified regarding null safety in the VoyagesByPortRequest interface.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-01-12)

## Pull request overview

This pull request replaces the boolean `includeNonSeaVessels` parameter with a more flexible `vesselType: Set<VesselType>` parameter across all byPort endpoints. The change introduces a new `VesselType` enum with two values (SEA_VESSEL and BARGE) to allow filtering by vessel type.

**Changes:**
- Introduced new `VesselType` enum to distinguish between sea vessels and barges
- Replaced `includeNonSeaVessels: Boolean` with `vesselType: Set<VesselType>` across all layers (controllers, services, datasources, request/response models, and client)
- Added `queryVesselTypeFilter` helper method in `NewEntryDataSource` to generate appropriate database filters based on vessel type selection
- Updated documentation to reflect the new parameter usage

### Reviewed changes

Copilot reviewed 13 out of 13 changed files in this pull request and generated 13 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/VesselType.kt | New enum defining vessel types (SEA_VESSEL, BARGE) |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/requestresponse/VoyagesByPortRequest.kt | Updated interface and data classes to use vesselType instead of includeNonSeaVessels |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/requestresponse/VisitByPortRequest.kt | Updated data class to use vesselType instead of includeNonSeaVessels |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/requestresponse/StatementOfFactsViewByPortRequest.kt | Updated data class to use vesselType instead of includeNonSeaVessels |
| src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageV2Controller.kt | Updated controller to accept vesselType parameter with @NotEmpty validation and @Validated annotation |
| src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVisitV2Controller.kt | Updated controller to accept vesselType parameter with @NotEmpty validation and @Validated annotation |
| src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiStatementOfFactsV2Controller.kt | Updated controller to accept vesselType parameter with @NotEmpty validation and @Validated annotation |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/api/VoyageV2Service.kt | Updated service methods to accept vesselType parameter instead of includeNonSeaVessels |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/api/VisitV2Service.kt | Updated service methods to accept vesselType parameter instead of includeNonSeaVessels |
| src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt | Added queryVesselTypeFilter helper method to generate database filters based on vessel type |
| src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVoyageDataSource.kt | Updated to use queryVesselTypeFilter instead of direct IMO filtering; removed unused imports |
| src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVisitDataSource.kt | Updated to use queryVesselTypeFilter instead of direct IMO filtering; removed unused imports |
| client/src/main/kotlin/nl/teqplay/vesselvoyage/client/VesselVoyageClient.kt | Updated client methods to use vesselType parameter with improved documentation |
</details>

### TeqJoostD — COMMENTED (2026-01-12)

_No comment._

### TeqJoostD — COMMENTED (2026-01-12)

_No comment._

### Darius-Wattimena — COMMENTED (2026-01-12)

_No comment._

### TeqJoostD — APPROVED (2026-01-12)

_No comment._

### github-actions[bot] — COMMENTED (2026-01-12)

Review completed. No suggestions at this time.

## Review Comments

### Copilot — 2026-01-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt`

The documentation states "null or empty: defaults to SEA_VESSEL only (backward compatibility)" but the function signature accepts a non-nullable `Set<VesselType>` parameter. This creates a mismatch between documentation and implementation. The function will never receive null, so this part of the documentation is misleading. Update the documentation to reflect that an empty set is handled by the `else` branch returning null (no filter).
```suggestion
     * Creates a MongoDB filter based on the requested vessel types.
     *
     * Behavior:
     * - Empty set: no filter is applied (returns {@code null}).
     * - SEA_VESSEL only: filter out barges ({@code imo != MISSING_IMO}).
     * - BARGE only: filter out sea vessels ({@code imo == MISSING_IMO}).
     * - Both SEA_VESSEL and BARGE: no filter is applied (returns {@code null}).
     *
     * Returning {@code null} indicates that no vessel-type filter should be added to the query.
```

### Copilot — 2026-01-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageV2Controller.kt`

The code passes `request.vesselType` directly to the service layer, but the interface `VoyagesByPortRequest` declares `vesselType` as nullable (`Set<VesselType>?`), while the service methods expect non-nullable `Set<VesselType>`. This creates a type mismatch that could lead to compilation errors or null pointer exceptions. Either the interface should be changed to non-nullable to match implementations, or null handling should be added here (e.g., `request.vesselType ?: setOf(VesselType.SEA_VESSEL)`).

### Copilot — 2026-01-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageV2Controller.kt`

The code passes `request.vesselType` directly to the service layer, but the interface `VoyagesByPortRequest` declares `vesselType` as nullable (`Set<VesselType>?`), while the service methods expect non-nullable `Set<VesselType>`. This creates a type mismatch that could lead to compilation errors or null pointer exceptions. Either the interface should be changed to non-nullable to match implementations, or null handling should be added here (e.g., `request.vesselType ?: setOf(VesselType.SEA_VESSEL)`).

### Copilot — 2026-01-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageV2Controller.kt`

The code passes `request.vesselType` directly to the service layer, but the interface `VoyagesByPortRequest` declares `vesselType` as nullable (`Set<VesselType>?`), while the service methods expect non-nullable `Set<VesselType>`. This creates a type mismatch that could lead to compilation errors or null pointer exceptions. Either the interface should be changed to non-nullable to match implementations, or null handling should be added here (e.g., `request.vesselType ?: setOf(VesselType.SEA_VESSEL)`).

### Copilot — 2026-01-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVisitV2Controller.kt`

The code passes `request.vesselType` directly to the service layer, but `VisitByPortRequest` declares `vesselType` as non-nullable with a default value. However, when this request comes via POST endpoint deserialization, if `vesselType` is not provided in the JSON, it could potentially be null depending on Jackson configuration. Consider adding explicit null-safety handling here (e.g., `request.vesselType ?: setOf(VesselType.SEA_VESSEL)`) to ensure backward compatibility.

### Copilot — 2026-01-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVisitV2Controller.kt`

The code passes `request.vesselType` directly to the service layer, but `VisitByPortRequest` declares `vesselType` as non-nullable with a default value. However, when this request comes via POST endpoint deserialization, if `vesselType` is not provided in the JSON, it could potentially be null depending on Jackson configuration. Consider adding explicit null-safety handling here (e.g., `request.vesselType ?: setOf(VesselType.SEA_VESSEL)`) to ensure backward compatibility.

### Copilot — 2026-01-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVisitV2Controller.kt`

The code passes `request.vesselType` directly to the service layer, but `VisitByPortRequest` declares `vesselType` as non-nullable with a default value. However, when this request comes via POST endpoint deserialization, if `vesselType` is not provided in the JSON, it could potentially be null depending on Jackson configuration. Consider adding explicit null-safety handling here (e.g., `request.vesselType ?: setOf(VesselType.SEA_VESSEL)`) to ensure backward compatibility.

### Copilot — 2026-01-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt`

The `else` branch in the `when` expression handles empty sets by returning null (no filter), which means all vessels will be returned. This contradicts the documented behavior that "null or empty: defaults to SEA_VESSEL only (backward compatibility)". When an empty set is passed, it should filter for SEA_VESSEL only to maintain backward compatibility, not return all vessels. Consider changing the else branch to return the same filter as SEA_VESSEL case: `NewEntry::imo ne StaticShipInfoService.MISSING_IMO`
```suggestion
            else -> NewEntry::imo ne StaticShipInfoService.MISSING_IMO // Default to sea vessels for empty or unexpected sets
```

### Copilot — 2026-01-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiStatementOfFactsV2Controller.kt`

The code passes `request.vesselType` directly to the service layer, but `StatementOfFactsViewByPortRequest` declares `vesselType` as non-nullable with a default value. However, when this request comes via POST endpoint deserialization, if `vesselType` is not provided in the JSON, it could potentially be null depending on Jackson configuration. Consider adding explicit null-safety handling here (e.g., `request.vesselType ?: setOf(VesselType.SEA_VESSEL)`) to ensure backward compatibility.

### Copilot — 2026-01-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiStatementOfFactsV2Controller.kt`

The code passes `request.vesselType` directly to the service layer, but `StatementOfFactsViewByPortRequest` declares `vesselType` as non-nullable with a default value. However, when this request comes via POST endpoint deserialization, if `vesselType` is not provided in the JSON, it could potentially be null depending on Jackson configuration. Consider adding explicit null-safety handling here (e.g., `request.vesselType ?: setOf(VesselType.SEA_VESSEL)`) to ensure backward compatibility.

### Copilot — 2026-01-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiStatementOfFactsV2Controller.kt`

The code passes `request.vesselType` directly to the service layer, but `StatementOfFactsViewByPortRequest` declares `vesselType` as non-nullable with a default value. However, when this request comes via POST endpoint deserialization, if `vesselType` is not provided in the JSON, it could potentially be null depending on Jackson configuration. Consider adding explicit null-safety handling here (e.g., `request.vesselType ?: setOf(VesselType.SEA_VESSEL)`) to ensure backward compatibility.

### Copilot — 2026-01-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt`

The new `queryVesselTypeFilter` function introduces critical filtering logic for vessel types, but there are no tests added to verify its behavior. This function handles four distinct cases (both types, SEA_VESSEL only, BARGE only, and empty set), all of which should be tested to ensure correct filtering. Add unit tests to verify that the function returns the correct BSON filters for each case.

### Copilot — 2026-01-12 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/requestresponse/VoyagesByPortRequest.kt`

The interface declares `vesselType` as nullable (`Set<VesselType>?`), but all implementing classes declare it as non-nullable (`Set<VesselType>`). This inconsistency can lead to confusion and potential runtime issues. The interface and implementations should match - either both nullable or both non-nullable. Since the implementations default to `setOf(VesselType.SEA_VESSEL)`, making both non-nullable appears to be the intended design.
```suggestion
    val vesselType: Set<VesselType>
```

### TeqJoostD — 2026-01-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVisitV2Controller.kt`

The validation makes the endpoint not backwards compatible. Is that a problem?

### TeqJoostD — 2026-01-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageV2Controller.kt`

Same here

### Darius-Wattimena — 2026-01-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVisitV2Controller.kt`

Not really, if you don't provide the `vesselType` it will default to the `setOf(...` which is there.
It will only fail when you provide for example this as URL `http://localhost:8080/v2/sof/byPort?...&view=PTO&vesselType=` where `vesselType` is empty instead of a value provided.

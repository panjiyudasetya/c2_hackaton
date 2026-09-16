---
id: github:teqplay/vesselvoyage-backend:pr:688
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 688
title: TCC-548 api adjustments
author: Darius-Wattimena
state: closed
date: '2025-12-22'
merged_at: '2026-01-05'
base_branch: develop
head_branch: TCC-548-api-adjustments
url: https://github.com/teqplay/vesselvoyage-backend/pull/688
labels: []
linked_issues: []
explicit_links: []
---
# PR #688: TCC-548 api adjustments

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/688  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-548-api-adjustments`  
**Created:** 2025-12-22  
**Merged:** 2026-01-05  

## Description

Changes done as described at https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1057751046/API+Migration+Plan+for+Barges+Changes+to+Endpoints+Models+and+Publishing

## Commits

- `0ab38541` **Darius Wattimena** (2025-12-22): Add support for barge visits and voyages in API models
- `b526d0a5` **Darius Wattimena** (2025-12-22): Refactor API models to use ApiVisit and ApiVoyage interfaces and always add the shipId when available
- `94016807` **Darius Wattimena** (2025-12-23): Fix multiple issues where the wrong output would be provided
- `676a8f30` **Darius Wattimena** (2025-12-23): Adjusted client to match new return types and add the ability to filter based on includeNonSeaVessels for the byPort endpoints
- `3b29a092` **Darius Wattimena** (2025-12-23): Add unit tests for VesselVoyageClient and update build.gradle for Kover support
- `e83bb305` **Darius Wattimena** (2025-12-23): Code cleanup
- `f57c5925` **Darius Wattimena** (2025-12-23): Add the option to query visits, voyages and sofs by shipId
- `f81d7243` **Darius Wattimena** (2025-12-23): Remove unneeded defaults to includeNonSeaVessels options in service and data sources
- `e1032d11` **Darius Wattimena** (2025-12-23): Make sure the Entry controller also does correct ongoing filtering to align with the other controllers
- `7bd9142a` **Darius Wattimena** (2025-12-24): ktlint
- `acf04a18` **Darius Wattimena** (2025-12-24): Merge branch 'TCC-570-internal-csi-id' into TCC-548-api-adjustments
- `d6b55ff4` **Darius Wattimena** (2025-12-24): Added logging so we know when we create a barge visit or voyage
- `dba4f6db` **Darius Wattimena** (2025-12-24): Removed unneeded warning logging when imo is null

## Reviews

### github-actions[bot] — COMMENTED (2025-12-23)

Review completed. The PR implements a comprehensive API migration to support both IMO vessels and barges with proper type hierarchy and shipId resolution. The implementation is well-structured with appropriate error handling and backward compatibility.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2025-12-23)

Review completed. I've analyzed the API adjustments for barge support and identified a potential logic issue with the interaction between `includeNonSeaVessels` and ship property filtering.

## Potential Bug: Barge Filtering with Ship Property Filters

When `includeNonSeaVessels=true` is combined with ship property filters (categories, DWT, TEU), barges may be incorrectly excluded from results.

**Root cause:**

In `BaseApiV2Controller.selectImosOrEmpty()`, the method returns a set of IMO numbers based on ship categories and property ranges. However:
1. This set only contains valid IMO numbers (never `MISSING_IMO`)
2. When this set is passed as `qualifyingImos` to data source methods, it's used to filter: `NewVisit::imo in qualifyingImos`
3. Since barges have `imo == MISSING_IMO`, they're excluded even when `includeNonSeaVessels=true`

**Affected methods:**
- `NewVisitDataSource.findByPortAreaId()` (lines 92-94)
- `NewVisitDataSource.findByAisTrueDestination()` (lines 118-120)
- `NewVoyageDataSource.findByPortAreaIds()` (lines 116-118)
- `NewVoyageDataSource.findByAisDestination()` (lines 161-163)

**Suggested fix:**

In each affected data source method, modify the `qualifyingImos` filtering logic:

```kotlin
if (qualifyingImos.isNotEmpty()) {
    if (includeNonSeaVessels) {
        // Include both: vessels matching qualifyingImos OR barges
        add(or(
            NewVisit::imo `in` qualifyingImos,
            NewVisit::imo eq StaticShipInfoService.MISSING_IMO
        ))
    } else {
        add(NewVisit::imo `in` qualifyingImos)
    }
}
```

**Alternative consideration:**

If ship property filters (categories, DWT, TEU) should not apply to barges at all, then the current behavior might be intentional. In that case, this should be documented clearly in the API documentation.

---
*🤖 Automated review complete. Please react with 👍 or 👎 to provide feedback on the usefulness of this review.*

### Darius-Wattimena — COMMENTED (2025-12-23)

_No comment._

### github-actions[bot] — COMMENTED (2025-12-23)

Review completed. The PR implements API adjustments for barge support with proper separation between IMO vessels and barges. The changes are well-structured with appropriate type hierarchies and routing key differentiation. A few potential edge cases around null handling have been identified in the inline comments.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2025-12-23)

Review completed. The previous automated review has already identified the key areas of concern. No additional suggestions at this time.

### github-actions[bot] — COMMENTED (2025-12-24)

Review completed. Found one type inconsistency issue in the routing key generation for barge SOF views.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2025-12-24)

Code review completed. Found one potential bug related to null handling in the routing key generation for barge SOF views.

### github-actions[bot] — COMMENTED (2025-12-24)

I've completed my review of this PR implementing API adjustments for barge support. The changes introduce proper separation between IMO vessels and barges through new model types and interfaces. Most of the critical issues have already been identified in previous reviews. I found one additional concern regarding potential null pointer issues in the mapper's shipId resolution logic that should be addressed.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2025-12-24)

## Review Summary

Reviewed the API migration changes for barges support. I've identified several potential issues that should be addressed:

### 1. Silent Error Handling in `resolveShipId`

**Location:** `src/main/kotlin/nl/teqplay/vesselvoyage/mapper/EntryV2Mapper.kt` (line ~331)

The `resolveShipId` function throws an `IllegalArgumentException` when shipId cannot be resolved, but this exception is caught and silently converted to `null` in calling code (e.g., `BaseApiV2Controller.convertToApiModels`). This could lead to data being silently dropped without proper logging.

**Recommendation:** Add logging before throwing the exception so there's visibility into which entries are being dropped:

```kotlin
@Named("resolveShipId")
fun resolveShipId(entry: NewEntry): String {
    return entry.shipId ?: staticShipInfoService.getShipIdByImo(entry.imo)
        ?: run {
            log.warn { "Could not resolve shipId for entry ${entry._id} (imo = ${entry.imo})" }
            throw IllegalArgumentException("Could not resolve shipId for entry ${entry._id} (imo = ${entry.imo})")
        }
}
```

### 2. Logical Inconsistency with `qualifyingImos` Filter

**Locations:** 
- `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVisitDataSource.kt` (lines ~84-93)
- `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVoyageDataSource.kt` (similar pattern in multiple methods)

When `includeNonSeaVessels` is true, the code removes the filter that excludes vessels with `MISSING_IMO`, but still applies the `qualifyingImos` filter. This creates a logical inconsistency where barges would be included by the first condition but then excluded by the IMO filter (since barges don't have valid IMO numbers).

**Recommendation:** Only apply the `qualifyingImos` filter when filtering for sea vessels, or modify it to handle barges:

```kotlin
if (!includeNonSeaVessels) {
    add(NewVisit::imo ne StaticShipInfoService.MISSING_IMO)
    if (qualifyingImos.isNotEmpty()) {
        add(NewVisit::imo `in` qualifyingImos)
    }
} else if (qualifyingImos.isNotEmpty()) {
    // When including barges, only filter by IMO for vessels that have one
    add(
        or(
            NewVisit::imo eq StaticShipInfoService.MISSING_IMO,
            NewVisit::imo `in` qualifyingImos
        )
    )
}
```

### 3. Potential Null Pointer in Grouping Logic

**Location:** `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/BaseApiV2Controller.kt` (line ~194)

Grouping by `shipId` could fail if any entries have `null` shipId values. While the mapper's `resolveShipId` is supposed to resolve these, if resolution fails and the exception is caught, entries with null shipIds could cause issues.

**Recommendation:** Add a null check before grouping:

```kotlin
val groupedByShipId = this.filter { it.shipId != null }.groupBy { it.shipId!! }
```

### 4. Misleading Deprecation Message

**Location:** `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/sof/portreporter/PortReporterStatementOfFactsView.kt` (line ~272)

The deprecation message says "0 if a barge" but barges use `StaticShipInfoService.MISSING_IMO` which might not be 0.

**Recommendation:** Update the deprecation message:

```kotlin
@Deprecated("Use id instead. For barges, this will be StaticShipInfoService.MISSING_IMO", replaceWith = ReplaceWith("id"))
val imo: Int,
```

---
*🤖 Automated review complete. Please react with 👍 or 👎 on this comment to provide feedback on its usefulness.*

### michel-teqplay — DISMISSED (2026-01-05)

_No comment._

### michel-teqplay — APPROVED (2026-01-05)

_No comment._

## Review Comments

### Darius-Wattimena — 2025-12-23 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVisitV2Controller.kt`

Fine given that VisitByImoResponse only expects ImoVisit not any barges

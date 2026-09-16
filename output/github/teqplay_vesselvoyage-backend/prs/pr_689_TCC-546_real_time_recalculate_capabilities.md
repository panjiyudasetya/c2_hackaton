---
id: github:teqplay/vesselvoyage-backend:pr:689
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 689
title: TCC-546 real time recalculate capabilities
author: Darius-Wattimena
state: closed
date: '2025-12-24'
merged_at: '2026-01-06'
base_branch: develop
head_branch: TCC-546-real-time-recalculate-capabilities
url: https://github.com/teqplay/vesselvoyage-backend/pull/689
labels: []
linked_issues: []
explicit_links: []
---
# PR #689: TCC-546 real time recalculate capabilities

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/689  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-546-real-time-recalculate-capabilities`  
**Created:** 2025-12-24  
**Merged:** 2026-01-06  

## Description

_No description._

## Commits

- `25cb62d2` **Darius Wattimena** (2025-12-24): Made it possible to do story recalculations based on shipId instead of imo
- `c11796ac` **Darius Wattimena** (2025-12-24): Fixed an issue where CSI ships wouldn't be added to the local cache because they use a value of 0 as IMO which should be invalid
- `a3d8ff5a` **Darius Wattimena** (2025-12-24): Adjusted tests to work with shipId instead of imo
- `4e11c64f` **Darius Wattimena** (2025-12-24): Made it so we always maintain a pairing between the diff message and trace item + reduce logging for out of order messages given they happen a lot for barges
- `b926600d` **Darius Wattimena** (2025-12-24): Made it so you can get the ship story by imo and ship id
- `7183fd81` **Darius Wattimena** (2025-12-24): Completely rework story recalculate to work both for imo and shipId on the same endpoint
- `c4b7d13c` **Darius Wattimena** (2025-12-24): Code cleanup
- `5d9d5eb7` **Darius Wattimena** (2025-12-28): Add a toggle to disable barges when processing AIS messages
- `2967f067` **Darius Wattimena** (2026-01-05): Refactor NewEntryDataSource to require ShipIdLazyLoader and make it impossible to get a null pointer
- `8e11566c` **Darius Wattimena** (2026-01-05): Made sure shipId is not null when we process events
- `94e7773d` **Darius Wattimena** (2026-01-05): ktlint
- `4275f7f9` **Darius Wattimena** (2026-01-05): flip check to actually work as intended
- `49cf0b3c` **Darius Wattimena** (2026-01-06): PR feedback

## Reviews

### github-actions[bot] — COMMENTED (2025-12-24)

Review completed. The PR successfully refactors the recalculation system to use shipId instead of IMO, which is a good improvement for supporting non-sea vessels. The changes are generally well-structured and consistent. No critical issues found.

---
*🤖 Automated review complete.*

### github-actions[bot] — COMMENTED (2025-12-28)

This PR implements support for real-time recalculation capabilities for non-sea vessels (barges) by transitioning from IMO-based to shipId-based processing. The changes are substantial but generally well-structured. I've identified a few potential issues that should be addressed.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2026-01-05)

Found a critical logic bug in the barge filtering condition that would cause barges to be skipped when they should be processed.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2026-01-05)

Review completed. No suggestions at this time.

### TeqJoostD — COMMENTED (2026-01-06)

_No comment._

### TeqJoostD — COMMENTED (2026-01-06)

_No comment._

### TeqJoostD — COMMENTED (2026-01-06)

_No comment._

### TeqJoostD — COMMENTED (2026-01-06)

_No comment._

### TeqJoostD — COMMENTED (2026-01-06)

_No comment._

### TeqJoostD — COMMENTED (2026-01-06)

_No comment._

### TeqJoostD — COMMENTED (2026-01-06)

_No comment._

### TeqJoostD — COMMENTED (2026-01-06)

_No comment._

### TeqJoostD — COMMENTED (2026-01-06)

_No comment._

### TeqJoostD — COMMENTED (2026-01-06)

_No comment._

### TeqJoostD — CHANGES_REQUESTED (2026-01-06)

some small changes

### Darius-Wattimena — COMMENTED (2026-01-06)

_No comment._

### Darius-Wattimena — COMMENTED (2026-01-06)

_No comment._

### Darius-Wattimena — COMMENTED (2026-01-06)

_No comment._

### Darius-Wattimena — COMMENTED (2026-01-06)

_No comment._

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-01-06)

## Pull request overview

This pull request implements real-time recalculation capabilities with support for barges (vessels without IMO numbers). The primary changes involve refactoring the codebase to use `shipId` as the main identifier instead of `imo`, while maintaining backward compatibility for IMO-based lookups. A new configuration flag `trace.enable-barges` is introduced to control whether non-sea vessels should be processed.

**Key Changes:**
- Migrated from IMO-based to shipId-based identification throughout the system
- Added support for barge processing via the `enableBarges` configuration flag
- Refactored data sources to require `ShipIdLazyLoader` for consistent shipId resolution
- Updated API endpoints to accept shipId instead of IMO as path parameters

### Reviewed changes

Copilot reviewed 40 out of 40 changed files in this pull request and generated 12 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/main/resources/application.properties | Added `trace.enable-barges=true` configuration flag |
| src/test/resources/application.properties | Added test configuration for barges support |
| src/main/kotlin/nl/teqplay/vesselvoyage/properties/TraceProperties.kt | Added `enableBarges` property for trace processing |
| src/main/kotlin/nl/teqplay/vesselvoyage/model/internal/StoryRepairShip.kt | Changed primary identifier from `imo` to `shipId` |
| src/main/kotlin/nl/teqplay/vesselvoyage/model/internal/ShipStory.kt | Added `shipId` field and made `imo` nullable |
| src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt | Made `ShipIdLazyLoader` required, added lazy loading to more methods, renamed `findRecalculatedByImo` to `findRecalculatedByShipId` |
| src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVisitDataSource.kt | Made `ShipIdLazyLoader` required in constructor |
| src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVoyageDataSource.kt | Made `ShipIdLazyLoader` required in constructor |
| src/main/kotlin/nl/teqplay/vesselvoyage/datasource/StoryRepairShipDataSource.kt | Changed parameter from `imo` to `shipId` |
| src/main/kotlin/nl/teqplay/vesselvoyage/datasource/ShipIdLazyLoader.kt | Changed to always assign a shipId (using "MISSING_IN_CSI" constant when not found) |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/EventFetchingService.kt | Renamed methods from `fetchEventsByIMO`/`fetchAisEngineEventsByIMO` to camelCase versions, added new methods for MMSI and shipId-based fetching |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/EntryProcessingService.kt | Added shipId parameter to processing methods, added temporary fix for missing shipIds on existing entries |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/StoryService.kt | Changed primary parameter from `imo` to `shipId`, added support for both IMO and shipId lookups |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/*.kt | Updated recalculation services to use shipId instead of IMO |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/TraceService.kt | Added shipId parameter for trace generation |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/ProcessingTraceService.kt | Fixed trace item/diff message pairing after sorting, changed log level from warn to debug |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/AisFetchingService.kt | Updated logic to handle MISSING_IMO constant |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/ShipLockService.kt | Changed generic constraint to non-nullable |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/ShipCacheService.kt | Added check to skip MISSING_IMO values |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt | Added barge filtering based on `enableBarges` flag |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/publisher/ChangesPublisherService.kt | Removed unused `staticShipInfoService` dependency |
| src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/*.kt | Updated endpoints to use shipId instead of IMO |
| src/main/kotlin/nl/teqplay/vesselvoyage/util/entryUtils.kt | Changed log level from info to debug for barge entry creation |
| Test files | Updated all tests to use shipId instead of IMO, updated mocks for renamed methods |
</details>

### github-actions[bot] — COMMENTED (2026-01-06)

Review completed. I've identified one potential issue related to a breaking database schema change that may require attention before merging.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### Darius-Wattimena — COMMENTED (2026-01-06)

_No comment._

### TeqJoostD — APPROVED (2026-01-06)

_No comment._

## Review Comments

### TeqJoostD — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingRecalculateV2Controller.kt`

Why rename to shipId when its still an imo that your passing

### TeqJoostD — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingShipController.kt`

Same here should be IMO not shipId

### TeqJoostD — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt`

Maybe change comment since loader is always enabled now

### TeqJoostD — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt`

.

### TeqJoostD — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt`

.

### TeqJoostD — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVoyageDataSource.kt`

.

### TeqJoostD — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/StoryRepairService.kt`

Might be good to clarify why we don't fix stories for non imo vessels

### TeqJoostD — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/EntryProcessingService.kt`

It says temporary but this will never get removed unless there is a data migration right?

### TeqJoostD — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/StoryService.kt`

This is still an imo

### TeqJoostD — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/StoryService.kt`

Same here

### Darius-Wattimena — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingRecalculateV2Controller.kt`

Because it can be either an `imo` or CSI `shipId`.

So when I provide `1234567` or `some-uuid-of-a-ship` then it would be able to resolve both of them.

### Darius-Wattimena — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/StoryRepairService.kt`

Good point, it doesn't make sense at all to do this. Will remove the check because it all should work fine

### Darius-Wattimena — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/EntryProcessingService.kt`

This is more there for so it allows to do a rollback, without this existing data will explode after you do a deployment.

I'll clarify that this can be removed once barges are working without any issue on production

### Darius-Wattimena — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/StoryService.kt`

Not really it supports 2 flows: by `imo` and by `shipId`.

The exception at line 46 will only be thrown when:
1. The provided `shipId` is a number.
2. The number couldn't be resolved to a `resolvedShipIdFromImo`.

If we provide a barge ship id it will just pass line 49 and find all the data based on shipId instead of any IMO.

Eventually when all the frontend parts are gone on the vesselvoyage side we can replace this code with just lookups by `shipId` without this dual identifier support.

### Copilot — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ManualRecalculationService.kt`

The variable name `recalculationTime` is used with `measureTimeMillis` which returns a Long representing milliseconds. While the log message correctly states "(... ms)", the variable name could be more explicit, such as `recalculationTimeMillis`, to make the unit clear without relying on the log statement.

### Copilot — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/AisFetchingService.kt`

The condition logic appears to be inverted. The original code checked `if (parsedImo != 0)` and would then use IMO-based lookup. The new code checks `if (parsedImo == null || parsedImo == StaticShipInfoService.MISSING_IMO)` and falls into the MMSI lookup branch. This means when we DO have a valid IMO (not null and not MISSING_IMO), we skip the IMO lookup entirely and only use MMSI, which is likely incorrect. The condition should be negated to preserve the original logic.

### Copilot — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/EntryProcessingService.kt`

The TODO comment mentions this is a temporary fix that can be removed once code is stable on production. However, there's no tracking information (ticket number, date added, or removal criteria). This makes it difficult to know when it's safe to remove this code. Consider adding a JIRA ticket reference or specific conditions under which this can be removed.
```suggestion
        // TODO[VESSELVOY-1234 - 2026-01-06] Temporary fix for shipId missing on existing entries created before shipId was mandatory.
        //  Removal criteria: remove this once production no longer contains such legacy entries and rollback to pre-fix data is no longer required.
```

### Copilot — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingShipController.kt`

The error message still references IMO in the error text, but the function now receives shipId as a parameter. The error message should be updated to reference shipId instead for consistency and accuracy.
```suggestion
            ?: throw NotFoundException("Ship with shipId $shipId not found")
```

### Copilot — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingRecalculateV2Controller.kt`

Inconsistent parameter naming in documentation. The parameter is named `shipIds` (plural) in the function signature, but the log message uses `ships` without the Id suffix. While not incorrect, using `shipIds` in the log would be more consistent with the actual parameter name and make the code easier to trace.

### Copilot — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/TraceService.kt`

Trailing comma is unnecessary here. The line ends with a comma but there are no more parameters following it, which goes against Kotlin style conventions.
```suggestion
                previousTraceLastDraught = previousTrace?.draught?.last
```

### Copilot — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/ShipLockService.kt`

The generic type constraint has been changed from `T` to `T : Any`, which means the return type can no longer be nullable. However, the function body may return a result from the `body` lambda that could potentially be null in some contexts. This change could break existing callers that expect nullable return values. Verify that all callers of this method are compatible with the non-nullable constraint.
```suggestion
    fun <T> executeBlocking(shipId: String, body: () -> T): T {
```

### Copilot — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/ShipIdLazyLoader.kt`

When a shipId cannot be resolved, the code now assigns it to "MISSING_IN_CSI". However, this constant value will be persisted to the database and used in queries. This could lead to data integrity issues where multiple unrelated ships that are missing in CSI all get assigned the same shipId, causing them to be grouped together incorrectly. Consider using a unique identifier per ship (e.g., "MISSING_IN_CSI_{imo}") or handling this case differently to avoid collisions.

### Copilot — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVoyageDataSource.kt`

The ShipIdLazyLoader is now required (not optional) in the constructor, but there's a risk of circular dependency issues during Spring initialization. The data sources need ShipIdLazyLoader, which needs StaticShipInfoService, which might depend on other services that use these data sources. Verify that the dependency graph doesn't create circular dependencies that would prevent the application from starting.

### Copilot — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt`

The findRecalculatedByShipId method no longer applies lazy loading of shipId (the shipIdLazyLoader.processEntries call was removed). This is inconsistent with other find methods in the same class that do apply lazy loading. This could lead to entries being returned without their shipId resolved, which may cause issues for callers expecting the shipId to be populated.
```suggestion
        val entries = collection.find(filter).toList()
        shipIdLazyLoader.processEntries(entries)
        return entries
```

### Copilot — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/StoryService.kt`

In the storyDryRunWithShipId function, when imo is not null but equals MISSING_IMO, the code still proceeds to create a ShipStory with MISSING_IMO instead of falling back to the shipId-based logic. The condition should check `if (imo == null || imo == StaticShipInfoService.MISSING_IMO)` to handle both cases consistently.
```suggestion
        if (imo == null || imo == StaticShipInfoService.MISSING_IMO) {
            // When no valid IMO is available, fall back to shipId-based dry run logic.
        } else {
```

### Copilot — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/EntryProcessingService.kt`

The function signature now includes a required shipId parameter with no default value, but the original overload that inferred shipId from events still exists. This creates two overloaded functions with similar but different parameter sets, which could be confusing. Consider adding a deprecation notice to the original function or documenting clearly when each should be used to avoid confusion about which version to call.

### Darius-Wattimena — 2026-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/model/internal/StoryRepairShip.kt`

Database is not filled for this collection

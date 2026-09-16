---
id: github:teqplay/vesselvoyage-backend:pr:678
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 678
title: TCC-548 Add CSI ID to internal ShipCache and AIS retrieving
author: Darius-Wattimena
state: closed
date: '2025-12-05'
merged_at: '2025-12-22'
base_branch: develop
head_branch: TCC-548-ship-cache-csi-id
url: https://github.com/teqplay/vesselvoyage-backend/pull/678
labels: []
linked_issues: []
explicit_links: []
---
# PR #678: TCC-548 Add CSI ID to internal ShipCache and AIS retrieving

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/678  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-548-ship-cache-csi-id`  
**Created:** 2025-12-05  
**Merged:** 2025-12-22  

## Description

_No description._

## Commits

- `9c1f66e7` **Darius Wattimena** (2025-12-05): Refactor ShipCache and the way how AIS is retrieved to use the CSI ship ID and improve data structure
- `16e3116f` **Darius Wattimena** (2025-12-05): Add unit tests for ShipCacheService to validate cache operations and mappings
- `8f15c8ea` **Darius Wattimena** (2025-12-08): ktlint
- `ccc4af96` **Darius Wattimena** (2025-12-08): Renamed variable to avoid var shadowing

## Reviews

### github-actions[bot] — COMMENTED (2025-12-05)

Code review completed. The refactoring improves the data structure by flattening the ShipCache model and adding CSI ID support for AIS retrieval. The changes are well-structured and maintain backward compatibility.

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-12-05)

## Pull request overview

This PR refactors the internal ShipCache model to support CSI ID as the primary identifier, enhancing ship data retrieval capabilities. The changes simplify the data structure by flattening nested cache objects and add support for retrieving ship information by CSI ID in addition to existing IMO and MMSI lookups.

Key changes include:
- Simplified ShipCache model from nested structure to flat fields (id, register, imoMmsiMapping)
- Added CSI ID-based retrieval methods in ShipCacheService and StaticShipInfoService
- Enhanced AisFetchingService to support CSI ID parameter for AIS trace retrieval
- Updated all dependent services and tests to use the new ShipCache structure

### Reviewed changes

Copilot reviewed 18 out of 18 changed files in this pull request and generated 13 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/vesselvoyage/model/internal/ShipCache.kt | Simplified ShipCache model by removing nested CsiShipCache and CsiImoMmsiCache classes, replacing with flat structure using CSI ID as primary identifier |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/ShipCacheService.kt | Added shipCacheById map and getCacheById method; updated cache population logic to use CSI ID; generalized updateShipCache to support any key type |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/StaticShipInfoService.kt | Added getShipMmsiByCsiId and getShipImoByCsiId methods; changed refresh logic from concurrent to sequential execution; removed unused concurrent imports |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/AisFetchingService.kt | Added csiId parameter to getShipTrace; renamed getTraceFromAIS to getTraceFromAisByImo; added getTraceFromAisByMmsi for MMSI-based retrieval |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/V1TraceService.kt | Updated method call from getTraceFromAIS to getTraceFromAisByImo |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/TraceService.kt | Added csiId: null parameter to getShipTrace calls |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt | Added csiId: null parameter to getShipTrace calls |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/EntryProcessingService.kt | Added csiId: null parameter to getShipTrace calls |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/port/PortStartProcessor.kt | Simplified getShipTraceFunction to always return empty list, removing conditional logic |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGenerator.kt | Updated ShipCache access from csi.register to register |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/api/PortReporterStatementOfFactsViewGenerator.kt | Updated ShipCache access from csi.register to register |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/ShipCacheServiceTest.kt | Added comprehensive test suite (22 tests) for ShipCacheService functionality including CSI ID lookups |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/StaticShipInfoServiceTest.kt | Removed test for CSI history IMO-MMSI mapping |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGeneratorTest.kt | Updated ShipCache construction to use new flat structure with id and register fields |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/api/PortReporterStatementOfFactsViewGeneratorTest.kt | Updated ShipCache construction to use new flat structure with id and register fields |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/StoryServiceTest.kt | Updated mock setup to include new csiId parameter in getShipTrace |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/ProcessingTraceServiceTest.kt | Updated mock setup to include new csiId parameter in getShipTrace |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingServiceTest.kt | Updated mock setup to include new csiId parameter in getShipTrace (with trailing commas) |
</details>



<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**src/test/kotlin/nl/teqplay/vesselvoyage/service/StaticShipInfoServiceTest.kt:183**
* Test coverage removed: The test `should create csi history imo mmsi mapping` has been deleted without replacement. This test was validating IMO-MMSI mapping functionality across different time ranges. While the PR adds CSI ID functionality, it should maintain test coverage for existing IMO-MMSI mapping behavior. Consider migrating this test to `ShipCacheServiceTest.kt` or ensuring equivalent coverage exists elsewhere.
```
    @Test
    fun `should use DiskCache - load without cache`() {
        val csiClient: CSIClient = mock()
        val slackMessageService: SlackMessageService = mock()
        val tempFileDataSource: TempFileDataSource = mock()

        doReturn(listOf<ShipRegisterInfoCache>()).whenever(csiClient).listShipRegisterInfoCache()
        doReturn(listOf<ShipRegisterMapping>()).whenever(csiClient).listShipRegisterMapping()

        val shipCacheService = ShipCacheService()
        StaticShipInfoService(
            testDiskCacheProperties,
            testAppProperties,
            csiClient,
            slackMessageService,
            shipCacheService,
            tempFileDataSource
        ).also {
            runBlocking { it.onStartup() }
        }

        // should invoke both readFromFile and fetching from the clients
        verify(csiClient, times(1)).listShipRegisterInfoCache()
        verify(csiClient, times(1)).listShipRegisterMapping()
        verify(tempFileDataSource, times(2)).readFromFile(any(), any<TypeReference<Any>>())
    }

    @Test
    fun `should use DiskCache - refresh`() {
        val csiClient: CSIClient = mock()
```
</details>

### github-actions[bot] — COMMENTED (2025-12-08)

Review completed. The refactoring to use CSI ship IDs in ShipCache and AIS retrieval looks well-implemented with proper fallback mechanisms and comprehensive test coverage.

### github-actions[bot] — COMMENTED (2025-12-08)

Review completed. No suggestions at this time.

### michel-teqplay — APPROVED (2025-12-18)

_No comment._

## Review Comments

### Copilot — 2025-12-05 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/ShipCacheService.kt`

Incorrect return value: The function always returns `true` on line 230, which will always count operations as "updated" rather than distinguishing between "added" and "updated". Since we're only updating existing caches (line 217-223 skips if cache doesn't exist), this should return `true` to correctly indicate an update operation. However, the comment on line 229 suggests this is intentional, but it makes the "added" count misleading in the log message on line 233. Consider either removing the "added" count from the log or fixing the logic to properly distinguish between adds and updates.
```suggestion
        log.info { "Completed loading in CSI imo mmsi mapping into ShipCache (updated = $totalUpdated)" }
```

### Copilot — 2025-12-05 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/port/PortStartProcessor.kt`

Dead code: The function `getShipTraceFunction` now unconditionally returns a lambda that always returns an empty list, making the `config` parameter unused. This suggests the entire conditional logic was removed, which may indicate incomplete implementation. If this is intentional and trace calculations are truly disabled, consider removing this function entirely and directly using `{ _, _, _ -> emptyList() }` at the call site, or document why this function still exists.

### Copilot — 2025-12-05 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingServiceTest.kt`

[nitpick] Trailing comma after the last parameter. In Kotlin, while trailing commas are allowed, this appears to be inconsistent with the other function calls in this file and creates unnecessary noise.
```suggestion
        verify(aisFetchingService, times(3)).getShipTrace(anyOrNull(), any<Int>(), any<ZonedDateTime>(), any<ZonedDateTime>())
```

### Copilot — 2025-12-05 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingServiceTest.kt`

[nitpick] Trailing comma after the last parameter. In Kotlin, while trailing commas are allowed, this appears to be inconsistent with the other function calls in this file and creates unnecessary noise.
```suggestion
        whenever(aisFetchingService.getShipTrace(any<String>(), any<Int>(), any<ZonedDateTime>(), any<ZonedDateTime>())).thenReturn(emptyList())
```

### Copilot — 2025-12-05 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/StaticShipInfoService.kt`

The removal of concurrent execution could negatively impact performance. The original code used `GlobalScope.launch` with multiple concurrent coroutines for `refreshCsiShips()` and `refreshCsiShipRegister()`. The new implementation runs these sequentially, which will increase the total refresh time. While the comment mentions that IMO-MMSI mapping needs ships loaded first, consider whether this sequential constraint is necessary during refresh (where data already exists) versus startup. If the constraint only applies to startup, the original concurrent approach for refresh was correct and should be restored.

### Copilot — 2025-12-05 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/ShipCacheServiceTest.kt`

Missing test coverage: While this test file provides good coverage for `ShipCacheService`, it lacks tests for the new CSI ID-based retrieval methods (`getCacheById`, `getShipMmsiByCsiId`, `getShipImoByCsiId`) when integrated with `StaticShipInfoService`. The removed test from `StaticShipInfoServiceTest.kt` tested the full integration with time-based IMO-MMSI mapping queries, which is not covered here.

### Copilot — 2025-12-05 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/StaticShipInfoService.kt`

Unused imports: The imports `GlobalScope`, `Dispatchers`, and `async` are no longer used after removing the concurrent execution logic. These should be removed to keep the code clean.
```suggestion

```

### Copilot — 2025-12-05 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/ShipCacheService.kt`

Outdated documentation: The KDoc comment still refers to "the IMO number of a vessel as its key" but the function has been generalized to work with any key type `T`. The documentation should be updated to reflect that this function now handles any identifier type (CSI ID, IMO, or MMSI).

### Copilot — 2025-12-05 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingServiceTest.kt`

[nitpick] Trailing comma after the last parameter. In Kotlin, while trailing commas are allowed, this appears to be inconsistent with the other function calls in this file and creates unnecessary noise.
```suggestion
        whenever(aisFetchingService.getShipTrace(anyOrNull(), any<Int>(), any<ZonedDateTime>(), any<ZonedDateTime>())).thenReturn(emptyList())
```

### Copilot — 2025-12-05 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingServiceTest.kt`

[nitpick] Trailing comma after the last parameter. In Kotlin, while trailing commas are allowed, this appears to be inconsistent with the other function calls in this file and creates unnecessary noise.
```suggestion
        whenever(aisFetchingService.getShipTrace(anyOrNull(), any<Int>(), any<ZonedDateTime>(), any<ZonedDateTime>()))
```

### Copilot — 2025-12-05 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingServiceTest.kt`

[nitpick] Trailing comma after the last parameter. In Kotlin, while trailing commas are allowed, this appears to be inconsistent with the other function calls in this file and creates unnecessary noise.
```suggestion
        whenever(aisFetchingService.getShipTrace(anyOrNull(), any<Int>(), any<ZonedDateTime>(), any<ZonedDateTime>()))
```

### Copilot — 2025-12-05 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingServiceTest.kt`

[nitpick] Trailing comma after the last parameter. In Kotlin, while trailing commas are allowed, this appears to be inconsistent with the other function calls in this file and creates unnecessary noise.
```suggestion
        whenever(aisFetchingService.getShipTrace(any<String>(), any<Int>(), any<ZonedDateTime>(), any<ZonedDateTime>())).thenReturn(emptyList())
```

### Copilot — 2025-12-05 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/AisFetchingService.kt`

Variable shadowing: The parameter `imo` is shadowed by reassigning it on line 38. This makes the code harder to understand and could lead to confusion about which value is being used. Consider using a different variable name for the resolved IMO value (e.g., `resolvedImo`) to make the code clearer.

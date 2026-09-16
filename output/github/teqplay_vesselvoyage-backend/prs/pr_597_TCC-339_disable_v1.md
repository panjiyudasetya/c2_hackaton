---
id: github:teqplay/vesselvoyage-backend:pr:597
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 597
title: TCC-339 disable v1
author: Darius-Wattimena
state: closed
date: '2025-08-19'
merged_at: '2025-08-25'
base_branch: develop
head_branch: TCC-339-disable-v1
url: https://github.com/teqplay/vesselvoyage-backend/pull/597
labels: []
linked_issues: []
explicit_links: []
---
# PR #597: TCC-339 disable v1

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/597  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-339-disable-v1`  
**Created:** 2025-08-19  
**Merged:** 2025-08-25  

## Description

_No description._

## Commits

- `91133abc` **Darius Wattimena** (2025-08-18): Mark all V1 related code as deprecated, adjust the ship cache to make use of Int instead of String and don't load in the V1 trace service when not enabled
- `4b9369b3` **Darius Wattimena** (2025-08-18): Adjusted some more code so it at least compiles
- `cb53fc4b` **Darius Wattimena** (2025-08-19): Correct tests to all work again
- `aeb7351c` **Darius Wattimena** (2025-08-19): ktlint please
- `ba18b268` **Darius Wattimena** (2025-08-19): Make sure to load in all ship data after the CSI ships are loaded in
- `19284e7a` **Darius Wattimena** (2025-08-19): Make the shipStatusService nullable as we don't load this in when running in revents mode
- `5216ed3a` **Darius Wattimena** (2025-08-19): Adjusted loading of ship state to be done via ID
- `b2405226` **Darius Wattimena** (2025-08-19): Added missing type field
- `7d1126fe` **Darius Wattimena** (2025-08-19): Merge branch 'develop' into TCC-339-disable-v1
- `4ed9e7dc` **Darius Wattimena** (2025-08-19): Make loading of ship data fully lazy as it is now quickly loaded by ids
- `a87fd92d` **Darius Wattimena** (2025-08-19): Fix NPE that can happen when the identifiers are unsynced with the current ship status
- `dd567e0e` **Darius Wattimena** (2025-08-19): Remove the identifiers as well when we remove the ship status from memory

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-08-19)

## Pull Request Overview

This PR disables v1 processing by removing v1-specific code, making the v1 APIs optional, and changing IMO/MMSI identifiers from String to Int types throughout the codebase.

- Removal of entire v1-specific services and test files
- Type conversion of ship identifiers from String to Int
- Introduction of conditional configuration to make v1 components optional

### Reviewed Changes

Copilot reviewed 148 out of 148 changed files in this pull request and generated 6 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| Multiple test utility files | Updated test helper functions to use Int types for IMO/MMSI instead of String |
| ESoFMergeV2ServiceTest.kt | Completely removed test file for v1 ESoF merge service |
| Various service classes | Changed method signatures and logic to use Int for ship identifiers |
| Util files | Added @Deprecated annotations to v1-specific utility functions |
| Property files | Marked v1-specific configuration properties as deprecated |
| Model files | Added new ship status identifier models for caching optimization |
</details>

### TeqJoostD — COMMENTED (2025-08-22)

_No comment._

### TeqJoostD — APPROVED (2025-08-22)

L G T M

## Review Comments

### Copilot — 2025-08-19 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGenerator.kt`

Method name has a typo: 'getCachyByMmsi' should be 'getCacheByMmsi'
```suggestion
            ?: mmsi?.let { shipCacheService.getCacheByMmsi(it)?.csi?.register?.toShipDetails() }
```

### Copilot — 2025-08-19 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGenerator.kt`

Converting imo to String but the field expects Int based on context. This could cause type inconsistency.
```suggestion
                imo = imo,
```

### Copilot — 2025-08-19 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/ShipCacheService.kt`

[nitpick] Multiple safe calls and string-to-int conversion could be optimized. Consider caching the result or using a more direct lookup.
```suggestion
        // This map should be kept up-to-date in updateCsiCache or wherever the cache is updated
        return mmsiByImo[imo]
```

### Copilot — 2025-08-19 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGeneratorTest.kt`

The mock setup expects String (imo) but the method signature was changed to accept Int. This will cause test failures.
```suggestion
        whenever(shipCacheService.getCacheByImo(eq(imo.toString()))).thenReturn(shipCache)
        val actual = generator.generate(visit = createNewVisit(imo = imo.toString()), esof = null, previousPortAreaId = null)
```

### Copilot — 2025-08-19 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGeneratorTest.kt`

Converting the result to Int suggests type mismatch. The assertion should directly compare Int values if imo is already Int.
```suggestion
        assertEquals(imo, actual.ship.imo)
```

### Copilot — 2025-08-19 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationService.kt`

[nitpick] Making v1TraceService nullable introduces potential null checks throughout the code. Consider using a null object pattern or feature flag to maintain cleaner code.
```suggestion
    private val v1TraceService: V1TraceService,
```

### TeqJoostD — 2025-08-22 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/model/NewEventProcessingResult.kt`

[nitpick] Seperate class or inside the NewEventProcessing class.

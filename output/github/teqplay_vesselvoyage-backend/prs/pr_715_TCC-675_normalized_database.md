---
id: github:teqplay/vesselvoyage-backend:pr:715
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 715
title: TCC-675 normalized database
author: Darius-Wattimena
state: closed
date: '2026-02-17'
merged_at: '2026-02-27'
base_branch: develop
head_branch: TCC-675-normalized-database
url: https://github.com/teqplay/vesselvoyage-backend/pull/715
labels: []
linked_issues: []
explicit_links: []
---
# PR #715: TCC-675 normalized database

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/715  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-675-normalized-database`  
**Created:** 2026-02-17  
**Merged:** 2026-02-27  

## Description

Adjusts the following:
1. Add normalized models and logic to retrieve from the new collections.
2. Add background process to convert the non-normalized models to the normalized ones.
3. Remove old code related to the Ship ID migration which was clashing with the normalized collections.
4. Remove support in data sources to find Visits or Voyages by IMO, only allows Ship ID or port lookups.

## Commits

- `a1cab65b` **Darius Wattimena** (2026-02-05): Implement normalized data models and data sources for visits, voyages and esofs
- `7593e8c1` **Darius Wattimena** (2026-02-06): Add tests for normalized data models and conversion logic
- `c7d3d073` **Darius Wattimena** (2026-02-06): Rework all finds and saves to make use of the normalized models
- `f3a7c997` **Darius Wattimena** (2026-02-09): Replace all byImo calls with shipId equivalents so both the normalized an non-normalized endpoints are called
- `e129ec09` **Darius Wattimena** (2026-02-09): Implement normalization migration service and data sources for visits, voyages, and ESoFs
- `6860edd0` **Darius Wattimena** (2026-02-09): Refactor API to use shipId instead of IMO under the hood
- `34f630a7` **Darius Wattimena** (2026-02-09): code cleanup
- `f8e6888d` **Darius Wattimena** (2026-02-10): Added the ability to migrate data from the denormalized data source the normalized variant
- `af74f539` **Darius Wattimena** (2026-02-11): Add dual writes so it is easier to revert back changes if we need to go back to the old version of VesselVoyage
- `36e9f68e` **Darius Wattimena** (2026-02-11): Correct default configuration
- `ddc1ed68` **Darius Wattimena** (2026-02-12): Merge branch 'develop' into TCC-675-normalized-database
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVoyageDataSource.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/StaticShipInfoService.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/AutomaticRecalculationService.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/RecalculationEnlargeTimeWindowService.kt
  #	src/test/kotlin/nl/teqplay/vesselvoyage/service/recalculation/RecalculationEnlargeTimeWindowServiceTest.kt
- `82c089a2` **Darius Wattimena** (2026-02-16): Fixed some compile issues after merging latest develop
- `7df0a567` **Darius Wattimena** (2026-02-17): Merge branch 'develop' into TCC-675-normalized-database
- `b3b2437b` **Darius Wattimena** (2026-02-17): Code cleanup after merging
- `35e4a572` **Darius Wattimena** (2026-02-17): Added controller so we can get the status on how far the migration is
- `98da08b8` **Darius Wattimena** (2026-02-17): ktlint
- `d2d85817` **Darius Wattimena** (2026-02-19): Track partial failures in migrateShip() to prevent marking ships as COMPLETED when individual entries fail
- `24c407de` **Darius Wattimena** (2026-02-19): Make saveForEntry and saveForEntryAndType atomic using bulkWrite
  Replace separate delete+insertMany with a single bulkWrite() call that
  includes a DeleteManyModel followed by InsertOneModel entries. This
  eliminates the window where concurrent reads could see incomplete data.
- `95b968d6` **Darius Wattimena** (2026-02-19): refactor: deduplicate voyage results during dual-write period
  Agent-Id: agent-9c8aa5f3-bfd8-4388-b4c6-64ba48487c58
  Linked-Note-Id: cd31c480-2c7e-480f-b592-ef9da050026c
- `61a30055` **Darius Wattimena** (2026-02-19): Fix countLimitedEntries double-counting in Visit and Voyage data sources
  During dual-write transition, entries exist in both normalized and old
  collections. The previous implementation naively added normalizedCount +
  oldCount, producing inflated totals.
  
  Fix: collect IDs from the normalized collection first, then count old
  collection entries excluding those IDs via Filters.nin. Return the sum
  of unique entries. This follows the same deduplication pattern already
  used in getLimitedEntries().
  
  Agent-Id: agent-44cac8bf-75f4-4dcc-b656-c577336856ba
- `a34c482f` **Darius Wattimena** (2026-02-19): fix: prevent double-counting in countLimitedEntries by excluding normali
  Agent-Id: agent-44cac8bf-75f4-4dcc-b656-c577336856ba
  Linked-Note-Id: 9103e958-2ccb-43d4-9aa7-d3e7ecbfad99
- `8c161d2e` **Darius Wattimena** (2026-02-20): refactor: streamline countLimitedEntries in NewVisitDataSource and NewVoyageDataSource

## Reviews

### github-actions[bot] — COMMENTED (2026-02-17)

## Code Review: Normalized Database Migration

I've reviewed the PR and identified several potential bugs related to data consistency during the migration period:

### 1. Double-counting in `countLimitedEntries()` ⚠️

**Location:** `NewVisitDataSource.kt` (lines 521-537) and `NewVoyageDataSource.kt` (similar pattern)

**Issue:** The method adds counts from both normalized and old collections, which will return incorrect totals during the migration period when data exists in both places. The code comment acknowledges this but doesn't fix it.

**Impact:** This could cause issues for pagination, UI display, or any logic that depends on accurate counts.

**Recommendation:** Track which entries have been migrated and exclude them from the old collection count by fetching normalized IDs first and using a `nin` (not in) filter on the old collection.

---

### 2. Stale data risk in `findNewestStartedBeforeByShipId()` and `findOldestEndedAfterByShipId()` ⚠️

**Location:** `NewVoyageDataSource.kt` (lines 221-230 and 254-263)

**Issue:** These methods combine results from both collections using `maxByOrNull`/`minByOrNull` on start time. During migration when dual-writes are happening, this could return stale data from the old collection if it hasn't been cleaned up yet, even though a newer version exists in the normalized collection.

**Impact:** Could return outdated voyage information.

**Recommendation:** Prioritize normalized data when it exists. Check the normalized collection first, and only fall back to the old collection if nothing is found.

---

### 3. Non-atomic delete-then-insert pattern ⚠️

**Location:** 
- `NormalizedStopDataSource.kt` (lines 42-51 in `saveForEntry()`)
- `NormalizedAreaActivityDataSource.kt` (lines 2993-3002 in `saveForEntryAndType()`)

**Issue:** Both methods delete existing data then insert new data in separate operations. This creates a window where reads will return incomplete data.

**Impact:** If a read happens between the delete and insert operations, it will return incomplete or missing data, potentially causing errors in the application.

**Recommendation:** Use MongoDB's `bulkWrite()` to combine the delete and insert operations into a single atomic operation, or consider using transactions if available.

---

### 4. Unnecessary re-migration ⚠️

**Location:** `NormalizationBackgroundMigrationService.kt` (lines 127-180 in `migrateShip()`)

**Issue:** The method calls `createOrReplace()` for all entries without checking if they're already in the normalized collection, potentially re-processing already-migrated data.

**Impact:** Wastes resources and could cause unnecessary database load during migration.

**Recommendation:** Check if each entry already exists in the normalized collection before calling `createOrReplace()`. This will make the migration restart-proof and more efficient.

---

### Summary

All identified issues are related to the dual-collection pattern during the migration period. The migration strategy is sound, but these edge cases should be addressed to ensure data consistency and correctness during the transition.

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-02-17)

## Pull request overview

This PR implements database normalization for Visit, Voyage, and ESoF data by introducing normalized storage collections and a background migration service to convert existing denormalized data.

**Changes:**
- Introduced normalized database models and datasources for storing visits, voyages, and ESoFs with references to child documents (stops, encounters, area activities, etc.)
- Added a background migration service to gradually convert denormalized data to normalized storage on a per-ship basis with progress tracking
- Removed deprecated IMO-based lookup methods in favor of Ship ID-based queries, with IMO-to-ShipID conversion at API boundaries

### Reviewed changes

Copilot reviewed 47 out of 47 changed files in this pull request and generated 2 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| NormalizationBackgroundMigrationService.kt | Background service for gradual migration of ship data to normalized storage |
| NormalizedStopDataSource.kt | Datasource for normalized stop documents stored separately from entries |
| NewVisitDataSource.kt | Updated to dual-write to both normalized and denormalized collections with fallback reads |
| NewVoyageDataSource.kt | Updated to dual-write to both normalized and denormalized collections with fallback reads |
| NewESoFDataSource.kt | Updated to dual-write to both normalized and denormalized collections with fallback reads |
| BaseApiV2Controller.kt | Simplified IMO-based queries to convert IMO to ShipID at API boundary |
| StoryService.kt | Refactored to use ShipID-based queries instead of conditional IMO/ShipID logic |
| NormalizationMigrationProgress.kt | Model for tracking per-ship migration progress |
</details>



<details>
<summary>Comments suppressed due to low confidence (2)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/service/migration/NormalizationBackgroundMigrationService.kt:1**
* Hard-coded sleep duration makes tests brittle and slow. Consider using a configurable timeout or a more robust synchronization mechanism like CountDownLatch or CompletableFuture to wait for migration completion.
**src/main/kotlin/nl/teqplay/vesselvoyage/service/api/VoyageV2Service.kt:1**
* The staticShipInfoService parameter is injected but never used in the class. This creates unnecessary coupling and should be removed.
</details>

### github-actions[bot] — COMMENTED (2026-02-17)

Review completed. I've identified one critical bug in the dual-read logic that could cause incorrect results during the migration period when entries exist in both collections.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2026-02-17)

Reviewed the normalized database implementation. Found a few potential issues related to data consistency during the migration period.

### github-actions[bot] — COMMENTED (2026-02-17)

Review completed. I've identified several potential data consistency and concurrency issues in the normalization implementation that should be addressed.

### michel-teqplay — APPROVED (2026-02-23)

_No comment._

## Review Comments

### Copilot — 2026-02-17 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVisitDataSource.kt`

The comment acknowledges double-counting but the code doesn't prevent it. During the dual-write transition period, entries exist in both collections, leading to incorrect counts. Consider fetching IDs from both collections and deduplicating before counting.
```suggestion
        // Build filter for normalized collection
        val normalizedFilter = if (shipIds.isEmpty()) {
            NormalizedVisit::limited eq limited
        } else {
            and(NormalizedVisit::limited eq limited, NormalizedVisit::shipId `in` shipIds)
        }

        // Collect IDs from normalized collection to avoid double-counting
        val normalizedIds: Set<String> = normalizedVisitCollection
            .find(normalizedFilter)
            .map { it._id }
            .toSet()

        // Collect IDs from old collection that are not present in normalized collection
        val oldUniqueIds = mutableSetOf<String>()
        val pageSize = 1_000
        var skip = 0

        while (true) {
            val batch = super.getLimitedEntries(limited, shipIds, pageSize, skip)
            if (batch.isEmpty()) {
                break
            }

            batch.forEach { visit ->
                val id = visit._id
                if (id !in normalizedIds) {
                    oldUniqueIds.add(id)
                }
            }

            // Advance pagination
            skip += batch.size
            if (batch.size < pageSize) {
                // No more results expected
                break
            }
        }

        // Total unique entries across both collections
        return normalizedIds.size.toLong() + oldUniqueIds.size.toLong()
```

### Copilot — 2026-02-17 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVoyageDataSource.kt`

Same double-counting issue as NewVisitDataSource. During the transition period when dual-writing is active, this will return inflated counts as entries exist in both collections.
```suggestion
        // Prefer normalized collection; fall back to old collection if none found
        return if (normalizedCount > 0) {
            normalizedCount
        } else {
            super.countLimitedEntries(limited, shipIds)
        }
```

### michel-teqplay — 2026-02-23 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewESoFDataSource.kt`

Better to just import this

### michel-teqplay — 2026-02-23 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewESoFDataSource.kt`

Same here

## Comments

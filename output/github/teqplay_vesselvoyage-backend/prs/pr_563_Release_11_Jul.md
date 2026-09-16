---
id: github:teqplay/vesselvoyage-backend:pr:563
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 563
title: Release 11 Jul
author: Darius-Wattimena
state: closed
date: '2025-07-11'
merged_at: '2025-07-11'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/563
labels: []
linked_issues: []
explicit_links: []
---
# PR #563: Release 11 Jul

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/563  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2025-07-11  
**Merged:** 2025-07-11  

## Description

_No description._

## Commits

- `792f6e0f` **Darius Wattimena** (2025-06-27): Update AIS processing logic to not spam warnings when the event processing is ahead of AIS processing
- `129af620` **Darius Wattimena** (2025-06-27): Adjusted how traces are inserted to be much more low weight and fixed the logic when we are not in sync with event processing so we don't drop AIS points
- `65222be1` **Darius Wattimena** (2025-06-27): Added an extra test case to ensure EOSP end events are properly ignored
- `d36221d8` **Darius Wattimena** (2025-06-27): Added some extra logging to identify some odd data cases
- `4c9ae92a` **Darius Wattimena** (2025-06-27): Disabled logging for V1 processing so we can see debug messages for V2 processing
- `f3f0903e` **Darius Wattimena** (2025-06-27): ktlint
- `0578a997` **Darius Wattimena** (2025-07-07): Merge branch 'develop' into TCC-147-processing-fixes
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageEndProcessor.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessor.kt
- `1b2931c5` **Darius Wattimena** (2025-07-07): Fixed compile issue after merging latest develop
- `ff91ca18` **Darius Wattimena** (2025-07-07): Added some additional logging to ensure we know what is happening when a bulk write issue occurs
- `00e20ebc` **Darius Wattimena** (2025-07-07): ktlint
- `0ba075ae` **Darius Wattimena** (2025-07-07): Updated logging to trace instead of debug
- `4be031fd` **Darius Wattimena** (2025-07-08): Also log the failed IDs
- `0db9f181` **Darius Wattimena** (2025-07-10): Adjusted how we get the failed ids so it hopefully works
- `1ba90428` **Darius Wattimena** (2025-07-10): Merge branch 'develop' into TCC-147-processing-fixes
- `fe7e6c13` **Darius Wattimena** (2025-07-10): Refactor error handling to extract failed IDs from the messages instead
- `c6b4b0da` **Darius Wattimena** (2025-07-10): Refactor ImoLockService to use ReentrantLock for improved concurrency handling and add unit tests for locking behavior
- `21cbf4a7` **Darius Wattimena** (2025-07-10): Reworked locking so it is hopefully performant
- `090acee1` **Darius Wattimena** (2025-07-10): Set logging to debug level to reduce unneeded spam
- `65f5cd38` **Darius Wattimena** (2025-07-10): Adjusted failed entry logging so we find the correct entity based on the change type
- `a88dcd1f` **Darius Wattimena** (2025-07-10): Adjusted locking to be using a try-finally block so we can ensure the ship is always unlocked even when something goes wrong
- `816c4f00` **Darius Wattimena** (2025-07-10): Fixed typo in variable name
- `425a8fbc` **Darius Wattimena** (2025-07-11): Fixed flow of locking so we always unlock the IMO even when something goes wrong
- `e9c05115` **Darius Wattimena** (2025-07-11): Reduce log levels when processing is blocked
- `31e4f4ff` **Darius Wattimena** (2025-07-11): Merge pull request #559 from teqplay/TCC-147-processing-fixes
  TCC-147 processing fixes
- `8d7346e7` **Darius Wattimena** (2025-07-11): Merge branch 'develop' into TCC-147-reduce-logging
- `b985d53b` **Darius Wattimena** (2025-07-11): Merge pull request #562 from teqplay/TCC-147-reduce-logging
  Reduce log levels when processing is blocked

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-11)

## Pull Request Overview

Implements new behaviors and refactors to improve event and AIS trace processing, lock management, and error handling.

- Added a new unit test for ignoring EOSP end events on unvisited ports and enhanced error logging.
- Refactored ProcessingTraceService to accept `NewEntry`, support updating previous traces, and improved cache access.
- Redesigned `ImoLockService` using `ReentrantLock` per IMO and updated locking logic.

### Reviewed Changes

Copilot reviewed 12 out of 12 changed files in this pull request and generated 1 comment.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/EventProcessingServiceTest.kt | New test for EOSP end-event handling |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/ProcessingTraceService.kt | Refactored to use `NewEntry` and handle previous trace updates |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/ProcessingTraceCacheService.kt | Exposed `getTraceDirectly` for direct DB fetch |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/ProcessingTraceServiceTest.kt | Updated tests to match new method signature |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/ImoLockService.kt | Replaced spin-based lock with per-IMO `ReentrantLock` |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/ImoLockServiceTest.kt | New tests for `ImoLockService` concurrency behaviors |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/PersistChangesService.kt | Added bulk-write error handling and debug logging |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/ProcessingShipStatusService.kt | Introduced `getLatestOngoingEntry` helper |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessor.kt | Added `finally` block to unlock and adjusted log levels |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt | Added error ack, unlock in `finally`, and log‐level tweaks |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageEndProcessor.kt | Added logging for unexpected state and removed unused variable |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/ShipStatusService.kt | Made datasources protected for subclass access |
</details>



<details>
<summary>Comments suppressed due to low confidence (2)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/ProcessingTraceCacheService.kt:17**
* Consider adding unit tests for getTraceDirectly to ensure direct DB fetch behavior is verified.
```
    fun getTraceDirectly(id: EntryId): NewTrace? {
```
**src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/EventProcessingServiceTest.kt:3352**
* The test expects a description that doesn't match the constant END_EVENT_NEW_SHIP_ISSUE used in the processor. Update either the test to use the processor's message or adjust the processor to emit this new description.
```
                    description = "End event received is not for any of the main ports we are currently visiting"
```
</details>

## Review Comments

### Copilot — 2025-07-11 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/ImoLockService.kt`

[nitpick] After unlocking, the lock remains in the imoLocks map, which may lead to unbounded memory growth. Consider removing the lock entry when it is no longer held.
```suggestion
            lock.unlock()
            // Remove the lock from the map if it is no longer held by any thread
            if (!lock.isLocked) {
                imoLocks.remove(imo)
            }
```

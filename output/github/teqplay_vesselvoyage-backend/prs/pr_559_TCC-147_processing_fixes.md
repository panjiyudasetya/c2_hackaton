---
id: github:teqplay/vesselvoyage-backend:pr:559
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 559
title: TCC-147 processing fixes
author: Darius-Wattimena
state: closed
date: '2025-07-07'
merged_at: '2025-07-11'
base_branch: develop
head_branch: TCC-147-processing-fixes
url: https://github.com/teqplay/vesselvoyage-backend/pull/559
labels: []
linked_issues: []
explicit_links: []
---
# PR #559: TCC-147 processing fixes

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/559  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-147-processing-fixes`  
**Created:** 2025-07-07  
**Merged:** 2025-07-11  

## Description

Adjusts the following:
- Covers an extra case of EOSP switching + added logging for a usecase that should be impossible.
- When inserting traces, instead use the last entry instead of full ship state.
- When inserting of traces is behind event processing instead insert the trace in the previous entry if within time range of AIS message.
- Disable V1 logging so we can enable DEBUG logging without seeing V1 issues as it will be disabled soon.

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

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-07)

## Pull Request Overview

This PR enhances event and trace processing by covering additional edge cases in EOSP handling, improving trace insertion logic to account for previous entries, and disabling legacy V1 logging.

- Adds a test and logging for impossible EOSP-switching scenarios.
- Refactors `ProcessingTraceService` to insert AIS points into previous traces within the correct time window.
- Disables V1 processing logs and extends AIS handler to use the new `getLatestOngoingEntry` API.

### Reviewed Changes

Copilot reviewed 9 out of 9 changed files in this pull request and generated 2 comments.

<details>
<summary>Show a summary per file</summary>

| File                                                          | Description                                                             |
| ------------------------------------------------------------- | ----------------------------------------------------------------------- |
| src/test/kotlin/.../EventProcessingServiceTest.kt              | Adds test to ignore EOSP end events without a matching visit           |
| src/main/kotlin/.../ProcessingTraceService.kt                  | Refactors trace insertion to update previous entries when needed       |
| src/test/kotlin/.../ProcessingTraceServiceTest.kt              | Updates tests to use `ongoingEntry` and adds a test for previous trace |
| src/main/kotlin/.../EventsDefaultMessageProcessor.kt           | Passes `logIssues=false` to disable V1 logging                         |
| src/main/kotlin/.../AisStreamingMessageHandler.kt              | Switches to `getLatestOngoingEntry` for trace insertion                |
| src/main/kotlin/.../EndOfSeaPassageEndProcessor.kt             | Adds warning log for impossible EOSP-switching cases                   |
| src/main/kotlin/.../ProcessingShipStatusService.kt             | Introduces `getLatestOngoingEntry` method                              |
</details>



<details>
<summary>Comments suppressed due to low confidence (2)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageEndProcessor.kt:62**
* No tests cover the new warning branch when a completed EOSP activity is detected. Consider adding a unit test to verify the log warning behavior and handling of this case.
```
        if (eospAreaActivities.any { activity -> activity.end != null }) {
```
**src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/EventProcessingServiceTest.kt:3352**
* [nitpick] This error message is slightly inconsistent with the constant END_EVENT_NEW_SHIP_ISSUE. Consider reusing the constant or aligning the message text for consistency.
```
                    description = "End event received is not for any of the main ports we are currently visiting"
```
</details>

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-10)

## Pull Request Overview

This PR refines event and trace processing by handling edge EOSP cases, improving trace insertion logic, and silencing legacy V1 logs to enable clean DEBUG output.

- Adds an EOSP end‐event test to ignore end events for never‐entered ports and logs impossible EOSP switches.
- Refactors `insertIntoCurrentTrace` to use the last entry context, inserting late AIS points into the previous trace when appropriate and updates related tests.
- Disables V1 logging in event processors and enhances bulk‐write error logging with `MongoBulkWriteException` handling.

### Reviewed Changes

Copilot reviewed 12 out of 12 changed files in this pull request and generated 2 comments.

<details>
<summary>Show a summary per file</summary>

| File                                                                                             | Description                                                                           |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| src/test/kotlin/.../EventProcessingServiceTest.kt                                                | New test for ignoring EOSP end events when no port was entered                       |
| src/test/kotlin/.../ProcessingTraceServiceTest.kt                                                | Refactors trace tests to use `ongoingEntry`, adds a test for updating previous trace |
| src/main/kotlin/.../ProcessingTraceService.kt                                                    | Updated `insertIntoCurrentTrace` signature and logic for inserting into previous trace|
| src/main/kotlin/.../ProcessingTraceCacheService.kt                                               | Added `getTraceDirectly` to fetch past traces bypassing cache                         |
| src/main/kotlin/.../EventsDefaultMessageProcessor.kt & AisStreamingMessageHandler.kt              | Unlock IMO after processing and disable old‐definition logging                        |
| src/main/kotlin/.../processing/eosp/EndOfSeaPassageEndProcessor.kt                                | Added logging for impossible EOSP switch and extra validity check                    |
| src/main/kotlin/.../ProcessingShipStatusService.kt & ShipStatusService.kt                        | Exposed data sources and added `getLatestOngoingEntry` for trace context              |
| src/main/kotlin/.../PersistChangesService.kt                                                     | Refactored bulk write error handling, added detailed debug for write failures         |
| src/main/kotlin/.../ImoLockService.kt & ImoLockServiceTest.kt                                     | Replaced spin lock with per‐IMO `ReentrantLock` and updated tests                     |
</details>



<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageEndProcessor.kt:67**
* The original check included `activity.isOngoing()` to ignore only ongoing activities. Removing it means finished activities may now be treated as ongoing, causing valid end events to be ignored. Consider restoring the `isOngoing()` check.
```
            eospAreaActivities.all { activity -> activity.areaId != areaId }
```
</details>

### leonjoosse — DISMISSED (2025-07-10)

_No comment._

### leonjoosse — APPROVED (2025-07-11)

_No comment._

## Review Comments

### Copilot — 2025-07-07 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/ProcessingTraceServiceTest.kt`

Typo in variable name 'previusVoyageEndLocation'. Consider renaming to 'previousVoyageEndLocation' for consistency.
```suggestion
        val previousVoyageEndLocation = Location(-2.0, -2.0)
        val previousVoyageTrace = NewTrace(
            _id = TEST_VOYAGE_ID,
            polyline = Polyline.of(listOf(previousVoyageEndLocation)),
```

### Copilot — 2025-07-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageEndProcessor.kt`

This condition ignores the ongoing status check and may match finished EOSP activities. Consider filtering only ongoing activities (e.g., activity.isOngoing()) to prevent handling completed activities incorrectly.
```suggestion
            eospAreaActivities.filter { it.isOngoing() }.all { activity -> activity.areaId != areaId }
```

### Copilot — 2025-07-10 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PersistChangesService.kt`

In `logDebugBulkWriteIssues`, the code always queries `newEsofDataSource`, even when handling visit or voyage changes. It should use the corresponding datasource for each change type to retrieve the correct records.
```suggestion
        val failedEntries = when (changes.firstOrNull()) {
            is VisitChange -> newVisitDataSource.findByIds(failedIds)
            is VoyageChange -> newVoyageDataSource.findByIds(failedIds)
            is ESoFChange -> newEsofDataSource.findByIds(failedIds)
            else -> {
                log.warn { "Unknown change type. Failed IDs: $failedIds" }
                emptyList()
            }
        }
        log.debug { "Failed IDs: $failedIds" }
        log.debug { "Current in DB: $failedEntries" }
        log.debug { "Attempted to Write: $changes" }
```

### Copilot — 2025-07-10 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/ProcessingTraceServiceTest.kt`

The variable name `previusVoyageEndLocation` is misspelled. Rename it to `previousVoyageEndLocation` for clarity.
```suggestion
        val previousVoyageEndLocation = Location(-2.0, -2.0)
        val previousVoyageTrace = NewTrace(
            _id = TEST_VOYAGE_ID,
            polyline = Polyline.of(listOf(previousVoyageEndLocation)),
```

---
id: github:teqplay/vesselvoyage-backend:pr:581
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 581
title: TCC-287 fix after recalculation
author: Darius-Wattimena
state: closed
date: '2025-07-31'
merged_at: '2025-08-05'
base_branch: develop
head_branch: TCC-287-fix-after-recalculation
url: https://github.com/teqplay/vesselvoyage-backend/pull/581
labels: []
linked_issues: []
explicit_links: []
---
# PR #581: TCC-287 fix after recalculation

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/581  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-287-fix-after-recalculation`  
**Created:** 2025-07-31  
**Merged:** 2025-08-05  

## Description

_No description._

## Commits

- `7f938c2b` **Darius Wattimena** (2025-07-28): Extended story dry running to have the possibility to not calculate drifting
- `43218d15` **Darius Wattimena** (2025-07-28): Added the possibility to repair the ship story after the full recalculation
- `d203591f` **Darius Wattimena** (2025-07-28): Do a full recalculation when we never ran revents for the ship and want to fix the ship story
- `5d779c8a` **Darius Wattimena** (2025-07-29): Schedule post-processing when doing a full story recalculation instead of calculating it on the spot
- `08d20da4` **Darius Wattimena** (2025-07-29): Added tests to ensure the stories are repaired with the expected behaviour and the changes are persisted and published
- `68874e4b` **Darius Wattimena** (2025-07-30): Added more test cases to cover all different type of scenarios that can happen when fixing a ship story
- `baccc632` **Darius Wattimena** (2025-07-30): Cleaned up code and made it so we also schedule a trace regeneration
- `62d9cd42` **Darius Wattimena** (2025-07-30): Added more test cases and make sure we verify that all traces will be scheduled for generation
- `68a468b3` **Darius Wattimena** (2025-07-30): Remove empty file
- `080f91f2` **Darius Wattimena** (2025-07-31): Added an option do ship repair for a batch of ships and run them automatically in the background
- `ced1b897` **Darius Wattimena** (2025-07-31): Adjusted existing tests to work with changes
- `4df406be` **Darius Wattimena** (2025-07-31): Adjusted story repair service so it is testable and it only starts doing things when all other components are ready for processing as well
- `a4401252` **Darius Wattimena** (2025-07-31): code cleanup
- `03410747` **Darius Wattimena** (2025-07-31): code feedback
- `f6e84822` **Darius Wattimena** (2025-07-31): Merge branch 'increase-api-memory' into TCC-287-fix-after-recalculation
- `bf0819e2` **Darius Wattimena** (2025-08-01): Improve documentation and removed some unused code
- `3c96c16d` **Darius Wattimena** (2025-08-01): Update src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/StoryRepairService.kt
  Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com>

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-31)

## Pull Request Overview

This PR implements a story repair service for vessel voyages that fixes broken ship stories after recalculation. The service attempts to repair stories by identifying recalculated entries and merging them with existing data, falling back to full recalculation if repair fails.

Key changes:
- Added new `StoryRepairService` with comprehensive logic for story repair
- Introduced configuration properties and data source for story repair functionality  
- Updated existing services to support optional drifting calculation and post-processing scheduling

### Reviewed Changes

Copilot reviewed 19 out of 20 changed files in this pull request and generated 6 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| `StoryRepairService.kt` | New service implementing the core story repair logic with grouping, merging, and persistence |
| `StoryRepairProperties.kt` | Configuration properties for enabling and configuring story repair |
| `StoryRepairShipDataSource.kt` | Data source for managing ships scheduled for story repair |
| `application.properties` | Added configuration for story repair service in both main and test resources |
| `ManualRecalculationService.kt` | Updated to support post-processing scheduling and exposed helper method |
| `EntryProcessingService.kt` | Added optional parameter to control drifting calculation |
| `PostProcessingService.kt` | Added overload for scheduling multiple entries |
| `ChangesPublisherService.kt` | Updated to handle nullable ship status parameters |
| `ProcessingRecalculateV2Controller.kt` | Added REST endpoints for triggering story repair |
| Various test files | Updated tests to accommodate service changes and added comprehensive test coverage |
</details>



<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/StoryRepairService.kt:139**
* Test method name contains duplicate word 'recalculate'. Should be 'should recalculate story having no dry run entries and no existing data'.
```
        val result = processGroup(
```
</details>

### TeqJoostD — COMMENTED (2025-08-01)

_No comment._

### TeqJoostD — CHANGES_REQUESTED (2025-08-01)

changes have been requested 😢 🙏

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-08-01)

## Pull Request Overview

This PR implements a story repair functionality (TCC-287) that provides a mechanism to repair broken ship stories by recalculating with EventHistory. The implementation adds a new service to identify and fix inconsistencies in vessel voyage data through targeted recalculation instead of full story recreation.

- Introduces `StoryRepairService` with threading support for concurrent repairs
- Adds story repair configuration properties and data source for tracking repair jobs
- Extends existing recalculation services to support the new repair workflow

### Reviewed Changes

Copilot reviewed 19 out of 20 changed files in this pull request and generated 2 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/StoryRepairService.kt` | Core service implementing story repair logic with sophisticated entry grouping and merging |
| `src/main/kotlin/nl/teqplay/vesselvoyage/properties/StoryRepairProperties.kt` | Configuration properties for enabling story repair and setting thread pool size |
| `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/StoryRepairShipDataSource.kt` | Data source for tracking ships scheduled for story repair |
| `src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingRecalculateV2Controller.kt` | REST endpoints for triggering story repair operations |
| `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ManualRecalculationService.kt` | Updated to support post-processing and new dry run parameters |
| `src/main/kotlin/nl/teqplay/vesselvoyage/service/EntryProcessingService.kt` | Added optional drifting calculation parameter for dry run processing |
| `src/main/kotlin/nl/teqplay/vesselvoyage/service/publisher/ChangesPublisherService.kt` | Enhanced to handle nullable ship status parameters |
| `src/test/kotlin/nl/teqplay/vesselvoyage/service/recalculation/StoryRepairRecalculationServiceTest.kt` | Comprehensive test suite covering various repair scenarios |
</details>



<details>
<summary>Comments suppressed due to low confidence (6)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/StoryRepairService.kt:570**
* [nitpick] The variable name 'zeroSecondVoyage' could be more descriptive. Consider renaming to something like 'syntheticConnectingVoyage' or 'bridgeVoyage' to better convey its purpose as a connecting element between entries.
```
                val zeroSecondVoyage = NewVoyage(
```
**src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/StoryRepairService.kt:610**
* [nitpick] The variable name 'zeroSecondVoyage' could be more descriptive. Consider renaming to something like 'syntheticConnectingVoyage' or 'bridgeVoyage' to better convey its purpose as a connecting element between entries.
```
                val zeroSecondVoyage = NewVoyage(
```
**src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/StoryRepairService.kt:458**
* The variable name 'blowUpDuration' is unclear and could be misinterpreted. Consider renaming to 'searchBufferDuration' or 'timeRangeExtension' to better convey its purpose.
```
        val blowUpDuration = Duration.ofMinutes(1)
```
**src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/StoryRepairService.kt:459**
* The variable name 'blownUpStart' is unclear and could be misinterpreted. Consider renaming to 'adjustedStartTime' or 'extendedStartTime' to better convey its purpose.
```
        val blownUpStart = maxOf(start.minus(blowUpDuration), attachingVoyage.start.time)
```
**src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/StoryRepairService.kt:464**
* Using 'blownUpStart' in the context of 'end = blownUpStart' is confusing as it suggests the end time is set to a start time. The variable name should be clearer about its adjusted nature.
```
            imo = imo,
```
**src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/StoryRepairService.kt:493**
* The variable 'blownUpStart' should be renamed consistently throughout the method to improve code clarity.
```
            start = blownUpStart,
```
</details>

### TeqJoostD — APPROVED (2025-08-05)

_No comment._

## Review Comments

### Copilot — 2025-07-31 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/recalculation/StoryRepairRecalculationServiceTest.kt`

Test method name contains duplicate word 'recalculate'. Should be 'should recalculate story having visit after attaching voyage and no existing data'.
```suggestion
    fun `should recalculate story having visit after attaching voyage and no existing data`() {
```

### Copilot — 2025-07-31 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/recalculation/StoryRepairRecalculationServiceTest.kt`

Test method name contains duplicate word 'recalculate'. Should be 'should recalculate story having visit after attaching voyage and delete existing data'.
```suggestion
    fun `should recalculate story having visit after attaching voyage and delete existing data`() {
```

### Copilot — 2025-07-31 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/recalculation/StoryRepairRecalculationServiceTest.kt`

Test method name contains duplicate word 'recalculate'. Should be 'should recalculate story having visit before attaching voyage and no existing data'.
```suggestion
    fun `should recalculate story having visit before attaching voyage and no existing data`() {
```

### Copilot — 2025-07-31 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/recalculation/StoryRepairRecalculationServiceTest.kt`

Test method name contains duplicate word 'recalculate'. Should be 'should recalculate story having visit before attaching voyage and delete existing data'.
```suggestion
    fun `should recalculate story having visit before attaching voyage and delete existing data`() {
```

### Copilot — 2025-07-31 on `src/main/kotlin/nl/teqplay/vesselvoyage/properties/StoryRepairProperties.kt`

Grammar error in comment. Should be 'The total amount of ships we can repair at the same time' or 'The total number of ships we can repair simultaneously'.
```suggestion
     * The total number of ships we can repair simultaneously.
```

### Copilot — 2025-07-31 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingRecalculateV2Controller.kt`

Missing @PreAuthorize annotation for security. This endpoint should have the same authorization as other recalculation endpoints.
```suggestion
    @PostMapping("/ship/repairStory/batch")
    @PreAuthorize("hasPermission(null,'${Resource.RECALCULATION}:${Operation.CREATE}')")
```

### TeqJoostD — 2025-08-01 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/StoryRepairShipDataSource.kt`

This is not implemented :(

### Copilot — 2025-08-01 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/StoryRepairService.kt`

The word 'revents' appears to be a typo. It should likely be 'events'.
```suggestion
 * A story can be repaired if any of the ship entries have been recalculated by events before.
```

### Copilot — 2025-08-01 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/StoryRepairService.kt`

The phrase 'searching events in not inclusive' has grammatical errors. It should be 'searching events is not inclusive'.
```suggestion
        // Blow up the start time a bit as searching events is not inclusive, meaning we need to extend the time range a bit
```

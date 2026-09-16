---
id: github:teqplay/vesselvoyage-backend:pr:635
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 635
title: TCC-341 Remove V1
author: Darius-Wattimena
state: closed
date: '2025-10-13'
merged_at: null
base_branch: develop
head_branch: TCC-341
url: https://github.com/teqplay/vesselvoyage-backend/pull/635
labels: []
linked_issues: []
explicit_links: []
---
# PR #635: TCC-341 Remove V1

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/635  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-341`  
**Created:** 2025-10-13  

## Description

_No description._

## Commits

- `ae534a34` **Darius Wattimena** (2025-09-02): WIP removing V1
- `09c88dce` **Darius Wattimena** (2025-09-15): Remove more VesselVoyage V1 code that isn't used anymore
- `42b84686` **Darius Wattimena** (2025-09-15): Updated SOF controller to make use of a custom validator to only allow valid visit IDs
- `81a8f6ba` **Darius Wattimena** (2025-10-09): Merge branch 'develop' into TCC-341
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiEntryController.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiPortController.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiShipController.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiTraceController.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVisitController.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageController.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingEventController.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingShipController.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingUserController.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingVisitController.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingVoyageController.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/properties/TraceProperties.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/EntryProcessingService.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/ProcessingService.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/SlowMovingService.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/api/EntryV2Service.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/EventProcessor.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/anchor/AnchorEndProcessor.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/encounter/EncounterBaseProcessor.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eta/EtaProcessor.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/movement/MovementEndProcessor.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/movement/MovementStartProcessor.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/status/StatusChangedProcessor.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessor.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationService.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/util/dateTimeUtils.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/util/entryUtils.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/util/esofUtils.kt
  #	src/main/resources/application.properties
- `37132834` **Darius Wattimena** (2025-10-13): Update aisengine models to snapshot version
- `24e3a705` **Darius Wattimena** (2025-10-13): Removed a bunch of existing warnings
- `baebe309` **Darius Wattimena** (2025-10-13): Merge branch 'develop' into TCC-341
  # Conflicts:
  #	build.gradle
- `6f5cc8b0` **Darius Wattimena** (2025-10-13): Lots of code cleanup + remove V1 tests
- `6c3e63b9` **Darius Wattimena** (2025-10-13): More clean up
- `6f7e5dc5` **Darius Wattimena** (2025-10-13): Remove unused imports and fix test mock return value

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-13)

## Pull Request Overview

This PR removes the V1 event processing implementation as part of the "TCC-341 Remove V1" initiative. The changes clean up legacy code paths, test files, and configuration while maintaining only the V2 implementation.

- Removes all V1-specific test classes and their associated test methods
- Cleans up configuration properties and validation utilities related to V1
- Updates service implementations to use only V2 processing paths
- Removes deprecated utility functions and model converters

### Reviewed Changes

Copilot reviewed 215 out of 284 changed files in this pull request and generated 2 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| Test files | Complete removal of V1 event processing test classes |
| Application properties | Removal of V1-specific configuration properties |
| Validation utils | Addition of new validation classes and removal of legacy utilities |
| Service implementations | Updates to remove V1 processing paths and dependencies |
| Utility classes | Cleanup of deprecated V1 utility functions and conversions |
</details>

### TeqJoostD — COMMENTED (2025-10-14)

_No comment._

### TeqJoostD — COMMENTED (2025-10-14)

_No comment._

### TeqJoostD — COMMENTED (2025-10-14)

_No comment._

### TeqJoostD — COMMENTED (2025-10-14)

_No comment._

### TeqJoostD — COMMENTED (2025-10-14)

_No comment._

### TeqJoostD — CHANGES_REQUESTED (2025-10-14)

small feedback

## Review Comments

### Copilot — 2025-10-13 on `src/test/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingV2EventControllerTest.kt`

Ensure test coverage includes verification that the V2 method is called correctly with the expected parameters and returns the mocked empty list.

### Copilot — 2025-10-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/TraceService.kt`

The class declaration removed the `open` modifier. Ensure this change doesn't break any existing inheritance relationships or test mocking scenarios that depend on the class being open.
```suggestion
open class TraceService(
```

### TeqJoostD — 2025-10-14 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/model/ReventsRecalculationStatus.kt`

Why not remove?

### TeqJoostD — 2025-10-14 on `api/build.gradle`

please create stable BUILD

### TeqJoostD — 2025-10-14 on `src/main/kotlin/nl/teqplay/vesselvoyage/config/PomaRestTemplateConfiguration.kt`

keycloakProperties.enabled?.let {}

Or is that not better

### TeqJoostD — 2025-10-14 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/ProcessingFrontendViewV2Service.kt`

dit is vies

### TeqJoostD — 2025-10-14 on `build.gradle`

Same here

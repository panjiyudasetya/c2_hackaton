---
id: github:teqplay/vesselvoyage-backend:pr:519
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 519
title: SPV-1948 Change VV models to AisEngine models
author: TeqJoostD
state: closed
date: '2025-05-28'
merged_at: '2025-07-03'
base_branch: develop
head_branch: SPV-1948
url: https://github.com/teqplay/vesselvoyage-backend/pull/519
labels: []
linked_issues: []
explicit_links: []
---
# PR #519: SPV-1948 Change VV models to AisEngine models

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/519  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `SPV-1948`  
**Created:** 2025-05-28  
**Merged:** 2025-07-03  

## Description

_No description._

## Commits

- `616c8334` **TeqJoostD** (2025-05-28): refactor: update event imports and deprecate old event types
- `0bf58932` **TeqJoostD** (2025-05-28): delete todo
- `de896ef4` **Darius Wattimena** (2025-05-28): Fix broken dependency loading
- `88de5814` **TeqJoostD** (2025-06-10): fix: merge conflicts
  fix: failing tests
  fix: apply feedback from PR session
- `e58105f4` **TeqJoostD** (2025-06-24): fix: resolve feedback
- `4d2afe78` **TeqJoostD** (2025-06-27): Merge branch 'develop' into SPV-1948
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGenerator.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/ActivityEventProcessor.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessor.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/util/entryUtils.kt
  #	src/test/kotlin/nl/teqplay/vesselvoyage/util/EntryUtilsTest.kt
- `e987a5f6` **TeqJoostD** (2025-06-27): fix merge conflicts
- `5ab0ef7e` **Joost Dambrink** (2025-07-02): Merge branch 'develop' into SPV-1948

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-05-28)

## Pull Request Overview

This PR (SPV-1948) removes several legacy event classes and interfaces while updating import references and adding a new dependency for the AisEngine models.  
- Removed obsolete event implementations including StatusChangedEvent, StartEndEvent, and related classes.  
- Updated Encounter and EncounterType imports to point to the new AisEngine package.  
- Added an implementation dependency for the AisEngine models in the build file.

### Reviewed Changes

Copilot reviewed 135 out of 135 changed files in this pull request and generated no comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/model/event/StatusChangedEvent.kt | Entire file removed (legacy event class) |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/model/event/StartEndEvent.kt | Entire file removed (legacy interface) |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/model/event/ShipToShipTransferEvent.kt | Entire file removed (legacy event class) |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/model/event/PortEvent.kt | Entire file removed (legacy event class) |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/model/event/PilotAreaEvent.kt | Entire file removed (legacy event class) |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/model/event/MovementEvent.kt | Entire file removed (legacy event class) |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/model/event/LockAreaEvent.kt | Entire file removed (legacy event class) |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/model/event/LocationBasedEvent.kt | Entire file removed (legacy event interface) |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/model/event/Event.kt | Entire file removed (core event definition) |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/model/event/EtaEvent.kt | Entire file removed (legacy event class) |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/model/event/EndOfSeaPassageEvent.kt | Entire file removed (legacy event class) |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/model/event/EncounterType.kt | Added deprecation annotation referencing the AisEngine EncounterType |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/model/event/EncounterEvent.kt | Entire file removed (legacy event class) |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/model/event/DestinationChangedEvent.kt | Entire file removed (legacy event class) |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/model/event/ApproachAreaEvent.kt | Entire file removed (legacy event class) |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/model/event/AnchorEvent.kt | Entire file removed (legacy event class) |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/model/event/AnchorAreaEvent.kt | Entire file removed (legacy event class) |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/model/Encounter.kt | Updated import to reference AisEngine EncounterType |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/Encounter.kt | Updated import to reference AisEngine EncounterType |
| api/build.gradle | Added dependency for nl.teqplay.aisengine:models and updated aisengine_version |
</details>



<details>
<summary>Comments suppressed due to low confidence (3)</summary>

**api/build.gradle:4**
* Ensure that the version tagging ('master-2.0.1') for the AisEngine models dependency meets your project's stability and upgrade policy requirements.
```
aisengine_version = "master-2.0.1"
```
**api/src/main/kotlin/nl/teqplay/vesselvoyage/model/event/EncounterType.kt:3**
* Confirm that the deprecation message clearly guides consumers to use the new EncounterType from AisEngine and that relevant documentation is updated accordingly.
```
@Deprecated("Use EncounterType from AisEngine instead")
```
**api/src/main/kotlin/nl/teqplay/vesselvoyage/model/Encounter.kt:3**
* Verify that updating the import for EncounterType consistently propagates throughout dependent modules to prevent potential mismatches with the new AisEngine types.
```
import nl.teqplay.aisengine.event.interfaces.EncounterEvent.EncounterType
```
</details>

### TeqJoostD — COMMENTED (2025-06-06)

_No comment._

### TeqJoostD — COMMENTED (2025-06-06)

_No comment._

### TeqJoostD — COMMENTED (2025-06-06)

_No comment._

### TeqJoostD — COMMENTED (2025-06-06)

_No comment._

### TeqJoostD — COMMENTED (2025-06-06)

_No comment._

### TeqJoostD — COMMENTED (2025-06-06)

_No comment._

### TeqJoostD — COMMENTED (2025-06-06)

_No comment._

### Darius-Wattimena — CHANGES_REQUESTED (2025-06-24)

_No comment._

### Darius-Wattimena — APPROVED (2025-07-02)

_No comment._

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-02)

## Pull Request Overview

This PR migrates existing VesselVoyage test fixtures and test code to use the new `AisEngine` event model types and updated JSON schema.

- Updated JSON fixtures to match the new field names and nested structures expected by `AisEngine` models.
- Replaced all uses of old `vesselvoyage.model.event.*` classes in tests with `nl.teqplay.aisengine.event.model` and `nl.teqplay.aisengine.event.interfaces` types.
- Refactored test‐utility functions (`helperFunctions.kt`, `TestUtil.kt`, etc.) to construct new `AreaStartEvent`, `AreaEndEvent`, `AnchoredEvent`, and other `AisEngine` event instances.

### Reviewed Changes

Copilot reviewed 139 out of 139 changed files in this pull request and generated no comments.

<details>
<summary>Show a summary per file</summary>

| File                                                                      | Description                                                     |
|---------------------------------------------------------------------------|-----------------------------------------------------------------|
| src/test/resources/events/eventbuffer-removal-events.json                 | Updated fixture JSON schema (field renames, nested ship/area)  |
| src/test/kotlin/nl/teqplay/vesselvoyage/util/TestUtil.kt                  | Swapped old event imports for `AisEngine` interfaces           |
| src/test/kotlin/nl/teqplay/vesselvoyage/util/EventUtilsTest.kt            | Removed legacy conversion tests                                |
| src/test/kotlin/nl/teqplay/vesselvoyage/util/EntryUtilsTest.kt            | Updated `updateMatchingPortAreaVisit` calls with new signature  |
| src/test/kotlin/nl/teqplay/vesselvoyage/logic/helperFunctions.kt          | Rewrote factories to produce `AisEngine` event model objects   |
| [many other test files under `src/test/kotlin/...`]                        | Replaced old event types/imports with `AisEngine` equivalents  |
</details>



<details>
<summary>Comments suppressed due to low confidence (1)</summary>


</details>

## Review Comments

### TeqJoostD — 2025-06-06 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/model/event/EncounterType.kt`

Database migration needed for this.

Add json alias to old model and do database migration after that.

### TeqJoostD — 2025-06-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/logic/EventTypeValidator.kt`

Reference to enum instead of this

### TeqJoostD — 2025-06-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/ActivityEventProcessor.kt`

Parse T instead of LocationBasedEvent

### TeqJoostD — 2025-06-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/ESofEventProcessor.kt`

Check if Event is also possible as T

### TeqJoostD — 2025-06-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/util/aisEngineEventUtils.kt`

Actual time is not set to predictedTime

### TeqJoostD — 2025-06-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/EventUtil.kt`

Reduce to is ActualEvent -> actualTime
else -> createdTime (not nullable)

### TeqJoostD — 2025-06-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/EventUtil.kt`

Check if this is needed? Or if we can do this in the logic itself

### Darius-Wattimena — 2025-06-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/movement/MovementStartProcessor.kt`

Can just call `event.actualTime` here directly?

### Darius-Wattimena — 2025-06-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/EventProcessingService.kt`

Might be nicer to not have all of this in a single line?

### Darius-Wattimena — 2025-06-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/EventProcessingService.kt`

Would change the description so we know this "type" of prediction isn't supported

### Darius-Wattimena — 2025-06-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/EventProcessingService.kt`

Same here, would be nice to include that this kind of area event isn't supported

### Darius-Wattimena — 2025-06-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/EventUtil.kt`

Would be nice to add some comment here why we first take the `actualTime` and otherwise the `createdTime` for events that don't have a time (e.g. predictions)

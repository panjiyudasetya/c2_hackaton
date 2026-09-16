---
id: github:teqplay/vesselvoyage-backend:pr:607
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 607
title: TCC-360 add the ability to measure vesselVoyage
author: Jamie-de-Leest
state: closed
date: '2025-09-16'
merged_at: '2025-09-29'
base_branch: develop
head_branch: TCC-360-Add-the-ability-to-measure-VesselVoyage
url: https://github.com/teqplay/vesselvoyage-backend/pull/607
labels: []
linked_issues: []
explicit_links: []
---
# PR #607: TCC-360 add the ability to measure vesselVoyage

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/607  
**State:** closed | **Author:** Jamie-de-Leest  
**Base ← Head:** `develop` ← `TCC-360-Add-the-ability-to-measure-VesselVoyage`  
**Created:** 2025-09-16  
**Merged:** 2025-09-29  

## Description

_No description._

## Commits

- `a446b03a` **Jamie de Leest** (2025-09-11): feat: implement measuring for Merge and PostProcessing
- `1f015be9` **Jamie de Leest** (2025-09-11): feat: add ApplicationEventPublisher mock to ReventsRecalculationServiceTest
- `454bf519` **Jamie de Leest** (2025-09-12): chore: fix typo
- `0b7b7e3e` **Jamie de Leest** (2025-09-12): test: create tests for the MeasuringService.kt and Event Publishing
- `8ff836de` **Jamie de Leest** (2025-09-15): Merge branch 'develop' into TCC-360-Add-the-ability-to-measure-VesselVoyage
- `f8c19fbe` **Jamie de Leest** (2025-09-15): fix: use save instead of insert
- `891f698b` **Jamie de Leest** (2025-09-15): chore: ktlint
- `a4a53233` **Jamie de Leest** (2025-09-15): test: fix tests to with try catch change
- `cac8c8bc` **Jamie de Leest** (2025-09-16): fix: fix typo
- `5ce58d00` **Jamie de Leest** (2025-09-17): feat: add scenarioId to post-processing events
- `38abbfb6` **Jamie de Leest** (2025-09-17): tests: fixing tests
- `c3975c95` **Jamie de Leest** (2025-09-17): feat: add more concurrency locking
- `d85451d7` **Jamie de Leest** (2025-09-17): Merge branch 'develop' into TCC-360-Add-the-ability-to-measure-VesselVoyage
- `7783bf04` **Jamie de Leest** (2025-09-24): fix: update endPostProcessedTime logic in MeasuringService
- `cb83d69d` **Jamie de Leest** (2025-09-26): Merge branch 'develop' into TCC-360-Add-the-ability-to-measure-VesselVoyage

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-09-16)

## Pull Request Overview

This PR adds the ability to measure vessel voyage processing times by implementing an event-driven measuring system. The implementation tracks the duration of merge operations and post-processing tasks for vessel voyage scenarios.

Key changes include:
- Implementation of a new MeasuringService that listens to Spring application events to track merge and post-processing timing
- Creation of Spring events (StartMergeEvent, EndMergeEvent, StartPostProcessingEvent, EndPostProcessingEvent) to signal the beginning and end of various processing phases
- Integration of event publishing into existing services (ReventsRecalculationService and PostProcessingService)

### Reviewed Changes

Copilot reviewed 11 out of 11 changed files in this pull request and generated 1 comment.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/MeasuringService.kt | New service that handles timing measurements by listening to processing events |
| src/main/kotlin/nl/teqplay/vesselvoyage/datasource/ScenarioMeasurementDataSource.kt | New data source for persisting scenario measurement data |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/ScenarioMeasurement.kt | New data model for storing scenario timing measurements |
| src/main/kotlin/nl/teqplay/vesselvoyage/spring/*.kt | New Spring event classes for tracking processing lifecycle |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationService.kt | Updated to publish merge and post-processing events |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt | Updated to publish end post-processing events |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/MeasuringServiceTest.kt | Comprehensive test suite for the new measuring service |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationServiceTest.kt | Updated tests to include event publisher mock and verification |
</details>

### michel-teqplay — DISMISSED (2025-09-17)

_No comment._

### michel-teqplay — DISMISSED (2025-09-23)

_No comment._

### Jamie-de-Leest — COMMENTED (2025-09-23)

_No comment._

### Darius-Wattimena — CHANGES_REQUESTED (2025-09-23)

Please fix the 1 line we discussed :)

### Darius-Wattimena — APPROVED (2025-09-24)

_No comment._

## Review Comments

### Copilot — 2025-09-16 on `src/main/kotlin/nl/teqplay/vesselvoyage/spring/EndPostProcessingEvent.kt`

The property name 'entyId' contains a typo. It should be 'entryId' to maintain consistency with naming conventions.
```suggestion
class EndPostProcessingEvent(source: Any, val entryId: String) : ApplicationEvent(source)
```

### Jamie-de-Leest — 2025-09-23 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/MeasuringService.kt`

```suggestion
                        updatedRunning.isEmpty()
```

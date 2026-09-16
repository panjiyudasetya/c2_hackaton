---
id: github:teqplay/vesselvoyage-backend:pr:509
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 509
title: 'SPV-2619: Trace api and client'
author: leonjoosse
state: closed
date: '2025-05-21'
merged_at: '2025-05-23'
base_branch: develop
head_branch: SPV-2619-trace-api-and-client
url: https://github.com/teqplay/vesselvoyage-backend/pull/509
labels: []
linked_issues: []
explicit_links: []
---
# PR #509: SPV-2619: Trace api and client

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/509  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `SPV-2619-trace-api-and-client`  
**Created:** 2025-05-21  
**Merged:** 2025-05-23  

## Description

Move trace stuff from `processing` only to both `processing+api`.
When called with `@ProfileApi` enabled, only returns item(s) from the database
When called with `@ProfileProcessing` enabled, returns the item from the database and triggers a background fetch of the trace if it does not exist.

The controller is moved to a different class: `ProcessingV2TraceController -> ApiTraceV2Controller`

## Commits

- `13a9e341` **leonj** (2025-05-21): Add methods to retrieve multiple traces by entry ids
- `ea7fa81f` **leonj** (2025-05-21): Move Trace endpoints from the PROCESSING to API, so it can be returned through the api, and used by the client

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-05-21)

## Pull Request Overview

This PR refactors trace retrieval to support both API and processing profiles by moving the processing controller into a unified API controller, introducing an API‐only service, and extending batch support.

- Moved and renamed the processing controller to `ApiTraceV2Controller` with conditional logic based on profiles.
- Added `TraceV2Service` for API‐only trace lookup and enhanced `ProcessingTraceService` to batch‐fetch and schedule missing traces.
- Updated models, mapper, data source, client, and tests to align with the new controller and data types.

### Reviewed Changes

Copilot reviewed 10 out of 10 changed files in this pull request and generated 3 comments.

<details>
<summary>Show a summary per file</summary>

| File                                                           | Description                                                      |
| -------------------------------------------------------------- | ---------------------------------------------------------------- |
| src/test/kotlin/.../ProcessingV2TraceControllerTest.kt         | Switched test to use `ApiTraceV2Controller` and `apiv2.model.Trace` |
| src/main/kotlin/.../service/trace/ProcessingTraceService.kt    | Added `getTracesByIds` with scheduling and updated docs         |
| src/main/kotlin/.../service/api/TraceV2Service.kt              | New service for API‐only trace lookups                          |
| src/main/kotlin/.../model/ApiTrace.kt                          | Removed legacy `ApiTrace` model                                 |
| src/main/kotlin/.../mapper/TraceMapper.kt                      | Updated import alias and added doc for `combinePolyline`        |
| src/main/kotlin/.../datasource/NewTraceDataSource.kt           | Added `findByIds` batch query                                   |
| src/main/kotlin/.../controller/api/ApiTraceV2Controller.kt     | New controller combining API and processing behaviors           |
| client/src/.../VesselVoyageClient.kt                           | Added `Traces` subclient for trace endpoints                    |
| api/src/.../apiv2/model/Trace.kt                               | Expanded `Trace` model with new fields and documentation        |
</details>



<details>
<summary>Comments suppressed due to low confidence (2)</summary>

**src/test/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingV2TraceControllerTest.kt:33**
* The test class is still named `ProcessingV2TraceControllerTest` but now targets `ApiTraceV2Controller`. Rename the test class (and file) to `ApiTraceV2ControllerTest` for clarity.
```
class ProcessingV2TraceControllerTest(
```
**src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiTraceV2Controller.kt:46**
* [nitpick] The method `findEntryId` returns a `Trace`. Rename it to `findTraceByEntryId` or `getTrace` to better convey its purpose.
```
fun findEntryId(
```
</details>

### Darius-Wattimena — DISMISSED (2025-05-22)

_No comment._

### Darius-Wattimena — APPROVED (2025-05-22)

_No comment._

## Review Comments

### Copilot — 2025-05-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/ProcessingTraceService.kt`

When scheduling missing traces, existing traces are discarded by returning an empty list. Consider returning the fetched `result` and scheduling only for the missing IDs to avoid dropping valid data.
```suggestion
            // Schedule the missing traces to be calculated
            scheduleTraceCalculation(missingIds, force = true)
```

### Copilot — 2025-05-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/ProcessingTraceService.kt`

The KDoc for this method says 'Get the trace by ID' but it actually fetches multiple traces. Update the comment to reflect batch behavior.
```suggestion
     * Get multiple traces by their IDs and optionally generate them in the background so next time they are needed, they are generated.
     * If any traces are missing, they will be scheduled for generation, and an empty list will be returned.
```

### Copilot — 2025-05-21 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/Trace.kt`

The `distanceMeters` property lacks a KDoc comment. Add a brief description to explain its units and edge cases (e.g., null when insufficient data).
```suggestion

    /**
     * Total distance covered during this trace, in meters. Null if there is insufficient data to calculate the distance.
     */
```

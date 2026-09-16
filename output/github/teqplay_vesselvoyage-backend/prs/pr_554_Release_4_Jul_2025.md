---
id: github:teqplay/vesselvoyage-backend:pr:554
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 554
title: Release 4 Jul 2025
author: Darius-Wattimena
state: closed
date: '2025-07-04'
merged_at: '2025-07-04'
base_branch: master
head_branch: master-with-trace-changes
url: https://github.com/teqplay/vesselvoyage-backend/pull/554
labels: []
linked_issues: []
explicit_links: []
---
# PR #554: Release 4 Jul 2025

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/554  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `master-with-trace-changes`  
**Created:** 2025-07-04  
**Merged:** 2025-07-04  

## Description

_No description._

## Commits

- `f62938b3` **Darius Wattimena** (2025-07-04): Cherry pick trace changes

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-04)

## Pull Request Overview

This PR replaces the old `TraceService` with a deprecated `V1TraceService` for processing flows, adds a new consolidated `TraceService` for API usage (including a non-blocking/blocking trace fetch), and refactors the `ProcessingTraceService` to extend the new API service. It also updates client code to support the new blocking parameter and adjusts tests accordingly.

- Swapped out `TraceService` references for `V1TraceService` in processing & test code  
- Introduced a new `TraceService` for API profile with `blocking` support and de-duplicated logic  
- Updated `VesselVoyageClient` to handle 404 as `null` and pass the `blocking` query parameter

### Reviewed Changes

Copilot reviewed 22 out of 22 changed files in this pull request and generated no comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/main/kotlin/.../service/trace/TraceService.kt | New API-facing service with background scheduling and blocking option |
| src/main/kotlin/.../service/V1TraceService.kt | Renamed legacy service with deprecation annotation |
| src/main/kotlin/.../service/trace/ProcessingTraceService.kt | Refactored to inherit from new API service and removed duplicate logic |
| client/src/main/kotlin/.../VesselVoyageClient.kt | Extended client to catch 404s and forward `blocking` param |
| src/main/kotlin/.../controller/api/ApiTraceV2Controller.kt | Updated controller to call new service and accept `blocking` |
| tests in src/test/kotlin/... | Renamed mocks and updated constructor params to use `v1TraceService` |
</details>



<details>
<summary>Comments suppressed due to low confidence (4)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiTraceV2Controller.kt:44**
* Add a unit test for `ApiTraceV2Controller` to verify that the `blocking` query parameter correctly toggles between immediate (blocking) trace retrieval and background scheduling behavior.
```
        @RequestParam(defaultValue = "false") blocking: Boolean
```
**client/src/main/kotlin/nl/teqplay/vesselvoyage/client/VesselVoyageClient.kt:576**
* Add integration or unit tests for the new `Traces.findById(id, blocking)` and `findByIds(ids, blocking)` methods to ensure the `blocking` parameter is correctly serialized into the HTTP request and that 404 responses return `null` as intended.
```
    class Traces(
```
**src/main/kotlin/nl/teqplay/vesselvoyage/service/StoryService.kt:40**
* Update the KDoc for `getStory` to remove references to the now-removed `forceTraces` parameter and explain the new behavior when `end` is provided without forcing trace regeneration.
```
        end: Instant?
```
**src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/TraceSimplifyService.kt:13**
* [nitpick] Having both `@ProfileProcessing` and `@ProfileApi` on the same service may register it under both contexts; consider separating the processing and API beans or documenting the intended overlap to avoid confusion.
```
@ProfileApi
```
</details>

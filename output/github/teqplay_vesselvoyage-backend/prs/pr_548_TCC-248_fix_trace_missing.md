---
id: github:teqplay/vesselvoyage-backend:pr:548
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 548
title: TCC-248 fix trace missing
author: Darius-Wattimena
state: closed
date: '2025-07-03'
merged_at: '2025-07-04'
base_branch: develop
head_branch: TCC-248-fix-trace-missing
url: https://github.com/teqplay/vesselvoyage-backend/pull/548
labels: []
linked_issues: []
explicit_links: []
---
# PR #548: TCC-248 fix trace missing

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/548  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-248-fix-trace-missing`  
**Created:** 2025-07-03  
**Merged:** 2025-07-04  

## Description

- VesselVoyage trace API endpoints now include a `blocking` option, so instead of scheduling the trace they will be blocked until we have them.
- Client also includes this `blocking` field.

## Commits

- `f7e978f3` **Darius Wattimena** (2025-07-02): Adjusted getting of the trace to be always being scheduled on both API and processing + added a blocking argument to ensure you always get a trace
- `2a6ba78a` **Darius Wattimena** (2025-07-02): Fix an issue where the TraceService bean wouldn't be loaded in and renamed the old TraceService so they don't clash with naming
- `7aa78113` **Darius Wattimena** (2025-07-03): Fix existing StoryService tests and removed unused parameter for trace generation
- `a699e675` **Darius Wattimena** (2025-07-03): Fix incorrectly mocked trace service and adjusted test name to match controller name
- `773a505c` **Darius Wattimena** (2025-07-03): ktlint
- `98ce2760` **Darius Wattimena** (2025-07-03): copilot feedback
- `a8bff051` **Darius Wattimena** (2025-07-03): Merge branch 'develop' into TCC-248-fix-trace-missing
- `79a04eb3` **Darius Wattimena** (2025-07-03): Merge branch 'develop' into TCC-248-fix-trace-missing
- `3d5e0043` **Darius Wattimena** (2025-07-03): PR feedback
- `ced28f48` **Darius Wattimena** (2025-07-03): ktlint

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-03)

## Pull Request Overview

This PR replaces the old `TraceService` with a new API‐focused `TraceService` (supporting blocking vs. background trace generation), renames the legacy implementation to `V1TraceService`, and migrates all callers and tests accordingly.

- Introduce `TraceService` under `service.trace` with a `blocking` flag and deprecate the old service as `V1TraceService`
- Update controllers, the client, and service implementations to inject and use `V1TraceService` or the new `TraceService`
- Adjust tests and mocks to match the renamed classes and updated method signatures

### Reviewed Changes

Copilot reviewed 22 out of 22 changed files in this pull request and generated 1 comment.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/test/kotlin/.../ReventsRecalculationServiceTest.kt | Swapped `TraceService` → `V1TraceService` import and mock |
| src/test/kotlin/.../EventProcessingScenarioTest.kt | Replaced `traceService` mock with `v1TraceService` |
| src/test/kotlin/.../TraceServiceTest.kt | Updated mock wrapper and constructor to use `V1TraceService` |
| src/test/kotlin/.../StoryServiceTest.kt | Adjusted `getTraceById` and `getStory` calls to new signatures |
| src/test/kotlin/.../ProcessingTraceServiceTest.kt | Renamed `ProcessingTraceSimplifyService` import to `TraceSimplifyService` |
| src/test/kotlin/.../EntryServiceTest.kt | Replaced verify calls from `traceService` to `v1TraceService` |
| src/test/kotlin/.../EntryProcessingServiceTest.kt | Replaced mock `traceService` with `v1TraceService` |
| src/test/kotlin/.../ApiTraceV2ControllerTest.kt | Updated package, imports, class name, and mock signature for new `getTraceById` |
| src/main/kotlin/.../trace/TraceSimplifyService.kt | Renamed class, added `@ProfileApi` |
| src/main/kotlin/.../trace/TraceService.kt | Added new API trace service implementation |
| src/main/kotlin/.../trace/ProcessingTraceService.kt | Refactored to extend new `TraceService` and removed duplicated scheduling logic |
| src/main/kotlin/.../recalculation/ReventsRecalculationService.kt | Swapped `TraceService` → `V1TraceService` dependency and calls |
| src/main/kotlin/.../queue/AisStreamingMessageHandler.kt | Swapped `TraceService` → `V1TraceService` |
| src/main/kotlin/.../service/api/TraceV2Service.kt | Removed obsolete `TraceV2Service` |
| src/main/kotlin/.../service/V1TraceService.kt | Renamed and deprecated old `TraceService` to `V1TraceService` |
| src/main/kotlin/.../StoryService.kt | Removed `forceTraces` parameter from `getStory` |
| src/main/kotlin/.../ProcessingService.kt | Swapped `traceService?.shutdown()` → `v1TraceService?.shutdown()` |
| src/main/kotlin/.../EntryProcessingService.kt | Replaced `traceService` calls with `v1TraceService` |
| src/main/kotlin/.../controller/processing/ProcessingStoryController.kt | Removed `forceTraces` param in endpoint |
| src/main/kotlin/.../controller/api/ApiTraceV2Controller.kt | Inject new `TraceService`, add `blocking` query parameter |
| src/main/kotlin/.../controller/api/ApiTraceController.kt | Swapped `TraceService` → `V1TraceService` |
| client/src/main/kotlin/.../VesselVoyageClient.kt | Extended `Traces` subclient with `blocking` param and new HTTP calls |
</details>



<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**src/test/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiTraceV2ControllerTest.kt:111**
* [nitpick] There are no tests exercising the new `blocking` query parameter behavior. Add test cases for `blocking=true` to verify that blocking trace requests generate immediately as intended.
```
            mockMvc.perform(traceRequest)
```
</details>

### leonjoosse — CHANGES_REQUESTED (2025-07-03)

_No comment._

### Darius-Wattimena — COMMENTED (2025-07-03)

_No comment._

### leonjoosse — DISMISSED (2025-07-03)

_No comment._

### leonjoosse — APPROVED (2025-07-03)

_No comment._

## Review Comments

### Copilot — 2025-07-03 on `src/test/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiTraceV2ControllerTest.kt`

The controller test still provides a `ProcessingTraceService` bean, but the controller now depends on `TraceService`. Update this test bean to mock and provide `TraceService` instead of `ProcessingTraceService`.

### leonjoosse — 2025-07-03 on `client/src/main/kotlin/nl/teqplay/vesselvoyage/client/VesselVoyageClient.kt`

Typo: `catch` --> `catched`

### leonjoosse — 2025-07-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiTraceV2Controller.kt`

Why is `this` here?

![test](https://y.yarn.co/538e0a58-acae-4133-b173-582903f4b386_text.gif)


### leonjoosse — 2025-07-03 on `src/test/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiTraceV2ControllerTest.kt`

Not really needed to change this, I suppose this is automatically done?

### leonjoosse — 2025-07-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/TraceService.kt`

Sure about the log level?

### leonjoosse — 2025-07-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/TraceService.kt`

Sure about the log level?

### leonjoosse — 2025-07-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/TraceService.kt`

Does Joaquin know about this exclude on fail? What should he do in such case?

### Darius-Wattimena — 2025-07-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiTraceV2Controller.kt`

No I confused myself, so this, refers to the controller method itself :)

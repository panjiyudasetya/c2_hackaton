---
id: github:teqplay/vesselvoyage-backend:pr:564
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 564
title: Fix ship status
author: Darius-Wattimena
state: closed
date: '2025-07-14'
merged_at: '2025-07-14'
base_branch: develop
head_branch: fix-ship-status
url: https://github.com/teqplay/vesselvoyage-backend/pull/564
labels: []
linked_issues: []
explicit_links: []
---
# PR #564: Fix ship status

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/564  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `fix-ship-status`  
**Created:** 2025-07-14  
**Merged:** 2025-07-14  

## Description

_No description._

## Commits

- `4a28352b` **Joost Dambrink** (2025-07-08): Merge pull request #560 from teqplay/develop
  Release 😃👍 -  🌸 ８．０８．２０２５ 🌸
- `053b8950` **Darius Wattimena** (2025-07-11): Merge pull request #563 from teqplay/develop
  Release 11 Jul
- `f89688ac` **Darius Wattimena** (2025-07-12): Introduce back the in-memory ship status
- `f25dfe5a` **Darius Wattimena** (2025-07-12): Also adjust getLatestOngoingEntry so it uses the in-memory version as well
- `523c9ee0` **Darius Wattimena** (2025-07-12): ktlint

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-14)

## Pull Request Overview

This PR ensures that cached ship statuses are cleared after recalculation runs, adds a metrics registry to the ship-status processing, and updates service signatures and tests to accommodate the changes.

- Always remove the ship status cache in both Revents and Manual recalculation services.
- Extend the `ShipStatusService` API with a new `removeStatus(Int)` method and hook in a Micrometer `MeterRegistry` for metrics.
- Update constructors and tests across several classes to pass in `SimpleMeterRegistry` and adjust verifications.

### Reviewed Changes

Copilot reviewed 9 out of 9 changed files in this pull request and generated 1 comment.

<details>
<summary>Show a summary per file</summary>

| File                                                                  | Description                                                         |
| --------------------------------------------------------------------- | ------------------------------------------------------------------- |
| ReventsRecalculationService.kt                                        | Calls `shipStatusService.removeStatus(imo)` after scheduling posts. |
| ManualRecalculationService.kt                                         | Adds `removeStatus` before and during full‐story recreation.        |
| ShipStatusService.kt                                                  | Adds abstract `removeStatus(Int)` alongside deprecated `remove`.    |
| ProcessingShipStatusService.kt                                        | Implements `removeStatus`, adds caching, metrics, and state counters.|
| ApiShipStatusService.kt                                               | Implements no-op `removeStatus` to satisfy the new API.             |
| `*Test.kt` files (3 locations)                                        | Inject `SimpleMeterRegistry` and adjust mock verifications.         |
</details>



<details>
<summary>Comments suppressed due to low confidence (4)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/service/ShipStatusService.kt:47**
* [nitpick] Having both `remove(String)` and `removeStatus(Int)` in the same abstract class may cause confusion about which method to use. Consider renaming `remove` to `removeV1Status` or similar, or consolidating the two methods under a single clear name.
```
    abstract fun removeStatus(imo: Int)
```
**src/main/kotlin/nl/teqplay/vesselvoyage/service/ProcessingShipStatusService.kt:49**
* [nitpick] Public API methods like `updateStatus`, `getStatus`, and `removeStatus` should have KDoc explaining their purpose and side effects, especially around metrics updates and cache invalidation.
```
    companion object {
```
**src/main/kotlin/nl/teqplay/vesselvoyage/service/ProcessingShipStatusService.kt:58**
* Missing import: `AtomicLong` is used but not imported. Add `import java.util.concurrent.atomic.AtomicLong` so the code compiles.
```
    private val totalOngoingVisits = metricRegistry.createGauge(Metric.STATE_SIZE, AtomicLong(0), TAG_STATE_VALUE_VISITS)
```
**src/main/kotlin/nl/teqplay/vesselvoyage/service/ShipStatusService.kt:47**
* The abstract base class still declares `abstract fun remove(imo: String)` and now also `removeStatus(Int)`, but `ProcessingShipStatusService` does not override `remove(String)`. Either provide a default implementation in the base class or force subclasses to override `remove(String)` to avoid a compilation error.
```
    abstract fun removeStatus(imo: Int)
```
</details>

### TeqJoostD — APPROVED (2025-07-14)

_No comment._

## Review Comments

### Copilot — 2025-07-14 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ManualRecalculationServiceTest.kt`

[nitpick] Verifying the exact number of `getStatus` invocations tightly couples the test to the implementation details and can make it brittle. Consider removing or relaxing this count‐based assertion to focus on behavior rather than call frequency.
```suggestion
        verify(shipStatusService, atLeastOnce()).getStatus(eq(testImo))
```

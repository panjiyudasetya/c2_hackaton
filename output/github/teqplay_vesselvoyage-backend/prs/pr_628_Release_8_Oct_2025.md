---
id: github:teqplay/vesselvoyage-backend:pr:628
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 628
title: Release 8 Oct 2025
author: Darius-Wattimena
state: closed
date: '2025-10-08'
merged_at: '2025-10-08'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/628
labels: []
linked_issues: []
explicit_links: []
---
# PR #628: Release 8 Oct 2025

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/628  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2025-10-08  
**Merged:** 2025-10-08  

## Description

_No description._

## Commits

- `047fb005` **Darius Wattimena** (2025-09-22): Added some extra tests to ensure the processing trace service is working as expected
- `7dffd96c` **Darius Wattimena** (2025-09-22): Adjusted the code so we only take visit and voyage changes when assessing if we need to handle trace changes
- `509408b2` **Darius Wattimena** (2025-09-26): Fully refactor trace generation when canceling existing and when PostProcessing
- `c0c57d3c` **Darius Wattimena** (2025-09-26): Merge branch 'TCC-424-journey-etas' into TCC-434-fix-broken-ship-traces
- `e08e2578` **Darius Wattimena** (2025-09-26): ktlint
- `8253d2c9` **Darius Wattimena** (2025-09-26): fix: prevent unnecessary trace recalculation for empty AIS messages
- `9653342a` **Darius Wattimena** (2025-09-29): Merge branch 'TCC-424-journey-etas' into TCC-434-fix-broken-ship-traces
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt
- `4c22883b` **Jamie de Leest** (2025-09-29): feat: add accuracy report generation and CSV export
- `34020766` **Darius Wattimena** (2025-09-29): Make blocking request log debug level
- `c7b496e6` **Jamie de Leest** (2025-09-29): test: add tests for accuracy report functions
- `731fbe99` **Jamie de Leest** (2025-09-29): chore: ktlint
- `8160bd00` **Jamie de Leest** (2025-09-30): chore: implement feedback
- `038c1df5` **Darius Wattimena** (2025-09-30): Add lastPointAt timestamp to NewTrace and handle past AIS points in ProcessingTraceService
- `4ef6a59e` **Darius Wattimena** (2025-09-30): Add logging for out-of-order AIS messages to fully log the diff message
- `a073fdde` **Darius Wattimena** (2025-09-30): Update existing tests to set the expected scenario id to null
- `c698e2cb` **Darius Wattimena** (2025-10-01): Refactor message processing to simplify locking and remove multi-threading solution
- `c0216126` **Darius Wattimena** (2025-10-02): Optimize locking mechanism in ImoLockService using StampedLock, index lookup in an array instead of a map and stripe lookup for better performance
- `697555e5` **Darius Wattimena** (2025-10-03): Merge branch 'develop' into TCC-434-fix-broken-ship-traces
- `24ee777d` **Jamie de Leest** (2025-10-03): feat: integrate ETA into entry mapping for visits and voyages
- `b1837145` **Darius Wattimena** (2025-10-03): Update TrueDestinationEtaProcessor to handle previous visit updates and add new parameters for ETA processing
- `73c4c5bd` **Darius Wattimena** (2025-10-03): Remove unused ETA prediction configurations from application properties which have been removed before
- `dee0c5b8` **Darius Wattimena** (2025-10-03): Update test to be the expected outcome
- `4701e1ba` **Darius Wattimena** (2025-10-03): Update tests to fully check the ship status as well
- `e5f1c4f2` **Darius Wattimena** (2025-10-03): Remove unneeded cast in test
- `a5d23f5d` **Jamie de Leest** (2025-10-03): test: fix wrong tests
- `d21654da` **Darius Wattimena** (2025-10-03): Merge pull request #625 from teqplay/TCC-470-always-update-visit-eta
  TCC-470 always update visit eta
- `dab600cb` **Jamie de Leest** (2025-10-03): refactor: change database calls to batch calls when possible
- `157df2c3` **Jamie de Leest** (2025-10-03): refactor: rename and add missing batch calls
- `ee97f871` **Jamie de Leest** (2025-10-03): chore: ktlint
- `a2f4ab74` **Darius Wattimena** (2025-10-03): Merge pull request #623 from teqplay/TCC-469-add-eta-to-entry-mapper
  TCC-469 integrate ETA into entry mapping for visits and voyages
- `acd8db4c` **Darius Wattimena** (2025-10-03): Merge branch 'develop' into TCC-434-fix-broken-ship-traces
- `1bc4eba1` **Darius Wattimena** (2025-10-03): fix: handle null currentEntryTrace in trace replacement logic
- `67425a5d` **jamie-teqplay** (2025-10-06): Merge pull request #619 from teqplay/TCC-435-accuracy-testing-report-generation
  TCC-435 accuracy testing report generation
- `e444d186` **Darius Wattimena** (2025-10-06): Merge branch 'develop' into TCC-434-fix-broken-ship-traces
- `3cee1d18` **Darius Wattimena** (2025-10-06): Add functionality to do full trace recalculation of already post-processed entries
- `5d074cfd` **Darius Wattimena** (2025-10-06): Adjusted the check when we run slow moving periods
- `5a2bd105` **Darius Wattimena** (2025-10-07): Reimplement concurrent processing of AIS messages
- `c3716a27` **Darius Wattimena** (2025-10-07): Improve concurrent AIS processing to make use of batch processing and lanes to reduce stress on the CPU
- `acaa88f1` **Darius Wattimena** (2025-10-07): Load in all ship status on startup to speed up processing later instead of doing it in a lazy way
- `65685cf0` **Darius Wattimena** (2025-10-07): Code cleanup
- `cfddd52b` **Darius Wattimena** (2025-10-07): Load ship statuses on startup for improved processing efficiency
- `484e00e1` **Darius Wattimena** (2025-10-07): PR feedback
- `9f08b072` **Darius Wattimena** (2025-10-08): Merge pull request #627 from teqplay/TCC-434-fix-broken-ship-traces
  TCC-434 fix broken ship traces

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-08)

## Pull Request Overview

This is a release PR containing various bug fixes, performance improvements, and infrastructure changes for the vessel voyage processing system. The changes span across configuration, service logic, testing, and trace processing capabilities.

- Refactored trace processing with batching and improved error handling
- Removed deprecated thread configuration and updated batching properties
- Enhanced post-processing with trace recalculation and retry mechanisms

### Reviewed Changes

Copilot reviewed 58 out of 58 changed files in this pull request and generated 2 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/test/resources/application.properties | Removed deprecated thread configuration and added trace batching properties |
| src/main/resources/application.properties | Removed deprecated configuration properties and added new batching settings |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/ProcessingTraceService.kt | Major refactoring of trace processing with batch support and improved error handling |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt | Complete rewrite with lane-based batching for AIS message processing |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/ImoLockService.kt | Replaced ReentrantLock with StampedLock for better performance |
| Multiple test files | Updated tests to remove deprecated thread configuration and add new test cases |
| Multiple service files | Various updates to support new ESoF wrapper patterns and improved functionality |
</details>



<details>
<summary>Comments suppressed due to low confidence (3)</summary>

**src/test/kotlin/nl/teqplay/vesselvoyage/service/SlowMovingServiceTest.kt:1**
* Unused import 'java.time.ZoneOffset' should be removed as it's no longer used after the service method signature change.
```
package nl.teqplay.vesselvoyage.service
```
**src/test/kotlin/nl/teqplay/vesselvoyage/service/SlowMovingServiceTest.kt:1**
* Unused variable 'aisFetchingService' should be removed as the SlowMovingService constructor no longer requires it.
```
package nl.teqplay.vesselvoyage.service
```
**src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt:1**
* Unused imports 'kotlin.time.DurationUnit' and 'kotlin.time.toDuration' should be removed as they are no longer used after the refactoring.
```
package nl.teqplay.vesselvoyage.service.queue
```
</details>

## Review Comments

### Copilot — 2025-10-08 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

[nitpick] Consider using a custom thread name prefix for better debugging and monitoring. For example: `Executors.newFixedThreadPool(LANE_COUNT, ThreadFactoryBuilder().setNameFormat(\"ais-lane-%d\").build())`

### Copilot — 2025-10-08 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/ProcessingService.kt`

[nitpick] The parameter 'shipStatusService' is nullable but used in async operations without null checking. Consider making it non-null or adding explicit null checks in the async block.

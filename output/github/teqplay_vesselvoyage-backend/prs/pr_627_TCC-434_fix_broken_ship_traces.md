---
id: github:teqplay/vesselvoyage-backend:pr:627
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 627
title: TCC-434 fix broken ship traces
author: Darius-Wattimena
state: closed
date: '2025-10-07'
merged_at: '2025-10-08'
base_branch: develop
head_branch: TCC-434-fix-broken-ship-traces
url: https://github.com/teqplay/vesselvoyage-backend/pull/627
labels: []
linked_issues: []
explicit_links: []
---
# PR #627: TCC-434 fix broken ship traces

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/627  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-434-fix-broken-ship-traces`  
**Created:** 2025-10-07  
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
- `34020766` **Darius Wattimena** (2025-09-29): Make blocking request log debug level
- `038c1df5` **Darius Wattimena** (2025-09-30): Add lastPointAt timestamp to NewTrace and handle past AIS points in ProcessingTraceService
- `4ef6a59e` **Darius Wattimena** (2025-09-30): Add logging for out-of-order AIS messages to fully log the diff message
- `a073fdde` **Darius Wattimena** (2025-09-30): Update existing tests to set the expected scenario id to null
- `c698e2cb` **Darius Wattimena** (2025-10-01): Refactor message processing to simplify locking and remove multi-threading solution
- `c0216126` **Darius Wattimena** (2025-10-02): Optimize locking mechanism in ImoLockService using StampedLock, index lookup in an array instead of a map and stripe lookup for better performance
- `697555e5` **Darius Wattimena** (2025-10-03): Merge branch 'develop' into TCC-434-fix-broken-ship-traces
- `acd8db4c` **Darius Wattimena** (2025-10-03): Merge branch 'develop' into TCC-434-fix-broken-ship-traces
- `1bc4eba1` **Darius Wattimena** (2025-10-03): fix: handle null currentEntryTrace in trace replacement logic
- `e444d186` **Darius Wattimena** (2025-10-06): Merge branch 'develop' into TCC-434-fix-broken-ship-traces
- `3cee1d18` **Darius Wattimena** (2025-10-06): Add functionality to do full trace recalculation of already post-processed entries
- `5d074cfd` **Darius Wattimena** (2025-10-06): Adjusted the check when we run slow moving periods
- `5a2bd105` **Darius Wattimena** (2025-10-07): Reimplement concurrent processing of AIS messages
- `c3716a27` **Darius Wattimena** (2025-10-07): Improve concurrent AIS processing to make use of batch processing and lanes to reduce stress on the CPU
- `acaa88f1` **Darius Wattimena** (2025-10-07): Load in all ship status on startup to speed up processing later instead of doing it in a lazy way
- `65685cf0` **Darius Wattimena** (2025-10-07): Code cleanup
- `cfddd52b` **Darius Wattimena** (2025-10-07): Load ship statuses on startup for improved processing efficiency
- `484e00e1` **Darius Wattimena** (2025-10-07): PR feedback

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-07)

## Pull Request Overview

This PR fixes broken ship traces by implementing significant improvements to the AIS streaming and trace processing systems. The changes move from individual message processing to batch processing, improve performance through better locking mechanisms, and fix race conditions in trace handling.

- Replaces per-message processing with batch processing for AIS streams to improve throughput and consistency
- Refactors ImoLockService from per-IMO locks to striped locking for better concurrency and performance
- Enhances trace processing to handle batched items and out-of-order AIS data more effectively

### Reviewed Changes

Copilot reviewed 37 out of 37 changed files in this pull request and generated 3 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/main/resources/application.properties | Moves trace thread configuration and adds batch processing parameters |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt | Implements lane-based batch processing for AIS messages with backpressure control |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/ProcessingTraceService.kt | Refactors to handle batch trace processing and improved merge logic |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/ImoLockService.kt | Replaces ReentrantLock with StampedLock and striped locking for better performance |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessor.kt | Simplifies event processing by removing queuing logic |
| Multiple test files | Updates test configurations to remove removed totalThreads parameter |
</details>

### michel-teqplay — DISMISSED (2025-10-07)

_No comment._

### michel-teqplay — APPROVED (2025-10-08)

_No comment._

## Review Comments

### Copilot — 2025-10-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/ImoLockService.kt`

This comment should explain the implications and acceptable risks of lock sharing between different IMOs, as this could be a source of confusion for future maintainers.
```suggestion
     * NOTE: The same lock may be used for different IMOs due to the striped locking approach.
     * This design trades a small risk of lock contention for significant memory and performance benefits.
     * - Implications: If two IMOs hash to the same stripe, their operations will be serialized, potentially causing minor delays.
     * - Acceptable risks: With 131,072 stripes and ~70k IMOs, the probability of collision is very low (~0.53 IMOs/stripe on average).
     *   Collisions only affect performance (not correctness), as operations for different IMOs are still properly synchronized.
     *   No deadlocks or data races are introduced by this approach.
     * - Rationale: Allocating a lock per IMO would be prohibitively expensive in terms of memory.
     *   Striped locking is a well-established technique for balancing concurrency and resource usage.
     * Future maintainers: Only change this if you have a strong reason and have considered the trade-offs.
```

### Copilot — 2025-10-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

The hash function implementation should be documented to explain why this specific bit mixing is used and how it helps distribute IMOs across lanes.
```suggestion

    /**
     * Hash function for distributing IMOs across lanes.
     * IMOs are 7-digit numbers, which can cause clustering if used directly with modulo.
     * The bit mixing (imo xor (imo ushr 16)) helps spread similar IMOs more evenly,
     * reducing contention and improving parallelism in lane processing.
     * The final index is always non-negative and within [0, LANE_COUNT).
     */
```

### Copilot — 2025-10-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt`

Using Thread.sleep() blocks the thread. Consider using a proper retry mechanism with exponential backoff or scheduling the retry asynchronously.

### michel-teqplay — 2025-10-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

I'm with copilot here, please explain your voodoo :) ;)

### michel-teqplay — 2025-10-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

If you're interrupted (why?), why interrupt again?

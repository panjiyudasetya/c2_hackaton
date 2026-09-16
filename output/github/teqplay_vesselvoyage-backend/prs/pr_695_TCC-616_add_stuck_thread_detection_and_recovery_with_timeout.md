---
id: github:teqplay/vesselvoyage-backend:pr:695
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 695
title: TCC-616 add stuck thread detection and recovery with timeouts
author: TeqJoostD
state: closed
date: '2026-01-13'
merged_at: '2026-01-23'
base_branch: develop
head_branch: TCC-616
url: https://github.com/teqplay/vesselvoyage-backend/pull/695
labels: []
linked_issues: []
explicit_links: []
---
# PR #695: TCC-616 add stuck thread detection and recovery with timeouts

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/695  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-616`  
**Created:** 2026-01-13  
**Merged:** 2026-01-23  

## Description

_No description._

## Commits

- `65e352f7` **TeqJoostD** (2026-01-13): feat(processing): add stuck thread detection and recovery with timeouts
- `077494a7` **Darius Wattimena** (2026-01-15): Merge branch 'develop' into TCC-616
- `aa0298a8` **TeqJoostD** (2026-01-22): remove stuck task tracking debug info

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-01-13)

Copilot encountered an error and was unable to review this pull request. You can try again by re-requesting a review.

### github-actions[bot] — COMMENTED (2026-01-13)

Review completed. The implementation adds comprehensive stuck thread detection and recovery mechanisms with proper timeout handling. The RestTemplate timeout configurations will help prevent indefinite blocking on external service calls.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2026-01-15)

Review completed. I've identified a few potential concurrency and resource management issues in `PostProcessingService.kt` that should be addressed:

## 1. Race Condition During Executor Recreation

**Location:** `forceTerminateAndRecreateExecutor()` method, line 352 where `executor = createExecutor()`

While the `executor` field is marked as `@Volatile`, the recreation logic is not atomic. If another thread calls `executePostProcessing()` or accesses the executor while recreation is happening, it could:
- Submit tasks to the old executor that's being shut down
- Access a partially initialized executor

**Suggested fix:** Add synchronization around executor access and recreation:

```kotlin
private val executorLock = Any()

private fun forceTerminateAndRecreateExecutor() {
    log.warn { "Force terminating stuck threads and recreating executor" }
    val stuckEntryIds = activeTaskTracking.keys.toList()
    
    synchronized(executorLock) {
        try {
            // ... shutdown logic ...
        } catch (e: Exception) {
            log.error(e) { "Error during executor shutdown" }
        }
        activeTaskTracking.clear()
        executor = createExecutor()
    }
    // ... rest of the method ...
}
```

You would also need to synchronize access in `runPostProcessingForEntry()` when calling `executor.execute {}`.

---

## 2. Potential Memory Leak in Task Tracking

**Location:** `runPostProcessingForEntry()` method, line 403 where `activeTaskTracking[entryId] = trackingInfo`

If `executor.execute()` throws an exception (e.g., `RejectedExecutionException` after shutdown), the tracking entry is added but the lambda never executes, so the entry won't be removed in the `finally` block.

**Suggested fix:** Move tracking addition inside the lambda or handle the exception:

```kotlin
private fun runPostProcessingForEntry(postProcessable: PostProcessable) {
    val entryId = postProcessable.entryId
    try {
        executor.execute {
            val trackingInfo = TaskTrackingInfo(entryId = entryId, startTime = Instant.now(), stage = "STARTING")
            activeTaskTracking[entryId] = trackingInfo
            
            try {
                // ... existing logic ...
            } catch (ex: Exception) {
                log.error(ex) { "Error while post-processing entry (id = $entryId)" }
            } finally {
                activeTaskTracking.remove(entryId)
            }
        }
    } catch (ex: RejectedExecutionException) {
        log.error(ex) { "Failed to submit post-processing task for entry $entryId" }
    }
}
```

---

## 3. Incomplete Cleanup in Shutdown Method

**Location:** `shutdown()` method, line 104

The `shutdown()` method doesn't clear the `activeTaskTracking` map. If the service is shut down while tasks are running, the tracking map will retain stale entries.

**Suggested fix:**

```kotlin
fun shutdown() {
    executor.shutdown()
    activeTaskTracking.clear()
}
```

---
*🤖 Automated review complete. Please react with 👍 or 👎 on this comment to provide feedback on its usefulness.*

### github-actions[bot] — COMMENTED (2026-01-22)

Review completed. The timeout configurations and stuck thread detection logic are well-implemented. I identified one potential race condition concern with the executor reassignment.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### michel-teqplay — APPROVED (2026-01-22)

There's an AI comment about a potential race condition, I think it's not impossible that this would happen, but I'm not sure how big of a deal it is. If you think it's fine then I'm ok with this :)

## Review Comments

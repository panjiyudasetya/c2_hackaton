---
id: github:teqplay/vesselvoyage-backend:pr:648
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 648
title: Remove the shutdownNow shutdown mechanism and replace with poison pil…
author: TeqJoostD
state: closed
date: '2025-10-22'
merged_at: null
base_branch: develop
head_branch: TCC-497
url: https://github.com/teqplay/vesselvoyage-backend/pull/648
labels: []
linked_issues: []
explicit_links: []
---
# PR #648: Remove the shutdownNow shutdown mechanism and replace with poison pil…

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/648  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-497`  
**Created:** 2025-10-22  

## Description

…l to prevent mongo blocking issue

## Commits

- `5955d866` **TeqJoostD** (2025-10-22): remove the shutdownNow shutdown mechanism and replace with poison pill to prevent mongo blocking issue
- `1a3ecac7` **TeqJoostD** (2025-10-22): Create timeout for awaiting termination
- `ac79fbd5` **TeqJoostD** (2025-10-23): Prevent multiple shutdowns/startups.
  Remove unused trace property

## Reviews

### michel-teqplay — DISMISSED (2025-10-22)

_No comment._

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-22)

## Pull Request Overview

This PR replaces the `shutdownNow()` mechanism in the AIS streaming message handler with a poison pill pattern to enable graceful shutdown and prevent MongoDB blocking issues during termination.

Key changes:
- Introduces a `LaneElement` sealed interface with `Item` and `PoisonPill` variants to signal shutdown
- Modifies `shutdown()` to insert poison pills into each lane instead of forcefully interrupting threads
- Updates `drainLane()` to process remaining items after receiving poison pill before terminating

### michel-teqplay — DISMISSED (2025-10-22)

_No comment._

## Review Comments

### Copilot — 2025-10-22 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

The shutdown sequence doesn't wait for workers to complete after sending poison pills. Consider using `processingExecutor.awaitTermination(timeout, TimeUnit)` after `shutdown()` to ensure all lanes finish processing their remaining items before returning. This prevents potential data loss if the application exits before workers complete.
```suggestion
        processingExecutor.shutdown()
        try {
            if (!processingExecutor.awaitTermination(60, TimeUnit.SECONDS)) {
                log.warn { "Processing executor did not terminate within the timeout." }
            }
        } catch (e: InterruptedException) {
            log.error(e) { "Interrupted while waiting for processing executor to terminate." }
            Thread.currentThread().interrupt()
        }
```

### Copilot — 2025-10-22 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

The `put()` operation can block indefinitely if lanes are at capacity. Consider using `offer()` with a timeout or clearing space in the queue before inserting poison pills to ensure the shutdown process doesn't hang.
```suggestion
        lanes.forEach { lane ->
            val offered = lane.offer(LaneElement.PoisonPill, 5, TimeUnit.SECONDS)
            if (!offered) {
                log.warn { "Failed to insert poison pill into lane within timeout. Lane may be full." }
            }
        }
```

### Copilot — 2025-10-22 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

The condition `queue.isNotEmpty()` introduces a race condition. After `running` becomes false, the queue might be empty when checked but new items could be added before the next iteration. Since poison pill stops new items from being routed to this lane, the condition should be `while (running)` and rely on `take()` throwing InterruptedException or returning poison pill.
```suggestion
        while (running) {
```

### Copilot — 2025-10-22 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

Corrected spelling of 'pil' in PR title to 'pill'.

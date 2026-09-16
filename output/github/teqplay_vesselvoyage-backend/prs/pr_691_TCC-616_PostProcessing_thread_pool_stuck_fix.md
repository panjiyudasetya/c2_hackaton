---
id: github:teqplay/vesselvoyage-backend:pr:691
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 691
title: TCC-616 PostProcessing thread pool stuck fix
author: TeqJoostD
state: closed
date: '2026-01-07'
merged_at: '2026-01-09'
base_branch: develop
head_branch: TCC-616
url: https://github.com/teqplay/vesselvoyage-backend/pull/691
labels: []
linked_issues: []
explicit_links: []
---
# PR #691: TCC-616 PostProcessing thread pool stuck fix

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/691  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-616`  
**Created:** 2026-01-07  
**Merged:** 2026-01-09  

## Description

_No description._

## Commits

- `367f6153` **TeqJoostD** (2026-01-07): Change thread pool settings for post-processing
  Add max timeout for thread pool
- `48d78169` **TeqJoostD** (2026-01-07): Revert some of the thread pool settings
- `bdd2d38f` **TeqJoostD** (2026-01-07): Introduce bounded queue with error message and slack notification again
- `ba3993eb` **TeqJoostD** (2026-01-07): Add test coverage for timeout mechanism
- `8630e763` **TeqJoostD** (2026-01-07): Introduce mechanism for cancelling task when taking too long
- `9ff0de67` **TeqJoostD** (2026-01-07): Increase queue size to 10000

## Reviews

### github-actions[bot] — COMMENTED (2026-01-07)

The PR introduces a timeout mechanism to prevent thread pool hangs, which is a good improvement. However, there is a critical data loss issue when tasks are cancelled. The implementation is otherwise well-tested and handles the timeout scenario appropriately.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-01-07)

## Pull request overview

This PR implements a fix for thread pool stuck issues in the PostProcessingService by adding timeout mechanisms and bounded queue capacity. The changes prevent the scheduled task from hanging indefinitely when post-processing tasks take too long to complete.

Key changes:
- Added configurable timeout for waiting on thread pool completion with automatic cancellation of pending tasks
- Introduced bounded queue capacity with rejection handler to prevent memory issues
- Enhanced logging to track thread pool activity and timeout events with duration measurements

### Reviewed changes

Copilot reviewed 3 out of 3 changed files in this pull request and generated 11 comments.

| File | Description |
| ---- | ----------- |
| PostProcessingProperties.kt | Added two new configuration properties: `threadPoolWaitTimeout` (default 15 minutes) and `queueCapacity` (default 100) to control thread pool behavior |
| PostProcessingService.kt | Implemented timeout logic for thread pool waiting, added rejection handler for queue saturation, created helper methods to cancel pending tasks and wait for active threads, and enhanced logging with duration tracking |
| PostProcessingServiceTest.kt | Added comprehensive test coverage for timeout scenarios, including tests for timeout behavior, normal completion, and direct testing of the `waitUntilThreadPoolIsEmpty` method using reflection |

### TeqJoostD — COMMENTED (2026-01-07)

_No comment._

### TeqJoostD — COMMENTED (2026-01-07)

_No comment._

### github-actions[bot] — COMMENTED (2026-01-07)

Review completed. The implementation addresses the thread pool stuck issue with timeout and cancellation mechanisms. No additional suggestions at this time.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### michel-teqplay — APPROVED (2026-01-08)

_No comment._

## Review Comments

### Copilot — 2026-01-07 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingServiceTest.kt`

The test creates a separate ThreadPoolTaskExecutor but doesn't wait for the blocking task to fully complete before calling shutdown. After releasing the latch on line 499, the task still needs time to exit cleanly. Consider using `executor.awaitTermination()` after shutdown to ensure proper cleanup, or add a small delay after the countdown.

### Copilot — 2026-01-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/properties/PostProcessingProperties.kt`

The default queue capacity of 100 seems quite small for a post-processing service that can handle up to 5000 items per cycle (MAX_POST_PROCESSING_PER_CYCLE). With only 1 thread by default and a small queue, the rejection handler will be triggered frequently. Consider either:
1. Increasing the default queue capacity to a more reasonable value (e.g., 1000 or 5000)
2. Making the queue capacity proportional to the MAX_POST_PROCESSING_PER_CYCLE
3. Documenting why 100 was chosen and the expected behavior when it fills up

### Copilot — 2026-01-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt`

There's a potential race condition between checking the active thread count on line 169 and draining the queue on line 170. If a thread becomes active after line 169 but before the queue is drained, the log message will report an incorrect number of active threads. Consider moving the `activeCount` capture to after the `cancelPendingTasks()` call, or capturing it within that method for more accuracy.
```suggestion
                val cancelledCount = cancelPendingTasks()
                val activeThreadsAfterCancel = executor.threadPoolExecutor.activeCount
                log.error {
                    "Thread pool wait timeout exceeded after ${properties.threadPoolWaitTimeout}. " +
                        "Cancelled $cancelledCount pending tasks. Waiting for $activeThreadsAfterCancel active threads to complete."
                }
                slackMessageService?.sendMessage(
                    title = "Post-processing thread pool timeout",
                    text = "Thread pool did not empty within ${properties.threadPoolWaitTimeout}. " +
                        "Cancelled $cancelledCount pending tasks. " +
                        "Waiting for $activeThreadsAfterCancel active threads to complete.",
```

### Copilot — 2026-01-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt`

The constant `SLACK_COLOR_RED` is used but not imported. This will cause a compilation error. Add the import statement at the top of the file: `import nl.teqplay.vesselvoyage.service.SLACK_COLOR_RED`

### Copilot — 2026-01-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt`

When pending tasks are drained from the queue due to timeout, they are discarded and never processed. The tasks are wrapped Runnables containing the postProcessable entry IDs, but there's no mechanism to extract the entry IDs and re-queue them back to the datasource for processing in the next cycle. This results in data loss - those entries will remain in an unprocessed state indefinitely.

Consider extracting the PostProcessable information from the drained tasks and either:
1. Re-adding them to the datasource for the next cycle
2. Keeping them in the queue but preventing new tasks from being added
3. Implementing a retry mechanism for timed-out batches
```suggestion
     * Handles pending tasks in the queue after a timeout.
     *
     * Previously this method drained the queue and discarded all pending tasks,
     * which could lead to permanent data loss for post-processing items that never
     * get rescheduled. To avoid that, we now leave tasks in the queue so they can
     * still be executed once the executor is free again.
     *
     * Running tasks are always allowed to complete to avoid data corruption.
     *
     * @return The number of tasks that were pending in the queue at the time of inspection.
     */
    private fun cancelPendingTasks(): Int {
        val queue = executor.threadPoolExecutor.queue
        val pendingTasksCount = queue.size
        log.warn {
            "Timeout reached while waiting for post-processing to finish. " +
                "Leaving $pendingTasksCount pending tasks in the executor queue to avoid data loss."
        }
        return pendingTasksCount
```

### Copilot — 2026-01-07 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingServiceTest.kt`

After the test releases the blocking latch and shuts down the service, the test doesn't verify that the thread actually completes. The `executionThread.join(2000)` on line 384 uses a timeout but doesn't check if the join was successful. Consider adding an assertion after line 396 to verify the execution thread has terminated: `assertFalse(executionThread.isAlive, "Execution thread should have terminated")`

### Copilot — 2026-01-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/properties/PostProcessingProperties.kt`

The documentation for `threadPoolWaitTimeout` states it "prevents the scheduled task from hanging indefinitely," but it doesn't explain what happens when the timeout is exceeded. Consider enhancing the documentation to mention that:
1. Pending tasks in the queue will be cancelled and lost
2. Active threads will be waited for indefinitely afterward (which could still cause hangs)
3. A Slack notification will be sent

This will help operators understand the operational implications and configure appropriate timeout values.
```suggestion
     * This prevents the scheduled task from hanging indefinitely.
     *
     * When this timeout is exceeded:
     * - Pending tasks still in the queue will be cancelled and will not be executed.
     * - Active worker threads are still waited for indefinitely, which means a stuck task can still cause a hang.
     * - A Slack notification will be sent to alert operators that the timeout was exceeded.
```

### Copilot — 2026-01-07 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingServiceTest.kt`

Missing test coverage for the queue rejection handler scenario. When the queue capacity is exceeded, the rejection handler is triggered, but there are no tests verifying:
1. That the rejection handler is called when the queue is full
2. That a Slack notification is sent
3. That the rejected task is handled appropriately (currently it's just dropped)

Consider adding a test that fills the queue and verifies the rejection behavior.

### Copilot — 2026-01-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt`

When pending tasks are drained from the queue on timeout, the `EndPostProcessingEvent` is never published for those cancelled entries. This event is typically published after processing completes (lines 275, 285, 391). If other parts of the system rely on this event, cancelled tasks could cause waiting components to hang indefinitely or behave incorrectly. Consider publishing an event (possibly a different event type) to indicate that processing was cancelled for these entries.

### Copilot — 2026-01-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt`

The rejected execution handler only logs and sends a Slack notification but doesn't handle the rejected task itself. This means rejected tasks will be silently dropped and never processed. Consider one of these approaches:

1. Re-queue the task back to the datasource so it can be picked up in the next cycle
2. Use a CallerRunsPolicy to execute the task in the calling thread 
3. Throw a RejectedExecutionException to fail fast and alert on the issue

The current implementation will result in data loss when the queue is full.
```suggestion
            )
            // Fallback to CallerRuns-style behavior to avoid silently dropping tasks when the queue is full.
            try {
                if (!executor.isShutdown) {
                    task.run()
                } else {
                    log.warn { "Post-processing task rejected after executor shutdown; task will not be executed." }
                }
            } catch (exception: Exception) {
                log.error(exception) { "Post-processing task execution failed in rejection handler." }
                throw exception
            }
```

### Copilot — 2026-01-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt`

The `waitForActiveThreadsToComplete()` method waits indefinitely for active threads to complete. If a thread is truly stuck (e.g., due to a deadlock or an infinite loop), this method will hang forever and prevent the next scheduled cycle from running. Consider adding a maximum wait time here as well, with appropriate error handling if that timeout is exceeded.

### TeqJoostD — 2026-01-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt`

They will just be picked up again...

### TeqJoostD — 2026-01-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt`

Will have to see with testing if this ever happens

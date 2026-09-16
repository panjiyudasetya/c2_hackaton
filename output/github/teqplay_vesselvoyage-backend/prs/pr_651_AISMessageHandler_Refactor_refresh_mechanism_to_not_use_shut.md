---
id: github:teqplay/vesselvoyage-backend:pr:651
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 651
title: AISMessageHandler Refactor refresh mechanism to not use shutdownNow
author: TeqJoostD
state: closed
date: '2025-10-27'
merged_at: '2025-10-28'
base_branch: develop
head_branch: TCC-497-Refresh-mechanism
url: https://github.com/teqplay/vesselvoyage-backend/pull/651
labels: []
linked_issues: []
explicit_links: []
---
# PR #651: AISMessageHandler Refactor refresh mechanism to not use shutdownNow

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/651  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-497-Refresh-mechanism`  
**Created:** 2025-10-27  
**Merged:** 2025-10-28  

## Description

_No description._

## Commits

- `f1b5434a` **TeqJoostD** (2025-10-27): Refactor refresh mechanism to not crash and use service independent implementation.
- `09a606ba` **TeqJoostD** (2025-10-27): small improvements

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-27)

## Pull Request Overview

This PR refactors the refresh mechanism for AIS and Events message handlers by removing the event-driven approach and implementing direct restart logic. The key motivation is to eliminate the use of `shutdownNow` (as mentioned in the title) and provide more controlled refresh behavior.

**Key changes:**
- Removed the `ProcessingRefreshEvent` class and its event-driven refresh mechanism
- Updated `EventsMessageHandler` to directly call `shutdown()` and `startup()` in `refreshConsumer()`
- Enhanced `AisStreamingMessageHandler` with a more sophisticated refresh process that drains the consumer, clears lanes, and re-establishes the subscription

### Reviewed Changes

Copilot reviewed 4 out of 4 changed files in this pull request and generated 4 comments.

| File | Description |
| ---- | ----------- |
| ProcessingRefreshEvent.kt | Completely removed the event class used for triggering processing refreshes |
| EventsMessageHandler.kt | Simplified refresh to directly invoke shutdown/startup instead of publishing an event |
| AisStreamingMessageHandler.kt | Implemented detailed refresh logic with consumer draining and lane clearing |
| ProcessingService.kt | Removed the event listener that handled ProcessingRefreshEvent |

### TeqJoostD — COMMENTED (2025-10-27)

_No comment._

### Darius-Wattimena — APPROVED (2025-10-28)

_No comment._

## Review Comments

### Copilot — 2025-10-27 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

This lambda duplicates the consumption logic that likely exists elsewhere in the class. The message handling logic should be extracted to avoid code duplication and ensure consistent behavior across startup and refresh scenarios.
```suggestion
                handleConsumerMessage(wrapper, message)
            }

    /**
     * Handles a message received from the consumer stream, updating the timestamp and processing the message.
     * Ensures consistent error handling and logging across consumer scenarios.
     */
    private fun handleConsumerMessage(wrapper: Any, message: Message) {
        try {
            receivedLastAisMessageAt = Instant.now()
            consumeMessage(natsMessage = message, data = wrapper)
        } catch (e: InterruptedException) {
            log.info(e) { "Got interrupted during consumption" }
        } catch (e: Exception) {
            log.error(e) { "Something went wrong during consumption" }
        }
    }
```

### Copilot — 2025-10-27 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

The documentation claims that unprocessed messages are NAcked for redelivery, but the implementation only calls `lane.clear()` without any explicit NAck logic. Either the documentation should be corrected or the implementation should include NAck calls.
```suggestion
     * This ensures no messages are lost during the refresh.
     *
     * Note: This implementation assumes that each lane contains ProcessingItem objects,
     * and that each ProcessingItem has a reference to the NATS Message to NAck.
     * If this is not the case, update the documentation accordingly.
     */
    private fun clearLanes() {
        for (i in 0 until LANE_COUNT) {
            val lane = lanes[i]

            // NAck all unprocessed messages in this lane before clearing
            for (item in lane) {
                // If item contains a NATS Message, NAck it
                if (item is ProcessingItem && item.natsMessage != null) {
                    try {
                        item.natsMessage.nak()
                    } catch (e: Exception) {
                        log.error(e) { "Failed to NAck message in lane $i" }
                    }
                }
            }
```

### Copilot — 2025-10-27 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

[nitpick] The loop uses index-based iteration when a more idiomatic Kotlin approach would be to iterate directly over the lanes collection using `lanes.forEach { it.clear() }` or `lanes.forEach(BlockingQueue<*>::clear)`.
```suggestion
        // Clear all items from each lane using idiomatic Kotlin iteration
        lanes.forEach { it.clear() }
```

### Copilot — 2025-10-27 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

There's a potential race condition between draining the consumer (line 126) and clearing lanes (line 130). Messages that were in-flight during drain could still be processed by existing lane workers, leading to inconsistent state. Consider waiting for lane processing to complete before restarting the consumer.

### TeqJoostD — 2025-10-27 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

no

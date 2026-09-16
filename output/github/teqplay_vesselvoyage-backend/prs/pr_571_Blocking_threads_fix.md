---
id: github:teqplay/vesselvoyage-backend:pr:571
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 571
title: Blocking threads fix
author: TeqJoostD
state: closed
date: '2025-07-15'
merged_at: '2025-07-15'
base_branch: develop
head_branch: blocking-threads-fix
url: https://github.com/teqplay/vesselvoyage-backend/pull/571
labels: []
linked_issues: []
explicit_links: []
---
# PR #571: Blocking threads fix

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/571  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `blocking-threads-fix`  
**Created:** 2025-07-15  
**Merged:** 2025-07-15  

## Description

_No description._

## Commits

- `d2547508` **Darius Wattimena** (2025-07-15): Attempt to rewrite handling of blocked ships
- `26894423` **TeqJoostD** (2025-07-15): Merge branch 'develop' into blocking-threads-fix
- `580d19f6` **Joost Dambrink** (2025-07-15): Update src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessor.kt
  Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com>
- `4c1966fb` **TeqJoostD** (2025-07-15): adjust queue take method
- `ecc8ddd4` **TeqJoostD** (2025-07-15): Merge remote-tracking branch 'origin/blocking-threads-fix' into blocking-threads-fix
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessor.kt
- `25de02cd` **TeqJoostD** (2025-07-15): Final change
- `a29e4171` **TeqJoostD** (2025-07-15): remove intterupt
- `db9d1a35` **Joost Dambrink** (2025-07-15): Merge branch 'develop' into blocking-threads-fix

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-15)

## Pull Request Overview

This PR updates background event processors to avoid indefinitely blocking threads by switching from a blocking `take()` to a timed `poll()` and tightening synchronization scopes.  
- Switched `queue.take()` to `queue.poll(5, TimeUnit.SECONDS)` in the default message processor  
- Moved synchronization to only cover the cleanup removal in both event handlers  
- Similar synchronization adjustment applied to the AIS streaming handler

### Reviewed Changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated 2 comments.

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessor.kt | Replaced blocking `take()` loop with timed `poll()`, added `TimeUnit` import, and narrowed `synchronized` block to only the removal of `inFlightEvents`. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt | Removed broad synchronization around processing, added a `synchronized` block only around the removal of `inFlightAisMessages`. |

### Darius-Wattimena — CHANGES_REQUESTED (2025-07-15)

_No comment._

### TeqJoostD — COMMENTED (2025-07-15)

_No comment._

### Darius-Wattimena — CHANGES_REQUESTED (2025-07-15)

_No comment._

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-15)

## Pull Request Overview

This PR updates the backlog processing loops to use `queue.poll` with a timeout, adds interruption handling, and adjusts where the `inFlight` synchronization occurs.

- Replaced `queue.take()` with `queue.poll(5, TimeUnit.SECONDS)` and exit on timeout
- Catches `InterruptedException` to break out of the loop
- Moved the `synchronized(inFlight*)` block to after processing instead of around the entire loop

### Reviewed Changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated 2 comments.

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessor.kt | Switched from `take()` to `poll`, added `InterruptedException` handling, and relocated `synchronized(inFlightEvents)` block |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt | Switched from `take()` to `poll`, added `InterruptedException` handling, and relocated `synchronized(inFlightAisMessages)` block |


<details>
<summary>Comments suppressed due to low confidence (2)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessor.kt:132**
* The initial synchronization around the backlog processing was removed before `executeBlocking`, which could allow multiple threads to start processing the same IMO concurrently. Consider restoring or replacing this lock to prevent race conditions on `inFlightEvents`.
```
            backgroundInFlightEventsProcessor.execute {
```
**src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt:237**
* The pre-loop synchronization on `inFlightAisMessages` was removed, which may allow concurrent processors for the same IMO. Ensure you reintroduce or replace this locking to avoid concurrent backlog processing for one IMO.
```
            backgroundInFlightEventsProcessor.execute {
```
</details>

### Darius-Wattimena — APPROVED (2025-07-15)

_No comment._

## Review Comments

### Copilot — 2025-07-15 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessor.kt`

LinkedBlockingQueue.poll(timeout) can throw InterruptedException; consider wrapping this call in a try-catch to handle interruptions (e.g., re-interrupt the thread and break the loop) so the executor thread isn’t terminated unexpectedly.
```suggestion
                        try {
                            val eventToProcess = queue.poll(5, TimeUnit.SECONDS)
                            if (eventToProcess == null) {
                                break
                            }

                            processEvent(eventToProcess.message, imo)
                            eventToProcess.natsMessage.ack()
                        } catch (e: InterruptedException) {
                            Thread.currentThread().interrupt()
                            log.warn { "Thread interrupted while processing backlog for $imo. Exiting loop." }
                            break
                        }
```

### Copilot — 2025-07-15 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

This still uses a blocking loop (likely queue.take()) which can block indefinitely; to mirror the fix above, switch to queue.poll(timeout, TimeUnit.SECONDS) and break when it returns null to prevent thread starvation.

### Darius-Wattimena — 2025-07-15 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

Probably should make this into a `poll(5, seconds)` as well?
Hence we might even want to reduce the 5 seconds to like 1 given that you want a quick response when retrieving something from an in-memory internal queue?

### TeqJoostD — 2025-07-15 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

Sorry didnt push my commits yet I see now

### Darius-Wattimena — 2025-07-15 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessor.kt`

I wouldn't interrupt the background thread, instead just breaking the blocking code we are executing should be enough

### Copilot — 2025-07-15 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessor.kt`

If `processEvent` or `ack` throws an unexpected exception, the final `synchronized(inFlightEvents)` cleanup won’t run, leaving the IMO marked in-flight indefinitely. Wrap the processing loop in a try-finally to ensure `inFlightEvents.remove(imo)` always executes.
```suggestion
                    try {
                        while (true) {
                            try {
                                val eventToProcess = queue.poll(5, TimeUnit.SECONDS) ?: break

                                processEvent(eventToProcess.message, imo)
                                eventToProcess.natsMessage.ack()
                            } catch (e: InterruptedException) {
                                log.warn { "Thread interrupted while processing backlog for $imo. Exiting loop." }
                                break
                            }
                        }
                    } finally {
                        synchronized(inFlightEvents) {
                            log.trace { "Done processing backlog now ${queue.size} events are left for $imo" }
                            inFlightEvents.remove(imo)
                        }
                    }
```

### Copilot — 2025-07-15 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

If `processMessage` or the acknowledgement callback throws, the final removal from `inFlightAisMessages` under `synchronized` won’t run. Enclose the loop in try-finally to guarantee cleanup of the in-flight map.

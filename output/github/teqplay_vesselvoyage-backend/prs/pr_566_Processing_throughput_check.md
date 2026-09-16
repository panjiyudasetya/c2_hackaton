---
id: github:teqplay/vesselvoyage-backend:pr:566
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 566
title: Processing throughput check
author: Darius-Wattimena
state: closed
date: '2025-07-14'
merged_at: '2025-07-15'
base_branch: develop
head_branch: processing-throughput-check
url: https://github.com/teqplay/vesselvoyage-backend/pull/566
labels: []
linked_issues: []
explicit_links: []
---
# PR #566: Processing throughput check

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/566  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `processing-throughput-check`  
**Created:** 2025-07-14  
**Merged:** 2025-07-15  

## Description

_No description._

## Commits

- `a0292adf` **Darius Wattimena** (2025-07-14): Add activeness monitoring for event processing and support to refresh all processing services when the ProcessingRefreshEvent is published internally
- `7837f16c` **Darius Wattimena** (2025-07-14): Also trigger activeness checks on AIS processing and adjusted existing tests
- `1445df43` **Darius Wattimena** (2025-07-14): Copilot feedback
- `d2fa0595` **Darius Wattimena** (2025-07-14): ktlint

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-14)

## Pull Request Overview

This PR adds activeness/throughput monitoring to the event and AIS consumers, enabling automatic refresh when idle.

- Introduces `ActivenessMonitoring` settings in both `EventProcessingProperties` and `TraceProperties` and updates application properties.
- Implements scheduled throughput checks and publishes `ProcessingRefreshEvent` in `EventsMessageHandler` and `AisStreamingMessageHandler`.
- Updates `ProcessingService` to listen for `ProcessingRefreshEvent` and restart processing.

### Reviewed Changes

Copilot reviewed 19 out of 19 changed files in this pull request and generated 4 comments.

<details>
<summary>Show a summary per file</summary>

| File                                                       | Description                                                 |
|------------------------------------------------------------|-------------------------------------------------------------|
| src/test/resources/application.properties                  | Add `activeness-monitoring` settings to test config         |
| src/main/resources/application.properties                  | Add `activeness-monitoring` settings to runtime config      |
| src/main/kotlin/nl/teqplay/vesselvoyage/spring/ProcessingRefreshEvent.kt | Define `ProcessingRefreshEvent`                              |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/EventsMessageHandler.kt | Add activeness monitoring, scheduling, and refresh logic     |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt | Add activeness monitoring, scheduling, and refresh logic     |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/ProcessingService.kt | Handle `ProcessingRefreshEvent` to restart processing      |
| src/main/kotlin/nl/teqplay/vesselvoyage/properties/TraceProperties.kt | Add nested `ActivenessMonitoring` in `TraceProperties`     |
| src/main/kotlin/nl/teqplay/vesselvoyage/properties/EventProcessingProperties.kt | Add nested `ActivenessMonitoring` in `EventProcessingProperties` |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/V1TraceService.kt | Change cleanup logs from INFO to DEBUG                     |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/MessageHandlerHealth.kt | Remove unused `MessageHandlerHealth` interface             |
| Test classes (multiple under `src/test/kotlin/...`)        | Update constructors to supply default `activenessMonitoring` |
</details>



<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/EventsMessageHandler.kt:85**
* Consider adding unit tests for `monitorThroughput` and `refreshConsumer` to verify that idle conditions correctly trigger the `ProcessingRefreshEvent`.
```
    @ConditionalOnProperty("event-processing.activeness-monitoring.enabled", havingValue = "true")
```
</details>

### TeqJoostD — APPROVED (2025-07-14)

_No comment._

## Review Comments

### Copilot — 2025-07-14 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/EventsMessageHandler.kt`

Mark `receivedLastEventAt` as `@Volatile` to ensure writes in the consumer thread are visible to the scheduled monitor thread.
```suggestion
) {
    @Volatile
```

### Copilot — 2025-07-14 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

Annotate `receivedLastEventAt` with `@Volatile` to guarantee visibility across the consumption and scheduled monitoring threads.
```suggestion
) {
    @Volatile
```

### Copilot — 2025-07-14 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/EventsMessageHandler.kt`

Use `Instant.now()` here instead of mixing `ZonedDateTime` with `Instant` to keep temporal types consistent in `Duration.between`.
```suggestion
        val now = Instant.now()
```

### Copilot — 2025-07-14 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

Prefer `Instant.now()` here to avoid mixing `Instant` and `ZonedDateTime` when computing the idle `Duration`.
```suggestion
        val now = Instant.now()
```

---
id: github:teqplay/vesselvoyage-backend:pr:659
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 659
title: publish changes from eta update result
author: TeqJoostD
state: closed
date: '2025-11-06'
merged_at: '2025-11-07'
base_branch: develop
head_branch: TCC-524
url: https://github.com/teqplay/vesselvoyage-backend/pull/659
labels: []
linked_issues: []
explicit_links: []
---
# PR #659: publish changes from eta update result

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/659  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-524`  
**Created:** 2025-11-06  
**Merged:** 2025-11-07  

## Description

_No description._

## Commits

- `f5462b54` **TeqJoostD** (2025-11-06): publish changes from eta update result
- `73a6f09f` **TeqJoostD** (2025-11-07): fix comment

## Reviews

### github-actions[bot] — COMMENTED (2025-11-06)

Review completed. No suggestions at this time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-11-06)

## Pull Request Overview

This PR integrates change publishing functionality into the `EtaPredictionMessageHandler` by adding the `ChangesPublisherService` dependency. When ETA predictions are processed and result in changes, these changes are now published to NATS.

Key changes:
- Added `ChangesPublisherService` as an optional dependency to `EtaPredictionMessageHandler`
- Implemented logic to publish changes when they are present after processing predictions
- Added comprehensive test coverage for both scenarios: when changes are present and when they are not

### Reviewed Changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated no comments.

| File | Description |
| ---- | ----------- |
| EtaPredictionMessageHandler.kt | Added `changesPublisherService` parameter and logic to publish changes after persistence |
| EtaPredictionMessageHandlerTest.kt | Added mock setup for `changesPublisherService` and two new test cases to verify publishing behavior |


<details>
<summary>Comments suppressed due to low confidence (6)</summary>

**src/test/kotlin/nl/teqplay/vesselvoyage/service/queue/EtaPredictionMessageHandlerTest.kt:67**
* The `verifyNoMoreInteractions` calls in existing tests should include `changesPublisherService` to ensure it's not being called unexpectedly in early-exit scenarios. This ensures complete verification of the handler's behavior.
```
        verifyNoMoreInteractions(staticShipInfoService, processingShipStatusService, persistChangesService, trueDestinationEtaProcessor)
```
**src/test/kotlin/nl/teqplay/vesselvoyage/service/queue/EtaPredictionMessageHandlerTest.kt:78**
* The `verifyNoMoreInteractions` calls in existing tests should include `changesPublisherService` to ensure it's not being called unexpectedly in early-exit scenarios. This ensures complete verification of the handler's behavior.
```
        verifyNoMoreInteractions(staticShipInfoService, processingShipStatusService, persistChangesService, trueDestinationEtaProcessor)
```
**src/test/kotlin/nl/teqplay/vesselvoyage/service/queue/EtaPredictionMessageHandlerTest.kt:91**
* The `verifyNoMoreInteractions` calls in existing tests should include `changesPublisherService` to ensure it's not being called unexpectedly in early-exit scenarios. This ensures complete verification of the handler's behavior.
```
        verifyNoMoreInteractions(staticShipInfoService, processingShipStatusService, persistChangesService, trueDestinationEtaProcessor)
```
**src/test/kotlin/nl/teqplay/vesselvoyage/service/queue/EtaPredictionMessageHandlerTest.kt:106**
* The `verifyNoMoreInteractions` calls in existing tests should include `changesPublisherService` to ensure it's not being called unexpectedly in early-exit scenarios. This ensures complete verification of the handler's behavior.
```
        verifyNoMoreInteractions(staticShipInfoService, processingShipStatusService, persistChangesService, trueDestinationEtaProcessor)
```
**src/test/kotlin/nl/teqplay/vesselvoyage/service/queue/EtaPredictionMessageHandlerTest.kt:124**
* The `verifyNoMoreInteractions` call should include `changesPublisherService` to ensure it's not being called when IMO lookup fails.
```
        verifyNoMoreInteractions(processingShipStatusService, persistChangesService, trueDestinationEtaProcessor)
```
**src/test/kotlin/nl/teqplay/vesselvoyage/service/queue/EtaPredictionMessageHandlerTest.kt:128**
* This test should verify that `changesPublisherService` is not called when there are no changes (empty list). Add `verifyNoMoreInteractions(changesPublisherService)` after line 155 to ensure consistency with the production code logic that only publishes when changes are non-empty.
```
    fun `processes valid prediction and persists changes when no issues`() {
```
</details>

### Darius-Wattimena — CHANGES_REQUESTED (2025-11-07)

_No comment._

### Darius-Wattimena — APPROVED (2025-11-07)

_No comment._

### github-actions[bot] — COMMENTED (2025-11-07)

Review completed. No suggestions at this time.

## Review Comments

### Darius-Wattimena — 2025-11-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/EtaPredictionMessageHandler.kt`

Comment is not valid, we only publish to RabbitMQ (this is handled by the `changesPublisherService` so no need to mention this I think)

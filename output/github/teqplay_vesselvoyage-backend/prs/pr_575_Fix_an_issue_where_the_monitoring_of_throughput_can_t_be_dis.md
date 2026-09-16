---
id: github:teqplay/vesselvoyage-backend:pr:575
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 575
title: Fix an issue where the monitoring of throughput can't be disabled
author: Darius-Wattimena
state: closed
date: '2025-07-17'
merged_at: '2025-07-17'
base_branch: develop
head_branch: fix-not-toggleble-monitoring
url: https://github.com/teqplay/vesselvoyage-backend/pull/575
labels: []
linked_issues: []
explicit_links: []
---
# PR #575: Fix an issue where the monitoring of throughput can't be disabled

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/575  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `fix-not-toggleble-monitoring`  
**Created:** 2025-07-17  
**Merged:** 2025-07-17  

## Description

_No description._

## Commits

- `979e89b5` **Darius Wattimena** (2025-07-17): Fix an issue where the monitoring of throughput can't be disabled

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-17)

## Pull Request Overview

This PR enables dynamic disabling of throughput monitoring by moving the property check into the scheduled method instead of relying on `@ConditionalOnProperty`.

- Removed `@ConditionalOnProperty` annotations from both handlers.
- Added runtime guard against `activenessMonitoring.enabled` in `monitorThroughput()` for both event and AIS streaming handlers.

### Reviewed Changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated 1 comment.

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/EventsMessageHandler.kt | Removed annotation and added runtime guard for event throughput monitoring. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt | Removed annotation and added runtime guard for AIS throughput monitoring. |


<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/EventsMessageHandler.kt:90**
* Add tests to verify that when `activenessMonitoring.enabled` is false, `monitorThroughput()` returns early and does not perform any checks or logging.
```
        if (!processingProperties.activenessMonitoring.enabled) {
```
</details>

### TeqJoostD — APPROVED (2025-07-17)

_No comment._

## Review Comments

### Copilot — 2025-07-17 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

[nitpick] Consider extracting the common runtime guard (`if (!…enabled) return`) into a shared helper or base class to reduce duplication across handlers.
```suggestion
        if (!isFeatureEnabled(traceProperties.activenessMonitoring.enabled, "Activeness monitoring is disabled.")) {
```

---
id: github:teqplay/vesselvoyage-backend:pr:577
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 577
title: Fix trace generation
author: Darius-Wattimena
state: closed
date: '2025-07-18'
merged_at: '2025-07-28'
base_branch: develop
head_branch: fix-trace-generation
url: https://github.com/teqplay/vesselvoyage-backend/pull/577
labels: []
linked_issues: []
explicit_links: []
---
# PR #577: Fix trace generation

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/577  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `fix-trace-generation`  
**Created:** 2025-07-18  
**Merged:** 2025-07-28  

## Description

_No description._

## Commits

- `82f14d8d` **Darius Wattimena** (2025-07-18): Always generate a trace even when the entry is not finished to ensure we don't get weird jumps in AIS
- `8f2f7976` **Darius Wattimena** (2025-07-18): Added a test case where we ensure the trace is generated event when we don't have an end time set
- `7cc28e13` **Darius Wattimena** (2025-07-18): Changed logic so we can provide a clock for testing
- `b8ef8289` **Darius Wattimena** (2025-07-18): ktlint please

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-18)

## Pull Request Overview

This PR fixes trace generation for ongoing visits by allowing trace generation for visits without an end time. Previously, the system would skip trace generation for unfinished visits, but now it uses the current time as the end time for ongoing visits.

- Modified trace generation logic to handle visits without end times
- Added Clock parameter for testability and time injection
- Updated test coverage for ongoing visit scenarios

### Reviewed Changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated 1 comment.

| File | Description |
| ---- | ----------- |
| TraceService.kt | Removes the early return for entries without end time and adds Clock parameter support for better testability |
| ProcessingTraceServiceTest.kt | Adds comprehensive test coverage for trace generation of ongoing visits without end times |


<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/TraceService.kt:361**
* The variable name 'startTime' is misleading as it represents the current time when trace generation begins, not the start time of a trace. Consider renaming to 'currentTime' or 'now' for clarity.
```
        val startTime = Instant.now(clock)
```
</details>

### TeqJoostD — DISMISSED (2025-07-18)

_No comment._

### TeqJoostD — COMMENTED (2025-07-18)

_No comment._

### TeqJoostD — APPROVED (2025-07-28)

_No comment._

## Review Comments

### Copilot — 2025-07-18 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/ProcessingTraceServiceTest.kt`

There is a spelling error in the variable name 'previusVisitEndLocation'. It should be 'previousVisitEndLocation'.

### TeqJoostD — 2025-07-18 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/ProcessingTraceServiceTest.kt`

bruh

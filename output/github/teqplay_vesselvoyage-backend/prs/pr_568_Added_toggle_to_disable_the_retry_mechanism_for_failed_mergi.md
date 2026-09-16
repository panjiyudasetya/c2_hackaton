---
id: github:teqplay/vesselvoyage-backend:pr:568
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 568
title: Added toggle to disable the retry mechanism for failed merging back
author: Darius-Wattimena
state: closed
date: '2025-07-15'
merged_at: '2025-07-15'
base_branch: develop
head_branch: retry-on-failed-revents
url: https://github.com/teqplay/vesselvoyage-backend/pull/568
labels: []
linked_issues: []
explicit_links: []
---
# PR #568: Added toggle to disable the retry mechanism for failed merging back

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/568  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `retry-on-failed-revents`  
**Created:** 2025-07-15  
**Merged:** 2025-07-15  

## Description

_No description._

## Commits

- `86f336be` **Darius Wattimena** (2025-07-15): Added toggle to disable the retry mechanism for failed merging back
- `30d795d6` **Darius Wattimena** (2025-07-15): Fixed compile issue in test

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-15)

## Pull Request Overview

This PR introduces a configuration toggle to disable the automatic retry logic for failed Revents merges.

- Add a new `revents-retry-enabled` flag in both main and test application properties
- Extend `RecalculationProperties` to include the new boolean toggle
- Update `ReventsRecalculationService` to respect the toggle when deciding to retry failed merges

### Reviewed Changes

Copilot reviewed 4 out of 4 changed files in this pull request and generated no comments.

| File                                                       | Description                                                          |
| ---------------------------------------------------------- | -------------------------------------------------------------------- |
| src/test/resources/application.properties                  | Add `recalculation.revents-retry-enabled=false` for tests            |
| src/main/resources/application.properties                  | Add `recalculation.revents-retry-enabled=true` for production        |
| src/main/kotlin/nl/teqplay/vesselvoyage/properties/RecalculationProperties.kt | Add `reventsRetryEnabled` field to properties data class             |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationService.kt | Inject and use the new toggle when evaluating retry logic            |


<details>
<summary>Comments suppressed due to low confidence (2)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationService.kt:607**
* Add unit tests for the scenario where `reventsRetryEnabled` is false to ensure that no retry attempts are initiated when the toggle is disabled.
```
        if (retryImos.isNotEmpty() && properties.reventsRetryEnabled) {
```
**src/main/resources/application.properties:205**
* [nitpick] Update the project’s configuration reference or README to document the new `recalculation.revents-retry-enabled` property and its default behavior.
```
recalculation.revents-retry-enabled=true
```
</details>

### TeqJoostD — APPROVED (2025-07-15)

_No comment._

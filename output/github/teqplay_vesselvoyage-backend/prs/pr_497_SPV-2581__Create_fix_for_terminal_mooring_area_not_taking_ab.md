---
id: github:teqplay/vesselvoyage-backend:pr:497
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 497
title: 'SPV-2581: Create fix for terminal mooring area not taking absolute duration'
author: TeqJoostD
state: closed
date: '2025-05-13'
merged_at: '2025-05-20'
base_branch: develop
head_branch: SPV-2581
url: https://github.com/teqplay/vesselvoyage-backend/pull/497
labels: []
linked_issues: []
explicit_links: []
---
# PR #497: SPV-2581: Create fix for terminal mooring area not taking absolute duration

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/497  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `SPV-2581`  
**Created:** 2025-05-13  
**Merged:** 2025-05-20  

## Description

_No description._

## Commits

- `cf7fbfa0` **TeqJoostD** (2025-05-13): fix: create fix for terminal mooring area not taking absolute duration

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-05-13)

## Pull Request Overview

This PR addresses SPV-2581 by ensuring that terminal mooring area calculations use an absolute duration to correctly determine the closest mooring activity relative to the berth visit.  
- Updated test cases to cover various terminal mooring scenarios using a new parameterized test.  
- Modified the mooring selection logic to use the absolute difference in duration.

### Reviewed Changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated 1 comment.

| File | Description |
| ---- | ----------- |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGeneratorTest.kt | Adjusted test data setup and parameter ordering in calls to createBerthVisit for clarity.  |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGenerator.kt | Corrected the mooring selection by using an absolute duration difference to pick the closest mooring. |


<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGenerator.kt:309**
* The use of .abs() ensures the closest mooring is selected regardless of whether the mooring occurs before or after the berth visit; verify that this adjustment aligns precisely with the intended business logic for all edge cases.
```
.minByOrNull { mooring -> Duration.between(mooring.start.time, firstBerth.start.time).abs() }
```
</details>

### Darius-Wattimena — APPROVED (2025-05-16)

_No comment._

## Review Comments

### Copilot — 2025-05-13 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGeneratorTest.kt`

[nitpick] Since named arguments are used in createBerthVisit, consider keeping a uniform parameter ordering across tests for enhanced clarity and consistency.

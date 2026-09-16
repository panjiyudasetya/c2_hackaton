---
id: github:teqplay/vesselvoyage-backend:pr:482
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 482
title: SPV-2560 add tolerance to qualification of arrival/departure tugs
author: TeqJoostD
state: closed
date: '2025-04-23'
merged_at: '2025-04-30'
base_branch: develop
head_branch: SPV-2560
url: https://github.com/teqplay/vesselvoyage-backend/pull/482
labels: []
linked_issues: []
explicit_links: []
---
# PR #482: SPV-2560 add tolerance to qualification of arrival/departure tugs

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/482  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `SPV-2560`  
**Created:** 2025-04-23  
**Merged:** 2025-04-30  

## Description

Arrival/Departure tugs should have tolerance to help low AIS ships


\* - - - - - - - - - - - - [ Berth Visit ] - - - - - - - - - - - - *
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [_tolerance_]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [_tolerance_]
🚢-----------🔚   (Still is **arrival** tug because it ends in the tolerance)
                                        
\* - - - - - - - - - - - - [ Berth Visit ] - - - - - - - - - - - - *
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [_tolerance_]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [_tolerance_]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 🚢-----------🔚 (Still **departure** tug because it start in the tolerance)
                               

## Commits

- `2200bb09` **TeqJoostD** (2025-04-23): feat: add tolerance to qualification of arrival/departure tugs

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-04-23)

## Pull Request Overview

This PR adds tolerance logic for qualifying arrival and departure tugs to better support low AIS reporting ships. Key changes include:
- Updating test cases to use minute-based timings with tolerance windows.
- Introducing plusMinutes and minusMinutes extensions for time calculations.
- Adding tolerance constants and adjustments in tug qualification checks.

### Reviewed Changes

Copilot reviewed 3 out of 3 changed files in this pull request and generated no comments.

| File | Description |
| ---- | ----------- |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGeneratorTest.kt | Updates tests to use minute-based time points and verifies tug qualifications with tolerance windows. |
| src/main/kotlin/nl/teqplay/vesselvoyage/util/startEndUtils.kt | Adds overloaded time manipulation functions and tolerance-aware StartEnd methods. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGenerator.kt | Introduces tolerance constants and applies them to tug qualification logic. |


<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**src/test/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGeneratorTest.kt:388**
* [nitpick] Consider adding additional test cases to cover edge conditions for tug qualification at the exact tolerance boundaries, ensuring both arrival and departure scenarios are comprehensively validated.
```
TugSource(null, currentFinished, tug(toleranceTimeAfter, toleranceTimeAfter), qualifies = false),
```
</details>

### Darius-Wattimena — APPROVED (2025-04-28)

_No comment._

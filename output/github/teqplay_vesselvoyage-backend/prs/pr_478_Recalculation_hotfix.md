---
id: github:teqplay/vesselvoyage-backend:pr:478
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 478
title: Recalculation hotfix
author: TeqJoostD
state: closed
date: '2025-04-22'
merged_at: '2025-04-22'
base_branch: develop
head_branch: recalculation-hotfix
url: https://github.com/teqplay/vesselvoyage-backend/pull/478
labels: []
linked_issues: []
explicit_links: []
---
# PR #478: Recalculation hotfix

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/478  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `recalculation-hotfix`  
**Created:** 2025-04-22  
**Merged:** 2025-04-22  

## Description

_No description._

## Commits

- `23f5e5fc` **TeqJoostD** (2025-04-22): fix: fix test

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-04-22)

## Pull Request Overview

This hotfix adjusts the recalculation logic to handle cases where the status phase is STOPPED, ensuring that such cases are treated as errors.  
- Introduces a boolean flag (phaseStopped) to capture STOPPED statuses.  
- Modifies the logic to set the finished state to ERROR when either an IMO crash is detected or when the phase is STOPPED.


<details>
<summary>Comments suppressed due to low confidence (2)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationService.kt:678**
* Verify that treating a STOPPED phase as an error condition is intended in all cases, and consider adding an inline comment to clarify why the STOPPED phase should result in an error state.
```
val phaseStopped = status.phase == STOPPED
```
**src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationService.kt:683**
* Double-check that combining 'didImoCrash' with 'phaseStopped' for determining the error state is correct, and document the rationale if this behavior is intentional.
```
val finishedState = if (didImoCrash || phaseStopped) {
```
</details>

### leonjoosse — APPROVED (2025-04-22)

_No comment._

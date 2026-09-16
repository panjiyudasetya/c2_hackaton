---
id: github:teqplay/vesselvoyage-backend:pr:650
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 650
title: Change voyage merge back to visit logic
author: TeqJoostD
state: closed
date: '2025-10-24'
merged_at: '2025-10-28'
base_branch: develop
head_branch: voyage-merge-back
url: https://github.com/teqplay/vesselvoyage-backend/pull/650
labels: []
linked_issues: []
explicit_links: []
---
# PR #650: Change voyage merge back to visit logic

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/650  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `voyage-merge-back`  
**Created:** 2025-10-24  
**Merged:** 2025-10-28  

## Description

@Darius-Wattimena lets discuss if this is better

## Commits

- `8b60ccd6` **TeqJoostD** (2025-10-24): Change voyage merge back to visit logic
- `11fd2fed` **TeqJoostD** (2025-10-24): comment
- `a6450fc5` **TeqJoostD** (2025-10-27): change comments
- `26d05f4f` **TeqJoostD** (2025-10-27): fix: tests

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-24)

## Pull Request Overview

This PR modifies the logic for determining when to resume a previous visit after an End of Sea Passage (EOSP) event. The change reduces the allowed time window and removes a condition that previously checked for empty port area activities.

Key changes:
- Reduced the time threshold from 7 days to 1 day for resuming visits
- Removed the condition checking if `portAreaActivities` is empty
- Updated the comment to reflect the new 2-day threshold (note: comment says 2 days but code uses 1 day)

### TeqJoostD — COMMENTED (2025-10-27)

_No comment._

### TeqJoostD — COMMENTED (2025-10-27)

_No comment._

### Darius-Wattimena — APPROVED (2025-10-28)

_No comment._

## Review Comments

### Copilot — 2025-10-24 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageStartProcessor.kt`

The comment states '2 days' but the code uses `Duration.ofDays(1)` (1 day). Either update the comment to say '1 day' or change the code to `Duration.ofDays(2)` to match the intended behavior.
```suggestion
            if (isSameEosp && voyageDuration < Duration.ofDays(2)) {
```

### TeqJoostD — 2025-10-27 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageStartProcessor.kt`

change comment then merge and test

### TeqJoostD — 2025-10-27 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageStartProcessor.kt`

Change comment as well

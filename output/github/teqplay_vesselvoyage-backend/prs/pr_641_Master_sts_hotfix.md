---
id: github:teqplay/vesselvoyage-backend:pr:641
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 641
title: Master sts hotfix
author: TeqJoostD
state: closed
date: '2025-10-20'
merged_at: '2025-10-21'
base_branch: develop
head_branch: master-sts-hotfix
url: https://github.com/teqplay/vesselvoyage-backend/pull/641
labels: []
linked_issues: []
explicit_links: []
---
# PR #641: Master sts hotfix

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/641  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `master-sts-hotfix`  
**Created:** 2025-10-20  
**Merged:** 2025-10-21  

## Description

_No description._

## Commits

- `75ced3d1` **Darius Wattimena** (2025-10-08): Merge pull request #630 from teqplay/develop
  Hotfix 8 Oct 2025
- `7a9bd504` **Darius Wattimena** (2025-10-13): Merge pull request #634 from teqplay/develop
  Release 13 Oct 2025
- `155d3c32` **Joost Dambrink** (2025-10-14): Merge pull request #637 from teqplay/develop
  Release 14 October
- `fce38b82` **TeqJoostD** (2025-10-16): refactor: increase mongo persistence size
- `b1795541` **Joost Dambrink** (2025-10-16): Merge pull request #639 from teqplay/mongo-increase
  Mongo persistence increase
- `9dc5245b` **TeqJoostD** (2025-10-17): add maximum duration for resuming visit

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-20)

## Pull Request Overview

Adds a 7‑day time gap threshold before resuming an End Of Sea Passage visit and increases MongoDB persistence storage size.
- Introduces duration calculation and conditional check to prevent resuming stale visits (>7 days).
- Increases MongoDB persistent volume size from 400Gi to 430Gi.

### Reviewed Changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated 4 comments.

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageStartProcessor.kt | Adds duration logic and 7‑day threshold to resume previous visit. |
| helm/values.processing-prod.yaml | Adjusts MongoDB persistence storage size setting. |

### michel-teqplay — APPROVED (2025-10-20)

_No comment._

## Review Comments

### Copilot — 2025-10-20 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageStartProcessor.kt`

visitEnd is nullable (due to the safe call on end?.time) but passed directly to Duration.between, which expects non-null Temporal values; this will not compile (type mismatch) or will throw if forced. Guard with visitEnd ?: return, or wrap in visitEnd?.let { val gap = Duration.between(it, voyageEnd) ... } and skip resuming when visitEnd is absent.

### Copilot — 2025-10-20 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageStartProcessor.kt`

voyageDuration does not clearly convey that it represents the gap since the previous visit ended; a more explicit name like timeSincePreviousVisitEnd or gapSincePreviousVisitEnd would improve clarity.

### Copilot — 2025-10-20 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageStartProcessor.kt`

New 7-day threshold logic should be covered by tests for boundaries (exactly 7 days, just under, just over) to ensure correct resume behavior and prevent regressions.

### Copilot — 2025-10-20 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageStartProcessor.kt`

Magic number 7 (days) should be extracted to a named constant (e.g., MAX_VISIT_RESUME_GAP_DAYS) to document intent and ease future adjustments.

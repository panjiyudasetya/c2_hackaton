---
id: github:teqplay/vesselvoyage-backend:pr:439
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 439
title: SPV-2543 Retry mechanism for illegal merging errors
author: TeqJoostD
state: closed
date: '2025-03-04'
merged_at: '2025-03-04'
base_branch: develop
head_branch: SPV-2543
url: https://github.com/teqplay/vesselvoyage-backend/pull/439
labels: []
linked_issues: []
explicit_links: []
---
# PR #439: SPV-2543 Retry mechanism for illegal merging errors

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/439  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `SPV-2543`  
**Created:** 2025-03-04  
**Merged:** 2025-03-04  

## Description

Changelist:
- Rework error mechanism to have warning level errors and partially fail the scenario based on the type of errors
- Create retry mechanism for ships with illegal windows (thus cannot be merged)

## Commits

- `bd475de1` **TeqJoostD** (2025-03-03): - feat: rework revents error mechanism
  - feat: add retry mechanism for revents on certain errors
- `fb5397ba` **TeqJoostD** (2025-03-03): feat: fix
- `f9f523e0` **TeqJoostD** (2025-03-03): feat: do full recalc instead of partial
- `eb4e6726` **TeqJoostD** (2025-03-03): fix: remove redundancy
- `40740a39` **TeqJoostD** (2025-03-03): fix: make sure revents checks all scenarios instead of first
- `c75e689d` **TeqJoostD** (2025-03-04): fix: use stable version
- `ac3e8fae` **Darius Wattimena** (2025-03-04): Merge branch 'develop' into SPV-2543
- `002a196d` **TeqJoostD** (2025-03-04): fix: add continue instead of return
- `16e2155d` **TeqJoostD** (2025-03-04): Merge remote-tracking branch 'origin/SPV-2543' into SPV-2543
- `53f5f404` **TeqJoostD** (2025-03-04): fix: ktlint

## Reviews

### Darius-Wattimena — CHANGES_REQUESTED (2025-03-04)

_No comment._

### Darius-Wattimena — APPROVED (2025-03-04)

![](https://media.makeameme.org/created/lgtm-19c36d.jpg)

## Review Comments

### Darius-Wattimena — 2025-03-04 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationService.kt`

Shouldn't all those `return` be a `continue`?

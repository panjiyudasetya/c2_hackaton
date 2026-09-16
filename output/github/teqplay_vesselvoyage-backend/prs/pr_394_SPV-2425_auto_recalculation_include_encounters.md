---
id: github:teqplay/vesselvoyage-backend:pr:394
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 394
title: SPV-2425 auto recalculation include encounters
author: Darius-Wattimena
state: closed
date: '2025-01-17'
merged_at: '2025-01-24'
base_branch: develop
head_branch: SPV-2425-encounter-as-well-on-auto-recal
url: https://github.com/teqplay/vesselvoyage-backend/pull/394
labels: []
linked_issues: []
explicit_links: []
---
# PR #394: SPV-2425 auto recalculation include encounters

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/394  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `SPV-2425-encounter-as-well-on-auto-recal`  
**Created:** 2025-01-17  
**Merged:** 2025-01-24  

## Description

This PR also includes removal of any logic that was used to override the merging back esof with encounters from event history. As that behaviour isn't possible anymore as we always run revents with the new encounter monitor changes

## Commits

- `7e8802ec` **Darius Wattimena** (2025-01-17): Add encounter monitor to automated scenario creation
- `0aa780ab` **Darius Wattimena** (2025-01-17): Removed logic to override encounters by events as they will always be running with encounters enabled
- `c915b9d6` **Darius Wattimena** (2025-01-17): ktlint
- `fc9dcd3b` **Darius Wattimena** (2025-01-21): Merge branch 'refs/heads/develop' into SPV-2425-encounter-as-well-on-auto-recal
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingRecalculateV2Controller.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/RecalculationOverwriteService.kt
  #	src/test/kotlin/nl/teqplay/vesselvoyage/service/recalculation/RecalculationOverwriteServiceTest.kt
- `3514a3a1` **Darius Wattimena** (2025-01-23): Removed the unneeded platform calls and made it so we log a bit more
- `59622d4e` **Darius Wattimena** (2025-01-23): Merge branch 'refs/heads/develop' into SPV-2425-encounter-as-well-on-auto-recal

## Reviews

### TeqJoostD — APPROVED (2025-01-23)

_No comment._

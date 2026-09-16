---
id: github:teqplay/vesselvoyage-backend:pr:764
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 764
title: Release 22 Apr 2026
author: Darius-Wattimena
state: closed
date: '2026-04-21'
merged_at: '2026-04-21'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/764
labels: []
linked_issues: []
explicit_links: []
---
# PR #764: Release 22 Apr 2026

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/764  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2026-04-21  
**Merged:** 2026-04-21  

## Description

_No description._

## Commits

- `dde419f2` **Jamie de Leest** (2026-04-07): update resources for vesselvoyage processing dev
- `c942bf37` **Jamie de Leest** (2026-04-14): update resources
- `d8183e0f` **Jamie de Leest** (2026-04-14): Merge branch 'develop' into DEV-1640-update-resources
  # Conflicts:
  #	helm/values.processing-data.yaml
- `a438afb7` **Jamie de Leest** (2026-04-16): update resources for dev and prod to round numbers
- `a3077545` **jamie-teqplay** (2026-04-16): Merge pull request #761 from teqplay/DEV-1640-update-resources
  DEV-1640 update resources
- `43aa8d63` **Darius Wattimena** (2026-04-17): Fixed an issue where ESOF related data would be missing in the published data to RabbitMQ
- `cb576fd7` **Darius Wattimena** (2026-04-17): Fix debug logging so it shows the correct field
- `fdd09a23` **Darius Wattimena** (2026-04-17): Rework fix so we don't need to do an additional db lookup when we already know the current esof of the updated visit or voyage
- `8afd1acc` **Darius Wattimena** (2026-04-17): Adjusted the tests so they take into account the issue with the missing esof
- `5cb37f29` **Darius Wattimena** (2026-04-17): ktlint
- `e5f54076` **Darius Wattimena** (2026-04-17): Add more tests to make sure all edge cases are covered
- `a0ceebab` **Darius Wattimena** (2026-04-20): Merge pull request #762 from teqplay/TCC-801-fix-missing-esof-in-published-sof
  TCC-801 fix missing esof in published sof

## Reviews

### TeqJoostD — APPROVED (2026-04-21)

_No comment._

### augmentcode[bot] — COMMENTED (2026-04-21)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

## Comments

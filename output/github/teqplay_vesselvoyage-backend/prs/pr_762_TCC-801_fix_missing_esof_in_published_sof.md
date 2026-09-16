---
id: github:teqplay/vesselvoyage-backend:pr:762
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 762
title: TCC-801 fix missing esof in published sof
author: Darius-Wattimena
state: closed
date: '2026-04-17'
merged_at: '2026-04-20'
base_branch: develop
head_branch: TCC-801-fix-missing-esof-in-published-sof
url: https://github.com/teqplay/vesselvoyage-backend/pull/762
labels: []
linked_issues: []
explicit_links: []
---
# PR #762: TCC-801 fix missing esof in published sof

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/762  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-801-fix-missing-esof-in-published-sof`  
**Created:** 2026-04-17  
**Merged:** 2026-04-20  

## Description

_No description._

## Commits

- `43aa8d63` **Darius Wattimena** (2026-04-17): Fixed an issue where ESOF related data would be missing in the published data to RabbitMQ
- `cb576fd7` **Darius Wattimena** (2026-04-17): Fix debug logging so it shows the correct field
- `fdd09a23` **Darius Wattimena** (2026-04-17): Rework fix so we don't need to do an additional db lookup when we already know the current esof of the updated visit or voyage
- `8afd1acc` **Darius Wattimena** (2026-04-17): Adjusted the tests so they take into account the issue with the missing esof
- `5cb37f29` **Darius Wattimena** (2026-04-17): ktlint
- `e5f54076` **Darius Wattimena** (2026-04-17): Add more tests to make sure all edge cases are covered

## Reviews

### augmentcode[bot] — COMMENTED (2026-04-17)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### michel-teqplay — APPROVED (2026-04-20)

_No comment._

## Comments

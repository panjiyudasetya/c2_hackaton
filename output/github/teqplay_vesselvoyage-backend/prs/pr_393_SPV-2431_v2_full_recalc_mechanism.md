---
id: github:teqplay/vesselvoyage-backend:pr:393
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 393
title: SPV-2431 v2 full recalc mechanism
author: Darius-Wattimena
state: closed
date: '2025-01-17'
merged_at: '2025-01-17'
base_branch: develop
head_branch: SPV-2431-v2-full-recalc-mechanism
url: https://github.com/teqplay/vesselvoyage-backend/pull/393
labels: []
linked_issues: []
explicit_links: []
---
# PR #393: SPV-2431 v2 full recalc mechanism

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/393  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `SPV-2431-v2-full-recalc-mechanism`  
**Created:** 2025-01-17  
**Merged:** 2025-01-17  

## Description

I still want to add the 2nd step on top of this which is triggering revents as an optional extra to schedule. But that will follow in the next PR

## Commits

- `32a47d7f` **Darius Wattimena** (2025-01-17): Added support to regenerate a ship story which fully replaces existing data of a ship
- `f39728b0` **Darius Wattimena** (2025-01-17): Fixed a small bug in the ship status service where counting of the updated statuses wouldn't work as expected
- `51c045bb` **Darius Wattimena** (2025-01-17): Extended the logic to also delete the ship traces as well so we don't end up with unneeded traces in the database
- `54caa89c` **Darius Wattimena** (2025-01-17): Merge branch 'refs/heads/develop' into SPV-2431-v2-full-recalc-mechanism
- `bc538874` **Darius Wattimena** (2025-01-17): Added an extra test case to ensure that we don't delete any data if the ship we want to recalculate is still in its initial state
- `869c6516` **Darius Wattimena** (2025-01-17): ktlint

## Reviews

### TeqJoostD — APPROVED (2025-01-17)

_No comment._

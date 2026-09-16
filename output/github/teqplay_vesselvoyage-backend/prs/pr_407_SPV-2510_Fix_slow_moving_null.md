---
id: github:teqplay/vesselvoyage-backend:pr:407
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 407
title: SPV-2510 Fix slow moving null
author: Darius-Wattimena
state: closed
date: '2025-01-31'
merged_at: '2025-02-03'
base_branch: develop
head_branch: fix-slow-moving-null
url: https://github.com/teqplay/vesselvoyage-backend/pull/407
labels: []
linked_issues: []
explicit_links: []
---
# PR #407: SPV-2510 Fix slow moving null

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/407  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `fix-slow-moving-null`  
**Created:** 2025-01-31  
**Merged:** 2025-02-03  

## Description

While the model was already prepared, we found out that the internal model always sets the slow steaming to `[]` even when we still have to request the drift predictor to find the slow moving periods.

## Commits

- `e2982d96` **Darius Wattimena** (2025-01-31): Fix an issue where the slow moving periods are set to an empty list when we still have to calculate them
- `8f4b2086` **Darius Wattimena** (2025-01-31): Adjusted the tests to reflect the expected null when slow moving periods are not calculated yet
- `704da57d` **Darius Wattimena** (2025-01-31): Updated comment on field with expected states of data
- `99193fe0` **Darius Wattimena** (2025-01-31): ktlint

## Reviews

### leonjoosse — APPROVED (2025-02-03)

_No comment._

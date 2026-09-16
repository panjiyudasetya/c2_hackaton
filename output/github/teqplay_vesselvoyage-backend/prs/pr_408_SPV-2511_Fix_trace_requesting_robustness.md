---
id: github:teqplay/vesselvoyage-backend:pr:408
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 408
title: SPV-2511 Fix trace requesting robustness
author: Darius-Wattimena
state: closed
date: '2025-01-31'
merged_at: '2025-02-03'
base_branch: develop
head_branch: fix-trace-requesting-robustness
url: https://github.com/teqplay/vesselvoyage-backend/pull/408
labels: []
linked_issues: []
explicit_links: []
---
# PR #408: SPV-2511 Fix trace requesting robustness

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/408  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `fix-trace-requesting-robustness`  
**Created:** 2025-01-31  
**Merged:** 2025-02-03  

## Description

_No description._

## Commits

- `08e51056` **Darius Wattimena** (2025-01-31): Fix an issue where requesting traces for slow moving would sometimes result in threads crashing because of an exception
- `2f919136` **Darius Wattimena** (2025-01-31): Also make sure not to crash when calculating ship trace in the background

## Reviews

### TeqJoostD — APPROVED (2025-02-03)

_No comment._

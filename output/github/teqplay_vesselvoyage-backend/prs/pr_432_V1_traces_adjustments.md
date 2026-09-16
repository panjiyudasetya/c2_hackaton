---
id: github:teqplay/vesselvoyage-backend:pr:432
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 432
title: V1 traces adjustments
author: Darius-Wattimena
state: closed
date: '2025-02-25'
merged_at: '2025-02-25'
base_branch: develop
head_branch: v1-traces-adjustments
url: https://github.com/teqplay/vesselvoyage-backend/pull/432
labels: []
linked_issues: []
explicit_links: []
---
# PR #432: V1 traces adjustments

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/432  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `v1-traces-adjustments`  
**Created:** 2025-02-25  
**Merged:** 2025-02-25  

## Description

Reverts back some changes I've done for the memory stability fixes. Some of them ended up being too much making traces not be correct in PortReporter

## Commits

- `ad0849e7` **Darius Wattimena** (2025-02-25): Revert back change for the max age of V1 traces to be using 10 days again

## Reviews

### leonjoosse — APPROVED (2025-02-25)

_No comment._

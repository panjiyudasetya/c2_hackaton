---
id: github:teqplay/vesselvoyage-backend:pr:420
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 420
title: SPV-2543 recalc ships in batch endpoint
author: Darius-Wattimena
state: closed
date: '2025-02-14'
merged_at: '2025-02-14'
base_branch: develop
head_branch: SPV-2543-recalc-ships
url: https://github.com/teqplay/vesselvoyage-backend/pull/420
labels: []
linked_issues: []
explicit_links: []
---
# PR #420: SPV-2543 recalc ships in batch endpoint

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/420  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `SPV-2543-recalc-ships`  
**Created:** 2025-02-14  
**Merged:** 2025-02-14  

## Description

This PR adds 1 endpoint to schedule revents for multiple ships (+ some cleanup)

## Commits

- `476e67d1` **Darius Wattimena** (2025-02-14): Added an endpoint to trigger revents for a batch of ships
- `998e42d3` **Darius Wattimena** (2025-02-14): Added support for validation annotations
- `099d6664` **Darius Wattimena** (2025-02-14): Made sure to validate that the array of imos is not empty
- `d5505c7f` **Darius Wattimena** (2025-02-14): Adjust frequency of checking revents to be done once every minute

## Reviews

### TeqJoostD — APPROVED (2025-02-14)

_No comment._

---
id: github:teqplay/vesselvoyage-backend:pr:520
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 520
title: '🦊 Hotfox: align client return type'
author: leonjoosse
state: closed
date: '2025-06-02'
merged_at: '2025-06-02'
base_branch: master
head_branch: hotfox-client-return-types
url: https://github.com/teqplay/vesselvoyage-backend/pull/520
labels: []
linked_issues: []
explicit_links: []
---
# PR #520: 🦊 Hotfox: align client return type

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/520  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `master` ← `hotfox-client-return-types`  
**Created:** 2025-06-02  
**Merged:** 2025-06-02  

## Description

[Copilot summary]

This pull request includes a small change to the `VesselVoyageClient` class in `client/src/main/kotlin/nl/teqplay/vesselvoyage/client/VesselVoyageClient.kt`. The return type of the `findByPortBatch` method was updated from `VisitsByPort` to `Array<VisitsByPort>` to better align with the expected response format.

## Commits

- `a85d1792` **leonj** (2025-06-02): Fix return type in VesselVoyageClient for visits.findByPortBatch

## Reviews

### Darius-Wattimena — APPROVED (2025-06-02)

_No comment._

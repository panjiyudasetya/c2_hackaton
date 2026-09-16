---
id: github:teqplay/vesselvoyage-backend:pr:424
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 424
title: SPV-2508 fix unresolved port id
author: Darius-Wattimena
state: closed
date: '2025-02-17'
merged_at: '2025-02-17'
base_branch: develop
head_branch: SPV-2508-fix-unresolved-port-id
url: https://github.com/teqplay/vesselvoyage-backend/pull/424
labels: []
linked_issues: []
explicit_links: []
---
# PR #424: SPV-2508 fix unresolved port id

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/424  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `SPV-2508-fix-unresolved-port-id`  
**Created:** 2025-02-17  
**Merged:** 2025-02-17  

## Description

Was testing the feature, but found out we resolve the previous port wrong as the values contain the `.eosp` suffix as well, which was not taken care of.

## Commits

- `ebba0d7d` **Darius Wattimena** (2025-02-17): Fix an issue where the previous port isn't correctly resolved

## Reviews

### leonjoosse — APPROVED (2025-02-17)

_No comment._

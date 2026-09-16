---
id: github:teqplay/vesselvoyage-backend:pr:390
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 390
title: SPV-2411 Add an `updatedAt` timestamp to entries and esof
author: Darius-Wattimena
state: closed
date: '2025-01-13'
merged_at: '2025-01-15'
base_branch: develop
head_branch: SPV-2411-update-at-timestamp
url: https://github.com/teqplay/vesselvoyage-backend/pull/390
labels: []
linked_issues: []
explicit_links: []
---
# PR #390: SPV-2411 Add an `updatedAt` timestamp to entries and esof

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/390  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `SPV-2411-update-at-timestamp`  
**Created:** 2025-01-13  
**Merged:** 2025-01-15  

## Description

Old PR https://bitbucket.org/teqplay/vesselvoyage-backend/pull-requests/396

## Commits

- `a2c8701d` **Darius Wattimena** (2024-12-09): Added updated at field to the internal esof visit and voyage models
- `a16d10a3` **Darius Wattimena** (2024-12-09): Add the updatedAt timestamp to all processors results and adjusted all tests to ensure this updated time is correctly set
- `b4ed9502` **Darius Wattimena** (2024-12-09): ktlint
- `90573d7f` **Darius Wattimena** (2025-01-13): Merge branch 'refs/heads/develop' into SPV-2411-update-at-timestamp
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/encounter/EncounterBaseProcessor.kt
- `cd0a336e` **Darius Wattimena** (2025-01-13): Fix compile issue after merging latest develop

## Reviews

### TeqJoostD — APPROVED (2025-01-15)

_No comment._

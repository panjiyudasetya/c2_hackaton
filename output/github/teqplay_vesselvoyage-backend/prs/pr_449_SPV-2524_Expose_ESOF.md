---
id: github:teqplay/vesselvoyage-backend:pr:449
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 449
title: SPV-2524 Expose ESOF
author: TeqJoostD
state: closed
date: '2025-03-14'
merged_at: '2025-03-17'
base_branch: develop
head_branch: SPV-2524
url: https://github.com/teqplay/vesselvoyage-backend/pull/449
labels: []
linked_issues: []
explicit_links: []
---
# PR #449: SPV-2524 Expose ESOF

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/449  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `SPV-2524`  
**Created:** 2025-03-14  
**Merged:** 2025-03-17  

## Description

_No description._

## Commits

- `ad8e0ba2` **TeqJoostD** (2025-03-12): -feat: add esof controller
- `53d84ec4` **TeqJoostD** (2025-03-17): Merge remote-tracking branch 'origin/SPV-2524' into SPV-2524
- `32adaae3` **TeqJoostD** (2025-03-17): -fix: remove usage of internal models

## Reviews

### Darius-Wattimena — CHANGES_REQUESTED (2025-03-14)

_No comment._

### Darius-Wattimena — APPROVED (2025-03-17)

_No comment._

## Review Comments

### Darius-Wattimena — 2025-03-14 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/Encounter.kt`

You shouldn't extend the `StartEnd` here as that is the model used in the internal models.

### Darius-Wattimena — 2025-03-14 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/Encounter.kt`

This is the wrong `LocationTime` there is one in this package already so the import can go

### Darius-Wattimena — 2025-03-14 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/ShipToShipTransfer.kt`

Same here wrong import + there shouldn't be a `StartEnd` 

### Darius-Wattimena — 2025-03-14 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/SlowMovingPeriod.kt`

Probably fine to use the internal model for now but it would be nice to eventually have a custom model for this.

### Darius-Wattimena — 2025-03-14 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/SlowMovingPeriod.kt`

Same here wrong import + there shouldn't be a StartEnd

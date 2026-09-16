---
id: github:teqplay/vesselvoyage-backend:pr:436
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 436
title: SPV-2549 pilot times for anchor only
author: Darius-Wattimena
state: closed
date: '2025-02-27'
merged_at: '2025-02-28'
base_branch: develop
head_branch: SPV-2549-pilot-times-for-anchor-only
url: https://github.com/teqplay/vesselvoyage-backend/pull/436
labels: []
linked_issues: []
explicit_links: []
---
# PR #436: SPV-2549 pilot times for anchor only

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/436  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `SPV-2549-pilot-times-for-anchor-only`  
**Created:** 2025-02-27  
**Merged:** 2025-02-28  

## Description

https://vesselvoyagedev.teqplay.nl/#/ships/9278052/sof/1df233ea-a888-4adf-99e2-c4061f2d559e.VISIT?mode=period&months=3 doesn't have a pilot inbound and outbound. With this change you will now have:
- Pilot inbound before the first anchor stop when there is no berth stop
- Pilot outbound after the last anchor stop when there is no berth stop

## Commits

- `e8c97762` **Darius Wattimena** (2025-02-27): Adjusted logic to also take into account the first anchor time for pilot detection when we never went to a berth
- `c57226cf` **Darius Wattimena** (2025-02-27): Adjusted existing test cases to support this new logic
- `69488181` **Darius Wattimena** (2025-02-27): Added additional test cases for inbound detection with the extra anchor area
- `e3b5f9bd` **Darius Wattimena** (2025-02-27): Added the possible cases for outbound pilots
- `9450a56d` **Darius Wattimena** (2025-02-27): Remove unused import

## Reviews

### TeqJoostD — APPROVED (2025-02-28)

_No comment._

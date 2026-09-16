---
id: github:teqplay/vesselvoyage-backend:pr:388
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 388
title: SPV-2467 departure tug flipped event
author: Darius-Wattimena
state: closed
date: '2025-01-08'
merged_at: '2025-01-13'
base_branch: develop
head_branch: SPV-2467-departure-tug-flipped-event
url: https://github.com/teqplay/vesselvoyage-backend/pull/388
labels: []
linked_issues: []
explicit_links: []
---
# PR #388: SPV-2467 departure tug flipped event

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/388  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `SPV-2467-departure-tug-flipped-event`  
**Created:** 2025-01-08  
**Merged:** 2025-01-13  

## Description

Made VesselVoyage more robust to support events (like the one in the screenshot) where the IMO and MMSI is flipped.
This means the service vessel identifiers are wrongly placed. We still need to fix this on the side of the EncounterMonitor but doing it here as a first start.

![Screenshot 2025-01-08 at 18 14 54](https://github.com/user-attachments/assets/791b9115-9d25-4d0a-b4f2-29458ee59a46)


## Commits

- `8e39729a` **Darius Wattimena** (2025-01-08): Fix an issue where tug departures wouldn't be selected correctly when the service vessel mmsi and imo were placed in the incorrect field
- `ef9fefa7` **Darius Wattimena** (2025-01-08): Added a test to cover the new behaviour and to not do anything when the wrong imo is provided
- `70a05bb9` **Darius Wattimena** (2025-01-08): ktlint

## Reviews

### TeqJoostD — APPROVED (2025-01-09)

_No comment._

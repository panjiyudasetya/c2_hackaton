---
id: github:teqplay/vesselvoyage-backend:pr:467
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 467
title: 'SPV-2575: PTO SOF drifting around anchorages'
author: leonjoosse
state: closed
date: '2025-03-25'
merged_at: '2025-04-04'
base_branch: develop
head_branch: SPV-2575-pto-sof-drifting-around-anchorages
url: https://github.com/teqplay/vesselvoyage-backend/pull/467
labels: []
linked_issues: []
explicit_links: []
---
# PR #467: SPV-2575: PTO SOF drifting around anchorages

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/467  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `SPV-2575-pto-sof-drifting-around-anchorages`  
**Created:** 2025-03-25  
**Merged:** 2025-04-04  

## Description

In the PTO SOF:
This implementation discards less slow moving periods around a vessel anchoring, by removing the intersecting part. That may result in more slow moving periods than originally in the visit SOF.

## Commits

- `f169c5f5` **leonj** (2025-03-19): PTO SOF: when filtering out slow moving segments, do not fully remove segments that overlap any anchor stop. Instead, do return the parts of slow moving segments that do not overlap the anchor stop
- `afe44447` **leonj** (2025-03-19): Merge branch 'develop' into SPV-2575-pto-sof-drifting-around-anchorages
- `4c73391d` **leonj** (2025-03-19): Merge branch 'develop' into SPV-2575-pto-sof-drifting-around-anchorages
- `de0fb15e` **leonj** (2025-03-25): Merge branch 'develop' into SPV-2575-pto-sof-drifting-around-anchorages
- `06c4d0f4` **leonj** (2025-04-02): Merge branch 'develop' into SPV-2575-pto-sof-drifting-around-anchorages

## Reviews

### Darius-Wattimena — APPROVED (2025-03-26)

_No comment._

---
id: github:teqplay/vesselvoyage-backend:pr:425
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 425
title: 'SPV-2518: Remove slow moving periods from PTO SOF that overlap berth visits
  and anchor stops'
author: leonjoosse
state: closed
date: '2025-02-17'
merged_at: '2025-02-18'
base_branch: develop
head_branch: SPV-2518-pto-sof-slow-moving-ignore-berth-anchor-stops
url: https://github.com/teqplay/vesselvoyage-backend/pull/425
labels: []
linked_issues: []
explicit_links: []
---
# PR #425: SPV-2518: Remove slow moving periods from PTO SOF that overlap berth visits and anchor stops

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/425  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `SPV-2518-pto-sof-slow-moving-ignore-berth-anchor-stops`  
**Created:** 2025-02-17  
**Merged:** 2025-02-18  

## Description

_No description._

## Commits

- `52009685` **leonj** (2025-02-14): PTO SOF: Filter out slow moving periods that overlap a berth visit or anchor stop. Let NewSlowMovingPeriod and AnchorStopInfo extend StartEnd interface to allow .overlaps() util functions
- `822ab293` **leonj** (2025-02-14): Extend StartEnd.overlaps() to also return true when A encloses B, or vice versa. Before, it only returned true when one started or ended in the other, but that did not cover an enclosing case.
- `8d2dae5d` **leonj** (2025-02-17): Merge branch 'develop' into SPV-2518-pto-sof-slow-moving-ignore-berth-anchor-stops
- `cb93c585` **leonj** (2025-02-18): Also use lock stops to filter out slow moving periods in the PTO SOF (next to berth visits and anchor stops)

## Reviews

### Darius-Wattimena — DISMISSED (2025-02-17)

_No comment._

### Darius-Wattimena — APPROVED (2025-02-18)

_No comment._

## Comments

### leonjoosse — 2025-02-18

Added the lock stops as well to filter out slow moving periods

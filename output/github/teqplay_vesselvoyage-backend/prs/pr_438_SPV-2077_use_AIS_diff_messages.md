---
id: github:teqplay/vesselvoyage-backend:pr:438
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 438
title: SPV-2077 use AIS diff messages
author: Darius-Wattimena
state: closed
date: '2025-03-03'
merged_at: '2025-03-04'
base_branch: develop
head_branch: SPV-2077-diff-messages
url: https://github.com/teqplay/vesselvoyage-backend/pull/438
labels: []
linked_issues: []
explicit_links: []
---
# PR #438: SPV-2077 use AIS diff messages

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/438  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `SPV-2077-diff-messages`  
**Created:** 2025-03-03  
**Merged:** 2025-03-04  

## Description

Adjusted all the logic to support diff messages instead of using the full blown historic messages.

This does require some care when deploying as I have to delete the old `vesselvoyage` consumer on the `ais-stream:history` stream.

In terms of performance:
- Historic messages = ~20k/second
- Diff message = ~100k/second

I didn't really check how much impact this has on the memory usage of VesselVoyage, but it might be something interesting to look at once deployed.

## Commits

- `cb2d4238` **Darius Wattimena** (2025-03-03): Changed the dependency to make use of the diff one instead of historic
- `67b71d83` **Darius Wattimena** (2025-03-03): Simplified lot of the AIS processing code to make use of diff messages instead of handling historic ones

## Reviews

### TeqJoostD — APPROVED (2025-03-04)

_No comment._

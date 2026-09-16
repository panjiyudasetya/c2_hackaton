---
id: github:teqplay/vesselvoyage-backend:pr:418
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 418
title: SPV-2513 Support TUG_WAITING_DEPARTURE in vesselvoyage
author: TeqJoostD
state: closed
date: '2025-02-13'
merged_at: '2025-02-21'
base_branch: develop
head_branch: SPV-2514
url: https://github.com/teqplay/vesselvoyage-backend/pull/418
labels: []
linked_issues: []
explicit_links: []
---
# PR #418: SPV-2513 Support TUG_WAITING_DEPARTURE in vesselvoyage

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/418  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `SPV-2514`  
**Created:** 2025-02-13  
**Merged:** 2025-02-21  

## Description

Changelist:
- Support for TUG_WAITING_DEPARTURE encounters in the Visit
- Support for TUG_WAITING_DEPARTURE in the PTO SOF
    - Including post-processing (Removing ghost encounters)
- Aligning berth visit departure start with TUG_WAITING_DEPARTURE encounters

## Commits

- `627ac64a` **TeqJoostD** (2025-02-12): feat: allow tug_waiting_departure events to be processed
- `1330c3ee` **TeqJoostD** (2025-02-12): fix
- `ef2da2a8` **TeqJoostD** (2025-02-12): fix: adjust tests
- `fd7288d4` **TeqJoostD** (2025-02-12): feat: filter out tug_waiting_departure events with no actual tug event
- `045b8a70` **TeqJoostD** (2025-02-12): fix: ktlint
- `2d3dcbfe` **TeqJoostD** (2025-02-13): fix: make sure only tug_waiting_departures are allowed when tug has happened after
- `4f98017d` **TeqJoostD** (2025-02-13): fix: ktlint :(
- `b77fe8d5` **TeqJoostD** (2025-02-13): feat: implement filtering of tugs in on the pto SOF side
- `c256023c` **TeqJoostD** (2025-02-13): fix: remove unused functions
- `5b80098f` **TeqJoostD** (2025-02-13): fix: ktlint
- `2a1623a2` **TeqJoostD** (2025-02-13): fix: broken test
- `4a7c045c` **TeqJoostD** (2025-02-13): feat: align the berth tug start times with the waiting departure encounters
- `572d75a7` **TeqJoostD** (2025-02-13): fix: pass the right encounter info
- `7629a9ae` **TeqJoostD** (2025-02-20): Merge branch 'develop' into SPV-2514
- `4dca6be8` **TeqJoostD** (2025-02-20): feat: adding tests

## Reviews

### Darius-Wattimena — CHANGES_REQUESTED (2025-02-14)

Could you add a test ensureing that the correct tug time is taken into account for when we generate the PTO SOF. Other than that LGTM.

### Darius-Wattimena — APPROVED (2025-02-20)

_No comment._

## Comments

### TeqJoostD — 2025-02-13

Please ignore the amount of commits, I think this is a bug in GitHub???

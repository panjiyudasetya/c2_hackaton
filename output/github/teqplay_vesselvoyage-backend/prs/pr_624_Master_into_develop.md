---
id: github:teqplay/vesselvoyage-backend:pr:624
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 624
title: Master into develop
author: TeqJoostD
state: closed
date: '2025-10-03'
merged_at: '2025-10-03'
base_branch: develop
head_branch: master
url: https://github.com/teqplay/vesselvoyage-backend/pull/624
labels: []
linked_issues: []
explicit_links: []
---
# PR #624: Master into develop

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/624  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `master`  
**Created:** 2025-10-03  
**Merged:** 2025-10-03  

## Description

_No description._

## Commits

- `80c01c00` **Darius Wattimena** (2025-08-13): Merge pull request #591 from teqplay/develop
  Release 2025-08-13
- `8ff04e1f` **Joost Dambrink** (2025-08-19): Merge pull request #596 from teqplay/develop
  Release 19/08/2025
- `501e5713` **Darius Wattimena** (2025-08-27): Merge pull request #600 from teqplay/develop
  Release 27-08-2025
- `435ff7f5` **Darius Wattimena** (2025-09-03): Merge pull request #602 from teqplay/develop
  Release 3 Sep 2025
- `98617302` **Darius Wattimena** (2025-09-10): Merge pull request #603 from teqplay/develop
  Release 10 Sep 2025
- `11a31ea1` **Darius Wattimena** (2025-09-16): Merge pull request #606 from teqplay/develop
  Release 16 Sep 2025
- `358ab41a` **Darius Wattimena** (2025-09-18): Merge pull request #609 from teqplay/develop
  Release 18 Sep 2025
- `b234861d` **Darius Wattimena** (2025-09-19): Merge pull request #611 from teqplay/develop
  Release 19 Sep 2025
- `1b7f8437` **Darius Wattimena** (2025-09-22): Merge pull request #613 from teqplay/develop
  Release 22 Sep 2025
- `62c6f8a7` **jamie-teqplay** (2025-09-26): Release 26-09-2025 Merge pull request #615 from teqplay/develop
  Release 26-09-2025
- `8d5b6333` **jamie-teqplay** (2025-09-29): Release 29-09-2025 Merge pull request #616 from teqplay/develop
  Release 29-09-2025
- `6c4a4d27` **TeqJoostD** (2025-10-03): fix: Sort entries before assuming the entries are sorted when merging back revents vesselvoyage changes.
- `e41c8d4c` **Joost Dambrink** (2025-10-03): Merge pull request #622 from teqplay/revents-merge-hotfix
  fix: Sort entries before assuming the entries are sorted when merging…

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-03)

## Pull Request Overview

This PR merges changes from master into develop branch, specifically updating the `EntriesMergeService` to sort entries by start time before processing them. This ensures consistent ordering when merging vessel voyage entries within a time window.

### Key Changes
- Added sorting of entries by start time at the beginning of the merge process
- Updated all subsequent references to use the sorted entries instead of the original unsorted list

### Darius-Wattimena — APPROVED (2025-10-03)

_No comment._

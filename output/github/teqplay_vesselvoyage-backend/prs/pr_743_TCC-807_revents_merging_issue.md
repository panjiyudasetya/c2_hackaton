---
id: github:teqplay/vesselvoyage-backend:pr:743
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 743
title: TCC-807 revents merging issue
author: Darius-Wattimena
state: closed
date: '2026-03-19'
merged_at: '2026-03-27'
base_branch: develop
head_branch: TCC-807-revents-merging-issue
url: https://github.com/teqplay/vesselvoyage-backend/pull/743
labels: []
linked_issues: []
explicit_links: []
---
# PR #743: TCC-807 revents merging issue

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/743  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-807-revents-merging-issue`  
**Created:** 2026-03-19  
**Merged:** 2026-03-27  

## Description

_No description._

## Commits

- `e35e04d7` **Darius Wattimena** (2026-03-19): Fixed a bunch of edge cases in revents merging where data would be dropped incorrectly and visits and voyages would be marked as updated wrongly
- `b4958512` **Darius Wattimena** (2026-03-19): Added extra tests cases to ensure the code is covered correctly
- `819ed075` **Darius Wattimena** (2026-03-19): Add test case when wrongly chained visit/voyage structures break to verify the correct visits and voyage are marked as regenerated
- `42742961` **Darius Wattimena** (2026-03-19): Remove unused import
- `7ab68443` **Darius Wattimena** (2026-03-27): Added documentation to clarify logic
- `e3795ef0` **Darius Wattimena** (2026-03-27): Update old kdocs which don't make sense anymore

## Reviews

### augmentcode[bot] — COMMENTED (2026-03-19)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F743%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — COMMENTED (2026-03-24)

_No comment._

### Darius-Wattimena — COMMENTED (2026-03-27)

_No comment._

### TeqJoostD — APPROVED (2026-03-27)

_No comment._

## Review Comments

### TeqJoostD — 2026-03-24 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/merge/EntriesMergeService.kt`


Should this not be startTime < window.to & startTime > window.from

### Darius-Wattimena — 2026-03-27 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/merge/EntriesMergeService.kt`

Isn't needed given entries that are still ongoing, which we retrieve from revents are basically all within the boundary.

This should also be only 1 entry that is ongoing, meaning the last entry in the whole visit/voyage chain.

## Comments

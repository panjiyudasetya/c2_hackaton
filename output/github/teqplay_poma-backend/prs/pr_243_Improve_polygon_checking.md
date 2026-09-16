---
id: github:teqplay/poma-backend:pr:243
source: github
type: pull_request
repo: teqplay/poma-backend
number: 243
title: Improve polygon checking
author: Darius-Wattimena
state: closed
date: '2026-03-20'
merged_at: '2026-03-24'
base_branch: develop
head_branch: corrupted-polygons
url: https://github.com/teqplay/poma-backend/pull/243
labels: []
linked_issues: []
explicit_links: []
---
# PR #243: Improve polygon checking

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/243  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `corrupted-polygons`  
**Created:** 2026-03-20  
**Merged:** 2026-03-24  

## Description

Turns out certain polygons just break the full system. Adjust the checks + added so we also check all other polygons we have in Poma.

## Commits

- `ecf50d32` **Darius Wattimena** (2026-03-20): Added temporary error logging when overlapping check fails
- `5a21147c` **Darius Wattimena** (2026-03-20): ktlint
- `0c848b1f` **Darius Wattimena** (2026-03-20): Reduce logging amount to just be ids
- `3a700b9f` **Darius Wattimena** (2026-03-20): Adjusted checked polygons to check more fields
- `973f655f` **Darius Wattimena** (2026-03-20): Add an additional check to ensure we don't allow duplicate polygon points which are almost identical which crash poma
- `18554332` **Darius Wattimena** (2026-03-20): code cleanup
- `182b95af` **Darius Wattimena** (2026-03-23): Adjust logic to make sure we also don't allow exact duplicate points in a polygon

## Reviews

### augmentcode[bot] — COMMENTED (2026-03-20)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fpoma-backend%2Fpull%2F243%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — COMMENTED (2026-03-20)

_No comment._

### TeqJoostD — DISMISSED (2026-03-20)

_No comment._

### michel-teqplay — CHANGES_REQUESTED (2026-03-23)

_No comment._

### michel-teqplay — APPROVED (2026-03-23)

_No comment._

## Review Comments

### TeqJoostD — 2026-03-20 on `src/main/kotlin/nl/teqplay/poma/generics/InfrastructureController.kt`

Not sure if possible, but might cause errors

### michel-teqplay — 2026-03-23 on `src/main/kotlin/nl/teqplay/poma/generics/InfrastructureController.kt`

Why are exact duplicates not an error? I think they should be, or you should include an explanation why exact duplicates are fine but almost-duplicates are not.

## Comments

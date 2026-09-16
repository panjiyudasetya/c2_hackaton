---
id: github:teqplay/vesselvoyage-backend:pr:729
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 729
title: TCC-676 improve data migration and tune start up
author: Darius-Wattimena
state: closed
date: '2026-03-10'
merged_at: '2026-03-12'
base_branch: develop
head_branch: TCC-676-improve-data-migration
url: https://github.com/teqplay/vesselvoyage-backend/pull/729
labels: []
linked_issues: []
explicit_links: []
---
# PR #729: TCC-676 improve data migration and tune start up

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/729  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-676-improve-data-migration`  
**Created:** 2026-03-10  
**Merged:** 2026-03-12  

## Description

This changes the following:
1. Improve migration task dedupe old data first, given we had quite some data duplication issues in the denormalized model it will result in insert errors without this fix.
2. Adjust ShipStatusService when processing to instead load in last hour only (which takes less than 2 minutes to start).
Currently with 1 day of data it will take around 5 minutes (and Kubernetes kills the pod at 5 minute time when not ready).

## Commits

- `e5c98fe5` **Darius Wattimena** (2026-03-10): Improved migration code to support deduping of corrupted data
- `c8218419` **Darius Wattimena** (2026-03-10): Added some additional test cases to make sure deduping works as expected
- `b34cc9dc` **Darius Wattimena** (2026-03-10): Code cleanup
- `520eacb0` **Darius Wattimena** (2026-03-10): Reduce recents ships to only be the last hour
- `3ad4e98c` **Darius Wattimena** (2026-03-10): Reduce bulk loading size to 1000 ships to keep the mongo queries fast enough
- `de0961f1` **Darius Wattimena** (2026-03-10): Move processing specific code away from the shared ship status service
- `e239f085` **Darius Wattimena** (2026-03-11): Added same deduping logic to revents as well

## Reviews

### augmentcode[bot] — COMMENTED (2026-03-10)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F729%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — APPROVED (2026-03-12)

_No comment._

## Review Comments

## Comments

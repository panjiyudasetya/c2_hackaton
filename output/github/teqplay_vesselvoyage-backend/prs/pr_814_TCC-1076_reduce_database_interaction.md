---
id: github:teqplay/vesselvoyage-backend:pr:814
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 814
title: TCC-1076 reduce database interaction
author: Darius-Wattimena
state: closed
date: '2026-07-10'
merged_at: '2026-07-10'
base_branch: develop
head_branch: TCC-1076-reduce-database-interaction
url: https://github.com/teqplay/vesselvoyage-backend/pull/814
labels: []
linked_issues: []
explicit_links: []
---
# PR #814: TCC-1076 reduce database interaction

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/814  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-1076-reduce-database-interaction`  
**Created:** 2026-07-10  
**Merged:** 2026-07-10  

## Description

_No description._

## Commits

- `7e19179b` **Darius Wattimena** (2026-07-10): Adjusted database writes to only write changes
- `be0e79cc` **Darius Wattimena** (2026-07-10): Adjusted tests to reflect this change
- `335195c4` **Darius Wattimena** (2026-07-10): Optimize the bulk writes to do inserts for new items
- `96023f48` **Darius Wattimena** (2026-07-10): Reduce writing to database when there is no change in status

## Reviews

### augmentcode[bot] — COMMENTED (2026-07-10)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F814%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — APPROVED (2026-07-10)

_No comment._

## Review Comments

## Comments

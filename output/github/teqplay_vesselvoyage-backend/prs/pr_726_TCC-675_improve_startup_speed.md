---
id: github:teqplay/vesselvoyage-backend:pr:726
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 726
title: TCC-675 improve startup speed
author: Darius-Wattimena
state: closed
date: '2026-03-06'
merged_at: null
base_branch: TCC-675-processing-fixes
head_branch: TCC-675-improve-startup-speed
url: https://github.com/teqplay/vesselvoyage-backend/pull/726
labels: []
linked_issues: []
explicit_links: []
---
# PR #726: TCC-675 improve startup speed

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/726  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `TCC-675-processing-fixes` ← `TCC-675-improve-startup-speed`  
**Created:** 2026-03-06  

## Description

_No description._

## Commits

- `4d0c3bd1` **Darius Wattimena** (2026-03-05): Adjusted how we load in ship state so it is faster and does less calls to the database
- `5688d1dc` **Darius Wattimena** (2026-03-05): Merge branch 'TCC-675-processing-fixes' into TCC-675-improve-startup-speed
- `eeeb30e2` **Darius Wattimena** (2026-03-06): Remove unused parameter from the ship status services
- `abd52f0c` **Darius Wattimena** (2026-03-06): Add unit testing for processing ship status service
- `aadc34e7` **Darius Wattimena** (2026-03-06): Rework index creation
- `7ec8ae55` **Darius Wattimena** (2026-03-06): ktlint
- `bdb72f5e` **Darius Wattimena** (2026-03-06): Add index for looking up by ais destination
- `711ae652` **Darius Wattimena** (2026-03-06): Improve loading of visits voyages and esofs by doing them in parallel

## Reviews

### augmentcode[bot] — COMMENTED (2026-03-06)

Review completed. 4 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F726%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

## Review Comments

## Comments

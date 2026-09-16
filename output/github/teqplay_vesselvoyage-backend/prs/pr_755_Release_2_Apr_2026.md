---
id: github:teqplay/vesselvoyage-backend:pr:755
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 755
title: Release 2 Apr 2026
author: Darius-Wattimena
state: closed
date: '2026-04-01'
merged_at: '2026-04-02'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/755
labels: []
linked_issues: []
explicit_links: []
---
# PR #755: Release 2 Apr 2026

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/755  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2026-04-01  
**Merged:** 2026-04-02  

## Description

_No description._

## Commits

- `f43f41f1` **Darius Wattimena** (2026-03-31): Enhance merging back to enlarge the window when no data is found within the scenario window
- `4efee82b` **Darius Wattimena** (2026-03-31): Add an additional test case
- `e866a797` **Darius Wattimena** (2026-03-31): Reduce amount of time needed to lock a ship when merging back with revents
- `5ce23662` **Darius Wattimena** (2026-03-31): Adjust VesselVoyage code to not startup when RabbitMQ connection timed out
- `69d09be6` **Darius Wattimena** (2026-03-31): Reduce logging level of old NATS monitoring
- `092d9c3c` **Darius Wattimena** (2026-03-31): Update DEV database resources
- `aed51c04` **Darius Wattimena** (2026-03-31): Update logic to ensure merging back visit before the first visit of a ship actually works as expected
- `f221115b` **Darius Wattimena** (2026-03-31): code cleanup
- `19871f57` **Darius Wattimena** (2026-04-01): Fix an issue where visits without a bridging voyage would break for port recalculations
- `bc55f7ce` **Darius Wattimena** (2026-04-01): Also make the PROD database bigger
- `a3c98798` **Darius Wattimena** (2026-04-01): Added more tests to ensure consecutive visits or consecutive voyages are correctly resolved
- `256d9908` **Darius Wattimena** (2026-04-01): Merge pull request #753 from teqplay/TCC-807-no-old-entries-within-window
  TCC-807 multiple bug fixes

## Reviews

### augmentcode[bot] — COMMENTED (2026-04-01)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F755%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### michel-teqplay — APPROVED (2026-04-02)

_No comment._

## Review Comments

## Comments

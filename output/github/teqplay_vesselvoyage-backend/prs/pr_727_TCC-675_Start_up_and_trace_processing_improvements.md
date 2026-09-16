---
id: github:teqplay/vesselvoyage-backend:pr:727
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 727
title: TCC-675 Start up and trace processing improvements
author: Darius-Wattimena
state: closed
date: '2026-03-06'
merged_at: '2026-03-09'
base_branch: develop
head_branch: TCC-675-trace-processing-speed-up
url: https://github.com/teqplay/vesselvoyage-backend/pull/727
labels: []
linked_issues: []
explicit_links: []
---
# PR #727: TCC-675 Start up and trace processing improvements

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/727  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-675-trace-processing-speed-up`  
**Created:** 2026-03-06  
**Merged:** 2026-03-09  

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
- `ed148092` **Darius Wattimena** (2026-03-06): Speed up trace processing to not need the current ship status but just the identifiers
- `1e5e6f37` **Darius Wattimena** (2026-03-06): Updated tests to work with new logic
- `a11769a1` **Darius Wattimena** (2026-03-06): Merge branch 'develop' into TCC-675-trace-processing-speed-up
- `94f33219` **Darius Wattimena** (2026-03-06): Apply changes to rabbitmq ais consumer as well
- `330ee5ae` **Darius Wattimena** (2026-03-06): Merge branch 'TCC-675-processing-fixes' into TCC-675-trace-processing-speed-up
- `86bbc00a` **Darius Wattimena** (2026-03-06): Minor improvements to loading of ship identifiers to set the correct updated at timestamps
- `268277f8` **Darius Wattimena** (2026-03-06): Set default date of all identifiers to min epoch to keep start up time fast initially
- `9fd2d133` **Darius Wattimena** (2026-03-06): Adjusted tests so they work
- `9897eb36` **Darius Wattimena** (2026-03-06): Improve brute force loading to be faster
- `f4006b4f` **Darius Wattimena** (2026-03-06): Adjust tests to work with new brute force loading mechanism
- `ed20d454` **Darius Wattimena** (2026-03-06): ktlint
- `431f9dbe` **Darius Wattimena** (2026-03-06): Set a default updatedAt to ensure we can load in older document
- `f9fe3e7f` **Darius Wattimena** (2026-03-06): Adjusted last updated at to be using EPOCH instead of MIN
- `2393bd37` **Darius Wattimena** (2026-03-06): Adjust mongo queries to be chunked to avoid bson query exceptions
- `4d436da5` **Darius Wattimena** (2026-03-09): Adjusted indexes so we can do loading of ship state by only the index
- `6ad3158c` **Darius Wattimena** (2026-03-09): Removed unused indexes from new and old collections
- `a974b17a` **Darius Wattimena** (2026-03-09): Move index creation to the background thread for the old collections and added a new index needed for faster ship state loading
- `ca591644` **Darius Wattimena** (2026-03-09): Adjusted loading of ships to be in smaller batches and log progress
- `e1b8d174` **Darius Wattimena** (2026-03-09): ktlint cleanup
- `367bdc38` **Darius Wattimena** (2026-03-09): Added additional logging so we can see how long each collection takes to load in a batch
- `7f9dc6c3` **Darius Wattimena** (2026-03-09): Merge branch 'develop' into TCC-675-trace-processing-speed-up

## Reviews

### augmentcode[bot] — COMMENTED (2026-03-06)

Review completed. 3 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F727%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — APPROVED (2026-03-09)

_No comment._

## Review Comments

## Comments

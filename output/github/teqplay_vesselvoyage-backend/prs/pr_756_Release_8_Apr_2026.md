---
id: github:teqplay/vesselvoyage-backend:pr:756
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 756
title: Release 8 Apr 2026
author: Darius-Wattimena
state: closed
date: '2026-04-07'
merged_at: '2026-04-09'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/756
labels: []
linked_issues: []
explicit_links: []
---
# PR #756: Release 8 Apr 2026

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/756  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2026-04-07  
**Merged:** 2026-04-09  

## Description

_No description._

## Commits

- `4577d122` **Darius Wattimena** (2026-03-27): Remove old V2 collections which have been replaced with the normalized collections
- `e8a4adbe` **Darius Wattimena** (2026-03-27): Add unit tests for cleaned up data sources
- `6a118229` **Darius Wattimena** (2026-03-27): ktlint
- `eea04cf0` **Darius Wattimena** (2026-03-27): Remove unused NewEntryDataSource abstract class as well
- `5ce026fc` **Darius Wattimena** (2026-03-27): ktlint
- `27a02274` **Darius Wattimena** (2026-03-27): Remove ship id lazy loading related code
- `ab5acc77` **Darius Wattimena** (2026-04-07): Merge branch 'develop' into TCC-677-remove-old-collections
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/merge/EntriesMergeV2Service.kt
  #	src/test/kotlin/nl/teqplay/vesselvoyage/service/merge/EntriesMergeV2ServiceTest.kt
  #	src/test/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationServiceTest.kt
- `3e6de6fa` **Darius Wattimena** (2026-04-07): Merge branch 'TCC-677-remove-old-collections' into TCC-677-ship-id-lazy-loading-remove
- `fe0d7893` **Darius Wattimena** (2026-04-07): Merge pull request #749 from teqplay/TCC-677-remove-old-collections
  TCC-677 remove non-normalised collections
- `0987ef8e` **Darius Wattimena** (2026-04-07): Merge pull request #750 from teqplay/TCC-677-ship-id-lazy-loading-remove
  TCC-677 Remove ship id migration code

## Reviews

### augmentcode[bot] — COMMENTED (2026-04-07)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F756%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### michel-teqplay — APPROVED (2026-04-08)

_No comment._

## Review Comments

## Comments

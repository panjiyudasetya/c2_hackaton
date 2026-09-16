---
id: github:teqplay/vesselvoyage-backend:pr:812
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 812
title: Add partial indexes for ongoing visits/voyages by port area
author: michel-teqplay
state: closed
date: '2026-07-07'
merged_at: '2026-07-08'
base_branch: develop
head_branch: TCC-1076-fix-index
url: https://github.com/teqplay/vesselvoyage-backend/pull/812
labels: []
linked_issues: []
explicit_links: []
---
# PR #812: Add partial indexes for ongoing visits/voyages by port area

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/812  
**State:** closed | **Author:** michel-teqplay  
**Base ← Head:** `develop` ← `TCC-1076-fix-index`  
**Created:** 2026-07-07  
**Merged:** 2026-07-08  

## Description

## Summary
- `findByPortAreaId`/`findByPortAreaIds` with `finished=ONGOING` had to scan every visit/voyage ever recorded for a port area, since the existing compound indexes can't bound on the top-level `end == null` predicate.
- Adds partial indexes (scoped to `end == null`) on `eospAreaActivity.areaId + start.time` for visits, and on `originPort + start.time` / `destinationPort + start.time` for voyages, built in the background so collection creation isn't locked.

## Test plan
- [x] Unit tests updated (index-creation latch counts bumped) and passing
- [x] Verified locally via `explain()` that the query planner now picks the new partial index (`isPartial: true`) over the old full index, with `direction: backward` matching the descending sort so no extra in-memory sort is needed

## Commits

- `e4d551e3` **Michel Wilson** (2026-07-06): Add partial indexes for ongoing visits/voyages by port area
  findByPortAreaId/findByPortAreaIds with finished=ONGOING was fetching
  every visit/voyage ever recorded for a port to filter out the finished
  ones in memory, since the existing compound indexes can't bound on the
  top-level "end == null" predicate via an "end.time" index key. Explain
  on a busy port showed 261k docs examined to return 504 ongoing visits.
  
  Add partial indexes scoped to end == null so these lookups scan only
  the currently-ongoing entries. Built in the background to avoid
  locking the collection during creation.
  
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `0ae9030b` **Michel Wilson** (2026-07-07): Address review feedback

## Reviews

### augmentcode[bot] — COMMENTED (2026-07-07)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F812%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### Darius-Wattimena — CHANGES_REQUESTED (2026-07-07)

_No comment._

### Darius-Wattimena — APPROVED (2026-07-07)

_No comment._

## Review Comments

### Darius-Wattimena — 2026-07-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/VisitV2DataSource.kt`

Settings background to true doesn't do anything I think? Not sure

### Darius-Wattimena — 2026-07-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/VoyageV2DataSource.kt`

Same to all the places you set this to true here as well

## Comments

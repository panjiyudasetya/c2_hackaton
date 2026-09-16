---
id: github:teqplay/vesselvoyage-backend:pr:772
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 772
title: TCC-929 fix missing published
author: Darius-Wattimena
state: closed
date: '2026-05-07'
merged_at: '2026-05-11'
base_branch: develop
head_branch: TCC-929-fix-missing-published
url: https://github.com/teqplay/vesselvoyage-backend/pull/772
labels: []
linked_issues: []
explicit_links: []
---
# PR #772: TCC-929 fix missing published

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/772  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-929-fix-missing-published`  
**Created:** 2026-05-07  
**Merged:** 2026-05-11  

## Description

_No description._

## Commits

- `016e01b5` **Darius Wattimena** (2026-05-06): Added persistAndPublish helper on PersistChangesService
  Centralizes the persist-then-publish flow so callers can persist V2 changes and broadcast them via ChangesPublisherService in a single call.
- `15d21680` **Darius Wattimena** (2026-05-06): Publish ESoF changes from PostProcessingService
  Resolves the ship's status before persistence and routes the post-processing ESoF change through persistAndPublish so the update is broadcast to RabbitMQ.
- `fb9a228b` **Darius Wattimena** (2026-05-06): Route ReventsRecalculationService merge persistence through PersistChangesService
  Converts merge results into VisitChange/VoyageChange/ESoFChange (UPDATE for upserts, DELETE for removals) and persists them via persistAndPublish so the merge outcome is broadcast.
- `7a6c799a` **Darius Wattimena** (2026-05-06): Publish broken-stop fixes from ProcessingStopService
  Replaces fixBrokenStopsInBatches with forEachBrokenStopsBatch on the V2 data sources so the service handles persistence, allowing ProcessingStopService to emit the fixed entries as Action.UPDATE changes via persistAndPublish.
- `b3cc13ca` **Darius Wattimena** (2026-05-06): ktlint
- `d5fee8a6` **Darius Wattimena** (2026-05-07): Attempt to fix an issue where certain post processing would result in exceptions being thrown
- `b13d8626` **Darius Wattimena** (2026-05-07): Fix flacky unit test setups when running in CI

## Reviews

### michel-teqplay — DISMISSED (2026-05-07)

_No comment._

### augmentcode[bot] — COMMENTED (2026-05-07)

Review completed. 3 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F772%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### michel-teqplay — DISMISSED (2026-05-07)

_No comment._

### michel-teqplay — APPROVED (2026-05-11)

_No comment._

## Review Comments

## Comments

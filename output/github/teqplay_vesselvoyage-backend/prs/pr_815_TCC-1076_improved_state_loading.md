---
id: github:teqplay/vesselvoyage-backend:pr:815
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 815
title: TCC-1076 improved state loading
author: Darius-Wattimena
state: closed
date: '2026-07-10'
merged_at: '2026-07-13'
base_branch: develop
head_branch: TCC-1076-improved-state-loading
url: https://github.com/teqplay/vesselvoyage-backend/pull/815
labels: []
linked_issues: []
explicit_links: []
---
# PR #815: TCC-1076 improved state loading

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/815  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-1076-improved-state-loading`  
**Created:** 2026-07-10  
**Merged:** 2026-07-13  

## Description

_No description._

## Commits

- `e2af9059` **Darius Wattimena** (2026-07-10): Experiment with loading ship state in a smarter way on startup to speed up consumption
- `23c36503` **Darius Wattimena** (2026-07-10): Update unit test to reflect new way of loading
- `06555dd4` **Darius Wattimena** (2026-07-13): Load ESoFs fresh by entry ID when hydrating status snapshots
  An ESoF can be created or updated without the snapshot being rewritten
  (e.g. by recalculations), so hydrating the snapshot copies could
  resurrect stale ESoFs on startup.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>

## Reviews

### augmentcode[bot] — COMMENTED (2026-07-10)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F815%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### michel-teqplay — DISMISSED (2026-07-13)

Mostly ok with this, but if you have the time i would really like it if you would refactor the duplication into something a bit nicer.
Also, much hydration! Very good with the hot weather.

### Darius-Wattimena — COMMENTED (2026-07-13)

_No comment._

### Darius-Wattimena — COMMENTED (2026-07-13)

_No comment._

### michel-teqplay — APPROVED (2026-07-13)

_No comment._

## Review Comments

### michel-teqplay — 2026-07-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/ProcessingShipStatusService.kt`

Somewhat meh, also, you're reusing the same pattern/structure 3 times :( If you extract this into a little helper fun you could probably also engineer it in a way that it returnst the map directly, avoiding the ugly `result` on a line? For the logging you can use `.also { }` btw, to avoid this.

### Darius-Wattimena — 2026-07-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/ShipStatusService.kt`

Fixed: snapshot hydration now reads the ESoFs fresh from their collection by the snapshot's entry IDs (`EsofV2DataSource.findByIds`) instead of hydrating the copies embedded in the snapshot, in both the single-ship and bulk startup paths. This covers ESoFs created or updated after the snapshot was written (e.g. by recalculations, which persist changes without refreshing the ship status). Costs one extra batched query on the small normalized ESoF parent documents per load batch; the entry-level staleness case is already guarded by the identifiers match.

### Darius-Wattimena — 2026-07-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/model/internal/ShipStatusSnapshot.kt`

Fixed the wording — and since hydration no longer reads the embedded ESoFs (see the other thread), the doc now also notes they are kept as the state at snapshot-write time while loading reads them fresh by entry ID.

## Comments

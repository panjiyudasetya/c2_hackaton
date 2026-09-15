---
id: github:teqplay/vesselvoyage-backend:pr:829
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 829
title: Make NewEntry.shipId non-nullable and drop migration-era fallbacks
author: Darius-Wattimena
state: closed
date: '2026-07-28'
merged_at: '2026-07-29'
base_branch: develop
head_branch: claude/pensive-swartz-4ec2d4
url: https://github.com/teqplay/vesselvoyage-backend/pull/829
labels: []
linked_issues: []
explicit_links: []
---
# PR #829: Make NewEntry.shipId non-nullable and drop migration-era fallbacks

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/829  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `claude/pensive-swartz-4ec2d4`  
**Created:** 2026-07-28  
**Merged:** 2026-07-29  

## Description

## What

All Visit/Voyage entries in the database now carry a CSI `shipId`, so the temporary nullability and its fallback machinery can go.

- **`shipId: String?` → `String`** on `NewEntry` / `NewVisit` / `NewVoyage` and the normalized DB models (`NormalizedVisit` / `NormalizedVoyage`), removing the "temporary null until all entries are migrated" TODO.
- **Removed all shipId null-handling**:
  - `EntryV2Mapper`: dropped the `resolveShipId` MapStruct qualifier and the `?: getShipIdByImo(...)`-or-throw resolution — `shipId` maps directly now.
  - `PostProcessingService`: dropped the IMO fallback and the "Ship ID is null" persist-without-broadcasting branch (and its now-unused `StaticShipInfoService` dependency).
  - `ChangesPublisherService`: dropped the catch that skipped outgoing changes when the mapper couldn't resolve a shipId.
  - `ShipStatusService`: removed both `shipId!!` in the identifier helpers.
  - `EntryProcessingService`: removed the shipId backfill shim whose TODO said it could go once the migration stabilised.
  - Tests: removed `?: TEST_SHIP_ID`-style fallbacks and `!!` usages.
- **`TraceService.generateTraceWithShipHistory`**: the IMO fetch branch was dead (shipId is always non-null now), so traces are always fetched by CSI id and the `imo` parameter is gone.

## Deprecated `NewEntry.imo` — investigated, kept

Dropping `imo` from the internal models is **not feasible without a data migration**:

1. `VisitV2DataSource` / `VoyageV2DataSource` implement the SEA_VESSEL/BARGE filter as `imo eq/ne MISSING_IMO` against the stored documents.
2. `imo == MISSING_IMO` is the barge discriminator in the mapper (`ImoVisit` vs `BargeVisit`), story MMSI resolution and SoF views.
3. The apiv2 wire models expose `imo`, and the processing endpoints serialize `NewEntry` directly.

The path to removing it later: add a stored vessel-type discriminator to the normalized collections + backfill, switch the filters/barge checks over, then resolve `imo` only at the API boundary.

## Testing

- `./gradlew test ktlintCheck` — 2216 tests, 0 failures, ktlint clean across root, `api` and `client`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Commits

- `468ad116` **Darius Wattimena** (2026-07-28): Make NewEntry.shipId non-nullable now all entries are migrated
  All Visit/Voyage documents carry a shipId since the migration completed,
  so the temporary nullability on NewEntry/NewVisit/NewVoyage and the
  normalized database models can go. Test helpers no longer need their
  null fallbacks either.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `97c5a2b1` **Darius Wattimena** (2026-07-28): Drop shipId resolution fallbacks now the field is always present
  Remove the IMO-based shipId resolution in EntryV2Mapper (including the
  resolveShipId MapStruct qualifier), the null-shipId branch in
  post-processing, the skip-on-unresolvable-shipId catch in the changes
  publisher, and the shipId backfill shim in EntryProcessingService that
  was marked for removal once the migration stabilised.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `0ef3f889` **Darius Wattimena** (2026-07-28): Always fetch entry traces by shipId instead of falling back to IMO
  generateTraceWithShipHistory only ever received a non-null shipId now,
  so the IMO fetch branch and parameter are dead. Also simplify the barge
  MMSI lookup in StoryService which no longer needs a null-shipId branch.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>

## Reviews

### augmentcode[bot] — COMMENTED (2026-07-28)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F829%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — APPROVED (2026-07-29)

_No comment._

## Review Comments

## Comments

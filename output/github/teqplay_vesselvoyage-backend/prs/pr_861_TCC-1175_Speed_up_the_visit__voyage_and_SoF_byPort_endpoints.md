---
id: github:teqplay/vesselvoyage-backend:pr:861
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 861
title: TCC-1175 Speed up the visit, voyage and SoF byPort endpoints
author: Darius-Wattimena
state: closed
date: '2026-08-20'
merged_at: '2026-08-21'
base_branch: develop
head_branch: TCC-1175-byport-query-performance
url: https://github.com/teqplay/vesselvoyage-backend/pull/861
labels: []
linked_issues: []
explicit_links: []
---
# PR #861: TCC-1175 Speed up the visit, voyage and SoF byPort endpoints

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/861  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-1175-byport-query-performance`  
**Created:** 2026-08-20  
**Merged:** 2026-08-21  

## Description

The `byPort` endpoints for visits, voyages and Statements of Facts were slow. The Mongo queries themselves were not the problem — the per-ship and per-visit fetches layered on top of the result set were.

## What changed

**Batching the N+1s**

- `BaseApiV2FilteringController.filterMultipleOngoing` called `esofV2Service.findAllById` *inside* the per-ship loop, and each call is ~4 Mongo round-trips. A port query spanning S ships cost ~4×S round-trips, on the default code path (`filterMultipleOngoing=true`). The filtering is now pure in-memory logic across all ship groups, followed by one bulk ESoF fetch.
- `ApiStatementOfFactsV2Controller.filterIfMultipleOngoing` ran the full `convertToApiModels` machinery — paying that per-ship cost — only to throw the ESoFs away and have `produceBulk` fetch them all again. It now uses a fetch-free filter.
- `EsofV2Service.produceBulk` collected `previousVoyageIds` but never used them, so `view=PTO` did one voyage `findById` per visit. It resolves them in one call now.
- That previous-voyage lookup needs exactly one field, `originPort`, but went through `findByIds`, which hydrates every voyage's normalized stops and area activities and then discards them. Added a projected `findOriginPortsByIds` and used it on both the bulk and single-visit paths.

**Voyage byPort limit returns the newest entries**

`VoyageV2DataSource.findByPortAreaIds`/`findByAisDestination` applied `limitIfNotNull` with no sort, so "limit N" returned an arbitrary N in natural order. They sort by `start.time` descending first, so a limit returns the newest N.

**Per-entry hydration work**

`joinNormalizedDataBulk` runs for every entry in the result set, so small waste multiplies by thousands: `collectAllActivityIds` was called twice per entry and each call copied all eleven activity id lists; it built its result by chaining ten list concatenations; and `sortedByStartTime` allocated a sorted copy of every activity list, most holding zero or one element.

**Visit byPort no longer advertises a limit it ignores**

The endpoint declared a `limit` query parameter and documented it in Swagger, but never copied it into `VisitByPortRequest` — the value was silently dropped. The parameter is gone.

An earlier revision of this branch wired that limit up for real and added one to `sof/byPort`. Both were reverted, because a limit combines badly with the multiple ongoing filter: the database applies the limit, the filter then drops stale ongoing entries from the page, and a caller asking for 10 entries gets 7. Making the limit exact needs paging to top the page back up — a lot of machinery for a parameter that never worked on these endpoints, so nothing can depend on it. The filtering is unchanged and stays the default. Bounding these result sets is worth revisiting on its own terms, together with a server-side default limit.

## Measured on a local dev Mongo

`develop` and this branch against the same database, `unlocode=NLRTM` over 2024-01-01 → now (2513 visits), median of 7 runs:

| endpoint | develop | this branch | |
|---|---|---|---|
| `sof/byPort?view=pto` | 1.555s | 1.037s | 1.50x |
| `sof/byPort?view=portreporter` | 1.312s | 1.039s | 1.26x |
| `visit/byPort` | 1.089s | 0.933s | 1.17x |

The `pto` − `portreporter` gap is what isolates the previous-voyage lookups: **+244ms on develop, −3ms here**. Resolving 519 previous ports now costs nothing measurable.

Gains scale with the number of ships in the result, so a busy port over a wide window benefits most; a single-ship window is unchanged.

## Compatibility

No change to any response shape. The published client artifact is untouched apart from a function body in `NormalizedVisit`, and the removed `limit` query parameter, which never had an effect.

## Verification

`./gradlew test ktlintCheck` passes. Unit tests cover the single bulk ESoF fetch with unchanged filtering semantics, the projected previous-port lookup (including that full voyages are never hydrated, and that a caller-supplied voyage still short-circuits the query), the ESoFs being fetched once end to end on the SoF path, and the voyage sort-before-limit.

Diffed full responses between two instances on the same database: `visit/byPort` is identical — same 2513 entries, same order, same content. For `sof/byPort?view=pto`, all 24MB match once `generationId` (which changes per generation) and the order of `cargoCategoryType` are normalised. That field is a `Set<CargoCategoryType>` on the Poma `Berth` model serialized as a JSON array: its order is stable within a process but arbitrary between processes, and this branch touches no file in that path.

Also measured, for context on what the filter actually does: over the same 2.5-year window, `filterMultipleOngoing=true` and `=false` returned identical counts at NLRTM, BEANR, SGSIN, DEHAM, GBLON and NLAMS — the filter dropped nothing anywhere.

## Deliberately not included

- Index fixes: the visit AIS-destination index keys on the whole `end` subdocument while the query filters `start.time`/`end.time` ranges, so only the `destination.actual` prefix is usable — the voyage-side equivalent gets this right. Also the `end`-only period branch leaves `start.time` unbounded, and index creation runs on a fire-and-forget `thread {}` that swallows failures.
- Caching the `categories` → shipId computation in `selectShipIdsOrEmpty`, which walks the ship register per request: adding `categories=TANKER` to a query returning 6 visits doubled its latency (0.125s → 0.260s).
- Parallelising the batch `POST` variants, which loop their requests sequentially.
- The real remaining lever is payload size — 6.3MB for the visits and 24MB for the PTO SoFs above. Cutting that means an opt-in projection or keyset pagination, both additive but needing consumer adoption.

🤖 Generated with [Claude Code](https://claude.com/claude-code)


## Commits

- `e45ed639` **Darius Wattimena** (2026-08-20): TCC-1175 Fetch ESoFs in one bulk call when filtering ongoing entries
  filterMultipleOngoing grouped the entries by ship and called
  esofV2Service.findAllById inside the per-ship loop, so a by-port query
  spanning S ships paid ~4xS Mongo round-trips. Hoist the ESoF fetch out of
  the loop: filter all ship groups first, then resolve the ESoFs of the
  surviving entries in a single bulk call.
  
  Also adds a filterMultipleOngoing overload that filters without resolving
  any ESoF, for callers that only need the filtered entries.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `92480676` **Darius Wattimena** (2026-08-20): TCC-1175 Stop fetching every ESoF twice on the SoF endpoints
  filterIfMultipleOngoing ran the full convertToApiModels machinery just to
  drop stale ongoing visits, fetched all ESoFs, threw them away and then let
  produceBulk fetch them all again. Use the fetch-free filter instead, so the
  ESoFs are only fetched once, by produceBulk.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `114e992e` **Darius Wattimena** (2026-08-20): TCC-1175 Bulk fetch the previous voyages in produceBulk
  produceBulk already collected the previousVoyageIds of all visits but never
  used them, so every visit did its own voyageV2Service.findById to resolve
  the previous port of the PTO view. Fetch them in a single call and hand them
  to produce as knownPreviousVoyage. Views that don't use the previous voyage
  fetch nothing at all.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `40aa4ebe` **Darius Wattimena** (2026-08-20): TCC-1175 Sort the voyage byPort queries before limiting them
  findByPortAreaIds and findByAisDestination applied the limit without a sort,
  so "limit N" returned an arbitrary N in natural order instead of the newest
  N. Sort descending on the start time first, which the origin/destination and
  AIS destination indexes already cover.
  
  Note that this also makes an unfiltered byPort response newest-first, where
  it used to follow the database's natural order.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `992e90c8` **Darius Wattimena** (2026-08-20): TCC-1175 Read only the origin port of the previous voyage
  Resolving the previous port of a PTO Statement of Facts needs exactly one
  field of the previous voyage: its origin port. Both produceBulk and the
  single visit path went through findByIds/findById, which hydrates the
  normalized stops and area activities of every one of those voyages and then
  discards them.
  
  Add a projected findOriginPortsByIds on the voyage data source and use that
  instead, so a by-port SoF request no longer hydrates a full voyage per
  visit.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `1df18b0d` **Darius Wattimena** (2026-08-20): TCC-1175 Trim the per-entry work in the bulk hydration
  Hydrating a by-port result set does the same work for every entry, so the
  waste adds up over the thousands of entries these endpoints return:
  
  - collectAllActivityIds was called twice per entry, and each call copies all
    eleven activity id lists. Collect them once and reuse them.
  - collectAllActivityIds built its result by chaining ten list concatenations,
    each allocating and copying a new list. Build one list instead.
  - sortedByStartTime allocated a sorted copy of every activity list, most of
    which hold zero or one element. Return those as they are.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `b7fb1fe5` **Darius Wattimena** (2026-08-21): TCC-1175 Drop the unused limit parameter from visit byPort
  The endpoint declared a limit query parameter and documented it in Swagger,
  but never copied it into VisitByPortRequest, so the value was silently
  ignored. Advertising a parameter the endpoint does not act on is worse than
  not offering one, and bounding the result set here does not combine well with
  the multiple ongoing filter: the database would apply the limit and the
  filter would then drop entries from the page, returning fewer entries than
  the caller asked for.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>

## Reviews

### augmentcode[bot] — COMMENTED (2026-08-20)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F861%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — APPROVED (2026-08-21)

_No comment._

## Review Comments

## Comments

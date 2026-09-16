---
id: github:teqplay/vesselvoyage-backend:pr:806
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 806
title: 'TCC-1015: generate revents Visit/Voyage entries by replaying events'
author: TeqJoostD
state: closed
date: '2026-07-01'
merged_at: '2026-07-14'
base_branch: develop
head_branch: TCC-1015
url: https://github.com/teqplay/vesselvoyage-backend/pull/806
labels: []
linked_issues: []
explicit_links: []
---
# PR #806: TCC-1015: generate revents Visit/Voyage entries by replaying events

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/806  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-1015`  
**Created:** 2026-07-01  
**Merged:** 2026-07-14  

## Description

## What

Generates revents Visit/Voyage entries in this backend by **replaying** the persisted `ActualEvent`s from ais-engine, instead of pulling entries that a VesselVoyage sidecar generated inside the revents pod.

Pairs with **ais-engine [#1532](https://github.com/teqplay/ais-engine/pull/1532)** (the sidecar removal). That PR must be released first.

## Changes

- **New** `ReventsReplayMergeService`: for each non-partial interest it
  - fetches events via `ReventsClient.fetchEventsByShipId` (`POST /events`),
  - replays them through `EntryProcessingService.processAisEngineEventsDryRunForStoryV2`,
  - sets `deleteExisting = replayedEntries.isEmpty()` (same condition the old ais-engine post-processing used),
  - applies `pruneEntries` **ported verbatim** from ais-engine `VesselVoyageMergingV2Service`,
  - emits the same `MergeEntryV2` shape the sidecar used to serve.
- `ReventsRecalculationService`: **only** the `mergeEntries` source changed — the merge `forEach` (filter → `entriesMergeV2Service.merge` → locking → persist → retries) is untouched, so merge behavior is preserved.
- Scenario completion is still detected by the existing **polling** (`checkScenarioProgress`); no push endpoint added.

## Verification

Built and tested against a locally-published ais-engine snapshot (`publishToMavenLocal`): `compileKotlin` green; `ReventsRecalculationServiceTest` (54) + new `ReventsReplayMergeServiceTest` (3) pass.

## ⚠️ Before merge

`aisengine_version` in `build.gradle` must be **bumped to the ais-engine TCC-1015 release** (see the `TODO(TCC-1015)` there). It currently references the pre-change version, so CI will not build until ais-engine #1532 is released.

## Judgment calls to review

- `calculateDrifting = false` on replay — drift/slow-moving + traces are computed by the existing post-merge step (`persistMergeResultV2`); encounters/STS in ESoF still come from the events.
- `pruneEntries` `areaIds = setOfNotNull(requestedPortAreaId)` reproduces ais-engine `scenario.toPortInterestAreaIds()` for single-port recalcs (null for ship scenarios → area filter skipped, as before).
- `getInterests(scenario)` is fetched per ship (filtered client-side) — same call count as before; could batch to one fetch as a follow-up.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Commits

- `7121c523` **TeqJoostD** (2026-07-01): TCC-1015: generate revents Visit/Voyage entries by replaying events
  Instead of pulling sidecar-generated entries from ais-engine, replay the
  persisted ActualEvents through EntryProcessingService to generate the
  entries locally, then merge as before.
  
  - Add ReventsReplayMergeService: fetch events via ReventsClient.fetchEventsByShipId,
    replay via EntryProcessingService.processAisEngineEventsDryRunForStoryV2,
    compute deleteExisting from the replay result, and apply the pruneEntries
    windowing (ported verbatim from ais-engine VesselVoyageMergingV2Service).
  - ReventsRecalculationService: swap only the mergeEntries source; the merge
    loop, per-ship locking, persistence and retries are unchanged.
  - Polling is retained; windowing/deleteExisting semantics match the former
    ais-engine merge path.
  
  Requires the ais-engine TCC-1015 release: aisengine_version must be bumped
  (TODO left in build.gradle).
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
- `d6870973` **TeqJoostD** (2026-07-07): TCC-1015: address review feedback + pin ais-engine snapshot
  Review (Augment):
  - Sort events by actualTime before replay (defensive; POST /events already
    sorts by actualTime, but replay is order-sensitive).
  - Make the port filter main-port-aware via InfraService so visits in sub-ports
    of the requested main port aren't pruned (mirrors isVisitInRequestedPort).
  - Document the deleteExisting semantics: a non-partial window that generates no
    entries deletes stale production data; entries pruned to empty (boundary-only,
    outside windowNoMargin) intentionally keep deleteExisting=false — parity with
    the former ais-engine merge path.
  
  Also pin aisengine_version to the published TCC-1015 snapshot (20260630-SNAPSHOT)
  and drop the local build workaround, so CI resolves the new API.
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
- `2f2f2da4` **TeqJoostD** (2026-07-07): TCC-1015: pin ais-engine to unique branch build revents-tcc-1015-b1
  The 20260630-SNAPSHOT publish resolved a stale build on CI. Republished the
  libraries with a clean, no-cache rebuild under a unique fixed version and pin
  to it, removing SNAPSHOT-metadata ambiguity. Verified the resolved
  client-revents-engine-api contains fetchEventsByShipId.
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
- `544252bb` **TeqJoostD** (2026-07-07): TCC-1015: own MergeEntryV2 locally; pin ais-engine revents-tcc-1015-b2
  MergeEntryV2 moves here (this backend is its only consumer) so ais-engine can
  drop its dependency on the vesselvoyage V2 entry model. It lives in the
  recalculation package, so the same-package consumers need no import.
  
  Pin aisengine_version to revents-tcc-1015-b2, the decoupled ais-engine build
  (models/revents-engine-common POMs no longer declare vesselvoyage:api).
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
- `bc4d861b` **TeqJoostD** (2026-07-07): Merge remote-tracking branch 'origin/develop' into TCC-1015
  # Conflicts:
  #	build.gradle
- `e7ecdeb8` **TeqJoostD** (2026-07-13): Merge remote-tracking branch 'origin/develop' into TCC-1015
- `80f06da1` **TeqJoostD** (2026-07-14): TCC-1015: bump ais-engine to 20260714-b1464.1
  The revents changes are now in a develop ais-engine release, so replace the
  temporary revents-tcc-1015-b2 branch snapshot with the proper build.
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>

## Reviews

### augmentcode[bot] — COMMENTED (2026-07-01)

Review completed. 3 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F806%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — COMMENTED (2026-07-07)

_No comment._

### TeqJoostD — COMMENTED (2026-07-07)

_No comment._

### TeqJoostD — COMMENTED (2026-07-07)

_No comment._

### Darius-Wattimena — CHANGES_REQUESTED (2026-07-09)

_No comment._

### Darius-Wattimena — APPROVED (2026-07-14)

_No comment._

## Review Comments

### TeqJoostD — 2026-07-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsReplayMergeService.kt`

Addressed in d6870973: the replay now sorts by `actualTime` before processing. `POST /events` already sorts ascending by `actualTime` server-side (ActualEventsBaseDataSource.fetch), so this is defensive but makes the order-sensitivity explicit.

### TeqJoostD — 2026-07-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsReplayMergeService.kt`

Addressed in d6870973: the port filter is now main-port-aware via `InfraService.getPortByAreaId(...)`/`mainPort` (same logic as `isVisitInRequestedPort`), so visits in sub-ports of the requested main port are kept.

### TeqJoostD — 2026-07-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsReplayMergeService.kt`

This is intentional and preserves the former merge behavior (documented in d6870973). `deleteExisting` is decided on the full with-margin window BEFORE pruning: no entries generated at all → delete stale data. If entries were generated but pruned to empty (they fell only in the margin, outside `windowNoMargin`), they are boundary-only and untrusted, so we conservatively leave existing production data untouched rather than deleting on uncertain data — matching the old ais-engine merge path. Changing this would be a behavior change beyond the refactor's scope.

### Darius-Wattimena — 2026-07-08 on `build.gradle`

Could we use a release version?

## Comments

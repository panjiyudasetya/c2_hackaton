---
id: github:teqplay/vesselvoyage-backend:pr:830
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 830
title: TCC-1137 Proactively repair fallback-ended activities using event history
author: Darius-Wattimena
state: closed
date: '2026-07-28'
merged_at: null
base_branch: develop
head_branch: TCC-1137-fix-fallback-activities
url: https://github.com/teqplay/vesselvoyage-backend/pull/830
labels: []
linked_issues: []
explicit_links: []
---
# PR #830: TCC-1137 Proactively repair fallback-ended activities using event history

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/830  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-1137-fix-fallback-activities`  
**Created:** 2026-07-28  

## Description

## What

When we miss an end event, activities/stops/encounters/STS transfers get closed with a fallback end (`end.fallback`, e.g. `ACTIVITY_END_BY_EOSP`). 9/10 times the real end event does exist in the AisEngine EventHistory and was only dropped in transit. This PR adds a repair mechanism that looks up the dropped end event and replaces the fallback end with the actual end location/time — both proactively for future entries and as a one-time fix for the existing broken data.

## How

**`FallbackEndRepairService`** — for a finished entry, collects every item with `end.fallback != null`, fetches the ship's events from EventHistory over the entry window (+24h margin), and matches each broken item to its end event via `EndEvent.startEventId` (works uniformly: area activities store their start event id as `id`, stops/encounters/STS store `startEventId`). Matches replace the fallback `LocationTime` and clear the marker; stops also get `endEventId` filled in.

Guards:
- Entries with nothing broken skip the EventHistory call entirely
- Ongoing entries are never touched (real-time correction paths still apply)
- **Regenerated entries are skipped** — they were rebuilt from replayed scenario events, so real-time EventHistory ids can never match
- Events without a location or producing a zero/negative duration are rejected
- `eospAreaActivity` is excluded: its end is the visit boundary itself (that stays `repairStory` territory)
- Event lookup goes by **shipId** (IMO/MMSI mapping applied) so MMSI-only ships like barges are covered

**Post-processing integration** — the repair runs as the first step of every normal post-processing run, so future entries self-heal automatically. Repaired entries are persisted as `VisitChange`/`VoyageChange` next to the usual ESoF change and republished (`FINAL`); the in-memory ship status is updated too. This lifts the old "post-processing only mutates the ESoF" constraint. A repair failure (EventHistory down) never blocks the other post-processing steps.

**Repair-only mode** — `PostProcessable.onlyFallbackEndRepair` runs just the repair: no trace rebuild, no slow-moving recalculation, `postProcessed` flag untouched. This is what the historic backfill uses. The flag only applies to entries that were already post-processed: an entry whose ESoF isn't `postProcessed` yet gets the full post-processing instead (which includes the repair). This matters because the queue holds one item per entry — a repair-only item can replace a regular item the real-time flow just queued, and the downgrade guarantees that full run still happens.

**Attempt tracking** — entries where a repair couldn't fix everything (event genuinely missing from EventHistory, or regenerated) are recorded in a new `fallbackEndRepairAttempt` collection, so re-running the bulk scheduling doesn't retry known-unrepairable entries. Retry them explicitly with `?retryPreviouslyAttempted=true`.

## Endpoints (`/v2/post-processing`)

- `POST /schedule/fallbackEndRepair` — schedule repair-only runs for all broken finished entries. Returns immediately; the detection and queueing run on a background thread (the queries take longer than the load balancer timeout, so there is deliberately no synchronous status/count endpoint — totals and progress are in the logs)
- `POST /schedule/fallbackEndRepair/{entryId}` — schedule a single entry (ignores the attempt marker, always runs)

## Notes

- The fallback-end detection queries on the normalized collections are unindexed scans — fine for occasional admin use, documented on the methods
- Scheduling a repair-only item replaces an already-queued regular post-processing item for the same entry (same `_id` upsert) — safe because of the repair-only downgrade described above

## Testing

- New `FallbackEndRepairServiceTest` (16 cases: each repairable type, all guards, attempt tracking, scheduling filters)
- `PostProcessingServiceTest` extended for repair-only and combined-mode behaviour
- `./gradlew test ktlintCheck` green

🤖 Generated with [Claude Code](https://claude.com/claude-code)




## Commits

- `29b8c793` **Darius Wattimena** (2026-07-28): Add support to fix broken visits or voyages which have fallback data to be proactively repaired
- `a93c84cb` **Darius Wattimena** (2026-07-28): Made the fallback scheduling save which entries we already tried fixing
- `7ae63e20` **Darius Wattimena** (2026-07-28): Adjust scheduling so we don't schedule still ongoing entries
- `0b47a598` **Darius Wattimena** (2026-07-28): Run full post-processing instead of repair-only when the entry was never post-processed
  A repair-only queue item replaces an already-queued regular post-processing
  item for the same entry. By downgrading to the full run (which includes the
  repair) when the ESoF isn't post-processed yet, that replacement can never
  lose the full post-processing.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `116d8adb` **Darius Wattimena** (2026-07-28): Attach the orphaned scheduling KDoc to its endpoint
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `556de8bb` **Darius Wattimena** (2026-07-29): Merge branch 'develop' into TCC-1137-fix-fallback-activities
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt
  #	src/test/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingServiceTest.kt
- `6a726690` **Darius Wattimena** (2026-07-30): Merge branch 'develop' into TCC-1137-fix-fallback-activities
- `37297628` **Darius Wattimena** (2026-07-30): Remove broken code after merging latest develop
- `d5373f57` **Darius Wattimena** (2026-07-30): Use aggregation instead of distinct for the fallback end detection queries
  Distinct returns all values in a single BSON document capped at 16MB,
  which the broken-entry id sets exceed on real data. An aggregation with
  a group stage streams the same result through a cursor.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `a48748c8` **Darius Wattimena** (2026-07-30): Add partial indexes for the fallback end detection queries
  The detection queries scanned the whole normalized collections, which
  takes longer than the load balancer request timeout. A partial index
  per collection containing only the documents with a fallback end keeps
  the queries fast and the indexes small. Index creation runs on a
  background thread so application startup isn't blocked by the initial
  index builds.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `cb6e5689` **Darius Wattimena** (2026-07-31): Drop the status endpoint, run the repair detection fully in the background
  Even indexed, counting all broken entries takes longer than the load
  balancer request timeout. The scheduling endpoint now returns
  immediately and does both the detection and the queueing on a
  background thread, with the totals visible in the logs instead of a
  status response.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>

## Reviews

### augmentcode[bot] — COMMENTED (2026-07-28)

Review completed. 4 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F830%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — COMMENTED (2026-07-29)

_No comment._

### TeqJoostD — DISMISSED (2026-07-29)

_No comment._

## Review Comments

### TeqJoostD — 2026-07-29 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NormalizedStopDataSource.kt`

Mongo doesn't persist null right?

## Comments

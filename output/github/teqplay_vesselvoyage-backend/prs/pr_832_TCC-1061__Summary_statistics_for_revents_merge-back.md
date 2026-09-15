---
id: github:teqplay/vesselvoyage-backend:pr:832
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 832
title: 'TCC-1061: Summary statistics for revents merge-back'
author: TeqJoostD
state: closed
date: '2026-07-29'
merged_at: '2026-08-03'
base_branch: develop
head_branch: TCC-1061
url: https://github.com/teqplay/vesselvoyage-backend/pull/832
labels: []
linked_issues: []
explicit_links: []
---
# PR #832: TCC-1061: Summary statistics for revents merge-back

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/832  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-1061`  
**Created:** 2026-07-29  
**Merged:** 2026-08-03  

## Description

## What

Adds **summary statistics** to the scenario details object shown on the scenario page, comparing the **previous dataset** (the data that gets overwritten during merge-back) with the **newly recalculated dataset**, aggregated over the whole scenario.

The statistics live on `ReventsRecalculationStatus` — the same object that already carries `progress` and `mergeFailureSummary` — as a new nullable `summaryStatistics` field. For both the `before` and `after` datasets it reports:

- Number of visits
- Number of encounters
- Average visit duration (over finished visits; `null` when there are none)

## How

- **Model** (`ReventsRecalculationStatus.kt`): new `summaryStatistics: SummaryStatistics?` (defaults to `null`, so existing constructions are unaffected). `SummaryStatistics(before, after)` where each side is a `DatasetStatistics(numberOfVisits, numberOfEncounters, averageVisitDuration)`.
- **Logic** (`ReventsRecalculationService.kt`): a private `MergeStatisticsCollector` (mirroring the existing `MergeFailureCollector`) accumulates counts and visit durations across every ship and window in the scenario. It's threaded through both merge-back entry points — the polled full-recalc flow (`checkScenarioProgress` → `fetchAndMergeDataV2`) and the explicit `MERGE_ONLY` flow (`runMergeScenario` → `mergeV2Data`) — down to `persistMergeResultV2`.
- In `persistMergeResultV2`, `recordMergeStatistics` captures the before/after snapshot **before the persist overwrites the previous data**:
  - **After** = the recalculated entries and their encounters.
  - **Before** = the existing entries/encounters being overwritten (the previous versions of the upserted ids plus the deleted ones; upsert and delete id sets are disjoint, so nothing is double-counted).
- Both flows attach the aggregated result to the final status persisted via `updateStatus`, so it's returned by the scenario-details endpoints.

## Testing

- New unit test `should record before-after summary statistics when merging back a scenario` in `ReventsRecalculationServiceTest`.
- `compileKotlin`, `ktlintCheck` (main + test), and the full `ReventsRecalculationServiceTest` (new + pre-existing) all pass locally.

## Note

"Previous dataset" is defined as the data actually overwritten per merged window (old versions of upserted entries + deleted entries), aggregated across all ships — matching the ticket's "the data we overwrite with the new data". If whole-scenario totals (including untouched entries) are preferred instead, that's a small change to the aggregation.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Commits

- `c5c78ff6` **TeqJoostD** (2026-07-29): TCC-1061: add before/after summary statistics to revents merge-back
  When merging back a scenario, compute summary statistics comparing the
  previous dataset (the data that gets overwritten) with the newly
  recalculated dataset, aggregated over the whole scenario.
  
  The statistics are exposed on the scenario details object
  (ReventsRecalculationStatus, alongside progress and mergeFailureSummary)
  as a SummaryStatistics(before, after), each carrying:
  - number of visits
  - number of encounters
  - average visit duration
  
  A MergeStatisticsCollector accumulates the counts across every ship and
  window, threaded through both merge-back entry points (the polled
  full-recalc flow and the explicit MERGE_ONLY flow) down to
  persistMergeResultV2, where the before/after snapshot is captured just
  before the persist overwrites the previous data.
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
- `c912a8fc` **TeqJoostD** (2026-07-30): Merge remote-tracking branch 'origin/develop' into TCC-1061
- `46daeb7c` **TeqJoostD** (2026-07-30): TCC-1061: compute merge-back stats from in-memory data, no extra DB reads
  The previous version re-queried visits and ESoFs in persistMergeResultV2
  to build the "before" dataset. That data was already loaded by the merge
  itself (findEntriesForMerge loads the old entries with their ESoFs), so
  the lookups were redundant.
  
  Surface the overwritten old entries on MergeResult.overwrittenEntries
  (the ones replaced in place or deleted), computed from the entries the
  merge already loaded. The field is excluded from MergeResult value
  equality since it is derived context, so the merge unit tests that assert
  on the outcome are unaffected. The statistics collector now derives
  visits/encounters/durations straight from these in-memory wrappers.
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
- `a98f15af` **TeqJoostD** (2026-07-31): TCC-1061: make merge-back stats a full period snapshot
  Before/after now describe the whole period, not just the entries the
  merge touched:
  
  - BEFORE = overwritten (replaced + deleted old versions) + untouched
  - AFTER  = recalculated (result entries) + untouched
  
  Untouched entries survive the merge, so they count on both sides and read
  as "unchanged"; deletes show only in before, creations only in after.
  
  All of it is still derived from the old entries the merge already loaded
  (now surfaced as MergeResult.overwrittenEntries + untouchedEntries) - no
  extra database reads.
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>

## Reviews

### augmentcode[bot] — COMMENTED (2026-07-29)

Review completed. 3 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F832%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### Darius-Wattimena — CHANGES_REQUESTED (2026-07-30)

_No comment._

### Darius-Wattimena — DISMISSED (2026-07-30)

_No comment._

### Darius-Wattimena — APPROVED (2026-07-31)

_No comment._

## Review Comments

### Darius-Wattimena — 2026-07-30 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationService.kt`

Doing finds here to the database is unneeded database operations. We finished merging so we should know all the new visits, voyages and esofs?

### Darius-Wattimena — 2026-07-30 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationService.kt`

Also the counted encounters here is the new amount, not the old amount?

## Comments

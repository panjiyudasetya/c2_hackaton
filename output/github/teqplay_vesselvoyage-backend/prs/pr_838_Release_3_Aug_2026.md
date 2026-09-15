---
id: github:teqplay/vesselvoyage-backend:pr:838
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 838
title: Release 3 Aug 2026
author: Darius-Wattimena
state: closed
date: '2026-08-03'
merged_at: '2026-08-03'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/838
labels: []
linked_issues: []
explicit_links: []
---
# PR #838: Release 3 Aug 2026

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/838  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2026-08-03  
**Merged:** 2026-08-03  

## Description

_No description._

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
- `10ca28dd` **Darius Wattimena** (2026-07-29): Merge pull request #829 from teqplay/claude/pensive-swartz-4ec2d4
  Make NewEntry.shipId non-nullable and drop migration-era fallbacks
- `51f502f2` **TeqJoostD** (2026-07-29): Increasing memory this time for real
- `20695013` **Darius Wattimena** (2026-07-29): Merge pull request #833 from teqplay/increase-vv-data-memory
  Increasing memory this time for real
- `27c74fff` **Darius Wattimena** (2026-07-29): Up version of AisEngine api models
- `de298197` **Darius Wattimena** (2026-07-29): Merge pull request #834 from teqplay/upgrade-ais-engine
  Up version of AisEngine api models
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
- `269e4b39` **Darius Wattimena** (2026-07-31): TCC-1062: record per-ship change statistics on revents merge-back
  Where TCC-1061 answers how a scenario changed the dataset as a whole,
  this answers what changed for one specific ship, per kind of stop,
  encounter and area activity. Every category counts how many items were
  added, modified, removed and left unchanged:
  
  - stops per stop type (berth, anchor, lock, unclassified)
  - encounters in total as well as per encounter type
  - ship-to-ship transfers
  - drifting (slow moving periods)
  - area activities per type, which covers both pass-throughs and the
    port, pilot, anchor, terminal mooring, lock and approach areas
  
  The counts land in a new revents.shipChanges collection, one document
  per scenario + ship, accumulating every window a ship was merged in.
  
  Items cannot be matched on their identifiers: revents replays the AIS
  data into freshly generated events, so the event ids an item refers to
  always differ between both datasets. ChangeMatcher therefore matches on
  time - largest overlap wins, with a tolerance for boundaries that only
  shifted a little - and compares everything but the generated ids to tell
  a modification from an unchanged item.
  
  Drifting is the odd one out. The recalculated entries have no slow
  moving periods at merge time, they are determined by the post-processing
  that runs afterwards. The previous periods are parked on the document
  together with the entries still to be post-processed, and
  EndPostProcessingEvent now carries the periods it just computed so the
  counts can be filled in once the last entry reports back. Until then the
  document says driftingPending instead of reporting a wrong number.
  
  Recording is best-effort: a failure is logged, never propagated, so
  statistics can't break a merge.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `e1ef5c79` **Darius Wattimena** (2026-07-31): TCC-1062: expose the per-ship merge-back changes over HTTP
  Two read endpoints on the recalculation controller, so the scenario page
  can show the per-ship changes view:
  
    GET /v2/recalculate/{scenarioId}/changes
    GET /v2/recalculate/{scenarioId}/changes/ship/{shipId}
  
  Both are guarded by recalculation:read, like the other recalculation
  reads. The internal drifting bookkeeping is stripped before returning;
  consumers read drifting and driftingPending instead.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `b1ead8b7` **Darius Wattimena** (2026-07-31): TCC-1153 Expose the encounter id in the ship encounter API
  Add a required `id` field to `ShipEncounterEntry`, populated from the
  normalized encounter's `_id` ("{entryId}:{startEventId}"), so consumers of
  /v2/encounter/byShipId, /byImo and /byMmsi can reference a specific encounter.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `c33c9c8a` **Darius Wattimena** (2026-07-31): Merge pull request #836 from teqplay/claude/encounter-api-ship-id-524529
  TCC-1153 Expose the encounter id in the ship encounter API
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
- `167bcc7a` **Darius Wattimena** (2026-07-31): Merge remote-tracking branch 'origin/TCC-1061' into TCC-1062-support-for-per-ship-changes
  TCC-1061 turned the merge-back statistics into a full period snapshot, so
  the per-ship changes follow suit:
  
  - MergeResult.withOverwrittenEntries became withPreviousEntries, which also
    surfaces the entries the merge left in place (untouchedEntries).
  - Those untouched entries now count on both sides of the per-ship
    comparison too, so their items read as unchanged instead of being left
    out of the picture entirely.
  
  Drifting needs the untouched entries handled apart from the rest. Their
  slow moving periods are already known, but they are never post-processed
  again, so they never report back through EndPostProcessingEvent. Feeding
  them into the previous side only would have made every one of them read as
  removed once the recalculated entries finished post-processing. They are
  therefore seeded into both sides right away, and only the recalculated
  entries are awaited (MergeChanges.driftingComplete).
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `80042e5f` **Darius Wattimena** (2026-07-31): TCC-1062: rename the drifting bookkeeping to unresolvedDrifting
  pendingDrifting and driftingPending read like typos of each other while
  they serve different audiences: the first is the bookkeeping the service
  builds up (parked periods plus the entries still owed), the second is the
  boolean the front-end reads.
  
  Both are still needed - the bookkeeping is stripped before the statistics
  are served, so without the flag a consumer could not tell "not determined
  yet" from "determined", and a null drifting cannot stand in for it: once
  the first window resolves, drifting holds numbers while a later window of
  the same ship can still be outstanding. That last part was documented
  wrongly, which is corrected here as well.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `6d5d1497` **Darius Wattimena** (2026-07-31): TCC-1062: keep reading the drifting bookkeeping under its former name
  Scenarios were already merged back on DEV, so their documents still store
  the bookkeeping as pendingDrifting. Mongo (de)serializes through Jackson
  (MongoJack's codec registry), so a @JsonAlias is enough to keep reading
  them. Without it those documents would not have failed loudly either -
  FAIL_ON_UNKNOWN_PROPERTIES is disabled - their bookkeeping would just have
  read as null, leaving driftingPending stuck on true forever and losing the
  parked periods on the next merged window.
  
  Writing keeps using the current name, so documents converge on their next
  save.
  
  The test that pins this down also caught ChangeCounts.hasChanges being
  serialized into every document as a derived field. It was unused, so it is
  dropped rather than annotated - the stored documents stay free of state
  that can go stale.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `2985182b` **Darius Wattimena** (2026-08-03): Add bulk static ship resolving by shipIds
  The static ship endpoints could only resolve a batch by IMO or by MMSI,
  while a shipId is the identifier the rest of V2 works with. Consumers
  holding shipIds had to fall back to calling the single-ship endpoint once
  per ship.
  
  POST /v1/ships/static/shipIds mirrors the IMO and MMSI variants, including
  leaving unknown ids out of the response instead of failing the request. No
  mapping step is needed since the input already is the identifier, and the
  lookup is an in-memory cache hit, so a batch costs no IO.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `5cb55c04` **Darius Wattimena** (2026-08-03): TCC-1062: drop the imo from the per-ship changes
  The front-end resolves ships through the static ship endpoints, so the
  changes output does not need to carry an IMO of its own - the shipId is
  enough to look one up. It also means the statistics no longer read the
  deprecated NewEntry.imo.
  
  Documents already written on DEV still hold the field. Nothing has to be
  done about that: the Mongo mapper has FAIL_ON_UNKNOWN_PROPERTIES disabled,
  so it is ignored on read and disappears on the next save.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `3a68d4a2` **Joost Dambrink** (2026-08-03): Merge pull request #832 from teqplay/TCC-1061
  TCC-1061: Summary statistics for revents merge-back
- `3f3df7ea` **Darius Wattimena** (2026-08-03): Merge pull request #835 from teqplay/TCC-1062-support-for-per-ship-changes
  TCC-1062: per-ship changes view for recalculation statistics

## Reviews

### TeqJoostD — APPROVED (2026-08-03)

_No comment._

### augmentcode[bot] — COMMENTED (2026-08-03)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F838%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

## Review Comments

## Comments

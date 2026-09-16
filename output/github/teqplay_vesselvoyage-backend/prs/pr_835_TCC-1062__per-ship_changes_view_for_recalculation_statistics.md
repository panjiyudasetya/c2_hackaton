---
id: github:teqplay/vesselvoyage-backend:pr:835
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 835
title: 'TCC-1062: per-ship changes view for recalculation statistics'
author: Darius-Wattimena
state: closed
date: '2026-07-31'
merged_at: '2026-08-03'
base_branch: develop
head_branch: TCC-1062-support-for-per-ship-changes
url: https://github.com/teqplay/vesselvoyage-backend/pull/835
labels: []
linked_issues: []
explicit_links: []
---
# PR #835: TCC-1062: per-ship changes view for recalculation statistics

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/835  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-1062-support-for-per-ship-changes`  
**Created:** 2026-07-31  
**Merged:** 2026-08-03  

## Description

Extends the merge-back statistics of TCC-1061 with the per-ship changes view. Targets `TCC-1061`, so the diff only shows this ticket's work.

Where TCC-1061 answers *how did this scenario change the dataset as a whole*, this answers *what changed for this specific ship*. Every category counts how many items were **added**, **modified**, **removed** and left **unchanged**:

- stops per stop type — berth, anchor, lock, unclassified
- encounters in total **and** per encounter type
- ship-to-ship transfers
- drifting (slow moving periods)
- area activities per type, which covers both pass-throughs (port, EOSP) and the port, pilot, anchor, terminal mooring, lock and approach areas

The counts land in a new `revents.shipChanges` collection, one document per scenario + ship, accumulating every window a ship was merged in.

## How items are matched

Items cannot be matched on their identifiers: revents replays the AIS data into freshly generated events, so the event ids a stop or encounter refers to — and anything derived from them — always differ between the previous and the recalculated dataset. Matching on ids would report nearly everything as removed + added and never as modified.

`ChangeMatcher` therefore matches on **time**: within a category, the pair with the largest overlap wins, and non-overlapping items may still be paired when the gap stays within a 15 minute tolerance, which covers an activity whose boundaries only shifted. Two matched items are *unchanged* when everything but the generated ids is equal, and *modified* otherwise. `otherMmsi` (encounters, ship-to-ship) and `areaId` (area activities) act as hard identity, so a different vessel or a different area is never a modification.

## Drifting is resolved later

At merge time the recalculated entries have no slow moving periods yet — drift is determined by the post-processing that runs afterwards. Counting the previous periods against an empty side would report every one of them as removed.

Instead the previous periods are parked on the document together with the entries still to be post-processed. `EndPostProcessingEvent` now carries the periods it just computed, so `ShipChangeStatisticsService` can fill in the counts once the last entry reports back — no extra reads. Until then the document exposes `driftingPending = true` and a null `drifting`, rather than a wrong number.

Two caveats worth knowing: a previous ESoF that was never post-processed (`slowMovingPeriods == null`) counts as no drifting, and if post-processing never completes for an entry the document stays `driftingPending` instead of reporting something wrong.

## Endpoints

Second commit, guarded by `recalculation:read` like the other recalculation reads:

```
GET /v2/recalculate/{scenarioId}/changes
GET /v2/recalculate/{scenarioId}/changes/ship/{shipId}
```

Both strip the internal drifting bookkeeping before returning; consumers read `drifting` and `driftingPending`.

## Notes

- Area activities cover the full `AreaActivityType` enum, so `BERTH`, `ANCHOR` and `OTHER_ONGOING_EOSP` are included on top of the types the card lists — same vocabulary as `NormalizedVisit`, no silent gaps.
- Recording is best-effort: a failure is logged, never propagated, so statistics can't break a merge.
- The two commits are split so the endpoint changes stand on their own; each was verified to build and pass on its own.

## Testing

`./gradlew ktlintCheck test` — clean, 2222 tests, 0 failures, 35 of them new (`ChangeMatcherTest`, `ShipChangeStatisticsCalculatorTest`, `ShipChangeStatisticsServiceTest`, plus one on the merge-back wiring in `ReventsRecalculationServiceTest`). All four Spring context tests pass, so the new beans wire in every profile.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Commits

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

## Reviews

### augmentcode[bot] — COMMENTED (2026-07-31)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F835%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — APPROVED (2026-08-03)

_No comment._

## Review Comments

## Comments

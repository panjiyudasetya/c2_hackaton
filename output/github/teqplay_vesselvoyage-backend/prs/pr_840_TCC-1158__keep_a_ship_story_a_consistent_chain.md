---
id: github:teqplay/vesselvoyage-backend:pr:840
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 840
title: 'TCC-1158: keep a ship story a consistent chain'
author: Darius-Wattimena
state: closed
date: '2026-08-04'
merged_at: '2026-08-05'
base_branch: develop
head_branch: claude/tcc-1158-investigation-cdbf3f
url: https://github.com/teqplay/vesselvoyage-backend/pull/840
labels: []
linked_issues: []
explicit_links:
- jira:TCC-1158
---
# PR #840: TCC-1158: keep a ship story a consistent chain

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/840  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `claude/tcc-1158-investigation-cdbf3f`  
**Created:** 2026-08-04  
**Merged:** 2026-08-05  

## Description

Fixes [TCC-1158](https://teqplaybv.atlassian.net/browse/TCC-1158). Pocca reported ships missing from a SmartFleet fleet; IMO 1030040 could not be resolved because the tail of its story was broken at one seam — a voyage truncated to 2m53s pointing at a visit that did not exist, and the visit that did follow starting 15h47m later with no `previous` and no `destination`.

## Root cause

A dry run reproduces the break with no database involved, so the replay produces it by itself. Two facts pin it down:

- The voyage carries `next = 81d7fdaa…VISIT` **and** the matching `destinationPort`, which only `finishVoyage` writes together — so that visit was created and then deleted.
- The following visit has `previous` and `destination` both null, which is the signature of `createNewVisit` being handed no current voyage — an entry created while the status was `NewInitialShipStatus`.

A `NewShipStatus` only carries the current entry and the two before it, and processing regularly walks further back than that: resuming a visit after drifting out of an EOSP, or resuming a voyage after a pass-through. Those paths set the references they can no longer describe to `null`, and every later decision that needs the preceding entry then silently does the wrong thing — a main port swap cannot re-link it, a pass-through cannot resume it and cancels the visit outright, resetting processing mid-story and leaving a hole in the timeline.

## Fix

Every entry stores its own `previous`, so the missing context can always be looked up by id. `EntryResolver` does that, with two implementations because the two pipelines keep their entries in different places:

- `StoredEntryResolver` — datasource lookups, for the live event pipeline.
- `ReplayEntryResolver` — records the changes a replay produces, for the dry run, the story repair and the revents replay. A replay starts from an initial status, so nothing it produced is stored yet and a datasource lookup would find nothing.

The status is completed on the way into processing at the three entry points rather than by threading a resolver through all 119 `onEventAndBuffer` call sites. Only missing references are looked up, so a healthy status costs nothing.

Two smaller processing fixes: the drift-back resume keeps pointing at the voyage before the resumed visit (no lookup needed at all), and a visit another entry references is closed rather than cancelled away when it turns out to be a pass-through.

## Also included

The first commit fixes real defects found while investigating, which are **not** what broke this ship:

- `StoryRepairService.mergeChanges` decided create-vs-update from the deleted time window rather than from what is stored, so a replayed entry stored outside that window stayed a `CREATE` and failed on a duplicate `_id`.
- `PersistChangesService` swallowed a failed bulk write while the caller went on to publish, reset the ship status and mark the repair finished. Added `persistChangesOrThrow` for the repair; the live consumer keeps its swallow-and-log.
- The datasources delete before they upsert, so a failing upsert emptied a range of the story without writing it back. They now write first when the id sets are disjoint.
- Both visit re-keying paths set the previous voyage's `next` but never the new visit's `previous`.

`StoryChainValidator` reports dangling references, one-sided links, gaps, overlaps and entries that end before they start — logged and counted, never blocking, so a story that is already broken stays writable and can be repaired. Exposed read-only as `GET /v2/recalculate/ship/{shipId}/validateStory`.

## Verification

`Tcc1158StoryChainScenarioTest` replays the 399 recorded events of IMO 1030040 through the real processors and asserts chain invariants. The story now reads:

| entry | from → to |
|---|---|
| `d4138d31…VISIT` (Campana) | 07-17 09:18:55 → 07-20 00:14:22 |
| `90e431f4…VOYAGE` | 07-20 00:14:22 → 07-20 02:04:23 |
| `6b1e6999…VISIT` (La Plata anchorage) | 07-20 02:04:23 → 07-22 10:14:03 |

Gap closed, links reciprocal, `previous` populated. The 2m53s voyage is deliberately gone: the ship left the Campana EOSP for 10 hours, made a 55 km run upriver without calling at any port, and came back, so the drift-back and pass-through rules fold it into the Campana visit as six pass-through EOSPs — reviewed against the trace and correct.

2272 tests pass, ktlint clean.

## Still to do

- Run `POST /v2/recalculate/ship/2aa38d4d-e966-4ba5-883b-4ce47772cf95/repairStory`, then `validateStory` to confirm, and check the ship resolves into the expected fleet.
- `ReventsRecalculationService.processShipIdForMergingV2` computes and persists a merge outside `ShipLockService` with `refreshShipStatus = false` — a real TOCTOU against the live pipeline, but not this bug and needing a distributed lock. Worth its own ticket.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

[TCC-1158]: https://teqplaybv.atlassian.net/browse/TCC-1158?atlOrigin=eyJpIjoiNWRkNTljNzYxNjVmNDY3MDlhMDU5Y2ZhYzA5YTRkZjUiLCJwIjoiZ2l0aHViLWNvbS1KU1cifQ

## Commits

- `8e327602` **Darius Wattimena** (2026-08-03): TCC-1158: stop the story repair leaving a half-written chain
  A story repair rewrites the tail of a ship story as one logical operation,
  but commits it as three independent, error-swallowing Mongo batches. For
  IMO 1030040 the voyage batch committed while the visit batch did not,
  which is what produced the whole reported symptom set at once: a voyage
  truncated to 2m53s, its next pointing at a visit that does not exist, and
  a ~16 hour hole in the timeline.
  
  The visit batch failed on a duplicate _id. Entry ids are derived from
  event ids, so a replay can re-create an entry whose stored version starts
  outside the repaired time range. mergeChanges only converted a CREATE
  into an UPDATE for ids it found in the time-window delete set, so such an
  entry stayed a CREATE and took the whole collection's batch down with it.
  Because deletes ran before the upserts, the range was emptied and never
  refilled, and PersistChangesService only logged the failure while the
  repair went on to publish, reset the ship status and mark itself done.
  
  - Resolve create-versus-update from what is actually stored (findByIds)
    instead of from the deleted time range, and drop the !! that went with
    the old bookkeeping.
  - Add persistChangesOrThrow and use it from the repair, so a failure no
    longer publishes, resets the ship status or finishes the repair. The
    live event pipeline keeps its swallow-and-log behaviour.
  - Write before deleting when a batch's written and deleted ids are
    disjoint, so a failing write changes nothing instead of leaving a hole.
    Same-id delete-and-recreate still deletes first.
  
  Separately, previous and destination both being null on a mid-story visit
  is the fingerprint of an entry created under NewInitialShipStatus, which
  every dry run starts from. The repair restored only previous, and only on
  the first replayed entry, so a null destination propagated down the tail
  by inheritance. Destination is now restored from the attaching voyage and
  carried forward until an entry reports its own.
  
  Both visit re-keying paths set the previous voyage's next but never the
  new visit's previous, and skipped the voyage update entirely when the
  previous voyage was not at hand, leaving that voyage pointing at the
  visit they had just deleted. They now write the link from both sides, and
  keep the existing id when the predecessor cannot be re-linked: the port
  correction still applies, only the id no longer follows the leading EOSP.
  
  Finally, add StoryChainValidator, which reports dangling references,
  one-sided links, gaps, overlaps and entries that end before they start.
  It logs and counts violations without ever blocking a write, so a story
  that is already broken stays writable and can be repaired. Exposed
  read-only as GET /v2/recalculate/ship/{shipId}/validateStory.
  
  Gaps are found by walking the entries in time order rather than by
  following links, because the missing link is exactly what a hole in the
  timeline looks like.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `90711b6a` **Darius Wattimena** (2026-08-03): TCC-1158: resolve a ship status's previous entries instead of losing them
  The dry run of IMO 1030040 reproduces the broken story with no database
  involved, so the earlier diagnosis was wrong about where this breaks: the
  replay produces it by itself. Two facts from that output pin it down. The
  voyage carries both `next = 81d7fdaa…VISIT` and the matching
  `destinationPort`, which only `finishVoyage` writes together, so that
  visit was created and then deleted again. And the visit that does follow
  has `previous` and `destination` both null, which is the signature of
  `createNewVisit` being handed no current voyage - an entry created while
  the status was NewInitialShipStatus. So the replay deleted a visit and
  reset itself mid-story, orphaning the voyage before it and leaving 15h47m
  of the timeline uncovered.
  
  A NewShipStatus only carries the current entry and the two before it, and
  processing regularly walks further back than that: resuming a visit after
  a drift-out of an EOSP, or resuming a voyage after a pass-through. Those
  paths set the references they can no longer describe to null, and from
  there every later decision that needs the preceding entry silently does
  the wrong thing - a main port swap cannot re-link it, a pass-through
  cannot resume it and cancels the visit outright.
  
  Every entry stores its own `previous`, so the missing context can always
  be looked up by id. Add an EntryResolver for that, with two
  implementations, because the two pipelines have their entries in
  different places:
  
  - StoredEntryResolver looks them up in the datasources, for the live
    event pipeline.
  - ReplayEntryResolver records the changes a replay produces, for the dry
    run, the story repair and the revents replay. A replay starts from an
    initial status, so nothing it produced is stored yet and a datasource
    lookup would have found nothing - which is exactly the path being
    debugged here.
  
  The status is then completed on the way into processing at the three
  entry points (EntryProcessingService.insertNew and its dry run, plus
  EventsReventsMessageProcessor), rather than by threading a resolver
  through all 119 onEventAndBuffer call sites. Only missing references are
  looked up, so a healthy status costs nothing.
  
  Two smaller fixes on top:
  
  - The drift-back resume keeps pointing at the voyage before the resumed
    visit rather than nulling it. Deleting the drifted-out voyage does not
    change what came before, and this needs no lookup at all.
  - A visit that another entry references is no longer cancelled away when
    it turns out to be a pass-through; it is closed instead, so nothing is
    left referencing an entry that stopped existing.
  
  ReplayEntryResolver.record also replaces the change-folding that
  processAisEngineEventsDryRunForStoryV2 did inline, so the dry run and the
  resolver agree on the story by construction instead of by duplication.
  
  Tcc1158StoryChainScenarioTest is included but red: it needs the real
  event list saved to src/test/resources/scenarios/1030040-tcc-1158.json,
  which is deliberately not invented here. It fails with that instruction
  until the fixture is in place.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `5a1454e7` **Darius Wattimena** (2026-08-04): TCC-1158: verify the story chain fix against the real events of IMO 1030040
  Replays the 436 recorded AIS engine events through the real processors and
  asserts the resulting story is a consistent chain: every reference
  resolves, both sides of each link agree, and the timeline is covered
  without gaps or overlaps.
  
  The seam assertion walks from the Campana visit to the La Plata anchorage
  visit rather than naming the 2m53s voyage the broken run produced. That
  voyage is deliberately no longer there: it only existed because the ship
  stepped outside the Campana EOSP for three minutes and the drift-back
  could not re-link it. The Campana visit now runs until the ship actually
  leaves that EOSP at 2026-07-20T00:14:22Z, followed by a 1h50m passage
  down to the anchorage - so the reported 15h47m hole is covered and the
  anchorage visit has a predecessor again.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `a965be22` **Darius Wattimena** (2026-08-04): Reduced events to the only ones we actually retrieve from the backend
- `72e54c64` **Darius Wattimena** (2026-08-04): Merge branch 'develop' into claude/tcc-1158-investigation-cdbf3f

## Reviews

### augmentcode[bot] — COMMENTED (2026-08-04)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F840%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — APPROVED (2026-08-04)

_No comment._

## Review Comments

## Comments

### TeqJoostD — 2026-08-04

augment review



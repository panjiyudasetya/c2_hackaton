---
id: github:teqplay/vesselvoyage-backend:pr:844
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 844
title: Release 6 Aug 2026
author: Darius-Wattimena
state: closed
date: '2026-08-06'
merged_at: '2026-08-06'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/844
labels: []
linked_issues: []
explicit_links: []
---
# PR #844: Release 6 Aug 2026

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/844  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2026-08-06  
**Merged:** 2026-08-06  

## Description

_No description._

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
- `60625428` **Darius Wattimena** (2026-08-05): Merge pull request #840 from teqplay/claude/tcc-1158-investigation-cdbf3f
  TCC-1158: keep a ship story a consistent chain

## Reviews

### TeqJoostD — APPROVED (2026-08-06)

_No comment._

## Comments

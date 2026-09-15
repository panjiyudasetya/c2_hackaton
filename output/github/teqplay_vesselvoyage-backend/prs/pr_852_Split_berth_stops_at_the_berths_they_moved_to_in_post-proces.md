---
id: github:teqplay/vesselvoyage-backend:pr:852
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 852
title: Split berth stops at the berths they moved to in post-processing
author: TeqJoostD
state: closed
date: '2026-08-11'
merged_at: '2026-08-18'
base_branch: develop
head_branch: claude/stop-berth-matching-ml8o3y
url: https://github.com/teqplay/vesselvoyage-backend/pull/852
labels: []
linked_issues: []
explicit_links: []
---
# PR #852: Split berth stops at the berths they moved to in post-processing

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/852  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `claude/stop-berth-matching-ml8o3y`  
**Created:** 2026-08-11  
**Merged:** 2026-08-18  

## Description

## The problem

A stop's berth is decided **once, from its start location**, and never revisited — `createNewStop` classifies the start point and freezes `type` + `areaId` for the stop's whole life. A ship that shifts along the quay without producing a stop end event therefore keeps one stop carrying the first berth for the entire stay, while `NewVisit.berthAreaActivities` correctly records both berth calls.

```
Stop     BERTH A ─────────────────────────────────  12:00 → 24:00
Berths   BERTH A ──────────────  BERTH B ─────────  12:00 → 18:00, 18:00 → 24:00
```

The second berth call is then **lost entirely**, not just mislabelled. Both SoF generators only keep berth activities whose area matches the stop's own berth (`alignWithBerthActivities`), so Berth B never becomes a berth visit — no terminal visit, no ATB, no ATD. This recovers missing berth calls rather than relabelling one.

## The rule

If another berth happens during a berth-classified stop, split the stop there — **unless that berth already has a stop of its own.**

Two properties the implementation deliberately holds on to:

- **The stop's own start and end never move.** A split only adds boundaries inside them, so the original span stays partitioned exactly, with no gaps and no overlaps. A stop that began before the ship entered the berth polygon keeps that overhang.
- **"Already has a stop" is matched per berth *call*, not per berth.** A ship doing A → B → back to A still gets a second stop for the evening return to A, because that call has no stop covering it. Matching on berth alone would lose it — the exact bug being fixed.

Three berths inside one stop means two cuts; stops with nothing new inside them are skipped without a write. There is no configuration: the splitter either finds an unaccounted berth call inside a stop or leaves the stop alone.

## Changes

- **`BerthStopSplitter`** (new, `service/postprocessing/`) — the rule as a pure, injectable class.
- **`PostProcessingService`** — runs the splitter, emits a `VisitChange`, and refreshes the entry cached on the ship status.
- **`FallbackType.STOP_SPLIT_BY_BERTH`** — marks derived boundaries so consumers can distinguish them from real stop events.

## Two things worth a reviewer's attention

**1. This is the first post-processing step that rewrites the entry, not just the ESoF.** The class KDoc previously said post-processing only mutates the ESoF; that contract is now explicitly relaxed for this one step, and the KDoc says so. The plumbing already supported it (`PersistChangesService` handles `VisitChange`, `PreviousEntryVersions.fromEntries` takes entries).

Consequence worth checking: `updateMatchingRecentVisitOrVoyageWrapper` now replaces the **entry** on the cached ship status, not only the esof. Without that, `EndOfSeaPassageStartProcessor.resumeVisit` reuses the cached entry and silently restores the pre-split stops.

**2. Segments need derived start event ids.** A stop's document id is `"{entryId}:{startEventId}"` and `NormalizedVisit.stopIds` is built from it with no uniqueness guard — reusing one silently drops a stop on the normalize round-trip. Later segments get `"{original}:berth:{berthActivityId}"`, derived from the berth activity's event id so a re-run reproduces them exactly and diffs to a no-op.

## Testing

15 tests for the splitter covering the split cases (two berths, three berths, the return-to-a-berth case), the skip cases (berth already has a stop, non-berth stops, ongoing stops, boundary outside the stop), plus edge preservation, id uniqueness, fallback marking, and idempotency. 2 tests in `PostProcessingServiceTest` cover the integration point: a `VisitChange` carrying the split stops is persisted and the cached entry is refreshed, and no `VisitChange` is emitted when nothing needed splitting.

⚠️ **The tests have not been executed.** They were written and reviewed but the sandbox they were authored in has no credentials for `s3://repo.teqplay.nl` (and jitpack 403s), so the `nl.teqplay.*` dependencies do not resolve and the project cannot compile there. `./gradlew ktlintCheck` passes clean, all model fields and test factory signatures were verified against source, and no test or resource hardcodes the `FallbackType` values — but **please treat the first CI run as the real compile check before merging.**

## Note on rollout

Re-running post-processing on already-split visits is a no-op (segments end where the next berth call begins, and `StartEnd` ranges are end-exclusive), so a backfill via existing recalculation paths is safe.

## Judgement call

Two berth calls starting on the exact same instant can only produce one boundary; the earliest-listed wins and the other is dropped. Deterministic, but arbitrary — if this shows up in real data it likely indicates overlapping berth polygons, which is a separate discussion.

## Commits

- `0a46151a` **Claude** (2026-08-11): Split berth stops at the berths they moved to in post-processing
  A stop's berth is decided once, from its start location, and never
  revisited. A ship that shifts along the quay without producing a stop end
  event keeps one stop carrying the first berth for the whole stay, while
  the visit's berth activities correctly record both calls.
  
  The second berth call is then lost entirely rather than just mislabelled:
  the SoF generators only keep berth activities matching the stop's own
  berth, so it never becomes a berth visit, terminal visit, or ATB/ATD.
  
  Add BerthStopSplitter, run as a post-processing step: if another berth
  happens during a berth-classified stop, split the stop there, unless that
  berth already has a stop of its own. Two properties it holds on to:
  
  - The stop's own start and end never move. A split only adds boundaries
    inside them, so the original span stays partitioned exactly, with no
    gaps and no overlaps.
  - "Already has a stop" is matched per berth call, not per berth, so a ship
    returning to a berth later in the visit still gets a second stop for
    that second call.
  
  Segments carry derived start event ids because a stop's document id is
  built from its start event id with no uniqueness guard, and derived
  boundaries are marked with a new STOP_SPLIT_BY_BERTH fallback type so
  consumers can tell them from real stop events.
  
  This is the first post-processing step that rewrites the entry itself
  rather than only the ESoF, so PostProcessingService now emits a
  VisitChange and refreshes the entry cached on the ship status - without
  that, resuming the visit would restore the pre-split stops. Guarded by
  post-processing.split-berth-stops as a kill switch.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01TLDWmWxCC92V5sQDdf7AFw
- `08a31f05` **Claude** (2026-08-11): Drop the berth stop split feature flag
  The flag was not asked for and the splitter needs no configuration: it
  either finds an unaccounted berth call inside a stop or leaves the stop
  alone.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01TLDWmWxCC92V5sQDdf7AFw
- `789eac3d` **Claude** (2026-08-14): Reconsider new segments so a return to the stop's own berth is split
  Splitting advanced the index past every segment it had just created, so a
  new segment was never itself considered for further cuts. Combined with
  the first pass only looking at berth calls foreign to the stop's own
  berth, a stop covering A -> B -> A lost the return to berth A: the cut at
  B was made, but the berth B segment that would expose the return to A was
  skipped.
  
  That reproduced exactly the data loss this splitter exists to prevent. The
  existing three berth test did not catch it because A -> B -> C are all
  foreign to A and so are collected in a single pass; the hole only opens
  when a berth repeats inside one stop.
  
  Leave the index in place after a split instead. This terminates because a
  berth call that produced a cut opens a segment carrying that same berth,
  so it is no longer foreign to it and can never cut again.
  
  The segment needing the extra cut is not always the last one, so
  re-checking only the final segment would have been incomplete - covered by
  a test for A -> B -> A -> C, where the un-cut return sits in the middle.
  
  Reported by augmentcode on PR #852.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01TLDWmWxCC92V5sQDdf7AFw

## Reviews

### augmentcode[bot] — COMMENTED (2026-08-11)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F852%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — COMMENTED (2026-08-14)

_No comment._

### Darius-Wattimena — APPROVED (2026-08-18)

_No comment._

## Review Comments

### TeqJoostD — 2026-08-14 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/postprocessing/BerthStopSplitter.kt`

Confirmed and fixed in 789eac3.

I reproduced this by simulating the splitter loop against the real start-inclusive / end-exclusive `overlaps` semantics rather than by inspection. For one `BERTH A` stop over berth calls A(12–16), B(16–20), A(20–24), the splitter produced `[A 12–16, B 16–24]` — the return to berth A lost, and four hours wrongly attributed to berth B. Exactly the data loss this splitter exists to prevent.

Worth noting the existing three-berth test didn't catch it because A → B → C are all foreign to A and get collected in a single pass. The hole only opens when a berth *repeats* inside one stop.

**One correction to the report:** the segment needing the extra cut isn't always the one just created at the tail. For A → B → A → C in a single stop, the un-cut return to A sits inside the *middle* B segment, so re-checking only the final segment would have been an incomplete fix. Every new segment has to be reconsidered.

The fix drops `index += segments.size` and leaves the index in place. Termination still holds: a berth call that produced a cut opens a segment carrying that same berth, so it is no longer foreign to it and can never cut again — cuts stay bounded by the berth-call count.

Three regression tests added: the reported A → B → A case (also asserting the two berth A segments keep distinct document ids), the A → B → A → C middle-segment case, and idempotency on re-run. The five existing scenarios — A → B, A → B → C, A → B → A across two separate stops, already-correct visits, and re-runs — are unchanged.

---
_Generated by [Claude Code](https://claude.ai/code)_

## Comments

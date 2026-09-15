---
id: github:teqplay/vesselvoyage-backend:pr:860
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 860
title: Delete port visits the recalculation no longer produces
author: TeqJoostD
state: closed
date: '2026-08-20'
merged_at: '2026-08-25'
base_branch: develop
head_branch: claude/port-recalc-polygon-size-v6ceyb
url: https://github.com/teqplay/vesselvoyage-backend/pull/860
labels: []
linked_issues: []
explicit_links: []
---
# PR #860: Delete port visits the recalculation no longer produces

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/860  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `claude/port-recalc-polygon-size-v6ceyb`  
**Created:** 2026-08-20  
**Merged:** 2026-08-25  

## Description

## Problem

When a port's polygons are redrawn much smaller, a port recalculation leaves stale visits behind, twice over:

1. Revents resolves the port's interests from the **current** polygons (0.1° bucket cover of their bounding boxes), so ships whose visits only exist because of the old, larger geometry are never part of the scenario at all.
2. Merge-back only force-deleted existing port visits when the replay produced **zero entries** for the whole window. A ship whose replay produced *something* (a sail-past voyage, a visit at another port) but no visit at the requested port kept its old, oversized visit untouched.

## Changes

**Expected-ship follow-up** (`recalculateByPort` / `fetchAndMergeDataV2`)
`recalculateByPort` captures `expectedShipIds` up front: every ship with a stored visit at the port (main-port aware, sub-ports included) overlapping the requested window. After merge-back these are diffed against the ships that actually merged; missed ships are recalculated in an automatic follow-up ships scenario. A ships scenario never computes an expected-ship diff of its own, so this cannot loop.

**New `deleteExisting` rule** (`ReventsReplayMergeService.buildMergeEntries`)
For port-scoped recalculations, a merge window whose replay contains no visit at the requested port sets `deleteExisting = true`, so the stale port visits are removed and their surrounding voyages (including 3+ voyage chains) are collapsed into one spanning voyage. Evaluated pre-pruning, so a port visit seen only in the window margin still counts as existing.

**Scenario-window deletion semantics** (`ReventsRecalculationService`)
Inside the scenario window there is always a verdict, so an old port visit with no overlapping recalculated visit is deleted:
- Force-deletion containment is measured against the **whole scenario window**, not the per-interest merge window.
- A post-merge sweep (`deleteOrphanPortVisits`) deletes remaining port visits that no merged window covers, bridging the surrounding voyages via the normal merge machinery. Partial interest windows do **not** protect their visits — a ship continuously near the port gets one giant partial window, which would shield exactly the stale visits the recalculation is meant to remove.
- The **only** protected visits are those crossing the scenario window boundary: kept, reported once per ship as a `VISIT_EXCEEDS_MERGE_WINDOW` warning (phase → `PARTIALLY_FAILED`), and routed into the existing retry-gated full-history recalculation. Ongoing visits (`end == null`) are kept silently — the live pipeline owns them.

## Tests

- `ReventsReplayMergeServiceTest`: port-scoped `deleteExisting` rules incl. margin conservatism; interest windows reported via `ShipMergeData`.
- `ReventsRecalculationServiceTest`: expected-ship capture + follow-up scheduling; containment against the scenario window (straddler kept + warned, contained deleted); one aggregated warning per ship; ongoing visit kept silently; orphan sweep deletes visits outside merged windows (including under partial windows) while merged-window visits stay with their per-window merge and boundary-crossing visits are warned; full-history retry scheduling.

Design doc with visualisations: internal artifact "Recalculating a Shrunken Port".

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01HrHpkpQnfztTtz6jcmKfaB

## Commits

- `46f9ea3b` **Claude** (2026-08-20): Delete port visits the recalculation no longer produces
  For port-scoped recalculations, a merge window whose replay produced
  entries but no visit at the requested port now sets deleteExisting, so
  stale visits from an old (larger) port polygon are removed and their
  surrounding voyages are bridged into one, instead of being left
  untouched because the replay was non-empty.
  
  Force-deletion also gains a containment guard: a visit that exceeds the
  merge window is never deleted (the replay only partially observed it).
  Such visits are kept, reported as a VISIT_EXCEEDS_MERGE_WINDOW warning
  on the recalculation status, and retried through the existing
  full-history ship recalculation so the whole visit is replayed with
  evidence.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01HrHpkpQnfztTtz6jcmKfaB
- `f0dacd05` **Claude** (2026-08-20): Fix import ordering in ReventsRecalculationServiceTest
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01HrHpkpQnfztTtz6jcmKfaB
- `12d49ca6` **Claude** (2026-08-20): Create port mocks before stubbing in ReventsReplayMergeServiceTest
  Building the Port mock inline inside thenReturn() starts a new stubbing
  while the infraService stubbing is still open, which Mockito rejects
  with UnfinishedStubbingException.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01HrHpkpQnfztTtz6jcmKfaB
- `7f69748b` **Claude** (2026-08-20): Follow-up recalculation for port ships the scenario missed
  recalculateByPort now captures the expected ship set up front: every
  ship with a stored visit at the port (main-port aware, sub-ports
  included) overlapping the requested window. After the scenario's
  merge-back, these expected ships are diffed against the ships that
  actually merged; ships the polygon-based interest resolution could not
  reach (e.g. after the port polygon shrank) or whose interest was
  partial are recalculated in an automatic follow-up ships scenario over
  the same window.
  
  The follow-up is a ships scenario, which never computes an
  expected-ship diff of its own, so the mechanism cannot loop.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01HrHpkpQnfztTtz6jcmKfaB
- `075a2577` **Joost Dambrink** (2026-08-20): Merge branch 'develop' into claude/port-recalc-polygon-size-v6ceyb
- `cebb69a6` **Claude** (2026-08-21): Aggregate VISIT_EXCEEDS_MERGE_WINDOW per ship and skip ongoing visits
  The warning was recorded once per merge window, so a frequent visitor
  produced a dozen warnings for one underlying problem; it is now emitted
  once per ship, listing all affected visits. Ongoing visits (end == null)
  are kept silently without warning or retry: the live pipeline owns them
  and they can never be fully observed, so they would re-warn on every
  recalculation without being actionable.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01HrHpkpQnfztTtz6jcmKfaB
- `ad633857` **Claude** (2026-08-21): Delete port visits outside every interest window
  Absence of an interest window is itself evidence: revents resolved the
  ship's presence at bucket level, so a period without any interest window
  means the ship was not near the port at all. Force-deletion containment
  is therefore measured against the whole scenario window instead of the
  per-interest merge window, and a new sweep deletes remaining port visits
  that lie outside every resolved interest window (partial windows count
  as observed and are never swept, since their data is incomplete).
  
  VISIT_EXCEEDS_MERGE_WINDOW now only fires for visits crossing the
  scenario window boundary itself - the one case where the recalculation
  genuinely did not observe the whole visit.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01HrHpkpQnfztTtz6jcmKfaB
- `d467d370` **Claude** (2026-08-21): Build ShipMergeData before stubbing in the bootstrap test
  shipMergeData reads the mocked MergeEntryV2's window; doing that inside
  thenReturn() interacts with a mock while the outer stubbing is still
  open, which Mockito rejects with UnfinishedStubbingException.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01HrHpkpQnfztTtz6jcmKfaB
- `5dc3d83a` **Claude** (2026-08-21): Drop the partial-window protection from the orphan sweep
  Inside the scenario window there is always a verdict: merged windows'
  replay handles the visits they overlap, and everywhere else the
  recalculation produced no visit - so the old visit must go. Partial
  interest windows no longer shield their visits (a ship continuously
  near the port gets one giant partial window, which protected exactly
  the stale visits a port recalculation is meant to remove). The only
  protected visits are those crossing the scenario window boundary.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01HrHpkpQnfztTtz6jcmKfaB
- `72b3d947` **Claude** (2026-08-21): Merge remote-tracking branch 'origin/develop' into claude/port-recalc-polygon-size-v6ceyb
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsReplayMergeService.kt
  #	src/test/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsReplayMergeServiceTest.kt
- `0f64c132` **Claude** (2026-08-21): Defer expected-ship collection to merge time so recalculateByPort responds immediately
  The visit query over the full requested window is slow for busy ports and
  blocked the API response. Computing it at merge time is equivalent: merged
  ships are excluded from the diff regardless, and unmerged ships' visits are
  untouched by the merge. The computed set is persisted onto the stored
  RecalculationPortResult for inspection.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01HrHpkpQnfztTtz6jcmKfaB
- `1a194de3` **Joost Dambrink** (2026-08-25): Merge branch 'develop' into claude/port-recalc-polygon-size-v6ceyb
- `c3150c37` **Claude** (2026-08-25): Fix compile error in test stub left by develop merge
  The merge of develop brought in a test (#859) that still stubbed
  ReventsReplayMergeService.buildMergeEntries with a List<MergeEntryV2>,
  while this branch changed its return type to ShipMergeData. Use the
  existing shipMergeData helper like the surrounding tests.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01Gxe5f4xMwEPPSevPXkw45p

## Reviews

### augmentcode[bot] — COMMENTED (2026-08-20)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### Darius-Wattimena — DISMISSED (2026-08-25)

_No comment._

### Darius-Wattimena — APPROVED (2026-08-25)

_No comment._

## Comments

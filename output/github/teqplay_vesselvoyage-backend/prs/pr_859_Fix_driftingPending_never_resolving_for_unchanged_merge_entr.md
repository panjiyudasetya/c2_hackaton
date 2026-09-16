---
id: github:teqplay/vesselvoyage-backend:pr:859
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 859
title: Fix driftingPending never resolving for unchanged merge entries
author: Darius-Wattimena
state: closed
date: '2026-08-19'
merged_at: '2026-08-24'
base_branch: develop
head_branch: fix/drifting-pending-unchanged-entries
url: https://github.com/teqplay/vesselvoyage-backend/pull/859
labels: []
linked_issues: []
explicit_links: []
---
# PR #859: Fix driftingPending never resolving for unchanged merge entries

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/859  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `fix/drifting-pending-unchanged-entries`  
**Created:** 2026-08-19  
**Merged:** 2026-08-24  

## Description

## Problem

`ShipChangeStatistics.driftingPending` stays `true` forever for entries a revents merge-back reproduced identically.

`recordMerge` registered **every** recalculated entry as pending post-processing, but [a833cb2d](https://github.com/teqplay/vesselvoyage-backend/commit/a833cb2d) (TCC-1121) stopped *scheduling* post-processing for entries the replay reproduced identically. Those entries never publish an `EndPostProcessingEvent`, and that event is the only thing that ever clears `pendingEntryIds` — there is no sweeper and no timeout — so the document is wedged permanently.

The skip is content-based (`isUnchangedFrom` is whole-document equality modulo `updatedAt`/`regenerated`), so it lands almost exclusively on **voyages**: a `NewVoyage` is a far thinner document than a `NewVisit`, so the replay reproduces it byte-identically far more often.

Observed on scenario `437f3e97`: 19 of 25 ships wedged, and every single stuck `pendingEntryIds` entry a `.VOYAGE`. The ESoFs of those ids were last written months before the merge, confirming the merge never touched them.

## Fix

`recordMerge` is handed `changedNewEntryIds` — the ids actually scheduled a few lines below it — instead of `sortedNewEntryIds`. `unchangedEntryIds` is already fully populated at that point, so the declaration just moves up.

## Two related defects in the same path

While tracing this I found the drifting counts that *did* resolve were also wrong — every resolved ship in the affected scenario showed pure additions (8, 66, 135, 144, 179, 180) with zero `unchanged`, which is not a plausible real diff:

1. **`postProcessed` with `slowMovingPeriods = null`.** Post-processing leaves the list null when it found no drifting at all. The calculator read that null as *"not post-processed yet"*, so one such entry made its whole side unknown. Knownness now keys on `postProcessed`.

2. **The unknown side was flattened to "no drifting"** by `orEmpty()`, and only on the previous side, so every period of the other side read as an addition. Both sides are nullable now, and a window whose drifting cannot be established is skipped with a warning rather than compared against an incomplete other side.

3. **An unchanged entry sits in both `overwritten`** (finalized, with periods) **and `recalculated`** (replayed, without) and never reports back, so after fix 1 its periods would read as `removed`. The calculator now reads the drifting of an entry that will not be post-processed again from the entry it replaced, so it reads as `unchanged`.

## Tests

- `ReventsRecalculationServiceTest` — an unchanged entry is not registered as pending, and is not scheduled. Verified to fail without the fix.
- `ShipChangeStatisticsServiceTest` — drifting resolves when the merge reproduced an entry unchanged and never scheduled it; a window with a never-post-processed entry is left alone rather than counted.
- `ShipChangeStatisticsCalculatorTest` — `postProcessed` with no periods counts as *no drifting* rather than *unknown*; a never-post-processed entry makes its whole side unknown; drifting of an entry that will not be post-processed again comes from the entry it replaced.

Existing fixtures were relying on the old "non-null periods = known" rule, so they now set `postProcessed` explicitly — which is what a stored ESoF actually looks like.

Full suite: 2318 tests, 0 failures. `ktlintCheck` clean.

## Note — existing wedged documents do not self-heal

This stops new merges from wedging, but the 19 documents already in that state need either a re-merge of the scenario or a manual `$unset` of `unresolvedDrifting` plus `driftingPending: false`. Their drifting counts will still reflect defect 2 above, since those were computed by the old code.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Commits

- `34567830` **Darius Wattimena** (2026-08-19): Fix driftingPending never resolving for unchanged merge entries
  A revents merge-back registered every recalculated entry as pending
  post-processing in the per-ship change statistics, but TCC-1121 stopped
  scheduling post-processing for entries the replay reproduced identically.
  Those entries never publish an EndPostProcessingEvent, and that event is
  the only thing that clears pendingEntryIds - there is no sweeper or
  timeout - so driftingPending stayed true forever.
  
  The skip is content-based, so it lands almost exclusively on voyages: a
  NewVoyage is a far thinner document than a NewVisit, so the replay
  reproduces it byte-identically far more often. Observed on a scenario
  where 19 of 25 ships were wedged, every stuck id a .VOYAGE.
  
  recordMerge is now handed changedNewEntryIds - the ids that are actually
  scheduled below it - instead of all of them.
  
  Two related defects in the same path made the drifting counts that did
  resolve wrong:
  
  - An ESoF can be postProcessed with slowMovingPeriods left null when
    post-processing found no drifting at all. The calculator read that null
    as "not post-processed yet", so a single such entry made its whole side
    unknown. Knownness now keys on postProcessed.
  
  - The unknown side was then flattened to "no drifting" with orEmpty() on
    the previous side only, so every period of the other side read as an
    addition. Both sides are now nullable and a window whose drifting
    cannot be established is skipped with a warning instead of compared
    against an incomplete other side.
  
  - An unchanged entry sits in both overwritten (finalized, with periods)
    and recalculated (replayed, without), and never reports back, so its
    periods read as removed. The calculator now reads the drifting of an
    entry that will not be post-processed again from the entry it replaced.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>

## Reviews

### augmentcode[bot] — COMMENTED (2026-08-19)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — APPROVED (2026-08-21)

_No comment._

## Comments

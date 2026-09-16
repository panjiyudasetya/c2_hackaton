---
id: github:teqplay/vesselvoyage-backend:pr:817
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 817
title: Fix port recalculation deleting off-port visits during merge-back
author: TeqJoostD
state: closed
date: '2026-07-12'
merged_at: null
base_branch: develop
head_branch: fix/port-recalc-off-port-visit-deletion
url: https://github.com/teqplay/vesselvoyage-backend/pull/817
labels: []
linked_issues: []
explicit_links: []
---
# PR #817: Fix port recalculation deleting off-port visits during merge-back

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/817  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `fix/port-recalc-off-port-visit-deletion`  
**Created:** 2026-07-12  

## Description

## Problem

Recalculating a port (e.g. `ESALG`) could delete a *different* port's visit from the ship's chain. Reported shape:

- Before: `… ESALG visit → Voyage → SGSIN visit`
- After: `… ESALG visit → Voyage` — the `SGSIN` visit was removed and the preceding voyage was stretched over the gap.

## Root cause

A port-scoped recalculation filters off-port visits out of the regenerated data and passes a port-scoped `shouldDeleteExistingEntry` to the merge. That predicate — and the carry-forward that preserves off-port visits — is **only honoured when `deleteExisting = true`**.

`processShipIdForMergingV2` passed `mergeEntry.deleteExisting` straight through from revents. When revents sent `false`, the port scoping was silently ignored: the plain merge treated the ship's off-port visits (e.g. `SGSIN`) as replaceable, deleted the ones the regenerated data didn't reproduce, and collapsed the surrounding voyages over them.

## Fix

Force `deleteExisting` on for port recalculations:

```kotlin
val deleteExisting = mergeEntry.deleteExisting || requestedPortAreaId != null
```

This reuses the existing, well-tested carry-forward path: only visits *in the recalculated port* are replaced, and every other visit is carried forward. Consistent with the existing "port scenario should remove off-port visits [from the regenerated set] but preserve surrounding voyages" tests. The "skip when nothing to merge" early-return is intentionally left keyed on the original flag to keep the change tight.

## Tests

- **`merge keeps off-port visits beyond the regenerated data during a port recalculation`** (`EntriesMergeV2ServiceTest`) — merge-level contract test on the exact `V0 → ESALG → V1 → SGSIN → V2` shape; asserts `SGSIN`/`V2` survive, `SGSIN` stays linked, and no voyage is stitched across it.
- **`port recalculation merges with deleteExisting so off-port entries are carried forward`** (`ReventsRecalculationServiceTest`) — regression guard: drives a port scenario through `checkScenarioProgress` and asserts the merge runs with `deleteExisting=true`. Verified to fail without the fix.

Full merge (base + V2) and recalculation suites pass.

## Follow-up (out of scope)

If revents ever emits a departing voyage that itself *spans across* an off-port visit's time (rather than stopping at it), that's a separate, murkier case this change does not address — it depends on whether a port-scoped recalc should overwrite off-port time at all.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Commits

- `0fb562f2` **TeqJoostD** (2026-07-12): Fix port recalculation deleting off-port visits during merge-back
  A port-scoped recalculation filters off-port visits out of the
  regenerated data and supplies a port-scoped shouldDeleteExistingEntry,
  but that predicate (and the carry-forward that preserves off-port
  visits) is only honoured by the merge when deleteExisting is true.
  processShipIdForMergingV2 passed mergeEntry.deleteExisting straight
  through, so when revents sent false the port scoping was silently
  ignored: the plain merge treated the ship's off-port visits as
  replaceable, deleted them, and collapsed the surrounding voyages over
  the gap (e.g. "ESALG -> Voyage -> SGSIN" became "ESALG -> Voyage").
  
  Force deleteExisting on for port recalculations so only visits in the
  recalculated port are replaced while other visits are carried forward.
  
  Adds a merge-level contract test and an orchestration regression test
  asserting a port recalc merges with deleteExisting=true.
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
- `06343a6e` **TeqJoostD** (2026-07-13): Merge remote-tracking branch 'origin/develop' into fix/port-recalc-off-port-visit-deletion
- `2efb4a14` **TeqJoostD** (2026-07-14): Merge remote-tracking branch 'origin/develop' into fix/port-recalc-off-port-visit-deletion
- `762b88a8` **TeqJoostD** (2026-07-14): Fix compile: use ReventsReplayMergeService.buildMergeEntries in regression test
  develop replaced reventsMergingV2Client.fetchEntriesForMergingByShipId
  with reventsReplayMergeService.buildMergeEntries; update the port-recalc
  regression test's mock accordingly.
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>

## Reviews

### augmentcode[bot] — COMMENTED (2026-07-12)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

## Comments

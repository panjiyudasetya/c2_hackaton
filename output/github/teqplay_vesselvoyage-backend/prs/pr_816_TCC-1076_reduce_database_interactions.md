---
id: github:teqplay/vesselvoyage-backend:pr:816
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 816
title: TCC-1076 reduce database interactions
author: Darius-Wattimena
state: closed
date: '2026-07-10'
merged_at: '2026-07-13'
base_branch: develop
head_branch: TCC-1076-unneeded-lookup-on-publishing
url: https://github.com/teqplay/vesselvoyage-backend/pull/816
labels: []
linked_issues: []
explicit_links: []
---
# PR #816: TCC-1076 reduce database interactions

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/816  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-1076-unneeded-lookup-on-publishing`  
**Created:** 2026-07-10  
**Merged:** 2026-07-13  

## Description

## Why

Profiling the processing deployment showed two unnecessary sources of steady-state database load:

1. **Publishing changes re-fetched state we already hold in memory.** `ChangesPublisherService` did up to 3 database lookups per published visit change (entry fallback lookup, and the previous voyage lookup inside the PTO SOF view), even though those documents were already present in the ship status or in the change set being published.
2. **Every AIS batch rewrote the full trace document.** `ProcessingTraceService` used a full-document replace per update, resending the unbounded `simplifiedPolyline` (the largest field, which only changes once per 100 trace items) on every write. Since a replace also puts the entire document in the oplog, this was amplified across replication.

## What

- `ChangesPublisherService` now collects the entries/ESoFs already in memory (ship statuses + change set) once per publish and resolves from those maps, only falling back to the database when an entry is genuinely not held (e.g. post-processing an aged-out entry). This also removes a wasted fallback lookup whose result was never used when the change set already contained the entry.
- `EsofV2Service.produce` accepts an optional `knownPreviousVoyage` so the PTO view no longer fetches the previous voyage the publisher already holds. Existing API callers are unaffected (parameter defaults to the old fetch behaviour, guarded by an entry-ID match).
- `NewTraceDataSource.updateOngoingTraceFields` performs a partial `$set` of only the fields that change while appending to an ongoing trace. The full replace now only happens on the 1-in-100 simplification pass where `simplifiedPolyline` actually changes.

## Impact

- Steady state: ~2-3 fewer reads per published visit change; trace update writes (and their oplog entries) shrink from the full document to a few hundred bytes of changed fields.
- Publish output is unchanged — the existing `ChangesPublisherServiceTest` cases pass without any expectation changes.


## Commits

- `f0d07982` **Darius Wattimena** (2026-07-10): Remove unneeded database lookup when publishing changes
- `64d05dc0` **Darius Wattimena** (2026-07-10): Reduce amount of database interaction when updating traces
- `47cd1252` **Darius Wattimena** (2026-07-13): Improve code documentation based on review feedback
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `cab74ab6` **Darius Wattimena** (2026-07-13): Update comment to make sense

## Reviews

### augmentcode[bot] — COMMENTED (2026-07-10)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — COMMENTED (2026-07-13)

_No comment._

### TeqJoostD — COMMENTED (2026-07-13)

_No comment._

### TeqJoostD — COMMENTED (2026-07-13)

_No comment._

### TeqJoostD — DISMISSED (2026-07-13)

_No comment._

### Darius-Wattimena — COMMENTED (2026-07-13)

_No comment._

### Darius-Wattimena — COMMENTED (2026-07-13)

_No comment._

### TeqJoostD — APPROVED (2026-07-13)

_No comment._

## Review Comments

### TeqJoostD — 2026-07-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewTraceDataSource.kt`

Great addition!

### TeqJoostD — 2026-07-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/EsofV2Service.kt`

@param next time please...

### TeqJoostD — 2026-07-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/publisher/ChangesPublisherService.kt`

Please write the comment in English next time

### Darius-Wattimena — 2026-07-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/EsofV2Service.kt`

Fixed — rewrote the KDoc in @param form.

### Darius-Wattimena — 2026-07-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/publisher/ChangesPublisherService.kt`

Fixed — rephrased the comment.

## Comments

### TeqJoostD — 2026-07-13

Please provide a description next time. Reduce database interactions? why?

### Darius-Wattimena — 2026-07-13

Added a description to the PR explaining the why and the impact.

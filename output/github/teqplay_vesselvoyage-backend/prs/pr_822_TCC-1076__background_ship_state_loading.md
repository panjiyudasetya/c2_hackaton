---
id: github:teqplay/vesselvoyage-backend:pr:822
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 822
title: 'TCC-1076: background ship state loading'
author: Darius-Wattimena
state: closed
date: '2026-07-20'
merged_at: '2026-07-21'
base_branch: develop
head_branch: TCC-1076-background-ship-state-loading
url: https://github.com/teqplay/vesselvoyage-backend/pull/822
labels: []
linked_issues: []
explicit_links:
- jira:TCC-1076
---
# PR #822: TCC-1076: background ship state loading

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/822  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-1076-background-ship-state-loading`  
**Created:** 2026-07-20  
**Merged:** 2026-07-21  

## Description

Follow-up to #821. Startup stays fast and lazy, but processing was slow to catch up on the event queues afterwards because every ship status had to be lazily loaded on first touch.

- After the consumers start, `ProcessingShipStatusService.preloadShipStatuses()` warms the in-memory cache in the background, **most recently updated ships first** (new `findAllOrderedByLastUpdated`, uses the existing `lastUpdatedAt` index), in batches of 1000 via the snapshot/bulk-query path.
- Safe alongside live processing: each insert happens under the existing `ShipLockService` ship lock (the same lock all live mutation paths hold), a ship already loaded or updated by live processing always wins, ships with stale identifiers are skipped (left to lazy loading, no brute force, no DB writes), and a ship removed mid-preload is tombstoned so it can't be resurrected.
- Runs at most once, yields between batches, holds the lock only for the in-memory insert, and stops on shutdown.

Note: once the preload completes, all ship statuses are in memory again (same footprint as before the lazy-loading change).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Commits

- `40ccf831` **Darius Wattimena** (2026-07-20): TCC-1076: preload ship statuses in the background after startup
  Startup stays fast and lazy, but processing now warms the in-memory ship
  status cache in the background once consumers have started, most recently
  updated ships first, so event consumption catches up quickly. The preload
  is read-only and purely additive: ships already loaded by live processing
  are never overwritten, ships with stale identifiers are left to the lazy
  loading path, and removals during the preload are never resurrected.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `b8de86a4` **Darius Wattimena** (2026-07-20): TCC-1076: insert preloaded ship statuses under the ship lock
  Use the existing striped ShipLockService for each preload insert, the same
  lock every live mutation path (event processing, AIS consumer, recalculations)
  already holds. This serializes the insert with removals, so the tombstone
  check and insert are now atomic and the undo branch is no longer needed.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `2ce57e9e` **Darius Wattimena** (2026-07-20): Log more times when loading in ship states
- `91604625` **Darius Wattimena** (2026-07-20): Code cleanup
- `223cbe4b` **Darius Wattimena** (2026-07-20): TCC-1076: run infra cache loads on the IO dispatcher
  The initial infra cache loads are blocking work (disk reads and HTTP calls
  to Poma) but ran on the caller's dispatcher, which is Dispatchers.Default
  in ApiStartUpService. Dispatch them on Dispatchers.IO so startup doesn't
  starve the Default pool.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `51479894` **Darius Wattimena** (2026-07-20): TCC-1076: split bulkLoadShipStatuses to reduce cognitive complexity
  Extract the snapshot hydration and entry assembly paths into their own
  methods, and drop the redundant isEmpty guards around findByIds calls
  (an empty id set already results in zero queries).
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `b25b1ad4` **Darius Wattimena** (2026-07-20): TCC-1076: unify lazy single-ship loading with the bulk assembly path
  The old per-entry loading in ShipStatusService (findById plus a separate
  ESoF lookup per entry, up to ~7 sequential queries) duplicated the assembly
  logic of the bulk loader. Move collectEntryIdsFromIdentifiers and
  assembleShipStatus into the base class and let the lazy single-ship load
  use the same batched lookups (state + 3 IN-queries at most). This also
  speeds up the API profile, which loads statuses through the same path.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>

## Reviews

### Jamie-de-Leest — APPROVED (2026-07-21)

_No comment._

## Comments

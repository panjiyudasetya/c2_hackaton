---
id: github:teqplay/vesselvoyage-backend:pr:845
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 845
title: TCC-1158 Upsert instead of insert new normalized documents
author: Darius-Wattimena
state: closed
date: '2026-08-06'
merged_at: '2026-08-06'
base_branch: develop
head_branch: TCC-1158
url: https://github.com/teqplay/vesselvoyage-backend/pull/845
labels: []
linked_issues: []
explicit_links:
- jira:TCC-1158
---
# PR #845: TCC-1158 Upsert instead of insert new normalized documents

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/845  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-1158`  
**Created:** 2026-08-06  
**Merged:** 2026-08-06  

## Description

## Problem

Repair story / full story recalculations fail with an E11000 duplicate key error when leftover normalized documents (e.g. encounters) are still in the database:

```
E11000 duplicate key error collection: vesselvoyage.encountersV2 index: _id_ dup key: { _id: "...VISIT:..." }
```

Normalized child documents have deterministic IDs (`"{entryId}:{startEventId}"` for encounters), so a recalculation regenerates exactly the same IDs. `buildDiffWriteModels` emitted an `InsertOneModel` for any document not in its comparison baseline — a stale leftover (e.g. orphaned by an earlier partial write, and missed by cleanup because it isn't referenced in the parent `NormalizedESoF`'s ID lists) then failed the whole entry's bulk write. Since `persistChanges` swallows the exception, the recalculation carried on with a half-written story.

## Fix

Write new documents as upserting replaces (`ReplaceOneModel` with `upsert(true)`) instead of inserts. Because the IDs are deterministic, this doesn't just tolerate a leftover — it overwrites it with the freshly calculated version, so recalculations self-heal corrupted state instead of getting stuck.

This covers all five normalized child collections (encounters, slow moving periods, STS transfers, area activities, stops) since they share `buildDiffWriteModels`.

## Testing

- Updated `NormalizedDiffUtilsTest` and `NormalizedEncounterDataSourceTest` to assert the upsert behaviour
- Full root-module test suite and ktlint pass

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Commits

- `6e915833` **Darius Wattimena** (2026-08-06): TCC-1158 Upsert instead of insert new normalized documents
  A recalculation (repair story / full story recreate) regenerates the
  same deterministic document ids (e.g. "{entryId}:{startEventId}" for
  encounters). When a leftover document from an earlier partial write or
  failed cleanup is still present, the diff-based save built an
  InsertOneModel for it, failing the whole entry with an E11000 duplicate
  key error.
  
  Writing new documents as upserting replaces instead makes the write
  idempotent: a stale leftover is simply overwritten with the freshly
  calculated version, so recalculations self-heal instead of getting
  stuck. This covers all normalized child collections (encounters, slow
  moving periods, STS transfers, area activities and stops) since they
  share buildDiffWriteModels.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>

## Reviews

### augmentcode[bot] — COMMENTED (2026-08-06)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — APPROVED (2026-08-06)

_No comment._

## Comments

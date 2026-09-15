---
id: github:teqplay/vesselvoyage-backend:pr:836
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 836
title: TCC-1153 Expose the encounter id in the ship encounter API
author: Darius-Wattimena
state: closed
date: '2026-07-31'
merged_at: '2026-07-31'
base_branch: develop
head_branch: claude/encounter-api-ship-id-524529
url: https://github.com/teqplay/vesselvoyage-backend/pull/836
labels: []
linked_issues: []
explicit_links: []
---
# PR #836: TCC-1153 Expose the encounter id in the ship encounter API

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/836  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `claude/encounter-api-ship-id-524529`  
**Created:** 2026-07-31  
**Merged:** 2026-07-31  

## Description

## Summary

`/v2/encounter/byShipId/{shipId}` (and the `byImo` / `byMmsi` variants, which share the response model) now return an `id` for every encounter, so consumers can reference a specific encounter.

- `ShipEncounterEntry` gets a required `id: String` field.
- Populated from `NormalizedEncounter._id`, i.e. `"{entryId}:{startEventId}"`.

## Testing

- `./gradlew :test --tests "*EncounterV2*"` — passes (assertions added for the new field in both `EncounterV2ServiceTest` and `ApiEncounterV2ControllerTest`).
- `./gradlew ktlintCheck` — passes.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Commits

- `b1ead8b7` **Darius Wattimena** (2026-07-31): TCC-1153 Expose the encounter id in the ship encounter API
  Add a required `id` field to `ShipEncounterEntry`, populated from the
  normalized encounter's `_id` ("{entryId}:{startEventId}"), so consumers of
  /v2/encounter/byShipId, /byImo and /byMmsi can reference a specific encounter.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>

## Reviews

### augmentcode[bot] — COMMENTED (2026-07-31)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — APPROVED (2026-07-31)

_No comment._

## Comments

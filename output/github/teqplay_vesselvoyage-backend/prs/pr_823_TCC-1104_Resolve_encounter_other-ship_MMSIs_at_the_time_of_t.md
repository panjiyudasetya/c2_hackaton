---
id: github:teqplay/vesselvoyage-backend:pr:823
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 823
title: TCC-1104 Resolve encounter other-ship MMSIs at the time of the encounter
author: Darius-Wattimena
state: closed
date: '2026-07-20'
merged_at: '2026-07-21'
base_branch: develop
head_branch: TCC-1104-encounter-imo-mmsi-matching
url: https://github.com/teqplay/vesselvoyage-backend/pull/823
labels: []
linked_issues: []
explicit_links:
- jira:TCC-1104
---
# PR #823: TCC-1104 Resolve encounter other-ship MMSIs at the time of the encounter

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/823  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-1104-encounter-imo-mmsi-matching`  
**Created:** 2026-07-20  
**Merged:** 2026-07-21  

## Description

## Problem

Encounters store the other ship's MMSI (and sometimes IMO), but MMSIs get reassigned between ships over time. The other-ship lookup in the encounter API only used the current-MMSI snapshot from the ship register, so encounters referencing a historical MMSI failed to resolve the other ship entirely — no `shipId`/`name` in the API output. On top of that, `EncounterV2Service` didn't use the stored `otherImo` for the details lookup at all.

The time-ranged IMO-MMSI mapping from CSI was already loaded into the ship cache, but only keyed by IMO — there was no reverse MMSI→IMO-at-time lookup.

## Changes

- **`ShipCacheService`**: build a reverse MMSI → (IMO, period) index while loading the CSI IMO-MMSI mapping, and add a time-aware `getImoByMmsi(mmsi, time)`. When two ships' mapping periods overlap, the most recently started mapping wins.
- **`StaticShipInfoService`**: new time-aware overloads `getImoFromMmsi(mmsi, time)` and `getShipDetailsByMMSI(mmsi, time)`, falling back to the current-snapshot behaviour when no mapping covers the time.
- **`EncounterV2Service`**: resolve the other ship by its IMO first (matching the SoF generators' pattern), otherwise by its MMSI at the encounter start time.
- **Pto/PortReporter Statement of Facts generators**: the final MMSI fallback now also resolves at the encounter start time.

No backfill needed: encounters stored with a null `otherImo` stay MMSI-only in Mongo but now resolve correctly at read time.

## Tests

- Reverse lookup: historical MMSI resolves within its window, misses outside it, overlap tie-break, mappings for unregistered ships ignored.
- Service overloads: reassigned MMSI resolves at the time it was used, snapshot fallback, and a case proving the plain lookup fails where the time-aware one succeeds.
- Encounter API: other ship resolved by `otherImo` when present, otherwise by MMSI at encounter start time.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Commits

- `5ab83887` **Darius Wattimena** (2026-07-20): TCC-1104 Resolve encounter other-ship MMSIs at the time of the encounter
  Encounters store the other ship's MMSI, but MMSIs get reassigned between
  ships over time. The lookup only used the current-MMSI snapshot from the
  ship register, so encounters with a historical MMSI (and API output for
  them) failed to resolve the other ship entirely.
  
  - Build a reverse MMSI -> (IMO, period) index from the CSI IMO-MMSI
    mapping and add time-aware getImoByMmsi/getShipDetailsByMMSI lookups,
    falling back to the current snapshot when no mapping covers the time
  - Resolve the other ship in the encounter API by its IMO first and
    otherwise by its MMSI at the encounter start time
  - Use the time-aware lookup for the MMSI fallback in both Statement of
    Facts generators
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>

## Reviews

### augmentcode[bot] — COMMENTED (2026-07-20)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F823%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### Jamie-de-Leest — APPROVED (2026-07-21)

_No comment._

## Review Comments

## Comments

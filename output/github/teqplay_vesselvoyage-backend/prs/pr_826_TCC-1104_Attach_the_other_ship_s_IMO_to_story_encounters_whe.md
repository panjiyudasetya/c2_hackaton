---
id: github:teqplay/vesselvoyage-backend:pr:826
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 826
title: TCC-1104 Attach the other ship's IMO to story encounters when known
author: Darius-Wattimena
state: closed
date: '2026-07-21'
merged_at: '2026-07-23'
base_branch: develop
head_branch: TCC-1104-story-encounter-imo
url: https://github.com/teqplay/vesselvoyage-backend/pull/826
labels: []
linked_issues: []
explicit_links: []
---
# PR #826: TCC-1104 Attach the other ship's IMO to story encounters when known

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/826  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-1104-story-encounter-imo`  
**Created:** 2026-07-21  
**Merged:** 2026-07-23  

## Description

## Problem

Follow-up to #823. Endpoints serving stored ESoF data (story, entry/visit/voyage, Statement of Facts) returned encounters as-is. Encounters captured without an IMO therefore surface with a null `otherImo`, and since consumers resolve ships by the identifiers they receive, such encounters resolve to the wrong ship (or none at all) once the MMSI has been reassigned to another vessel.

## Changes

**Centralized ESoF enrichment (read side).** A new `EsofEnrichmentService` attaches the other ship's IMO to encounters and ship-to-ship transfers that don't carry one, by resolving the MMSI **at the time of the encounter** through the time-aware IMO-MMSI mapping introduced in #823 (with its current-snapshot fallback). It is applied centrally in `EsofV2Service` — `findById`, `findAllById` and `produce` — so every outward-facing consumer gets complete data automatically: the entry/visit/voyage/esof/SoF/paginated API controllers, the frontend view, filtered journeys, outgoing SoF messages, and the story endpoints. Dry-run stories enrich their in-memory ESoFs with the same service.

- Encounters that already carry an IMO are left untouched (no lookup performed); unresolvable MMSIs stay null.
- `EsofV2Service` is now strictly the read side (documented on the class): **post-processing**, which reads ESoFs and persists them back, now reads the raw stored ESoF through `EsofV2DataSource` directly — like the revents/manual recalculation flows already do — so derived IMO values never reach the database. `findAllNonPostProcessed` moved to the datasource accordingly.

**Why not enrich in the datasource?** Recalculation flows read ESoFs via `EsofV2DataSource` and persist them back via `bulkWriteChanges`; enriching there would bake possibly outdated mapping resolutions into `encountersV2`, and the encounter merge/dedupe logic in `esofUtils` assumes stored field values. The service/datasource split keeps the line explicit: enriched read-only projections above, raw stored data below.

**Time-aware ship resolution endpoint.** `POST /v1/ships/static/mmsis` now accepts an optional `time` query parameter. Without it the behaviour is unchanged (current MMSI); with it, MMSIs are resolved at that moment via the historical mapping. Used by the frontend to resolve encounter counterpart ships at the encounter start time (see teqplay/vesselvoyage#129).

## Tests

- `EsofV2ServiceTest`: `findById`/`findAllById`/`produce` return/pass enriched ESoFs.
- `EsofEnrichmentServiceTest`: IMO attached from mapping at encounter time, stored IMO untouched and not re-resolved, unresolvable MMSI stays null, `MISSING_IMO` placeholder filtered, STS transfer enrichment.
- `StoryServiceTest`: dry-run ESoFs are enriched.
- `PostProcessingServiceTest` rewired to the raw datasource; full test suite passes.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Commits

- `44d48d26` **Darius Wattimena** (2026-07-21): TCC-1104 Attach the other ship's IMO to story encounters when known
  The story endpoint serialized stored encounters as-is, so encounters
  captured without an IMO surfaced with a null otherImo. The frontend
  resolves ships by their identifiers, meaning such encounters resolved to
  the wrong ship (or none) once the MMSI was reassigned.
  
  Enrich the ESoF in the story read path: when an encounter or
  ship-to-ship transfer has no otherImo, resolve the MMSI at the time of
  the encounter through the time-aware IMO-MMSI mapping introduced for
  TCC-1104. Stored data is left untouched, so newly resolved mapping
  tickets are picked up automatically.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `bf412a70` **Darius Wattimena** (2026-07-21): TCC-1104 Extract ESoF encounter IMO enrichment into a reusable service
  Move the other-ship IMO resolution out of StoryService into a dedicated
  EsofEnrichmentService so future consumers exposing ESoF data outward can
  reuse it with a single call instead of reimplementing the lookup.
  
  The enrichment deliberately stays out of the EsofV2DataSource read path:
  recalculation flows (revents, manual recalculation, post-processing)
  read ESoFs and persist them back, which would bake derived IMO values
  into the database, and the encounter merge/dedupe logic assumes the
  stored field values. The service documents that enriched models must
  only be used for read-only projections.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `9363ecc2` **Darius Wattimena** (2026-07-21): TCC-1104 Support resolving MMSIs at a point in time in the static ships endpoint
  /v1/ships/static/mmsis resolved MMSIs only against the ships currently
  using them. Add an optional 'time' query parameter so consumers passing
  historical MMSIs (e.g. from encounters) get the ship that was using the
  MMSI at that moment, based on the time-aware IMO-MMSI mapping.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `1a8f3c43` **Darius Wattimena** (2026-07-21): TCC-1104 Enrich all outward-facing ESoF reads with resolved other-ship IMOs
  Centralize the encounter IMO enrichment in EsofV2Service instead of
  applying it per consumer: findById, findAllById and produce now return
  ESoFs enriched by EsofEnrichmentService, so every public endpoint (entry
  /visit/voyage/esof/SoF/paginated controllers), the frontend view,
  journeys and outgoing SoF messages expose complete data automatically.
  
  EsofV2Service is now strictly the read side: post-processing, which
  reads ESoFs and persists them back, reads the raw stored ESoF through
  EsofV2DataSource directly, like the other recalculation flows already
  do. findAllNonPostProcessed moves with it. This keeps derived IMO
  values out of the database.
  
  StoryService no longer enriches stored ESoFs itself (it gets them
  enriched from EsofV2Service) and only enriches the in-memory dry-run
  ESoFs that never pass through that read path.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `0414abbc` **Darius Wattimena** (2026-07-21): TCC-1104 Treat the missing-imo placeholder as unresolved during enrichment
  Stored encounters may carry MISSING_IMO (0) instead of null when the
  IMO is unknown. The enrichment now resolves the MMSI at the encounter
  time in both cases, so consumers never receive the unusable placeholder.
  
  Addresses PR review feedback.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>

## Reviews

### augmentcode[bot] — COMMENTED (2026-07-21)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F826%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — APPROVED (2026-07-22)

_No comment._

## Review Comments

## Comments

### Darius-Wattimena — 2026-07-21

Applied review feedback in 0414abbc: the enrichment now treats `MISSING_IMO` (0) the same as `null` — both resolve the MMSI at the encounter time — so the unusable placeholder never reaches consumers. Added a test covering a stored `otherImo = 0` being re-resolved.

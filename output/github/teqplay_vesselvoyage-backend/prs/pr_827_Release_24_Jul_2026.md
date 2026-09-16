---
id: github:teqplay/vesselvoyage-backend:pr:827
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 827
title: Release 24 Jul 2026
author: Darius-Wattimena
state: closed
date: '2026-07-24'
merged_at: '2026-07-24'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/827
labels: []
linked_issues: []
explicit_links: []
---
# PR #827: Release 24 Jul 2026

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/827  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2026-07-24  
**Merged:** 2026-07-24  

## Description

_No description._

## Commits

- `b5d75c5f` **damon02** (2026-07-14): TCC-1102: resolve pomaEntities on the /v2/journey/{imo} endpoint
  The journey endpoint returned raw poma IDs; resolve the departure/arrival
  portIds into full Poma entities grouped by infra area type, mirroring the
  way ShipStory exposes its pomaEntities. Conversion Port -> PomaEntity goes
  through a new MapStruct PomaEntityMapper per the repo mapper convention.
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
- `626b2a23` **damon02** (2026-07-14): TCC-1102: expose pomaEntities via internal-only processing endpoint
  Per review feedback: the shared Journey model must not change for all
  journey endpoints. Reverts the Journey/PomaEntity API-model changes and
  instead wraps the untouched Journey in an internal-only InternalJourney
  (journey + pomaEntities as raw PomaModel grouped by internal
  InfraAreaType, like ShipStory), served by a new processing-profile-only
  ProcessingJourneyController at /v2/journey/internal/imo/{imo}, modeled
  on ProcessingStoryController.
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
- `d15e693f` **Damon Asberg** (2026-07-16): Merge pull request #820 from teqplay/feature/TCC-1102
  TCC-1102: resolve pomaEntities on the /v2/journey/{imo} endpoint
- `8164ddf4` **Darius Wattimena** (2026-07-17): Adjust VesselVoyage startup to do full lazy loading of all ships
- `1a5e8407` **Darius Wattimena** (2026-07-17): Adjust CSI loading to be faster
- `4399f9da` **Darius Wattimena** (2026-07-17): Add support gzip responses to make csi and poma loading even faster
- `40ccf831` **Darius Wattimena** (2026-07-20): TCC-1076: preload ship statuses in the background after startup
  Startup stays fast and lazy, but processing now warms the in-memory ship
  status cache in the background once consumers have started, most recently
  updated ships first, so event consumption catches up quickly. The preload
  is read-only and purely additive: ships already loaded by live processing
  are never overwritten, ships with stale identifiers are left to the lazy
  loading path, and removals during the preload are never resurrected.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `972443df` **Darius Wattimena** (2026-07-20): Merge pull request #821 from teqplay/TCC-1076-start-up
  TCC-1076 start up improvements
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
- `0221c3ca` **Darius Wattimena** (2026-07-21): Merge pull request #822 from teqplay/TCC-1076-background-ship-state-loading
  TCC-1076: background ship state loading
- `dc0e873c` **Darius Wattimena** (2026-07-21): Merge pull request #823 from teqplay/TCC-1104-encounter-imo-mmsi-matching
  TCC-1104 Resolve encounter other-ship MMSIs at the time of the encounter
- `0d52bea2` **Darius Wattimena** (2026-07-21): Use globalObjectMapper in slackError to support Instant serialization
  The bare jacksonObjectMapper() lacked the JSR-310 module, so serializing
  the event's actualTime threw InvalidDefinitionException and the whole
  message was dropped during event processing.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `74c51741` **Darius Wattimena** (2026-07-21): Drain AIS lane queues on shutdown before Mongo closes
  Messages routed to a lane are acked immediately, but on shutdown the
  lane workers kept flushing to Mongo while Spring destroyed the Mongo
  client, failing with MongoServerUnavailableException and losing the
  already-acked in-flight items (up to 1000).
  
  RabbitMqConsumersService.shutdown() now closes the channels first (no
  new deliveries) and then drains the lane queues while Mongo is still
  open, bounded by a 30s timeout. Late deliveries during shutdown are
  dropped instead of blocking on lanes no longer being drained.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
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
- `d6dc5bab` **Darius Wattimena** (2026-07-21): Address review feedback on shutdown drain
  - Split drainLane into awaitNextBatch and flushBatchLogged to reduce
    cognitive complexity
  - Propagate InterruptedException out of the flush catch blocks so a
    forced shutdown (shutdownNow) can stop lane workers promptly
  - Handle InterruptedException from awaitTermination so the forced-stop
    path still runs
  - Run the lane drain in a finally block so a failure while closing a
    consumer can't skip it
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `9256bd45` **Darius Wattimena** (2026-07-21): Make the berth-end Slack notification best-effort
  Review feedback: serialization or Slack failures in slackError could
  still bubble up and drop the message being processed. Wrap the whole
  notification in a try/catch and log a warning instead.
  
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
- `627d60df` **Darius Wattimena** (2026-07-23): Merge pull request #824 from teqplay/fix/slack-error-jackson-instant
  Use globalObjectMapper in slackError to support Instant serialization
- `b478b2ee` **Darius Wattimena** (2026-07-23): Merge pull request #825 from teqplay/fix/shutdown-drain-ais-lanes
  Drain AIS lane queues on shutdown before Mongo closes
- `e31b9a60` **Darius Wattimena** (2026-07-23): Merge pull request #826 from teqplay/TCC-1104-story-encounter-imo
  TCC-1104 Attach the other ship's IMO to story encounters when known

## Reviews

### augmentcode[bot] — COMMENTED (2026-07-24)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### augmentcode[bot] — COMMENTED (2026-07-24)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F827%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### augmentcode[bot] — COMMENTED (2026-07-24)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F827%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — APPROVED (2026-07-24)

_No comment._

## Review Comments

## Comments

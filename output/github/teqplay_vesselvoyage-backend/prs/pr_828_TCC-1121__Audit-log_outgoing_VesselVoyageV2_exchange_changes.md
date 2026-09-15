---
id: github:teqplay/vesselvoyage-backend:pr:828
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 828
title: 'TCC-1121: Audit-log outgoing VesselVoyageV2 exchange changes behind a flag'
author: TeqJoostD
state: closed
date: '2026-07-28'
merged_at: '2026-08-04'
base_branch: develop
head_branch: TCC-1121
url: https://github.com/teqplay/vesselvoyage-backend/pull/828
labels: []
linked_issues: []
explicit_links: []
---
# PR #828: TCC-1121: Audit-log outgoing VesselVoyageV2 exchange changes behind a flag

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/828  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-1121`  
**Created:** 2026-07-28  
**Merged:** 2026-08-04  

## Description

## Why

We suspect some recalculated (revents) visits/voyages don't put their PTO updates on the `VesselVoyageV2` exchange, but we have no record of what actually went out. This adds an opt-in audit trail so we can diff "what a scenario should have emitted" against "what was actually published" and pinpoint the gaps.

## What

When `event-publishing.outgoing-change-log.enabled=true`, every change published to the exchange is also written to a new `outgoingChangeLog` Mongo collection. Each record holds:

| field | meaning |
|---|---|
| `scenarioId` | recalculation scenario the change came from (`null` for live processing) |
| `queuedAt` | when the change was put on the exchange |
| `change` | the change itself, serialized exactly as published |
| `exchange`, `routingKey` | where/how it went out (e.g. `SOFVIEW.PTO.FINAL.UPDATE.<imo>`) |

Collection is compound-indexed on `(scenarioId, queuedAt)` for "what did scenario X emit, in order" lookups.

## How

- Logging lives in `RabbitMqOutgoingChangeSender.send` — the single choke point every published event passes through, and the one place with the serialized bytes. It logs the exact payload right after the send, and is **best-effort**: a logging failure is caught and never blocks or fails the real publish.
- The scenario is carried via `ScenarioLoggingContext`, a thread-bound (MDC-style) ambient value. The revents merge (`persistMergeResultV2`) and post-processing (`runPostProcessingTasks`) wrap their publish in `withScenarioId(scenarioId) { … }`; the sender reads `currentScenarioId()` when writing the audit record. Publishing is synchronous on the same thread, so the tag is accurate, and the context is always cleared via `try/finally` so it never leaks across the post-processing thread pool.
- **Why not thread a `scenarioId` param through `persistAndPublish` → `tryPublishNewChanges` → `send`?** That was the first approach, but adding a defaulted param to those widely-verified methods broke 45 existing tests on Mockito argument-matcher counting. The ambient context keeps the publish APIs unchanged, so all prior tests pass untouched.

## Flag

Off by default (`event-publishing.outgoing-change-log.enabled=false`). Intended to be switched on while investigating missing events, then off again — it writes one Mongo doc per published event, so it's high-volume on a busy live instance and not meant to run permanently.

## Notes for reviewers

- It captures **every** event on the exchange (entries + SOF, live + recalculated), not just PTO — most useful for "what did we miss." Easy to scope to scenario-driven events only if preferred.
- `change` is stored as the published JSON string rather than a typed/parsed document, to avoid Mongo codec issues with the sealed `OutgoingChange` hierarchy and to capture the exact bytes sent.

## Testing

- `RabbitMqOutgoingChangeSenderTest` (5 cases): always publishes; flag off → no log; flag on → logs all fields; live change (no context) → null scenario; logging failure doesn't break the publish.
- `ScenarioLoggingContextTest`: default null, set/clear, nesting restore, and clears on throw.
- Full `./gradlew :test` (2157 tests) and `ktlint` green.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Commits

- `c7d72d28` **TeqJoostD** (2026-07-28): TCC-1121: audit-log outgoing VesselVoyageV2 exchange changes behind a flag
  Adds an opt-in audit trail of every change published to the VesselVoyageV2
  exchange, so we can find out which events actually went out (e.g. PTO updates
  a recalculation should have produced but didn't).
  
  Each record captures the originating scenario id (null for live processing),
  when the change was queued, the exchange + routing key, and the change itself
  serialized exactly as published. Written to the new `outgoingChangeLog`
  collection only when `event-publishing.outgoing-change-log.enabled` is true.
  
  Logging happens in RabbitMqOutgoingChangeSender (the single publish choke
  point) and is best-effort: a logging failure never blocks or fails the actual
  publish. scenarioId is threaded from the revents merge and post-processing
  paths through persistAndPublish -> tryPublishNewChanges -> the sender; all new
  params default to null so existing callers are unaffected.
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
- `f31ddc77` **TeqJoostD** (2026-07-28): TCC-1121: carry scenarioId via ambient context instead of publish params
  Threading scenarioId through persistAndPublish/tryPublishNewChanges/send added a
  defaulted param to widely-verified methods, which broke 45 existing tests on
  Mockito argument-matcher counting.
  
  Replace it with a thread-bound ScenarioLoggingContext (MDC-style): the revents
  merge and post-processing wrap their publish in withScenarioId(...), and the
  sender reads the current scenario when writing the audit record. Publishing is
  synchronous on the same thread, so the tag is accurate; the context is always
  cleared via try/finally so it never leaks across the post-processing thread pool.
  
  This keeps the publish APIs unchanged (all prior tests pass untouched). Adds
  ScenarioLoggingContextTest for the set/clear/nesting/throw semantics.
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
- `4db009aa` **TeqJoostD** (2026-07-29): Merge branch 'develop' into TCC-1121
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt
- `a8e8c9b4` **TeqJoostD** (2026-07-29): TCC-1121: only audit PTO changes, skip PortReporter and entry changes
  The audit log is only interested in PTO statement-of-facts changes. Filter in
  the sender on the routing-key PTO segment (matches both SOFVIEW.PTO.* and
  BARGE_SOFVIEW.PTO.*), skipping PortReporter (.PORTREPORTER.) and entry
  (VISIT./VOYAGE.) changes. Publishing to the exchange is unaffected.
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
- `52c14aa3` **TeqJoostD** (2026-07-29): TCC-1121: narrow audit log to FINAL PTO and LIVE PTO deletions
  Audit only the routing keys we care about:
    - SOFVIEW.PTO.FINAL.#        (every finalized PTO change)
    - SOFVIEW.PTO.LIVE.DELETE.#  (live PTO deletions only)
  
  Live PTO create/update, PortReporter, entry changes and barge SOF views are
  skipped. Publishing to the exchange is unaffected.
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
- `a8ecc362` **TeqJoostD** (2026-07-29): Merge branch 'develop' into TCC-1121
- `ffa531fd` **TeqJoostD** (2026-08-04): Merge branch 'develop' into TCC-1121
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationService.kt
- `452c835b` **TeqJoostD** (2026-08-04): ktlint

## Reviews

### augmentcode[bot] — COMMENTED (2026-07-28)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F828%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### Darius-Wattimena — DISMISSED (2026-08-04)

_No comment._

### Darius-Wattimena — APPROVED (2026-08-04)

_No comment._

## Review Comments

## Comments

---
id: github:teqplay/vesselvoyage-backend:pr:820
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 820
title: 'TCC-1102: resolve pomaEntities on the /v2/journey/{imo} endpoint'
author: damon02
state: closed
date: '2026-07-14'
merged_at: '2026-07-16'
base_branch: develop
head_branch: feature/TCC-1102
url: https://github.com/teqplay/vesselvoyage-backend/pull/820
labels: []
linked_issues: []
explicit_links: []
---
# PR #820: TCC-1102: resolve pomaEntities on the /v2/journey/{imo} endpoint

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/820  
**State:** closed | **Author:** damon02  
**Base ← Head:** `develop` ← `feature/TCC-1102`  
**Created:** 2026-07-14  
**Merged:** 2026-07-16  

## Description

## What this does

TCC-1102 — the `/v2/journey/{imo}` endpoint returned raw poma IDs that the frontend had to resolve itself.

**Reworked after Darius's review feedback:** the shared `Journey` model is untouched (it serves all journey
endpoints and external consumers). Instead there's a new **internal-only** endpoint on the **processing profile**,
modeled on `ProcessingStoryController`:

- `GET /v2/journey/internal/imo/{imo}` (`ProcessingJourneyController`, `@ProfileProcessing`, `SHIP:READ`) returns
- `InternalJourney` — a wrapper `(journey: Journey, pomaEntities: Map<InfraAreaType, List<PomaModel>>)` exposing the
  resolved Poma entities as **raw internal `PomaModel`s grouped by the internal `InfraAreaType`**, exactly the way
  `ShipStory` exposes its `pomaEntities`.
- `JourneyService` carries `@ProfileApi @ProfileProcessing` so the one service backs both controllers; the public
  endpoints keep returning the plain `Journey`.

The first commit's approach (`pomaEntities` on the shared `Journey` DTO + api-module `PomaEntity`/`PomaInfraAreaType`
models + MapStruct mapper) is fully reverted — those files are deleted and `Journey.kt` is byte-identical to `develop`.

cc @Darius-Wattimena @TeqJoostD @michel-teqplay

---

## Verification

- First commit: `Test & build`, Kover, SonarCloud all green on CI.
- Rework commit `626b2a23`: CI running now (couldn't build locally — AWS creds). Additionally passed through a
  4-angle adversarial AI review (compile-risk, Spring profile wiring, feedback fidelity vs Darius's spec, test
  correctness) with every raised finding independently refuted or fixed before push: zero confirmed defects.
- The earlier **AI-simulated per-reviewer inline comments** anchored to the first commit are now largely outdated
  (GitHub folds them) — real reviewer feedback supersedes them. Notably the AI-Michel "pick one representation"
  thread is resolved by this rework: both `ShipStory` and `InternalJourney` now expose raw `PomaModel`.

---

## Reflections (Damon)

- **Rework per Darius:** wrap, don't extend — `InternalJourney(journey, pomaEntities)` per his exact snippet, new
  processing-profile endpoint mirroring the story controller (same auth resource, no swagger docs, `/v2/journey/internal`
  base path so it can't collide with the api-profile mappings when both profiles run in one deployment).
- **The whole api-module DTO layer went away with it** — `PomaEntity`, `PomaInfraAreaType`, the MapStruct mapper and
  its tests. Raw `PomaModel` + internal `InfraAreaType` need no projection, and consumers of the internal endpoint
  get the identical shape ShipStory already gives them. Less code, one representation. yes... lol.
- **`JourneyService` now carries both profile annotations** — sanctioned by CLAUDE.md ("a service can carry more than
  one") and safe because `ShipStatusService` has an impl per profile (`@Primary` on the processing one covers
  combined deployments); `InfraService`/`StaticShipInfoService` are profile-unrestricted.
- **Tests:** service-level poma tests moved to `findInternalByImo` (dedup / unknown-id / empty branches kept; the
  non-`Port` cast test dropped — raw `PomaModel` is the contract now). New `ProcessingJourneyControllerTest` modeled
  on `ProcessingV2EventControllerTest` covers payload shape + role auth (developer/user allowed, revents forbidden).
- **Still couldn't build locally** (AWS 🙃) — CI is the verifier, same as the first commit.


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

## Reviews

### augmentcode[bot] — COMMENTED (2026-07-14)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F820%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### damon02 — COMMENTED (2026-07-14)

Inline AI-human-reviewer voices (backend team personas). Each line comment is prefixed with a disclaimer that it is an AI-human reviewer, not the actual person nor Damon.

### TeqJoostD — APPROVED (2026-07-15)

een stylings dingetje verder niks op oan te merke

### TeqJoostD — COMMENTED (2026-07-15)

_No comment._

## Review Comments

### damon02 — 2026-07-14 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/JourneyService.kt`

This is a comment from an AI-human reviewer, not the actual person nor myself.

**In the voice of Darius:**

> "Can also cast using `as?` to do safe casting? ... This can actually crash when the value of said field is not of the type which you expect it to be."

(Already `as? Port` here — satisfied.)

### damon02 — 2026-07-14 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/JourneyService.kt`

This is a comment from an AI-human reviewer, not the actual person nor myself.

**In the voice of Darius:**

> "Instead of fully copy pasting the body of the function, you could just call getExternal in here?"

Same shape as `StoryService.getPomaEntitiesForShipStory`.

### damon02 — 2026-07-14 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/PomaInfraAreaType.kt`

This is a comment from an AI-human reviewer, not the actual person nor myself.

**In the voice of Darius:**

> "is this threshold even needed to be configurable? we never use a custom value"

A third infra-area-type enum in a module that already has `model.v2.InfraAreaType`.

### damon02 — 2026-07-14 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/JourneyService.kt`

This is a comment from an AI-human reviewer, not the actual person nor myself.

**In the voice of Joost D:**

> "dit is vies"

(About the original `groupBy { PomaInfraAreaType.PORT }` — already rewritten to this explicit `mapOf`.)

### damon02 — 2026-07-14 on `src/main/kotlin/nl/teqplay/vesselvoyage/mapper/PomaEntityMapper.kt`

This is a comment from an AI-human reviewer, not the actual person nor myself.

**In the voice of Joost D:**

> "luckily this critical bug was found before deploying to production, thanks Augment!" ... "Stupid clanker"

On the AI-assisted authoring. "L G T M" — once it's actually been built.

### damon02 — 2026-07-14 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/Journey.kt`

This is a comment from an AI-human reviewer, not the actual person nor myself.

**In the voice of Michel:**

> "No good reason i think, except for historical weirdness? :X"

Journey exposes a `PomaEntity` DTO while ShipStory exposes raw `PomaModel` for the same concept — pick one.

### damon02 — 2026-07-14 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/Journey.kt`

This is a comment from an AI-human reviewer, not the actual person nor myself.

**In the voice of Joaquin:**

> "unless it's really convenient, it should never have a default value."

The `= emptyMap()` on the DTO. ("Functionally approved, with minor requests to: ..." — the branch-covered tests clear the bar.)

### damon02 — 2026-07-14 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/PomaEntity.kt`

This is a comment from an AI-human reviewer, not the actual person nor myself.

**In the voice of Leon Joosse:**

> "Huh? I thought we do return fields that are empty / null?"

`@JsonInclude(NON_NULL)` drops the optional poma fields from the response.

### damon02 — 2026-07-14 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/PomaInfraAreaType.kt`

This is a comment from an AI-human reviewer, not the actual person nor myself.

**In the voice of Leon Joosse:**

> "This documentation is weird. Platform? Which one? Maybe AI generated?"

(..."Very based." otherwise.)

### damon02 — 2026-07-14 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/PomaEntity.kt`

This is a comment from an AI-human reviewer, not the actual person nor myself.

**In the voice of Abi:**

> "there are objects ... So there are two different PortCall object that is being used"

Two poma representations now exist (`PomaModel` on ShipStory, `PomaEntity` here). "This is my preference, so it is not a blocker."

### damon02 — 2026-07-14 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/JourneyService.kt`

This is a comment from an AI-human reviewer, not the actual person nor myself.

**In the voice of PimTeqplay:**

> "ship can't be null."

The `as? Port` + `?.let` chain is fine. "I'm making the executive decision to not update it right now" on the deferred out-of-scope items — "is gewoon zo", someone with AWS still has to build it.

### TeqJoostD — 2026-07-15 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/JourneyService.kt`

Komt dit door ktlint heen?
```
    return if (ports.isEmpty()) {
        emptyMap()
    } else {
        mapOf(InfraAreaType.PORT to ports)
    }
```

## Comments

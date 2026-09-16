---
id: confluence:1276051457
source: confluence
type: page
space: TC
title: Analysis notes for Pilot events detection
author: Joaquin Marquez Bugella
date: '2026-07-07'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1276051457
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1276051457
---
# Analysis notes for Pilot events detection

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1276051457  

## Content

none

---

# 0. Intro and purpose

tbc

# 1. Context and constraints

he solution needs to fit these domain realities:

* A `Portcall` is made of multiple movements and visits
* Those movements can involve:

  + sea
  + anchorage
  + berth
* The pilot may change from movement to movement
* Some pilot-related events can be detected from `portcall.visits`
* Some cannot, and must be detected from the **raw PCS movement data**
* The current legacy `PilotTiming` on `PortcallVisit` is not sufficient for this feature

Important current-code observations:

* `SgMdhService` already uses `visitType` with values like `BERTH`, `ANCHORAGE`, `PILOTBOARDINGPLACE`
* `EventService.createPredictionEventForUpdateType(...)` already has partial support for non-berth predicted events
* However, the overall `visit` model and the external `PortcallPlusPortcallVisit` payload are still largely **berth-centric**
* POCCA / Corpus Christi currently does **not** model sea/anchorage movements as visits, which is why some pilot events cannot be derived from visits alone

# 2. Options evaluated

Three options have been evaluated

* **Option 1:** Extend the current portcall/visit model and reuse the existing PCS update flow.

  + Useful as part of the final solution, but **not enough as the main strategy**.
* **Option 2:** Create dedicated pilot detector services per PCS, separate from the current portcall update flow.

  + **Feasible, but not preferred** unless the main goal is strict isolation or experimental rollout with minimal coupling.
* **Option 3:** Extend each PCS service to update portcalls and also detect/create/publish pilot events.

  + **This option is recommended as the primary implementation strategy**.  
    **Each PCS integration should remain responsible for detecting pilot-related changes** from its own source model and publishing the corresponding pilot events. To support correctness and de-duplication, this should be complemented by additive model evolution in Portcall/PortcallVisit and a small common post-update hook that exposes the raw source model together with the current and updated portcall state.

## Option 1: Extend the current portcall/visit model and reuse the existing PCS update flow

### Description

Extend `PortcallVisit` with pilot timestamp fields and generate pilot events by diffing visit changes, similar to how some current visit-related events are emitted today.

### Advantages

* Reuses the existing portcall update mechanism
* Reuses persisted old/new state comparison
* Natural fit for visit-related event generation
* Easier to understand when pilot information clearly belongs to a visit edge

### Limitations

This option alone is **not sufficient**.

Main reasons:

* Some pilot events are **not represented in visits**
* POCCA currently derives meaningful timing from **movements involving sea/anchorage**
* Those movements are not always materialized as `visits`
* So visit-only diffing would miss valid pilot events

### Conclusion on option 1

Useful as part of the final solution, but **not enough as the main strategy**.

## Option 2: Create dedicated pilot detector services per PCS, separate from the current portcall update flow

### Description

Keep the current portcall update logic untouched, and build dedicated pilot-event services per PCS integration.

### Advantages

* Strong separation of concerns
* Low direct impact on current portcall update flow
* Can work directly with raw PCS source data
* Easier to isolate if piloting as an experiment

### Drawbacks

* Duplicates PCS-specific parsing and detection logic
* Duplicates scheduling / fetch lifecycle concerns
* Increases risk of drift between:

  + the portcall state
  + the pilot detector interpretation of the same PCS data
* More services to maintain

### Conclusion on option 2

Feasible, but not preferred unless the main goal is strict isolation or experimental rollout with minimal coupling.

## Option 3: Extend each PCS service to update portcalls and also detect/create/publish pilot events

### Description

Each PCS service remains responsible for:

1. fetching its source data
2. updating the portcall
3. detecting pilot-related changes from the raw source data
4. creating and publishing the pilot events (`PortcallPlusPilotEvent`)

### PortcallPlusPilotEvents

For a specific and reliable design towards the pilot events, the following events should be defined, implementing, at least the `AisEngine` interface `PortcallPlusEvent` and possibly the `AreaBasedEvent`:

* `PortcallPlusEstimatedTimePilotOnBoard`

  + Identified from **DEPARTING** movements **FROM** a location where the pilot and scheduled or estimated time is set.
  + It should implement `PredictedEvent`.
  + The resulting subject would be `event.external.portcallplus.prediction.pilot.onboard.<areaType>.<areaId>`
* `PortcallPlusActualTimePilotOnBoard`

  + Identified from **DEPARTING** movements **FROM** a location where the pilot and actual time is set.
  + It should implement `ActualEvent`.
  + The resulting **subject** would be

    `event.external.portcallplus.actual.pilot.onboard.<areaType>.<areaId>`
* `PortcallPlusEstimatedTimePilotOffBoard`

  + Identified from **ARRIVING** movements **TO** a location where the pilot and estimated time is set.
  + It should implement `PredictedEvent`.
  + The resulting **subject** would be

    `event.external.portcallplus.prediction.pilot.offboard.<areaType>.<areaId>`
* `PortcallPlusActualTimePilotOffBoard`

  + Identified from **ARRIVING** movements **TO** a location where the pilot and actual time is set.
  + It should implement `ActualEvent`.
  + The resulting **subject** would be

    `event.external.portcallplus.actual.pilot.offboard.<areaType>.<areaId>`

### Why this fits best

This is the best fit for the current architecture because the PCS service already knows:

* the source model semantics
* how to interpret fields like:

  + `scheduledTime`
  + `underwayTime`
  + `offTime`
  + `from_stop_location`
  + `to_stop_location`
* whether pilot info is meaningful and how it maps to the movement

In other words:

> pilot event detection is inherently PCS-specific, so it belongs closest to the PCS adapter.

### Conclusion on option 3

**Recommended option**, but with a small common extension:

* not just event publishing
* also support for comparing persisted normalized pilot state

### Why pure 3 still needs a small shared enhancement

The main issue with a pure "detect and publish directly from source changes" approach is this:

After the current update flow, the shared code often only sees the resulting `Portcall`, not the original `ServiceModel`.

For correct pilot detection, especially for movement-driven cases, the detector may need all three:

* `serviceModel`
* `currentPortcall`
* `updatedPortcall`

Therefore, the recommended refinement is to add a **small optional post-update hook** in the common update pipeline, so that PCS services can do:

* compare raw source semantics
* compare persisted state
* build and publish pilot events

This is a **small lifecycle extension**, not a redesign of task scheduling.

# 3. Main design conclusion from the discussion

## Keep option 3 as the backbone

PCS services should own pilot-event detection logic.

## Add persisted normalized pilot state

A pure event-only approach is too fragile for some cases.

Persisting normalized pilot state gives:

* reliable diffing
* deduplication
* support for movement-driven cases not represented as visits

## Treat a visit as a node with two edges

This was a key design conclusion.

Instead of thinking:

* "pilot onboarding belongs only to arrival or departure"

the better model is:

* a visit has an **arrival edge**
* a visit has a **departure edge**
* each edge may carry:

  + estimated onboard
  + actual onboard
  + estimated offboard
  + actual offboard
  + pilot identity

This solves the "first visit / last visit" gap.

### Naming conclusion

Your `arrival` / `departure` intuition is valid, as long as those are understood as **edge containers**, not event types.

Even clearer naming could be:

* `arrivalLeg`
* `departureLeg`

But the concept is the same.

## Design discussions

### Discussion conclusion on the "first edge / last edge" problem

The gap disappears if:

* the **first actual visit** stores pilot data on its `arrival` edge
* the **last actual visit** stores pilot data on its `departure` edge

That means:

* no need to invent a synthetic "sea visit"
* sea can remain an implicit boundary
* the model remains cleaner

### Discussion conclusion on anchorage visits

We discussed the shifting case:

* berth -> anchorage
* anchorage -> berth

#### Conclusion

Anchorage should likely become a **first-class visit type** in the internal `Portcall.visits` model.

Recommended direction:

* **yes** to anchorage and pilot boarding place visits
* **no** to sea as a synthetic visit

Why:

* anchorage is a real operational node in the movement graph
* it helps represent shifting accurately
* it helps attach pilot edge data more naturally
* it reduces ambiguity around berth/anchorage transitions

### Discussion conclusion on current event model impacts

We identified that the main risk is **not** simply `createEventIfVisitsChanged(...)`.

The bigger issues are:

#### 1) `PortcallPlusVisitsUpdateEvent` payload is incomplete

Current `PortcallPlusPortcallVisit` does not carry:

* `visitType`

That is a limitation if visits can now be:

* berth
* anchorage
* pilot boarding place

#### 2) External visit payload is berth-centric

Field names are berth-specific:

* `berthName`
* `berthEta`
* `berthAta`
* etc.

If visits become generic location stops, this external contract should be reviewed.

#### 3) Some current actual event creation is still berth-biased

ETA/ETD prediction handling already has some non-berth support, but ATA/ATD event generation is more berth-oriented.

## Data model migration conclusion

We discussed whether this implies database conversion.

### Conclusion

Not necessarily at first.

If the internal model evolution is **additive**, then an immediate DB migration is not mandatory.

### Recommended migration style

* keep old fields
* add new fields
* default new fields from old ones where appropriate
* continue reading old documents safely

### Example policy discussed

For old persisted data:

* legacy berth fields remain available
* new generic fields can be initialized from old ones conditionally
* that condition can be strict, e.g. only for `visitType == BERTH`, if the intention is not to normalize questionable historical non-berth data

### Important outcome

This supports a **phased migration**, rather than a risky big-bang conversion.

## Recommended target architecture

### Internal model direction

#### `PortcallVisit`

Evolve from a berth-only structure toward a generic location-stop structure.

Suggested direction:

* preserve legacy berth fields initially
* add normalized location/pilot edge data
* support visit types:

  + `BERTH`
  + `ANCHORAGE`
  + `PILOTBOARDINGPLACE`

##### Pilot edge model

Each visit should conceptually have:

* `arrival` or `arrivalLeg`
* `departure` or `departureLeg`

Each edge may carry:

* estimated onboard
* actual onboard
* estimated offboard
* actual offboard
* pilot identity

#### Optional movement-level pilot state

For PCS cases where pilot-relevant transitions do not map naturally to a visit, keep a normalized movement-level pilot state at `Portcall` level, keyed by movement id.

This is especially useful for POCCA-style movement-only logic.

### Common service flow direction

Recommended lifecycle:

1. fetch source models
2. convert/update portcall
3. persist updated portcall
4. run generic existing event logic
5. run optional PCS-specific supplementary pilot-event detection hook
6. publish pilot events

#### Key principle

Keep source-specific detection **out of** generic `EventService` where possible.

Use the PCS service to decide:

* what changed
* whether it is pilot-related
* which event should be emitted

Use common services to support:

* state comparison
* publishing
* shared helpers

## Elaborated action plan

### Phase 0 — Design alignment and scope lock

#### Goals

* lock the target semantics before implementation
* avoid refactoring churn later

#### Decisions to confirm

* `arrival` / `departure` as edge containers
* each edge can hold both onboard and offboard timestamps
* anchorage and pilot boarding place become first-class visit types
* sea remains implicit, not a visit
* whether movement-level pilot state is needed in `Portcall`
* where the 4 new pilot event classes live:

  + likely external/shared event dependency
* whether external visit payload needs extension or versioning

#### Deliverables

* approved domain model
* approved naming
* approved scope for phase 1 rollout

### Phase 1 — Internal model evolution

#### Goals

* add the minimum internal state needed for pilot tracking
* avoid breaking persisted data

#### Proposed work

* evolve `PortcallVisit` additively
* add pilot identity model
* add pilot edge data model
* add edge fields for arrival and departure
* optionally add normalized movement-level pilot state at `Portcall` level
* preserve old berth fields for compatibility

#### Migration strategy

* additive only
* no immediate destructive DB migration
* old persisted fields remain available
* defaults/backward compatibility applied where appropriate

#### Deliverables

* updated internal model
* backward-compatible deserialization
* documented transition policy for old fields vs new fields

### Phase 2 — Common update-pipeline enhancement

#### Goals

* enable PCS services to detect pilot events using:

  + raw service model
  + previous portcall state
  + updated portcall state

#### Proposed work

* introduce a lightweight update context that preserves `ServiceModel`
* add an optional post-update hook in the common update flow
* keep the scheduler/task orchestration unchanged
* keep existing generic event generation intact

#### Deliverables

* common supplementary-event hook
* service update context
* publishing support for supplementary pilot events

### Phase 3 — External event model evolution

#### Goals

* support the four new pilot events
* make the visit payload compatible with non-berth visit semantics

#### Proposed work

* add the 4 pilot event classes (`PortcallPlusPilotEvent`) in the shared event model dependency
* review `PortcallPlusPortcallVisit`
* decide one of:

  + additive extension
  + versioned V2 payload/event
* add `visitType`
* address berth-specific field naming concerns

#### Deliverables

* external/shared event model ready
* routing/publishing strategy validated
* compatibility strategy documented

### Phase 4 — POCCA / Corpus Christi implementation first

#### Why first

POCCA is currently the clearest working example for movement-based pilot logic.

#### Proposed rules to implement first

* `EstimatedTimePilotOnBoard`

  + from `SEA` or anchorage-like origin
  + pilot info present
  + `scheduledTime` changed
* `ActualTimePilotOnBoard`

  + from `SEA` or anchorage-like origin
  + pilot info present
  + `underwayTime` changed
* `EstimatedTimePilotOffBoard`

  + to `SEA` or anchorage-like destination
  + only if source actually provides a relevant estimated offboarding value
  + POCCA currently appears not to
* `ActualTimePilotOffBoard`

  + to `SEA` or anchorage-like destination
  + pilot info present
  + `offTime` changed

#### Additional handling

* berth -> anchorage shifts
* anchorage -> berth shifts
* corrected movements
* pilot changes between consecutive movements

#### Deliverables

* POCCA pilot timestamps persisted
* POCCA pilot events emitted
* POCCA-specific tests passing

### Phase 5 — Visit model broadening

#### Goals

* make visits represent actual operational stops, not only berths

#### Proposed work

* allow anchorage visits in internal `Portcall.visits`
* adapt visit matching logic where needed
* ensure non-berth visits are not forced through berth-only assumptions
* revisit sort/match behavior for anchorage transitions

#### Deliverables

* internal visit graph supports berth/anchorage/pilot boarding place
* no regression on current berth-based behavior

### Phase 6 — EventService alignment

#### Goals

* ensure generic event generation behaves correctly for non-berth visits

#### Proposed work

* review visit-based ETA/ETD logic with new visit types
* review ATA/ATD area generation for non-berth visits
* update `PortcallPlusVisitsUpdateEvent` mapping
* identify and publish new `PortcallPlusPilotEvent`s
* keep generic logic generic, not PCS-specific

#### Deliverables

* consistent area semantics for visit events
* correct behavior for anchorage and pilot boarding place visits

### Phase 7 — Migration, compatibility, and rollout

#### Goals

* reduce implementation risk
* support incremental rollout

#### Proposed work

* feature flag or PCS-specific enablement
* roll out POCCA first
* monitor emitted events
* decide whether and when to backfill old portcalls
* postpone hard removal of legacy berth fields until proven safe

#### Deliverables

* controlled production rollout
* observability for pilot-event generation
* migration/backfill decision after validation
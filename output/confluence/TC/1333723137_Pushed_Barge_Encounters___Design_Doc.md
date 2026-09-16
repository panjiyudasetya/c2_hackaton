---
id: confluence:1333723137
source: confluence
type: page
space: TC
title: Pushed Barge Encounters — Design Doc
author: Michel Wilson
date: '2026-09-09'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1333723137
explicit_links:
- jira:TCC-1188
- jira:TCC-1055
- jira:TCC-1189
- jira:TCC-1207
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1333723137
---
# Pushed Barge Encounters — Design Doc

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1333723137  

## Content

**Status: draft.** Structure and reasoning are settled; the *numbers* are not. Items marked **TODO** need domain input or measurement against real AIS traces. Written for TCC-1188, under epic TCC-1055.

**This is an enhancement of an existing, live detector — not a new one.** `EncounterType.BARGE_PUSH` is already detected from `ShipRole.PUSHBARGE` and already fires in production. Everything below changes the behaviour of that existing type.

## 1. Overview

### Problem statement

A pushed barge is a dumb barge with no AIS transponder, pushed by a small tug ("push boat") that does transmit. Two things follow.

**We cannot see the barge.** The AIS `TransponderPosition` we hold describes the push boat's own hull, and the barge extends beyond it. So the only vessel we can observe may sit well clear of the sea vessel while the barge is squarely alongside.

**The current detector does not check alongside at all.** The `BARGE_PUSH` rule is `boardBoardDetectorForRole(ShipRole.PUSHBARGE, alongside = false)` — that `false` disables the alongside test, leaving only a proximity check. So today a push boat near a stationary sea vessel produces a `BARGE_PUSH` encounter whether or not it is actually alongside, and against whichever sea vessel the bucket scan happens to reach. That is the accuracy gap this document closes.

A barge encounter does **not** correspond one-to-one with a bunkering: the same push boats move cargo barges alongside the same sea vessels in an identical-looking manoeuvre. This design therefore reports only the encounter, tagged with a coarse bunker/cargo hint from CSI, and leaves the bunker call to `vesselvoyage` (§9).

### Goals

* `BARGE_PUSH` events that reliably mean "this push boat was alongside *this* sea vessel", with the barge's real extent accounted for.
* Emit both **long** encounters (a transfer) and **short** ones (a suspected drop-off or pick-up). Do not try to tell them apart; publish the times and let the consumer decide.
* **A first attempt at classifying what kind of barge encounter it is** — bunkering or cargo — by carrying the push boat's CSI subtype (§3) onto the event. Coarse by construction: the subtype describes the *pusher*, not the barge it happens to be pushing that day, so it is a starting point for `vesselvoyage` rather than an answer.
* Real-time, using the existing start/end machinery.

### Non-goals

* **Deciding that an encounter is a bunkering.** That happens in `vesselvoyage`. §9.
* **Merging a drop-off and a later pick-up into one operation.** Also `vesselvoyage`, later. The behaviour is suspected to occur (§2) but is not modelled here.
* Volume or fuel-type estimation.
* Identifying the barge itself. A dumb barge has no MMSI or IMO, so no CSI register entry, and the CSI model carries no push-boat→barge relation.
* A new encounter type. `BARGE_PUSH` is reused.

## 2. Domain background

**TODO** — from Gavin, Leon and Richard:

* Which US ports, which operators, and how many push boats already carry the `PUSHBARGE` role.
* **A single representative barge length**, plus a sense of the spread around it. That one number is all §4 needs. The spread matters because the same value is applied fleet-wide, so it *is* the error budget. Figures carried over from European river practice will be wrong: US barges are materially larger.
* Whether push boats commonly serve both fuel and cargo barges, which bounds how far the CSI subtype in §3 can be trusted.

### Drop-off and pick-up

A push boat is not permanently coupled to its barge. It is suspected that a push boat may deliver a barge, depart, and return — or be replaced by a different push boat — to collect it later, leaving the barge alongside unobserved in between.

This document does **not** model that. It emits each alongside period as its own encounter, short ones included, which is exactly what a later consumer needs in order to stitch two short encounters into one operation (§9). Recording the suspicion here so the shape of the data reads as deliberate: **a pair of short encounters hours apart on the same sea vessel is the expected signature of a drop-off and pick-up.**

Case 1 — push boat stays
push boat ──────[ alongside sea vessel, hours ]──────▶ departs
encounter │◀──────── one long encounter ──────▶│
Case 2 — drop-off and pick-up
push boat A ──[ short ]──▶ departs
push boat B ──[ short ]──▶ departs (with barge)
barge │◀─────── alongside, unobserved ───────▶│
encounters │◀ short ▶│ │◀ short ▶│

Confirming that this happens, and how often, is a research task, not a blocker.

## 3. What we can observe today

| Entity | AIS | How we know it |
| --- | --- | --- |
| Sea vessel (main) | yes | `ShipState.relevantSeaShip` |
| Push boat (service) | yes | `ShipRole.PUSHBARGE` — already exists, no new flag needed |
| Barge | **no** | never observed — its extent is *assumed*, its cargo *labelled* via the push boat |

### The one CSI change

Identification needs nothing new: `ShipRole.PUSHBARGE` already marks these vessels and already drives the `BARGE_PUSH` rule. What is missing is what the barge carries. Add a **push-barge subtype** — `BUNKER`, `CARGO`, `UNKNOWN` — on vessels holding that role, defaulting to `UNKNOWN` so an unlabelled push boat still produces encounters.

`encounter-monitor` reads the subtype and stamps it on the event (§8). It travels the same path the role already takes, from CSI through to `ShipState`.

**Note:** TCC-1189 is written as a push-boat *boolean*. Since the role already exists, that ticket should be re-scoped to deliver this subtype instead.

## 4. Detecting that the barge is alongside

Two changes: switch the `BARGE_PUSH` rule to `alongside = true`, and make the alongside test account for the barge rather than only the push boat.

### Accounting for the barge

`isAlongside()` currently treats the service vessel as a single point and asks whether that point falls beside the sea vessel's hull. For a push boat, that point is at the wrong end of the convoy — it sits at the after end of a barge that may be several times its own length.

**Recommendation:** move the point along the convoy axis by roughly half the barge length, so the tested position approximates the middle of the convoy rather than its tail. This is a small, contained change: the geometry stays a point-versus-hull test, only the point moves.

A fuller treatment would give the service vessel a fore/aft extent and test the whole convoy centreline against the sea vessel's hull as a segment. That is more accurate but a larger change to a shared function, and it is not obviously worth it until we know how badly the simple version performs. Recorded in §12.

### The heading problem, which is the real obstacle

Moving the point requires knowing which way the convoy points, and **these vessels largely do not report a reliable true heading** — no magnetic compass, so the AIS heading field is absent or wrong. `ShipState.heading` is already nullable and `isAlongside` already degrades to a plain distance check when it is missing, which is precisely the case we care about.

Course over ground does not rescue this. It is meaningful only when the vessel is moving, and these encounters are by definition with a stationary or near-stationary convoy.

Options, none of them free:

* **Use the sea vessel's heading as the axis.** A barge alongside for transfer lies parallel to the sea vessel, and the sea vessel's heading *is* generally reliable. Extend the search along that axis instead of the push boat's own. Removes the dependency on the push boat's heading entirely. **Caveat:** it does not tell us whether the barge lies forward or aft of the push boat, so the extension has to be symmetric — effectively widening the accepted band along the quay by a barge length in both directions. Crude, but it fails in the safe direction.
* **Carry the heading from the approach.** Remember the push boat's course over ground from while it was still under way and reuse it once stopped. More precise when available, but adds state and is empty for a convoy already alongside when we start observing it.
* **Do nothing directional** and simply widen the alongside distance. Simplest, and it loses the distinction between "alongside" and "somewhere nearby" — which is the thing we are trying to fix.

**Recommendation:** the first. Assume parallel, extend symmetrically along the sea vessel's axis, and accept the loss of precision. It needs no new state and no unreliable input.

**Consequence worth stating.** Assuming parallelism means we cannot also *use* parallelism to tell candidate sea vessels apart — see §5.

### Bounding the damage

A `PUSHBARGE`-role vessel is treated as having a barge whether or not it currently does, and the assumed extent is fleet-wide rather than per-vessel. Two bounds:

* **Hard cap on the raw distance.** Require the un-extended push boat to be within the existing `EndDistance.ALONGSIDE` (130 m) of the sea vessel before any barge extension applies. One explicit number that bounds the error however wrong the barge length is.
* **Clamp the extension** so a configuration mistake cannot produce an implausibly long convoy.

## 5. Picking the right sea vessel

The accuracy question that matters most, and the one the current detector does not address at all. `detectEncounters` evaluates every nearby pair independently, so a single push boat can open concurrent encounters against two sea vessels when at most one is real.

This is harder than it first looks, because §4 spent the strongest available discriminator. A parallel-heading test — "the convoy lies parallel to the sea vessel, so reject candidates it is skewed to" — would separate a genuine alongside from a convoy passing close astern better than any distance threshold. But it needs the push boat's heading, which we do not have, and §4's fallback *assumes* parallelism rather than measuring it. What is assumed cannot discriminate.

What remains is heading-free:

* **Perpendicular distance to the hull line.** The push boat's *position* is reliable even when its heading is not. Prefer the sea vessel whose hull line the push boat is laterally closest to. This is the primary discriminator.
* **Longitudinal overlap** as a tie-break: prefer the candidate whose hull the convoy actually sits beside rather than one it merely reaches past. Coarse, because §4's symmetric extension makes the convoy footprint long in both directions.
* **Lowest MMSI** as a final tie-break, purely so the outcome is deterministic and reproducible in trace tests.

Emit at most one `BARGE_PUSH` encounter per push boat at a time.

**Stickiness.** Once an encounter is established, do not switch counterparty mid-encounter even if another candidate becomes momentarily closer. Ending and restarting against a different sea vessel because of a metre of GPS jitter is worse than being slightly wrong for the duration.

**Honest caveat.** Without the heading test, selection rests on lateral distance alone, and two vessels berthed close together on the same quay line may not be separable at all. If that turns out to be common, the options are to accept the error, or to bring in berth knowledge, which `encounter-monitor` does not have today. **TODO:** check against real US port layouts how often two candidates are genuinely ambiguous.

## 6. Detection rule and structure

There is **no cross-encounter state**. Encounters stay ordinary pair-keyed `EncounterState` records going through `processNormalEncounter` like every other alongside type — no sea-vessel-keyed operation, no new Redis entity, no sweep.

Nor is there a rule-ordering problem. `ShipState.role` is single-valued, so a `PUSHBARGE` vessel cannot match the `TUG`-keyed rules, and the `BARGE_PUSH` rule already sits ahead of `TUG_WAITING_DEPARTURE` in `detectionRules`.

What changes:

* The `BARGE_PUSH` rule goes from `alongside = false` to the barge-aware alongside check of §4.
* The sea-vessel selection of §5.
* An `EncounterMetadata` subtype for the label. §8.
* Endurance, below.

### Endurance

`BARGE_PUSH` currently uses `Timeout.LONG` (6 minutes). A drop-off manoeuvre lasts minutes, and §9 needs those short encounters, so 6 minutes will discard part of the drop-off/pick-up signal before it is ever emitted.

**Recommendation:** move to `Timeout.NORMAL` (3 minutes) and tune from traces. Shorter keeps genuine drop-offs but admits more passing traffic; longer is cleaner but silently drops half the signal. Since a spurious short encounter costs `vesselvoyage` far less than a missing one, err short.

## 7. Effect on existing consumers

`BARGE_PUSH` is live and does reach Platform (`PushBargeEvent`) and portreporter (`PUSH_BARGE.ATS` / `.ATC`), so this changes what those consumers see. The changes cut both ways: turning on the alongside check is **stricter** and will remove encounters that were merely nearby, while the barge extension and the shorter endurance are **looser**.

In practice the risk looks low — `BARGE_PUSH` is barely used downstream. So the recommendation is to apply the change **globally** rather than gating it to US ports, which also avoids having to make the endurance area-dependent (`checkEndurance` switches on encounter type alone, so scoping it would mean threading a flag through the encounter state).

Worth a heads-up to consumers regardless, and TCC-1207's Definition of Done already asks for that. If the comparison in §10 shows more movement than expected, gating to configured areas remains the fallback.

## 8. Events and the label

`otherShip` carries the push boat's MMSI, `ship` the selected sea vessel. Start and end times are the encounter's real boundaries — they are most of what §9 consumes, so their accuracy is what this design is judged on.

The subtype rides on the event as a new `EncounterMetadata` subtype. Precedent exists — `TugEncounterMetadata`, `BoatmanEncounterMetadata`, `STSEncounterMetadata` — and both event classes already have a `metadata` field, so no event-model surgery. Build it at publish time from `ShipState` rather than persisting it: the subtype is available live whenever an event fires, and `EncounterState.startMetadata` persists a Jackson-polymorphic interface into a Redis hash, which is fragile.

**Note:** the Platform converter does not propagate `metadata`, so the label will not reach Platform or portreporter. That is fine — `vesselvoyage` consumes the ais-engine event directly.

## 9. Handoff to `vesselvoyage`

`vesselvoyage` becomes the source of truth for bunker events. It consumes `BARGE_PUSH` start/end pairs and needs, per encounter: the sea vessel, the push boat, the start and end times, and the subtype label.

1. Read the subtype off the event. `BUNKER` → candidate bunkering; `CARGO` → discard; `UNKNOWN` → **TODO**, decide whether to emit or hold.
2. Emit a bunker event for a long encounter.
3. **Later:** merge two short encounters on the same sea vessel, separated by a gap, into one bunkering spanning drop-off to pick-up (§2). Doing this in `vesselvoyage` rather than here is deliberate — it can be revised, backfilled and re-run against stored encounters, whereas the same logic in `encounter-monitor` would be a stateful stream with no second chance.

**TODO** — agree the contract with the `vesselvoyage` owners, in particular the `UNKNOWN` case and whether a maximum gap should bound the future merging.

## 10. Validation and testing

* **Geometry unit tests** in `ShipTest`: a push boat placed progressively further from the sea vessel's hull, asserting the barge extension brings genuinely-alongside cases into range without pulling in distant ones; plus heading-null rows, since that is the normal case here and not an edge case.
* **Sea-vessel selection**: two candidate sea vessels at realistic berth spacing — the correct one is chosen, only one encounter opens, and jitter does not switch the counterparty mid-encounter.
* **Regression.** The existing `BARGE_PUSH` expectations in `EncounterServiceTraceTest` are the regression suite. Any movement is a consumer-visible change and must be explained, not re-baselined.
* **Before/after comparison** over recorded AIS, to see how much the encounter set actually moves. This is what tells us whether §7's "apply globally" recommendation holds.
* **Data dependency, not an afterthought.** The barge length and the endurance stay placeholders until we have real US traces.

## 11. Open questions

1. **Barge length and its spread** (§2). One configured value covers the fleet, so the spread is the error budget. Needs domain input.
2. **The heading problem** (§4). Is the symmetric parallel assumption good enough, or do we need to carry the approach course? Answerable from traces.
3. **Ambiguous sea vessels** (§5). Without a heading-based test, how often are two berthed vessels genuinely inseparable?
4. **Unknown-subtype handling** (§9). When the push boat's subtype is `UNKNOWN`, should `vesselvoyage` emit an uncertain bunker event or hold it back?

## 12. Future expansion

* Merging drop-off and pick-up encounters, in `vesselvoyage` (§9).
* Giving the service vessel a true fore/aft extent and testing the convoy centreline as a segment against the sea vessel's hull, rather than moving a single point (§4).
* **A subtype that varies over time.** The subtype is currently a fixed property of the push boat, so a pusher that works both bunker and cargo barges is necessarily mislabelled some of the time. Giving it validity periods in CSI — so it can be corrected for a stretch rather than forever — would sharpen §9's conversion without changing anything in this design. Note this interacts with stamping the label on the event (§8): a time-varying subtype is only useful if it is resolved for the encounter's own time window.
* Better bunker/cargo discrimination than any per-vessel label — berth knowledge, or encounter duration as a signal.
* Propagating the subtype label through the Platform converter, if a consumer there ever wants it (§8).
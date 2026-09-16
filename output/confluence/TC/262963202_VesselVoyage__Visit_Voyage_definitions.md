---
id: confluence:262963202
source: confluence
type: page
space: TC
title: 'VesselVoyage: Visit/Voyage definitions'
author: Leon Joosse (Unlicensed)
date: '2024-05-27'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/262963202
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/262963202
---
# VesselVoyage: Visit/Voyage definitions

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/262963202  

## Content

# V1 Definitions

## Glossary

* **Visit:** A vessel having a Stop within the EOS boundaries of a port.
* **Voyage:** The travel between 2 Visits.
* **Stop:** A vessel stops moving at a location for at least 15 minutes.
* **Pass-through:** A vessel passes through a port inner area without having a Stop.

## General Rules

* **Only 1 Visit or Voyage can happen at the time.**
* **A Visit can only be followed up by a Voyage.**
* **A Voyage can only be followed up by a Visit.**

## Visit

* **A Visit is created when having any Stop inside the EOS.** The Visit start time is the first EOS AreaStartEvent `eventTime`.
* **A Visit is finished when leaving the EOS area of the main port.** The Visit end time is the main port EOS AreaEndEvent `eventTime`.

## Voyage

* **A Voyage cannot be triggered by itself.** There must always be a Visit before a Voyage, following up with a Visit if the Voyage is not finished.
* **A Voyage is created when the currently ongoing Visit is finished.** The Voyage start time is the finished/previous Visit’s end time.
* **A Voyage is finished when a new Visit is created.** The Voyage end time is the created Visit’s start time.

## Stop

* **A Stop is created when a vessel stops moving for at least 15 minutes.** The Stop’s start time is the VesselStopStartEvent `eventTime`.
* **A Stop is finished when a vessel starts moving again when stopped.** The Stop’s end time is the VesselStopEndEvent `eventTime`.
* **A Stop must always be in the time window of a Visit or Voyage.**
* **A Stop can be split into multiple stops when the Stop’s time window overlaps the start or end time of a Visit or Voyage.**

  + When being split, a reference to the split stops should be attached to identify them.
  + When split, the Stop should be merged back when resuming the previous Visit or Voyage when the current entry is cancelled.

## Pass-through

* **A Pass-through must always be in the time window of a Visit or Voyage.**
* **A Pass-through can be placed on a Visit when we enter the inner area of a sub-port of the Visit port, but we do not stop.** For example, we have a Visit for NLRTM and go through NLVLA without stopping.

# API models

## Visit

| **Field** | **Type** | **Note** |
| --- | --- | --- |
| entryId | String |  |
| start.time | Instant |  |
| start.location | Location |  |
| end.time | Instant |  |
| end.location | Location |  |
| port.main | String | Either Poma ID or unlocode |
| port.sub | List<String> | Either Poma ID or unlocode |
| trace.polyline | Polyline |  |
| trace.slowSteaming[\*].start.time | Instant |  |
| trace.slowSteaming[\*].start.location | Location |  |
| trace.slowSteaming[\*].end.time | Instant |  |
| trace.slowSteaming[\*].end.location | Location |  |
| trace.slowSteaming[\*].speed.min | Float |  |
| trace.slowSteaming[\*].speed.max | Float |  |
| trace.slowSteaming[\*].speed.average | Float |  |
| trace.speed.min | Float |  |
| trace.speed.max | Float |  |
| trace.speed.average | Float |  |
| stop[\*].start.time | Instant |  |
| stop[\*].start.location | Location |  |
| stop[\*].end.time | Instant |  |
| stop[\*].end.location | Location |  |
| stop[\*].location | Location | Actual location |
| stop[\*].area.type | String | Berth, Anchor, Lock or unclasified |
| stop[\*].area.id | String | Either Poma ID or area name |
| stop[\*].accuracy | Float | Accuracy in percentage |
| passThrough[\*].port | String | Either Poma ID or unlocode |
| passThrough[\*].start.time | Instant |  |
| passThrough[\*].start.location | Location |  |
| passThrough[\*].end.time | Instant |  |
| passThrough[\*].end.location | Location |  |
| previous.port | String | Either Poma ID or unlocode |
| previous.entryId | String | The previous Voyage |
| next.port | String | Destination of next Visit or empty if we don’t know anything  Either Poma ID or unlocode |
| next.entryId | String | The next Voyage if we have any |

## Statement of Facts (SoF)

The SoF will have 2 different models, with timestamps grouped based on either the Port view or Terminal view.

### Port SoF

In the Port SoF we will have 3 different containers with activities.

1. **Arrival**: denotes all activities before the first berth/terminal visit, after entering the EOSP. Basically, all activities before going into the port. Such as anchoring, piloting, waiting.
2. **In Port**: denotes all activities in the port, such as berth/terminal visits
3. **Departure**: denotes all activities after the last berth/terminal visit, such as piloting, anchoring and exiting the EOSP

| **Field** | **Type** | **Note** |
| --- | --- | --- |
| entryId | String |  |
| arrival.start | Location & Instant | EOS start time |
| arrival.activity[\*].time | Instant |  |
| arrival.activity[\*].location | Location |  |
| arrival.activity[\*].type | String | Type of the activity (e.g. anchor up) |
| arrival.end | Location & Instant | Determined in this order, before the first berth visit:   1. First pilot start encounter before first berth stop 2. Last pilot area exit before first berth stop **Note:** at a later moment, align with PTO by applying -15 minutes, as it is not realistic for the event to happen at the edge of the pilot area 3. Last Anchor Up before first berth stop (event only, not based on an area!) 4. First Port ATA ('first' to have no confusion with main + sub ports) 5. EOS ATA |
| inPort.start | Location & Instant | Same value as `arrival.end` |
| inPort.activity[\*].time | Instant |  |
| inPort.activity[\*].location | Location |  |
| inPort.activity[\*].type | String |  |
| inPort.end | Location & Instant | The first available event in the list:   1. First pilot end encounter event, after leaving the last port 2. First pilot area start, after leaving last port 3. Last Port ATD |
| departure.start | Location & Instant | Same value as `inPort.end` |
| departure.activity[\*].time | Instant |  |
| departure.activity[\*].location | Location |  |
| departure.activity[\*].type | String |  |
| departure.end | Location & Instant | EOS ATD |

### Terminal SoF

In the Terminal SoF we will have 4 different containers with activities.

1. Pre-Arrival
2. Arrival
3. In Port
4. Departure

| **Field** | **Type** | **Note** |
| --- | --- | --- |
| entryId | String |  |
| preArrival.start | Location & Instant | EOS start time |
| preArrival.activity[\*].time | Instant |  |
| preArrival.activity[\*].location | Location |  |
| preArrival.activity[\*].type | String | Type of the activity (e.g. anchor up) |
| preArrival.end | Location & Instant | First Anchor ATD |
| arrival.start | Location & Instant | Same value as `preArrival.end` |
| arrival.activity[\*].time | Instant |  |
| arrival.activity[\*].location | Location |  |
| arrival.activity[\*].type | String |  |
| arrival.end | Location & Instant | Port ATA |
| inPort.start | Location & Instant | Same value as `arrival.end` |
| inPort.activity[\*].time | Instant |  |
| inPort.activity[\*].location | Location |  |
| inPort.activity[\*].type | String |  |
| inPort.end | Location & Instant | Port ATD |
| departure.start | Location & Instant | Same value as `inPort.end` |
| departure.activity[\*].time | Instant |  |
| departure.activity[\*].location | Location |  |
| departure.activity[\*].type | String |  |
| departure.end | Location & Instant | EOS ATD |

## Voyage

| **Field** | **Type** | **Note** |
| --- | --- | --- |
| entryId | String |  |
| start.time | Instant |  |
| start.location | Location |  |
| end.time | Instant |  |
| end.location | Location |  |
| trace.polyline | Polyline |  |
| trace.slowSteaming[\*].start.time | Instant |  |
| trace.slowSteaming[\*].start.location | Location |  |
| trace.slowSteaming[\*].end.time | Instant |  |
| trace.slowSteaming[\*].end.location | Location |  |
| trace.slowSteaming[\*].speed.min | Float |  |
| trace.slowSteaming[\*].speed.max | Float |  |
| trace.slowSteaming[\*].speed.average | Float |  |
| trace.speed.min | Float |  |
| trace.speed.max | Float |  |
| trace.speed.average | Float |  |
| stop[\*].start.time | Instant |  |
| stop[\*].start.location | Location |  |
| stop[\*].end.time | Instant |  |
| stop[\*].end.location | Location |  |
| stop[\*].location | Location | Actual location |
| stop[\*].area.type | String | Berth, Anchor, Lock or unclasified |
| stop[\*].area.id | String | Either Poma ID or area name |
| stop[\*].accuracy | Float | Accuracy in percentage |
| passThrough[\*].port | String | Either Poma ID or unlocode |
| passThrough[\*].start.time | Instant |  |
| passThrough[\*].start.location | Location |  |
| passThrough[\*].end.time | Instant |  |
| passThrough[\*].end.location | Location |  |
| previous.port | String | Main port of the Visit before this Voyage  Either Poma ID or unlocode |
| previous.entryId | String | The previous Visit |
| next.port | String | Destination of Voyage or main port of the next Visit if we already have one  Either Poma ID or unlocode |
| next.entryId | String | The next Visit if we have any |

---

# V0 Definition

## General

In VesselVoyage, each ship has a Story. This Story is built of multiple entries. An entry can be classified under the following categories:

* Visit: A stay at a port.
* Voyage: The travel from and to a Visit.

Depending on where our first ais point of the vessel was found, we are either starting with a Visit or with a Voyage.

## Per event definitions

### PortStartEvent

| **Status** | **Action** |
| --- | --- |
| No State | Create initial Visit. |
| Ongoing Visit | When part of Visit:   * Update ongoing Visit by adding a new PortAreaVisit to `portAreas`.   When not part of Visit:   * Create a new Voyage    + The new Voyage is starting from the ongoing Visit end time (either Port or Anchor) and ending at the PortStartEvent `eventTime`. * Create a new Visit.    + The new Visit is starting at the PortStartEvent `eventTime`. |
| Ongoing Voyage | Start a new Visit, ending the current Voyage. |

### PortEndEvent

| **Status** | **Action** |
| --- | --- |
| No State | Create initial Voyage. |
| Ongoing Visit | When pass through:   * Delete the ongoing visit. * Unfinish the previous Voyage. * Add pass through PortAreaVisit to Voyage.   When not a pass through update the Visit and finish the matching PortAreaVisit.   * When all `portAreas` are finished    + Finish the ongoing Visit.   + Combine any overlapping stops.   + Create a new Voyage. * When not all `portAreas` are finished only update the ongoing Visit. |
| Ongoing Voyage | Ignore event. |

### AnchorStartEvent

| **Status** | **Action** |
| --- | --- |
| No State | Create initial Visit. |
| Ongoing Visit | Add AnchorAreaVisit to ongoing Visit. |
| Ongoing Voyage | * End ongoing Voyage. * Start a new Visit for the port it currently has as its destination. |

### AnchorEndEvent

| **Status** | **Action** |
| --- | --- |
| No State | Ignore event. |
| Ongoing Visit | Replace last matching AnchorAreaVisit endTime with event time. |
| Ongoing Voyage | Ignore event. |

### DestinationChangedEvent

| **Status** | **Action** |
| --- | --- |
| Any State | Update `aisDestination` and `trueDestination` on currently ongoing entry.  Additionally clear the `eta` if not matching the `trueDestination` port. |

### EtaEvent

| **Status** | **Action** |
| --- | --- |
| Any State | Update `eta` if the `destination` on the event is the same as the currently known `trueDestination`. |

### MovementEndEvent

| **Status** | **Action** |
| --- | --- |
| Any State | Create a new stop.  Update the `esof` on the current Visit/Voyage.   * Regroup `esof` distributing it correctly over the current Visit/Voyage and previous visit and previous voyage. |

### MovementStartEvent

| **Status** | **Action** |
| --- | --- |
| Any State | Finish ongoing stop and use as fallback.  Try to find v2 stops using trace of the ship.  When determined as better we use the v2 stops, otherwise the fallback.   * Update the `esof` of the current Visit/Voyage with the better determined stops. * Regroup `esof` distributing it correctly over the current Visit/Voyage and previous Visit and previous Voyage. |

### UniqueBerthStartEvent

| **Status** | **Action** |
| --- | --- |
| No State | Ignore event. |
| Ongoing Visit | Create new BerthAreaVisit and add to ongoing Visit.  Merge current stops with the provided berth event. |
| Ongoing Voyage | Ignore event. |

### UniqueBerthEndEvent

| **Status** | **Action** |
| --- | --- |
| No State | Ignore event. |
| Ongoing Visit | Update the end time of the matching BerthAreaVisit on the ongoing Visit.  Merge current stops with the provided berth event. |
| Ongoing Voyage | Ignore event. |

### EncounterStartEvent

| **Status** | **Action** |
| --- | --- |
| Any State | Create new Encounter if none ongoing for same ships.   * Add new Encounter to `esof`. * Update ongoing Visit/Voyage with new `esof`. * Regroup `esof` distributing it correctly over the current Visit/Voyage and previous Visit and previous Voyage. |

### EncounterEndEvent

| **Status** | **Action** |
| --- | --- |
| Any State | Update end time on the matching Encounter.   * Update `esof` with updated Encounter. * Update ongoing Visit/Voyage with new `esof`. * Regroup `esof` distributing it correctly over the current Visit/Voyage and previous Visit and previous Voyage. |

### StatusChangedEvent

| **Status** | **Action** |
| --- | --- |
| Any State | Only process status MOORED and AT\_ANCHOR.  Ignore event if currently not having an ongoing stop.  Update last ongoing stop `aisType` (and also `type` if we don’t have a `pomaType`)   * MOORED = `StopType.BERTH` * AT\_ANCHOR = `StopType.ANCHOR_AREA`      * Update `esof` with new type * Update ongoing Visit/Voyage with new `esof`. * Regroup `esof` distributing it correctly over the current Visit/Voyage and previous Visit and previous Voyage. |

### Detailed logic

| **Event** | **Check** | **Action** |
| --- | --- | --- |
| PortStartEvent | is part of Visit | Check if part of Visit by matching one of the following checks:   * Check if any Visit `portAreas` `ported` is equal to the PortStartEvent `portId`. * Check if we have any `anchorAreas` but no `portAreas`. * Check if any Visit `portAreas` `outerArea` overlap our PortStartEvent `outerArea`.    + If one of the areas doesn’t have an `outerArea`. Fallback as still matching if the location of the ports are less then `100_000` meters away from each other |
| PortEndEvent | is Visit pass through | Check if the current Visit is a “pass throught“ by checking if all PortAreaVisit.  Mark as not a pass through when matching any:   * Not finished, having no PortAreaVisit `endTime` or `endLocation`. * When we have a stop that started before the PortAreaVisit `endTime` and ended after the PortAreaVisit `startTime` and the stop is not typed as UNCLASSIFIED.   Mark as a pass through when matching any:   * Duration of the PortAreaVisit is less than 30 minutes. * Average speed durating the PortAreaVisit is bigger than 1 meter per second. |
---
id: confluence:194576397
source: confluence
type: page
space: TC
title: 'VesselVoyage: Merging Berth Events and Stops.'
author: Darius Wattimena
date: '2023-07-31'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/194576397
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/194576397
---
# VesselVoyage: Merging Berth Events and Stops.

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/194576397  

## Content

Merging Berth events with Stops is quite tricky to do. This document will explain the planned changes to have the Berth event, and Stops eventually joined. Besides this, a description of how Berth events can be combined with Stops for different scenarios will be included.

## What changes will be made?

Short-term changes:

* The `accuracy` field will be introduced. This field exposes how accurate the Stop is.

  + LOW = Based on movement event only.
  + MEDIUM = After the start movement event, using stop detection mechanism using AIS data.
  + HIGH = Based on Berth events.
  + HIGHEST = Afterwards, on leaving the port, merging related stops.
* Fields will be added to the Stop for the `BerthStartEvent`:

  + `berthStartEventId`
  + `berthStartEventTime`
  + `berthStartEventLocation`
* Fields will be added to the Stop for the `BerthEndEvent`:

  + `berthEndEventId`
  + `berthEndEventTime`
  + `berthEndEventLocation`
* Berth events and Stops will be merged.

Long-term changes:

* Decouple processing and API parts for robustness purposes.
* We don’t use movement start/stop events as the source for stop detection. Instead, a new event will be introduced in AisEngine that will detect a Stop with much higher accuracy.

## How will Berth events and Stops be merged?

|  | **Scenario** | **On a** `UniqueBerthEvent` **start event** | **On a** `UniqueBerthEvent` **end event** |
| --- | --- | --- | --- |
| 1 | The Visit has no Stops. | The event will create a new Stop, using the `eventTime` and `location` of the `UniqueBerthEvent` as the stops `startTime` and `startLocation`, respectively. | Create a new Stop using the V2 mechanism to determine the Stop `startTime`, `startLocation` and use the `UniqueBerthEvent`for the `endTime` and `endLocation`. |
| 2 | When there is only a single Stop on the Visit, and still ongoing. | If we didn’t receive a start event yet, update the `berthStartEvent` fields. Search the related berth using Poma so we can fill the `pomaId`, `name`.    When we already received a `BerthStartEvent`:   * Create a new Stop if the event is not the same Berth. Finish the ongoing Stop. * Drop the event if for the same Berth. | Drop the event when the stop is not related to event.    Finish the stop and update the `berthEndEvent` fields for the following case:   * When already received start event for Stop * When no event start event is ever received |
| 3 | When the single Stop on the Visit is already finished. | Create a new Stop if the finished Stop is not the same Berth.  Otherwise, unfinish the Stop when no `movementStartEventId` was found. We can assume some jitter happened, resulting in an unexpected berth start and end event.  When there is a `movementStartEventId` on the Stop, create a new Stop instead. Assuming the vessel moved away from the Berth but came back. | When the Stop is of a different Berth or when the time between the berth end events is *too long*. Create a new Stop and calculate the `startTime` using the V2 mechanism.  Otherwise drop the event. |
| 4 | When there are multiple Stops on the Visit, but the latest is ongoing. | Check if the start event is related to a finished stop. Update the `berthStartEvent` fields from the event. When already set instead drop the event.  When not matching, handle the ongoing Stop like Scenario #2. | Check if the end event is related to a finished Stop. Update the `berthEndEvent` fields from the event. When already set instead drop the event.  When not matching, handle the ongoing Stop like Scenario #2. |
| 5 | When there are multiple Stops on the Visit, but all are already finished. | Check if the start event is related to a stop. Update the `berthStartEvent` fields from the event. When already set instead drop the event.  When not overlapping, handle the same way as Scenario #1 by creating a new Stop. | Check if the end event is related to a finished Stop. Update the `berthEndEvent` fields from the event. When already set instead drop the event.  When not overlapping, handle the same way as Scenario #1 by creating a new Stop. |

---

## Envision meeting notes

- Berth events including:
- Merge v2 stops
- Real-time part
- Should we expose stops if there are berth events?
- Can we make a stop more accurate earlier ?
- Should we change movement start/stop events as a source for stop detections?
- AisEngine monitor startStopVisit
- Should we trigger v2 maybe earlier (2 hrs after arrival?)
- For non-berth info, probably yes
- Should we expose more clearly how accurate our assessment is?
- yes
- Start scheduling the processing / API split for robustness purposes
v1: start/stop on stop moving - low
v2: afterwards on start moving - medium
------------------------------------------------------------------------
v3: Berth events - high
v4: Afterwards on leaving the port, merging related stops - highest
- stop1 - anchor
- stop2 - unknown
- stop3 - berth
pre-berth:
berth - accuracy: high/medium/low
post-berth:
- stop4 - unknown
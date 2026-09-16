---
id: confluence:223805441
source: confluence
type: page
space: TC
title: Ship stop event
author: Former user (Deleted)
date: '2024-03-11'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/223805441
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/223805441
---
# Ship stop event

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/223805441  

## Content

# Problem

We currently don’t have an event where we can easily detect on a real-time basis if a ship fully stopped. While we do have the MovementEvent, it does limit itself on speed. In VesselVoyage, a correction mechanism was built to have more accurate stops at the berth. This is, however, one of the few use cases where we want to detect the stopping behaviour of a vessel.

note

Slow steaming is not seen as the stopping of a vessel, thus not part of the problem.

Slow steaming is not seen as the stopping of a vessel, thus not part of the problem.

## Use cases

We would like to have an event (or multiple events) to cover the following situations:

### Case 1: Stops where the vessel is typically lying very still

* Berth stop
* Vessel rotations at a Turning basin (Zwaaikom)
* Lock stop
* Unclassified stop in port

**Challenges**

* Distinguish between natural movement and AIS jitter.
* How to determine accurate stop times.
* When to combine stops?

### Case 2: Stops where the vessel typically still has relevant movement

* Anchor stop
* Board-board operations (both at anchorage and open sea, floating hose)
* Unclassified stop at open water

**Challenges**

* How to deal with limited AIS coverage?
* What is the minimum stop time relevant to be seen relevant?
* When to combine stops? (e.g. drifting between anchor locations)

---

# Solution

## General Idea

To detect multiple types of stops, we’ve decided to create two levels of events. Here, level 1 will be a basic event, which is similar to a movement event. However, the boundaries are set quite strict. A more in-depth level 2 event will be created to cover the situations we want to be able to detect. You could see this mechanism similar to how the BerthEvent is the basis for the ConfirmedBerthEvent work.

## The Basic Event

The basic event will be the backbone of the events created later. This event will not be saved in our EventHistory as we foresee it will be triggering quite often as the conditions will be much lower than the existing MovementEvent.

The start condition:

* The ship’s speed is below … knots

The end condition:

* The ship’s speed is above … knots

## The Detailed Events

The detailed event will be a follow-up of the basic event. We mainly focus on providing an event for the situations we want to solve. We foresee that the more detailed events need more than speed to detect events. So, the location and time will also be used to make the detailed events possible.

### Ship “Not Moving” Event

This event will cover the situation where we want to detect when a ship is entirely stopped, not moving at all.

The start condition:

* We received a basic event indicating that we stopped moving
* We stayed around the same location
* We didn’t receive a basic event indicating that we started moving after … minutes

The end condition:

* We received a basic event indicating that we started moving
* We moved away from the start location, travelling … meters
* We have been moving for … minutes

## Samples

1. Normal case

   1. <https://vesselvoyage.teqplay.nl/#/ships/9514755/story/f4895d54-4869-4cae-94bf-b87c5271fe7e.VISIT> <https://timeline.teqplay.nl/255802790?selectedTime=1709546400000&URL=https%3A%2F%2Finternalapidev.teqplay.dev%2Fv0&from=1709546400000&to=1709953200000> 1 anchor stop, 9 berth stops
2. Turning basin

   1. <https://timeline.teqplay.nl/211866090?selectedTime=1660655254000&URL=https%3A%2F%2Finternalapidev.teqplay.dev%2Fv0&from=1660649400000&to=1660658400000> 2022-08-16 13:07:34
3. Turning before entering berth (turning should be a separate stop)

   1. <https://timeline.teqplay.nl/228401800?selectedTime=1710086400000&URL=https%3A%2F%2Finternalapidev.teqplay.dev%2Fv0&from=1710086400000&to=1710093600000> 2024-03-10 16:15
   2. <https://vesselvoyagedev.teqplay.nl/#/ships/9229300/story/a5685c2f-918b-459f-95ac-af3f100e5bb5.VISIT> <https://timeline.teqplay.nl/636017173?selectedTime=1710126000000&URL=https%3A%2F%2Finternalapidev.teqplay.dev%2Fv0&from=1710126000000&to=1710133200000> 2024-03-11 03:40
   3. <https://vesselvoyagedev.teqplay.nl/#/ships/9619957/story/3d30aa33-d4fb-4856-afca-071f7f6499ad.VISIT> <https://timeline.teqplay.nl/219018986?selectedTime=1709931511274&URL=https%3A%2F%2Finternalapidev.teqplay.dev%2Fv0&from=1709924400000&to=1709931600000> 2024-03-08 19:20
4. Lock

   1. <https://timeline.teqplay.nl/205269790?selectedTime=1690848780918&URL=https%3A%2F%2Finternalapidev.teqplay.dev%2Fv0&from=1690833600000&to=1690849800000> stops before and inside lock (2x)
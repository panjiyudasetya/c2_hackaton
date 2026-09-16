---
id: confluence:688488449
source: confluence
type: page
space: TC
title: Area Occupancy Component
author: Darius Wattimena
date: '2025-05-02'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/688488449
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/688488449
---
# Area Occupancy Component

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/688488449  

## Content

# Area Occupancy Component

## Overview

The Area Occupancy component is designed to track vessel movements in and out of predefined areas. It maintains records of each ship's entry and exit events and periodically generates snapshots of vessel presence in these areas.

## Objective

The Area Occupancy component solves the following objects:

1. Being able to give the occupancy of an area with all the ships in this area.
2. Provide an API where you can request this occupancy by area.

## Features

* **Area Occupancy Tracking:** Each ship entering and exiting is tracked per area, generating an AreaVisit entry which will be persisted for each ship entering and exiting an area.
* **Realtime Events:** To track area occupancy area events will be consumed from our realtime event feed.
* **Snapshot Generation:** Periodic snapshots of vessels present in the area are taken, providing an “overview“ of the occupancy at that time.

  + MVP Scoped outRed **Tracking Ship Location:** Knowing where the ship currently is when taking the area occupancy is key to do further calculations. Especially for areas such as berths this can be very useful.
* **Snapshot Publishing:** Snapshots are published to PTO via RabbitMQ.
* **Historical Data Retrieval:** An API is provided for Timeline to fetch AreaVisits within a specified time window.
* **Recalculation:** Occupancy should be very flexible and being able to regenerate data easily. This is needed to support more than just real-time area occupancy, but also backfill older data.

  + **Area Visit Regeneration:** Being able to recalculate all AreaVisits for a single area.

    - **Real-time Based:** Events are taking from EventHistory to regenerate all AreaVisit.
    - MVP Scoped outRed **Revents Based:** When updates on areas are being made, use revents to regenerate any area and calculate ship and area occupancy.
  + **Occupancy Correcting:** After the vessel is either filtered out or historic data is recalculated, the already generated snapshots should be invalidated and new data based on the new occupancy should be published to PTO.
* MVP Scoped outRed **Occupancy Filtering:** Events alone aren’t the most reliant source of data. Because of this there are cases where ships (like “Ghost Vessels”) can enter a berth, get a single AIS point and never leave. This would skew the area occupancy. Because of this, unreasonable area occupancies are being filtered out after not receiving any AIS for said vessel for a configurable amount.

This component will NOT make it possible to ask area occupancy for a ship but only resolving them by area.

The user should instead use the EventHistory component if they want to know all areas a ship is currently occupying.

## Occupancy Filtering

The occupancy will be filtered out when a ship has no AIS for x amount of days. This value will be configurable per area.

Once the ship is marked to be filtered out, the ship is removed from the area occupancy.

note

The following values are not set in stone, they are still up for discussion. The values should be based on the coverage of the port eventually?

The following values are not set in stone, they are still up for discussion. The values should be based on the coverage of the port eventually?

| **Area** | **Max days no AIS** |
| --- | --- |
| Port | 14 |
| Terminal | 7 |
| Berth | 7 |
| Anchor | 14 |
| Any other area | 14 |

## Default use cases

### Default Case 1: Ship enters berth, snapshot is taken and leaves berth

Steps:

1. Ship enters berth, AreaVisit is created.
2. Snapshot is taken in the specified interval, in the example 2 ships would be found for this area.
3. Ship leaves berth, AreaVisit is finished.
4. The specified interval of snapshots triggers again, ship left the area so only the remaining ship will be found for the area occupancy.

Overview

Timeline

note

You can be in multiple areas at the same time when they overlap. Meaning we can be in a Berth, Terminal and Port all at the same time.

You can be in multiple areas at the same time when they overlap. Meaning we can be in a Berth, Terminal and Port all at the same time.

## Exceptional use cases

### Case 1: Ship enters berth, bad AIS signal and jitters out of the berth

Steps:

1. Ship enters berth, AreaVisit is created.
2. Snapshot is taken in the specified interval, in the example 2 ships would be found for this area.
3. Ship leaves berth because of jitter, AreaVisit is finished.
4. Snapshot is taken, only 1 ship will be reported for this area as other ship jittered out.
5. Ship jitters back into area, new AreaVisit is created.
6. Snapshot is taken, now including both ships again.
7. Ship leaves berth, AreaVisit is finished.

Overview

Timeline

### Case 2: Ship enters berth but physically ship overlaps multiple berths

Steps:

1. Ship enters berth, AreaVisit is created.
2. Snapshot is taken in the specified interval, only area occupancy of middle berth the big ship is found for. The right berth has no ships in their occupancy.
3. Ship moves out of the berth, AreaVisit is finished.
4. Snapshot is taken but without any occupancy, ship is in neither the middle or right berth.
5. Ship enters right berth, AreaVisit is created.
6. Ship leaves right berth, AreaVisit is finished.

Overview

Timeline

### Case 3: Ship enters berth, switches MMSI

Steps:

1. Ship enters berth, AreaVisit is created.
2. Snapshot is taken in the specified interval, in the example 2 ships would be found for this area.
3. AIS adapter is switched off.
4. Snapshot is made, still having 2 ships in this area.
5. New AIS adapter is showing, a new ship is inside area, **NO** AreaVisit is created.
6. Snapshot is made, still 2 ships in this area, but with the old AIS adapter.
7. Snapshot is made some time later, blue ship is now filtered out as the last time we received AIS from this ship is above the filtering threshold. This means only the 1 ship (the green one) will be taken into account for the occupancy.
8. Purple ship leaves berth, nothing is done.

Overview

Timeline

note

This case has quite some technical limitations. Different approaches could be possible but it would either result in heavy computing on the side of the AreaOccupancy component or a whole different approach of how the AreaMonitor works.

This case has quite some technical limitations. Different approaches could be possible but it would either result in heavy computing on the side of the AreaOccupancy component or a whole different approach of how the AreaMonitor works.

### Case 4: Ships are next to each other in the same berth

Steps:

1. Ship enters berth, AreaVisit is created.
2. Snapshot is taken in the specified interval, 2 ships are reported in this area for the occupancy. The occupancy is only based on the amount of vessels inside the area, not based on what position each ship is currently in.
3. Ship leaves berth, AreaVisit is finished.
4. The specified interval of snapshots triggers again, ship left the area so only the remaining ship will be found for the area occupancy.

Overview

Timeline

---

## Data Models

### AreaVisit

| **Field** | **Type** | **Note** |
| --- | --- | --- |
| \_id | String | Unique ID, reused event ID from start event. |
| area | String | Poma ID |
| type | AreaType (enum) | AisEngine area type (directly taken from AreaEvent) |
| start | Timestamp | Time of entering the area (AreaStartEvent actual time) |
| end | Timestamp | Time of exiting the area (AreaEndEvent actual time) |
| source | Enum | Indicator how this area visit came to be. (`RealTime` or `Recalculation`) |
| vessel | Vessel | Vessel object including CSI identifier and AIS MMSI |

### Vessel

| **Field** | **Type** | **Note** |
| --- | --- | --- |
| id | String | CSI identifier |
| mmsi | Int | AIS MMSI |

### AreaOccupancy

| **Field** | **Type** | **Note** |
| --- | --- | --- |
| area | String | Poma ID |
| type | AreaType (enum) | AisEngine area type |
| ships | Collection of Vessels | Vessel object including CSI identifier and AIS MMSI |
| timestamp | Timestamp | UTC ISO when this area occupancy was generated |
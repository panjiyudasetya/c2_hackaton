---
id: confluence:567541842
source: confluence
type: page
space: TC
title: Area Status Service
author: Richard van Klaveren
date: '2024-12-10'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/567541842
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/567541842
---
# Area Status Service

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/567541842  

## Content

Areas within Teqplay are being monitored by the area monitor component of the Ais Engine with the focus on real-time detections in a streaming environment. However, the actual and historical state of areas currently is not exposed or accessible anywhere for external use.

For the long-term approach, it is clear that such status information should be made available in the Data Platform, however, the Data Warehouse is not guaranteed to be real-time up-to-date. There is a clear requirement to get actual and recent area history (e.g. in the context of current anchor place monitoring) So, the need for a new service is born, let’s call it for now the `AreaStatus` service.

## Requirements

For this service, we see the following roles / requirements:

1. Provide real-time actual `area status`
2. Provide recent (5 days) `area status`
3. Provide any visit to an area that started (also long time ago) but is not finished yet (?)
4. Should be possible to run real-time and based on (r)events
5. Should be possible to query per area and for all areas related to a port

The roles of the Data warehouse in this area would then be:

1. Share long-term visits per area
2. Share KPI like information allowing to make an assessment on whether actual status is normal, more busy, less busy

## Area Status

In above statements we’re referring to a `areaStatus`. So, we consider following data fields relevant part of such `areaStatus`:

* **Area Id:** basically the Poma Id of the area
* **Area Type:** The type of the area being monitored, supporting all area types in PoMa, but e.g. Port inner area, Port  EOS, Anchor, Terminal, Berth.
* **Vessels inside:** for the vessels inside, we want to collect following information

  + Id: IMO / MMSI / CSI Id
  + Stopped: A flag indicating whether the vessel also stopped in the area. This can be used to distinguish between those vessels that actually anchored / berthed or passed through the area.
  + Duration inside (startTime + endTime): The duration that the vessel is already inside the area, including the startTime when the vessel entered the area and (if applicable) the endTime when the vessel left the area again.
  + Cargo category: The cargo category of the vessel (e.g. TANKER, CONTAINER, BULK, …)
  + DWT (category): The DWT of the vessel or in case of a container vessel the TEU, based on CSI
  + [Link to VesselVoyage Visit + stop]: In the case of a vessel included in Vesselvoyage: A link to VesselVoyage detected Visit and Stop, to allow fast tracing where the vessel came from etc.

## Overview

The AreaStatus service is embedded within the Teqplay architecture as depcited in the image below and has 2 main functionalities:

1. State Updater: receiving incremental updates based on (mostly) area events from the AreaMonitor. Based on such events a consistent state can be calculated and presented to the users of the service. The state updater is responsible for maintaining and persisting such state, and apply fixes where the area events are contradicting each other (e.g. entering the same area twice without exiting the area or so).
2. State Validator: The risk of parsing only incremental updates is that upon failure of one of the components in the chain an inconsistent state will be created. The role of the state validator is to validate if the state is still correct and consistent, and to fix the state if not consistent anymore. An example could be: vessels switching of their AIS transponder in an area and switching a new AIS transponder with different id outside the area. If there would be no state validator, there is a risk this will never be noticed. The state validator will run at very low frequency, e.g. checking all areas once per week.

The idea would be that AreaStatus component will only have limited history, just enough to guarantee overlap with the timeframe covered by the data platform. The AreaStatus component should be able to run as well based on (r)events, at least to initially fill the status of the AreaStatus for areas newly added to PoMa. Also, it is not foreseen yet to be a service hosting predictions on future areaStatus.

It was briefly discussed if this component should be combined with other services like the service keeping state of the TugStatus or so, but it was agreed that this should be a small service with a clear scope.
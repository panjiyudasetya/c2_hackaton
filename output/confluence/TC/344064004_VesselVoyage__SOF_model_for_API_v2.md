---
id: confluence:344064004
source: confluence
type: page
space: TC
title: 'VesselVoyage: SOF model for API v2'
author: Leon Joosse (Unlicensed)
date: '2024-06-10'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/344064004
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/344064004
---
# VesselVoyage: SOF model for API v2

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/344064004  

## Content

VesselVoyage V2 API the Statement Of Facts view on a visit. This SOF model denotes facts more explicitly than the visit. The aim is that the consumer has to do as less calculations on the data as possible.

A SOF is based on a VesselVoyage visit, using the end-of-sea-passage (EOSP) as boundaries. It starts when the ship enters the EOSP and ends when the ship departs from the EOSP.

Supporting classes, such as `LocationTime`, are described below the model table.

## Definition

| **Field** | **Type** | **Note** |
| --- | --- | --- |
| version | Int | SOF generator version |
| generationId | String / Uuid | Generation id, for future use when other products will use versioning |
| id | String | Unique ID for this SOF. This is usually the visit where this SOF is based on |
| start | LocationTime | EOSP start |
| end | LocationTime | EOSP end |
| **area** | Area | Details on the EOSP area, following the POMA definition |
| area.id | String | EOSP area id |
| area.unlocode | String | EOSP main port name, e.g. `NLRTM` |
| area.name | String | EOSP name, e.g. `PORT OF ROTTERDAM` |
| area.type | String | `END_OF_SEA_PASSAGE` |
| **ship** | Ship | The ship where this SOF is about, following the entry from CSI |
| ship.type | String | Ship type, e.g. `TANKER` |
| ship.imo | Int |  |
| ship.name | String |  |
| **pilotInbound** | Pilot | Last pilot before the first berth visit, or null if there was no pilot encounter. Note that these may happen outside pilot areas.  Other pilot encounters are available in the `encounters` list, where `type=PILOT`. |
| pilotInbound.start | LocationTime |  |
| pilotInbound.end | LocationTime |  |
| pilotInbound.**ship** | Ship | The pilot ship |
| pilotInbound.ship.imo | Int? | Be aware that a pilot does not always have an IMO number |
| pilotInbound.ship.mmsi | Int? | Be aware that a pilot does not always have an MMSI number |
| pilotInbound.name | String |  |
| pilotInbound.**area** | Area? | The pilot area details, following the POMA definition.  Null if the pilot inbound did not took place in a pilot area |
| pilotInbound.area.id | String |  |
| pilotInbound.area.name | String |  |
| pilotInbound.area.type | String | `PILOT` |
| **pilotOutbound** | Pilot? | Last pilot before the first berth visit, or null if there was no pilot encounter. Note that these may happen outside pilot areas.  Other pilot encounters are available in the `encounters` list, where `type=PILOT`. |
| pilotOutbound.start | LocationTime |  |
| pilotOutbound.end | LocationTime |  |
| pilotOutbound.**ship** | Ship | The pilot ship |
| pilotOutbound.ship.imo | Int? | Be aware that a pilot does not always have an IMO number |
| pilotOutbound.ship.mmsi | Int? | Be aware that a pilot does not always have an MMSI number |
| pilotOutbound.name | String |  |
| pilotOutbound.**area** | Area? | The pilot area details, following the POMA definition.  Null if the pilot inbound did not took place in a pilot area |
| pilotOutbound.area.id | String |  |
| pilotOutbound.area.name | String |  |
| pilotOutbound.area.type | String | `PILOT` |
| **anchorVisits** | List<AnchorVisit> | List of anchor visits, where the ship stopped at least once |
| anchorVisits[\*].portAreaRef |  | The port area where this anchor area is part of. Use this reference to look-up the port area from the `portArea[*].ref` list |
| anchorVisits[\*].start | LocationTime |  |
| anchorVisits[\*].end | LocationTime |  |
| anchorVisits[\*].area | Area | The anchor area details, following the POMA definition |
| anchorVisits[\*].area.id | String | The area id, |
| anchorVisits[\*].area.name | String |  |
| anchorVisits[\*].area.type | String | `ANCHOR` |
| **portAreas** | List<PortArea> | List of port area that the ship visited or sailed through inside the EOSP.  Note: an entry for one port may occur multiple times, for example once for entering and one for departing. Such as at Hamburg, where port DESTA is in the canal leading to Hamburg: |
| portAreas[\*].ref | Int | A unique reference for this portArea.  If a port appears multiple times, as explained with the DESTA example here above, then both get a unique reference number. |
| portAreas[\*].isPassThrough | Boolean | Whether the ship only passed through this port area. True when the ship never made a stop in this port area, thus only passed through. False when the ship made at least one stop in this port area. |
| portAreas[\*].start | LocationTime |  |
| portAreas[\*].end |  |  |
| portAreas[\*].**area** | Area | The port area details, following the POMA definition.  Note that this is the port inner area (not the EOSP!). |
| portAreas[\*].area.id |  |  |
| portAreas[\*].area.unlocode |  |  |
| portAreas[\*].area.name |  |  |
| portAreas[\*].area.type |  | `PORT` |
| **berthVisits** | List<BerthVisit> | The list of berth visits that happened in the EOSP.  All berth visits are always linked to a port area. Use `portAreaRef` to match to `portAreas[*].ref`.  A berth visit may be linked to a terminal visit, if the berth has a `terminalId` set. Use `terminalVisitRef` to match to `terminalVisits[*].ref`. |
| berthVisits[\*].ref | Int | Unique reference for this berth visit (within this statement of facts) |
| berthVisits[\*].terminalVisitRef | Int? | If this berth has a `terminalId` set, this is the terminal visit, otherwise null. This refers to `terminalVisits[*].ref` |
| berthVisits[\*].portAreaRef | Int | This port area where this berth visit took place.  This refers to `portAreas[*].ref` |
| berthVisits[\*].**visit** | BerthVisitInfo | Details on the visit |
| berthVisits[\*].visit.start | LocationTime | Ship enters the berth area |
| berthVisits[\*].visit.firstLineSecured | LocationTime? | On arrival at the berth, the first tug arrives |
| berthVisits[\*].visit.allFast | LocationTime? | On arrival at the berth, the last tug departs |
| berthVisits[\*].visit.lastLineReleased | LocationTime? | On departure from the berth, the last tug departs This may also be known as ‘waiting for departure’ |
| berthVisits[\*].visit.end | LocationTime | Ship exits the berth area |
| berthVisits[\*].**berth** | BerthInfo | Details on the berth, following the POMA definition |
| berthVisits[\*].berth.id | String |  |
| berthVisits[\*].berth.name | String |  |
| berthVisits[\*].berth.cargoType | List<String> | Cargo types as defined in POMA, such as `["CONTAINER"]` |
| berthVisits[\*].berth.mooringType | String | Mooring type as defined in POMA, such as `QUAY` |
| berthVisits[\*].berth.terminalId | String? |  |
| berthVisits[\*].isCargoOperation | String | Whether a cargo operation is **likely** taking place at this berth.  `YES`: the `berth.cargoType` and `ship.type` match; e.g. a `CONTAINER` berth and `CONTAINER` ship. A ship usually moors at a suitable berth to do a cargo operations, so the system assumes that is the case.  `NO`: the `berth.cargoType` and `ship.type` match  Other values are possible in the future. |
| berthVisits[\*].**arrivalTugs** | List<Tug> | List of tugs supporting the ship’s berth arrival |
| berthVisits[\*].arrivalTugs[\*].**ship** | TugInfo | Tug info, as defined in CSI |
| berthVisits[\*].arrivalTugs[\*].ship.imo | Int? | A tug has at least an IMO or an MMSI |
| berthVisits[\*].arrivalTugs[\*].ship.mmsi | Int? | A tug has at least an IMO or an MMSI |
| berthVisits[\*].arrivalTugs[\*].ship.name | String |  |
| berthVisits[\*].arrivalTugs[\*].start | LocationTime |  |
| berthVisits[\*].arrivalTugs[\*].end | LocationTime |  |
| berthVisits[\*].**departureTugs** | List<Tug> | List of tugs supporting the ship’s berth departure |
| berthVisits[\*].departureTugs[\*].**ship** | TugInfo | Tug info, as defined in CSI |
| berthVisits[\*].departureTugs[\*].ship.imo | Int? | A tug has at least an IMO or an MMSI |
| berthVisits[\*].departureTugs[\*].ship.mmsi | Int? | A tug has at least an IMO or an MMSI |
| berthVisits[\*].departureTugs[\*].ship.name | String |  |
| berthVisits[\*].departureTugs[\*].start | LocationTime |  |
| berthVisits[\*].departureTugs[\*].end | LocationTime |  |
| **terminalVisits** | List<TerminalVisit> | The list of terminal visits that happened in the EOSP.  A terminal visit is composed of 1 or more berth visits. Berth visits links to a terminal visit, matching `berthVisit.terminalVisitRef` to `terminalVisit.ref`. Only passing through the terminal area or terminal mooring area will not generate a terminal visit.  The system finds adjacent berth visits where the `berth.terminalId` are the same. Those adjacent berth visits make up the terminal visit. A terminal visit always takes place in 1 port area, as a terminal is supposed to be in 1 port area.  All terminal visits are always linked to a port area. Use `portAreaRef` to match to `portAreas[*].ref`. |
| terminalVisits[\*].ref | Int | Unique reference for this terminal visit (within this statement of facts) |
| terminalVisits[\*].portAreaRef | Int | The port area where this berth visit took place. This refers to `portAreas[*].ref` |
| terminalVisits[\*].**visit** |  |  |
| terminalVisits[\*].visit.start | LocationTime | Terminal visit start, essentially the `start` of the first berth visit within this terminal visit |
| terminalVisits[\*].visit.end | LocationTime | Terminal visit end, essentially the `end` of the last berth visit within this terminal visit |
| terminalVisits[\*].visit.mooringStart | LocationTime | When the ship entered the `terminal.mooring` area (this area is defined in poma) |
| terminalVisits[\*].visit.mooringEnd | LocationTime | When the ship left the `terminal.mooring` area (this area is defined in poma) |
| terminalVisits[\*].**terminal** | TerminalInfo | Details on the terminal, following the POMA definition |
| terminalVisits[\*].terminal.id | String |  |
| terminalVisits[\*].terminal.name | String |  |
| terminalVisits[\*].terminal.type | String | `TERMINAL` |
| **lockVisits** | List<LockVisit> | Locks encountered within the EOSP. **This is not implemented yet** |
| lockVisits[\*].portAreaRef | Int? | The port area ref, when this lock is part of a port area. This refers to `portAreas[*].ref` |
| lockVisits[\*].start | LocationTime |  |
| lockVisits[\*].end | LocationTime |  |
| lockVisits[\*].**lock** | LockInfo | Details on the lock, following the POMA definition |
| lockVisits[\*].lock.id | String |  |
| lockVisits[\*].lock.name | String |  |
| lockVisits[\*].lock.type | String | `LOCK` |
| **approachAreas** | ApproachArea |  |
| approachAreas[\*].portAreaRef | Int? |  |
| approachAreas[\*].approachArea | ApproachAreaInfo |  |
| approachAreas[\*].approachArea.id | String |  |
| approachAreas[\*].approachArea.name | String |  |
| approachAreas[\*].approachArea.type | String |  |
| approachAreas[\*].start | LocationTime |  |
| approachAreas[\*].end | LocationTime |  |
| **unclassifiedStops** | List<UnclassifiedStop> | A stop inside the EOSP that couldn't be classified as anchor, pilot, berth or terminal visits. May be caused by a missing definition in POMA, or there is simply no area to be defined at that place. |
| unclassifiedStops[\*].portAreaRef | Int? | When the stop happened inside a portArea |
| unclassifiedStops[\*].start | LocationTime |  |
| unclassifiedStops[\*].end | LocationTime |  |
| **encounters** | List<EncounterInfo> | List of other ships encountered inside the EOSP, such as pilots, bunkers, tugs and other service vessels. |
| encounters[\*].type | String | Type of encounter. This is not necessarily the type of the ship.  Possible values: AUTHORITY BARGE\_BUNKER BOATMEN BUNKER CARGO\_BARGE CRANE FENDER LUBES PILOT PUSH\_BARGE SUPPLY\_BARGE SWOG TANKER\_BARGE TENDER TUG TUG\_WAITING\_FOR\_ARRIVAL TUG\_WAITING\_FOR\_DEPARTURE WASTE WATER WATER\_BARGE UNCLASSIFIED |
| encounters[\*].**ship** | Ship | The encountered ship, following the entry from CSI |
| encounters[\*].ship.imo | Int? | Be aware that a pilot does not always have an IMO number |
| encounters[\*].ship.mmsi | Int? | Be aware that a pilot does not always have an MMSI number |
| encounters[\*].ship.name | String |  |
| encounters[\*].ship.type | String | One of the ship types, as defined in CSI |
| encounters[\*].start | LocationTime |  |
| encounters[\*].end | LocationTime |  |
| encounters[\*].berthVisitRef | Int? | If this took place during a berth visit, referring to `berthVisit.ref` |
| encounters[\*].terminalVisitRef | Int? | If this took place during a terminal visit, referring to `terminalVisit.ref` |
| encounters[\*].portAreaRef | Int? | If this took place during inside a port area, referring to `portArea.ref` |

### **LocationTime** model

The `LocationTime` model is frequently used in the SOF. When something happens, it always happens at a place. Therefore we combine this into the `LocationTime` object.

| **Field** | **Type** | **Note** |
| --- | --- | --- |
| location.lat | Float | Location latitude |
| location.lon | Float | Location longitude |
| time | String | ISO 8601 datetime. Always in UTC.  Example: `2024-05-26T09:08:52Z` |
| fallback | String? | When this LocationTime was not recorded in the system in the normal way, the event can sometimes be derived. This field indicates which fallback method was used to derive this LocationTime.  For example: when the ship exits the EOSP, all open activities need to end, as that is the boundary for this statement of facts. Normally, the system would receive end events for open activities. But when missing them, the system will take the EOSP end as end of all open activities in the SOF. |
---
id: confluence:133529608
source: confluence
type: page
space: TC
title: NATS event subjects
author: Darius Wattimena
date: '2022-08-16'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/133529608
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/133529608
---
# NATS event subjects

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/133529608  

## Content

This document will explain how the NATS subject of each event will be. Some basic rules will be followed so each event subject will be the same.

* The subject of an event will be fully lowercased.
* multi-word part of the subject will be written in *kebab-case.*
* each part of the subject will be separated by a dot.

With the following two rules in mind, the following order will be followed:

`event.<event-type>.<event-sub-type>.<area-type>.<area-identifier>`

| **Subject part** | **Occurence** | **Note** |
| --- | --- | --- |
| event | Always | Prefix of the subject that will always be `event` |
| event-type | Always | The base type of the event. For example `area` or `prediction` |
| event-sub-type | If applicable | The sub-type of the event. For example `start`/`stop` or `end`. For the Ais lost/recover events it can be `lost` or `recover`. |
| area-type | Only area based | Any of the `AreaType` that are stated in the `AreaIdentifier`. For example `port` or `pilot-boarding-place` |
| area-identifier | Only area based | Unique identifier of the area. This will be the UUID provided by PoMa. When not available the value will be defaulted to `unknown` |

Applying all this will make us have the following list of subjects:

| **Event** | **Subject** |
| --- | --- |
| `AisDestinationChangedEvent` | `event.ais-changed.destination` |
| `AisDraughtChangedEvent` | `event.ais-changed.draught` |
| `AisEtaChangedEvent` | `event.ais-changed.eta` |
| `AisStatusChangedEvent` | `event.ais-changed.status` |
| `AreaStartEvent` | `event.area.start.<area-type>.<area-identifier>` |
| `AreaEndEvent` | `event.area.end.<area-type>.<area-identifier>` |
| `ConfirmedBerthStartEvent` | `event.berth-confirmed.start.<area-type>.<area-identifier>` |
| `ConfirmedBerthEndEvent` | `event.berth-confirmed.end.<area-type>.<area-identifier>` |
| `UniqueBerthStartEvent` | `event.berth-unique.start.<area-type>.<area-identifier>` |
| `UniqueBerthEndEvent` | `event.berth-unique.end.<area-type>.<area-identifier>` |
| `EncounterStartEvent` | `event.encounter.start.<encounter-type>`  `event.encounter.end.<encounter-type>`  *Note: This event has two sub-types to make it possible to subscribe on the encounter type or start/end. For example it is needed to request* `event.encounter.*.tug` or `event.encounter.start.*` |
| `EncounterEndEvent` |
| `ShipMovingStartEvent` | `event.ship-moving.start` |
| `ShipMovingEndEvent` | `event.ship-moving.end` |
| `SpeedChangedEvent` | `event.ship-speed-changed.accelerating` or `event.ship-speed-changed.slowing-down` |
| `TrueDestinationChangedEvent` | `event.true-changed.destination` |
| `AisLostEvent` | `event.ais.lost` |
| `AisRecoverEvent` | `event.ais.recover` |
| `AnchoredStartEvent` | `event.anchored.start.<area-type>.<area-identifier>` |
| `AnchoredEndEvent` | `event.anchored.end.<area-type>.<area-identifier>` |
| `EtaEvent` | `event.prediction.eta.<area-type>.<area-identifier>` |
| `EtdEvent` | `event.prediction.etd.<area-type>.<area-identifier>` |
| `LockEtaEvent` | `event.prediction.lock-eta.<area-type>.<area-identifier>` |
| `LockEtdEvent` | `event.prediction.lock-etd.<area-type>.<area-identifier>` |
| `PortcallPilotBoardingEtaEvent` | `event.prediction.portcall-pilot-boarding-eta.<area-type>.<area-identifier>` |
| `AtaEvent` | `event.actual.ata.<area-type>.<area-identifier>` |
| `AtdEvent` | `event.actual.atd.<area-type>.<area-identifier>` |
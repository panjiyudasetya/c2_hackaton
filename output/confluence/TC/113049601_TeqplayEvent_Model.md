---
id: confluence:113049601
source: confluence
type: page
space: TC
title: TeqplayEvent Model
author: Joost Dambrink (Unlicensed)
date: '2025-01-09'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/113049601
explicit_links:
- jira:ISO-8601
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/113049601
---
# TeqplayEvent Model

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/113049601  

## Content

The original proposal by Jos:

* Document - <https://docs.google.com/document/d/1pDVd3I3q4uPAUUrMVPpe9pxqh-MuC3xvZP_m5D5pBEo/edit>
* Presentation - <https://docs.google.com/presentation/d/1u2i1FwT8rUFMcr5E93qzfPpRE68qRyaHy3gZMcuK5mk/edit#slide=id.p>
* Proof of Concept - <https://bitbucket.org/teqplay/platform/src/f8ef629628413b12679a11e7d7ca841adc52bd14/platform/src/main/java/nl/teqplay/experiment/TeqplayEventProposal.kt?at=feat/teqplayevent_data_model_proposal>

Links to the new implementations:

* Teqplay Events PR - <https://bitbucket.org/teqplay/ais-engine/pull-requests/49>
* Teqplay Prediction Events PR - <https://bitbucket.org/teqplay/ais-engine/pull-requests/50>

---

## Event timestamps

* All timestamps will be typed as an `Instant`. We don't want to use a `long`. Timezone information isn't important at this point. End-user applications should do this.
* All timestamps will be saved as an `ISODate` in MongoDB. When saved, they will follow the ISO-8601 standard.
* The naming will be following *camelCase.* We will also remove the existing confusion between the current naming we have right now. For example, between `eventTime` and `datetime`. We remove the confusion by explicitly specifying what kind of timestamp we are talking about. Some examples:

  + `createdTime`, the time when the event was created on the side of Teqplay.
  + `actualTime`, the time when the event actually took place.
  + `predictedTime`, the time when the ship is predicted to arrive/depart.
  + It will not be re-using the above fields when the timestamp doesn't fall under one of the following time fields. Instead, it will introduce its own time field.
* When an event is regenerated, the `createdTime` will be the time of regeneration, but an additional `regenerated` boolean field will be provided.

## Ship identifiers

The current `shipMmsi` and `shipImo` fields will be moved to a `ShipIdentifier` class. This object will contain a `mmsi` and `imo` field so it can be reused. For example, with encounter events where both `ship` and `otherShip` are used.

A `ShipIdentifier` should always contain a `mmsi` or `imo` but it is possible to provide both if available. The reason why `mmsi` can be null is because of vessels such as push barges that only have an `imo` number.

kotlindata class ShipIdentifier(
val mmsi: String?,
val imo: String?
)

## Area identifiers

A new field will be added to an event containing the area the event happened. This isn't the same as the `location` of the event.

* The area will contain information about the type of area, such as an `ANCHOR`, together with an internal identifier (Poma identifier).
* A `name` field will be added to add support for custom areas that aren't tied to Poma.
* A `platformLegacyEventName` for backward compatibility won’t be added to the model itself but will be implemented in the bidirectional event converter instead.
* Every kind of area will be added to the list of AreaType. Adding an `AreaType.CUSTOM` is something we want to avoid.

This also means that for each AreaIdentifier, an `id` or `name` always should be provided.

kotlindata class AreaIdentifier(
val id: String?,
val type: AreaType,
val name: String? = null
) {
enum class AreaType {
PORT,
ANCHOR,
/\*\*
\* Also known as pilotarea in platform
\*/
PILOT\_BOARDING\_PLACE,
TERMINAL,
BERTH,
VHF,
END\_OF\_SEA\_PASSAGE,
LOCK,
BASIN,
TUG,
/\*\*
\* All nautical mile areas, for example area.rtm12nm
\*/
NAUTICAL\_MILE,
TERMINAL\_NEARBY,
APPROACH\_POINT,
FAIRWAY,
REGION
}
}

## Location

Location-based events will make use of the Location model. This model is already used by AisEngine. We will also make use of this model in the TeqplayEvents to generalize the geolocation information of a ship. It contains latitude and longitude. The model looks as follows:

kotlindata class Location(
val lat: Double,
val lon: Double
)

## Base models

The new event model will make use of Kotlin data classes and interfaces. Inheritance and subclassing will be avoided.

An event model will contain one or multiple of the following interfaces extending the `Event` interface. The `Event` interface will have all the essential information about an event, removing the currently unneeded fields such as `title` and `description`.

* `_id` a UUID used to identify this event and to be able to save it in the database
* `createdTime` the time when the event was created
* `deleted` an optional boolean, when set to true this event got marked as deleted
* `regenerated` an optional boolean, when set to true this event was regenerated and not included when null

kotlintypealias EventIdentifier = String
@JsonTypeInfo(use = JsonTypeInfo.Id.NAME, include = JsonTypeInfo.As.PROPERTY, property = "type")
@JsonSubTypes(
JsonSubTypes.Type(value = EncounterEvent::class, name = "EncounterEvent")
// All the other events we have
)
interface Event {
val \_id: EventIdentifier
val createdTime: Instant
val deleted: Boolean?
val regenerated: Boolean?
}

### ActualEvent

All events that contain an `actualTime` field will be extending the `ActualEvent` interface. This will look as follows:

kotlininterface ActualEvent : Event {
val actualTime: Instant
}

### LocationBasedShipEvent

The biggest bulk of events will be implementing the `LocationBasedShipEvent` interface.

The LocationBasedShipEvent will contain:

* `ship` field containing the identifiers of the vessel
* `location` containing the latitude and longitude of a vessel

kotlininterface LocationBasedShipEvent : ActualEvent {
val ship: ShipIdentifier
val location: Location
}

### PredictionEvent

The `PredictionEvent` interface will be applied to all events that have some kind of prediction, this can be an ETA or an ETD prediction.

The PredictionEvent will contain:

* `ucrn` the unique call reference number. This is the portcall id for most cases.
* `ship` field containing the identifiers of the vessel
* `area` the area where the prediction is going towards
* `vesselAgent` optionally, the agent that is tied to this ETA prediction
* `predictedTime` the time when the ship should be

kotlininterface PredictionEvent : Event {
val ucrn: String
val ship: ShipIdentifier
val area: AreaIdentifier?
val vesselAgent: String?
val predictedTime: Instant
}

#### LockEvent

While closely tied to PredictionEvents, there are big differences where some of the fields are not used, and others are introduced.

A LockEvent will contain:

* `ship` field containing the identifiers of the vessel
* `area` the area where the prediction is going towards
* `direction` if they are going towards or away from the area that is behind the lock
* `predictedTime` the time when the ship should be

kotlininterface LockEvent : Event {
val ship: ShipIdentifier
val area: AreaIdentifier?
val direction : LockDirection
val predictedTime: Instant
enum class LockDirection {
INBOUND, OUTBOUND
}
}

#### PortcallPilotBoardingEtaEvent

This ETA event is also close to the PredictionEvents while being completely custom. Because of this, the basic model itself is already the implementation.

PortcallPilotBoardingEtaEvent contains the following:

* `portcallId` the portcall this ETA prediction is tied to
* `ship` field containing the identifiers of the vessel
* `area` the area where the prediction is going towards
* `predictedTime` the time when the ship should be predicted to do something. In the case of an ETA event, it is the time when the ship should arrive.

kotlindata class PortcallPilotBoardingEtaEvent(
override val \_id: EventIdentifier,
val portcallId: String,
val ship: ShipIdentifier,
val area: AreaIdentifier?,
val predictedTime: Instant,
override val createdTime: Instant = Instant.now(),
override val deleted: Boolean? = null,
override val regenerated: Boolean? = null
) : Event

### Start-End events

Every event with a start and end should follow the same structure. Start events will extend the `ActualEvent` interface. Stop events will also extend the `ActualEvent` interface but with an additional `startEventId` field. This field will refer to the id of the related start event.

The interfaces will look as follows:

kotlininterface StartEvent : ActualEventkotlininterface EndEvent : ActualEvent {
val startEventId: EventIdentifier?
}

## Grouping events

There are multiple event types that can potentially be grouped. Being Encounter events, ShipInfoChanged events, Area events and Berth events.

### ShipInfoChanged events

For ShipInfoChanged events, we look at the AisDiff message and, based on that, create a `DestinationChangedEvent`, `DraughtChangedEvent`, `StatusChangedEvent` and `AisEtaChangedEvent` containing all an `oldValue` and `newValue`.

While this could be grouped, it has been decided to make explicit events for each diff event. All the events will extend the `AisDiffEvent` interface, containing the `oldValue` and `newValue` fields. The two fields will be of type `T` to allow each type of changed ais info.

kotlininterface AisDiffEvent<T> : LocationBasedShipEvent, ActualEvent {
val oldValue: T?
val newValue: T?
}

| **Platform Event** | **Value Type** | **New Event Type** |
| --- | --- | --- |
| `DestinationChangedEvent` | `String` | `AisDestinationChangedEvent` |
| `DraughtChangedEvent` | `Float` | `AisDraughtChangedEvent` |
| `StatusChangedEvent` | `AisMessage.ShipStatus` | `AisStatusChangedEvent` |
| `AisEtaChangedEvent` | `Instant` | `AisEtaChangedEvent` |

Platform expects to also contain the `oldTrueDestination` and `newTrueDestination` in the `DestinationChangedEvent`. A new event will be created containing only those values for backwards compatibility. The `TrueDestinationChangedEvent` will be fired based on the `AisDestinationChangedEvent`.

### Encounter events

For Encounter events, we create a specific EncounterEvent for the ShipRole the vessel is in contact with. This means when a vessel encounters a Tug, we fire a `TugEvent`. This can be grouped into a new `EncounterEvent`, including an `encounterType` enum which can have the following values:

* TUG
* PILOT
* BOATMAN
* BUNKER
* AUTHORITY
* WASTE
* SWOG
* WATER
* TENDER
* FENDER
* CRANE
* LUBES
* TUG\_WAITING\_DEPARTURE
* SHIP\_TO\_SHIP

And the following barge-specific encounter types:

* BARGE\_SUPPLY (currently called SUPPLYBARGE)
* BARGE\_CARGO (currently called CARGOBARGE)
* BARGE\_TANKER (currently called TANKERBARGE)
* BARGE\_PUSH (currently called PUSHBARGE)
* BARGE\_WATER (Only NLRTM)
* BARGE\_BUNKER (Only NLRTM)

Each encounter event will implement the `EncounterEvent` interface. This interface contains:

* `otherShip` the ship it is encountering with.
* `encounterType` the type of encounter that is happening.

kotlininterface EncounterEvent : LocationBasedShipEvent {
val otherShip: ShipIdentifier
val encounterType: EncounterType
enum class EncounterType {
TUG,
PILOT,
BOATMAN,
BUNKER,
AUTHORITY,
WASTE,
SWOG,
WATER,
TENDER,
FENDER,
CRANE,
LUBES,
TUG\_WAITING\_DEPARTURE,
BARGE\_SUPPLY,
BARGE\_CARGO,
BARGE\_TANKER,
BARGE\_PUSH,
BARGE\_WATER,
BARGE\_BUNKER,
SHIP\_TO\_SHIP,
UNCLASSIFIED
}
}

### Area events

Most of the area events can be grouped as well because they mainly include an `areaName` field which could potentially be added to the `AreaIdentifier` model as an optional field. For example, a `TerminalEvent` contains a `terminalName`. While others such as `VhfEvent` or `EndSeaPassageEvent` have no additional fields, having specific event classes for them is quite unneeded.

The basic interface of each AreaEvent would look as follows:

kotlininterface AreaEvent : LocationBasedShipEvent {
val area: AreaIdentifier
val draught: Float?
}

A start event would then look as follows:

kotlindata class AreaStartEvent(
override val \_id: EventIdentifier,
override val ship: ShipIdentifier,
override val area: AreaIdentifier,
override val draught: Float?,
override val location: Location,
override val actualTime: Instant,
override val createdTime: Instant = Instant.now(),
override val regenerated: Boolean? = null
) : AreaEvent, StartEvent

Which will generate in JSON as:

json{
"type": "AreaStartEvent",
"\_id": "868caeee-d996-43c7-958d-6498a76bedaf",
"ship": {
"mmsi": "244060924",
"imo": null
},
"area": {
"id": "fb2e147b-45e0-4f89-8807-51e642aa65ba",
"type": "PORT",
"name": "NLRTM",
"platformLegacyEventName": "area.port"
},
"draught": 5.9,
"location": {
"lat": 5.5,
"lon": 6.6
},
"actualTime": 1657895321.7114563,
"createdTime": 1657895921.7114563,
"regenerated": null
}

An end event will then look as follows, containing only an additional `startEventId` field:

kotlindata class AreaEndEvent(
override val \_id: EventIdentifier,
override val startEventId: EventIdentifier?,
override val ship: ShipIdentifier,
override val area: AreaIdentifier,
override val draught: Float?,
override val location: Location,
override val actualTime: Instant,
override val createdTime: Instant = Instant.now(),
override val regenerated: Boolean? = null
) : AreaEvent, EndEvent

Which will then translate to the following in JSON:

json{
"type": "AreaEndEvent",
"\_id": "0b6b385b-2665-4765-af3f-ecde20ae8de1",
"startEventId": "d3948eab-9e4b-4507-8b3c-c6eb0c15fe25",
"ship": {
"mmsi": "244060924",
"imo": null
},
"area": {
"id": "0ab1e02e-f80c-4000-bcb3-4d36e6169ebb",
"type": "PORT",
"name": "NLRTM",
"platformLegacyEventName": "area.port"
},
"draught": 5.8,
"location": {
"lat": 5.6,
"lon": 6.7
},
"actualTime": 1657896682.9766006,
"createdTime": 1657896982.9766006,
"regenerated": null
}

### Berth events

Currently, we have three different berth events. Being `BerthEvent`, `ConfirmedBerthEvent` and `UniqueBerthEvent`. This is not ideal as they are pretty much identical with some additional fields.

* `originalTimestamp` on the `ConfirmedBerthEvent` and `UniqueBerthEvent` referring to the time of the original `BerthEvent`.
* `relatedEventId` currently can be filled in for all Berth events, although this shouldn’t be the case for BertStartEvents
* `startBollard` and `endBollard`. They are no longer used and will be removed from the new model.

Because of this, `BerthEvent` can be moved to the `AreaEvent` model. `ConfirmedBerthEvent` and `UniqueBerthEvent` will be created with this additional field.

The Confirmed and Unique BerthEvents will be implementing the `DelayedBerthEvent` interface. This will contain a reference to the `BerthEvent` and the original time. This will look as follows:

kotlininterface DelayedBerthEvent : AreaEvent {
val berthEventId: EventIdentifier
}

This would then be implemented as follows for a ConfirmedBerthStartEvent:

kotlindata class ConfirmedBerthStartEvent(
override val \_id: EventIdentifier,
override val berthEventId: EventIdentifier,
override val ship: ShipIdentifier,
override val area: AreaIdentifier,
override val draught: Float?,
override val location: Location,
override val originalTime: Instant,
override val actualTime: Instant,
override val createdTime: Instant,
override val regenerated: Boolean?,
) : DelayedBerthEvent, StartEvent

Which will look as follows in JSON:

json{
"type": "ConfirmedBerthStartEvent",
"\_id": "919401e1-d5b6-4a4e-bedb-a796d2e67d5a",
"berthEventId": "2684d0b4-472c-4157-9684-c8594f459e36",
"ship": {
"mmsi": "244060924",
"imo": null
},
"area": {
"id": "6d45a876-3387-46a1-a3cc-b83049ac6cb1",
"type": "BERTH",
"name": "NLRTM",
"platformLegacyEventName": "ship-infrastructure.terminal"
},
"draught": 5.9,
"location": {
"lat": 5.7,
"lon": 6.8
},
"actualTime": 1657896739.2850673,
"createdTime": 1657897639.443164,
"regenerated": null
}

---

## All events

|  | **Platform Event Type** | **Platform Class** | **New Event Type** | **Used interfaces beside the Event interface** |
| --- | --- | --- | --- | --- |
| 1 | `ship.movement.start` | `ShipMovingEvent` | `ShipMovingStartEvent` | `LocationBasedShipEvent`, `StartEvent`, `ActualEvent` |
| 2 | `ship.movement.end` | `ShipMovingEndEvent` | `LocationBasedShipEvent`, `EndEvent`, `ActualEvent` |
| 3 | `ship.destinationchanged` | `DestinationChangedEvent` | `AisDestinationChangedEvent` | `AisDiffEvent<String>`, `LocationBasedShipEvent`, `ActualEvent` |
| 4 | `ship.speedchanged` | `SpeedChangedEvent` | `AisStatusChangedEvent` | `LocationBasedShipEvent`, `ActualEvent` |
| 5 | `ship.draughtchanged` | `DraughtChangedEvent` | `AisDraughtChangedEvent` | `AisDiffEvent<Float>`, `LocationBasedShipEvent`, `ActualEvent` |
| 6 | `ship.statuschanged` | `StatusChangedEvent` | `AisStatusChangedEvent` | `AisDiffEvent<AisMessage.ShipStatus>`, `LocationBasedShipEvent`, `ActualEvent` |
| 7 | `ship.aisetachanged` | `AisEtaChangedEvent` | `AisEtaChangedEvent` | `AisDiffEvent<Long>`, `LocationBasedShipEvent`, `ActualEvent` |
| 8 | `ais.lost` | `AisLostEvent` | `AisLostEvent` | `LocationBasedShipEvent`, `ActualEvent` |
| 9 | `ais.recover` | `AisRecoveredEvent` | `AisRecoverEvent` |
| 10 | `ship.anchored` | `AnchoredEvent` | `AnchoredStartEvent` | `AnchoredEvent`, `LocationBasedShipEvent`, `StartEvent`, `ActualEvent` |
| 11 | `AnchoredEndEvent` | `AnchoredEvent`, `LocationBasedShipEvent`, `EndEvent`, `ActualEvent` |
| 12 | `ship-ship.pilot` | `PilotEvent` | `EncounterStartEvent` | `EncounterEvent`, `LocationBasedShipEvent`, `ActualEvent`  For start events also `StartEvent`  For end events also `EndEvent` |
| 13 | `EncounterEndEvent` |
| 14 | `ship-ship.tug` | `TugEvent` | `EncounterStartEvent` |
| 15 | `EncounterEndEvent` |
| 16 | `ship-ship...` (any other ship-ship event) | `...Event` | `EncounterStartEvent` |
| 17 | `EncounterEndEvent` |
| 18 | `encounter.bridge` & `encounter.lock` | `ShipInfraEncounterEvent` | `AreaStartEvent` | `AreaEvent`, `LocationBasedShipEvent`, `ActualEvent`  For start events also `StartEvent`  For end events also `EndEvent` |
| 19 | `AreaEndEvent` |
| 20 | `area.port.<UNLO_CODE>.start` | `PortAtaAtdEvent` | `AreaStartEvent` |
| 21 | `area.port.<UNLO_CODE>.end` | `AreaEndEvent` |
| 22 | `area.vhf.?.start` | `VhfEvent` | `AreaStartEvent` |
| 23 | `area.vhf.?.end` | `AreaEndEvent` |
| 24 | `area.sgsin.eosp.start` | `EndSeaPassageEvent` | `AreaStartEvent` |
| 25 | `area.sgsin.eosp.end` | `AreaEndEvent` |
| 26 | `area.terminal.<POMA_NAME>.start` | `TerminalEvent` | `AreaStartEvent` |
| 27 | `area.terminal.<POMA_NAME>.end` | `AreaEndEvent` |
| 28 | Custom area configuration in `areamonitor.conf` | `TeqplayLocationBasedEvent` | `AreaStartEvent` |
| 29 | `AreaEndEvent` |
| 30 | `ship-infrastructure.terminal.start` | `BerthEvent` | `AreaStartEvent` |
| 31 | `ship-infrastructure.terminal.end` | `AreaEndEvent` |
| 32 | `ship-infrastructure.terminal.start.confirmed` | `ConfirmedBerthEvent` | `ConfirmedBerthStartEvent` | `DelayedBerthEvent`, `AreaEvent`, `LocationBasedShipEvent`, `ActualEvent`    For start events also `StartEvent`  For end events also `EndEvent` |
| 33 | `ship-infrastructure.terminal.end.confirmed` | `ConfirmedBerthEndEvent` |
| 34 | `ship-infrastructure.terminal.start.unique` | `UniqueBerthEvent` | `UniqueBerthStartEvent` |
| 35 | `ship-infrastructure.terminal.end.unique` | `UniqueBerthEndEvent` |
| 36 | `ship.eta` | `EtaEvent` | `EtaEvent` | `PredictionEvent` |
| 37 | `ship.eta.pilotBoardingPlace` | `PortcallPilotBoardingEtaEvent` | `PortcallPilotBoardingEtaEvent` | none |
| 38 | `ship.eta.berth` | `PortcallBerthEtaEvent` | `EtaEvent` | `PredictionEvent` |
| 39 | `ship.eta.lock` | `LockEvent` | `LockEtaEvent` | `LockEvent` |
| 40 | `ship.eta.port` | `EtaEvent` | `EtaEvent` | `PredictionEvent` |
| 41 | `ship.eta.nomination` | `EtaEvent` | `EtaEvent` | `PredictionEvent` |
| 42 | `ship.etd` | `EtdEvent` | `EtdEvent` | `PredictionEvent` |
| 43 | `ship.etd.berth` | `EtdEvent` | `EtdEvent` | `PredictionEvent` |
| 44 | `ship.etd.lock` | `LockEvent` | `LockEtdEvent` | `LockEvent` |
| 45 | `ship.etd.nomination` | `EtdEvent` | `EtdEvent` | `PredictionEvent` |
| 46 | `ship.ata` | `AtaEvent` | `AtaEvent` | `ArrivalEvent`, `ActualEvent` |
| 47 | `ship.atd` | `AtdEvent` | `AtdEvent` | `DepartureEvent`, `ActualEvent` |
---
id: confluence:1057751046
source: confluence
type: page
space: TC
title: 'API Migration Plan for Barges: Changes to Endpoints, Models and Publishing'
author: Darius Wattimena
date: '2026-01-20'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1057751046
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1057751046
---
# API Migration Plan for Barges: Changes to Endpoints, Models and Publishing

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1057751046  

## Content

This document outlines the proposed changes to the VesselVoyage API to facilitate support for barges.

## API Endpoints

To enable barge support in VesselVoyage, the following updates are proposed:

* **CSI Ship ID as Primary Identifier:**   
  The CSI Ship ID will be added to the `ShipDetails` API model and will serve as the primary identifier. The `imo` and `mmsi` will still be available, although while it was already nullable the `imo` field will always be `null` when retrieving barge data.
* **Enhanced** `byPort` Endpoint:   
  The existing `byPort` endpoint will be updated to return non-sea vessels when you request  
  using the `vesselType` param, default `SEA_VESSEL` when not provided. So by default it will maintain the existing behaviour and won’t return any barges in its response. This param is a list where you can do the following:

  + Only sea vessels is `/byPort?vesselType=SEA_VESSEL`
  + Only barges is `/byPort?vesselType=BARGE`
  + Both sea vessel and barges is `/byPort?vesselType=SEA_VESSEL,BARGE`
* **New** `byShipId` Endpoints:   
  Introduce new `byShipId` endpoints (both single and bulk) for Entries, Visits, Voyages, and SOF.
* **New Barge Models:**   
  Add `BargeVisit` and `BargeVoyage` API models, with `_type` values of `BARGE_VISIT` and `BARGE_VOYAGE` respectively.

  + The ShipID will always be provided.
  + Only non-IMO ships will be included in these models.
  + These models will contain the same fields as the existing Visit and Voyage API models, except for the IMO field.
* **Model Renaming for Clarity:**   
  Rename the existing `Visit` and `Voyage` models to `ImoVisit` and `ImoVoyage` to indicate that an IMO number is mandatory. The `_type` field will retain the original `API_VISIT` and `API_VOYAGE` values.

## RabbitMQ Integration

For outgoing changes which are published automatically to RabbitMQ, the renamed `ImoVisit` and `ImoVoyage`, and SOF models will continue to be published without breaking changes. Meaning no direct impact on the existing applications while using the existing API models.

* **Barge Data Routing:**   
  Barge-related data will be published to RabbitMQ, however they won’t be available on any queue unless subscribed to the new routing keys specific to barges.

  + Current routing keys: `VISIT.*`, `VOYAGE.*`, and `SOFVIEW.<VIEW>.*`
  + New routing keys for barges: `BARGE_VISIT.*`, `BARGE_VOYAGE.*`, and `BARGE_SOFVIEW.<VIEW>.*`

## Details

### Visit and Voyage type hierarchy changes

The following changes only impact applications that make use of the VesselVoyage API models or client as Kotlin library.

As noted before:

* The `data class` `Visit` has been renamed to `ImoVisit`
* The `data class` `Voyage` has been renamed to `ImoVoyage`

Additionally extra interfaces are added for an easier time handling with API visits and voyages.

Overview:

wide760Entry (base interface)
├── ApiVisit (sealed interface)
│ ├── ImoVisit (implements ApiVisit, ImoEntry)
│ └── BargeVisit (implements ApiVisit)
└── ApiVoyage (sealed interface)
├── ImoVoyage (implements ApiVoyage, ImoEntry)
└── BargeVoyage (implements ApiVoyage)
ImoEntry (extends Entry with imo: Int field)

### Visit changes

| **Endpoint** | **Method** | **Change** | **Note** |
| --- | --- | --- | --- |
| v2/visit/{id} | GET | breakingRed | Can return a barge visit when providing a visit id of a barge. |
| v2/visit/ids | POST | breakingRed | Can return a mix of imo visits and barge visits given the ids that are provided. |
| v2/visit/byImo | GET | non breakingYellow | Stays the same in terms of JSON output. Only change with this is that in a JVM environment the return type went from `Visit` to `ImoVisit`. |
| POST | non breakingYellow |
| v2/visit/byPort | GET | non breakingYellow | Now includes a `vesselType` options, default `SEA_VESSEL` when not provided. This is a list where you can do the following:   * Only sea vessels is `/byPort?vesselType=SEA_VESSEL` * Only barges is `/byPort?vesselType=BARGE` * Both sea vessel and barges is `/byPort?vesselType=SEA_VESSEL,BARGE`   Example JSON output: When the field is not set (current behaviour)json{ "request": { "start": "2025-12-19T12:00:00Z", "end": null, "unlocode": "USPON", "areaId": null, "aisTrueDestination": null, "categories": null, "finished": null, "confirmed": null, "minDwt": null, "maxDwt": null, "minTeu": null, "maxTeu": null, "filterMultipleOngoing": true, "vesselType": ["SEA\_VESSEL"] }, "data": [ { "\_type": "API\_VISIT", "entryId": "67f387ec-90e7-44e4-8376-4b22774c994b.VISIT", "shipId": "48f57e7d-570b-48ac-bbd8-e4e05eaccc09", "imo": 1089431, "start": { "location": { "lat": 29.98351166666667, "lon": -93.89188166666666 }, "time": "2025-12-19T16:48:23Z", "fallback": null }, "end": null, "port": { "main": "USPON", "sub": [] }, "portTimes": [ { "id": "7373CF647C22C4CF2A308685E7999A2EEBFCCE59", "unlocode": "USBPT", "start": { "location": { "lat": 29.984211666666667, "lon": -93.89660333333333 }, "time": "2025-12-19T16:50:35Z", "fallback": null }, "end": null } ], "trace": null, "stop": [], "passThrough": [], "previous": null, "next": null, "destination": null, "finished": false, "destinationPortEta": null }, { "\_type": "API\_VISIT", "entryId": "1a81c130-d250-4e1d-9ccb-b14ac12565e4.VISIT", "shipId": "dda3b883-ef91-46d8-ae23-994e4ea6898a", "imo": 9596997, "start": { "location": { "lat": 29.983753333333333, "lon": -93.89230666666667 }, "time": "2025-12-19T16:47:55Z", "fallback": null }, "end": null, "port": { "main": "USPON", "sub": [] }, "portTimes": [ { "id": "7373CF647C22C4CF2A308685E7999A2EEBFCCE59", "unlocode": "USBPT", "start": { "location": { "lat": 29.98448, "lon": -93.896805 }, "time": "2025-12-19T16:49:51Z", "fallback": null }, "end": null } ], "trace": null, "stop": [], "passThrough": [], "previous": null, "next": null, "destination": null, "finished": false, "destinationPortEta": null }, { "\_type": "API\_VISIT", "entryId": "40c61547-31af-41f7-b165-bcb5296f7dab.VISIT", "shipId": "9772c75e-13dd-4115-a2b0-d29f5cd670ea", "imo": 9686792, "start": { "location": { "lat": 29.989753333333333, "lon": -93.92717333333333 }, "time": "2025-12-19T15:01:32Z", "fallback": null }, "end": { "location": { "lat": 29.996218333333335, "lon": -93.94574666666668 }, "time": "2025-12-19T15:52:13Z", "fallback": null }, "port": { "main": "USPON", "sub": [] }, "portTimes": [ { "id": "3B57CC10964483E322F3F4EC195BC92F659FE91E", "unlocode": "USPON", "start": { "location": { "lat": 29.989753333333333, "lon": -93.92717333333333 }, "time": "2025-12-19T15:01:32Z", "fallback": null }, "end": { "location": { "lat": 29.996218333333335, "lon": -93.94574666666668 }, "time": "2025-12-19T15:52:13Z", "fallback": null } } ], "trace": null, "stop": [ { "start": { "location": { "lat": 29.99020833333333, "lon": -93.92836000000001 }, "time": "2025-12-19T15:04:18Z", "fallback": null }, "end": { "location": { "lat": 29.990201666666668, "lon": -93.93035499999999 }, "time": "2025-12-19T15:44:41Z", "fallback": null }, "location": { "lat": 29.990103571428563, "lon": -93.9302096031746 }, "area": { "type": "Berth", "id": "E8E0C07A3E2F0C52400C841D8DA2BA4BF4C7E5EC" }, "accuracy": null } ], "passThrough": [], "previous": { "port": null, "entryId": "40c61547-31af-41f7-b165-bcb5296f7dab.VOYAGE" }, "next": { "port": null, "entryId": "444ad396-2248-4f0b-8b04-1568bf37289a.VOYAGE" }, "destination": null, "finished": true, "destinationPortEta": null }, { "\_type": "API\_VISIT", "entryId": "ab121fc9-221c-4433-b39b-9e35b39ffbef.VISIT", "shipId": "2293fa4b-2b6c-488c-b996-6b8052a574a3", "imo": 9716004, "start": { "location": { "lat": 29.98400333333333, "lon": -93.893845 }, "time": "2025-12-19T14:39:56Z", "fallback": null }, "end": null, "port": { "main": "USPON", "sub": [] }, "portTimes": [ { "id": "7373CF647C22C4CF2A308685E7999A2EEBFCCE59", "unlocode": "USBPT", "start": { "location": { "lat": 29.98451833333333, "lon": -93.89652166666666 }, "time": "2025-12-19T14:40:56Z", "fallback": null }, "end": null }, { "id": "3B57CC10964483E322F3F4EC195BC92F659FE91E", "unlocode": "USPON", "start": { "location": { "lat": 29.99001333333333, "lon": -93.92672833333333 }, "time": "2025-12-19T15:00:37Z", "fallback": null }, "end": null } ], "trace": null, "stop": [ { "start": { "location": { "lat": 29.99026, "lon": -93.92794666666667 }, "time": "2025-12-19T15:04:13Z", "fallback": null }, "end": null, "location": null, "area": { "type": "Unclassified", "id": null }, "accuracy": null } ], "passThrough": [], "previous": null, "next": null, "destination": null, "finished": false, "destinationPortEta": null } ] }When the field is set to truejson "request": { "start": "2025-12-19T12:00:00Z", "end": null, "unlocode": "USPON", "areaId": null, "aisTrueDestination": null, "categories": null, "finished": null, "confirmed": null, "minDwt": null, "maxDwt": null, "minTeu": null, "maxTeu": null, "filterMultipleOngoing": true, "vesselType": ["SEA\_VESSEL", "BARGE"] }, "data": [ { "\_type": "API\_VISIT", "entryId": "67f387ec-90e7-44e4-8376-4b22774c994b.VISIT", "shipId": "48f57e7d-570b-48ac-bbd8-e4e05eaccc09", "imo": 1089431, "start": { "location": { "lat": 29.98351166666667, "lon": -93.89188166666666 }, "time": "2025-12-19T16:48:23Z", "fallback": null }, "end": null, "port": { "main": "USPON", "sub": [] }, "portTimes": [ { "id": "7373CF647C22C4CF2A308685E7999A2EEBFCCE59", "unlocode": "USBPT", "start": { "location": { "lat": 29.984211666666667, "lon": -93.89660333333333 }, "time": "2025-12-19T16:50:35Z", "fallback": null }, "end": null } ], "trace": null, "stop": [], "passThrough": [], "previous": null, "next": null, "destination": null, "finished": false, "destinationPortEta": null }, { "\_type": "API\_VISIT", "entryId": "1a81c130-d250-4e1d-9ccb-b14ac12565e4.VISIT", "shipId": "dda3b883-ef91-46d8-ae23-994e4ea6898a", "imo": 9596997, "start": { "location": { "lat": 29.983753333333333, "lon": -93.89230666666667 }, "time": "2025-12-19T16:47:55Z", "fallback": null }, "end": null, "port": { "main": "USPON", "sub": [] }, "portTimes": [ { "id": "7373CF647C22C4CF2A308685E7999A2EEBFCCE59", "unlocode": "USBPT", "start": { "location": { "lat": 29.98448, "lon": -93.896805 }, "time": "2025-12-19T16:49:51Z", "fallback": null }, "end": null } ], "trace": null, "stop": [], "passThrough": [], "previous": null, "next": null, "destination": null, "finished": false, "destinationPortEta": null }, { "\_type": "API\_VISIT", "entryId": "40c61547-31af-41f7-b165-bcb5296f7dab.VISIT", "shipId": "9772c75e-13dd-4115-a2b0-d29f5cd670ea", "imo": 9686792, "start": { "location": { "lat": 29.989753333333333, "lon": -93.92717333333333 }, "time": "2025-12-19T15:01:32Z", "fallback": null }, "end": { "location": { "lat": 29.996218333333335, "lon": -93.94574666666668 }, "time": "2025-12-19T15:52:13Z", "fallback": null }, "port": { "main": "USPON", "sub": [] }, "portTimes": [ { "id": "3B57CC10964483E322F3F4EC195BC92F659FE91E", "unlocode": "USPON", "start": { "location": { "lat": 29.989753333333333, "lon": -93.92717333333333 }, "time": "2025-12-19T15:01:32Z", "fallback": null }, "end": { "location": { "lat": 29.996218333333335, "lon": -93.94574666666668 }, "time": "2025-12-19T15:52:13Z", "fallback": null } } ], "trace": null, "stop": [ { "start": { "location": { "lat": 29.99020833333333, "lon": -93.92836000000001 }, "time": "2025-12-19T15:04:18Z", "fallback": null }, "end": { "location": { "lat": 29.990201666666668, "lon": -93.93035499999999 }, "time": "2025-12-19T15:44:41Z", "fallback": null }, "location": { "lat": 29.990103571428563, "lon": -93.9302096031746 }, "area": { "type": "Berth", "id": "E8E0C07A3E2F0C52400C841D8DA2BA4BF4C7E5EC" }, "accuracy": null } ], "passThrough": [], "previous": { "port": null, "entryId": "40c61547-31af-41f7-b165-bcb5296f7dab.VOYAGE" }, "next": { "port": null, "entryId": "444ad396-2248-4f0b-8b04-1568bf37289a.VOYAGE" }, "destination": null, "finished": true, "destinationPortEta": null }, { "\_type": "API\_VISIT", "entryId": "ab121fc9-221c-4433-b39b-9e35b39ffbef.VISIT", "shipId": "2293fa4b-2b6c-488c-b996-6b8052a574a3", "imo": 9716004, "start": { "location": { "lat": 29.98400333333333, "lon": -93.893845 }, "time": "2025-12-19T14:39:56Z", "fallback": null }, "end": null, "port": { "main": "USPON", "sub": [] }, "portTimes": [ { "id": "7373CF647C22C4CF2A308685E7999A2EEBFCCE59", "unlocode": "USBPT", "start": { "location": { "lat": 29.98451833333333, "lon": -93.89652166666666 }, "time": "2025-12-19T14:40:56Z", "fallback": null }, "end": null }, { "id": "3B57CC10964483E322F3F4EC195BC92F659FE91E", "unlocode": "USPON", "start": { "location": { "lat": 29.99001333333333, "lon": -93.92672833333333 }, "time": "2025-12-19T15:00:37Z", "fallback": null }, "end": null } ], "trace": null, "stop": [ { "start": { "location": { "lat": 29.99026, "lon": -93.92794666666667 }, "time": "2025-12-19T15:04:13Z", "fallback": null }, "end": null, "location": null, "area": { "type": "Unclassified", "id": null }, "accuracy": null } ], "passThrough": [], "previous": null, "next": null, "destination": null, "finished": false, "destinationPortEta": null }, { "\_type": "BARGE\_VISIT", "entryId": "f943dbea-9f26-4746-a156-0479ad0d2893.VISIT", "shipId": "d70342e3-f9bb-4eb2-ba9c-0899b82e8ef5", "start": { "location": { "lat": 29.9952, "lon": -93.94406666666667 }, "time": "2025-12-19T12:22:15Z", "fallback": null }, "end": null, "port": { "main": "USPON", "sub": [] }, "portTimes": [ { "id": "3B57CC10964483E322F3F4EC195BC92F659FE91E", "unlocode": "USPON", "start": { "location": { "lat": 29.9952, "lon": -93.94406666666667 }, "time": "2025-12-19T12:22:15Z", "fallback": null }, "end": null } ], "trace": null, "stop": [ { "start": { "location": { "lat": 29.99425, "lon": -93.94313333333334 }, "time": "2025-12-19T12:30:25Z", "fallback": null }, "end": { "location": { "lat": 29.994216666666667, "lon": -93.943 }, "time": "2025-12-19T14:32:44.495Z", "fallback": null }, "location": { "lat": 29.9942380952381, "lon": -93.94314523809524 }, "area": { "type": "Unclassified", "id": null }, "accuracy": null }, { "start": { "location": { "lat": 29.99271666666667, "lon": -93.93863333333334 }, "time": "2025-12-19T14:39:45Z", "fallback": null }, "end": null, "location": null, "area": { "type": "Berth", "id": "E045A1F5ED995678F41C4D5830959BDBC57395F8" }, "accuracy": null } ], "passThrough": [], "previous": null, "next": null, "destination": null, "finished": false, "destinationPortEta": null } ] } Do note that in the 2nd JSON output there is a new entry with a barge visit with no `imo` field, given the ship doesn’t have one. json{ "\_type": "BARGE\_VISIT", "entryId": "f943dbea-9f26-4746-a156-0479ad0d2893.VISIT", "shipId": "d70342e3-f9bb-4eb2-ba9c-0899b82e8ef5" } |
| POST | non breakingYellow |
| v2/visit/byShipId | GET | NewGreen | Similar behaviour how the byImo endpoints worked, instead of an IMO you provide a CSI Ship ID as the ship identifier. Next to this, the endpoint can return both `ImoVisit` and `BargeVisit` meaning that depending on the usage you might have to support both JSON outputs. |
| POST | NewGreen |

### Voyage changes

| **Endpoint** | **Method** | **Change** | **Note** |
| --- | --- | --- | --- |
| v2/voyage/{id} | GET | breakingRed | Can return a barge voyage when providing a voyage id of a barge. |
| v2/voyage/ids | POST | breakingRed | Can return a mix of imo voyages and barge voyages given the ids that are provided. |
| v2/voyage/byImo | GET | non breakingYellow | Stays the same in terms of JSON output. Only change with this is that in a JVM environment the return type went from `Voyage` to `ImoVoyage`. |
| POST | non breakingYellow |
| v2/voyage/byPort | GET | non breakingYellow | Now includes a `vesselType` options, default `SEA_VESSEL` when not provided. This is a list where you can do the following:   * Only sea vessels is `/byPort?vesselType=SEA_VESSEL` * Only barges is `/byPort?vesselType=BARGE` * Both sea vessel and barges is `/byPort?vesselType=SEA_VESSEL,BARGE`   Example JSON output: When the field is not set (current behaviour)json{ "request": { "originPortUnlocodes": [ "ESALG" ], "destinationPortUnlocodes": [], "start": null, "end": null, "limit": null, "categories": null, "finished": false, "minDwt": null, "maxDwt": null, "minTeu": null, "maxTeu": null, "filterMultipleOngoing": true, "vesselType": ["SEA\_VESSEL"] }, "data": [] }When the field is set to truejson{ "request": { "originPortUnlocodes": [ "ESALG" ], "destinationPortUnlocodes": [], "start": null, "end": null, "limit": null, "categories": null, "finished": false, "minDwt": null, "maxDwt": null, "minTeu": null, "maxTeu": null, "filterMultipleOngoing": true, "vesselType": ["SEA\_VESSEL", "BARGE"] }, "data": [ { "\_type": "BARGE\_VOYAGE", "entryId": "406561fc-74c4-46f5-b673-13c93ba1ddb1.VOYAGE", "shipId": "53eae7bc-a869-4cf4-a556-6050e06e4556", "start": { "location": { "lat": 35.96845833333334, "lon": -5.7628466666666665 }, "time": "2025-12-16T18:28:35Z", "fallback": null }, "end": null, "trace": null, "stop": [], "passThrough": [], "previous": { "port": "ESALG", "entryId": "cc1dfeaa-c152-4377-b9fa-563a14dd1123.VISIT" }, "next": null, "destination": null, "finished": false, "destinationPortEta": null } ] } Do note that in the 2nd JSON output there is a new entry with a barge voyage with no `imo` field, given the ship doesn’t have one. json{ "\_type": "BARGE\_VOYAGE", "entryId": "406561fc-74c4-46f5-b673-13c93ba1ddb1.VOYAGE", "shipId": "53eae7bc-a869-4cf4-a556-6050e06e4556", } |
| POST | non breakingYellow |
| v2/voyage/byShipId | GET | NewGreen | Similar behaviour how the byImo endpoints worked, instead of an IMO you provide a CSI Ship ID as the ship identifier. Next to this, the endpoint can return both `ImoVisit` and `BargeVisit` meaning that depending on the usage you might have to support both JSON outputs. |
| POST | NewGreen |

### Statement of Facts changes (PTO View)

For all JSON outputs, an `id` field has been added in the `ship` object is added.

Ship object for an IMO vessel:

json"ship": {
"id": "48f57e7d-570b-48ac-bbd8-e4e05eaccc09",
"mmsi": "368406380",
"imo": "1089431",
"name": "RIO GULF",
"categories": {
"v1": null,
"v2": null,
"v3": null
},
"length": null,
"beam": null,
"maxDraught": null,
"dwt": null
}

Ship object for a barge:

json"ship": {
"id": "d70342e3-f9bb-4eb2-ba9c-0899b82e8ef5",
"mmsi": "367653530",
"imo": null,
"name": "LILY C",
"categories": {
"v1": null,
"v2": null,
"v3": null
},
"length": null,
"beam": null,
"maxDraught": null,
"dwt": null
}

Note that `imo` is always `null` in this case.

| **Endpoint** | **Method** | **Change** | **Note** |
| --- | --- | --- | --- |
| v2/sof/byVisit/{id} | GET | breakingRed | When a visit id is provided of a ship with an IMO then `ship.imo` will be filled, when this ship is a barge this field will be always `null`. |
| v2/sof/byImo | GET | non breakingYellow | IMO based endpoints, will always have a value in the `ship.imo` field. |
| POST | non breakingYellow |
| v2/sof/byImo/{imo}/lookaround | GET | non breakingYellow |
| v2/sof/byPort | GET | non breakingYellow | Now includes a `vesselType` options, default `SEA_VESSEL` when not provided. Meaning you will only get back IMO ships like we normally would. This `vesselType` param a list where you can do the following:   * Only sea vessels is `/byPort?vesselType=SEA_VESSEL` * Only barges is `/byPort?vesselType=BARGE` * Both sea vessel and barges is `/byPort?vesselType=SEA_VESSEL,BARGE`   When `BARGE` is included it will contains ships where the `ship.imo` field will be `null`. It will still be filled in for all IMO based ships. |
| POST | non breakingYellow |
| v2/sof/byShipId | GET | NewGreen | Similar behaviour how the byImo endpoints worked, instead of an IMO you provide a CSI Ship ID as the ship identifier. For IMO based ships `ship.imo` will be filled, for barges this will be `null`. |
| POST | NewGreen |

### Statement of Facts changes (PortReporter View)

For all JSON outputs:

1. An `id` field has been added in the `ship` object is added.
2. The `ship.imo` field is always `0` for a barge.

Ship object for an IMO vessel:

json"ship": {
"id": "48f57e7d-570b-48ac-bbd8-e4e05eaccc09",
"imo": 1089431,
"name": "RIO GULF",
"type": null
}

Ship object for a barge:

json"ship": {
"id": "d70342e3-f9bb-4eb2-ba9c-0899b82e8ef5",
"imo": 0,
"name": "LILY C",
"type": null
}

| **Endpoint** | **Method** | **Change** | **Note** |
| --- | --- | --- | --- |
| v2/sof/byVisit/{id} | GET | breakingRed | When a visit id is provided of a ship with an IMO then `ship.imo` will be filled, when this ship is a barge this field will be always `0`. |
| v2/sof/byImo | GET | non breakingYellow | IMO based endpoints, will always have a value in the `ship.imo` field. |
| POST | non breakingYellow |
| v2/sof/byImo/{imo}/lookaround | GET | non breakingYellow |
| v2/sof/byPort | GET | non breakingYellow | Now includes a `vesselType` options, default `SEA_VESSEL` when not provided. Meaning you will only get back IMO ships like we normally would. This `vesselType` param a list where you can do the following:   * Only sea vessels is `/byPort?vesselType=SEA_VESSEL` * Only barges is `/byPort?vesselType=BARGE` * Both sea vessel and barges is `/byPort?vesselType=SEA_VESSEL,BARGE`   When `BARGE` is included it will contains ships where the `ship.imo` field will be `0`. It will still be filled in for all IMO based ships. |
| POST | non breakingYellow |
| v2/sof/byShipId | GET | NewGreen | Similar behaviour how the byImo endpoints worked, instead of an IMO you provide a CSI Ship ID as the ship identifier. For IMO based ships `ship.imo` will be filled, for barges this will be `0`. |
| POST | NewGreen |
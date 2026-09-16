---
id: confluence:325484545
source: confluence
type: page
space: TC
title: API V2 endpoints
author: Leon Joosse (Unlicensed)
date: '2024-04-11'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/325484545
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/325484545
---
# API V2 endpoints

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/325484545  

## Content

none

# V2 API description

V2 of the VesselVoyage API.

Changes compared to V1:

* Added `journal`: pair of visit and the preceding visit
* URLs are now structured to what data it returns: `/v2/datatype/{selectorkey}/{selectorvalue}`.  
  For example, to retrieve the entries for a ship:

  + `/v1/ship/{imo}/history`
  + `/v2/entry/byImo/{imo}`
* V2 has bulk endpoints available for most queries. See the table below for more information.

# Data types with available queries

singlePurple allows a single request (1 id, 1 imo, etc)  
bulkGreen allows multiple requests (multiple ids, multiple imos, etc)

| **Name** | **Description** | **Available queries** | **Additional filters** | **Supports** |
| --- | --- | --- | --- | --- |
| Entry | Lists visits and voyages | * By entry id |  | singlePurple bulkGreen |
| * By ship `imo`,    + with a `timerange`   + recent `{number}` of entries | * `finished=true|false` or omit / `null` for all * `categoriesV1` * `categoriesV2` * `deadWeightTonnages` range * `limit` newBlue | singlePurple bulkGreen |
| * Query object |  | singlePurple |
| Journal | List of **voyage + visit pairs**, meaning the visit and the preceding voyage.  Note that the voyage can be null, in case of the very first recorded visit of the ship.  The trace is included in each visit / voyage. | * By visit id or ids |  | singlePurple bulkGreen |
| * By ship `imo`,    + with a `timerange`   + recent `{number}` of entries | * `finished=true|false` or omit / `null` for all * `categoriesV1` * `categoriesV2` * `deadWeightTonnages` range * `limit` newBlue | singlePurple bulkGreen |
| * Query object |  | singlePurple |
| Visit | Visit to a port.  The trace is included in each visit. | * By id or ids * By id, plus `{number}` of visits before / after it possible deprecationYellow |  | singlePurple bulkGreen |
| * By ship `imo`,    + with a `timerange`   + recent `{number}` of recent visits | * `finished=true|false` or omit / `null` for all * `categoriesV1` * `categoriesV2` * `deadWeightTonnages` range * `limit` newBlue | singlePurple bulkGreen |
| * By port `unlocode`, with a `timerange` | * `finished=true|false` or omit / `null` for all * `categoriesV1` * `categoriesV2` * `deadWeightTonnages` range * `limit` newBlue | singlePurple bulkGreen |
| * Query object |  | singlePurple |
| Voyage | Voyage between visits  The trace is included in each voyage. | * By id or ids |  | singlePurple bulkGreen |
| * By ship `imo`,    + with a `timerange`   + recent `{number}` of recent visits | * `finished=true|false` or omit / `null` for all * `categoriesV1` * `categoriesV2` * `deadWeightTonnages` range * `limit` newBlue | singlePurple bulkGreen |
| * By `origin`, with a timerange * By `destination`, with a timerange * By `origin` + `destination`, with a timerange | * `finished=true|false` or omit / `null` for all * `categoriesV1` * `categoriesV2` * `deadWeightTonnages` range * `limit` newBlue | singlePurple bulkGreen |
| * Query object |  | singlePurple |
| Statement of facts (SOF) | Statement of facts timestamps based on a visit.  There are 2 views available:   1. port, with timestamp buckets **arrival**, **in-port** and **departure** 2. terminal, with timestamp buckets **pre-arrival**, **arrival**, **in-port** and **departure**   Refer to the V2 definition for the exact details. | * By visit id or ids |  | singlePurple bulkGreen |
| * By ship `imo`    + with a `timerange`   + recent `{number}` of recent visits | * `finished=true|false` or omit / `null` for all * `categoriesV1` * `categoriesV2` * `deadWeightTonnages` range * `limit` newBlue | singlePurple bulkGreen |

# Endpoint comparison V1 / V2

| **V1 controller** | **V1** | **V2** |
| --- | --- | --- |
| **Entries** | /v1/entries /v1/entries/{id} /v1/entries/metadata/imos /v1/entries/visits/{imo} | /v2/entry /v2/entry/{id} - - Note the new `/v2/journal` endpoints, to retrieve visit + preceding voyage pairs instead of separate visit/voyage/visit/etc |
| **Ports** | /v1/ports/{portId}/visits /v1/ports/{portId}/anchorages /v1/ports/{portId}/next /v1/ports/{portId}/previous | /v2/visit/byPort?unlocode= or ?pomaId= - /v2/voyage/byPort?destination= /v2/voyage/byPort?origin= |
| **Ships** | text/v1/ships/{imo}/recent /v1/ships/{imo}/history /v1/ships/recent /v1/ships/history /v1/ships/{imo}/history/visits /v1/ships/{imo}/history/voyages | /v2/entries/byImo/{imo}?last= or /v2/journal/byImo/{imo}?last= /v2/entries/byImo/{imo}?start&end or /v2/journal/byImo/{imo}?start&end /v2/entries/byImo or /v2/journal/byImo /v2/entries/byImo or /v2/journal/byImo /v2/visit/byImo/{imo} /v2/voyage/byImo/{imo} |
| **Trace** | /v1/traces/\* | Traces are now included in all `Visit` and `Voyage` objects |
| **Visit** | /v1/visits/ports/{id} /v1/visits/previous/{imo}?before= /v1/visits/{imo}/ids /v1/visits/{imo}/count /v1/visits/query | /v2/visit/byPort?unlocode= or ?pomaId= - - - /v2/visit/query |
| **Voyage** | /v1/voyages/query | /v2/voyage/query |

# V2 endpoints spec

## Limits and sorting

* A **limit is not enforced** by default on all endpoints, unless otherwise specifically stated in the spec.   
  On most list requests, you can set your own `limit`.
* All lists are returned old to new, looking at a start timestamps (as those are always available)

## Entries

|  | **ENTRIES** | **Request** | **Parameters** | **Response** |
| --- | --- | --- | --- | --- |
| 1 | By visit id | GET /v2/entry/{id}POST /v2/entry/ids [ "id1", "id2", "id3", ... ] | Required   * `{id}`: visit id | **GET response**  200 OK 404 Not Found: obj with the given id does not exist { visit obj } **POST response**  200 OK. When an entry is not found, it is returned as `null` { "id1": { visit obj }, "id2": { voyage obj }, "id3": null } The response shows the examples:   1. `id1`: a visit 2. `id2`: a voyage 3. `id3`: this id was not found in visit and voyage database |
| 2 | By ship imo and time range | GET /v2/entry/byImo/{imo} ?start=.. &end=..POST /v2/entry/byImo [ { "imo": "1234567", "start": 123, "end": 456, // optional filters }, ... ] | Required   * `imo`: imo of the ship * `start`: time window start * `end`: time window end   Optional   * `finished=true|false` or omit / null for all * `categoriesV1` * `categoriesV2` * `deadWeightTonnages` range * `limit` newBlue | There is no id in the request objects, so the response includes the request so the caller can identify what response belongs to what request. (could be IMO, but what if you have multiple requests per IMO)  **GET response**:  200 OK 404 Not Found: ship does not exist { "request": { "imo": "1234567", "start": 123, "end": 456 // optional filters }, "data": [ { visit obj }, { voyage obj }, ... ] } **POST response**: [ { "request": { "imo": "1234567", "start": 123, ... }, "data": [ { visit obj }, { voyage obj }, ... ] }, ... ] |
| 3 | Most recent amount by ship imo | GET /v2/entry/byImo/{imo} ?last=10POST /v2/journal/byImo [ { "imo": "1234567", "last": 10, // optional filters }, ... ] | Required   * `imo`: imo of the ship * `last`: amount of entries, in other words: “<number> most recent items”   Optional   * `finished=true|false` or omit / null for all * `categoriesV1` * `categoriesV2` * `deadWeightTonnages` range * `limit` newBlue     **Note**: requesting 10 items typically will result in half the amount of visits and voyages. In other words, 5 visits and 5 voyages. This can vary depending on your optional filters. | **GET response**:  200 OK 404 Not Found: ship does not exist [ { "visit": { .. }, "precedingVoyage": { .. }, { "visit": { .. }, "precedingVoyage": { .. }, ... ] **POST response**: [ { "request": { "imo": "1234567", "last": 10, ... }, "data": [ { "visit": { .. }, "precedingVoyage": { .. }}, ... ] }, ... ] |

## Journal

|  | **JOURNAL** | **Request** | **Parameters** | **Response** |
| --- | --- | --- | --- | --- |
| 1 | By visit id | GET /v2/journal/{id}POST /v2/journal/ids [ "visit1", "visit2", "visit3", ... ] | Required   * `{id}`: visit id | Visit with voyage  **GET response**  200 OK 400 Bad Request: object for the given id is not a visit 404 Not Found: visit does not exist { "visit": { visit obj }, "precedingVoyage": { voyage obj, or null if not available } } **POST response** { "visit1": { "visit": { visit obj }, "precedingVoyage": { voyage obj } }, "visit2":{ "visit": { visit obj }, "precedingVoyage": null }, "visit3": null } Endpoint always returns 200 OK.  The response shows the examples:   1. `visit1`: the visit and preceding voyage 2. `visit2`: the visit is there, but there was no preceding voyage in the system 3. `visit3`: this visit does not exist, or is not a visit |
| 2 | By ship imo and time range | GET /v2/journal/byImo/{imo} ?start=.. &end=..POST /v2/journal/byImo [ { "imo": "1234567", "start": 123, "end": 456, // optional filters }, ... ] | Required   * `imo`: imo of the ship * `start`: time window start * `end`: time window end   Optional   * `finished=true|false` or omit / null for all * `categoriesV1` * `categoriesV2` * `deadWeightTonnages` range * `limit` newBlue | List of visits with their preceding voyages.  There is no id in the request objects, so the response includes the request so the caller can identify what response belongs to what request. (could be IMO, but what if you have multiple requests per IMO)  **GET response**:  200 OK 404 Not Found: ship does not exist { "request": { "imo": "1234567", "start": 123, "end": 456 // optional filters }, "data": [ { "visit": { .. }, "precedingVoyage": { .. }, { "visit": { .. }, "precedingVoyage": { .. }, ... ] } **POST response**: [ { "request": { "imo": "1234567", "start": 123, ... }, "data": [ { "visit": { .. }, "precedingVoyage": { .. }}, ... ] }, ... ] |
| 3 | Most recent amount by ship imo | GET /v2/journal/byImo/{imo} ?last=10POST /v2/journal/byImo [ { "imo": "1234567", "last": 10, // optional filters }, ... ] | Required   * `imo`: imo of the ship * `last`: amount of entries, in other words: “<number> most recent items”   Optional   * `finished=true|false` or omit / null for all * `categoriesV1` * `categoriesV2` * `deadWeightTonnages` range * `limit` newBlue     **Note**: requesting 10 items typically will result in half the amount of visits and voyages. In other words, 5 visits and 5 voyages. This can vary depending on your optional filters. | List of visits with their preceding voyages.  **GET response**:  200 OK 404 Not Found: ship does not exist { "request": { "imo": "1234567", "last": 10, // optional filters }, "data": [ { "visit": { .. }, "precedingVoyage": { .. }, { "visit": { .. }, "precedingVoyage": { .. }, ... ] } **POST response**: [ { "request": { "imo": "1234567", "last": 10, ... }, "data": [ { "visit": { .. }, "precedingVoyage": { .. }}, ... ] }, ... ] |

## Visit

|  | **VISITS** | **Request** | **Parameters** | **Response** |
| --- | --- | --- | --- | --- |
| 1 | By id or ids | GET /v2/visit/{id}POST /v2/visit/ids [ "id1", "id2", ... ] | Required   * `{id}`: visit id | **GET response**  200 OK 404 Not Found: visit does not exist { visit obj } **POST response** { "id1": { visit obj }, "id2": { visit obj } } |
| 2 | By ship imo and time range | GET /v2/visit/byImo/{imo} ?start=.. &end=..POST /v2/visit/byImo [ { "imo": "1234567", "start": 123, "end": 456, // optional filters }, ... ] | Required   * `imo`: imo of the ship * `start`: time window start * `end`: time window end   Optional   * `finished=true|false or omit / null for all` * `categoriesV1` * `categoriesV2` * `deadWeightTonnages` range * `limit` newBlue | **GET response**:  200 OK 404 Not Found: ship does not exist { "request": { "imo": "1234567", "start": 123, "end: 456", "finishedState": "all" }, "data": [ { "type": "visit", ... }, ... ] } **POST response**: array of the above objects |
| 3 | Most recent amount by ship imo | GET /v2/visit/byImo/{imo} ?last=..POST /v2/ship/byImo [ { "imo": "1234567", "last": 10, // optional filters }, ... ] **TODO:** do we need an identifier per request in POST? So caller can easily lookup by id in the response? Can use IMO, but fails if caller does multiple requests per IMO | Required   * `imo`: imo of the ship * `last`: number of entries   Optional   * `finished=true|false` or omit / null for all * `categoriesV1` * `categoriesV2` * `deadWeightTonnages` range * `limit` newBlue | **GET response**:  200 OK 404 Not Found: ship does not exist { "request": { "imo": "1234567", "last": 10, // optional filters }, "data": [ { "type": "visit", ... }, ... ] } **POST response**: array of the above response object |
| 4 | By port (unlocode or poma id) with a time range  `POST` allows multiple requests at once. | Use `unlocode` or `pomaId` GET /v2/visit/byPort ?unlocode=NLRTM &pomaId=AAA &start=.. &end=..POST /v2/visits/byPort [ { "unlocode": "NLRTM", "pomaId": "AAA", "start": 123, "end": 456 }, ... ] | Required   * One of:    + `unlocode`: unlocode   + `pomaId`: poma id of the port * `start`: time window start * `end`: time window end   Providing both `unlocode` and `pomaId` results in a 400 Bad Request.  Optional   * `finished=true|false or omit / null for all` * `categoriesV1` * `categoriesV2` * `deadWeightTonnages` range * `limit` newBlue | **GET response**:  200 OK [ { "type": "visit", ... }, ... ] **POST response** [ { "request": { "unlocode": "NLRTM", "pomaId": "AAA", "start": 123, "end": 456 // optional filters }, "data": [ { "type": "visit", ... }, ... ] }, ... ] |
| 5 | Query | POST /v2/visit/query | **TODO** | **TODO** |

## Voyages

| **VOYAGE** | **Request** | **Parameters** | **Response** |
| --- | --- | --- | --- |
| By id or ids | GET /v2/voyage/{id}POST /v2/voyage/ids [ "id1", "id2", ... ] | Required   * `{id}`: voyage id | **GET response**  200 OK 404 Not Found: voyage does not exist { voyage obj } **POST response** { "id1": { voyage obj }, "id2": { voyage obj } } |
| By ship imo and time range | GET /v2/voyage/byImo/{imo} ?start=.. &end=..POST /v2/voyage/byImo [ { "imo": "1234567", "start": 123, "end": 456, // optional filters }, ... ] | Required   * `imo`: imo of the ship * `start`: time window start * `end`: time window end   Optional   * `finished=true|false` or omit / null for all * `categoriesV1` * `categoriesV2` * `deadWeightTonnages` range * `limit` newBlue | **GET response**:  200 OK 404 Not Found: ship does not exist { "request": { "imo": "1234567", "start": 123, "end: 456", "finishedState": "all" }, "data": [ { "type": "voyage", ... }, ... ] } **POST response**: array of the above objects |
| Last number of voyages by ship IMO | GET /v2/voyage/byImo/{imo} ?last=10POST /v2/voyage/byImo [ { "imo": "1234567", "last": 10, // optional filters }, ... ] | Required   * `imo`: imo of the ship * `last`: number of entries   Optional   * … | **GET response**:  200 OK 404 Not Found: ship not found [ { "type": "voyage", ... }, ... ] **POST response**:  200 OK 404 Not found: ship not found [ { "request": { "imo": "1234567", "last": 10, "finishedState": "all" }, "data": [ { "type": "voyage", ... }, ... ] }, ... ] |
| By origin and/or destination with a time range | Using unlocodes: GET /v2/voyage/byPort ?originUnlocodes=NLRTM,NLAMS &destinationUnlocodes=BEANR,BEGNE &start=.. &end=.. GET /v2/voyage/byPort ?originPomaIds=AAA,BBB &destinationPomaIds=CCC,DDD &start=.. &end=..POST /v2/voyage/byPort [ { "originPomaIds": ["NLRTM", "NLAMS"], "destinationPomaIds": ["BEANR", "BEGNE"], "start": 123, "end": 456 }, ... ] POST /v2/voyage/byPort [ { "originPomaIds": ["AAAA", ...], "destinationPomaIds": ["BBBB", ...], "start": 123, "end": 456 }, ... ] | Required (using unlocodes):   * `originUnlocodes`: voyage originated from this port (comma separate for multiple) * `destinationUnlocodes`: voyage destined for this port (comma separate for multiple) * `start`: time window start * `end`: time window end   Required (using poma ids):   * `originPomaIds`: poma id of the voyage origin port * `destinationPomaIds`: poma id of the voyage destination port * `start`: time window start * `end`: time window end   Mixing poma id and unlocode query parameters results in a 400 Bad Request.  Optional   * `finished=true|false` or omit / null for all * `categoriesV1` * `categoriesV2` * `deadWeightTonnages` range * `limit` newBlue   When providing `origin` and `destination`, the resulting `voyage.origin` is in `query.origin` AND `voyage.destination` is in `query.destination`.  **Note on main / sub ports**: If `origin` / `destination` is not a main port (for example NLVLA inside NLRTM), then you’ll get no results, because everything is attached to the main port (as the EOSP area of the main port covers all sub ports). | **GET response**: { "request": { "origin": ["NLRTM", "NLAMS"], "destination": ["BEANR", "BEGNE"], "start": 123, "end": 456 // optional filters }, "data": [ { "type": "voyage", ... }, ... ] } **POST response** { "request": { // when using unlocodes, otherwise empty "originUnlocodes": ["NLRTM", "NLAMS"], "destinationUnlocodes": ["BEANR", "BEGNE"], // when using pomaIds, otherwise empty "originPomaIds": ["AAA", "BBB"], "destinationPomaIds": ["CCC", "DDD"], "start": 123, "end": 456 // optional filters }, "data": [ { "type": "voyage", ... }, ... ] } |
| Query | POST /v2/voyage/query [ ] | **TODO** | **TODO** |

## Statement of facts (SOF)

| **SOF** | **Request** | **Parameters** | **Response** |
| --- | --- | --- | --- |
| By visit id | GET /v2/sof/byVisit/{visitId} [?view=port|terminal]POST /v2/sof/byVisit [ "visit1", "visit2", ... ] | Required   * `{id}`: visit id   Optional   * `{view}`: `port` or `terminal` (default is `port` (arrival, in-port, departure)) | **GET response**  200 OK with result 400 Bad Request: object if the given id is not a visit 404 Not Found: visit not found { "visitId": "visit1", "view": "port|terminal", "sof": { sof obj } } **POST response**  200 OK, non existing visits return as `null` { "visit1": { "visitId": "visit1", "view": "port|terminal", "sof": { sof obj } }, "visit2": null // if the visit doesn't exist ... } |
| By ship imo and time range | GET /v2/sof/byImo/{imo} ?start=.. &end=.. [&view=port|terminal]POST /v2/sof/byImo [ { "imo": "1234567", "view": "port|terminal", "start": 123, "end": 456, // optional filters }, ... ] | Required   * `imo`: imo of the ship * `start`: time window start * `end`: time window end   Optional   * `finished=true|false` or omit / null for all * `categoriesV1` * `categoriesV2` * `deadWeightTonnages` range * `limit` newBlue | **GET response**  200 OK 404 Not Found: ship not found [ { "entryId": "visit1", sof obj }, ... ] **POST response** [ { "request": { "imo": "1234567", "view": "port|terminal", "start": 123, "end": 456, // optional filters }, "view": "port|terminal", "sof": { "entryId": "visit1" sof obj } }, ... ] |
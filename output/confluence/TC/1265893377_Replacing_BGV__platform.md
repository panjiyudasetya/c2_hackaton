---
id: confluence:1265893377
source: confluence
type: page
space: TC
title: Replacing BGV (platform)
author: Joost Laurman
date: '2026-07-01'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1265893377
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1265893377
---
# Replacing BGV (platform)

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1265893377  

## Content

## Introduction

**Blauwe Golf Verbindend** (BGV) is an external Dutch data service that provides real-time information about **inland waterway infrastructure** — specifically **berths, bridges, and locks**. In the platform, it's integrated as one of the external data sources for infrastructure updates.

### What the integration does in this codebase

1. **HTTP client** — `BlauweGolfVerbindendService` (Retrofit interface) calls the public REST API at `https://blauwegolfverbindend.nl/rest/information`, with three main endpoints:

   * `/berth` — berth listings + details (by ISRS code)
   * `/bridge` — bridge status + planned openings
   * `/lock` — lock listings + lock planning
2. **Adapter** — `BlauweGolfVerbindendMonitorAdapter` runs periodically and:

   * Pulls paginated berth/bridge/lock data from BGV
   * Updates internal berth records (dimensions, mooring info, occupancy, geometry)
   * Updates **bridge movements** (OPEN / CLOSED / OPENING / CLOSING / BLOCKED) and pushes short-term planned openings into the `infraMovementSubSystem`
   * Updates lock planning
   * **Normally runs every 5 minutes**
3. **Berth name mapping** — `BgvBerthMappingSubSystemImpl` loads a CSV that maps BGV/Pronto berth identifiers to Teqplay's internal berth names, so external references line up with the platform's infrastructure model.

On their website is stating that since 4 February 2026 it’s no longer functional. On other websites like [data.overheid.nl](http://data.overheid.nl) they are still stating that real-time bridge information is coming from BGV and that it’s only exposed on [vaarweginformatie.nl](http://vaarweginformatie.nl) as a service.

## Alternatives

RWS FIS ([vaarweginformatie.nl](http://vaarweginformatie.nl)) has a endpoint. This endpoint can fetch **bridge**, **lock** (chamber) and **berth** status changes since a specific timestamp.

jsonwide760{
"lastModificationTimeMs": 1782915161322,
"modifications": [
{ "modificationType": "UPDATE",
"status": {
"isrs": "NLRTM002010545700513",
"timestamp": 1782911506048,
"status": "CLOSED", // seen: OPEN, CLOSED, OPENING, UNKNOWN, BLOCKED
"hasPlannedOpenings": false,
"hasActiveObstructions": false
}
}, ...
]
}

It is keyed by ISRS code and it returns the changes that happened since the given timestamp. No official documentation could be found. Maybe we can ask for this somewhere?

## What BGV actually feeds into the platform

### **Startup-phase**

On startup the cache is still cold. So on the first run after a restart it does a `/details` call to ***every*** bridge, lock and berth. With that it creates in-memory caches that aren’t persisted. There is a cache for berths in Mongo.

### Phase 1

Every 5 minutes it fetches:

* `retrieveBerths()` — full list of every berth's `commonData` (isrs + name + lat/lon + `lastModification` timestamp)
* `retrieveLocks()` — full list of every lock's `commonData`
* `retrieveBridges()` — full list of every bridge's `commonData`

These calls return **all** items on every run, no delta filtering. Just the light "common data" — no status, no planning, no occupancy yet.

### Phase 2

For each item in the run it compares the `lastModification` from BGV time against the one we already cached before. Only if the timestamp is advanced we do a `/details/{isrs}` call to get:

* bridge → `bridgeStatus`, `plannedOpeningTimes[]`, `bridgeOpenings[]`, `obstructions[]`
* lock → `lockStatus`, `lockPlanning[]` (green/red light times), `obstructions[]`
* berth → occupancy fields + all static metadata

There is al fallback every 24h to fetch all data from BGV no matter if there was an update. Following reasons could be fixed with this:

* berth not yet in our DB, or
* never had an update time set, or
* exists but was never enriched by BGV before, or
* BGV bumped `lastModification` since we last stored it.

## How FIS can take-over

| **Need** | **RWS FIS availability** | **Endpoint** |
| --- | --- | --- |
| Bridge planning | Available in detail as `plannedOpenings` | `/frp/api/geodynamic/bridge/details/?isrs=...` |
| Bridge obstructions | Available in detail as `obstructions` | same bridge detail endpoint |
| Lock movements / planning | Available as chamber detail `plannedLockingTimes` | `/frp/api/geodynamic/chamber/details/?isrsCodes=...` |
| Lock/chamber obstructions | Available as chamber detail `obstructions` | same chamber detail endpoint |
| Static bridge/lock/chamber data | Available via current FIS geo/VNDS API | `/frp/api/geo/all?types=BRIDGE` |

The delta/summary feeds are:

* Bridges: `/frp/api/geodynamic/bridge/status/?timestampSinceMs=0`
* Chambers: `/frp/api/geodynamic/chamber/status/?timestampSinceMs=0`

Bridge summaries include:

wide760{
"isrs": "...",
"timestamp": 1782932412911,
"status": "CLOSED",
"hasPlannedOpenings": true,
"hasActiveObstructions": false
}

Bridge detail shape:

wide760{
"bridgeStatus": { "...": "..." },
"sailingDirection": "UNKNOWN",
"plannedOpenings": [],
"obstructions": []
}

Chamber detail shape:

wide760{
"name": "Sluiskolk Oostsluis Terneuzen",
"chamberStatus": { "...": "..." },
"plannedLockingTimes": [],
"obstructions": []
}

So the migration implication should be adjusted slightly:

* `status`: no BGV detail call needed; inline in FIS geodynamic summary.
* `planning`: use FIS bridge `plannedOpenings` and chamber `plannedLockingTimes`.
* `lockMovements`: use chamber status/details, then aggregate to lock if your model needs lock-level output.
* `obstructions`: use FIS bridge/chamber `obstructions`.
* `static`: use FIS geo/VNDS, not BGV.
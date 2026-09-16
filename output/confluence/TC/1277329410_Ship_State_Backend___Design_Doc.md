---
id: confluence:1277329410
source: confluence
type: page
space: TC
title: Ship State Backend — Design Doc
author: Michel Wilson
date: '2026-07-09'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1277329410
explicit_links:
- jira:ISO-8601
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1277329410
---
# Ship State Backend — Design Doc

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1277329410  

## Content

## 1. Overview

### Problem statement

Several internal consumers need a fast answer to "what do we currently know  
about ship X (by MMSI)?" — its latest reported name/location/speed, its  
resolved true destination, and when it last took on bunkers. Today this  
information is scattered across the `ais-diff` and `events` RabbitMQ streams  
with no single queryable "current state" store, and no direct-Redis access  
pattern exists for internal services (everything today goes over HTTP).

### Goals

* Keep AIS-based state keyed by MMSI
* Maintain one Redis record per MMSI holding: name, location, speed, true  
  destination, and last bunker-encounter timestamp.
* Keep that record up to date by consuming the `ais-diff` and `events`  
  queues.
* Expose the state to other internal services via a new, low-latency  
  **direct-Redis client library** (no network hop through an API).
* Expose the same state over HTTP via new endpoints on the existing `api`  
  project, using that same client library.

### Non-goals

* The scope is to store AIS-based data only, not other data such as portcall information
* This is **not** a historical/time-series store — only the latest known  
  value per field is kept, no history of past states.
* This service does **not** call `portmatcher` itself. Destination  
  resolution happens upstream (see §4); we only consume the already-resolved  
  value.
* Not an event-sourcing system — no replay, no audit log of state  
  transitions, just a current-state cache.

## 2. Architecture

wide760 ┌──────────────┐ ┌──────────────┐
│ ais-diff queue│ │ events queue │
└──────┬───────┘ └──────┬───────┘
│ │
▼ ▼
┌────────────────────────────────────────┐
│ ship-state-backend (new, │
│ standalone service) │
│ - ais-diff consumer │
│ - events consumer │
│ (filters: true-destination-changed, │
│ encounter-end where type=BUNKER) │
└───────────────────┬─────────────────────┘
│ per-field HSET
▼
┌───────────────┐
│ Redis │
│ ship-state: │
│ current:{mmsi}│
└───────┬───────┘
│ read-only
┌─────────────┴──────────────┐
▼ ▼
┌──────────────────┐ ┌───────────────────┐
│ ship-state-client │◄────────┤ api project │
│ (new Kotlin lib, │ depends│ GET /v1/ship-state │
│ direct Redis read)│ │ /{mmsi} │
└─────────┬─────────┘ └───────────────────┘
│
▼
other internal services
(depend on the client lib
the same way `api` does)

The new service (`ship-state-backend`) is a **standalone deployable**, not a  
new module inside `ais-engine`. It depends on `ais-engine`'s published  
`models` Maven artifact for the shared message/event schemas  
(`AisDiffMessage`, `TrueDestinationChangedEvent`, `EncounterEndEvent`, etc.)  
but owns its own RabbitMQ listener wiring rather than reusing  
`ais-engine`'s internal `rabbitmq-ais` / `rabbitmq-event` library modules.

## 3. Redis data model

**Key:** `ship-state:current:{mmsi}` — matches the existing  
`<module>:<entity>:<id>` convention used by `ais-engine`'s monitor apps  
(e.g. `stop-monitor:stop-state:{mmsi}`).

**Structure:** Redis **hash**, written via individual field operations  
(`HSET`) rather than a single serialized JSON blob — see §4 for why.

| Field | Type | Present when |
| --- | --- | --- |
| `name` | string | Once first `ais-diff` message with a name seen |
| `lat` | double | Once first `ais-diff` message seen |
| `lon` | double | Once first `ais-diff` message seen |
| `speedOverGround` | float | Once first `ais-diff` message with speed seen |
| `trueDestination` | string | Once a `TrueDestinationChangedEvent` with a non-null `trueDestination` is seen; absent until then, and can revert to absent if a later event resolves to `null` |
| `lastBunkerEncounterTime` | ISO-8601 instant | Once the ship has been the *bunkered* vessel in at least one **valid** `BUNKER` encounter; absent until then |

**Missing fields:** callers must treat any of the above as optional/absent —  
a ship with no bunker history simply has no `lastBunkerEncounterTime` field,  
not a null placeholder. Same for `trueDestination` before resolution.

**TTL:** exposed as a **configurable** property on the service (e.g.  
`ship-state.redis.ttl`), **disabled by default** to match existing  
`ais-engine` Redis usage (none of which uses TTL today). This is a knob to  
tune later once real MMSI cardinality / Redis memory usage is understood —  
not a fixed policy baked into the schema.

**Schema evolution:** because fields are named (not a serialized blob),  
adding new fields is naturally backward/forward compatible — old readers  
ignore fields they don't recognize, and a missing field just reads as  
absent. Given the schema isn't expected to see more than incremental field  
additions, this doc recommends treating it as **append-only** (never  
repurpose a field name or silently change its type/meaning) and  
deliberately **skips an explicit** `schemaVersion` field as unneeded  
overhead for now. If a genuinely breaking change is ever needed, prefer  
introducing a new field name and migrating readers over reinterpreting an  
existing one.

## 4. Message consumption & merge design

Two independent consumers (`ais-diff`, `events`) update the same per-MMSI  
record without coordinating with each other. This is the central risk the  
handover asked to be flagged explicitly.

**The risk:** if the service followed `ais-engine`'s existing  
`@RedisHash` + `CrudRepository.save()` convention literally, each consumer  
would read the *whole* record, modify its own fields, and write the whole  
record back. Two consumers doing this concurrently for the same MMSI can  
lose each other's updates (classic read-modify-write race) — e.g. an  
`ais-diff` update to `speedOverGround` could clobber a `trueDestination`  
value written moments earlier by the events consumer, or vice versa.

**Recommendation:** use `RedisTemplate`'s **hash operations** to `HSET`  
only the specific fields each consumer owns:

* `ais-diff` consumer writes: `name`, `lat`, `lon`, `speedOverGround`  
  (extracted from `AisDiffMessage`'s `AisDiffField<T, U>` wrappers via  
  `.latest()`).
* `events` consumer writes:

  + `trueDestination`, from `TrueDestinationChangedEvent.trueDestination`  
    (already portmatcher-resolved upstream — see below).
  + `lastBunkerEncounterTime`, from `EncounterEndEvent.actualTime`, **only**  
    **when** `encounterType == BUNKER` **and** `valid == true`.

Because each consumer only ever writes its own fields, and Redis hash field  
writes are atomic, there is no lost-update race — this avoids the problem  
entirely without needing in-process locking or a single-writer thread. This  
is a deliberate deviation from the whole-object `@RedisHash`/  
`CrudRepository` pattern used elsewhere in `ais-engine`, chosen specifically  
because (unlike those single-consumer monitor apps) this service has two  
independent writers touching the same key.

**Which vessel gets the bunker timestamp:** `EncounterEndEvent` carries both  
`ship` and `otherShip`. For `BUNKER`-type encounters, `encounter-monitor`'s  
detection logic enforces (not incidentally) that `ship` is always the  
**main vessel being bunkered** and `otherShip` is always the **service**  
**vessel** (the bunker tanker/barge). Only `event.ship.mmsi`'s  
`lastBunkerEncounterTime` is updated — the supplier vessel (`otherShip`) is  
not touched, since the goal is to record when a ship last took on fuel, not  
track supplier activity.

**Portmatcher:** resolution of the raw AIS destination string into a  
normalized port happens entirely upstream, in an external Platform service,  
before `TrueDestinationChangedEvent` is published to the `events` queue.  
This service does not call portmatcher and has no dependency on it — it  
only consumes the already-resolved `trueDestination` field.

## 5. Client library design

* **Language:** Kotlin, published as a Maven artifact from the same  
  `ship-state-backend` repo.
* **Connectivity:** Spring Data Redis (`RedisTemplate`/Lettuce), connecting  
  directly to the same Redis instance the consumer service writes to.
* **Interface**, modeled on the existing `ShipCurrentClient` shape (from  
  `ais-engine`'s `client-ship-history` module) for consistency with how  
  internal clients already look:

  kotlininterface ShipStateClient {
  fun findByMmsi(mmsi: Int): ShipState?
  fun findByMmsiList(mmsis: List<Int>): Map<Int, ShipState>
  fun findAll(): Flow<ShipState> // Or some other async mechanism
  }
  data class ShipState(
  val mmsi: Int,
  val name: String?,
  val lat: Double?,
  val lon: Double?,
  val speedOverGround: Float?,
  val trueDestination: String?,
  val lastBunkerEncounterTime: Instant?,
  )
* **Error handling:** if Redis is unavailable, the client retries with  
  backoff (a small retry wrapper of its own, shaped like `ais-engine`'s  
  `@RedisRetryable` — reusing that annotation directly wasn't judged worth  
  pursuing since it isn't published outside `ais-engine`). After retries  
  are exhausted, the client throws rather than silently returning `null`,  
  so callers can distinguish "unknown ship" from "store unavailable."
* **Configuration:** Redis connection details (host/port/credentials) are  
  injected via a Kubernetes ConfigMap — consistent across the service and  
  every consumer of the client library, including `api`. No new  
  secrets-distribution mechanism is needed.

## 6. REST API design (`api` project)

New controller following the existing `/v1/` versioning and  
Controller → Service → Client layering already used in `api` (see  
`UabAisController`, `AuthController`).

**Endpoint:** `GET /v1/ship-state/{mmsi}`

* **Auth:** Keycloak-protected like existing endpoints, gated behind a new  
  `ship-state` scope.
* **Response (200):**

  json{
  "mmsi": 244660338,
  "name": "EXAMPLE VESSEL",
  "location": { "lat": 51.9225, "lon": 4.47917 },
  "speedOverGround": 12.4,
  "trueDestination": "BEANR",
  "lastBunkerEncounterTime": "2026-06-30T14:22:00Z"
  }

  Fields with no known value are simply omitted (matching the Redis  
  model), except `mmsi` which is always present.
* **Not found (404):** returned via a custom exception + `@ResponseStatus`  
  (matching `api`'s existing error-handling convention) when the MMSI has  
  no record in Redis at all.
* **Scope:** single-MMSI lookups only for now. A batch endpoint is a natural future  
  extension but is out of scope until there's real demand for it.

`api` will depend on the `ship-state-client` library directly to serve this  
endpoint — this is a new category of dependency for `api` (direct Redis  
network access), which today only talks to other services over HTTP.

## 7. Future expansion

* **Canceling events:** if in the future it becomes possible for Vesselvoyage to cancel a bunker event or an area event, the proposed plan ahead is to create a REST connection between Vesselvoyage and the ship state service with which Vesselvoyage can remove the last bunker time and update it with an older value.
* **Store more event info:** record the ongoing area/berth events and other start/end events (encounters, stops …)
* **Indices:** be able to retrieve vessels via other mechanisms, such as by true destination, by area?
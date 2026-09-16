---
id: confluence:652148746
source: confluence
type: page
space: TC
title: Prediction API (in platform)
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652148746
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652148746
---
# Prediction API (in platform)

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652148746  

## Content

Documentation about the API for making ETA/ETD predictions. You can predict ETAs and ETDs for a journey, for example ETA NLRTM, ETD NLRTM and ETA USHOU. It's possible to return route polylines, debug info and use more fine-grained setings.

* all timestamps are milliseconds since epoch
* all durations are in milliseconds
* all speeds are in knots

## Contents

* API
* Features
* Input
* Output
* Examples
* Features (explained)

# API

POST /ship/predict
body: PredictionInput
return: PredictionOutput

# Features

* minimal required input & fine-grained control via opt-in flags and settings
* dealing with errors & exposing used locations
* cache control
* reproducibility
* client library (via skeleton-plugins)

*These features are explained under* `Features (explained)` *on the bottom of this doc, it's encouraged to keep reading though if you haven't before.*

# Input

## Models

\* = required
? = conditionally required (either one value or another, supplying both is allowed occasionally)
= not required, automatically defaulted

### PredictionInput

{
? "imo": string | null, // default `null`
? "mmsi": string | null, // default `null`
"strict": boolean, // default `false`
"overwrite": PredictionShip | null, // default `null`
\* "chain": boolean,
\* "requests": Array<PredictionRequest>,
"flags": PredictionFlags // defaulted if not specified
}

* IMO or MMSI or both (IMO is first searched, if not found then MMSI is used as fallback)

| field | description |
| --- | --- |
| `imo`, `mmsi` | identifiers of the ship |
| `strict` | whether the request should be treated in "strict mode", no default values will be returned, use of proper predictors will be enforced |
| `overwrite` | overwrite the initial ship details |
| `chain` | whether the `requests` need to be chained, meaning it indicates a journey\* of a ship where the starting and ending times need to be linked |
| `requests` | the prediction requests that need to be turned into responses |
| `flags` | optional flags denoting what optional information can be toggled on/off |

### PredictionShip

{
\* "speedOverGround": number,
\* "timeLastUpdate": number,
\* "location": Location
}

* ship object used when overwriting

### Location

{
\* "latitude": number,
\* "longitude": number
}

### PredictionFlags

{
"route": boolean, // default `false`
"routeId": boolean, // default `false`
"path": boolean, // default `false`
"debug": boolean, // default `false`
}

* Every visit and voyage have these fields, but they are always default to `null`. If a flag like `route` is enabled here, then all segments will contain a field named `route` containing the route as polyline. Which can be shown on the map with a [Polyline decoder](http://polylinedecode.teqplay.nl/).

### PredictionRequest

type PredictionRequest = VisitPrediction | VoyagePrediction
interface PredictionRequest {
// depending on which type of prediction
// - visit prediction = ETD for a specific location
// - voyage prediction = ETA for a journey between two locations
"predictionType": "VISIT" | "VOYAGE",
"id": string | null // default `null`
}

| field | description |
| --- | --- |
| `id` | an optional id of the request, is passed verbatim in the response as well |

**VisitPrediction**

{
\* "predictionType": "VISIT",
"id": string | null, // default `null`
\* "location": PredictionLocation,
"ata": number | null, // default `null`
"resolveAta": boolean | null, // default `null`
"manualDuration": number | null, // default `null`
"durationCorrection": boolean | null // default `null`
}

| field | description |
| --- | --- |
| `ata` | the starting time at this location, can be provided if you know it in advance already |
| `resolveAta` | whether the `ata` should automatically be resolved by looking for events (port start events if `unlocode` is specified in the `location` |
| `manualDuration` | whether the duration should be overwritten by the specified manual duration, when you want to use/force a custom duration (the amount you expect to wait at the specified `location`) |
| `durationCorrection` | whether the duration and ETD should be corrected so they will not result in an ETD in the past by setting this flag you ensure that the resulting ETD will always be later or equal to the request time |

**VoyagePrediction**

{
\* "predictionType": "VOYAGE",
"id": string | null, // default `null`
\* "from": PredictionLocation,
\* "to": PredictionLocation,
"manualSpeed": number | null, // default `null`
"fallbackWhenBelowMinimumSpeed": boolean | null, // default `null`
}

| field | description |
| --- | --- |
| `manualSpeed` | whether the speed should be overwritten by the specified manual speed, when you want to use/force a custom speed |
| `fallbackWhenBelowMinimumSpeed` | normally an ETA prediction will fail if the speed is too low, by enabling this fallback only speeds that are high enough will be used |

About `fallbackWhenBelowMinimumSpeed`  
There are several available speeds: manual speed, prediction speed, ship speed, average speed and default speed

If the `manualSpeed` is specified, then `fallbackWhenBelowMinimumSpeed` will have no effect.

Some scenarios:

* `fallbackWhenBelowMinimumSpeed=false`; the ship speed will be used, unless the prediction speed is available
* `fallbackWhenBelowMinimumSpeed=true`; the first speed will be used that's not below the minimum speed: prediction speed, ship speed or average speed, if all are below then the default speed will be used
* `fallbackWhenBelowMinimumSpeed=true, strict=true`; if `strict` is also set and a default speed was used, then the segment will get an `error=true`

*Note: this object also supports* `forceGenericPredictor: boolean | null` *and* `checkMovingToPort: boolean | null`*, those are only used for backwardscompatibility though, and shouldn't be used*

### PredictionLocation

{
? "shipLocation": boolean | null, // default `null`
? "unlocode": string | null, // default `null`
? "berthId": string | null, // default `null`
? "point": Location | null, // default `null`
}

* only one must be specified
* `berthId` can be the `berthId`, `berthName` or `berthNameLong`
* in the output the `point` will always be filled in with the used coordinates

# Output

## Models

### PredictionOutput

{
"requestId": string,
"requestTime": number,
"ship": ShipInfo,
"imo": string | null,
"mmsi": string | null,
"strict": boolean,
"overwrite": PredictionShip | null,
"chain": boolean,
"responses": Array<PredictionResponse>,
"flags": PredictionFlags,
"reproducible": boolean,
"requester": PredictionRequester
}

* for more info about the `reproducible` field, see `Features (explained) > Reproducibility`

### PredictionRequester

{
"type": "USER" | "INTERNAL",
"name": string
}

### PredictionResponse

type PredictionResponse = PredictedVisit | PredictedVoyage
interface PredictionResponse = {
"predictionType": "VISIT" | "VOYAGE", // depending on which type of prediction
"id": string | null,
"duration": number,
"error": boolean,
"errorType": PredictionErrorType | null,
"errorMessage": string | null,
"calculatedAt": number,
"calculationTime": number,
"accuracy": number | null,
"route": string | null,
"routeId": string | null,
"path": Array<HistoricShipInfo> | null,
"distance": number | null,
"debug": DebugPredictionObject | null
}
enum PredictionErrorType {
LOCATION\_MULTIPLE\_PROVIDED,
LOCATION\_NOT\_FOUND,
TOO\_LOW\_SPEED,
DEFAULT\_PREDICTOR\_NOT\_ALLOWED,
NO\_SUITABLE\_PREDICTOR
}
interface DebugPredictionObject {
"predictor": PredictorType
}

**PredictedVisit**

type PredictedVisit = {
...VisitPrediction,
...PredictionResponse,
"location": PredictionLocation,
"errorMargin": number | null,
"etd": number,
"debug": DebugVisitPredictionObject | null
}
type DebugVisitPredictionObject = {
"predictor": PredictorType
}

* `errorMargin` is an error margin around the `duration` in hours

**PredictedVoyage**

type PredictedVoyage = {
...VoyagePrediction,
...PredictionResponse,
"from": PredictionLocation,
"to": PredictionLocation,
"eta": number,
"distance": number,
"debug": DebugVoyagePredictionObject | null
}
type DebugVoyagePredictionObject = {
"predictor": PredictorType,
"speed": VoyageSpeed
}
type VoyageSpeed = {
"value": number,
"predictor": SpeedPredictorType
}

# Examples

*Note: these examples mostly use* `chain=true`*, it's also possible to use* `chain=false` *but that's mostly only useful for a really specific use case. Let's not get into details about that just yet and start of with some simpler examples first.*

When switching on `chain` you will opt into some nice benefits. Good to know though this also enforces one extra rule:

* the "start"/from location must always match the "end"/to location of the previous request item, so

  + ship => NLRTM, NLRTM => USHOU is valid
  + ship => NLRTM, ship => USHOU is NOT valid

You will benefit from:

* the ETAs and ETDs will automatically be calculated for you, when you specify a voyage from the current ship location to NLRTM and after a voyage to USHOU then the ETA of USHOU will also take into account the sailing to NLRTM first as well
* if any item has `error=true`, then all subsequent items will also have this flag set, as the requests represent a journey as a chain. You can use all prediction responses that have `error=false`, even if predictions at some point have `error=true`

To demonstrate the difference between `chain=true` and `chain=false`:

|  | duration | `chain=true` | `chain=false` |
| --- | --- | --- | --- |
| voyage: ship => NLRTM | 1500 | ETA 1500 + current time | ETA 1500 + current time |
| visit: NLRTM | 50 | ETD 50 + 1500 (previous) = 1550 | ETD 50 + current time |
| voyage: NLRTM => USHOU | 3000 | ETA 3000 + 1550 (previous) = 4550 | ETA 3000 + current time |

As you can see, starting from the second entry, the duration of the current item will be summed with the previous time if `chain=true`. `chain=false` will simply copy the duration and sum it only with the current time to get a time in the future. This also demonstrates why you'll most likely only need to use `chain=true`. And when the need arises to switch to `chain=false`, keep in mind that the ETA/ETD calculation will change.

1. **Voyage from current ship location to NLRTM**

Let's say you want to know when a specific vessel will enter NLRTM (using a voyage prediction).

{
"imo": "9328053",
"chain": true,
"requests": [
{
"predictionType": "VOYAGE",
"from": { "shipLocation": true },
"to": { "unlocode": "NLRTM" }
}
]
}

*Note: if the vessel is anchored or laying still in general, an ETA cannot be calculated. If you encounter an* `error=true` *then please select a vessel which is sailing towards NLRTM at the moment of requesting, so you get a proper ETA/voyage prediction*

2. **Voyage from NLRTM to USHOU**

Let's say you also want to know how long this vessel will sail from NLRTM to USHOU.

{
"imo": "9328053",
"chain": true,
"requests": [
{
"predictionType": "VOYAGE",
"from": { "unlocode": "NLRTM" },
"to": { "unlocode": "USHOU" }
}
]
}

3. **Voyage from NLRTM to USHOU including route**

At this point you might be curious what route would be taken by this vessel while sailing between NLRTM and USHOU.

By default the route isn't returned, but a flag can be turned on to return a route polyline if it's available (turn on `flags.route`)

{
"imo": "9328053",
"chain": true,
"requests": [
{
"predictionType": "VOYAGE",
"from": { "unlocode": "NLRTM" },
"to": { "unlocode": "USHOU" }
}
],
"flags": { "route": true }
}

You can now find a `route` field inside the predicted voyage object, you can copy this polyline and plot it on a map to view it (for example with a [Polyline decoder](http://polylinedecode.teqplay.nl/)).

4. **Chained voyage predictions**

Up to this point you did two voyage predictions, viewed a predicted route and you gathered two durations and ETAs.

* one duration and ETA for the voyage; ship => NLRTM
* one duration and ETA for the voyage; NLRTM => USHOU

At this point you could realize the ETA for NLRTM => USHOU is "incorrect", you'd rather want to know what the ETA would be if the vessel first sails to NLRTM and to USHOU after.

You can accomplish this by combining both voyage predictions in the same request. It's really important that `chain` is set to `true` for this scenario, it will make sure that the ETA of the NLRTM=>USHOU voyage will be shifted by the time that is taken for all previous voyages+visits (in this example the voyage to NLRTM).

{
"imo": "9328053",
"chain": true,
"requests": [
{
"predictionType": "VOYAGE",
"from": { "shipLocation": true },
"to": { "unlocode": "NLRTM" }
},
{
"predictionType": "VOYAGE",
"from": { "unlocode": "NLRTM" },
"to": { "unlocode": "USHOU" }
}
]
}

5. **Visit prediction for NLRTM**

The vessel will probably not sail that long journey without doing some operations in NLRTM first. To request the time taken within a port you can do a visit prediction for a supplied `unlocode`.

{
"imo": "9328053",
"chain": true,
"requests": [
{
"predictionType": "VISIT",
"location": { "unlocode": "NLRTM" }
}
]
}

6. **Combining voyage & visit predictions (ship=>NLRTM=>USHOU)**

By combining voyage & visit predictions you can get:

* ETA NLRTM; *a voyage from the current ship location => NLRTM*
* ETD NLRTM; *a visit for NLRTM*
* ETA USHOU; *a voyage from NLRTM => USHOU*

{
"imo": "9328053",
"chain": true,
"requests": [
{
"predictionType": "VOYAGE",
"from": { "shipLocation": true },
"to": { "unlocode": "NLRTM" }
},
{
"predictionType": "VISIT",
"location": { "unlocode": "NLRTM" }
}
{
"predictionType": "VOYAGE",
"from": { "unlocode": "NLRTM" },
"to": { "unlocode": "USHOU" }
}
]
}

7. **Dealing with reality**

It seems like NLRTM is really busy at the moment, and your vessel can't enter immediately. We still want to predict our ETAs/ETDs but we also want to take into account that we will arrive in NLRTM a bit later. Although the vessel has to wait for a moment, we luckily (somehow) know it will only take about one hour before the vessel can enter.

We can indicate a vessel will stay in its current position for an X amount of time by using a visit prediction as well.

{
"imo": "9328053",
"chain": true,
"requests": [
{
"predictionType": "VISIT",
"location": { "shipLocation": true },
"ata": 1640255573376,
"manualDuration": 3600000
},
{
"predictionType": "VOYAGE",
"from": { "shipLocation": true },
"to": { "unlocode": "NLRTM" }
},
... // omitted for brevity
]
}

We specify the `manualDuration` with `1 hour = 3.600.000 ms`, and supply an `ata` as well. The `ata` is really important in this scenario because we need a set moment in time when the 1 hour "countdown" started ticking.

(If we wouldn't have supplied an `ata` it would always use the current time as reference, so when requesting predictions every 10 minutes our predictions would shift by 10 minutes every time as well because of the passing of time.)

8. **Dealing with uncertainty**

Sadly reality will not always hold true. Although we know that the vessel can enter in about an hour, it might be that the vessel still can't enter by then. So, we know the vessel will need to stay for at least an hour, whenever the vessel can actually start moving in we will get an update (by someone) that the vessel is moving. After that point we can stop making this first visit prediction and just continue with our voyage prediction of ship=>NLRTM as before.

{
"imo": "9328053",
"chain": true,
"requests": [
{
"predictionType": "VISIT",
"location": { "shipLocation": true },
"ata": 1640255573376,
"manualDuration": 3600000,
"durationCorrection": true
},
{
"predictionType": "VOYAGE",
"from": { "shipLocation": true },
"to": { "unlocode": "NLRTM" }
},
... // omitted for brevity
]
}

We just added `durationCorrection=true`, by doing this we are essentially telling the predictor:

> "I know the vessel will need to stay for at least an hour, but I'm not sure if it will need to stay for longer. If it does I will still keep using the same input for my predictions. But I expect the predictor to shift the predictions and take into account that the stay might be longer than manually specified."

A bit more technical explanation:

eta = ata + manualDuration
if durationCorrection and eta < currentTime:
eta = currentTime
return eta

9. **Dealing with (lack of) pre-existing knowledge**

Alright, the vessel was finally able to enter NLRTM. But now we want to know when it will exit! (and what its ETA USHOU will be)

Let's say we have some pre-existing knowledge:  
We know the ATA NLRTM for the vessel and we want to supply that to the predictor.

{
"imo": "9328053",
"chain": true,
"requests": [
{
"predictionType": "VISIT",
"location": { "unlocode": "NLRTM" },
"ata": 1640255573376
},
{
"predictionType": "VOYAGE",
"from": { "unlocode": "NLRTM" },
"to": { "unlocode": "USHOU" }
}
]
}

We supply the known `ata` to the predictor and our `etd` will be `ata + predicted duration`. (again if we suspect the stay might be longer than predicted then we could also supply `durationCorrection=true` here, so the USHOU ETA will be shifted by any extra time taken)

Let's say we have no pre-existing knowledge:  
We only know the vessel entered NLRTM, but we have no clue about its ATA.

{
"imo": "9328053",
"chain": true,
"requests": [
{
"predictionType": "VISIT",
"location": { "unlocode": "NLRTM" },
"resolveAta": true
},
{
"predictionType": "VOYAGE",
"from": { "unlocode": "NLRTM" },
"to": { "unlocode": "USHOU" }
}
]
}

By supplying `resolveAta=true` we tell the predictor to resolve the ATA for us. The predictor will search for all recent events for this vessel in NLRTM and use the found ATA. We could save the resolved ATA now and use it in subsequent requests to save the predictor some computation time later (so supplying the `ata=...` and removing the `resolveAta=true`).

**10. Optimizing predictions by "tagging" segments**  
Let's say we'd like to make >5.000 prediction requests for a given data set. Performance-wise we might consider sending only 100 prediction requests per API request, as to not to stress the API too much.

To do this we might manually split our >5.000 prediction requests into chunks of 100, send our requests and then say:

* prediction request 0 = request 1, index 0
* prediction request 1 = request 1, index 1
* ...
* prediction request 101 = request 2, index 1
* ...
* prediction request 5285 = request 86, index 85

Quite cumbersome, as we now need to handle chunking our requests, keeping track of request counts and indices and also passing our results into the right place.

Instead of doing that, we can use IDs per segment!

Let's say those >5.000 prediction requests were actually all about different voyages from the current ship location to different ports all over the world. It could be that we'd like to plot all ports and how long it takes for this ship to get there.

We could then set the `id` of every voyage to the port the ship is heading to in that request. So something like:

* prediction request, ship => NLRTM = `id=NLRTM`
* prediction request, ship => BEANR = `id=BEANR`
* prediction request, ship => USHOU = `id=USHOU`
* ...

Instead of keeping track of different requests and all their indices, we could now send all requests, get all responses and merge them all into one big responses list. If we want to combine our prediction to specific ports now, we can just search them by their ID. So for NLRTM we just search for one prediction response where `id=NLRTM`, etc. etc.

**11. "Hyper-optimizing" predictions by combining multiple requests into one**  
In the beginning we recommended using `chain=true` because of the benefits you get for free. You can also use `chain=false`, this will mostly have the following impact:

* you can't use the ETAs and ETDs as you would with `chain=true`, if certain segments should be chained you'd need to do the ETA/ETD calculation manually yourself

Opting out of chaining also gives you some really powerful capabilities, but also can become quite complex quite quickly.

Imagine the following use case:

> A vessel is guaranteed to visit NLRTM, NLAMS and BEANR. Our client needs to make an informed decision; "what route should I take and which port should I visit first?", as visiting a port could take a varying amount of time and there could be restrictions; like not being allowed to sail directly from BEANR to NLRTM. Our client also mentions knowing that in BEANR specific berth has been reserved, so we know beforehand our visit will take about 3 hours. And, as if that wasn't enough, we also want to show to our client exactly which route the vessel would need to sail to accomplish this ETA!

This already starts off quite complex, and trying to use `chain=true` would not be practical. You'd need to brute force all possibilities beforehand and then make N requests. It's definitely not recommendable (or even viable) to do that!

Let's first identify all possibilties:

ship can sail from its current ship location to:
- NLRTM
- NLAMS
- BEANR
ship will visit:
- NLRTM
- NLAMS
- BEANR (we know specifically which berth and how long the visit will take)
ship can sail the following voyages:
- NLRTM => NLAMS, NLRTM => BEANR
- NLAMS => NLRTM, NLAMS => BEANR
- BEANR => NLAMS (as mentioned before, sailing directly from BEANR => NLRTM is not allowed)

As chaining has been turned off, we can actually send these prediction requests all at once!

{
"imo": "9328053",
"chain": false,
"requests": [
// voyages from the current ship location to all available ports
{ "predictionType": "VOYAGE", "from": { "shipLocation": true }, "to": { "unlocode": "NLRTM" } },
{ "predictionType": "VOYAGE", "from": { "shipLocation": true }, "to": { "unlocode": "NLAMS" } },
{ "predictionType": "VOYAGE", "from": { "shipLocation": true }, "to": { "unlocode": "BEANR" } },
// all visit durations for all available ports
{ "predictionType": "VISIT", "location": { "unlocode": "NLRTM" } },
{ "predictionType": "VISIT", "location": { "unlocode": "NLAMS" } },
{
"predictionType": "VISIT",
"location": { "berthId": "OUR\_BEANR\_BERTH\_ID" },
"manualDuration": 10800000
},
// and finally the available voyages
{ "predictionType": "VOYAGE", "from": { "unlocode": "NLRTM" }, "to": { "unlocode": "NLAMS" } },
{ "predictionType": "VOYAGE", "from": { "unlocode": "NLRTM" }, "to": { "berthId": "OUR\_BEANR\_BERTH\_ID" } },
{ "predictionType": "VOYAGE", "from": { "unlocode": "NLAMS" }, "to": { "unlocode": "NLRTM" } },
{ "predictionType": "VOYAGE", "from": { "unlocode": "NLAMS" }, "to": { "berthId": "OUR\_BEANR\_BERTH\_ID" } },
{ "predictionType": "VOYAGE", "from": { "berthId": "OUR\_BEANR\_BERTH\_ID" }, "to": { "unlocode": "NLAMS" } }
],
"flags": { "route": true }
}

Quite some predictions all together! We now know all the different segments, how long they will take and maybe even which segments turn out not to be possible.

We can now calculate all the routes for our client at our end. Finding out which route is optimal (maybe even considering eco-friendliness or waiting times). Putting the optimal route in order and grabbing all `route` items to transform it into one big polyline showing the optimal route!

We can also optimize our requests by saving all segments that will not change (the `duration` between for example NLRTM=>NLAMS or NLAMS=> BEANR will not change). So when we want to calculate again which port can be reached closest, we'd only need to redo all ship => [PORT] predictions. Also if a certain requirement changes we can make a specific request only for that change, without having to bother the API with all the possibilites again.

# Features (explained)

## Minimal required input & fine-grained control via opt-in flags and settings

One can start sending requests fairly quickly, only needing to specify which ship it's about and the from/to locations. Additional fields can be returned via flags, for example the `route` that's taken or `debug` info. Additional fields on a voyage or visit can also be opted-in to, like `manualSpeed` or `manualDuration`.

This API ensures all non-required settings are defaulted, as additional flags/settings are only required if you need more control/specific outcomes.

## Dealing with errors & exposing used locations

**Dealing with errors**  
There are two types of errors you can expect:

* request-based errors
* segment-based errors (error on a voyage/visit basis)

Request-based errors will only occur if: you have malformatted the request or the ship doesn't exist (or when `chain=true` if the content of the request is malformatted)

Any other error will be caught by the segment-based errors. Every voyage and visit also exposes `error`, `errorType` and `errorMessage`. The API will always return a `responses` list that has the same N size as the initial `requests` list size. Errors are indicated via `error=true`, which tells you the prediction results may not be used for that segment (you may however use the `errorType`, `errorMessage` or optional `debug` info to trace where the prediction goes wrong). The `errorType` uses an enum that identifies a specific "error type" (like `LOCATION_NOT_FOUND`). The `errorMessage` is an optional human-readable error message that can provide more details to the occurred error.

**Exposing used locations**  
When using `shipLocation`, `unlocode` or `berthId` as a location within your request. On response, the `point` of that location will always be set to:

* `shipLocation=true`, the ship location
* `unlocode`, the port location
* `berthId`, the berth location

This provides itself useful if you'd like to plot all locations and routes on a map for example.

## Cache control

All requests that are made can be specified as "segments", where you can have voyage and visit segments. All different segments can be cached individually with different TTLs if so desired.

*Note: caching is currently not implemented, but the following pointers can be used for implementation:*

Important to note though, when to "cache bust"? This differs per segment "type":

* voyage between NLRTM => USHOU can be cached for longer in general (keep in mind that a cached voyage NLRTM=>USHOU can't be the same item for a voyage NLRTM=>USHOU AND `manualSpeed=10`, the "base" segment must be cached, so the raw route from NLRTM=>USHOU and the modifiers like `manualSpeed` and `fallbackWhenBelowMinimumSpeed` can/must be applied later to that cached item)
* voyage between ship location => NLRTM, could be calculated on the fly every time it's required, or it could be cached as long as there is no new ship update yet (new location and time)
* visit at NLRTM, can be cached but only for that specific ship or within its category (a TANKER might take less/more time than a CARGO)

## Reproducibility

The `reproducible` flag denotes if the request is reproducible. (The `requester` object indicates which user/internal component requested predictions)

To reproduce the request you have to re-construct the input and overwrite the ship info (so it's inline with the ship details used in the initial request.

You can use the following steps to ensure reproducibility:

1. Copy `imo`, `mmsi`, `strict`, `chain` and `flags`
2. Copy `overwrite`, this ensures that the ship details are inline with the initial request
3. The `responses` in the output object need to be turned into `requests` in the input object, per item in the list:

   * as the `PredictionResponse` object is a superset of `PredictionRequest` you can copy the object as a whole and only make one small modification
   * in the `from`, `to` and `location`, ensure that only one field is specified (only pass `shipLocation`, `unlocode` or `berthId` if it exists, otherwise only pass `point`)

## Client library (via skeleton-plugins)

A client library for this API resides in the `skeleton-plugins:platform-client` package.

There are two steps we'll go through in using the client library:

* the initial step, using a `FutureShipClient` to send requests
* the next(/better) step, using the `ShipPredictionClient` wrapper

### FutureShipClient

By calling `predict` on an instance of `FutureShipClient` you can pass a `PredictionInput`, a request will be made for you and a `PredictionOutput` will be returned.

Example in Kotlin (see Example #6 for the JSON body that is generated for this request):

val shipLocation = PredictionLocation(shipLocation = true)
val portNLRTM = PredictionLocation(unlocode = "NLRTM")
val portUSHOU = PredictionLocation(unlocode = "USHOU")
val input = PredictionInput(
imo = "9328053",
chain = true,
requests = listOf(
VoyagePrediction(from = shipLocation, to = portNLRTM),
VisitPrediction(location = portNLRTM),
VoyagePrediction(from = portNLRTM, to = portUSHOU)
)
)
val output = futureShipClient.predict(input)

Why NOT to use the `FutureShipClient` directly, and instead use the `ShipPredictionClient`. Imagine how we'd get the ETA NLRTM, ETD NLRTM and ETA USHOU, an example:

val voyageNLRTM = output.responses[0] as PredictedVoyage
val visitNLRTM = output.responses[1] as PredictedVisit
val voyageUSHOU = output.responses[2] as PredictedVoyage
if (!voyageNLRTM.error) println("ETA NLRTM: ${voyageNLRTM.eta}")
if (!visitNLRTM.error) println("ETD NLRTM: ${visitNLRTM.etd}")
if (!voyageUSHOU.error) println("ETA USHOU: ${voyageUSHOU.eta}")

It's quite ugly to have to cast all of these intermediate segments manually, and risk making mistakes if we ever change the requests later on (and forget this code exists, as it might exist off-screen or in another file entirely).

You now know how the `FutureShipClient` works and why you should instead use the `ShipPredictionClient`!

### ShipPredictionClient

This client uses the `FutureShipClient` under the hood, but it gives you some nice extra features:

* (optional) callbacks per segment (or group)
* grouping segments
* caching (opt-in)
* `onFailure` hook that catches all errors (be aware that by default `onFailure=null`, so all errors are swallowed!, please implement error handling)

To start using the `ShipPredictionClient`, transform your code:

// before
val output = futureShipClient.predict(input)
// after
val output = ShipPredictionClient.predict(futureShipClient, input)
// be sure to also add error handling now, using `onFailure`
val output = ShipPredictionClient.predict(
futureShipClient = futureShipClient,
input = input,
onFailure = { input, exception ->
log.error(exception) { "Something went wrong with: $input" }
}
)

**Callbacks**  
Let's take the previous example and start by implementing callbacks:

* wrap all predictions with their equivalent `Wrapper` object, `VoyagePrediction` gets wrapped by a `VoyagePredictionWrapper` for example.
* implement the callback `onResponse`, also add the print statements from before inside the callback

val shipLocation = PredictionLocation(shipLocation = true)
val portNLRTM = PredictionLocation(unlocode = "NLRTM")
val portUSHOU = PredictionLocation(unlocode = "USHOU")
val input = PredictionInput(
imo = "9328053",
chain = true,
requests = listOf(
VoyagePredictionWrapper(
request = VoyagePrediction(from = shipLocation, to = portNLRTM),
onResponse = { output, voyage ->
if (!voyage.error) println("ETA NLRTM: ${voyage.eta}")
}
),
VisitPredictionWrapper(
request = VisitPrediction(location = portNLRTM),
onResponse = { output, visit ->
if (!visit.error) println("ETD NLRTM: ${visit.etd}")
}
),
VoyagePredictionWrapper(
request = VoyagePrediction(from = portNLRTM, to = portUSHOU),
onResponse = { output, voyage ->
if (!voyage.error) println("ETA USHOU: ${voyage.eta}")
}
)
)
)
// predict still returns the PredictionOutput, but we don't need `output` as a variable anymore
// handling of the responses now gets handled inside our callbacks
ShipPredictionClient.predict(futureShipClient, input /\*, onFailure \*/)

The input object and output handling are now coupled quite nicely, and we can even go one step further and start moving the requests into a separate method.

val shipLocation = PredictionLocation(shipLocation = true)
val portNLRTM = PredictionLocation(unlocode = "NLRTM")
val portUSHOU = PredictionLocation(unlocode = "USHOU")
val input = PredictionInput(
imo = "9328053",
chain = true,
requests = requestVia(from = shipLocation, via = portNLRTM, to = portUSHOU)
)
ShipPredictionClient.predict(futureShipClient, input /\*, onFailure \*/)
...
fun requestVia(from: PredictionLocation, via: PredictionLocation, to: PredictionLocation) = listOf(
VoyagePredictionWrapper(
request = VoyagePrediction(from = shipLocation, to = portNLRTM),
onResponse = { output, voyage ->
if (!voyage.error) println("ETA ${voyage.to}: ${voyage.eta}")
}
),
VisitPredictionWrapper(
request = VisitPrediction(location = portNLRTM),
onResponse = { output, visit ->
if (!visit.error) println("ETD ${visit.location}: ${visit.etd}")
}
),
VoyagePredictionWrapper(
request = VoyagePrediction(from = portNLRTM, to = portUSHOU),
onResponse = { output, voyage ->
if (!voyage.error) println("ETA ${voyage.to}: ${voyage.eta}")
}
)
)

We could now also easily swap our requests with different methods.

**Grouping segments**  
Let's say that in our data model we'd like to group the voyage to NLRTM and visit in NLRTM. The `ShipPredictionClient` supports this (including callbacks) with the `GroupPredictionWrapper`:

listOf(
GroupPredictionWrapper(
requests = listOf(
VoyagePrediction(from = from, to = via),
VisitPrediction(location = via)
),
onResponse = { output, responses ->
if (responses.none { it.error }) {
val voyage = responses[0] as PredictedVoyage
val visit = responses[1] as PredictedVisit
println("ETA ${voyage.to}: ${voyage.eta}")
println("ETD ${visit.location}: ${visit.etd}")
}
}
),
VoyagePredictionWrapper(
request = VoyagePrediction(from = via, to = to),
onResponse = { output, voyage ->
if (!voyage.error) println("ETA ${voyage.to}: ${voyage.eta}")
}
)
)

**Caching**  
Let's create an easier example to introduce caching:

data class PortPrediction(val unlocode: String) {
var eta: Long? = null
}
val port = PortPrediction("NLRTM")
...
listOf(
VoyagePredictionWrapper(
request = VoyagePrediction(
from = PredictionLocation(shipLocation = true),
to = PredictionLocation(unlocode = port.unlocode)
),
onResponse = { output, voyage ->
if (!voyage.error) port.eta = voyage.eta
}
)
)
...
ship.heading = port

In this example we make a request from the current ship location to a port, we add the predicted ETA to an object and then set the heading of the ship to that port (which includes the predicted ETA).

If we don't make another request with the same segments for this ship, then we don't need to bother with caching, but if we do then we can use the built-in caching mechanism.

The `ShipPredictionClient` doesn't hold a cache itself, it only acts upon being given a cache and a specific `key` with which you identify the request you are making.

val cache = mutableMapOf<String, CachedResult>()
...
val key = "9328053=>NLRTM"
ShipPredictionClient.predict(futureShipClient, input, key, cache, onFailure)
ShipPredictionClient.predict(futureShipClient, input, key, cache, onFailure)

We run the `predict` twice, as it's added to our `cache` after the first run the second call will utilize this cache.

You are free in how you want to implement caching:

* caching per "prediction interval", for example: every hour you make N predictions, you use an empty cache after every interval
* caching with TTL (useful if you don't do "prediction intervals"), for example: you make predictions on behalf of a user, you initialize an empty cache on application startup and the TTL takes care of removing cached items

**Really important: make sure you generate a** `key` **that will always be the same for similar input!**

You could for example create a key for: voyage ship => NLRTM, `key=9328053=>NLRTM`

If you'd also generate the `key=9328053=>NLRTM` for a NLRTM visit, then it will break! (obviously)

As you can specify callbacks, these callbacks must always be "fresh", that-is the results of the requests will be cached for you, not the callbacks! This ensures you can pass different objects/callbacks, but feeding cached data into your callbacks.

Small example to see that in action:

data class PortPrediction(val unlocode: String) {
var eta: Long? = null
}
fun request(port: PortPrediction) = listOf(
VoyagePredictionWrapper(
request = VoyagePrediction(
from = PredictionLocation(shipLocation = true),
to = PredictionLocation(unlocode = port.unlocode)
),
onResponse = { output, voyage ->
if (!voyage.error) port.eta = voyage.eta
}
)
)
val port1 = PortPrediction("NLRTM")
val port2 = PortPrediction("NLRTM")
val input1 = PredictionInput(imo = "9328053", chain = true, requests = request(port1))
val input2 = PredictionInput(imo = "9328053", chain = true, requests = request(port2))
val cache = mutableMapOf<String, CachedResult>()
val key = "9328053=>NLRTM"
// port1={ unlocode=NLRTM, eta=null }, port2={ unlocode=NLRTM, eta=null }
ShipPredictionClient.predict(futureShipClient, input1, key, cache, onFailure)
// port1={ unlocode=NLRTM, eta=... }, port2={ unlocode=NLRTM, eta=null }
// at this point the `cache` will contain one item under the `key`
// the request we will do now uses the same cache key, but has other callbacks (namely the callbacks for `port2`, instead of `port1`)
// the cached data gets fed into the new callbacks this way
ShipPredictionClient.predict(futureShipClient, input2, key, cache, onFailure)
// port1={ unlocode=NLRTM, eta=... }, port2={ unlocode=NLRTM, eta=... }
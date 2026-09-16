---
id: confluence:746160200
source: confluence
type: page
space: TC
title: ETA predictor architecture
author: Michel Wilson
date: '2025-10-08'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/746160200
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/746160200
---
# ETA predictor architecture

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/746160200  

## Content

# System overview

The ETA predictor is a scalable system designed to give travel time predictions as well as arrival time predictions for sea vessels, based on departure location and destination location. The voyage between departure and arrival location can be composed of multiple different segments of different types, such as travel, port visit, anchoring.

Prediction requests can be done single-shot and dynamically, where the arrival time is updated whenever the predictor deems it to be outdated. Dynamic prediction requests are event-driven and scope-based. Every time the prediction is updated, it is published to a KV store. This is done for multiple scopes, where every scope contains at most one prediction request for a vessel. The predictor will have one built-in scope which contains true destination-based prediction requests: for every vessel, a prediction request will be generated to the last-known true destination. Additionally, external applications can use the REST API to add, update or delete prediction requests in custom scopes. This can be used to create more precise predictions in case more information is known about the vessel schedule.

Scalability is ensured by decoupling the API and request scheduling and generating from the actual prediction making, which is expected to be the greatest bottleneck. NATS request/reply is used as a decoupling mechanism, whereby a queue group is used to be able to seamlessly scale the number of processing nodes in the system.

# Architecture/components

The system can be divided into the following components, which will be briefly described below:

* Prediction modules
* Prediction coordinator
* REST API
* Location request updater
* Request generator/updater
* Request repository
* Scheduler
* KV store

The REST API, request generator/updater and data repository are one component, the API component, and the coordinator, scheduler and prediction modules are a second component, the processing component. They communicate using a NATS request/reply module, where there can be more than one processing component. The processing components use queue group support in the broker to distribute the load in a round-robin way.

## Prediction modules

A prediction can contain different segment types, and for each segment type, the system contains a different module to make the actual prediction. Every prediction module takes as input the ship details, and optionally a start timestamp and the previous prediction output. If the start timestamp is omitted, the module will just output the duration of the segment, and the prediction will be stateless. If the start timestamp is given, the predictor might also consider the current level of congestion in a port or on a route to influence the prediction. The previous prediction is optional, and is used to “short circuit” the predictor in case no significant changes have occurred. A good example is a predicted travel: if the vessel stays on the predicted path, no new route needs to be predicted.

| Predictor | Input | Output |
| --- | --- | --- |
| Travel | Ship details, start/end location, speed | Leg duration, route, (optional) arrival time |
| Port Visit | Ship details, port codes | Port stay duration, (optional) departure time |
| Anchor | Ship details, anchorage code | Anchoring duration, (optional) departure time |

* The **Travel Predictor** is about the movement between locations (voyages).
* The **Port Visit Predictor** is about the time spent at a port.
* The **Anchor Predictor** is about time spent anchored (not at berth).

## Prediction coordinator

Given a complete prediction request, this component calls a prediction module for each segment of the prediction request. To support predictions using a departure time, the modules are called sequentially, as the arrival time of one segment is the departure time of the next segment. After all segments have been calculated, the results are concatenated together and returned.

## REST API

Controllers to make single-shot predictions and to manage specific dynamic predictions.

## Location request updater

A small component that receives ship location updates, and uses this to update existing prediction requests. If the ship has moved significantly (above a certain threshold), any dynamic prediction requests for this ship that start with a travel segment are updated: the start location of the travel segment is replaced with the current location of the ship, and the request is submitted to the repository.

## Request generator/updater for true destination scope

A small component that receives true destination updates and creates/updates dynamic prediction requests consisting solely of a travel segment, from the current location of the vessel to the true destination.

## Request repository

The request repository stores dynamic prediction requests per scope, backed by a Mongo database, and it also manages submitting the requests via NATS request/reply to the processing nodes. This component manages the processing rate by ensuring that there is a limited number of prediction requests “in flight” at any given time.

## Scheduler

The scheduler receives requests over the NATS request/reply queue and does the heavy lifting, in such a way that the concurrency is limited (i.e., a set number of threads and a work queue are employed). Events or requests can add work to the scheduler, and based on the priority (synchronous requests have a higher priority) they are executed on the available threads. The scheduler threads call the coordinator to do the actual prediction work.

## KV store

The dynamic prediction results are stored in a NATS KV store, and can be accessed using the prediction scope and the MMSI of the vessel. NATS is used here to be able to subscribe to a specific prediction or to an entire scope. Whenever the value for a key is added or updated, a subscriber is notified automatically.

# Prediction behavior and Segment Lifecycle

The previous sections describe the system architecture and the components responsible for handling prediction requests, coordination, and data flow. To complement this, this following section details the **behavioral design** of the predictor — how prediction segments are created, updated, and transitioned based on vessel movement, destination changes, and port boundary events. This section explains the lifecycle of travel and port visit segments and how they evolve as a vessel moves through different operational states, ensuring the system’s predictions remain accurate and consistent over time.

### Overview

The ETA predictor operates on the basis of *segments* that represent distinct parts of a vessel’s voyage. Each prediction request consists of one or more segments, such as a **travel** segment (movement between two locations) or a **port visit** segment (stay within a port). This section describes how the predictor dynamically manages these segments based on vessel position, destination updates, and port boundary crossings.

The goal of this behavior model is to ensure consistent, event-driven updates to predictions, reflecting the vessel’s actual operational state — at sea, entering port, within port, or leaving port — while maintaining scalability and real-time responsiveness.

### Key Concepts and Definitions

* **Pilot Boarding Place (PBP)**  
  A defined area where the ship’s pilot boards the vessel prior to entering the port. Ports may have multiple PBPs, each serving different approach routes.
* **True Destination**  
  The UNLOCODE corresponding to the *AIS destination* field value transmitted by the vessel. It determines the port for which the ETA prediction is made.
* **Outer Boundary**  
  The area enclosing the port and its adjacent operational zones, including PBPs and anchor areas. Crossing this boundary signifies arrival at the port for vessels without defined PBPs.
* **Inner Boundary**  
  The area encompassing the actual port infrastructure, such as basins and berths. Crossing this boundary signifies the vessel has departed the port area.
* **Port Center**  
  A reference point roughly in the middle of the port. It is used as a routing proxy when no PBP or specific berth is available, though not all vessels may be able to physically reach it due to size constraints.

### Vessel States and Segment Composition

The predictor recognizes four high-level vessel states, each corresponding to specific segment configurations:

| Vessel State | Triggering Condition |
| --- | --- |
| **At Sea** | Vessel outside outer boundary and not within PBP |
| **Entering Port** | Crossing into PBP or inner boundary |
| **In Port** | Vessel within inner boundary and stationary or slow-moving |
| **Leaving Port** | Vessel crosses outer boundary and sets new true destination. If the port has no outer boundary, the inner boundary is used. |

### Prediction Behavior

#### Ship at Sea

When a vessel is underway and a prediction request is initiated, the system determines the most appropriate destination point for the route:

* **Ports with multiple PBPs:**

  1. Determine a rough route to the port center based on the true destination.
  2. Identify the PBP nearest to this route.
  3. Use the center of that PBP as the destination for route and ETA calculation.
* **Ports with a single PBP:**  
  Use the center of that PBP as the route endpoint.
* **Ports without PBPs:**

  1. Compute a rough route to the port center.
  2. Determine the intersection between the route and the port’s inner boundary.
  3. Use that intersection point as the destination for route and ETA calculation.

The resulting prediction request consists of two segments:

1. **Travel Segment** – from current vessel location to the selected destination point.
2. **Port Visit Segment** – representing the expected stay at the destination port.

The predictor continuously monitors vessel movement. If the vessel moves significantly (beyond a configurable *distance threshold*, e.g., several kilometers) or deviates from the planned route, the start location of the travel segment is updated and a new route is calculated. Predictions are recalculated and published to the KV store accordingly.

#### Entering Port and Staying in Port

When the vessel arrives at or within port limits, the travel segment is completed, and prediction updates focus on the port visit:

* **Ports with PBPs:**

  + When entering a PBP area, the vessel is considered to have *arrived*. The travel segment is removed.
  + The **port visit segment** begins updating the expected **ETD** (estimated time of departure).
  + Once the vessel leaves the PBP area (indicating the start of movement toward berth), the system continues updating ETD until the port stay prediction stabilizes.
* **Ports without PBPs:**

  + When the vessel crosses into the inner boundary, it is marked as *arrived*.
  + The travel segment is removed, and ETD predictions for the port visit segment begin.
  + Once the vessel exits the port again (crossing the outer boundary), the port visit segment ends.

In this state, the prediction request typically contains only a **port visit segment**.  
If the vessel updates its *true destination* while in port, a new **travel segment** and **port visit segment** are appended to the prediction request, based on the route from the inner boundary exit point to the next port.

**ETD prediction behavior:**

* If the vessel stays longer than expected:

  + **No updated true destination:** ETD is set to the current time (cannot be accurately estimated).
  + **Updated true destination:** The system identifies the point on the outer boundary where the ship will exit, computes travel time to that point, and sets ETD as *current time + travel time to boundary* (ETD cannot be earlier than this).

When the ship starts moving within the port, ETD is continuously updated based on current position and estimated time to reach the outer boundary.

#### Leaving Port

When the vessel crosses the **outer boundary**, it is considered to have *departed* the port.  
At this point:

* The **port visit segment** is removed.
* The system transitions back to the *At Sea* state, creating a new **travel + port visit** segment pair toward the vessel’s current *true destination*.

This ensures that predictions seamlessly continue for the vessel’s onward voyage without manual reinitialization.

### Segment Updates and Recalculation Triggers

To maintain accuracy while avoiding excessive computation, updates are triggered by configurable parameters:

| Trigger | Description | Default Behavior |
| --- | --- | --- |
| **Movement threshold** | Vessel moves beyond a configured distance from last start point | Recalculate route and ETA |
| **Route deviation** | Vessel position exceeds allowed distance from predicted path | Discard route and request new one from RouteScout |
| **True destination update** | New UNLOCODE differs from previous | Recreate travel segment and recompute prediction |
| **Boundary crossing** | Vessel crosses outer or inner port boundary | Transition between travel and port visit segments |

All recalculated results are published to the NATS KV store, maintaining consistent, real-time visibility for subscribers.

### Configuration and Future Extensions

The following parameters and behaviors are configurable:

* Distance threshold for significant movement or deviation (in kilometers).
* Update interval for ETD recalculations during port stay.
* Boundary definitions and port metadata sources (via POMA).

Potential future extensions include:

* Incorporating berth-level details once the actual berth position becomes known.
* Integrating congestion and traffic models for more dynamic port stay estimation.
* Supporting additional segment types (e.g., *anchorage*, *pilotage*, or *canal transit*) using the same segment-based design pattern.

Together, these behavioral rules and lifecycle transitions ensure that the ETA predictor maintains a coherent and continuously updated representation of each vessel’s voyage. By aligning travel and port visit segments with actual vessel states and movement patterns, the system provides accurate, event-driven predictions without manual intervention. This behavioral layer effectively bridges the architectural components and the operational logic of the predictor, enabling scalable, automated updates for all vessels worldwide.

# Use case examples

## One-shot prediction via REST

* A prediction is submitted via the REST endpoint to the API module. This can either be a prediction in “simple” form (i.e., from one lat/lon point to another lat/lon point), or a complete prediction request in the form of a list of prediction segments. In the first case the controller converts the simple prediction into a single travel segment.
* The prediction is submitted via NATS request/reply to the processing module, where it is scheduled for immediate execution, on the first thread that becomes available. This call blocks, waiting for a response. To ensure that the prediction is picked up immediately, a separate request/reply topic is used.
* The scheduler thread calls the coordinator, which retrieves the necessary external information, such as ship details etc, needed for the prediction, and which calls into the specific prediction modules needed for this prediction.
* Using NATS request/reply the response is handed all the way back to the caller via the controller.

## True destination change

* A true destination event is received by the true destination request generator/updater in the API module. The generator retrieves the current dynamic prediction request from the repository, and notices that the travel segment has a different destination. The segment is updated, and the request is saved to the repository. Then, the request is submitted via NATS request/reply to the processing module.
* The scheduler picks up the prediction when a thread becomes available, and hands it to the coordinator for updating and processing.
* The coordinator updates external information if this is needed, based on age. Then, the individual prediction modules are called. The travel predictor discards the path from the previous prediction, since the destination of the travel segment has changed. This leads to a call to RouteScout to update the path. Then, the prediction continues as normal.
* The reply is posted to the API module via NATS, and it stores the result in the KV store.

## Location change

* An AIS diff event is received by the location request updater in the API module with a new location for a ship. The updater retrieves prediction requests for this ship for all scopes from the repository. If the validity of a prediction has expired, the start location of the first leg is updated, and the new prediction request is saved to the repository and submitted via NATS to the processing module.
* In the processing module, the coordinator updates external information if this is needed, based on age, and then calls the individual prediction modules. The travel module compares the start location to the path from the previous prediction. If it is close enough, the path is truncated to start at the point closest to the current location, and all times are updated. If the ship has deviated from the path, it is discarded, and RouteScout is called to update the path. Then the prediction continues as normal.
* The result is sent as a reply to the API module, which stores the result in the KV store.

## Custom dynamic request scope

If an application wishes to have more complex dynamic prediction requests than the default true destination request generator provides, it is possible to create a custom scope in which the application can manage its own prediction requests.

As an example, imagine an external application that has knowledge of the schedule of a container vessel that has received an update to this schedule.

* A schedule update is received for a vessel. Via the REST API, a prediction request is submitted in the scope of this particular application. The request is based on the schedule of the vessel and contains multiple travel and port visit segments
* The API module stores the updated prediction request in the repository, and sends a prediction request via NATS to the processing module.
* When a thread becomes available, the prediction request is processed, and the result is sent as a reply over NATS. The API module then stores the result in the KV store, on which the external application is subscribed
* Whenever the vessel position is updated significantly, the prediction request is updated and sent to the processing module again, like above.
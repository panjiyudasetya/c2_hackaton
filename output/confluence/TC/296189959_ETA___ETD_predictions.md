---
id: confluence:296189959
source: confluence
type: page
space: TC
title: ETA / ETD predictions
author: Former user (Deleted)
date: '2024-03-08'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/296189959
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/296189959
---
# ETA / ETD predictions

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/296189959  

## Content

ETA = Estimated Time of Arrival at the EOS of a port

ETD = Estimated time of Departure from a terminal.

### Functional Requirements + scoping

1. When talking about ETA / ETD predictions we focus on port predictions only, where the ETA reflects the moment that the vessel will arrive in the End Of Seapassage (EOS).
2. For each ship I should be able to get an ETA timestamp to any port based on the current situation. This would include a `from` location, `to` location and a `displayable route` as an output
3. The prediction should also be possible for a ship characteristics (like a capesize tanker)
4. The ETD predictions is basically the timestamp when a vessel is planned to leave a certain terminal, taking into account arrival time and shipType, and where possible (in future?) also the cargo type and amount.
5. The design should be extensible, allowing next stops to be included but also having (still unforeseen) predictors like ‘expected waiting time at anchorage’.
6. It should be performant enough to produce for all sea-vessels world-wide every 15 minutes the prediction to 1 next stop, and for 10% of them a prediction to the stop after
7. The prediction mechanism should support a request response interface with user friendly endpoints, which would give an ETA / ETD prediction to any next location at the world, within a response time of 2 seconds

## Sync API

Predictions can be made in a synchronous fashion, using a request/reply pattern. This can be done over a transport like HTTP or NATS. The end-user application sends a request directly to an instance of the predictor, responding with the ETA/ETD predictions.

When multiple applications make requests, there are some possibilities for caching. The service will at least know where all ships are, to be able to resolve from an IMO/MMSI to where that ship is at that point in time. Possibly it could also cache prediction results, but that will need to be discussed further how that would work, and if it would even be needed (if it’s given that the prediction itself is performant enough to not require caching).

## Async API

Predictions can also be made in an asynchronous fashion. An end-user application, like SmartFleet, only knows which ships the predictions need to be made on, as well as what to predict. However, they want to:

* stay updated with ETA/ETD predictions
* not need to manually request predictions in a loop on a set interval

The end-user application “subscribes” on a specific ship and adds what predictions need to be made. A “prediction subscription manager” component combines all subscriptions made by various end-user applications, and it is responsible for requesting predictions on their behalf. The responses of these predictions can then be distributed directly to the end-user application, or can be relayed via the subscription manager (to be decided).

The “prediction subscription manager” can use various triggers to make prediction requests:

* listen to real-time AIS
* trigger every X minutes, or on an interval looking at the AIS updates
* triggering when the ship moves an X distance, either in general or based on moving along or away from the route

To fully close the loop, the end-user applications should also be able to “unsubscribe” from their prediction requests. The “prediction subscription manager” should also have some mechanism to “keep-alive” the subscription, occasionally checking if the end-user application is still willing to receive prediction updates and it didn’t ‘forget’ to unsubscribe. This allows an end-user application to “unsubscribe” from predictions for efficiency purposes, but it will otherwise be caught by the “keep-alive” mechanism.
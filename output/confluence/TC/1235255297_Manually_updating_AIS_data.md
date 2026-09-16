---
id: confluence:1235255297
source: confluence
type: page
space: TC
title: Manually updating AIS data
author: Michel Wilson
date: '2026-06-03'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1235255297
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1235255297
---
# Manually updating AIS data

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1235255297  

## Content

In rare cases, it is needed to manually update/fix AIS data. An example would be to fix a wrong destination for a ship. This can be done by `POST`ing AIS message data to the relevant endpoints of the ais-stream application, together with a M2M authentication token.

## Getting a token

Get a M2M token by doing a `POST` to

* `https://keycloak.teqplay.nl/auth/realms/prod/protocol/openid-connect/token` for production,
* `https://keycloakdev.teqplay.nl/auth/realms/dev/protocol/openid-connect/token` for development,

with an `application/x-www-form-urlencoded` body containing the following values:

* `grant_type` set to `client_credentials`,
* `client_id` set to the name of your Keycloak client application, and
* `client_secret` to the secret for that application.

The Keycloak application must have access to the `ais-stream` scope, otherwise the token will be rejected.

## Perform an update

Four different types of updates can be done via the controller: position messages, long-range position messages, static messages and station messages. In practice, only position and static messages will be used.

### Position update

Do a `POST` to `/v1/ais/update/position` with an `application/json` body like the example below:

jsonwide760{
"mmsi": 244820000,
"location": {
"lat": 12.34,
"lon": 56.78
},
"heading": 45,
"speedOverGround": 7.2,
"courseOverGround": 42.8
}

The `mmsi` field is mandatory, all the other fields are optional.

### Static update

Do a `POST` to `/v1/ais/update/static` with an `application/json` body like the example below:

jsonwide760{
"mmsi": 244820000,
"imo": 9876543,
"name": "MV HORIZON",
"callSign": "PBHZ",
"shipType": "CARGO",
"draught": 8.5,
"eta": "2026-06-10T14:00:00Z",
"destination": "ROTTERDAM",
"transponderPosition": {
"distanceToBow": 120,
"distanceToStern": 30,
"distanceToPort": 15,
"distanceToStarboard": 15
},
"positionSensorType": "GPS"
}

The `mmsi` field is again mandatory, all the other fields are optional.
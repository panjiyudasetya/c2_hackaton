---
id: confluence:1283588097
source: confluence
type: page
space: TC
title: Overview of the ofiniti-map-api Middleware Backend and Client Management Options
author: David Hansson
date: '2026-07-13'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1283588097
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1283588097
---
# Overview of the ofiniti-map-api Middleware Backend and Client Management Options

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1283588097  

## Content

# ofiniti-map-api — Overview Plan

> Middleware backend between the `ofiniti-map` (fleet-map) web component and the Teqplay API (main-api). This document presents our considerations and intended approach, for validation by the core component team.

## 1. Context

`ofiniti-map` is an embeddable MapLibre web component (`<fleet-map>`) that customers drop into their own web pages to show vessels by IMO. Today its vessel data is mocked. To show real data it needs the main-api (`/v1/ship/current/imo`), which is authenticated with Keycloak client credentials — credentials that must never ship to the browser. We also need to control **which customers** may embed the map and fetch vessel data.  
  
[https://ofinitimap.teqplay.dev](https://ofinitimap.teqplay.dev/)

## 2. Options considered

We considered two ways to support this use case:

1. **A new backend instance specific for ofiniti-map** (`ofiniti-map-api`): a small middleware service with its own database of registered clients that are allowed to call the vessel list from ofiniti-map.
2. **Extending main-api (**`api/*`**)**: add a new endpoint to the existing gateway, plus a new database for registered ofiniti-map clients. Note that main-api is currently a Spring Cloud Gateway with no database of its own — this option would introduce state into a service that is today a stateless proxy.

## 3. Question to the core component team

We would like your perspective before we commit:

* Is a **dedicated backend for ofiniti-map** a good approach, keeping this product-specific client management out of main-api?
* Or do you think **main-api should be extended** to manage these ofiniti-map clients and expose this endpoint itself?

Our preference is option 1 (dedicated backend), for these reasons: main-api stays a stateless gateway; the ofiniti-map client model (browser tokens + referer allowlists) is product-specific and shouldn't leak into the shared API surface; and the service can evolve/deploy independently. The rest of this document describes that approach.

## 4. Our approach

wide760┌─────────────┐ GET /vessels?imos=... ┌─────────────────┐ Bearer (ofiniti-map-server) ┌─────────────┐
│ ofiniti-map │ ─────────────────────────► │ ofiniti-map-api │ ─────────────────────────────► │ main-api │
│ (browser) │ token + referer check │ (this service) │ /v1/ship/current/imo │ (gateway) │
└─────────────┘ └─────────────────┘ └─────────────┘

### 4.1 New backend initiated from skeleton-backend

We will create a new backend, initiated from **skeleton-backend** (our standard boilerplate). That gives us out of the box: Kotlin + Spring Boot, MongoDB (`datasource2`), Spring Security, actuator health + Prometheus metrics, Docker → ECR, Helm values, and the standard GitHub Actions CI.

### 4.2 Own database of registered ofiniti-map clients

We will create our own database (MongoDB, `mapClients` collection) storing the list of clients registered as ofiniti-map clients. Each client has:

* an **API token** (stored hashed) that the customer embeds alongside the map component, and
* one or more **allowed referer domains**.

A request is served only when **both** match a registered, active client — same model as Google Maps browser keys: the token is visible in the customer's page by design, and the referer restriction limits where it can be used from. Clients are provisioned manually for now (no self-service registration).

### 4.3 New API endpoint calling main-api for authenticated users

We will expose one endpoint for authenticated (registered) users:

wide760GET /vessels?imos={imo,imo,...}
Authorization: Bearer <client-token>

For each request, ofiniti-map-api calls main-api `/v1/ship/current/imo` for the requested vessels and returns only the fields the map needs — ship name, location, heading, vessel status, and IMO — dropping the rest of the upstream payload:

wide760[
{
"imo": 9321481,
"name": "MV Nordic Star",
"location": { "lat": 51.95, "lon": 4.14 },
"heading": 87,
"status": "UNDER\_WAY\_USING\_ENGINE"
}
]

Implementation note to validate: main-api exposes both `GET /v1/ship/current/imo/{imo}` (per vessel) and batch `POST /v1/ship/current/imo` (list of IMOs in one call). We would prefer the batch endpoint and fall back to per-IMO GETs only if there's a reason not to. Upstream returns an array per IMO (multiple transponders can share an IMO); we take the most recent message per IMO.

### 4.4 Own Keycloak account: `ofiniti-map-server`

To be authorized on main-api, ofiniti-map-api will have its own account registered in Keycloak as the `ofiniti-map-server` client (confidential client, client-credentials grant). The service logs in via `POST /v1/auth/token`, caches the access token, and refreshes it before expiry.

This way we can call `/v1/ship/current/imo` **without passing our users through to main-api**: end users/customers never receive Teqplay credentials, and main-api only ever sees one known service account.

### 4.5 Default access policy

With this approach, by default we **only allow ofiniti-map component users to the defined endpoint**: registered clients can call `GET /vessels` and nothing else. No other main-api capability is exposed through this service, and unregistered or referer-mismatched callers are rejected (`401`/`403`).

## 5. Open questions for the core component team

1. Dedicated backend vs extending main-api (§3) — which do you prefer?
2. Batch `POST /v1/ship/current/imo` vs per-IMO `GET` — any objection to the batch endpoint?
3. Is a dedicated Keycloak confidential client (`ofiniti-map-server`, audience `api`) the right way to provision the upstream credentials?
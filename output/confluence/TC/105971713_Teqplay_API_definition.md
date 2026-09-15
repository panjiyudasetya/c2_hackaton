---
id: confluence:105971713
source: confluence
type: page
space: TC
title: Teqplay API definition
author: Richard van Klaveren
date: '2025-06-30'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/105971713
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/105971713
---
# Teqplay API definition

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/105971713  

## Content

The Teqplay API will contain multiple components. An internal API will be used by our applications and an external API will be accessible to customers that want to use the Teqplay API. In the diagram below a quick overview can be found of how this will end up looking.

Internal and external API overview

# API rules

## General

* The internal API is accessible from the outside but is only allowed to be used for internal applications.
* The internal API should not be used by the frontend of itself. For example, the portreporter site should always call the portreporter backend.
* The external API will only be used to forward endpoints to the internal API. The HTTP method used can differ from the standard used in the internal API if requested by a 3rd party.
* The APIs will be found on the following base URLs:

  + Internal endpoints are accessible via `internal.teqplay.nl/...`
  + External endpoints are accessible via `api.teqplay.nl/...`

## Request endpoints

### Grouping

The internal and external API endpoints will be grouped based on multiple levels.

* The API starts with the version of the API, where v0 is the backward compatible API with platform, v1 is the first self-defined API version.
* The first level will be grouped based on entityType. For example `/ship` or `/infra`.
* A second level is used to group different elements closely related like `/infra/berth` or `/ship/current` (for actual ship info) or `/ship/static` (for registry information)
* Optionally a third level will be used to specify the entity's identifier.

  + For ships, this is an MMSI.
  + For ports, this is the UNLOCODE.
  + By default, this is the database ID of said entity.
* The next level will be grouped based on the functionality if the endpoints go a layer deeper. For example `/polygon` when having `ship` as our first level entity, like `/ship/history/polygon` will allow to request ship updates in a certain polygon.
* In general filtering will take place based on request parameters. Example: `/infra/terminal?port=NLRTM`, however in some cases we also allow filtering based on extended path like `/infra/terminal/port/{unlocode}.` In very specific filtering cases a ‘query’ endpoint could be added at level 2, like `/ship/query`.

This will result in endpoints that look as follows:

* Find all ships `/ship`
* Find a ship by mmsi `/ship/current/{MMSI}`
* Find the history of a ship `/ship/history/mmsi/{MMSI}`
* Find all ships in a port `/ship?port={UNLOCODE}`
* Find a ship filtered by IMO `/ship?imo=1234567`

### URL versioning

Endpoints will make use of versioning. This will look as follows:

* For the first version of an endpoint `internal.teqplay.nl/v1/...`
* When a breaking change is made `internal.teqplay.nl/v2/...`

### The functionality of the endpoint is described by the HTTP method

The following standard should be followed when possible. This doesn't apply to the external API if the customer needs/wants a specific HTTP method.

| **Method** | **Description** |
| --- | --- |
| GET | Retrieve a resource |
| POST | Create a new resource |
| PUT | Update an existing resource where the whole resource is provided |
| PATCH | Update an existing resource where the resource is only partially updated |
| DELETE | Delete an existing resource |

### Parameters

All request params will be following *camelCase*, for example, `berthId`.

#### Pagination

When applying pagination, a `limit` and `offset` always need to be provided in a request.

* The `limit` parameter specifies the maximum of items that can be retrieved. A maximum of the limit needs to be handled by the target application, and the target application uses the default limit when not provided.
* The `offset` parameter specifies the number of items that need to be skipped. A default value of 0 will be used when not provided, skipping no items.

This will look as followed:

* Limit of 50, default offset `?limit=50`
* Limit of 50, skipping the first 10 items `?limit=50&offset=10`

#### Sorting

When sorting is available on the endpoint, a `sort` field needs to be provided.

* This field must always contain one field name but can also have more fields if desired. A comma (`,`) is used before every new item when sorting on multiple fields.
* The sorting order for each field can optionally be added next to each field and is split with a colon (`:`). The values used for sorting are `asc` for ascending and `desc` for descending.
* The default sorting order is Ascending when no order is specified.

This will look as followed:

* Single field sorting `?sort=berthId`
* Single field sorting with the sorting order provided `?sort=berthId:desc`
* Multi-field sorting `?sort=berthId,portId`
* Multi-field sorting with the sorting order provided `?sort=berthId:asc,portId:desc`

## Authentication & Authorization

Authentication will be done on the side of the internal API. Other backends can access the internal and external API using a KeyCloak token.

* Requesting a KeyCloak token via an endpoint will be accessible in the external and internal API. However, the actual request to the endpoint is made on the side of the internal API.

  + This request requires a `clientId` and `clientSecret` in a JSON body.
  + This request will be a `POST`.
* The KeyCloak token will be validated on the side of the internal API and must contain the audience of `api` to be accepted.
* The KeyCloak token needs to contain the audience of the target application, and this audience will be checked on the side of the target application.
* The KeyCloak token is added via the `Authorization` header with the `Bearer` prefix. Resulting in `Authorization: Bearer <token>`.
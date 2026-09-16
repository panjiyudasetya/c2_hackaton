---
id: confluence:1217527826
source: confluence
type: page
space: TC
title: Poma Ports Insight Definition
author: Michel Wilson
date: '2026-06-22'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217527826
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217527826
---
# Poma Ports Insight Definition

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217527826  

## Content

## POMA port mapping levels

There are four mapping levels on a port:

1. `NOT MAPPED`
2. `PORT MAPPED`
3. `BASIC MAPPED`
4. `FULLY MAPPED`

---

## `NOT MAPPED`

Always considered complete.

No validation requirements are enforced for mapping completeness.

---

## `PORT MAPPED`

Only the port itself needs to be valid.

Required valid fields:

* port `area`
* port `name`
* port `displayName`
* port `unlocode`
* port `countryCode`

Optional but checked when present:

* `outerArea` must not be invalid
* `eosArea` must not be invalid

Infrastructure is ignored for this level:

* terminals ignored
* berths ignored
* anchorages ignored
* pilot boarding places ignored

---

## `BASIC_MAPPED`

Everything from `PORT_MAPPED`, plus terminals and berths.

Required:

### Port

Same as `PORT_MAPPED`.

### Terminals

There must be at least one terminal.

Every terminal must have valid:

* `id`
* `name`
* `area`
* `ports` mapping to the parent port
* linked berths

Terminal `cargoType` is **not required** for this level.

### Berths

There must be at least one berth.

Every berth must have valid:

* `id`
* `name`
* `area`
* `ports` mapping to the parent port

Berth `cargoCategoryType` is **not required** for this level.

Ignored:

* anchorages
* pilot boarding places

---

## `FULLY_MAPPED`

Everything from `BASIC_MAPPED`, plus all infrastructure and cargo fields.

Required:

### Port

Same as `PORT_MAPPED`.

### Terminals

There must be at least one terminal.

Every terminal must have valid:

* `id`
* `name`
* `cargoType`
* `area`
* `ports` mapping to the parent port
* linked berths

### Berths

There must be at least one berth.

Every berth must have valid:

* `id`
* `name`
* `functionType`
* `cargoCategoryType`, when `functionType` includes `CARGOOPS`
* `area`
* `ports` mapping to the parent port

### Anchorages

There must be at least one anchorage.

Every anchorage must have valid:

* `id`
* `name`
* `area`
* `ports` mapping to the parent port

### Pilot boarding places

There must be at least one pilot boarding place.

Every pilot boarding place must have valid:

* `id`
* `name`
* `area`
* `ports` mapping to the parent port

### EOS area

For `FULLY_MAPPED`, the `eosArea` is checked against all infrastructure areas:

* terminals
* berths
* anchorages
* pilot boarding places

It must contain all of them if present.
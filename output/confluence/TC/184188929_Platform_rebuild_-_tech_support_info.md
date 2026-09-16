---
id: confluence:184188929
source: confluence
type: page
space: TC
title: Platform rebuild - tech support info
author: Darius Wattimena
date: '2023-05-22'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/184188929
explicit_links: []
---
# Platform rebuild - tech support info

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/184188929  

## Content

# Encounter Monitor

Related topics in Platform configuration:

PILOT = "ENCOUNTER.SHIP"
TUG = "ENCOUNTER.SHIP"
SWOG = "ENCOUNTER.SHIP"
WASTE = "ENCOUNTER.SHIP"
AUTHORITY = "ENCOUNTER.SHIP"
BOATMAN = "ENCOUNTER.SHIP"
BUNKER = "ENCOUNTER.SHIP"
WATER = "ENCOUNTER.SHIP"
TENDER = "ENCOUNTER.SHIP"
CRANE = "ENCOUNTER.SHIP"
FENDER = "ENCOUNTER.SHIP"
SUPPLYBARGE = "ENCOUNTER.SHIP"
PUSHBARGE = "ENCOUNTER.SHIP"
TANKERBARGE = "ENCOUNTER.SHIP"
CARGOBARGE = "ENCOUNTER.SHIP"
BARGE\_WATER = "ENCOUNTER.SHIP"
BARGE\_BUNKER = "ENCOUNTER.SHIP"
LUBES = "ENCOUNTER.SHIP"
TUG\_WAITING\_DEPARTURE = "ENCOUNTER.SHIP"

## Switch encounter events back to Platform Encounter Monitor

On Backend:

1. Remove encounter events from `externalamqp.in.topics` list
2. Enable encounter monitor, set `encounter.enabled` to true

On Backend Pronto:

1. Remove encounter events from `externalamqp.in.topics` list
2. Enable encounter monitor, set `encounter.enabled` to true

On Backend Global:

1. Remove encounter events from `externalamqp.in.topics` list
2. Enable encounter monitor, set `encounter.enabled` to true

On RabbitMQ:

1. Open the `AisEngineTeqplayEvents` exchange and unbind all `ship-ship.#`

   1. TeqplayEvents-VesselVoyage
   2. TeqplayEvents-backend
   3. TeqplayEvents-backendpronto
   4. TeqplayEvents-backendglobal
2. Open the `TeqplayEvents` exchange and add the binding for `ship-ship.#` for the following servers

   1. TeqplayEvents-VesselVoyage
   2. TeqplayEvents-backend
   3. TeqplayEvents-backendpronto
   4. **DO NOT ADD** TeqplayEvents-backendglobal global is the producer of encounter events on the `TeqplayEvents`.
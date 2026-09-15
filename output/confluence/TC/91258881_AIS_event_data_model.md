---
id: confluence:91258881
source: confluence
type: page
space: TC
title: AIS event data model
author: Darius Wattimena
date: '2022-07-18'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/91258881
explicit_links: []
---
# AIS event data model

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/91258881  

## Content

The new AIS event model (ShipInfo) will always be an event from an AIS message, thus removing all the derived fields. The initial idea is to keep the same flexible AIS message model which supports multiple message types.

| **Field** | **New Field Name** | **Send to new queue** | **Send to legacy Platform** | **Changes** | **Note** |
| --- | --- | --- | --- | --- | --- |
| teqplayId | - | - | - | Deleted | Can be deleted as MMSI should be always there |
| **mmsi\*** | **-** | **Always** | **Always** |  | **Will be the leading field and never** `null` |
| imoNumber | imo | If contains | If contains | Rename | Quite tricky with the current `ShipUtils.NO_IMO` mechanism |
| eni | - | If contains | If contains |  |  |
| name | - | When changed | If contains |  |  |
| callSign | - | When changed | If contains |  |  |
| location | - | If contains | If contains | Changed to minimal Location model (Only `latitude` & `longitude`) |  |
| destination | - | When changed | If contains |  |  |
| trueDestination | - | - | - | Deleted | Should be derived outside of the AIS message |
| timeLastUpdate | messageTime | Always | Always | Changed to an Instant, rename |  |
| timeLastStaticUpdate | - | - | - | Deleted | Should be determined on the side of the old platform |
| eta | - | If contains | If contains | Changed to an Instant |  |
| speedOverGround | - | If contains | If contains |  |  |
| courseOverGround | - | If contains | If contains |  |  |
| rateOfTurn | - | If contains | If contains |  |  |
| trueHeading | heading | If contains | If contains | Rename |  |
| calculatedHeading | - | - | - | Deleted | Should be derived outside of the AIS message |
| maxDraught | draught | If contains | If contains |  |  |
| alternateDraught | - | - | - | Deleted | Old inland ais message field |
| communicationState | - | - | - | Deleted | Unused |
| positionAccuracy | - | If contains | If contains |  |  |
| posAccuracyMeters | - | - | - | Deleted | Only used by Recreant? |
| positionOfTransponder | transponderPosition | When changed | If contains | Rename |  |
| aisVersion | - | When changed | If contains |  |  |
| positionSensorType | - | When changed | If contains |  |  |
| source | sources | Always | If contains | Changes to a list of sources | Currently, we merge multiple messages from multiple sources into 1 |
| category | - | - | - | Deleted | Derived field (Determined in `roepletterlijst-scheepvaart.csv`) |
| shipType | - | When changed | If contains |  |  |
| role | - | When changed | If contains | Deleted | Derived field (Set on `updateShipRoles` by `ShipRolesMonitor`) |
| status | - | When changed | If contains |  |  |
| dimensions | - | - | - | Deleted | Only used by Recreant? |
| specialManeuverIndicator | specialManeuverStatus | When changed | If contains | Rename |  |
| combinationType | eriClassification | When changed | If contains | Rename |  |
| hazardCode | - | - | - | Change from Int to Enum? | Old inland ais message field |
| visible | - | - | - | Deleted | Derived field, should not be here |
| loadedStatus | - | - | - | Deleted | Old inland ais message field |
| isSeaVessel | - | - | - | Deleted | Derived field, should not be here |
| usingRaim | - | - | - | Deleted | Unused |
| DataTerminalEquipped | usingDataTerminal | When changed | If contains | Rename |  |
| streamingIsNewUpdate | - | - | - | Deleted | Derived field, should not be here |

For the implementation itself, we could split this up into more null safe models, one for each message type. An example can be as followed for a type position A message:

| **Field** | **Mandator** | **Note** |
| --- | --- | --- |
| mmsi | Yes |  |
| messageTime | Yes |  |
| status | Yes |  |
| rateOfTurn | Yes |  |
| speedOverGround | No | `null` when not available/invalid |
| positionAccuracy | Yes |  |
| location | No | `null` when not available/invalid |
| courseOverGround | No | `null` when not available/invalid |
| heading | Yes |  |
| specialManeuverStatus | No | `null` when not available |
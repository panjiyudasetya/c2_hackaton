---
id: confluence:268632065
source: confluence
type: page
space: TC
title: KMongo deprecated move to official Kotlin driver
author: Jamie de Leest
date: '2024-08-28'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/268632065
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/268632065
---
# KMongo deprecated move to official Kotlin driver

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/268632065  

## Content

# List of applications and order of migration

| **Backend (repo name)** | **Order Group** | **Upgraded** | **Note** |
| --- | --- | --- | --- |
| smartfleet | 0 | Done |  |
| terminalplanner-backend | 1 | Done | Test: Francisco  Deploy: Jamie (Gavin check if working) |
| api | 2 | No | The only project having Spring Boot 3+  does not use mongo |
| CSI | 2 | Done | Test: Francisco : Tested  Deploy: Jamie |
| nexmoservice | 2 | No | does not use mongo |
| poma-backend | 2 | Done | Test: Francisco : Tested  Deploy: Jamie |
| portlocaltime-backend | 2 | No | does not use mongo |
| skeleton-backend | 2 | Done | Doesn’t need to be deployed |
| cargooptima-backend | 3 | Done | uses datasource history, still in PR, awaits cargooptima approval  Ask Joaquin to push this forward  Test: Francisco  Deploy: Jamie  is running on dev since 31/07/2024 to detect changes |
| portcallplus | 3 | Done | Deploy: Jamie |
| PortMatcher | 3 | Done | Deploy: Jamie |
| RouteScout | 3 | Done |  |
| shipsparelogistics-backend | 3 | Done |  |
| vesselcompliance-backend | 3 | On Dev | Awaiting until LeonJ is back from vacation. When PR is created ask LeonJ to push this forward.    Await results of pilot meeting 12-06-2024  meeting planned to implement changes on dev 10-07-2024 |
| vesselvoyage-backend | 3 | Done | Will be picked up by Darius when V2 changes will go live |
| backendPortReporter | 4 | Done | tested on DEV by Francisco |
| chorus-backend | 4 | On separate branch | Continue on preparing changes  Wait with getting this into develop, needs full integration test |
| fuelboss-backend | 4 | On separate branch | Continue on preparing changes  Wait with getting this into develop, needs full integration test |
| scrapeshark-backend | 4 | Done | Deploy: Jamie |
| vesselmatcher-backend | 4 | Done | Deploy when LeonJ is back from vacation.  Deploy: Jamie |
| ais-engine | 5 | On Dev | List of Apps   1. AisStream 2. AisRabbitMQ 3. AisDiff 4. AnchorMonitor 5. AreaMonitor 6. BerthMonitor 7. EncounterMonitor 8. StopMonitor? (Only DEV now) 9. ShipHistory 10. EventHistory 11. Revents components     TODO:   1. Deploy on DEV see if it works together with Darius 2. Create PR 3. Darius will deploy to PROD |
| portpublisher-backend | 6 | Done | Deploy: Jamie |
| portsupport-backend | 6 | Done | Deploy: Jamie |
| terminallineup-backend | 6 | Done | Sync with Wouter how to deploy on DEV first  Deploy: Jamie |
| functionalmonitoring-backend | 7 | Done | Deploy: Jamie |
| lineupcalculator-backend | 7 | Done | is not deployed anymore, Can be merged to master |
| pdfrenderer | 7 | Done | Deploy: Jamie |
| datastore-backend |  | only Dev | there are some non KMongo related commits on dev that are not merged to master awaiting feedback before merge |
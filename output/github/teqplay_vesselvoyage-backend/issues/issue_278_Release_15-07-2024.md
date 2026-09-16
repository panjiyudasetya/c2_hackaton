---
id: github:teqplay/vesselvoyage-backend:issue:278
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 278
title: Release 15-07-2024
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/278
labels: []
explicit_links: []
---
# Issue #278: Release 15-07-2024

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/278  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [e06987218d36...365cf23aa4d7](https://github.com/teqplay/vesselvoyage-backend/compare/e06987218d36...365cf23aa4d7)
**Merge commit:** [365cf23aa4d7](https://github.com/teqplay/vesselvoyage-backend/commit/365cf23aa4d7)
**Author:** Darius Wattimena
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/vesselvoyage-backend/tree/master)
**Closed On:** 2024-07-15T08:31:16.903820+00:00
**Status:** MERGED

# Changes
* Add V2 event and trace processing
    * New Visits and Voyage models for internal use
    * New ShipState for the new models
    
* V2 API models
* Toggle to enable real-time processing `processing.enable-real-time=true`
* Toggle to enable new event processing `event-processing.enable-new-definition=false`
* Toggle to enable new trace processing `trace.enable-new-definition=false`
* Add support to run VesselVoyage inside revents
    * NATS stream for V2 changes currently only used when revent profile is enabled
    
* Visit/Voyage merging for V2 to use with revents recalculation
* Recalculation of V2 flow using revents
```
revents.url=<https://reventsbackenddev.teqplay.nl>
revents.domain=keycloakdev.teqplay.nl
revents.realm=dev
revents.client-id=vesselvoyage
revents.client-secret=
```
* Event processing stats now go via Grafana
* Replaced self made Poma models with Poma API package ones
* Reworked InfraService to have support for more Poma entities like locks, terminals, etc.
* Removed statistics endpoints \(TODO ask David if we can get the frontend removed of this\)
* Removed old database migration
* Changed event processing to use AisEngine events instead of Platform event models
* kmongo deprecation
* When searching entries by id return a 404 when not found
# Breaking changes
* RabbitMQ event and AIS processing replaced with NATS
```
nats.ais-stream.enabled=false
nats.ais-stream.url=nats://localhost:4222
nats.ais-stream.username=
nats.ais-stream.password=
nats.event-stream.enabled=false
nats.event-stream.url=nats://localhost:4222
nats.event-stream.username=
nats.event-stream.password=
```


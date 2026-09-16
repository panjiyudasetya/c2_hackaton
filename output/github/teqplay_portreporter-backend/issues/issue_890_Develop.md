---
id: github:teqplay/portreporter-backend:issue:890
source: github
type: issue
repo: teqplay/portreporter-backend
number: 890
title: Develop
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/890
labels: []
explicit_links: []
---
# Issue #890: Develop

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/890  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [88442a5eb6e8...d510ea188784](https://github.com/teqplay/portreporter-backend/compare/88442a5eb6e8...d510ea188784)
**Merge commit:** [d510ea188784](https://github.com/teqplay/portreporter-backend/commit/d510ea188784)
**Author:** Shravan Shetty
**Reviewers:** Wouter Naloop
**Approvers:** Former user
**Source Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/portreporter-backend/tree/master)
**Closed On:** 2021-05-12T09:29:56.191283+00:00
**Status:** MERGED

* SmartFleet connection
* update: increased infeasible event trigger only on 3.5hrs deviation rather than 3
* update: message format for infeasible eta notification
* fix: minor fixes on infeasible event notification
* Finalize PortReporter to SmartFleet connection
* make sure a config eta notification is only triggered based on duration selected, to avoid spamming
* update: added unit test for config eta is more than eventEta
* allow access to shippingline user to /ship controller
* Add ability to list fleets of multiple companies at once
* fix: update agent even if not subscribed for, when nominated by the ADMIN
* fix: berth eta events must also be considered for portcall destinations
* fix: notification eventType is saved as formattedType instead of subscriptionType
* SmartFleet: bug fix for controller & use email for getting the user
* Fix: correct annotation and use POST for SmartFleet call
* SmartFleet: remove autoShips & add disable flag to voyage & use historic and predicted traces from SmartFleet
* SmartFleet bugfix: missing auto ships as ShipInfo and StaticShipInfo
* update: handle ship imo/mmsi change
* allowed configurable nxtport external sync



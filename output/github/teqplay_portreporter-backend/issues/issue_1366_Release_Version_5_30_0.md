---
id: github:teqplay/portreporter-backend:issue:1366
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1366
title: Release/Version 5.30.0
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1366
labels: []
explicit_links: []
---
# Issue #1366: Release/Version 5.30.0

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1366  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [6107df6fed09...5c369522e744](https://github.com/teqplay/portreporter-backend/compare/6107df6fed09...5c369522e744)
**Merge commit:** [5c369522e744](https://github.com/teqplay/portreporter-backend/commit/5c369522e744)
**Author:** Shan Minh Nguyen
**Reviewers:** 
**Approvers:** 
**Source Branch:** [release/version_5.30.0](https://github.com/teqplay/portreporter-backend/tree/release/version_5.30.0)
**Destination Branch:** [master](https://github.com/teqplay/portreporter-backend/tree/master)
**Closed On:** 2024-03-20T09:22:02.657242+00:00
**Status:** MERGED

* Added PortCallOrderLogicTest.kt and `test getOrdersForPortcall`
* Added `test isLastOrderForPortcallStayOut`
* Added `test getVisitForPortcall` and added some getTestObjects to TestHelper.kt
* Added `test findVisitsForExchange` and permitAction helper function, also added more getTestObjects to TestHelper.kt
* Added `test orderInboundVisit`
* Added `test orderInboundVisitWithDependencyOnPortcall` and getTestPortEntry
* Added `test orderShiftingVisit`
* Added `test orderOutboundVisit`
* Added `test checkIfActionIsPermitted`
* Added `test fetchVisit`
* Made a separate `test getVisitForPortcall - fail on visit not found`
* Made a separate `test findVisitsForExchange - fail on berth not found`, improved readability
* Split off the throws from `test orderInboundVisit`, improved readability
* Split off the throws from `test orderInboundVisitWithDependencyOnPortcall`, improved readability
* Split off the throw from `test orderShiftingVisit`, improved readability
* Split off the throw from `test orderOutboundVisit`, improved readability
* Split off the throws from `test checkIfActionIsPermitted`
* Split off the throws from `test fetchVisit`
* Added exception message checks to the assertThrows
* Changed `test getOrdersForPortcall` to use the fun with a user, class%, method% and line% now all 100%
* Added some lowercase functions to various functions for emails.
* Changed `when` to whenever, changed `permitAction` to `setup checkIfActionIsPermitted` and other minor improvements
* Reworked some logic and added a generic function for case insensitive searching.
* KTlint commit of shame.
* Updated base version to snapshots.
* Added missing configuration to enable JVM metrics
* Removed unneeded disabling of all actuator endpoints
* Updated vesselvoyage models through api
* remove fleet intel import controller and calls to platform
* ktlint
* Made copy and deprecated old endpoint of shippingLine and added external ref to the copied endpoint to allow both shippinglineId and externalRef.
* Fixed some methods behaviour.
* Added logging whenever a subsystem is degraded. Temporary measure for checking for develop.
* Added a flag to ignore an internal service's degraded status if enabled.
* Fixed the check by checking substring as well for degraded status when ignoring the degraded status
* Remove calls into platform to get portcalls
* Updated with some feedback from Joaquin in PR 741.
* Remove some more unused stuff
* Updated versions for release


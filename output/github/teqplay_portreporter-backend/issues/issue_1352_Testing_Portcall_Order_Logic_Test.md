---
id: github:teqplay/portreporter-backend:issue:1352
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1352
title: Testing/Portcall Order Logic Test
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1352
labels: []
explicit_links: []
---
# Issue #1352: Testing/Portcall Order Logic Test

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1352  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [5b603d9413f3...2035a915f382](https://github.com/teqplay/portreporter-backend/compare/5b603d9413f3...2035a915f382)
**Merge commit:** [2035a915f382](https://github.com/teqplay/portreporter-backend/commit/2035a915f382)
**Author:** Pim van den Toorn
**Reviewers:** Shan Minh Nguyen
**Approvers:** Former user, Pim van den Toorn
**Source Branch:** [testing/portcall_order_logic_test](https://github.com/teqplay/portreporter-backend/tree/testing/portcall_order_logic_test)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2024-02-21T09:39:15.123474+00:00
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


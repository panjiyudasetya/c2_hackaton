---
id: github:teqplay/portreporter-backend:issue:1342
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1342
title: Testing/Portcall Logic Test
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1342
labels: []
explicit_links: []
---
# Issue #1342: Testing/Portcall Logic Test

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1342  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [33c8ad6f9b56...e1fa37ac79bc](https://github.com/teqplay/portreporter-backend/compare/33c8ad6f9b56...e1fa37ac79bc)
**Merge commit:** [e1fa37ac79bc](https://github.com/teqplay/portreporter-backend/commit/e1fa37ac79bc)
**Author:** Pim van den Toorn
**Reviewers:** Joaquin Marquez Bugella, Shan Minh Nguyen
**Approvers:** Joaquin Marquez Bugella, Pim van den Toorn, Shan Minh Nguyen
**Source Branch:** [testing/portcall_logic_test](https://github.com/teqplay/portreporter-backend/tree/testing/portcall_logic_test)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-12-05T12:31:38.923778+00:00
**Status:** MERGED

* Updated the assert functions from junit.Assert to junit.jupiter.api.Assertions
* ktlint indentation fix
* Added PortCallEventTime.toESoFEvent test, moved PortCallLogicTest to same package as PortCallLogic
* Added extra assert to PortCallEventTime.toESoFEvent test, to test the default arguments
* Added List<ESoFEvent>.splitListToIndex test
* Added List<ESoFEvent>.getStartOfOutbound test, added getTestPortCallEventTime and getTestESoFEvent to TestHelper
* Added List<ESoFEvent>.getEndOfInbound test
* Added List<ESoFEvent>.toESoFEventCategories test
* Added List<ESoFEvent>.addEventIndexes test
* Added List<ESoFEvent>.groupTugs test
* Added PortCallEventTime.isDuringVisit test, added helper fun testTime
* Added List<ESoFEvent>.findEstimateEvent test
* Added List<ESoFEvent>.findAlreadyStoredEstimateEventMatch test
* Added List<ESoFEvent>.findActualEventForEstimate test
* Added List<ESoFEvent>.findClosingEventForStartServiceEvent test
* Added List<ESoFEvent>.getGroupedEvents test
* Added PortCallStatusEventsMetaData.getAllPortcallEvents test, changed getTestPortCallEventTime eventId to random string to get unique objects
* Added getESofEventsByPortcall test
* Added getShipsGoingToBerthInTheFuture test, added getShipRegisterInfoTest to TestHelper
* Added getFilteredStatusEvents test
* Added `test updatePortcallsInPortcallPlus fail on user not being authorized` and `test updatePortcallsInPortcallPlus fail on portcallId is null`
* Added `test updatePortcallsInPortcallPlus fail on portCallPlusPortCall is null` and `test updatePortcallsInPortcallPlus`
* Changed the updatePortcallsInPortcallPlus tests to include createPortcallsInPortcallPlus
* Added `test getPortcallsFromPortcallPlus fail on user not being authorized` and `test getPortcallsFromPortcallPlus`
* Added `test getOrCreatePortcall createSubscription`
* Added `test getActivePortCallsAndTerminals`
* Added `test getEtaPredictionInfo`
* Added `test getPortcallTimestamps`
* Added `test getPortcallTimestamps empty on unauthorized user`, removed some bloat
* Added `test updatePortcallExternalRef`, changed a split\(System.lineSeparator\) to lines\(\)


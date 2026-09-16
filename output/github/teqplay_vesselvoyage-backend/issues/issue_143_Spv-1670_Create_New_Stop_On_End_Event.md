---
id: github:teqplay/vesselvoyage-backend:issue:143
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 143
title: Spv-1670 Create New Stop On End Event
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/143
labels: []
explicit_links: []
---
# Issue #143: Spv-1670 Create New Stop On End Event

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/143  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [872f6919e5bc...7e43f2e3f4b8](https://github.com/teqplay/vesselvoyage-backend/compare/872f6919e5bc...7e43f2e3f4b8)
**Merge commit:** [7e43f2e3f4b8](https://github.com/teqplay/vesselvoyage-backend/commit/7e43f2e3f4b8)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [SPV-1670_create_new_stop_on_end_event](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1670_create_new_stop_on_end_event)
**Destination Branch:** [SPV-1656_stop_improvements](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1656_stop_improvements)
**Closed On:** 2023-09-15T07:52:17.745942+00:00
**Status:** MERGED

* Added logic what to do when merge a berth end event with a stop
* Changed the calculate stop mechanism to be working without a movement event
* Changed the processing of movement event to directly provide the event id, time and location
* Changed berth event merging mechanism to include creating a stop on berth end event when no matching stop
* Added two test cases that results in a new stop being created from an end event
* Fixed an issue in the calculate stop mechanism where the poma type wouldn't be set correctly
* Fixed some unexpected behaviour when merging the berth event with a stop or when creating a new one
* code cleanup
* Make sure to fill in the poma details on the merged stops
* Adjusted changes as we already set the poma info
* Adjusted the tests to ensure the poma info and detection info is correctly set


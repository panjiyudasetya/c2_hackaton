---
id: github:teqplay/portreporter-backend:issue:1303
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1303
title: 'Prp-2167 : New Endpoint To Obtain The Most Recent Fleet Still Containing A
  Given Imo.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1303
labels: []
explicit_links: []
---
# Issue #1303: Prp-2167 : New Endpoint To Obtain The Most Recent Fleet Still Containing A Given Imo.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1303  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [e8a04b7512cc...f5d795ae560b](https://github.com/teqplay/portreporter-backend/compare/e8a04b7512cc...f5d795ae560b)
**Merge commit:** [f5d795ae560b](https://github.com/teqplay/portreporter-backend/commit/f5d795ae560b)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Wouter Naloop, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [feat/PRP-2167/endpoint_to_get_most_recent_fleet_still_containing_an_imo](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-2167/endpoint_to_get_most_recent_fleet_still_containing_an_imo)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-07-04T11:53:46.654280+00:00
**Status:** MERGED

As the title states, the aim is to provide the FE with a new endpoint to get the most recent fleet \(id\) still containing a given imo.
For that, PortReporter will consult SmartFleet, however, as it’s not implemented yet, a fallback is in place to obtain that info from the received events.
The fallback can be enabled/disabled with with a config flag.
Thus, while SmartFleet implements it, the flag will be turned to true.
Main changes here are:
1. Adding the new flag in the config and use it in case smartFleet returns with a ModelNotFoundException \(yes, but I don’t control Smartfleet’s response for non-existent endpoints\).
2. Adding new endpoint `/v1/smartfleet/firstContaining/{imo} ` in SmartFleetController
3. Adding a new logic method in `SmartFleetLogic` to get the requested data.
    1. calling a new SmartFleetConnection method.
    2. If still not implemented in SmartFleet backend, call the fallback when the config flag is true.
    
4. Implement the fallback in `SmartFleetEventLogic`
5. Implement the required mongo search in `SmartFleetEventDataSource`
6. Some processsing clean-ups and small improvements.
7. UnitTest :slight_smile: 


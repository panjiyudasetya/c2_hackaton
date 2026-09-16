---
id: github:teqplay/vesselvoyage-backend:issue:137
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 137
title: Spv-1669 Create New Stop
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/137
labels: []
explicit_links: []
---
# Issue #137: Spv-1669 Create New Stop

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/137  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [e51a4c188481...58166360f5e8](https://github.com/teqplay/vesselvoyage-backend/compare/e51a4c188481...58166360f5e8)
**Merge commit:** [58166360f5e8](https://github.com/teqplay/vesselvoyage-backend/commit/58166360f5e8)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop
**Approvers:** Former user
**Source Branch:** [SPV-1669_create_new_stop](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1669_create_new_stop)
**Destination Branch:** [SPV-1656_stop_improvements](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1656_stop_improvements)
**Closed On:** 2023-09-01T11:48:21.464792+00:00
**Status:** MERGED

* Set up basic structure
* Added logic needed to create a new Stop on the berth start event
* Fixed the return type of tryMergeWithBerthEvent
* Moved the logic of creating berths to the helperFunctions file so they can be reused
* Added tests to cover the creating of a new Stop when there are no known stops
* Added some extra tests to ensure a new Stop is also created when no matching stop is found in the current stops


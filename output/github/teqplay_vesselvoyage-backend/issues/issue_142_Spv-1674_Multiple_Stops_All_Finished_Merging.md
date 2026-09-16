---
id: github:teqplay/vesselvoyage-backend:issue:142
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 142
title: Spv-1674 Multiple Stops All Finished Merging
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/142
labels: []
explicit_links: []
---
# Issue #142: Spv-1674 Multiple Stops All Finished Merging

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/142  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [368ffd2b589f...872f6919e5bc](https://github.com/teqplay/vesselvoyage-backend/compare/368ffd2b589f...872f6919e5bc)
**Merge commit:** [872f6919e5bc](https://github.com/teqplay/vesselvoyage-backend/commit/872f6919e5bc)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [SPV-1674_multiple_stops_all_finished_merging](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1674_multiple_stops_all_finished_merging)
**Destination Branch:** [SPV-1656_stop_improvements](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1656_stop_improvements)
**Closed On:** 2023-09-15T07:49:56.725994+00:00
**Status:** MERGED

* Implemented the logic when we have multiple stops and all are finished
* Changed the logic when we should drop an event, also adding the needed logic when we have an end event
* Reverted unintended naming revert
* Added a couple test cases
* ktlint
* Adjust existing tests and added a new tests case to create a new stop when all are finished and none are matching


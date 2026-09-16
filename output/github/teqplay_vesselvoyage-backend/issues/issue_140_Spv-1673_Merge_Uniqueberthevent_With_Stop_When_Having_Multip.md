---
id: github:teqplay/vesselvoyage-backend:issue:140
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 140
title: Spv-1673 Merge Uniqueberthevent With Stop When Having Multiple Stops With The
  Latest Ongoing
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/140
labels: []
explicit_links: []
---
# Issue #140: Spv-1673 Merge Uniqueberthevent With Stop When Having Multiple Stops With The Latest Ongoing

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/140  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [c37421fa9ff6...368ffd2b589f](https://github.com/teqplay/vesselvoyage-backend/compare/c37421fa9ff6...368ffd2b589f)
**Merge commit:** [368ffd2b589f](https://github.com/teqplay/vesselvoyage-backend/commit/368ffd2b589f)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [SPV-1673_multiple_stops_latest_ongoing_merging](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1673_multiple_stops_latest_ongoing_merging)
**Destination Branch:** [SPV-1656_stop_improvements](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1656_stop_improvements)
**Closed On:** 2023-09-04T12:33:59.950608+00:00
**Status:** MERGED

* Added support to merge stops when having multiple finished and the latest ongoing
* Fixed an issue where replacing a stop would result in the list order being changed
* Added all test cases possible when merging a start UniqueBerthEvent with multiple stops having the latest ongoing
* Updated logic to match expected behaviour


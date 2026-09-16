---
id: github:teqplay/vesselvoyage-backend:issue:147
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 147
title: Spv-1656 Stop Merging Fixes
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/147
labels: []
explicit_links: []
---
# Issue #147: Spv-1656 Stop Merging Fixes

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/147  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [1d8e9eda99d1...baf40bf1cb69](https://github.com/teqplay/vesselvoyage-backend/compare/1d8e9eda99d1...baf40bf1cb69)
**Merge commit:** [baf40bf1cb69](https://github.com/teqplay/vesselvoyage-backend/commit/baf40bf1cb69)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [SPV-1656_stop_merging_fixes](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1656_stop_merging_fixes)
**Destination Branch:** [SPV-1656_stop_improvements](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1656_stop_improvements)
**Closed On:** 2023-10-02T08:35:20.906202+00:00
**Status:** MERGED

* Make sure to don't throw exceptions when requesting berths as this can result in processing of events stopping
* Fix a case where the stop wouldn't be merged with the berth event when being in the berth for a long time
* Adjusted creating of a finished stop in test to include an actual time as well
* removed unused import
* Added an extra test to test a special case where the stop is created by a movement event with a time after the original time of the berth event
* Fixed the case where a unique berth event with an original time before the stop would not be merged correctly
* Corrected an old test which now fails because of the new merging tactics
* Code cleanup
* Increase the range when we merge stops with berth events


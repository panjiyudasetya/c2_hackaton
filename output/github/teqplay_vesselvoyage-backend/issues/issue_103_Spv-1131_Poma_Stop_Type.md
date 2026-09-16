---
id: github:teqplay/vesselvoyage-backend:issue:103
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 103
title: Spv-1131 Poma Stop Type
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/103
labels: []
explicit_links: []
---
# Issue #103: Spv-1131 Poma Stop Type

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/103  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [227f5dd926c6...0974d976b012](https://github.com/teqplay/vesselvoyage-backend/compare/227f5dd926c6...0974d976b012)
**Merge commit:** [0974d976b012](https://github.com/teqplay/vesselvoyage-backend/commit/0974d976b012)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [SPV-1131_poma_stop_type](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1131_poma_stop_type)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-12-01T14:20:11.536293+00:00
**Status:** MERGED

* Started supporting poma berths \+ added location based maps for finding anchorages and berths faster
* ktlint
* Finalized logic to identify the poma type of a stop
* Fixed some unit tests to support the new helper functions to find the berths and anchorages when processing events
* Added unit tests to cover the new functionality to change the stop type based on the berth found in poma
* ktlint


---
id: github:teqplay/vesselvoyage-backend:issue:90
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 90
title: Spv-1120 Stop Detection Improvements
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/90
labels: []
explicit_links: []
---
# Issue #90: Spv-1120 Stop Detection Improvements

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/90  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [206c438fb489...f3306877427d](https://github.com/teqplay/vesselvoyage-backend/compare/206c438fb489...f3306877427d)
**Merge commit:** [f3306877427d](https://github.com/teqplay/vesselvoyage-backend/commit/f3306877427d)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop
**Approvers:** Former user
**Source Branch:** [SPV-1120_stop_detection_improvements](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1120_stop_detection_improvements)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-10-10T07:38:57.694461+00:00
**Status:** MERGED

Followup PR for the stop detection changes. The most notable changes are:

* Always use the trace from platform instead of using the ongoing trace, as this can also be simplified.
* Added `ESOF_STOP_MAX_ONGOING_SPEED` that will be used to check when the latest stop is ongoing.



---
id: github:teqplay/vesselvoyage-backend:issue:14
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 14
title: Fix/Filter Ignored Shiptypes
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/14
labels: []
explicit_links: []
---
# Issue #14: Fix/Filter Ignored Shiptypes

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/14  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [8b0be1aa4156...799186f0890e](https://github.com/teqplay/vesselvoyage-backend/compare/8b0be1aa4156...799186f0890e)
**Merge commit:** [799186f0890e](https://github.com/teqplay/vesselvoyage-backend/commit/799186f0890e)
**Author:** Jos de Jong
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [fix/filter_ignored_shiptypes](https://github.com/teqplay/vesselvoyage-backend/tree/fix/filter_ignored_shiptypes)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2021-09-23T08:52:27.514186+00:00
**Status:** MERGED

Fix a stupid bug introduced after a refactoring from using mmsi’s to using imo’s. 

basically, `getShipTypeFromIMO(teqplayEvent.shipMmsi)` must be `getShipTypeFromIMO(imo)`. 

Added a few other small improvements and unit tests.



---
id: github:teqplay/vesselvoyage-backend:issue:327
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 327
title: Spv-2290 Sof Pilots
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/327
labels: []
explicit_links:
- jira:SPV-2290
---
# Issue #327: Spv-2290 Sof Pilots

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/327  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [27c0f758b739...0d28351c9288](https://github.com/teqplay/vesselvoyage-backend/compare/27c0f758b739...0d28351c9288)
**Merge commit:** [0d28351c9288](https://github.com/teqplay/vesselvoyage-backend/commit/0d28351c9288)
**Author:** Leon Joosse
**Reviewers:** Michel Wilson, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-2290-pilots](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2290-pilots)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-08-22T12:40:41.596385+00:00
**Status:** MERGED

Adds the inbound and outbound pilot for the PTO SOF:
* Inbound pilot: last pilot encounter before first berth
* Outbound pilot first pilot encounter after last berth
The system also tries to match the pilot boarding place area to the pilot encounter, based on `encounter.start..end` and `pilotAreaActivity.start..end`. 


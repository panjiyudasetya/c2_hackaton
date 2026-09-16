---
id: github:teqplay/vesselvoyage-backend:issue:201
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 201
title: 'Feat: Expose Poma Areaid For Port & Add Dry-Run V2 Endpoint For (R)Events'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/201
labels: []
explicit_links:
- jira:SPV-2059
---
# Issue #201: Feat: Expose Poma Areaid For Port & Add Dry-Run V2 Endpoint For (R)Events

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/201  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [5be65e2a8cf6...c63dcb157722](https://github.com/teqplay/vesselvoyage-backend/compare/5be65e2a8cf6...c63dcb157722)
**Merge commit:** [c63dcb157722](https://github.com/teqplay/vesselvoyage-backend/commit/c63dcb157722)
**Author:** Former user
**Reviewers:** Wouter Naloop, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-2059-add-dry-run-endpoint-for-revents](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2059-add-dry-run-endpoint-for-revents)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-04-08T07:46:02.539430+00:00
**Status:** MERGED

This PR contains a fix for ports in the V2 definitions having the unlocode as their `areaId`, whereas it should be the POMA ID instead.
Also, adding support for dry-running events for V2, to be used by \(r\)events when doing post-processing/bypassing.


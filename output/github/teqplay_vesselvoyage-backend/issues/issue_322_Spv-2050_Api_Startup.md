---
id: github:teqplay/vesselvoyage-backend:issue:322
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 322
title: Spv-2050 Api Startup
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/322
labels: []
explicit_links:
- jira:SPV-2050
---
# Issue #322: Spv-2050 Api Startup

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/322  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [e776c8d4135e...601c401efa58](https://github.com/teqplay/vesselvoyage-backend/compare/e776c8d4135e...601c401efa58)
**Merge commit:** [601c401efa58](https://github.com/teqplay/vesselvoyage-backend/commit/601c401efa58)
**Author:** Leon Joosse
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-2050-api-startup](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2050-api-startup)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-08-14T12:26:20.467152+00:00
**Status:** MERGED

* Add `ApiStartUpService`, to load `infraService` and `staticShipInfoService` blocking \(before application can receive requests\)
* Fix nullability issue and view constant


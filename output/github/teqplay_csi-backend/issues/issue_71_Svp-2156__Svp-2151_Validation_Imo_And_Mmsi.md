---
id: github:teqplay/csi-backend:issue:71
source: github
type: issue
repo: teqplay/csi-backend
number: 71
title: Svp-2156, Svp-2151 Validation Imo And Mmsi
author: jbugella
state: closed
date: '2025-01-07'
url: https://github.com/teqplay/csi-backend/issues/71
labels: []
explicit_links:
- jira:SVP-2156
---
# Issue #71: Svp-2156, Svp-2151 Validation Imo And Mmsi

**Repo:** teqplay/csi-backend  
**URL:** https://github.com/teqplay/csi-backend/issues/71  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-07  
**Closed:** 2025-01-07  

## Description

**Full diff:** [701037d2e4b6...c7451ef5d997](https://github.com/teqplay/csi-backend/compare/701037d2e4b6...c7451ef5d997)
**Merge commit:** [c7451ef5d997](https://github.com/teqplay/csi-backend/commit/c7451ef5d997)
**Author:** Jamie de Leest
**Reviewers:** Michel Wilson, Darius Wattimena
**Approvers:** Former user
**Source Branch:** [SVP-2156-Validation-imo-and-mmsi](https://github.com/teqplay/csi-backend/tree/SVP-2156-Validation-imo-and-mmsi)
**Destination Branch:** [develop](https://github.com/teqplay/csi-backend/tree/develop)
**Closed On:** 2024-06-25T08:09:00.780616+00:00
**Status:** MERGED

* Validate IMO and MMSI on ticket completion
* Generate Tickets For invalid IMOs and MMSIs
* added a duplicate imo check to ship validation
* enforced validation in ShipRegisterInfoService
* changed ticket creation for invalid imo and mmsi
* Fixed tests  and created a test for imo and mmsi validation
* Fixed that ship counted them selfs as a duplicate imo
* added support for ghostShip and Disabled filter in advanced search


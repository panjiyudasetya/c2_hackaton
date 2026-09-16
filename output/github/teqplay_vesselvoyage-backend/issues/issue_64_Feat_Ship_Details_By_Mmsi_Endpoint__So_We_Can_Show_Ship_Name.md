---
id: github:teqplay/vesselvoyage-backend:issue:64
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 64
title: Feat/Ship Details By Mmsi Endpoint, So We Can Show Ship Names For All Encounters
  With Barges
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/64
labels: []
explicit_links: []
---
# Issue #64: Feat/Ship Details By Mmsi Endpoint, So We Can Show Ship Names For All Encounters With Barges

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/64  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [6ee31bd38bea...15adf256daa2](https://github.com/teqplay/vesselvoyage-backend/compare/6ee31bd38bea...15adf256daa2)
**Merge commit:** [15adf256daa2](https://github.com/teqplay/vesselvoyage-backend/commit/15adf256daa2)
**Author:** Jos de Jong
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [feat/ship_details_by_mmsi_endpoint](https://github.com/teqplay/vesselvoyage-backend/tree/feat/ship_details_by_mmsi_endpoint)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-02-23T11:13:07.309825+00:00
**Status:** MERGED

* Implement endpoint /v1/ships/static/mmsis, fetching from CSI with fallback on platform
* Implement caching for it
* There is a breaking change needed in the `ShipDetails` model, making the `imo` nullable. As far as I know, this model is only used for the VesselVoyage frontend
* You can see that the refactoring needed now in the unit test would benefit from rewriting it to Spring tests, that would be less verbose :grin:


---
id: github:teqplay/vesselvoyage-backend:issue:349
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 349
title: Spv-2372 Extend V2 Apis With Finished Filter
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/349
labels: []
explicit_links: []
---
# Issue #349: Spv-2372 Extend V2 Apis With Finished Filter

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/349  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [7050b0576477...5a89c40e6fe3](https://github.com/teqplay/vesselvoyage-backend/compare/7050b0576477...5a89c40e6fe3)
**Merge commit:** [5a89c40e6fe3](https://github.com/teqplay/vesselvoyage-backend/commit/5a89c40e6fe3)
**Author:** Leon Joosse
**Reviewers:** Michel Wilson, Darius Wattimena, Joost Dambrink
**Approvers:** Joost Dambrink, Darius Wattimena
**Source Branch:** [SPV-2372-extend-v2-apis](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2372-extend-v2-apis)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-10-23T09:31:30.538567+00:00
**Status:** MERGED

This PR adds a filter to visit/voyage/sof list endpoints, to limit the result set to only finished entries, ongoing entries or both.
For services and data layer I implemented an enum to pass around the filter, the endpoints use a `Boolean?`. An enum in an endpoint is usually a bad idea, think of the case we had with ShipCategoryV1 and V2 with CSI, therefore using a Boolean


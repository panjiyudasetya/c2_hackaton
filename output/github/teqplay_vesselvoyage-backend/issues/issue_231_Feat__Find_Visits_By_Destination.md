---
id: github:teqplay/vesselvoyage-backend:issue:231
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 231
title: 'Feat: Find Visits By Destination'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/231
labels: []
explicit_links: []
---
# Issue #231: Feat: Find Visits By Destination

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/231  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [0874b61da2ab...170be6454d0b](https://github.com/teqplay/vesselvoyage-backend/compare/0874b61da2ab...170be6454d0b)
**Merge commit:** [170be6454d0b](https://github.com/teqplay/vesselvoyage-backend/commit/170be6454d0b)
**Author:** Former user
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-1573-request-visits-by-destination](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1573-request-visits-by-destination)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-05-13T09:04:06.475188+00:00
**Status:** MERGED

When a ship enters another port or goes into an anchorage, it will transition from the voyage to a visit.
At that moment SmartFleet will lose track of the ship, since it can’t find entries by destination for this ship anymore.
To solve this VesselVoyage gets an endpoint that returns non-finished visits where a destination matches.


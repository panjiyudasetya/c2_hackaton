---
id: github:teqplay/vesselvoyage-backend:issue:200
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 200
title: 'Feat: Add Endpoint To Track Scenarios, Created Outside Of Vesselvoyage'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/200
labels: []
explicit_links:
- jira:SPV-2033
---
# Issue #200: Feat: Add Endpoint To Track Scenarios, Created Outside Of Vesselvoyage

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/200  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [52987549f184...94f04f3d04ec](https://github.com/teqplay/vesselvoyage-backend/compare/52987549f184...94f04f3d04ec)
**Merge commit:** [94f04f3d04ec](https://github.com/teqplay/vesselvoyage-backend/commit/94f04f3d04ec)
**Author:** Former user
**Reviewers:** Wouter Naloop, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-2033-allow-pto-to-inform-vessel-voyage-of-running-scenarios](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2033-allow-pto-to-inform-vessel-voyage-of-running-scenarios)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-08-26T07:49:35.828403+00:00
**Status:** MERGED

Adds an endpoint to track scenarios that have been created outside of VesselVoyage. This way PTO could create a report, and later on send a request to VesselVoyage when its approved to merge back the data.
The endpoint is:
```
POST /v2/recalculate/scenario/{scenarioId}
```


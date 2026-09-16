---
id: github:teqplay/vesselvoyage-backend:issue:161
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 161
title: Spv-1939 Split Processing
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/161
labels: []
explicit_links: []
---
# Issue #161: Spv-1939 Split Processing

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/161  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [2d6b4fc9f849...d2cd6ce5132f](https://github.com/teqplay/vesselvoyage-backend/compare/2d6b4fc9f849...d2cd6ce5132f)
**Merge commit:** [d2cd6ce5132f](https://github.com/teqplay/vesselvoyage-backend/commit/d2cd6ce5132f)
**Author:** Darius Wattimena
**Reviewers:** Michel Wilson, Wouter Naloop
**Approvers:** Former user
**Source Branch:** [SPV-1939-split-processing](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1939-split-processing)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-02-07T10:51:32.932630+00:00
**Status:** MERGED

* Added profile annotations for processing and api
* Added profile annotations to all endpoints and some services
* Make sure everything works when either using the processing or api profile
* Adjusted processing tests to ensure they work with the new ShipStateService
* Changed application test to ensure they work with the correct profiles
* code cleanup
---
When running VesselVoyage you now have to provide one of the following profiles:
`api` to only expose endpoints that don’t touch any processing
`processing` to do any processing of events and save the updated Visit/Voyage in the database \(this also includes any frontend related calls\)
You can also enable both profiles to get the same backend as is currently running on prod and dev


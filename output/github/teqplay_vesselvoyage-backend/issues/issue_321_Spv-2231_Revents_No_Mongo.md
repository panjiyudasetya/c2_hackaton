---
id: github:teqplay/vesselvoyage-backend:issue:321
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 321
title: Spv-2231 Revents No Mongo
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/321
labels: []
explicit_links: []
---
# Issue #321: Spv-2231 Revents No Mongo

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/321  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [fe37e7c431b9...1a9b9922eeac](https://github.com/teqplay/vesselvoyage-backend/compare/fe37e7c431b9...1a9b9922eeac)
**Merge commit:** [1a9b9922eeac](https://github.com/teqplay/vesselvoyage-backend/commit/1a9b9922eeac)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse, Wouter Naloop
**Approvers:** Leon Joosse
**Source Branch:** [SPV-2231-revents-no-mongo](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2231-revents-no-mongo)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-08-15T09:19:23.520198+00:00
**Status:** MERGED

* Exclude mongo when running in revents mode
* Added profiles where needed to be able to exclude mongo and split the trace service to have getting the AIS data available when running in revents
* Cleaned up code and make sure VesselVoyage can run when only having the API profile enabled
* Exclude the mongo auth AutoConfiguration aswell
* Added more auto configurations that need to be excluded when running revents
* Added more missing excluding of auto configurations


---
id: github:teqplay/vesselvoyage-backend:issue:238
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 238
title: Spv-2119 Pilot Area Support
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/238
labels: []
explicit_links:
- jira:SPV-2119
---
# Issue #238: Spv-2119 Pilot Area Support

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/238  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [ab70ec24f119...da96d1f7a2b5](https://github.com/teqplay/vesselvoyage-backend/compare/ab70ec24f119...da96d1f7a2b5)
**Merge commit:** [da96d1f7a2b5](https://github.com/teqplay/vesselvoyage-backend/commit/da96d1f7a2b5)
**Author:** Darius Wattimena
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [SPV-2119-pilot-area-support](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2119-pilot-area-support)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-05-23T09:25:02.658911+00:00
**Status:** MERGED

* Added a bit more logging when loading an infra cache
* Adjust tests to expect support for pilot area events to adjust the pilotAreaActivities field
* Added an event model for a pilot area event
* Added all classes needed to support pilot area event processing
* Adjusted existing tests to include the new PilotAreaProcessor


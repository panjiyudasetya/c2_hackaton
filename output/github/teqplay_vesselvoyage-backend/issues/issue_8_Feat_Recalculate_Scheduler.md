---
id: github:teqplay/vesselvoyage-backend:issue:8
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 8
title: Feat/Recalculate Scheduler
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/8
labels: []
explicit_links: []
---
# Issue #8: Feat/Recalculate Scheduler

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/8  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [6d5b0253d5ca...1fa7dfb5bd33](https://github.com/teqplay/vesselvoyage-backend/compare/6d5b0253d5ca...1fa7dfb5bd33)
**Merge commit:** [1fa7dfb5bd33](https://github.com/teqplay/vesselvoyage-backend/commit/1fa7dfb5bd33)
**Author:** Jos de Jong
**Reviewers:** 
**Approvers:** 
**Source Branch:** [feat/recalculate_scheduler](https://github.com/teqplay/vesselvoyage-backend/tree/feat/recalculate_scheduler)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2021-08-24T07:42:42.121607+00:00
**Status:** MERGED

* Implement `RecalculationService`
* Rename and merge permission VISIT and VOYAGE to SHIP
* Reduce the amount of logging by changing a lot of `log.info` into `log.debug`
* Log stats once a minute with the amount of received and processed events
* Improve the event stats a bit
* Let the processEvent functions return a list with issues too instead of logging them
* Ignore EtaRequestEvent and HamisPilotBoardingEtaEvent for now
* Check the returned `issues` in ProcessAnchorEventTest
* Update to the latest version of platform and skeleton \(fixing not being able to unmarshall the new `PortcallFinishEvent`\)



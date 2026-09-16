---
id: github:teqplay/portreporter-backend:issue:866
source: github
type: issue
repo: teqplay/portreporter-backend
number: 866
title: Release 4.5.0
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/866
labels: []
explicit_links: []
---
# Issue #866: Release 4.5.0

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/866  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [fc84f02092e1...7a05e0024295](https://github.com/teqplay/portreporter-backend/compare/fc84f02092e1...7a05e0024295)
**Merge commit:** [7a05e0024295](https://github.com/teqplay/portreporter-backend/commit/7a05e0024295)
**Author:** Shravan Shetty
**Reviewers:** 
**Approvers:** 
**Source Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/portreporter-backend/tree/master)
**Closed On:** 2021-03-19T08:27:30.450570+00:00
**Status:** MERGED

* adding pbp eta agent, berth eta agent and nomination agent events.
* fix: add subscriptionIds only for bargeMissed events
* update: added a static list of companies/sources for which subscription based on alias should be done. Added Vopak SGSIN as a result
* fix: get nextCategory for shifting event too
* update: cleanup. Use fromLocation from previousVisit, rather than parse the events
* fix: do not show official reporting for non-NLRTM ports
* update: moved no notification on portcall cancellation from notificationLogic to official reporting qualification function
* allow same ship as part of multiple timecharters
* update: added eta prediction info for a specific port



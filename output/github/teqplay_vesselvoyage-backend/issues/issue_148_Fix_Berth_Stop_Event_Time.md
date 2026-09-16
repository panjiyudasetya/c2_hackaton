---
id: github:teqplay/vesselvoyage-backend:issue:148
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 148
title: Fix/Berth Stop Event Time
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/148
labels: []
explicit_links: []
---
# Issue #148: Fix/Berth Stop Event Time

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/148  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [ea6233b0ba9c...8379a4ce44f0](https://github.com/teqplay/vesselvoyage-backend/compare/ea6233b0ba9c...8379a4ce44f0)
**Merge commit:** [8379a4ce44f0](https://github.com/teqplay/vesselvoyage-backend/commit/8379a4ce44f0)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [fix/berth_stop_event_time](https://github.com/teqplay/vesselvoyage-backend/tree/fix/berth_stop_event_time)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2023-10-23T13:30:29.567580+00:00
**Status:** MERGED

* Added an extra test case to ensure no new berth event is added when the time is already filled
* Changed around some code to make sure the berth event times are not overwritten


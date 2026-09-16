---
id: github:teqplay/portreporter-backend:issue:1356
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1356
title: Some Small Fixes And Renamed Functions To Clearly Show What They Are Doing.
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1356
labels: []
explicit_links: []
---
# Issue #1356: Some Small Fixes And Renamed Functions To Clearly Show What They Are Doing.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1356  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [39b01e1439a8...9d3baa272a45](https://github.com/teqplay/portreporter-backend/compare/39b01e1439a8...9d3baa272a45)
**Merge commit:** [9d3baa272a45](https://github.com/teqplay/portreporter-backend/commit/9d3baa272a45)
**Author:** Shan Minh Nguyen
**Reviewers:** Wouter Naloop, Darius Wattimena, Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella, Wouter Naloop
**Source Branch:** [feature/hotfixes_pre_handle_and_caching_timers](https://github.com/teqplay/portreporter-backend/tree/feature/hotfixes_pre_handle_and_caching_timers)
**Destination Branch:** [master](https://github.com/teqplay/portreporter-backend/tree/master)
**Closed On:** 2024-01-11T15:20:22.508343+00:00
**Status:** MERGED

* Internal services should only report UP or Degraded so removed the DOWN.
* Also removed some unnecessary code and renamed them for clearer read purposes
* 1 Bugfix where it returned true instead of false where it would allow endpoint requests to be executed whilst the service might be down
* Lowered the CSI caching timers to 5 minutes to be more in line with other caching in PRP \(previously requested by Maurice to be 24 hours would’ve been sufficient\)


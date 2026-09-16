---
id: github:teqplay/portreporter-backend:issue:1280
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1280
title: 'Smartfleetevents : Make The Smartfleetmessageformat Leaner Around The Event''S
  Port.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1280
labels: []
explicit_links: []
---
# Issue #1280: Smartfleetevents : Make The Smartfleetmessageformat Leaner Around The Event'S Port.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1280  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [42c0b0118e63...bea6dd74cf04](https://github.com/teqplay/portreporter-backend/compare/42c0b0118e63...bea6dd74cf04)
**Merge commit:** [bea6dd74cf04](https://github.com/teqplay/portreporter-backend/commit/bea6dd74cf04)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Wouter Naloop, Shan Minh Nguyen
**Approvers:** Shan Minh Nguyen
**Source Branch:** [feat/make_SmartFleetMessageFormat_leaner](https://github.com/teqplay/portreporter-backend/tree/feat/make_SmartFleetMessageFormat_leaner)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-05-31T10:13:00.454080+00:00
**Status:** MERGED

Restructuring a bit the code as following:
1. Move `getUNLOCODEFromAreaMonitorType` and `getUNLOCODEFromAreaPortType` from `PortCallEventUtils.kt` to `SmartFleetEventLogic.kt`
2. Use the already calculated event’s port in to as argument for `messageFormat` instead of `pomaInfrastructureClient` to avoid unnecessary calculations and calls.
3. Adapt unitTests.


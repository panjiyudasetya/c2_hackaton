---
id: github:teqplay/portreporter-backend:issue:963
source: github
type: issue
repo: teqplay/portreporter-backend
number: 963
title: Management Of Smartfleet Service Exceptions
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/963
labels: []
explicit_links: []
---
# Issue #963: Management Of Smartfleet Service Exceptions

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/963  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [ee4e0d6478ee...f5d719babc86](https://github.com/teqplay/portreporter-backend/compare/ee4e0d6478ee...f5d719babc86)
**Merge commit:** [f5d719babc86](https://github.com/teqplay/portreporter-backend/commit/f5d719babc86)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman
**Approvers:** Former user
**Source Branch:** [PRP-116-return-502-instead-of-401-when-smart-fleet-is-down](https://github.com/teqplay/portreporter-backend/tree/PRP-116-return-502-instead-of-401-when-smart-fleet-is-down)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2021-10-05T06:46:32.588893+00:00
**Status:** MERGED

* Manage SmartFleet service responses returning HTTP Status 502 instead of 401.
* Manage the situation when SmartFleet secret key is shorter than 32 chars \(it triggered a NPE\).


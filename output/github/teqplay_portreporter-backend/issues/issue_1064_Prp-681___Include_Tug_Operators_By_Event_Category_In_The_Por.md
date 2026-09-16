---
id: github:teqplay/portreporter-backend:issue:1064
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1064
title: 'Prp-681 : Include Tug Operators By Event Category In The Portcall'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1064
labels: []
explicit_links: []
---
# Issue #1064: Prp-681 : Include Tug Operators By Event Category In The Portcall

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1064  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [409156ad5535...cc28da365346](https://github.com/teqplay/portreporter-backend/compare/409156ad5535...cc28da365346)
**Merge commit:** [cc28da365346](https://github.com/teqplay/portreporter-backend/commit/cc28da365346)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [PRP-681/feat/adding_tug_operation_info_to_portcall](https://github.com/teqplay/portreporter-backend/tree/PRP-681/feat/adding_tug_operation_info_to_portcall)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-04-11T08:34:48.495120+00:00
**Status:** MERGED

* Including the new field _**towingOperators**_ in the portcall data model.
* Obtaining the tugOperator when the event **TUGSSTANDBY\_AT\_VESSEL** arrives and update the corresponding towingOperator in the portcall current status.
* Additionally, the port field is included in the tugOperator model.



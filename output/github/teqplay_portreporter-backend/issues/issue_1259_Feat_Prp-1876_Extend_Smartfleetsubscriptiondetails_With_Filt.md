---
id: github:teqplay/portreporter-backend:issue:1259
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1259
title: Feat/Prp-1876/Extend Smartfleetsubscriptiondetails With Filterbyports
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1259
labels: []
explicit_links:
- jira:PRP-1876
---
# Issue #1259: Feat/Prp-1876/Extend Smartfleetsubscriptiondetails With Filterbyports

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1259  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [390c2af99071...8ffdb96c4540](https://github.com/teqplay/portreporter-backend/compare/390c2af99071...8ffdb96c4540)
**Merge commit:** [8ffdb96c4540](https://github.com/teqplay/portreporter-backend/commit/8ffdb96c4540)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Wouter Naloop
**Approvers:** Former user
**Source Branch:** [feat/PRP-1876/extend_SmartFleetSubscriptionDetails_with_filterByPorts](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-1876/extend_SmartFleetSubscriptionDetails_with_filterByPorts)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-05-05T07:36:42.239447+00:00
**Status:** MERGED

* Extending SmartfleetSubscriptionDetails with Ports \(if empty, it’s not filtered\).
* Obtaining ports from Berth and Port's events with fallbacks \(in case of missing them\).
* Adding unitTests for port filtering scenarios.
* **Bonus!** Fix a SmartFleetSubscritionDetails scenario \(it was not possible to remove subscriptions when no mediums\).


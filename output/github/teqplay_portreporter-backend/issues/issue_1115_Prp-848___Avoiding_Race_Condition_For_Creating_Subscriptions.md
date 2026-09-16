---
id: github:teqplay/portreporter-backend:issue:1115
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1115
title: 'Prp-848 : Avoiding Race Condition For Creating Subscriptions For The Same
  User.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1115
labels: []
explicit_links:
- jira:PRP-848
---
# Issue #1115: Prp-848 : Avoiding Race Condition For Creating Subscriptions For The Same User.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1115  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [037365ebb37f...ffe192f08ceb](https://github.com/teqplay/portreporter-backend/compare/037365ebb37f...ffe192f08ceb)
**Merge commit:** [ffe192f08ceb](https://github.com/teqplay/portreporter-backend/commit/ffe192f08ceb)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [feat/PRP-848/avoid_misleading_create_subscription_mongo_error](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-848/avoid_misleading_create_subscription_mongo_error)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-06-24T08:13:13.711807+00:00
**Status:** MERGED

Just removing parallel run of the four subscriptionProfile assigments.



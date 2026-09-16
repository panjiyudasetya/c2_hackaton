---
id: github:teqplay/portreporter-backend:issue:916
source: github
type: issue
repo: teqplay/portreporter-backend
number: 916
title: N24/48 Prediction Subscription
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/916
labels: []
explicit_links: []
---
# Issue #916: N24/48 Prediction Subscription

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/916  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [d57ce5c1af2b...811ec3b6ad6a](https://github.com/teqplay/portreporter-backend/compare/d57ce5c1af2b...811ec3b6ad6a)
**Merge commit:** [811ec3b6ad6a](https://github.com/teqplay/portreporter-backend/commit/811ec3b6ad6a)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Shravan Shetty
**Approvers:** Shravan Shetty
**Source Branch:** [N24/48_prediction_subscription](https://github.com/teqplay/portreporter-backend/tree/N24/48_prediction_subscription)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2021-07-27T09:21:12.960586+00:00
**Status:** MERGED

* Using PortCallEventType.name instead of PortcallEventType.getEventName\(\) in getPortCallEventTypeString\(String\)
* Removing elements from medium hashset in 'serialization test \(10\)' in SubscriptionLogicTest as hashset element's order is not guaranteed, which introduces a random degree of failing in the test case


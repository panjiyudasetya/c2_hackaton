---
id: github:teqplay/portreporter-backend:issue:1214
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1214
title: 'Prp-1460: New Endpoint For Getting The Payment Delay Statistics Given A Period
  Of Time.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1214
labels: []
explicit_links:
- jira:PRP-1460
---
# Issue #1214: Prp-1460: New Endpoint For Getting The Payment Delay Statistics Given A Period Of Time.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1214  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [6fd036021046...169511a3acd6](https://github.com/teqplay/portreporter-backend/compare/6fd036021046...169511a3acd6)
**Merge commit:** [169511a3acd6](https://github.com/teqplay/portreporter-backend/commit/169511a3acd6)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Wouter Naloop, Darius Wattimena, Gavin den Hollander
**Approvers:** Wouter Naloop
**Source Branch:** [feat/PRP-1460/new_endpoint_to_obtain_payment_duration_statistics_in_buckets](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-1460/new_endpoint_to_obtain_payment_duration_statistics_in_buckets)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-02-21T11:55:52.924041+00:00
**Status:** MERGED

Endpoint to get the payment delay statistics \(total and grouped by company\), classified as:
* In time \(0-7 days\)
* Late \(8-90 days\)
* Very late \(90-180 days\)
* Extremely late \(>180 days\)
* Unpaid
Adding you, @{5e37d9154512b80ca4319871} , as for getting the distinct pairs company/type I’m using an aggregate and you seem familiar to them.


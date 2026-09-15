---
id: github:teqplay/vesselvoyage-backend:issue:368
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 368
title: 'Spv-2391: Fix For Thread Lock When Rabbitmq Goes Down'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/368
labels: []
explicit_links:
- jira:SPV-2391
---
# Issue #368: Spv-2391: Fix For Thread Lock When Rabbitmq Goes Down

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/368  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [e30d8c14fe5b...aad337a35481](https://github.com/teqplay/vesselvoyage-backend/compare/e30d8c14fe5b...aad337a35481)
**Merge commit:** [aad337a35481](https://github.com/teqplay/vesselvoyage-backend/commit/aad337a35481)
**Author:** Joost Dambrink
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-2391-thread-lock](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2391-thread-lock)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-11-15T08:07:42.385852+00:00
**Status:** MERGED

* create recursive retry mechanism instead of throwing exception for rabbitmq send
* added test


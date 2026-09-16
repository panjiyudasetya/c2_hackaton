---
id: github:teqplay/portreporter-backend:issue:1389
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1389
title: Feature/Updated Custom Interceptors And Update Skeleton Version
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1389
labels: []
explicit_links: []
---
# Issue #1389: Feature/Updated Custom Interceptors And Update Skeleton Version

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1389  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [e1e286ecc389...d88ad3de9fa4](https://github.com/teqplay/portreporter-backend/compare/e1e286ecc389...d88ad3de9fa4)
**Merge commit:** [d88ad3de9fa4](https://github.com/teqplay/portreporter-backend/commit/d88ad3de9fa4)
**Author:** Shan Minh Nguyen
**Reviewers:** Darius Wattimena, Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [feature/updated_custom_interceptors](https://github.com/teqplay/portreporter-backend/tree/feature/updated_custom_interceptors)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2024-09-05T08:46:54.642813+00:00
**Status:** MERGED

* Catching 5xx status codes since it got ignored due to the exception only sending 4xx status codes
* KTLint
* Updated skeleton version and updated SmartFleetEventLogic due to PoMa model update
* Updated unit test due to poma model update


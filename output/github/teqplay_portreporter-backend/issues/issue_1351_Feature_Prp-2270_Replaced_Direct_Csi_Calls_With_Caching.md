---
id: github:teqplay/portreporter-backend:issue:1351
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1351
title: Feature/Prp-2270 Replaced Direct Csi Calls With Caching
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1351
labels: []
explicit_links: []
---
# Issue #1351: Feature/Prp-2270 Replaced Direct Csi Calls With Caching

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1351  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [e1fa37ac79bc...9f4625651ecd](https://github.com/teqplay/portreporter-backend/compare/e1fa37ac79bc...9f4625651ecd)
**Merge commit:** [9f4625651ecd](https://github.com/teqplay/portreporter-backend/commit/9f4625651ecd)
**Author:** Shan Minh Nguyen
**Reviewers:** Wouter Naloop, Joaquin Marquez Bugella
**Approvers:** Former user
**Source Branch:** [feature/PRP-2270_replaced_direct_csi_calls_with_caching](https://github.com/teqplay/portreporter-backend/tree/feature/PRP-2270_replaced_direct_csi_calls_with_caching)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-12-06T07:57:57.732255+00:00
**Status:** MERGED

* Replaced all csi calls in shipcontroller with a caching proxy to csi.
* KTLint commit of shame.


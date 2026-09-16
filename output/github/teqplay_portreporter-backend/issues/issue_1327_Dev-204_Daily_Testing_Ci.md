---
id: github:teqplay/portreporter-backend:issue:1327
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1327
title: Dev-204 Daily Testing Ci
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1327
labels: []
explicit_links: []
---
# Issue #1327: Dev-204 Daily Testing Ci

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1327  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [05f92f8062a5...2e61f24407d4](https://github.com/teqplay/portreporter-backend/compare/05f92f8062a5...2e61f24407d4)
**Merge commit:** [2e61f24407d4](https://github.com/teqplay/portreporter-backend/commit/2e61f24407d4)
**Author:** Darius Wattimena
**Reviewers:** Joaquin Marquez Bugella, Shan Minh Nguyen
**Approvers:** Shan Minh Nguyen
**Source Branch:** [DEV-204_daily_testing_ci](https://github.com/teqplay/portreporter-backend/tree/DEV-204_daily_testing_ci)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-09-07T15:25:19.765927+00:00
**Status:** MERGED

* Updated CI script to set the tested daily testing version to latest build
* Added missing reference to TAG
* Correctly set tag
* Set build number first to avoid null
* Make sure to update daily testing version when on develop branch


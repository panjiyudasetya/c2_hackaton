---
id: github:teqplay/portreporter-backend:issue:894
source: github
type: issue
repo: teqplay/portreporter-backend
number: 894
title: Dashboard Column Configurations
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/894
labels: []
explicit_links: []
---
# Issue #894: Dashboard Column Configurations

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/894  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [77640dc60e80...5622910357dd](https://github.com/teqplay/portreporter-backend/compare/77640dc60e80...5622910357dd)
**Merge commit:** [5622910357dd](https://github.com/teqplay/portreporter-backend/commit/5622910357dd)
**Author:** Former user
**Reviewers:** Shravan Shetty
**Approvers:** Shravan Shetty
**Source Branch:** [dashboard-column-configuration](https://github.com/teqplay/portreporter-backend/tree/dashboard-column-configuration)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2024-08-26T07:49:40.292654+00:00
**Status:** MERGED

Related card:  
[https://trello.com/c/3l9ebbcj/8568-43-add-column-configuration-per-company-per-company-type](https://trello.com/c/3l9ebbcj/8568-43-add-column-configuration-per-company-per-company-type)

Changes:

* adds a `DashboardController` which currently only contains the column configurations, but could later on be extended
* the column configuration first looks for the specific company and then to a default config, and lastly throws an exception if nothing is found



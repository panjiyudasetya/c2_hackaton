---
id: github:teqplay/poma-backend:issue:131
source: github
type: issue
repo: teqplay/poma-backend
number: 131
title: Develop
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/131
labels: []
explicit_links: []
---
# Issue #131: Develop

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/131  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [dedbea03066f...7cc7226d1b3a](https://github.com/teqplay/poma-backend/compare/dedbea03066f...7cc7226d1b3a)
**Merge commit:** [7cc7226d1b3a](https://github.com/teqplay/poma-backend/commit/7cc7226d1b3a)
**Author:** Wouter Naloop
**Reviewers:** Darius Wattimena, Jamie de Leest
**Approvers:** Darius Wattimena
**Source Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/poma-backend/tree/master)
**Closed On:** 2024-04-11T11:36:33.375550+00:00
**Status:** MERGED

* Expose JVM metrics
* fix replace port, when port is not exists in teqplay database
* Removed KMongo from datasource's
* ktlint \+ fixing tests
* fix security paths
* removed mavenLocal repository
* Fixed mongoAutoConfiguration to a localhost database
* changed skeleton version to the fixed version
* in sanitizing of the data make sure "" means the same as null to prevent other project from failing on the ?: checks


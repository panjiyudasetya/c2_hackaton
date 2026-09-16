---
id: github:teqplay/poma-backend:issue:29
source: github
type: issue
repo: teqplay/poma-backend
number: 29
title: Develop
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/29
labels: []
explicit_links: []
---
# Issue #29: Develop

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/29  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [2c1ea481a315...5f2ab3facbcf](https://github.com/teqplay/poma-backend/compare/2c1ea481a315...5f2ab3facbcf)
**Merge commit:** [5f2ab3facbcf](https://github.com/teqplay/poma-backend/commit/5f2ab3facbcf)
**Author:** Wouter Naloop
**Reviewers:** Darius Wattimena
**Approvers:** 
**Source Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/poma-backend/tree/master)
**Closed On:** 2022-03-23T10:36:49.868796+00:00
**Status:** MERGED

* Add all countries to poma

* Add endpoint for country statistics

* Add country statistics as endpoint, use portId in the port count endpoint instead of unlocode

* add script endpoint to do the initial database migration

* decrease memory footprint of hbr import, only do the hbr import every tuesday

* move the import files to the correct folder

* move the import files to the correct folder, add a manual override option to the area

* remove unused parameter from correct countries, rename correct countries, add better documentation

* fix shadowing variable name, fix constructor call of terminal service

* attempt to fix the finding of the countries file in resources

* attempt 2 to fix the finding of the countries file in resources

* attempt 3 to fix the finding of the countries file in resources

* rename the json var name -> fullname

* alter regions to have multiple ports and countries within it, Added several statistics endpoints, Added countrycode as filter for ports

* remove unneccesary model by generalization

* remove the security bypass

* Add ktlint, move the convert methods to the service classes so its available in the statisticsService, big code style refactor due to ktlint

* another way of defining the ktlint check

* removed unneccesary ktlint block in build.gradle

* change the return type of the port count by country

* ktlint format

* comment fix

* add fallback for country not filled in

* get countrycount rewritten to start from the countries list with mapping

* ktlint pls

* get all non validated ports aswell

* get all non validated ports aswell

* merge


---
id: github:teqplay/portreporter-backend:issue:902
source: github
type: issue
repo: teqplay/portreporter-backend
number: 902
title: Release 4.12.0
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/902
labels: []
explicit_links: []
---
# Issue #902: Release 4.12.0

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/902  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [51c1922515c5...51c1922515c5](https://github.com/teqplay/portreporter-backend/compare/51c1922515c5...51c1922515c5)
**Merge commit:** [51c1922515c5](https://github.com/teqplay/portreporter-backend/commit/51c1922515c5)
**Author:** Shravan Shetty
**Reviewers:** 
**Approvers:** 
**Source Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/portreporter-backend/tree/master)
**Closed On:** 2021-06-28T12:34:42.383221+00:00
**Status:** MERGED

* update: process portcall finished event
* update: clean up
* bumped version to 4.12.0 snapshot version
* added a seperate constructor for null authorities\_ref because kotlin defaulting does not work with jackson
* next attempt to solve the nullable authority ref issue
* Apply a margin to the portcall search for SmartFleet
* Implement Frontend 'IDashboardColumn' and 'IDashboardColumnAccessor' for the dashboard column configuration
* fix: throw 403 instead of 401, when roles do not match
* added log when emails are sent out
* Make column config tooltip optional



---
id: github:teqplay/portreporter-backend:issue:783
source: github
type: issue
repo: teqplay/portreporter-backend
number: 783
title: Develop
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/783
labels: []
explicit_links: []
---
# Issue #783: Develop

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/783  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [27f0700e1fcf...135a81e35f84](https://github.com/teqplay/portreporter-backend/compare/27f0700e1fcf...135a81e35f84)
**Merge commit:** [135a81e35f84](https://github.com/teqplay/portreporter-backend/commit/135a81e35f84)
**Author:** Shravan Shetty
**Reviewers:** 
**Approvers:** Shravan Shetty
**Source Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/portreporter-backend/tree/master)
**Closed On:** 2020-07-06T13:54:09.743468+00:00
**Status:** MERGED

* remove unnecessary file
* update: added a base logic layer, and a base controller
* added USHOU to all ports. anchor events similar to SGSIN
* minor clean up
* mapping anchor up event as inbound or outbound for ushou
* update: auth connection a spring service too
* update: moved common login patterns to AuthInterceptor. Used by both platformConnection and portcall\+ connection
* update: proxy from portreporter to portcall\+
* update: review feedback from wouter
* fix: issues with mapping the version in BaseService
* minor swagger fixes
* update: append shipInfo to created Portcall. Also create empty subscription for them
* update: create subscription even if portcall exists
* fix: issue with fetching company while creating portcall
* fix: show subscriptions already existing when creating portcalls
* update: removed unnecessary double check if user has subscription
* update: clean up
* issue with fetching invoice options per company
* fix: do not trim the portcall search pattern
* fix: update invoice email with logged in users email if null
* fix: create empty subscription for ADMIN when creating portcall
* update: portcall restructure clean up. Moved some methods
* update: added controller to fetch all ports linked to a user
* fix: disallow portcall creation for non-admins for SGSIN, USHOU
* fix: replaced preconditoon to unauthorized exception
* fix: throw precondition exception instead of auth
* portcall update unit tests
* update: changed mutable ports of companies to immutable
* update: added unit test to check portcall creation for user linked to multiple companies
* update: added potential drop tender message for USHOU



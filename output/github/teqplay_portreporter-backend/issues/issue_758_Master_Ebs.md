---
id: github:teqplay/portreporter-backend:issue:758
source: github
type: issue
repo: teqplay/portreporter-backend
number: 758
title: Master Ebs
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/758
labels: []
explicit_links: []
---
# Issue #758: Master Ebs

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/758  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [55c6b173b7ce...c4bdf434b241](https://github.com/teqplay/portreporter-backend/compare/55c6b173b7ce...c4bdf434b241)
**Merge commit:** [c4bdf434b241](https://github.com/teqplay/portreporter-backend/commit/c4bdf434b241)
**Author:** Shravan Shetty
**Reviewers:** Wouter Naloop
**Approvers:** 
**Source Branch:** [master_ebs](https://github.com/teqplay/portreporter-backend/tree/master_ebs)
**Destination Branch:** [master](https://github.com/teqplay/portreporter-backend/tree/master)
**Closed On:** 2020-04-06T14:01:58.006590+00:00
**Status:** MERGED

* update circle ci scripts
* deploy to beanstalk
* circle-ci: re-enable deployment from any branch
* automatic ssh keys management
* increased log retention to 3months
* duplicate valiable due to conflicts
* removing error page filtering
* removing error page filtering - try2
* removing error page filtering - try3
* removing error page filtering - try4
* removing error page filtering - try5
* throw 401 if token is not found or parseable
* added a custom error controller
* enabled /error redirection
* workaround test 500 from auth
* retry fix 500 error
* logging the error if a token is invalid or expired
* created endpoint to get the times of portcalls
* firstOrNull instead of first
* added a lot of logging
* using the correct eventType field
* changed endpoint name
* Added a proxy endpoint for getting areas from platform
* add portEta and portEtd to timestamps endpoint
* attempt to return error message on auth error
* clean up
* moved the main method inside application class
* removed a log
* removed deprecated shippingLineId and agencyId from userProfile
* added cloudwatch config for seeing memory stuff
* adding papertrail integration
* extend the portcall with maxDraught, owner and flag
* Use new location of key management script
* organized imports
* restrict portcall invoice fetch to a month
* Change subject of pilot ladder messages
* Correcting the pilot ladder messages
* allow branches with master as prefix to production
* bumped version to 2.0.0
* fix: change config elements with array type read as string
* fix: missed config key name update
* fix: aligned css/styling paths in templates
* fix: aligned css/styling paths in templates. try 2
* fix: aligned css/styling paths in templates. try 3
* fix: invoice and sof template styling

    \(cherry picked from commit 573f64e74579b91987f8b62ffb52f4abcc5f177d\)


* bumped version to 2.0.1



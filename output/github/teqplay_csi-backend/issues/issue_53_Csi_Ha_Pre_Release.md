---
id: github:teqplay/csi-backend:issue:53
source: github
type: issue
repo: teqplay/csi-backend
number: 53
title: Csi Ha Pre Release
author: jbugella
state: closed
date: '2025-01-07'
url: https://github.com/teqplay/csi-backend/issues/53
labels: []
explicit_links:
- jira:PRA-324
- jira:PRA-284
---
# Issue #53: Csi Ha Pre Release

**Repo:** teqplay/csi-backend  
**URL:** https://github.com/teqplay/csi-backend/issues/53  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-07  
**Closed:** 2025-01-07  

## Description

**Full diff:** [b1e8abec6e96...7d9642e2ba00](https://github.com/teqplay/csi-backend/compare/b1e8abec6e96...7d9642e2ba00)
**Merge commit:** [7d9642e2ba00](https://github.com/teqplay/csi-backend/commit/7d9642e2ba00)
**Author:** Former user
**Reviewers:** 
**Approvers:** 
**Source Branch:** [CSI-HA-pre-release](https://github.com/teqplay/csi-backend/tree/CSI-HA-pre-release)
**Destination Branch:** [develop](https://github.com/teqplay/csi-backend/tree/develop)
**Closed On:** 2023-03-13T09:33:27.360105+00:00
**Status:** MERGED

* Merged in PRA-324-HA \(pull request #46\)
    CSI HA init

    * HA: init
    * Use different URL
    * Fix :dockerPushImage task
    * Fix :getVersion task
    
    Approved-by: Michel Wilson

* Merged in PRA-284/init-data \(pull request #47\)
    Load data on startup

    * Load data on startup
    * PR Feedback & small cleanup
    
    Approved-by: Michel Wilson

* Merged in PRA-284/cleanup \(pull request #48\)
    Cleanup dead/irrelevant code

    * HA: init
    * Load data on startup
    * PR Feedback & small cleanup
    * Cleanup dead/irrelevant code
    
    Approved-by: Michel Wilson

* Merged in PRA-284/publish \(pull request #49\)
    On update to any ship/characteristics/mapping, publish event

    * HA: init
    * Load data on startup
    * PR Feedback & small cleanup
    * On update to any ship/characteristics/mapping, publish event
    * re-delete import files
    * Up skeleton-plugins
    
    Approved-by: Michel Wilson

* Merged in PRA-284/subscribe \(pull request #50\)
    Subscribe to updates of any ship/characteristics/mapping

    * HA: init
    * Load data on startup
    * PR Feedback & small cleanup
    * Subscribe to updates of any ship/characteristics/mapping
    * fix: unique ephemeral consumer name & store on disk
    * Finalize: RollingUpdate with variable replicas & fill data based on build cache & move UserClaimsServiceImpl
    
    Approved-by: Michel Wilson

* Merged in CSI-HA-pre-release-finalize \(pull request #53\)
    CSI HA pre release finalize

    * Fix :getVersion
    * Upgrade .circleci/config.yml
    * Use build-cache, up Gradle wrapper & use Kotlin version from wrapper
    * Upgrade .circleci/config.yml
    * Up Spring Boot version
    


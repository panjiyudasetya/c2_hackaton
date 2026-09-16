---
id: github:teqplay/portreporter-backend:issue:1395
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1395
title: Release/V5 33 1
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1395
labels: []
explicit_links: []
---
# Issue #1395: Release/V5 33 1

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1395  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [a3518942b177...f10ee0c38387](https://github.com/teqplay/portreporter-backend/compare/a3518942b177...f10ee0c38387)
**Merge commit:** [f10ee0c38387](https://github.com/teqplay/portreporter-backend/commit/f10ee0c38387)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Shan Minh Nguyen
**Approvers:** Shan Minh Nguyen
**Source Branch:** [release/v5_33_1](https://github.com/teqplay/portreporter-backend/tree/release/v5_33_1)
**Destination Branch:** [master](https://github.com/teqplay/portreporter-backend/tree/master)
**Closed On:** 2024-09-23T10:07:20.830451+00:00
**Status:** MERGED

* Merged in feature/setup\_new\_environment \(pull request #778\)
    Feature/setup new environment

    * Added new environment to build via CI
    * Removed timezone as it causes failure of config map settings of cron
    * Updated hostname for the staging environment
    * Removing unused lines from ci config
    
    Approved-by: Joaquin Marquez Bugella

* New snapshot version 5.34.0-SNAPSHOT
* New subversion 5.33.1 to automate network policies creation via circleci scripts.


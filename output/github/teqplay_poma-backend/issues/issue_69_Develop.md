---
id: github:teqplay/poma-backend:issue:69
source: github
type: issue
repo: teqplay/poma-backend
number: 69
title: Develop
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/69
labels: []
explicit_links: []
---
# Issue #69: Develop

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/69  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [a74d8d1529ea...a5a8898c3590](https://github.com/teqplay/poma-backend/compare/a74d8d1529ea...a5a8898c3590)
**Merge commit:** [a5a8898c3590](https://github.com/teqplay/poma-backend/commit/a5a8898c3590)
**Author:** Wouter Naloop
**Reviewers:** 
**Approvers:** 
**Source Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/poma-backend/tree/master)
**Closed On:** 2023-06-22T14:37:38.955568+00:00
**Status:** MERGED

* SPV-1520: Add mainPort to Port model
* SPV-1520: Remove todo that was already done
* SPV-1520: remove defaulting that isn't supposed to be there, but was there for local testing
* SPV-1520: reverse search for biggest ports as this makes sure the biggest port is always the main port, renamed percentage to blowUpFactor and changed its scaling to allow for more than 100% blowup area size and the option to scale down, use the kotlin IllegalArgument instead of the java one
* SPV-1520: ktlint
* SPV-1560: Rename Region to Custom Area
* SPV-1562: add the nm areas as hardcoded non generic areas to make it easier to set a standard for the other applications. If I made it generic, you don't know what you will get neccesarily
* SPV-1560: ktlint pls
* Added shell script to sync the poma production database to develop
* SPV-1534: upgrade skeleton and change konfig to configuration properties
* SPV-1534: ktlint
* SPV-1534: tell spring to search for properties
* Add the modeltype for customarea, Change the unique index of ports to a normal index. it didn't make sense, make the ports nullable so the FE can leave them out


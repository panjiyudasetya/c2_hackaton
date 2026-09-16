---
id: github:teqplay/vesselvoyage-backend:issue:158
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 158
title: Spv-1191 Remove Konfig
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/158
labels: []
explicit_links:
- jira:SPV-1191
---
# Issue #158: Spv-1191 Remove Konfig

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/158  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [7d9dacee952e...7b28e76500b1](https://github.com/teqplay/vesselvoyage-backend/compare/7d9dacee952e...7b28e76500b1)
**Merge commit:** [7b28e76500b1](https://github.com/teqplay/vesselvoyage-backend/commit/7b28e76500b1)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [SPV-1191-remove-konfig](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1191-remove-konfig)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-01-30T13:36:02.567443+00:00
**Status:** MERGED

* Removed konfig library
* Changed all places in the application that use konfig to instead use configuration properties to get their config
* Adjusted existing configuration to match naming convention of spring
* Removed old konfig class and related imports
* Changed event filter so it actually works
* Adjusted tests to work with configuration changes
* Corrected incorrectly set duration


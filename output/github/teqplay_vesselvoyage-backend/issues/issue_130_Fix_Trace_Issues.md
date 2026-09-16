---
id: github:teqplay/vesselvoyage-backend:issue:130
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 130
title: Fix/Trace Issues
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/130
labels: []
explicit_links: []
---
# Issue #130: Fix/Trace Issues

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/130  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [5616fdb41a08...3148f115004a](https://github.com/teqplay/vesselvoyage-backend/compare/5616fdb41a08...3148f115004a)
**Merge commit:** [3148f115004a](https://github.com/teqplay/vesselvoyage-backend/commit/3148f115004a)
**Author:** Darius Wattimena
**Reviewers:** Joost Laurman, Wouter Naloop
**Approvers:** Wouter Naloop, Joost Laurman
**Source Branch:** [fix/trace_issues](https://github.com/teqplay/vesselvoyage-backend/tree/fix/trace_issues)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2023-06-23T08:40:29.850658+00:00
**Status:** MERGED

* Fixed an issue where getting the trace of a vessel would result in an exception being thrown
* Fixed an issue where retrieving traces would crash event processing when trying to retrieve traces when no imo mmsi mapping would be returned
* Added tests cases for where event processing could crash


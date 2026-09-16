---
id: github:teqplay/vesselvoyage-backend:issue:118
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 118
title: Hotfix Fast Traces Request
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/118
labels: []
explicit_links: []
---
# Issue #118: Hotfix Fast Traces Request

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/118  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [319e1504ef38...ca15403267fb](https://github.com/teqplay/vesselvoyage-backend/compare/319e1504ef38...ca15403267fb)
**Merge commit:** [ca15403267fb](https://github.com/teqplay/vesselvoyage-backend/commit/ca15403267fb)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop, Gavin den Hollander
**Approvers:** Gavin den Hollander
**Source Branch:** [hotfix_fast_traces_request](https://github.com/teqplay/vesselvoyage-backend/tree/hotfix_fast_traces_request)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2023-03-09T14:23:48.566285+00:00
**Status:** MERGED

* Changed some logic in how the traces are retrieved when requested
* Added the possibility to schedule retrieving of historic traces when they don't exist in the database
* Updated some log levels
* Fixed an issue where the stop combining logic would result in a null pointer
* Replaced tests with new ones
* Changed some logic and changed a test to reflect the intended behaviour


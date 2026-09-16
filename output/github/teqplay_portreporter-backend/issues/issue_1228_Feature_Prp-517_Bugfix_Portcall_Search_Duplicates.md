---
id: github:teqplay/portreporter-backend:issue:1228
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1228
title: Feature/Prp-517 Bugfix Portcall Search Duplicates
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1228
labels: []
explicit_links: []
---
# Issue #1228: Feature/Prp-517 Bugfix Portcall Search Duplicates

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1228  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [0f9f36a6bf46...40096fd77c20](https://github.com/teqplay/portreporter-backend/compare/0f9f36a6bf46...40096fd77c20)
**Merge commit:** [40096fd77c20](https://github.com/teqplay/portreporter-backend/commit/40096fd77c20)
**Author:** Shan Minh Nguyen
**Reviewers:** Wouter Naloop, Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella, Wouter Naloop
**Source Branch:** [feature/PRP-517_bugfix_portcall_search_duplicates](https://github.com/teqplay/portreporter-backend/tree/feature/PRP-517_bugfix_portcall_search_duplicates)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-03-06T10:18:30.717731+00:00
**Status:** MERGED

* Added a distinct to fetching portcalls when searching and receiving duplicates.
* Added unit tests to account for distinct in searching for portcalls.
* Fixed unit tests.


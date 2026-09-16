---
id: github:teqplay/portreporter-backend:issue:798
source: github
type: issue
repo: teqplay/portreporter-backend
number: 798
title: Configurable Official Reporting
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/798
labels: []
explicit_links: []
---
# Issue #798: Configurable Official Reporting

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/798  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [f8ed7c252720...5e5ed7a4334c](https://github.com/teqplay/portreporter-backend/compare/f8ed7c252720...5e5ed7a4334c)
**Merge commit:** [5e5ed7a4334c](https://github.com/teqplay/portreporter-backend/commit/5e5ed7a4334c)
**Author:** Former user
**Reviewers:** Shravan Shetty, Joost Laurman
**Approvers:** Shravan Shetty
**Source Branch:** [official-reporting-configurable](https://github.com/teqplay/portreporter-backend/tree/official-reporting-configurable)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2020-09-09T13:47:20.008974+00:00
**Status:** MERGED

* Support Configurable Official Reporting
* Fix subscription tests

Added a way of making official reporting configurable. There are a bunch of TODOs still, because for some things I have questions/comments and others are just for checking.

Maybe most important question is: how configurable do we want it to be? For now I made it configurable in ‘whole’ hours, e.g. 3 hours, but do we also want to indicate ‘half’ hours or more specifically minutes? So 3.5 hours or 3 hours and 10 minutes, for example.


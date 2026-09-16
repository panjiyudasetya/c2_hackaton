---
id: github:teqplay/portreporter-backend:issue:1171
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1171
title: 'Prp-1320 : Temporal Issue With Column Autosizing Due To Lack Of System Library.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1171
labels: []
explicit_links:
- jira:PRP-1320
---
# Issue #1171: Prp-1320 : Temporal Issue With Column Autosizing Due To Lack Of System Library.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1171  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [7db356c8b15b...ca3620f4ca66](https://github.com/teqplay/portreporter-backend/compare/7db356c8b15b...ca3620f4ca66)
**Merge commit:** [ca3620f4ca66](https://github.com/teqplay/portreporter-backend/commit/ca3620f4ca66)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [fix/PRP-1320/autosizing_issue](https://github.com/teqplay/portreporter-backend/tree/fix/PRP-1320/autosizing_issue)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-10-03T14:40:16.662850+00:00
**Status:** MERGED

As it’s not something fixable by code \(every call to autoSizeColumn will raise an exception\), I’ve commented out  all calls temporally.


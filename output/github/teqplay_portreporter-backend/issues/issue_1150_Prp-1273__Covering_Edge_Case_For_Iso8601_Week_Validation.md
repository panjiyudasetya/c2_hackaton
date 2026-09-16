---
id: github:teqplay/portreporter-backend:issue:1150
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1150
title: 'Prp-1273: Covering Edge Case For Iso8601 Week Validation.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1150
labels: []
explicit_links:
- jira:PRP-1273
---
# Issue #1150: Prp-1273: Covering Edge Case For Iso8601 Week Validation.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1150  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [41b2ff32e4ac...c5321f6c8231](https://github.com/teqplay/portreporter-backend/compare/41b2ff32e4ac...c5321f6c8231)
**Merge commit:** [c5321f6c8231](https://github.com/teqplay/portreporter-backend/commit/c5321f6c8231)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [feat/PRP-1273/edge_case_for_week_validation](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-1273/edge_case_for_week_validation)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-09-01T13:54:11.808559+00:00
**Status:** MERGED

The method `validateWeekFormat()` didn’t cover the edge case `2019-W01` \(which oddly falled into` 2018-W01`\)


---
id: github:teqplay/portreporter-backend:issue:961
source: github
type: issue
repo: teqplay/portreporter-backend
number: 961
title: Prp-7 Review Repetitive Log About Error
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/961
labels: []
explicit_links: []
---
# Issue #961: Prp-7 Review Repetitive Log About Error

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/961  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [b6b2d92ac5df...499fbdb9a20a](https://github.com/teqplay/portreporter-backend/compare/b6b2d92ac5df...499fbdb9a20a)
**Merge commit:** [499fbdb9a20a](https://github.com/teqplay/portreporter-backend/commit/499fbdb9a20a)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Wouter Naloop
**Approvers:** Wouter Naloop, Former user
**Source Branch:** [PRP-7-review-repetitive-log-about-error-](https://github.com/teqplay/portreporter-backend/tree/PRP-7-review-repetitive-log-about-error-)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2021-10-04T08:40:54.613781+00:00
**Status:** MERGED

Avoiding multiple scheduling on the same task.

There’s no unitTest as it’s preventing from a minor exception triggered on a DB task.


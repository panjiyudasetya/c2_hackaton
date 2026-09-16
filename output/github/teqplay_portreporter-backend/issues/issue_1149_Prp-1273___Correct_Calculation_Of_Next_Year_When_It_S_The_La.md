---
id: github:teqplay/portreporter-backend:issue:1149
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1149
title: 'Prp-1273 : Correct Calculation Of Next Year When It''S The Last Week Of The
  Year.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1149
labels: []
explicit_links:
- jira:PRP-1273
---
# Issue #1149: Prp-1273 : Correct Calculation Of Next Year When It'S The Last Week Of The Year.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1149  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [d25e162d9b11...41b2ff32e4ac](https://github.com/teqplay/portreporter-backend/compare/d25e162d9b11...41b2ff32e4ac)
**Merge commit:** [41b2ff32e4ac](https://github.com/teqplay/portreporter-backend/commit/41b2ff32e4ac)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [feat/PRP-1273/correct_calculation_of_next_week](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-1273/correct_calculation_of_next_week)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-09-01T12:37:53.570515+00:00
**Status:** MERGED

Because calculating using time formatters sometimes gives a wrong week in the first weeks of the year \(`2018-12-31` would produce `2018-01`\) even applying the right locale \(iso8601 doesn’t really cover correctly the weeks\), the calculation of the next week must be done in a less elegant way.


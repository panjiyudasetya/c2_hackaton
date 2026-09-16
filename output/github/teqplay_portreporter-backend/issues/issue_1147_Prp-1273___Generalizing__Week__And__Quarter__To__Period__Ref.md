---
id: github:teqplay/portreporter-backend:issue:1147
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1147
title: 'Prp-1273 : Generalizing ''Week'' And ''Quarter'' To ''Period'' Refactoring
  Classes ''Invoiceweeklyinfo'' And ''Invoicequarterinfo'' To ''Invoiceinfobyperiod''
  For The Frontend Convenience.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1147
labels: []
explicit_links: []
---
# Issue #1147: Prp-1273 : Generalizing 'Week' And 'Quarter' To 'Period' Refactoring Classes 'Invoiceweeklyinfo' And 'Invoicequarterinfo' To 'Invoiceinfobyperiod' For The Frontend Convenience.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1147  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [445b40fc72fe...6b2d3084b8a9](https://github.com/teqplay/portreporter-backend/compare/445b40fc72fe...6b2d3084b8a9)
**Merge commit:** [6b2d3084b8a9](https://github.com/teqplay/portreporter-backend/commit/6b2d3084b8a9)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Damon Asberg, Wouter Naloop
**Approvers:** Damon Asberg, Wouter Naloop
**Source Branch:** [feat/PRP-1273/generalizing_weeks_and_quarters_to_periods](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-1273/generalizing_weeks_and_quarters_to_periods)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-08-31T13:21:03.636413+00:00
**Status:** MERGED

It’s just refactoring `InvoiceWeeklyInfo` and `InvoiceQuarterInfo` to `InvoiceInfoByPeriod` to return `period` instead of `week` and `quarter` respectively.


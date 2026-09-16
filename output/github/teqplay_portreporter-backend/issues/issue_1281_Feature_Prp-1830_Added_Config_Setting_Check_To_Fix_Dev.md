---
id: github:teqplay/portreporter-backend:issue:1281
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1281
title: Feature/Prp-1830 Added Config Setting Check To Fix Dev
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1281
labels: []
explicit_links: []
---
# Issue #1281: Feature/Prp-1830 Added Config Setting Check To Fix Dev

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1281  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [9456336c60f8...03029a08502b](https://github.com/teqplay/portreporter-backend/compare/9456336c60f8...03029a08502b)
**Merge commit:** [03029a08502b](https://github.com/teqplay/portreporter-backend/commit/03029a08502b)
**Author:** Shan Minh Nguyen
**Reviewers:** Joost Laurman, Wouter Naloop, Joaquin Marquez Bugella
**Approvers:** Former user
**Source Branch:** [feature/PRP-1830_added_config_setting_check_to_fix_dev](https://github.com/teqplay/portreporter-backend/tree/feature/PRP-1830_added_config_setting_check_to_fix_dev)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-06-05T14:51:03.048679+00:00
**Status:** MERGED

* Made error logging for Exact better by having the iterations configurable.  
  This will only be set on dev as there will only be errors coming out of it whilst live could have errors but this is dependent on the invoice statuses \(unpaid or not\).
* Reset limit  on fetching invoices back to previous.


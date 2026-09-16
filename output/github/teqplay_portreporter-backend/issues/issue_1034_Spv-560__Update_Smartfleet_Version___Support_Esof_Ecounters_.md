---
id: github:teqplay/portreporter-backend:issue:1034
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1034
title: 'Spv-560: Update Smartfleet Version & Support Esof.Ecounters With Nullable
  ''Otherimo'''
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1034
labels: []
explicit_links:
- jira:SPV-560
---
# Issue #1034: Spv-560: Update Smartfleet Version & Support Esof.Ecounters With Nullable 'Otherimo'

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1034  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [7dd226dfc276...88a31ba0e0b9](https://github.com/teqplay/portreporter-backend/compare/7dd226dfc276...88a31ba0e0b9)
**Merge commit:** [88a31ba0e0b9](https://github.com/teqplay/portreporter-backend/commit/88a31ba0e0b9)
**Author:** Former user
**Reviewers:** Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [SPV-560-update-smartfleet-and-portreport](https://github.com/teqplay/portreporter-backend/tree/SPV-560-update-smartfleet-and-portreport)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2024-08-26T07:49:38.772365+00:00
**Status:** MERGED

VesselVoyage had a model change, which made `esof.encounters[].otherImo` nullable

SmartFleet has already been deployed to support this change, only PortReporter left.

Already identified with Damon, there is no frontend dependency for this one.


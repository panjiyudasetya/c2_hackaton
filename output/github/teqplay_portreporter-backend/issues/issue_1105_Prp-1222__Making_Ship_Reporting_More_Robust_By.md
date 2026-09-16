---
id: github:teqplay/portreporter-backend:issue:1105
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1105
title: 'Prp-1222: Making Ship Reporting More Robust By'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1105
labels: []
explicit_links:
- jira:PRP-1222
---
# Issue #1105: Prp-1222: Making Ship Reporting More Robust By

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1105  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [ce3df4a77043...2d9e3a557d4e](https://github.com/teqplay/portreporter-backend/compare/ce3df4a77043...2d9e3a557d4e)
**Merge commit:** [2d9e3a557d4e](https://github.com/teqplay/portreporter-backend/commit/2d9e3a557d4e)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Michel Wilson
**Approvers:** Joost Laurman
**Source Branch:** [PRP-1222/fix/prevent_ship_reports_from_breaking_due_to_data_model_not_compliant](https://github.com/teqplay/portreporter-backend/tree/PRP-1222/fix/prevent_ship_reports_from_breaking_due_to_data_model_not_compliant)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-06-08T07:29:23.697747+00:00
**Status:** MERGED

Making Ship reporting more robust by:
* Adding additional filters to prevent null values that provoke a DataModelException
* Identifying unmatched ShipReportTypes, which are resolved to UNKNOWN.
* Improving efficiency by not generating reports that no subscriber is interested in.
* Making the process more readable and extensible, preventing from repeating-one-self.


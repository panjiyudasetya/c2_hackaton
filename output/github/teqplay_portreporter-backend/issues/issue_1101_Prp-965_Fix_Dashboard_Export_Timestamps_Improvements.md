---
id: github:teqplay/portreporter-backend:issue:1101
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1101
title: Prp-965/Fix/Dashboard Export Timestamps Improvements
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1101
labels: []
explicit_links:
- jira:PRP-965
---
# Issue #1101: Prp-965/Fix/Dashboard Export Timestamps Improvements

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1101  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [592311552231...ffd240f3a00a](https://github.com/teqplay/portreporter-backend/compare/592311552231...ffd240f3a00a)
**Merge commit:** [ffd240f3a00a](https://github.com/teqplay/portreporter-backend/commit/ffd240f3a00a)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [PRP-965/fix/dashboard_export_timestamps_improvements](https://github.com/teqplay/portreporter-backend/tree/PRP-965/fix/dashboard_export_timestamps_improvements)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-05-27T10:01:49.724761+00:00
**Status:** MERGED

Some improvements in:
* Timestamp formats \(dealing with different incoming formats: long, string with and without milliseconds.
* Applying the timezone set as the endpoint param _timezoneFormat_ instead each particular linked portcall. 
* PortcallAlias data access \(make them accessible filtered by the user view\).
* Array access for PORTCALL type \(from mongo style \(key.key.0.key\) to javascript \(key.key\[0\].key\)
* Export dashboard with correct timestamps for Smartfleet view \(not using the linked portcall, but the voyage’s timestamps\).


---
id: github:teqplay/vesselvoyage-backend:issue:282
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 282
title: Spv-2265 Api Processing Story Endpoint
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/282
labels: []
explicit_links:
- jira:SPV-2265
---
# Issue #282: Spv-2265 Api Processing Story Endpoint

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/282  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [391e0124b4e8...1769334e545e](https://github.com/teqplay/vesselvoyage-backend/compare/391e0124b4e8...1769334e545e)
**Merge commit:** [1769334e545e](https://github.com/teqplay/vesselvoyage-backend/commit/1769334e545e)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Leon Joosse
**Source Branch:** [SPV-2265-api-story-endpoint](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2265-api-story-endpoint)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-24T08:02:44.363072+00:00
**Status:** MERGED

* Adjusted controllers to mostly use int as value instead of string for the imo number
* Extended story controller to include an endpoint that instead of dry-running gets the data from the database
* Fix test having compile issue


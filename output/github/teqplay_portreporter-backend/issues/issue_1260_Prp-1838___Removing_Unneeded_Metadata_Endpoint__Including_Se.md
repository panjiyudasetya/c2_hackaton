---
id: github:teqplay/portreporter-backend:issue:1260
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1260
title: 'Prp-1838 : Removing Unneeded Metadata Endpoint. Including Searchpattern In
  The New Field For Searching. Include The Fleet Field In The Notification Model.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1260
labels: []
explicit_links: []
---
# Issue #1260: Prp-1838 : Removing Unneeded Metadata Endpoint. Including Searchpattern In The New Field For Searching. Include The Fleet Field In The Notification Model.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1260  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [76738597d1df...390c2af99071](https://github.com/teqplay/portreporter-backend/compare/76738597d1df...390c2af99071)
**Merge commit:** [390c2af99071](https://github.com/teqplay/portreporter-backend/commit/390c2af99071)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Wouter Naloop, Shan Minh Nguyen
**Approvers:** Joost Laurman
**Source Branch:** [feat/PRP-1838/include_fleetName_in_notification_when_SFEvent](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-1838/include_fleetName_in_notification_when_SFEvent)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-05-04T15:15:14.895113+00:00
**Status:** MERGED

We need to extend the Notification data model for two purposes in case of SF notifications:
* Display the fleetname.
* Search by fleetname.
For this:
1. Removing unneeded metadata endpoint \(previously introduced in the same Jira card\).
2. Include the fleet field in the Notification model.
3. Include the fleetMinimal in the Notification construction.
4. Including searchPattern in the new field for searching.


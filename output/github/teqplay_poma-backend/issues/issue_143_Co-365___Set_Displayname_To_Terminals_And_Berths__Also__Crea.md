---
id: github:teqplay/poma-backend:issue:143
source: github
type: issue
repo: teqplay/poma-backend
number: 143
title: 'Co-365 : Set Displayname To Terminals And Berths. Also, Created 3 Endpoints
  For Capitalizing Ports, Terminals And Berths''S Displaynames.'
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/143
labels: []
explicit_links: []
---
# Issue #143: Co-365 : Set Displayname To Terminals And Berths. Also, Created 3 Endpoints For Capitalizing Ports, Terminals And Berths'S Displaynames.

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/143  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [f56da46b32b8...188ecafb9d00](https://github.com/teqplay/poma-backend/compare/f56da46b32b8...188ecafb9d00)
**Merge commit:** [188ecafb9d00](https://github.com/teqplay/poma-backend/commit/188ecafb9d00)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Wouter Naloop, Pim van den Toorn, Maryam Tavakoli
**Approvers:** Pim van den Toorn
**Source Branch:** [feat/CO-365/add_displayName_to_terminal_and_berths](https://github.com/teqplay/poma-backend/tree/feat/CO-365/add_displayName_to_terminal_and_berths)
**Destination Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Closed On:** 2024-08-21T08:44:40.222832+00:00
**Status:** MERGED

Adding a `displayName` field to the Terminal and Berth models, similar to the existing Port's one.
Additionally, I’ve added a 3 admin endpoints to capitalize them when there’s a discrepancy \(i.e. the live merged database has some port’s displayNames all in uppercase\).
As a remark, these endpoints are asynchronous, as we don’t need to wait for them to finish and, in order not to overload poma \(it’s over a `datasource.getAll()`\) , the update is done sequentially.
Also note that I’ve added a default empty string value for them in the base models, so the db deserialization don’t raise any issues when the fields are not yet populated.


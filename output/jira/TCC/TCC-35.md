---
id: jira:TCC-35
source: jira
type: issue
key: TCC-35
project: TCC
board: TCC board
issuetype: Story
priority: Medium
assignee: Unassigned
labels: []
components: []
title: Add filter option to only return chronological datapoints for ship history
  endpoints
author: Damon Asberg
status: To Do
date: '2025-03-25'
url: https://teqplaybv.atlassian.net/browse/TCC-35
explicit_links:
- jira:IT-207
- jira:TCC-153
---
# [TCC-35] Add filter option to only return chronological datapoints for ship history endpoints

**URL:** https://teqplaybv.atlassian.net/browse/TCC-35  
**Type:** Story | **Status:** To Do | **Priority:** Medium  
**Reporter:** Damon Asberg | **Assignee:** Unassigned  
**Created:** 2025-03-25 | **Updated:** 2025-06-18  
**Board:** TCC board  
**Parent:** [TCC-153] Tech Debt  

## Description

All {{AISHistoricMessage}}’s have a {{historic}} field. If this is true, this means it has not been received in chronological order.

In the “old” timeline, there is a toggle which listens to this field (when it was still called {{streamingIsNewUpdate}}.) In the new Timeline, we now added that this filter is applied right after fetching, but why should it not be passed to the backend to do this filtering for us?

We will also need this option to ensure snapshot creation is correct and matches what the frontend is showing us.



----

DoD:

Add optional parameter to ShipHistory so we can filter on the {{historic}} field. We can only filter after retrieving the data from the database/s3.

## Linked issues

- blocks: [IT-207] Filter out any AIS message where historic=true by default for snapshots

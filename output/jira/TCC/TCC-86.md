---
id: jira:TCC-86
source: jira
type: issue
key: TCC-86
project: TCC
board: TCC board
issuetype: Bug
priority: Medium
assignee: Unassigned
labels: []
components: []
title: Fix an issue where we sometimes miss area end events
author: Darius Wattimena
status: To Do
date: '2025-02-24'
url: https://teqplaybv.atlassian.net/browse/TCC-86
explicit_links:
- jira:SPV-2545
---
# [TCC-86] Fix an issue where we sometimes miss area end events

**URL:** https://teqplaybv.atlassian.net/browse/TCC-86  
**Type:** Bug | **Status:** To Do | **Priority:** Medium  
**Reporter:** Darius Wattimena | **Assignee:** Unassigned  
**Created:** 2025-02-24 | **Updated:** 2025-05-22  
**Board:** TCC board  

## Description

[https://vesselvoyagedev.teqplay.nl/#/ships/9315953/story/080bffce-e2fd-4cf1-aa2f-956e043b9e7d.VISIT?mode=period&months=3|https://vesselvoyagedev.teqplay.nl/#/ships/9315953/story/080bffce-e2fd-4cf1-aa2f-956e043b9e7d.VISIT?mode=period&months=3|smart-link]  missed EOSP end event which should’ve happened on the 2025-01-05.

Interesting to note:

* Event doesn’t exist in EventHistory.
* Event was missed on real-time processing.

## Linked issues

- relates to: [SPV-2545] Fix an issue where a visit is not ended when a EOSP event is missed

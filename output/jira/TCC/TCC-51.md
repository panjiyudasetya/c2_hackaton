---
id: jira:TCC-51
source: jira
type: issue
key: TCC-51
project: TCC
board: TCC board
issuetype: Story
priority: Medium
assignee: Joost Dambrink
labels: []
components: []
title: Routescout route calculation weight improvements
author: Joost Dambrink
status: To Do
date: '2025-03-12'
url: https://teqplaybv.atlassian.net/browse/TCC-51
explicit_links:
- jira:TCC-67
- jira:TCC-68
- jira:TCC-69
---
# [TCC-51] Routescout route calculation weight improvements

**URL:** https://teqplaybv.atlassian.net/browse/TCC-51  
**Type:** Story | **Status:** To Do | **Priority:** Medium  
**Reporter:** Joost Dambrink | **Assignee:** Joost Dambrink  
**Created:** 2025-03-12 | **Updated:** 2025-05-26  
**Board:** TCC board  

## Description

When a vessel does not fit a bridge or lock, we’re currently heavily increasing the weight (infinity) of that route to make it less favourable. However, this has some side-effects when a vessel is close to such an edge it will snap to that edge and only produce invalid routes, whereas there might be a route right next to it that does have allowed dimensions of that vessel. Solution direction might be to calculate multiple routes if there is more than 1 line the startpoint could snap to. 

Example case: lock of terneuzen, where the middle lock was still not opened, but the reverse geocoded locations all ended up on that edge. Now that edge has been removed. 

## Subtasks

- [TCC-67] Investigate the route calculation alogrithm and what impact our costum weight have on it (To Do)
- [TCC-68] Write unit-tests for routing algorithm (To Do)
- [TCC-69] Improve routing algorithm (To Do)

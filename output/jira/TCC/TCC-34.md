---
id: jira:TCC-34
source: jira
type: issue
key: TCC-34
project: TCC
board: TCC board
issuetype: Story
priority: Medium
assignee: Unassigned
labels: []
components: []
title: RouteScout improve the routes starting and ending from geocoded locations
author: Joost Laurman
status: To Do
date: '2025-03-10'
url: https://teqplaybv.atlassian.net/browse/TCC-34
explicit_links: []
---
# [TCC-34] RouteScout improve the routes starting and ending from geocoded locations

**URL:** https://teqplaybv.atlassian.net/browse/TCC-34  
**Type:** Story | **Status:** To Do | **Priority:** Medium  
**Reporter:** Joost Laurman | **Assignee:** Unassigned  
**Created:** 2025-03-10 | **Updated:** 2025-05-22  
**Board:** TCC board  

## Description

When routes are starting from geocoded locations it picks the location closest to the geocoded location. If this is a location where the ship can’t sail, it won’t look further for any alternative routes, it just returns one which is unsailable.

Example route:

Bethune, France → Oosterhout, Netherlands

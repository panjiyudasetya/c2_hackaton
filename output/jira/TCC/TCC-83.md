---
id: jira:TCC-83
source: jira
type: issue
key: TCC-83
project: TCC
board: TCC board
issuetype: Bug
priority: Medium
assignee: Unassigned
labels: []
components: []
title: Event history composed events buggy in timeline
author: Gavin den Hollander
status: To Do
date: '2024-10-21'
url: https://teqplaybv.atlassian.net/browse/TCC-83
explicit_links: []
---
# [TCC-83] Event history composed events buggy in timeline

**URL:** https://teqplaybv.atlassian.net/browse/TCC-83  
**Type:** Bug | **Status:** To Do | **Priority:** Medium  
**Reporter:** Gavin den Hollander | **Assignee:** Unassigned  
**Created:** 2024-10-21 | **Updated:** 2025-05-22  
**Board:** TCC board  

## Description

The composed events in timeline appear to be buggy, according to Damon this is because the data is not matched as expected by the backend. The result of this is that the timeline in the old timeline can not be trusted.

Since we use the tool for validating quite some of our systems it might be worth it to spend some time on this. 

example: [https://timeline.teqplay.nl/316011550?from=1675977006000&to=1676319876798&timezone=UTC&URL=https%3A%2F%2Finternalapi.teqplay.dev%2Fv0&selectedTime=1676148224852|https://timeline.teqplay.nl/316011550?from=1675977006000&to=1676319876798&timezone=UTC&URL=https%3A%2F%2Finternalapi.teqplay.dev%2Fv0&selectedTime=1676148224852|smart-link]  

The tug events in this example ar really strange.

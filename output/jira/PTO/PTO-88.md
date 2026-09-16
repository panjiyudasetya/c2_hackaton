---
id: jira:PTO-88
source: jira
type: issue
key: PTO-88
project: PTO
board: PTO board
issuetype: Task
priority: Medium
assignee: Maryam Tavakoli
labels: []
components: []
title: Increase robustness on 'https://backendpomasandbox.teqplay.nl/v1/all/mergedatabases'
  call
author: Richard van Klaveren
status: Done
date: '2023-10-01'
url: https://teqplaybv.atlassian.net/browse/PTO-88
explicit_links: []
---
# [PTO-88] Increase robustness on 'https://backendpomasandbox.teqplay.nl/v1/all/mergedatabases' call

**URL:** https://teqplaybv.atlassian.net/browse/PTO-88  
**Type:** Task | **Status:** Done | **Priority:** Medium  
**Reporter:** Richard van Klaveren | **Assignee:** Maryam Tavakoli  
**Created:** 2023-10-01 | **Updated:** 2023-10-26  
**Board:** PTO board  

## Description

The call has been resulting too often in a 500, which is fully blocking generation of reports based on new data

→ Unit test to be developed
--> weekly task to report when it goes wrong in the weekly world of ports update

Timebox: 4hr

## Comments

### Maryam Tavakoli — 2023-10-16

I added a weekly task and monitoring logs, also configured in slack in world-of-port-monitoring channel.

### Richard van Klaveren — 2023-10-16

Maryam will notify when this can be 'tested'

### Richard van Klaveren — 2023-10-26

Have not seen instability anymore since, so moving to done

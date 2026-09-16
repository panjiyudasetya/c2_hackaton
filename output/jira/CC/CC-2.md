---
id: jira:CC-2
source: jira
type: issue
key: CC-2
project: CC
board: CC board
issuetype: Story
priority: Medium
assignee: Pim van den Toorn
labels: []
components: []
title: Add support to fully sync the poma database from A to B
author: Darius Wattimena
status: Done
date: '2024-07-18'
url: https://teqplaybv.atlassian.net/browse/CC-2
explicit_links:
- jira:CC-1
---
# [CC-2] Add support to fully sync the poma database from A to B

**URL:** https://teqplaybv.atlassian.net/browse/CC-2  
**Type:** Story | **Status:** Done | **Priority:** Medium  
**Reporter:** Darius Wattimena | **Assignee:** Pim van den Toorn  
**Created:** 2024-07-18 | **Updated:** 2024-10-28  
**Board:** CC board  
**Parent:** [CC-1] Poma Syncing  

## Description

_No description._

## Comments

### Richard van Klaveren — 2024-10-28

[~accountid:63e224de8978d7a4353c94ca] Can you enlighten me on the endpoints relevant here?

### Pim van den Toorn — 2024-10-28

[~accountid:557058:0ffdaf08-199c-4b89-afe7-ac0306e26b29] The endpoints are:

/v1/sync/{source}?synchronize=false

/v1/sync/{source}/{infrastructureType}?synchronize=false

/v1/sync/{source}/ports?ports=NLRTM,BEANR&synchronize=false 

Where 

source = PROD/DEV/SANDBOX 

infrastructureType = ANCHORAGE/PORT/TERMINAL/etc.

ports = unlocodes

synchronize = false to just show the differences, true to also actually synchronize

### Richard van Klaveren — 2024-10-28

Tested [{color:#ffffff}https://backendpomadev.teqplay.nl/v1/sync/PROD?synchronize=false{color}|https://backendpomadev.teqplay.nl/v1/sync/PROD&synchronize=false]

Seems to work properly :-)


[{color:#ffffff}https://backendpomadev.teqplay.nl/v1/sync/PROD/TERMINAL&synchronize=false{color}|https://backendpomadev.teqplay.nl/v1/sync/PROD/TERMINAL&synchronize=false]

Seems to work properly :-)



[{color:#ffffff}https://backendpomadev.teqplay.nl/v1/sync/PROD/ports?synchronize=false{color}|https://backendpomadev.teqplay.nl/v1/sync/PROD/ports?ports=NLRTM,BEANR&synchronize=false]{color:#ffffff} works{color}

works properly, when doing ‘[https://backendpomadev.teqplay.nl/v1/sync/PROD/ports?ports=SGJUR&synchronize=true|https://backendpomadev.teqplay.nl/v1/sync/PROD/ports?ports=SGJUR&synchronize=true]’ it fails since not yet deployed to live

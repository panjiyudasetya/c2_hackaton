---
id: jira:TCC-90
source: jira
type: issue
key: TCC-90
project: TCC
board: TCC board
issuetype: Bug
priority: Medium
assignee: Pim van den Toorn
labels: []
components: []
title: ShipHistory returning only part of the world when taking a view larger than
  the whole world
author: Richard van Klaveren
status: Done
date: '2025-01-20'
url: https://teqplaybv.atlassian.net/browse/TCC-90
explicit_links: []
---
# [TCC-90] ShipHistory returning only part of the world when taking a view larger than the whole world

**URL:** https://teqplaybv.atlassian.net/browse/TCC-90  
**Type:** Bug | **Status:** Done | **Priority:** Medium  
**Reporter:** Richard van Klaveren | **Assignee:** Pim van den Toorn  
**Created:** 2025-01-20 | **Updated:** 2025-05-26  
**Board:** TCC board  

## Description

ShipHistory seems to make a mistake when the range requested goes beyond the -180 to +180 range. 

Request:

{noformat}
https://api.teqplay.nl/v0/ship?topLeftLat=86.57422361983717&topLeftLon=-270.35156250000006&bottomRightLat=-75.93088543216642&bottomRightLon=333.63281250000006{noformat}

Result:



!image-20250120-075352.png|width=1368,height=726,alt="image-20250120-075352.png"!



83k ships, whereas there are more than 165k active ships

## Comments

### Pim van den Toorn — 2025-03-25

The actual fix was easy, getting ShipHistory to run locally was a pain

### Pim van den Toorn — 2025-03-26

!image-20250326-091544.png|width=1731,height=1068,alt="image-20250326-091544.png"!

It works, the request is ~14MB and takes about 10 seconds.

If you want the ships drawn on the other maps as well it’s a FE thing

### Richard van Klaveren — 2025-03-31

I see indeed the fixed behaviour, nice!

### Pim van den Toorn — 2025-05-21

Was never fully finished, as one test failed in a suspicious way; this had to do with bucketing stuff which went way too deep, and Darius was on vacation at the time

### Pim van den Toorn — 2025-05-22

Looked at it again and fixed it, will test on monday

### Pim van den Toorn — 2025-05-26

Done and merged with develop

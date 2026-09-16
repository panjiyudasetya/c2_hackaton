---
id: jira:PTO-74
source: jira
type: subtask
key: PTO-74
project: PTO
board: PTO board
issuetype: Sub-task
priority: Medium
assignee: Richard van Klaveren
labels: []
components: []
title: Prepare report Tangier
author: Richard van Klaveren
status: Done
date: '2023-10-02'
url: https://teqplaybv.atlassian.net/browse/PTO-74
explicit_links:
- jira:PTO-72
---
# [PTO-74] Prepare report Tangier

**URL:** https://teqplaybv.atlassian.net/browse/PTO-74  
**Type:** Sub-task | **Status:** Done | **Priority:** Medium  
**Reporter:** Richard van Klaveren | **Assignee:** Richard van Klaveren  
**Created:** 2023-10-02 | **Updated:** 2023-10-16  
**Board:** PTO board  
**Parent:** [PTO-72] Address any relevant bugs detected while running APM Reports  

## Description

_No description._

## Comments

### Richard van Klaveren — 2023-10-13

Report generated, issues detected and generated cards for:

MAPTM:

* Could we please update the export to excel year/month to 2022/01 instead of 2022/1 to allow alphanumerical sorting?
* 610f72ae-882a-4920-8db3-b16795e475be.VISIT has negative non berth time inbound
* 610f72ae-882a-4920-8db3-b16795e475be.VISIT has no waiting time outside the port, but has anchor time? --> create a card to check (r)events first
* 610f72ae-882a-4920-8db3-b16795e475be.VISIT has AIS glitch to 3 locations and then back, can we fix somehow? (card is in place, solution there)

[https://timeline.teqplay.nl/636014741?from=1657051980000&to=1657493350000&timezone=UTC&URL=https%3A%2F%2Finternalapidev.teqplay.dev%2Fv0&selectedTime=1657325904649|https://timeline.teqplay.nl/636014741?from=1657051980000&to=1657493350000&timezone=UTC&URL=https%3A%2F%2Finternalapidev.teqplay.dev%2Fv0&selectedTime=1657325904649|smart-link] 

* 0278a1f9-d757-4281-8b9b-fc97c75245a9.VISIT why is 'mmsi' and timeline referring to the current mmsi and not to the mmsi at that moment? --> create a card to fix in pto ETL
* 0278a1f9-d757-4281-8b9b-fc97c75245a9.VISIT vessel is anchored for 3+ hours, why no anchor-down/up detected? --> create a card to check (r)events
* 0278a1f9-d757-4281-8b9b-fc97c75245a9.VISIT negative non berth time inbound, since entering port twice.... how can we fix? --> Create a card: should be 2 port visits, vesselvoyage issue?
* 0278a1f9-d757-4281-8b9b-fc97c75245a9.VISIT has for second visit at least 18 hours of waiting time outside the port, only 5 hours are captured --> create slow steaming card

[https://timeline.teqplay.nl/256677000?from=1645490580000&to=1645863960000&timezone=UTC&URL=https%3A%2F%2Finternalapidev.teqplay.dev%2Fv0&selectedTime=1645678641249|https://timeline.teqplay.nl/256677000?from=1645490580000&to=1645863960000&timezone=UTC&URL=https%3A%2F%2Finternalapidev.teqplay.dev%2Fv0&selectedTime=1645678641249|smart-link] 

* 786f336d-de1b-4822-a1e7-c002a43de711.VISIT again wrong mmsi for imo at that time in timeline url and mmsi 
* 786f336d-de1b-4822-a1e7-c002a43de711.VISIT vessel at anchor not detected? was anchored for 7 (?) hours --> seems ok, since only 1 update at anchorage
* 786f336d-de1b-4822-a1e7-c002a43de711.VISIT pilot-to-pilot of 0.46 hrs, but time at berth 7.65 hours --> create card to make it aligned

---
id: jira:PTO-73
source: jira
type: subtask
key: PTO-73
project: PTO
board: PTO board
issuetype: Sub-task
priority: Medium
assignee: Richard van Klaveren
labels: []
components: []
title: Prepare report Port Elizabeth
author: Richard van Klaveren
status: Done
date: '2023-10-02'
url: https://teqplaybv.atlassian.net/browse/PTO-73
explicit_links:
- jira:PTO-72
---
# [PTO-73] Prepare report Port Elizabeth

**URL:** https://teqplaybv.atlassian.net/browse/PTO-73  
**Type:** Sub-task | **Status:** Done | **Priority:** Medium  
**Reporter:** Richard van Klaveren | **Assignee:** Richard van Klaveren  
**Created:** 2023-10-02 | **Updated:** 2023-10-16  
**Board:** PTO board  
**Parent:** [PTO-72] Address any relevant bugs detected while running APM Reports  

## Description

_No description._

## Comments

### Richard van Klaveren — 2023-10-13

report created, issues detected (and created cards for):

USNYC:

* 13f521a3-760b-42ea-8a27-25034dd6e700.VISIT - anchor down at 2022-05-01, but only registered at 2022-05-03 ???
* 13f521a3-760b-42ea-8a27-25034dd6e700.VISIT - Why is 'waiting time in port' 385 hours? Vessel was waiting alot outside the port right?

[https://timeline.teqplay.nl/477318700?URL=https%3A%2F%2Fbackendglobal.teqplay.nl&from=1658475300000&to=1660974792000&selectedTime=1660861302139|https://timeline.teqplay.nl/477318700?URL=https%3A%2F%2Fbackendglobal.teqplay.nl&from=1658475300000&to=1660974792000&selectedTime=1660861302139|smart-link] 

* 807afe42-9658-422c-8345-740c69911ee7.VISIT - same here, 385 hours whereas actual anchor time about 600 hours.... (which seem to be reflected again in 'wainting inside port') but the vessel did not wait in port?
* applied to another 7 visits here....
* --> (r)events: increase 2 weeks to a month....?? --> envision Friday!
* --> PTO ETL: Waiting time inside the port: fix that outside does not count as inside
* 9401445a-83b5-4392-b7da-fdf7ab837c7b.VISIT looks like we're open for vessels without any role? shouldn't we exclude them from the report? --> validation part

[https://timeline.teqplay.nl/229945000?from=1658708880000&to=1661412840000&timezone=UTC&URL=https%3A%2F%2Fbackendpronto.teqplay.nl&selectedTime=1659858310832|https://timeline.teqplay.nl/229945000?from=1658708880000&to=1661412840000&timezone=UTC&URL=https%3A%2F%2Fbackendpronto.teqplay.nl&selectedTime=1659858310832|smart-link] 

* 3f5f8ff6-6e61-4494-9b19-4efa831e1195.VISIT seems like pilot on board is completely off, vessel still preparing for a visit of Savannah ?! Resulting in a very high non berth time inbound
--> Create a card PTO ETL side
* d7c34e51-ff35-4e4f-b291-60bb551d863b.VISIT has pilot on board while at anchor? anchor up seems to be quite off
* d7c34e51-ff35-4e4f-b291-60bb551d863b.VISIT second visit is quite off, pilot 30-11, berth 22-12.... there were 6! port visits in between. Super glue?
+--> Create a card on (r)events to check why there was no anchor up: [https://timeline.teqplay.nl/636093143?from=1669815636000&to=1671892900664&timezone=UTC|https://timeline.teqplay.nl/636093143?from=1669815636000&to=1671892900664&timezone=UTC|smart-link] 
* (r)events: create a card on scalability (2.5 years) (garbage collection)
* PTO-ETL --> change the process to generate the report as last step in pto etl, instead of on request.

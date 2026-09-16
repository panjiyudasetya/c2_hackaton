---
id: jira:CC-9
source: jira
type: subtask
key: CC-9
project: CC
board: CC board
issuetype: Subtask
priority: Medium
assignee: Michel Wilson
labels: []
components: []
title: 'Stop sending out pilot events detected with this extra parameter from PortReporter
  Monitor '
author: Richard van Klaveren
status: Done
date: '2024-06-23'
url: https://teqplaybv.atlassian.net/browse/CC-9
explicit_links:
- jira:CC-7
---
# [CC-9] Stop sending out pilot events detected with this extra parameter from PortReporter Monitor 

**URL:** https://teqplaybv.atlassian.net/browse/CC-9  
**Type:** Subtask | **Status:** Done | **Priority:** Medium  
**Reporter:** Richard van Klaveren | **Assignee:** Michel Wilson  
**Created:** 2024-06-23 | **Updated:** 2024-11-06  
**Board:** CC board  
**Parent:** [CC-7] I want to prevent flipflopping pilot events in singapore (onboard /disembarked)  

## Description

_No description._

## Comments

### Richard van Klaveren — 2024-09-05

testing this behaviour, following went great:

[https://portreporterdev.teqplay.nl/portcall/SGSIN93364642409030T|https://portreporterdev.teqplay.nl/portcall/SGSIN93364642409030T|smart-link] 



There are also a couple where I would have expected other behavior with the filtered out data:

* [https://portreporterdev.teqplay.nl/portcall/SGSIN96412352409010T|https://portreporterdev.teqplay.nl/portcall/SGSIN96412352409010T|smart-link]  is missing a pilot going on board at 2-09-2024 14:01 which should not have been filtered out (resulting probably in a strange fallback being generated?) [https://timeline.teqplay.nl/538004914?from=1725244080000&to=1725486608000&URL=https%3A%2F%2Fapi.teqplay.nl%2Fv0&selectedTime=1725278481272&selectedEvent=c8375055-05b8-4bac-b6f8-b6cfd2b0019f|https://timeline.teqplay.nl/538004914?from=1725244080000&to=1725486608000&URL=https%3A%2F%2Fapi.teqplay.nl%2Fv0&selectedTime=1725278481272&selectedEvent=c8375055-05b8-4bac-b6f8-b6cfd2b0019f|smart-link] 
* [https://portreporterdev.teqplay.nl/portcall/SGSIN99280232409030T?fleetId=55267756-08f1-411a-a5fb-c1f5d4623d0d|https://portreporterdev.teqplay.nl/portcall/SGSIN99280232409030T?fleetId=55267756-08f1-411a-a5fb-c1f5d4623d0d|smart-link] is missing a pilot going on board at 03-09-2024 7:43, seems not detected at all, why? [https://timeline.teqplay.nl/636021545?from=1725324480000&to=1725448451000&URL=https%3A%2F%2Fapi.teqplay.nl%2Fv0&selectedTime=1725342179258|https://timeline.teqplay.nl/636021545?from=1725324480000&to=1725448451000&URL=https%3A%2F%2Fapi.teqplay.nl%2Fv0&selectedTime=1725342179258|smart-link] also unclear why there are pilot events at 03-09-2024 09:14 and 03-09-2024 11:08, those are actually those cases that should have been filtered out?!
* [https://portreporterdev.teqplay.nl/portcall/SGSIN94566162409010T?fleetId=55267756-08f1-411a-a5fb-c1f5d4623d0d|https://portreporterdev.teqplay.nl/portcall/SGSIN94566162409010T?fleetId=55267756-08f1-411a-a5fb-c1f5d4623d0d|smart-link]  why is the pilot event at 04-09-2024 8:08 seen as ‘pilot on board’, should be a disembarked just after leaving the anchorage? [https://timeline.teqplay.nl/353874000?from=1725151800000&to=1725437439000&URL=https%3A%2F%2Fapi.teqplay.nl%2Fv0&selectedTime=1725430313141|https://timeline.teqplay.nl/353874000?from=1725151800000&to=1725437439000&URL=https%3A%2F%2Fapi.teqplay.nl%2Fv0&selectedTime=1725430313141|smart-link]

### Richard van Klaveren — 2024-10-28

Let’s timebox to 4 hrs and focus only on item 1 and 3, and move to done after

### Michel Wilson — 2024-11-06

Tested both these cases, and haven’t been able to reproduce it using the events downloaded from event history, so I believe we can move these to done, [~accountid:557058:0ffdaf08-199c-4b89-afe7-ac0306e26b29] ?

### Richard van Klaveren — 2024-11-06

yap, as agreed

---
id: jira:CC-5
source: jira
type: issue
key: CC-5
project: CC
board: CC board
issuetype: Story
priority: Medium
assignee: Pim van den Toorn
labels: []
components: []
title: Add the ability to trace when a synced happened
author: Darius Wattimena
status: Done
date: '2024-07-18'
url: https://teqplaybv.atlassian.net/browse/CC-5
explicit_links:
- jira:CC-1
---
# [CC-5] Add the ability to trace when a synced happened

**URL:** https://teqplaybv.atlassian.net/browse/CC-5  
**Type:** Story | **Status:** Done | **Priority:** Medium  
**Reporter:** Darius Wattimena | **Assignee:** Pim van den Toorn  
**Created:** 2024-07-18 | **Updated:** 2024-10-28  
**Board:** CC board  
**Parent:** [CC-1] Poma Syncing  

## Description

This should include multiple things:

* When did the sync happen
* What got synced (high level, no details). For example all berths, all port of rotterdam entities, etc.
* Who triggered the sync (automated process or done by user x)

## Comments

### Pim van den Toorn — 2024-10-28

Test by performing a sync and checking the mongoDB. There is a sync_log collection with an entry for every sync that happened

### Richard van Klaveren — 2024-10-28

like a charm!

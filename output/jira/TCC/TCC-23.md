---
id: jira:TCC-23
source: jira
type: issue
key: TCC-23
project: TCC
board: TCC board
issuetype: Story
priority: Medium
assignee: Joost Dambrink
labels: []
components: []
title: Increase the speed the stop-monitor can consume the NATS stream
author: Richard van Klaveren
status: Done
date: '2025-04-09'
url: https://teqplaybv.atlassian.net/browse/TCC-23
explicit_links:
- jira:TCC-152
- jira:TCC-170
- jira:TCC-244
- jira:TCC-220
- jira:TCC-169
- jira:TCC-171
- jira:TCC-261
---
# [TCC-23] Increase the speed the stop-monitor can consume the NATS stream

**URL:** https://teqplaybv.atlassian.net/browse/TCC-23  
**Type:** Story | **Status:** Done | **Priority:** Medium  
**Reporter:** Richard van Klaveren | **Assignee:** Joost Dambrink  
**Created:** 2025-04-09 | **Updated:** 2025-07-24  
**Board:** TCC board  
**Parent:** [TCC-152] Production Issues  

## Description

Anytime something happens with NATS, leading to some backlog of items to be processed, all monitors quickly catch-up the missed messages. Except for 1: the stop monitor. When the stop-monitor needs to catch-up for 15 minutes not consuming, it easily takes 45 minutes. Since this is reducing heavily the flexibility, and also makes every ‘small’ incident immediately taking 3 times as long, we want to envision how to update the stop monitor (resources, architecture, scalability ….) to reduce the catch-up time

At the RnD day JoostD already did some nice things with removing the NATS KV dependency from StopMonitor.

## Subtasks

- [TCC-170] Implement changes needed to improve the stop monitor speed (Done)
- [TCC-244] See if restarting the redis cluster makes data be lost (Done)
- [TCC-220] Adjust revents if needed (Done)
- [TCC-169] Envision how to make the stop monitor faster (Done)
- [TCC-171] Check with DevOps what kind of set up we want for the redis server (Done)
- [TCC-261] Set up redis cluster in Production (Done)

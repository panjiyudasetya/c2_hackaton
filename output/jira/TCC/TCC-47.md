---
id: jira:TCC-47
source: jira
type: issue
key: TCC-47
project: TCC
board: TCC board
issuetype: Story
priority: Medium
assignee: Unassigned
labels: []
components: []
title: Improve Spring Boot application testing in AisEngine for both normal and revents
author: Darius Wattimena
status: To Do
date: '2024-10-31'
url: https://teqplaybv.atlassian.net/browse/TCC-47
explicit_links: []
---
# [TCC-47] Improve Spring Boot application testing in AisEngine for both normal and revents

**URL:** https://teqplaybv.atlassian.net/browse/TCC-47  
**Type:** Story | **Status:** To Do | **Priority:** Medium  
**Reporter:** Darius Wattimena | **Assignee:** Unassigned  
**Created:** 2024-10-31 | **Updated:** 2025-05-22  
**Board:** TCC board  

## Description

Almost all apps in AisEngine don’t have any context loading test. This means we will find out very late when something is broken in the normal flow or when running the revents flow.

The different flows:

# The normal flow (without {{revents}} profile)
# The revents flow (with {{revents}} profile)

VesselVoyage already has tests for this, so taking inspiration from there might be nice starting point.

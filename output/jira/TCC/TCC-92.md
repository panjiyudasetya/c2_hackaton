---
id: jira:TCC-92
source: jira
type: issue
key: TCC-92
project: TCC
board: TCC board
issuetype: Bug
priority: Medium
assignee: Unassigned
labels: []
components: []
title: Encounter monitor internal cache is not always synced with NATS kv when NATS
  is unavaialble
author: Joost Dambrink
status: To Do
date: '2025-04-09'
url: https://teqplaybv.atlassian.net/browse/TCC-92
explicit_links: []
---
# [TCC-92] Encounter monitor internal cache is not always synced with NATS kv when NATS is unavaialble

**URL:** https://teqplaybv.atlassian.net/browse/TCC-92  
**Type:** Bug | **Status:** To Do | **Priority:** Medium  
**Reporter:** Joost Dambrink | **Assignee:** Unassigned  
**Created:** 2025-04-09 | **Updated:** 2025-05-22  
**Board:** TCC board  

## Description

Encounter-monitor could not connect to the busy NATS, thus not being able to delete certain values from the KV store. but deleting them from its internal cache. Which leaves a lot of messages in the KV  store which are not updated (removed) anymore because they are not in the cache. Restarted encounter-monitor so it retrieves the whole KV store again and goes every encounter and deletes all of the ongoing (not ongoing) messages that should have been deleted again. This is also what triggered the slow consumer.

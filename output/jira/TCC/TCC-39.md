---
id: jira:TCC-39
source: jira
type: issue
key: TCC-39
project: TCC
board: TCC board
issuetype: Story
priority: Medium
assignee: Unassigned
labels: []
components: []
title: Investigate why route with many locks doesn't return certain route
author: Joost Laurman
status: To Do
date: '2025-03-12'
url: https://teqplaybv.atlassian.net/browse/TCC-39
explicit_links: []
---
# [TCC-39] Investigate why route with many locks doesn't return certain route

**URL:** https://teqplaybv.atlassian.net/browse/TCC-39  
**Type:** Story | **Status:** To Do | **Priority:** Medium  
**Reporter:** Joost Laurman | **Assignee:** Unassigned  
**Created:** 2025-03-12 | **Updated:** 2025-05-22  
**Board:** TCC board  

## Description

This lock seems to be the problem / drop that overflows the buckets. It’s a lock with ID FRXXXVA125LOCKS00821 and name Ecluse n.16 de Campagne

!afbeelding-20250312-131242.png|width=1457,height=1203,alt="afbeelding-20250312-131242.png"!

!afbeelding-20250312-131210.png|width=1590,height=1195,alt="afbeelding-20250312-131210.png"!

---
id: jira:TCC-30
source: jira
type: issue
key: TCC-30
project: TCC
board: TCC board
issuetype: Bug
priority: Medium
assignee: Michel Wilson
labels: []
components: []
title: Fix AIS data is lost some times when restarting ship history
author: Richard van Klaveren
status: Done
date: '2025-01-20'
url: https://teqplaybv.atlassian.net/browse/TCC-30
explicit_links:
- jira:TCC-152
---
# [TCC-30] Fix AIS data is lost some times when restarting ship history

**URL:** https://teqplaybv.atlassian.net/browse/TCC-30  
**Type:** Bug | **Status:** Done | **Priority:** Medium  
**Reporter:** Richard van Klaveren | **Assignee:** Michel Wilson  
**Created:** 2025-01-20 | **Updated:** 2025-07-02  
**Board:** TCC board  
**Parent:** [TCC-152] Production Issues  

## Description

Darius reported he has seen this case happening, and will report to Michel what he has seen happening or how it could be reproduced.



This happens because we use a Thread.interupt.

Fix is making sure we don’t do this.

----

DoD:

When restarting ship history processor it will not throw an exception that it can’t write data to mongo.

## Comments

### Richard van Klaveren — 2025-02-17

Thread.interrupt wrongly applied (see backend meeting slides). Fix is developed, but waiting for sprint boot PR (Darius) to be applied

### Richard van Klaveren — 2025-04-14

Addressed 3/4, only 1 point to go

### Michel Wilson — 2025-06-04

[~accountid:5e37d9154512b80ca4319871] Code is reviewable, but there’s also a PR in skeleton-plugin that needs to be merged for this code to be merged, it currently depends on a snapshot version of skeleton-plugins.

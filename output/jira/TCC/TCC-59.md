---
id: jira:TCC-59
source: jira
type: issue
key: TCC-59
project: TCC
board: TCC board
issuetype: Story
priority: Medium
assignee: Michel Wilson
labels: []
components: []
title: Convert ShipHistory and eventhistory to a real streaming component to prevent
  memory issues and instability
author: Richard van Klaveren
status: Done
date: '2025-03-11'
url: https://teqplaybv.atlassian.net/browse/TCC-59
explicit_links:
- jira:TCC-154
- jira:TCC-3
- jira:TCC-174
- jira:TCC-172
- jira:TCC-173
- jira:TCC-473
- jira:TCC-484
- jira:TCC-471
---
# [TCC-59] Convert ShipHistory and eventhistory to a real streaming component to prevent memory issues and instability

**URL:** https://teqplaybv.atlassian.net/browse/TCC-59  
**Type:** Story | **Status:** Done | **Priority:** Medium  
**Reporter:** Richard van Klaveren | **Assignee:** Michel Wilson  
**Created:** 2025-03-11 | **Updated:** 2025-10-14  
**Board:** TCC board  
**Parent:** [TCC-3] Ship & Event History fully streaming  

## Description

To eventually test this:

Do a side by side comparison between PROD and DEV, here DEV would be running async while PROD would still be running the old sync way.

----

DoD:

* Regression test between DEV and LIVE (V0 endpoints + V1 endpoints)
* Data is still being pushed correctly to MongoDB as before
* Data is still being pushed correctly to S3 as before

## Linked issues

- implements: [TCC-154] Fix issue where ship-history-processer goes OOM when starting up

## Subtasks

- [TCC-174] Create reactive version of ShipStateService to be used in ShipHistory (Done)
- [TCC-172] Replace mongo driver in bucketing with Kotlin Coroutine driver (Done)
- [TCC-173] Replace S3 client with AsyncS3Client (Done)
- [TCC-473] Add retry on S3 network timeout (Done)
- [TCC-484] Fix models not being compatible with Kotlin 1.9 (Done)
- [TCC-471] Deploy ShipHistory and EvenHistory to production (Done)

## Comments

### Darius Wattimena — 2025-05-28

Envision result:

# Replace Mongo driver with Kotlin Coroutine Driver
# Replace S3 with AsyncS3Client
# Create reactive version of ShipStateService to be used in ShipHistory

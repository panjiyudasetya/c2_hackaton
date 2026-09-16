---
id: jira:PTO-86
source: jira
type: subtask
key: PTO-86
project: PTO
board: PTO board
issuetype: Sub-task
priority: Medium
assignee: Maryam Tavakoli
labels: []
components: []
title: Expose the report via an additional endpoint
author: Richard van Klaveren
status: Done
date: '2023-07-28'
url: https://teqplaybv.atlassian.net/browse/PTO-86
explicit_links:
- jira:PTO-84
---
# [PTO-86] Expose the report via an additional endpoint

**URL:** https://teqplaybv.atlassian.net/browse/PTO-86  
**Type:** Sub-task | **Status:** Done | **Priority:** Medium  
**Reporter:** Richard van Klaveren | **Assignee:** Maryam Tavakoli  
**Created:** 2023-07-28 | **Updated:** 2023-11-26  
**Board:** PTO board  
**Parent:** [PTO-84] As a PTO user, I would like to extend the ETL process with a 'detected issues' report, sharing all deficiencies being detected during generation  

## Description

_No description._

## Comments

### Maryam Tavakoli — 2023-11-13

the file will be available via endpoints:

Dev: https://pto-etldev.teqplay.nl/apmt/export/log/excel/{reportId}

Live: https://pto-etl.teqplay.nl/apmt/export/log/excel/{reportId}

### Richard van Klaveren — 2023-11-26

Functionally tested, works like a charm 🙂

One additional suggestion: would be nice to provide mime/type for excel or provide a filename with .xlsx to make storing even easier. But very workable also without 🙂

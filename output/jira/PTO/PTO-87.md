---
id: jira:PTO-87
source: jira
type: subtask
key: PTO-87
project: PTO
board: PTO board
issuetype: Sub-task
priority: Medium
assignee: David Hansson
labels: []
components: []
title: Update the front-end
author: Richard van Klaveren
status: Done
date: '2023-07-28'
url: https://teqplaybv.atlassian.net/browse/PTO-87
explicit_links:
- jira:PTO-84
---
# [PTO-87] Update the front-end

**URL:** https://teqplaybv.atlassian.net/browse/PTO-87  
**Type:** Sub-task | **Status:** Done | **Priority:** Medium  
**Reporter:** Richard van Klaveren | **Assignee:** David Hansson  
**Created:** 2023-07-28 | **Updated:** 2023-12-12  
**Board:** PTO board  
**Parent:** [PTO-84] As a PTO user, I would like to extend the ETL process with a 'detected issues' report, sharing all deficiencies being detected during generation  

## Description

for log report an endpoint is available to download the report:
Dev: [https://pto-etldev.teqplay.nl/apmt/export/log/excel/{reportId}|https://pto-etldev.teqplay.nl/apmt/export/log/excel/%7BreportId%7D]
Live: [https://pto-etl.teqplay.nl/apmt/export/log/excel/{reportId}|https://pto-etl.teqplay.nl/apmt/export/log/excel/%7BreportId%7D]

you can get a reportId from in inspect

!image-20231211-153143.png|width=720,height=208!

## Comments

### David Hansson — 2023-12-12

[~accountid:557058:0ffdaf08-199c-4b89-afe7-ac0306e26b29]  Would be nice if you can test it

*How to test:*

#  Find a completed report (_charter or terminal_)
#  Click on the new green icon
#  Should now be downloaded and automatically open

### Richard van Klaveren — 2023-12-12

works like a charm [~accountid:60dc34047536500070a88ced] !

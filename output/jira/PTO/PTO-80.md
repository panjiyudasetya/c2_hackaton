---
id: jira:PTO-80
source: jira
type: subtask
key: PTO-80
project: PTO
board: PTO board
issuetype: Sub-task
priority: Low
assignee: Maryam Tavakoli
labels: []
components: []
title: Generate charterer view and use the (empty) template via separate endpoint
author: Richard van Klaveren
status: Done
date: '2023-04-16'
url: https://teqplaybv.atlassian.net/browse/PTO-80
explicit_links:
- jira:PTO-78
---
# [PTO-80] Generate charterer view and use the (empty) template via separate endpoint

**URL:** https://teqplaybv.atlassian.net/browse/PTO-80  
**Type:** Sub-task | **Status:** Done | **Priority:** Low  
**Reporter:** Richard van Klaveren | **Assignee:** Maryam Tavakoli  
**Created:** 2023-04-16 | **Updated:** 2024-02-03  
**Board:** PTO board  
**Parent:** [PTO-78] As a PTO user I want to extend current 'terminal' focus in the reports with a 'charterer' report  

## Description

_No description._

## Comments

### Richard van Klaveren — 2023-06-26

Using portVisit and BerthVisit as usual, but extend with inclusion of multiple ports

### Richard van Klaveren — 2023-09-12

[~accountid:63ff18a9896d10ebd470a1b3] How could I test this? What is the endpoint I should call?

### Richard van Klaveren — 2023-09-15

Maryam: for this one all the endpoints are available in [https://pto-etldev.teqplay.nl/swagger-ui/index.html#|https://pto-etldev.teqplay.nl/swagger-ui/index.html#|smart-link] 
but for testing it. I going to talk to David to see if he deployed FE so you can easily test i.

### Richard van Klaveren — 2023-09-22

tested it with a simple report for North Sea Tankers (3 vessels) visiting NLRTM, BEGNE, NLVLI and NLTNZ….


!image-20230922-072732.png|width=1435,height=241!

### Richard van Klaveren — 2023-10-16

Maryam will let me know when I can test it again

### Richard van Klaveren — 2023-10-30

template will need some updates

### Richard van Klaveren — 2024-02-03

not testing, since currently not in scope, moving to done to clean-up.

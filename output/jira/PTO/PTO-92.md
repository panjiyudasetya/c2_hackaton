---
id: jira:PTO-92
source: jira
type: subtask
key: PTO-92
project: PTO
board: PTO board
issuetype: Sub-task
priority: Medium
assignee: Maryam Tavakoli
labels: []
components: []
title: Envision how to collect this information
author: Richard van Klaveren
status: Done
date: '2023-09-03'
url: https://teqplaybv.atlassian.net/browse/PTO-92
explicit_links:
- jira:PTO-90
---
# [PTO-92] Envision how to collect this information

**URL:** https://teqplaybv.atlassian.net/browse/PTO-92  
**Type:** Sub-task | **Status:** Done | **Priority:** Medium  
**Reporter:** Richard van Klaveren | **Assignee:** Maryam Tavakoli  
**Created:** 2023-09-03 | **Updated:** 2023-10-16  
**Board:** PTO board  
**Parent:** [PTO-90] As a APMT PTO user I want to have an initial mapping of container shippinglines available to compare shippinglines performance  

## Description

_No description._

## Comments

### Richard van Klaveren — 2023-09-12

moving this card to testing…. had the envisioning yesterday. In short, the outcomes:

* Will not focus on completeness at all
* Focus on being able to run the mapping (based on csv inputs and name matching) in Kotlin on any set of IMO’s
** Apply this function to any PTO ETL run with the relevant IMO’s and put the matching shipping lines in the data warehouse / data mart / excel output
** Apply this function to all IMO’s in CSI with categories v2 ‘container' to get a way to monitor coverage

Further extension of coverage will only become a topic when APMT will ask for this

[~accountid:63ff18a9896d10ebd470a1b3] could you please validate above is a proper summary of the meeting and move the card to done if so?

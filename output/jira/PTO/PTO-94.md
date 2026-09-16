---
id: jira:PTO-94
source: jira
type: subtask
key: PTO-94
project: PTO
board: PTO board
issuetype: Sub-task
priority: Medium
assignee: Maryam Tavakoli
labels: []
components: []
title: Make process in ETL to 'collect' shippingline information
author: Richard van Klaveren
status: Done
date: '2023-09-03'
url: https://teqplaybv.atlassian.net/browse/PTO-94
explicit_links:
- jira:PTO-90
---
# [PTO-94] Make process in ETL to 'collect' shippingline information

**URL:** https://teqplaybv.atlassian.net/browse/PTO-94  
**Type:** Sub-task | **Status:** Done | **Priority:** Medium  
**Reporter:** Richard van Klaveren | **Assignee:** Maryam Tavakoli  
**Created:** 2023-09-03 | **Updated:** 2023-10-16  
**Board:** PTO board  
**Parent:** [PTO-90] As a APMT PTO user I want to have an initial mapping of container shippinglines available to compare shippinglines performance  

## Description

Using just the sources we used during the experiment being:

* Avaliable static sheets with imo’s and shipping lines
* Name matching

The result should be available for 2 purposes: 

# generating inputs for the ETL process shippingline
# Calculating the coverage of shipping line per vessel

## Comments

### Richard van Klaveren — 2023-10-09

there is no shippingline information in latest exports? how can I test?

### Richard van Klaveren — 2023-10-13

Noticed the relevant shippingline info is in the database, and applied in the excel export

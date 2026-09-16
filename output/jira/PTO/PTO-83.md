---
id: jira:PTO-83
source: jira
type: issue
key: PTO-83
project: PTO
board: PTO board
issuetype: Task
priority: High
assignee: Wouter Naloop
labels: []
components: []
title: As a datamart+excel user i want to see if a berthvisit was for cargo operation
  or for waiting, and want to reflect that in the port visits by including waitingTimeBerths
author: Wouter Naloop
status: Done
date: '2023-09-19'
url: https://teqplaybv.atlassian.net/browse/PTO-83
explicit_links: []
---
# [PTO-83] As a datamart+excel user i want to see if a berthvisit was for cargo operation or for waiting, and want to reflect that in the port visits by including waitingTimeBerths

**URL:** https://teqplaybv.atlassian.net/browse/PTO-83  
**Type:** Task | **Status:** Done | **Priority:** High  
**Reporter:** Wouter Naloop | **Assignee:** Wouter Naloop  
**Created:** 2023-09-19 | **Updated:** 2023-10-30  
**Board:** PTO board  

## Description

* Add cargoOperation Boolean to the datamart model and fill it on generation based on the berth catergory types and the ship type
* count these berths marked as cargoOperation as CargoDurationBerths
* count the berths markes as none cargoOperations as WaitingDurationBerths

---
id: jira:TCC-84
source: jira
type: issue
key: TCC-84
project: TCC
board: TCC board
issuetype: Bug
priority: Medium
assignee: Unassigned
labels: []
components: []
title: CSI - Ship search column order doesn't work in a few cases
author: Francisco Jose Muros Muriano
status: To Do
date: '2024-10-31'
url: https://teqplaybv.atlassian.net/browse/TCC-84
explicit_links:
- jira:TCC-152
---
# [TCC-84] CSI - Ship search column order doesn't work in a few cases

**URL:** https://teqplaybv.atlassian.net/browse/TCC-84  
**Type:** Bug | **Status:** To Do | **Priority:** Medium  
**Reporter:** Francisco Jose Muros Muriano | **Assignee:** Unassigned  
**Created:** 2024-10-31 | **Updated:** 2025-08-08  
**Board:** TCC board  
**Parent:** [TCC-152] Production Issues  

## Description

There is a few cases where the order by columns are not working in the Ship search screen:

* Ordering by name, we show a few ships before receiving the ships that starts by Z
!image-20241031-095652.png|width=762,height=520,alt="image-20241031-095652.png"!



* Ordering by ENI, if we order by this column, we get empty results in both ways
* Ordering by any column value when the search field is filled with any character
!image-20241031-100150.png|width=1527,height=480,alt="image-20241031-100150.png"!

Probably a backend issue? Frontend could be sending the wrong parameter

----

DoD:

The backend returns the data correctly sorted.

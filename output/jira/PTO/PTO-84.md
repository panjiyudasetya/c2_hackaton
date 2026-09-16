---
id: jira:PTO-84
source: jira
type: issue
key: PTO-84
project: PTO
board: PTO board
issuetype: Story
priority: Medium
assignee: Unassigned
labels: []
components: []
title: As a PTO user, I would like to extend the ETL process with a 'detected issues'
  report, sharing all deficiencies being detected during generation
author: Richard van Klaveren
status: Done
date: '2023-07-28'
url: https://teqplaybv.atlassian.net/browse/PTO-84
explicit_links:
- jira:PTO-85
- jira:PTO-86
- jira:PTO-87
---
# [PTO-84] As a PTO user, I would like to extend the ETL process with a 'detected issues' report, sharing all deficiencies being detected during generation

**URL:** https://teqplaybv.atlassian.net/browse/PTO-84  
**Type:** Story | **Status:** Done | **Priority:** Medium  
**Reporter:** Richard van Klaveren | **Assignee:** Unassigned  
**Created:** 2023-07-28 | **Updated:** 2024-01-08  
**Board:** PTO board  

## Description

Currently we do have a smooth process running to generate Excel reports for PTO.  Issues detected during the process are ‘swallowed’, and although available in the logs not pro-actively shared. Would like to have a report (next to, or in the Excel Spreadsheet) holding all  detected issues like:

* no DWT or length available for a vessel
* Vessel V2 type missing
* non-matching events detected (e.g. Anchor down without an anchor-up)

## Subtasks

- [PTO-85] Write the bug-reports into S3 and store ref in run (Done)
- [PTO-86] Expose the report via an additional endpoint (Done)
- [PTO-87] Update the front-end (Done)

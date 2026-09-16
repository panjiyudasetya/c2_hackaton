---
id: github:teqplay/vesselvoyage-backend:issue:156
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 156
title: Pto-441 Better Stop Detection Revents
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/156
labels: []
explicit_links:
- jira:PTO-441
---
# Issue #156: Pto-441 Better Stop Detection Revents

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/156  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [3c5923aaaf0a...e4d4889470cf](https://github.com/teqplay/vesselvoyage-backend/compare/3c5923aaaf0a...e4d4889470cf)
**Merge commit:** [e4d4889470cf](https://github.com/teqplay/vesselvoyage-backend/commit/e4d4889470cf)
**Author:** Darius Wattimena
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [PTO-441-better-stop-detection-revents](https://github.com/teqplay/vesselvoyage-backend/tree/PTO-441-better-stop-detection-revents)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-02-16T13:05:02.182775+00:00
**Status:** MERGED

* Added initial code to recalculate the stops in a faster way by asking all traces of the entry in one go
* Adjusted the logic a bit how we determine the timespan of the trace


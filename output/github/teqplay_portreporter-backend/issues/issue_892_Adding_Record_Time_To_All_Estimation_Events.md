---
id: github:teqplay/portreporter-backend:issue:892
source: github
type: issue
repo: teqplay/portreporter-backend
number: 892
title: Adding Record Time To All Estimation Events
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/892
labels: []
explicit_links: []
---
# Issue #892: Adding Record Time To All Estimation Events

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/892  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [e885e7d2b78a...ae7f5e9f2108](https://github.com/teqplay/portreporter-backend/compare/e885e7d2b78a...ae7f5e9f2108)
**Merge commit:** [ae7f5e9f2108](https://github.com/teqplay/portreporter-backend/commit/ae7f5e9f2108)
**Author:** Wouter Naloop
**Reviewers:** Shravan Shetty
**Approvers:** Shravan Shetty, Former user
**Source Branch:** [feat/estimation_recordtime](https://github.com/teqplay/portreporter-backend/tree/feat/estimation_recordtime)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2021-05-18T07:40:13.066028+00:00
**Status:** MERGED

This eta recordtime is added because we want to know the time the last eta is handed out in Portsupport.   
Before this the only option to get that was to look through all events and find the last eta event. And take the recordTime from that


---
id: github:teqplay/portreporter-backend:issue:959
source: github
type: issue
repo: teqplay/portreporter-backend
number: 959
title: 'Columnconfig: Add New Endpoint To Make ''Companyid'' Optional'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/959
labels: []
explicit_links: []
---
# Issue #959: Columnconfig: Add New Endpoint To Make 'Companyid' Optional

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/959  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [574b367d0da0...7534f8f925f2](https://github.com/teqplay/portreporter-backend/compare/574b367d0da0...7534f8f925f2)
**Merge commit:** [7534f8f925f2](https://github.com/teqplay/portreporter-backend/commit/7534f8f925f2)
**Author:** Former user
**Reviewers:** Wouter Naloop, Joaquin Marquez Bugella
**Approvers:** Wouter Naloop
**Source Branch:** [PRP-179-make-companyid-an-optional-reque](https://github.com/teqplay/portreporter-backend/tree/PRP-179-make-companyid-an-optional-reque)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2024-08-26T07:49:39.488897+00:00
**Status:** MERGED

This enables the frontend to be able to send column config GET requests, without requiring the `companyId` to be available.


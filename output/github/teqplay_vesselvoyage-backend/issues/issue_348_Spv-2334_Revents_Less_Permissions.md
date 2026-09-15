---
id: github:teqplay/vesselvoyage-backend:issue:348
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 348
title: Spv-2334 Revents Less Permissions
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/348
labels: []
explicit_links: []
---
# Issue #348: Spv-2334 Revents Less Permissions

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/348  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [c716cbe216e7...6fb9f8817996](https://github.com/teqplay/vesselvoyage-backend/compare/c716cbe216e7...6fb9f8817996)
**Merge commit:** [6fb9f8817996](https://github.com/teqplay/vesselvoyage-backend/commit/6fb9f8817996)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse, Joost Dambrink
**Approvers:** Joost Dambrink
**Source Branch:** [SPV-2334-revents-less-permissions](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2334-revents-less-permissions)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-10-15T12:44:47.344050+00:00
**Status:** MERGED

* Added test cases to ensure permissions are set correctly
* Added a new revents role that only has access to the events controller
* Moved models of events to the internal model package instead
* Add test cases that cover the V2 event controllers as well


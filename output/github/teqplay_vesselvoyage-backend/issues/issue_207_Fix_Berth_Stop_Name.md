---
id: github:teqplay/vesselvoyage-backend:issue:207
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 207
title: Fix Berth Stop Name
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/207
labels: []
explicit_links: []
---
# Issue #207: Fix Berth Stop Name

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/207  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [e1ded53b0dca...147c4c1cfa3f](https://github.com/teqplay/vesselvoyage-backend/compare/e1ded53b0dca...147c4c1cfa3f)
**Merge commit:** [147c4c1cfa3f](https://github.com/teqplay/vesselvoyage-backend/commit/147c4c1cfa3f)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop, Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [fix-berth-stop-name](https://github.com/teqplay/vesselvoyage-backend/tree/fix-berth-stop-name)
**Destination Branch:** [master](https://github.com/teqplay/vesselvoyage-backend/tree/master)
**Closed On:** 2024-04-11T13:31:31.140596+00:00
**Status:** MERGED

* Fix an issue where the bert name long would not be set correctly if the returned value is blank
* Adjusted test to ensure the berth long name isn't used when it is blank


---
id: github:teqplay/portreporter-backend:issue:1135
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1135
title: 'Prp-1320 : Avoid Exceptions By Same Sheet Names When Exporting Backend Usage
  Stats.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1135
labels: []
explicit_links: []
---
# Issue #1135: Prp-1320 : Avoid Exceptions By Same Sheet Names When Exporting Backend Usage Stats.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1135  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [72c56bb4fd65...cd215112359c](https://github.com/teqplay/portreporter-backend/compare/72c56bb4fd65...cd215112359c)
**Merge commit:** [cd215112359c](https://github.com/teqplay/portreporter-backend/commit/cd215112359c)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman
**Approvers:** Former user
**Source Branch:** [fix/PRP-1320/avoid_sheetname_collisions_in_backend_stats_export](https://github.com/teqplay/portreporter-backend/tree/fix/PRP-1320/avoid_sheetname_collisions_in_backend_stats_export)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-08-03T10:43:05.087254+00:00
**Status:** MERGED

Hey guys, this is no feature inclusion, but just a address an external problem and fix an internal one:
* A POI bug with sheet names
* Correct grouping of stats based on companyId and companyName \(I was doing it by name\)
About the first issue, It happens that POI library complains whenever a sheet is attempted to be created when there’s another one with the same name.
Funny thing is that very self POI sheet name validation is wrong \(so the bug is on their side\), even providing different sheet names:
1. it checks for collisions \(sheets with same name\)
2. it truncates to 31 chars!
3. it does some additional checks
4. and finally adds the sheet
You can see if two sheet names share the first 31 chars, the exception is guaranteed.
This fix is to prevent it by adding a prefix in case of collision.


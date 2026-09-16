---
id: github:teqplay/portreporter-backend:issue:1016
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1016
title: Prp-509/Fix/Dont Allow Two Visits In Arrived Statue For Same Portcall
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1016
labels: []
explicit_links: []
---
# Issue #1016: Prp-509/Fix/Dont Allow Two Visits In Arrived Statue For Same Portcall

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1016  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [95b6b9a5ed3a...1296583a0a1c](https://github.com/teqplay/portreporter-backend/compare/95b6b9a5ed3a...1296583a0a1c)
**Merge commit:** [1296583a0a1c](https://github.com/teqplay/portreporter-backend/commit/1296583a0a1c)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Wouter Naloop
**Approvers:** Wouter Naloop, Joost Laurman
**Source Branch:** [PRP-509/fix/Dont_allow_two_visits_in_ARRIVED_statue_for_same_portcall](https://github.com/teqplay/portreporter-backend/tree/PRP-509/fix/Dont_allow_two_visits_in_ARRIVED_statue_for_same_portcall)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2021-12-22T17:12:36.769239+00:00
**Status:** MERGED

* PRP-509: When portcall's visit transitions to ARRIVED triggered by an ATA event, move any of the same portcall's ARRIVED visit to SCHEDULED
* PRP-509 : adapt UnitTests and avoid potential recursive calls on transitVisit\(...\) via postActions



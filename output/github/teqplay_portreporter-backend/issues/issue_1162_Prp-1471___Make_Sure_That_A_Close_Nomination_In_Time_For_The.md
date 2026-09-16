---
id: github:teqplay/portreporter-backend:issue:1162
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1162
title: 'Prp-1471 : Make Sure That A Close Nomination In Time For The Same Vessel,
  Company And Port But A Different'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1162
labels: []
explicit_links:
- jira:PRP-1471
---
# Issue #1162: Prp-1471 : Make Sure That A Close Nomination In Time For The Same Vessel, Company And Port But A Different

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1162  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [b8654c1daa23...560c3cbeb0ad](https://github.com/teqplay/portreporter-backend/compare/b8654c1daa23...560c3cbeb0ad)
**Merge commit:** [560c3cbeb0ad](https://github.com/teqplay/portreporter-backend/commit/560c3cbeb0ad)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Wouter Naloop, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [fix/PRP-1471/nomination_matching_by_reference](https://github.com/teqplay/portreporter-backend/tree/fix/PRP-1471/nomination_matching_by_reference)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-09-21T13:28:44.314376+00:00
**Status:** MERGED

Make sure that a close nomination in time for the same vessel, company and port but a different  
reference produces a new nomination instead of updating it \(by mistake as the eta's timerange is close enough\).


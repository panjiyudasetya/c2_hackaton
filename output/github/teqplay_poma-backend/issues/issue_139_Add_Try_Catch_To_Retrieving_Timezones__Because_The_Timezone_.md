---
id: github:teqplay/poma-backend:issue:139
source: github
type: issue
repo: teqplay/poma-backend
number: 139
title: Add Try Catch To Retrieving Timezones, Because The Timezone Stuff Uses Poma.
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/139
labels: []
explicit_links: []
---
# Issue #139: Add Try Catch To Retrieving Timezones, Because The Timezone Stuff Uses Poma.

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/139  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [fe807190a169...fef0b7e07708](https://github.com/teqplay/poma-backend/compare/fe807190a169...fef0b7e07708)
**Merge commit:** [fef0b7e07708](https://github.com/teqplay/poma-backend/commit/fef0b7e07708)
**Author:** Wouter Naloop
**Reviewers:** Joost Dambrink, Pim van den Toorn
**Approvers:** Pim van den Toorn
**Source Branch:** [fix/timezone-fetch](https://github.com/teqplay/poma-backend/tree/fix/timezone-fetch)
**Destination Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Closed On:** 2024-07-03T11:54:49.057130+00:00
**Status:** MERGED

So when trying to add a poma port it tries to ask for that poma port and gives a 404


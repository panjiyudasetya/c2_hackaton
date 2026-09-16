---
id: github:teqplay/poma-backend:issue:146
source: github
type: issue
repo: teqplay/poma-backend
number: 146
title: Cc-4 Sync Whitelist
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/146
labels: []
explicit_links: []
---
# Issue #146: Cc-4 Sync Whitelist

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/146  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [d23dba8e2c7d...85006b6f38b9](https://github.com/teqplay/poma-backend/compare/d23dba8e2c7d...85006b6f38b9)
**Merge commit:** [85006b6f38b9](https://github.com/teqplay/poma-backend/commit/85006b6f38b9)
**Author:** Pim van den Toorn
**Reviewers:** Darius Wattimena, Joost Dambrink
**Approvers:** Joost Dambrink, Darius Wattimena
**Source Branch:** [CC-4-sync-whitelist](https://github.com/teqplay/poma-backend/tree/CC-4-sync-whitelist)
**Destination Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Closed On:** 2024-08-27T16:18:51.391854+00:00
**Status:** MERGED

These changes include the ones from CC-2 and CC-3, 
compare with that or merge the other PR to compare with develop \(Waiting for Darius' approval\)

* Insert and insertMany are now insert if not exists
* Removed secured from whitelist getAll
* Added synchronizeWhitelist


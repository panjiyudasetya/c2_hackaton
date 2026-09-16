---
id: github:teqplay/poma-backend:issue:48
source: github
type: issue
repo: teqplay/poma-backend
number: 48
title: Pra-463/Hashed Uniqueids
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/48
labels: []
explicit_links: []
---
# Issue #48: Pra-463/Hashed Uniqueids

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/48  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [0abe30a5de59...32461e054a34](https://github.com/teqplay/poma-backend/compare/0abe30a5de59...32461e054a34)
**Merge commit:** [32461e054a34](https://github.com/teqplay/poma-backend/commit/32461e054a34)
**Author:** Wouter Naloop
**Reviewers:** Joost Laurman, Michel Wilson, Darius Wattimena
**Approvers:** Joost Laurman, Former user, Darius Wattimena
**Source Branch:** [PRA-463/hashed_uniqueids](https://github.com/teqplay/poma-backend/tree/PRA-463/hashed_uniqueids)
**Destination Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Closed On:** 2023-01-30T10:49:59.732514+00:00
**Status:** MERGED

* PRA-463: hash the uniqueId, remove the createOrUpdate method which had the possibilty to override \_id if it was given by the frontend
* PRA-463: removed uniqueId to uppercase, because that is not always the case for legacy reasons
* PRA-463: ktlint pls


---
id: github:teqplay/vesselvoyage-backend:issue:126
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 126
title: 'Prp-1896 : Visitvoyage Should Be A Data Class.'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/126
labels: []
explicit_links:
- jira:PRP-1896
---
# Issue #126: Prp-1896 : Visitvoyage Should Be A Data Class.

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/126  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [16e7dcb29fa7...1e8431a11f97](https://github.com/teqplay/vesselvoyage-backend/compare/16e7dcb29fa7...1e8431a11f97)
**Merge commit:** [1e8431a11f97](https://github.com/teqplay/vesselvoyage-backend/commit/1e8431a11f97)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Darius Wattimena
**Approvers:** Former user
**Source Branch:** [feat/PRP-1896/VisitVoyage_should_be_a_data_class](https://github.com/teqplay/vesselvoyage-backend/tree/feat/PRP-1896/VisitVoyage_should_be_a_data_class)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2023-06-12T07:50:05.461124+00:00
**Status:** MERGED

It should be data class, otherwise jackson will build up a `LinkedHashMap` instead.


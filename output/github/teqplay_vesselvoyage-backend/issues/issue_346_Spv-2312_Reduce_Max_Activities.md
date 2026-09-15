---
id: github:teqplay/vesselvoyage-backend:issue:346
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 346
title: Spv-2312 Reduce Max Activities
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/346
labels: []
explicit_links: []
---
# Issue #346: Spv-2312 Reduce Max Activities

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/346  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [d10cd0ec4a4c...b83fbfce9d90](https://github.com/teqplay/vesselvoyage-backend/compare/d10cd0ec4a4c...b83fbfce9d90)
**Merge commit:** [b83fbfce9d90](https://github.com/teqplay/vesselvoyage-backend/commit/b83fbfce9d90)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse, Joost Dambrink
**Approvers:** Joost Dambrink
**Source Branch:** [reduce-max-activities](https://github.com/teqplay/vesselvoyage-backend/tree/reduce-max-activities)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-09-30T08:48:49.179024+00:00
**Status:** MERGED

* Lowered the total amount of activities one field can have
* Adjusted test cases to reflect the expected max of 50
* Make sure to use the same constant for all places where we limit


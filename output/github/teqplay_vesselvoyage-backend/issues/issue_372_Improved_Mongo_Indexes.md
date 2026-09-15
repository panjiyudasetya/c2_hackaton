---
id: github:teqplay/vesselvoyage-backend:issue:372
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 372
title: Improved Mongo Indexes
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/372
labels: []
explicit_links: []
---
# Issue #372: Improved Mongo Indexes

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/372  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [d52de3594cc3...c0c37623957f](https://github.com/teqplay/vesselvoyage-backend/compare/d52de3594cc3...c0c37623957f)
**Merge commit:** [c0c37623957f](https://github.com/teqplay/vesselvoyage-backend/commit/c0c37623957f)
**Author:** Darius Wattimena
**Reviewers:** Michel Wilson, Joost Dambrink
**Approvers:** Michel Wilson
**Source Branch:** [improved-mongo-indexes](https://github.com/teqplay/vesselvoyage-backend/tree/improved-mongo-indexes)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-11-19T16:05:23.317947+00:00
**Status:** MERGED

* Adjusted mongo indexes so they are more stable
* Removed unneeded imo index
* Instead use the time field as otherwise the index doesn't make any sense
* Added back needed index


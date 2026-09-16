---
id: github:teqplay/vesselvoyage-backend:issue:246
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 246
title: Spv-2139 Non Nullable Area Id
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/246
labels: []
explicit_links:
- jira:SPV-2139
---
# Issue #246: Spv-2139 Non Nullable Area Id

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/246  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [8d24131c999b...e9d2a812d6c7](https://github.com/teqplay/vesselvoyage-backend/compare/8d24131c999b...e9d2a812d6c7)
**Merge commit:** [e9d2a812d6c7](https://github.com/teqplay/vesselvoyage-backend/commit/e9d2a812d6c7)
**Author:** Darius Wattimena
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [SPV-2139-non-nullable-area-id](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2139-non-nullable-area-id)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-05-28T13:11:37.328620+00:00
**Status:** MERGED

* Adjusted the code so areaId is always provided as otherwise an AreaActivity can't be made
* Fixed some test utils that allowed null but was never used


---
id: github:teqplay/vesselvoyage-backend:issue:71
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 71
title: Spv-746 Hotfix/Grouping Edge Cases
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/71
labels: []
explicit_links: []
---
# Issue #71: Spv-746 Hotfix/Grouping Edge Cases

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/71  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [90ba9d932bda...641e5a5ebfdc](https://github.com/teqplay/vesselvoyage-backend/compare/90ba9d932bda...641e5a5ebfdc)
**Merge commit:** [641e5a5ebfdc](https://github.com/teqplay/vesselvoyage-backend/commit/641e5a5ebfdc)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [hotfix/grouping-edge-case](https://github.com/teqplay/vesselvoyage-backend/tree/hotfix/grouping-edge-case)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-03-29T13:30:03.315212+00:00
**Status:** MERGED

* Fixed an issue where grouping where the from date is bigger than the to date would throw an exception
* Fixed an extra edge case where the provided mapping would have incorrect values



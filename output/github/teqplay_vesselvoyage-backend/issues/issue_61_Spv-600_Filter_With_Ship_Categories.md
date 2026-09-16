---
id: github:teqplay/vesselvoyage-backend:issue:61
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 61
title: Spv-600 Filter With Ship Categories
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/61
labels: []
explicit_links: []
---
# Issue #61: Spv-600 Filter With Ship Categories

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/61  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [bcbf9ba3cbcd...32d71928d5a0](https://github.com/teqplay/vesselvoyage-backend/compare/bcbf9ba3cbcd...32d71928d5a0)
**Merge commit:** [32d71928d5a0](https://github.com/teqplay/vesselvoyage-backend/commit/32d71928d5a0)
**Author:** Darius Wattimena
**Reviewers:** Jos de Jong
**Approvers:** Jos de Jong
**Source Branch:** [SPV-600_filter-with-ship-categories](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-600_filter-with-ship-categories)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-02-22T10:52:53.955630+00:00
**Status:** MERGED

* Fixed an issue where the require wouldn't trigger when the startTime is higher than the endTime when querying visits
* Fixed an issue where the requires on the voyage data source wouldn't work as intended
* Changed querying for visits and voyages to make use of csi ship categories
* Fixed a missing capital 'M' in a variable name



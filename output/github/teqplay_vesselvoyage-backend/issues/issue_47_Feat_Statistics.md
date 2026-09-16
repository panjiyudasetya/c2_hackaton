---
id: github:teqplay/vesselvoyage-backend:issue:47
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 47
title: Feat/Statistics
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/47
labels: []
explicit_links: []
---
# Issue #47: Feat/Statistics

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/47  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [3c1e6314b4d2...7af2a8683614](https://github.com/teqplay/vesselvoyage-backend/compare/3c1e6314b4d2...7af2a8683614)
**Merge commit:** [7af2a8683614](https://github.com/teqplay/vesselvoyage-backend/commit/7af2a8683614)
**Author:** Jos de Jong
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena, Former user
**Source Branch:** [feat/statistics](https://github.com/teqplay/vesselvoyage-backend/tree/feat/statistics)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-01-28T12:53:48.779993+00:00
**Status:** MERGED

You can try out the statistics on DEV: [https://vesselvoyagedev.teqplay.nl/#/statistics/ports](https://vesselvoyagedev.teqplay.nl/#/statistics/ports)  \(three new statistics pages\)
This PR implements a first set of statistics:
* Port statistics: calculated by querying all visits of the selected ports that started in the selected period, and calculating the average durations of those grouped per port per month.
* Ship statistics: calculated by querying all visits and voyages of the selected ships that started in the selected period, and calculating the average durations of those grouped per ship per month.
* Visit statistics: calculated by querying all visits of the selected port that started in the selected period, and calculating the durations of each individual visit.
It’s a large PR but it’s no rocket science:
* Implemented data models, statistics functions, and endpoints to get stats as JSON or CSV
* Not related to this PR: moved constants into a single file model/constants.kt, it started to confuse me.
* Unit tests :sweat_smile:


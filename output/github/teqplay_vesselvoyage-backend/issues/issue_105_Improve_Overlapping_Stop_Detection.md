---
id: github:teqplay/vesselvoyage-backend:issue:105
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 105
title: Improve Overlapping Stop Detection
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/105
labels: []
explicit_links: []
---
# Issue #105: Improve Overlapping Stop Detection

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/105  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [285747a18a2b...75facd0fce56](https://github.com/teqplay/vesselvoyage-backend/compare/285747a18a2b...75facd0fce56)
**Merge commit:** [75facd0fce56](https://github.com/teqplay/vesselvoyage-backend/commit/75facd0fce56)
**Author:** Darius Wattimena
**Reviewers:** Gavin den Hollander
**Approvers:** Former user
**Source Branch:** [improve_overlapping_stop_detection](https://github.com/teqplay/vesselvoyage-backend/tree/improve_overlapping_stop_detection)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-08-26T07:49:36.888984+00:00
**Status:** MERGED

* Implemented an extra step to combine overlapping stops that are from different movement event blocks
* ktlint
* Added tests to combine stops when they overlap and are short time between or when having a certain dimension


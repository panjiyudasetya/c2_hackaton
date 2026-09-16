---
id: github:teqplay/vesselvoyage-backend:issue:299
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 299
title: 'Api Model: Extend Slow Moving Period'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/299
labels: []
explicit_links: []
---
# Issue #299: Api Model: Extend Slow Moving Period

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/299  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [ce24f099c111...d7b34d2b1d56](https://github.com/teqplay/vesselvoyage-backend/compare/ce24f099c111...d7b34d2b1d56)
**Merge commit:** [d7b34d2b1d56](https://github.com/teqplay/vesselvoyage-backend/commit/d7b34d2b1d56)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Leon Joosse, Former user
**Source Branch:** [extend-slow-moving-period](https://github.com/teqplay/vesselvoyage-backend/tree/extend-slow-moving-period)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-30T14:36:12.613328+00:00
**Status:** MERGED

We are currently not filling in the slow moving periods in the esof \(always defaulting to an empty list\). So adding the `id` field is a non-breaking change.
The addition of an ID field was something David and I decided as we need some unique id for each item on the frontend side → [https://bitbucket.org/teqplay/vesselvoyage/pull-requests/38#comment-525391746](https://bitbucket.org/teqplay/vesselvoyage/pull-requests/38#comment-525391746)


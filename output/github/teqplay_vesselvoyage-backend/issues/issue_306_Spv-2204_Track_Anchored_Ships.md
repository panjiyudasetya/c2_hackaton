---
id: github:teqplay/vesselvoyage-backend:issue:306
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 306
title: Spv-2204 Track Anchored Ships
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/306
labels: []
explicit_links: []
---
# Issue #306: Spv-2204 Track Anchored Ships

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/306  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [a2611902dafb...ef70b88b7226](https://github.com/teqplay/vesselvoyage-backend/compare/a2611902dafb...ef70b88b7226)
**Merge commit:** [ef70b88b7226](https://github.com/teqplay/vesselvoyage-backend/commit/ef70b88b7226)
**Author:** Darius Wattimena
**Reviewers:** Michel Wilson, Leon Joosse
**Approvers:** Former user
**Source Branch:** [SPV-2204-track-anchored-ships](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2204-track-anchored-ships)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-08-01T15:14:12.024245+00:00
**Status:** MERGED

Decided together with Michel to use event rate as tracking the anchored ships will otherwise be very hard.
Also good thing to note, we only call `getGauge` when there are no `issues` and the event resulted in `changes`. So the counter is only counted when all went well and the event is not ignored.


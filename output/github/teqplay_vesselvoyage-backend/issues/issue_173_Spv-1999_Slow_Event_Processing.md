---
id: github:teqplay/vesselvoyage-backend:issue:173
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 173
title: Spv-1999 Slow Event Processing
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/173
labels: []
explicit_links: []
---
# Issue #173: Spv-1999 Slow Event Processing

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/173  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [6985dc39aba4...e1ded53b0dca](https://github.com/teqplay/vesselvoyage-backend/compare/6985dc39aba4...e1ded53b0dca)
**Merge commit:** [e1ded53b0dca](https://github.com/teqplay/vesselvoyage-backend/commit/e1ded53b0dca)
**Author:** Darius Wattimena
**Reviewers:** Joost Laurman, Michel Wilson, Shan Minh Nguyen
**Approvers:** Michel Wilson, Shan Minh Nguyen
**Source Branch:** [SPV-1999-slow-event-processing](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1999-slow-event-processing)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-03-07T11:20:57.863510+00:00
**Status:** MERGED

When going over the problem I’ve noticed that UniqueBerthEvent took a long time, especially the END ones. The cause of this ended up being that when there were 100 berth visits already we still processed the END events as the safeguarding was only done when we would retrieve a START event.
This PR fixes the issue by moving the check to the base processor instead, meaning it will be used by both the start and end event processor


---
id: github:teqplay/vesselvoyage-backend:issue:7
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 7
title: Fix/Inconsistent Voyage Start Time
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/7
labels: []
explicit_links: []
---
# Issue #7: Fix/Inconsistent Voyage Start Time

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/7  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [4ca6dbb7d3a3...a728c7fa809c](https://github.com/teqplay/vesselvoyage-backend/compare/4ca6dbb7d3a3...a728c7fa809c)
**Merge commit:** [a728c7fa809c](https://github.com/teqplay/vesselvoyage-backend/commit/a728c7fa809c)
**Author:** Jos de Jong
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [fix/inconsistent_voyage_start_time](https://github.com/teqplay/vesselvoyage-backend/tree/fix/inconsistent_voyage_start_time)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2021-08-12T14:45:53.677586+00:00
**Status:** MERGED

Fix startTime of a voyage not always being consistent with the endTime of the preceding visit: issue when the end time of the anchorage is later than then end event of the port area event \(an edge case\)

@{5c57efac4912b735b9e0646c} only if you still have time today to have a short look, else I’ll just merge it.


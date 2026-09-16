---
id: github:teqplay/vesselvoyage-backend:issue:12
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 12
title: Implement A New Discontinue Action In Case A Ship Is Removed From The System
  After A Recalculation
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/12
labels: []
explicit_links: []
---
# Issue #12: Implement A New Discontinue Action In Case A Ship Is Removed From The System After A Recalculation

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/12  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [3ca51a1a8d9d...0027f16a1ca2](https://github.com/teqplay/vesselvoyage-backend/compare/3ca51a1a8d9d...0027f16a1ca2)
**Merge commit:** [0027f16a1ca2](https://github.com/teqplay/vesselvoyage-backend/commit/0027f16a1ca2)
**Author:** Jos de Jong
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [fix/discontinue_status_update](https://github.com/teqplay/vesselvoyage-backend/tree/fix/discontinue_status_update)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2021-09-23T08:51:08.399734+00:00
**Status:** MERGED

So now, when after recalculation a ship is removed from the system \(for example because it is a pleasure craft or so\), an event will be put on the queue like:

```
Change(Action.DISCONTINUE, entry)
```

Instead of radio silence


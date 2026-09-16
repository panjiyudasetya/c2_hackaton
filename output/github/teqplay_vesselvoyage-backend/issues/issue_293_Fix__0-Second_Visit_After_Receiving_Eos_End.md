---
id: github:teqplay/vesselvoyage-backend:issue:293
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 293
title: 'Fix: 0-Second Visit After Receiving Eos End'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/293
labels: []
explicit_links: []
---
# Issue #293: Fix: 0-Second Visit After Receiving Eos End

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/293  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [769b1bb13672...b70f7c7974bc](https://github.com/teqplay/vesselvoyage-backend/compare/769b1bb13672...b70f7c7974bc)
**Merge commit:** [b70f7c7974bc](https://github.com/teqplay/vesselvoyage-backend/commit/b70f7c7974bc)
**Author:** Former user
**Reviewers:** Leon Joosse, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [fix/0-second-visit](https://github.com/teqplay/vesselvoyage-backend/tree/fix/0-second-visit)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-26T06:47:03.879807+00:00
**Status:** MERGED

If a ship enters two EOS' and we leave the first, we create a 0-second voyage and start a visit for the other EOS. If we now also get the other EOS end, then we’d create a 0-second visit.
Without the `currentVisit.start.time == voyageStartLocationTime.time` check, we could get a 0-second voyage followed by a visit that would become 0-second as well.
For example:
![](https://bitbucket.org/repo/k5G8e7j/images/3061277499-image.png)
We handle this case as a pass through.


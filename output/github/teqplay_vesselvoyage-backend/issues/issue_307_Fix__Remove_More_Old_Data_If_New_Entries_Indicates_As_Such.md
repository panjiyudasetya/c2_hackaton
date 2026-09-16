---
id: github:teqplay/vesselvoyage-backend:issue:307
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 307
title: 'Fix: Remove More Old Data If New Entries Indicates As Such'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/307
labels: []
explicit_links: []
---
# Issue #307: Fix: Remove More Old Data If New Entries Indicates As Such

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/307  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [d7b34d2b1d56...d5074e5bec22](https://github.com/teqplay/vesselvoyage-backend/compare/d7b34d2b1d56...d5074e5bec22)
**Merge commit:** [d5074e5bec22](https://github.com/teqplay/vesselvoyage-backend/commit/d5074e5bec22)
**Author:** Former user
**Reviewers:** Leon Joosse, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [fix/remove-more-old-data-if-new-indicates](https://github.com/teqplay/vesselvoyage-backend/tree/fix/remove-more-old-data-if-new-indicates)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-31T07:23:42.348988+00:00
**Status:** MERGED

Taking this as an example:
![](https://bitbucket.org/repo/k5G8e7j/images/715811548-image.png)
The `USPTM` and `USORF` visits are not removed, whereas we’d expect them to be if we regenerate up to 2024-07-28.
When looking at the new data, to be merged back:
![](https://bitbucket.org/repo/k5G8e7j/images/255494707-image.png)
It seems the `USPTM` and `USORF` visits should be removed because the ship was in a voyage at that moment.

However, I envisioned that “missing” data in this case meant we couldn’t invalidate and remove those old visits. Looking at it again though, it is required to remove these.
This PR removes code that allowed for this ‘more sensitive’ approach to merging back, instead we just trust that \(r\)events and VesselVoyage do the right thing and we are guaranteed that there really is no data here.


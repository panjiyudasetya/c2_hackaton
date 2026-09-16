---
id: github:teqplay/vesselvoyage-backend:issue:43
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 43
title: Process To Uniqueberthevents Into Visit.Berthareavisit[]
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/43
labels: []
explicit_links: []
---
# Issue #43: Process To Uniqueberthevents Into Visit.Berthareavisit[]

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/43  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [6dc41140f97c...d58d8fe99e19](https://github.com/teqplay/vesselvoyage-backend/compare/6dc41140f97c...d58d8fe99e19)
**Merge commit:** [d58d8fe99e19](https://github.com/teqplay/vesselvoyage-backend/commit/d58d8fe99e19)
**Author:** Jos de Jong
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [feat/berth_events](https://github.com/teqplay/vesselvoyage-backend/tree/feat/berth_events)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-08-26T07:49:38.817111+00:00
**Status:** MERGED

This PR adds support for \(unique\) berth events: process those events and put them in `Visit.berthAreas`.
* Implement a new `processUniqueBerthEvent`
* Implement a generic helper function `replaceLastMatchingEventPair` and use this 3 times:
    * `updateMatchingPortAreaVisit` \(formerly `updatePortAreasWithEndEvent`\)
    
        `updateMatchingAnchorAreaVisit` \(formerly `updateVisitWithAnchorEndEvent`\)
    
    
        `updateMatchingBerthAreaVisit` \(new\)
    
    
* Fix a small non-related bug: make `Encounter.otherImo` nullable \(many encounters are with barges for waste collection etc\)
* Implement tests \(also some non-related tests\)

IMPORTANT: When deploying, need to do a data migration of all visits:
```
db.visits.updateMany({ berthAreas: { "$exists" : false } }, { $set: { berthAreas: [] }})
```


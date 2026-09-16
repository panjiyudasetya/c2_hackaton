---
id: github:teqplay/vesselvoyage-backend:issue:125
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 125
title: Develop
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/125
labels: []
explicit_links: []
---
# Issue #125: Develop

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/125  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [8d828130d21f...16e7dcb29fa7](https://github.com/teqplay/vesselvoyage-backend/compare/8d828130d21f...16e7dcb29fa7)
**Merge commit:** [16e7dcb29fa7](https://github.com/teqplay/vesselvoyage-backend/commit/16e7dcb29fa7)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/vesselvoyage-backend/tree/master)
**Closed On:** 2023-06-07T15:54:47.100969+00:00
**Status:** MERGED

* Merged in feat/PRP-1896/new\_endpoints\_to\_retrieve\_visit\_info \(pull request #130\)
    PRP-1896 : New endpoints to retrieve the combined visit\+voyage pairs, retrieve visitIds for a given imo and retrieve count of visits by imo.

    * PRP-1896 : New endpoints to retrieve the combined visit\+voyage pairs, retrieve visitIds for a given imo and retrieve count of visits by imo.
    * PRP-1896 : Feedback applied consisted in renaming and setting a more readable logic \(findConsecutiveVisits -> findPastVisits & findFutureVisits, and other\).
    
    Approved-by: Darius Wattimena

* Merged in feat/PRP-1896/return\_VisitsVoyage\_pairs\_with\_visit\_previousEntryId\_relation \(pull request #132\)
    Feat/PRP-1896/return VisitsVoyage pairs with visit previousEntryId relation

    * PRP-1896 : New endpoints to retrieve the combined visit\+voyage pairs, retrieve visitIds for a given imo and retrieve count of visits by imo.
    * PRP-1896 : Feedback applied consisted in renaming and setting a more readable logic \(findConsecutiveVisits -> findPastVisits & findFutureVisits, and other\).
    * PRP-1896 : Return pairs VisitVoyage so the relation is leadingVisit of a voyage.
    * Merge branch 'develop' into feat/PRP-1896/return\_VisitsVoyage\_pairs\_with\_visit\_previousEntryId\_relation
    * PRP-1896 : Don't supervise Voyage nullability in each pair, just return it as it is.
    
    Approved-by: Darius Wattimena



---
id: github:teqplay/vesselvoyage-backend:issue:42
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 42
title: Refactor Visitshipstatus.Regroupesof And Fix/Extend Voyageshipstatus.Regroupesof
  Which Was Not Handling Previousvoyage
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/42
labels: []
explicit_links: []
---
# Issue #42: Refactor Visitshipstatus.Regroupesof And Fix/Extend Voyageshipstatus.Regroupesof Which Was Not Handling Previousvoyage

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/42  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [c10b5f3eb1d5...6dc41140f97c](https://github.com/teqplay/vesselvoyage-backend/compare/c10b5f3eb1d5...6dc41140f97c)
**Merge commit:** [6dc41140f97c](https://github.com/teqplay/vesselvoyage-backend/commit/6dc41140f97c)
**Author:** Jos de Jong
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena, Former user
**Source Branch:** [fix/esof_regrouping_voyageshipstatus](https://github.com/teqplay/vesselvoyage-backend/tree/fix/esof_regrouping_voyageshipstatus)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-01-13T11:33:46.316677+00:00
**Status:** MERGED

There was a bug in the regrouping of e-sof items. For example the following ship has a visit in SGSIN at 2021-12-03, and the e-sof contains encounters and stops from far before the visit \(in November\), which should be attached to the previous voyage instead: [https://vesselvoyagedev.teqplay.nl/#/ships/9705146/story](https://vesselvoyagedev.teqplay.nl/#/ships/9705146/story)

The cause was that the function `VoyageShipStatus.regroupESof()` wasn’t handling `previousVoyage` and emptying it instead, putting all events into `previousVisit` and `voyage`.

To solve this, I inlined the contents of the private helper function `regroupESof(visitBefore, voyage, visitAfter)` into the two functions where it was used, `VisitShipStatus.regroupESof()` and `VoyageShipStatus.regroupESof()` and changed `VoyageShipStatus.regroupESof()` to also handle `previousVoyage`.


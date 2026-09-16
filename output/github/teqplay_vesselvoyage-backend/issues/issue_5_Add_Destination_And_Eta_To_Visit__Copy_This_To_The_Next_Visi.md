---
id: github:teqplay/vesselvoyage-backend:issue:5
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 5
title: Add Destination And Eta To Visit. Copy This To The Next Visit/Voyage
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/5
labels: []
explicit_links: []
---
# Issue #5: Add Destination And Eta To Visit. Copy This To The Next Visit/Voyage

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/5  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [bfeec9be4dd2...0aa55e031a6f](https://github.com/teqplay/vesselvoyage-backend/compare/bfeec9be4dd2...0aa55e031a6f)
**Merge commit:** [0aa55e031a6f](https://github.com/teqplay/vesselvoyage-backend/commit/0aa55e031a6f)
**Author:** Jos de Jong
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [feat/visit_destination](https://github.com/teqplay/vesselvoyage-backend/tree/feat/visit_destination)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2021-07-16T07:54:35.922397+00:00
**Status:** MERGED

* There is duplicated logic now in processDestinationChangedEvent and processEtaEvent. It’s not much in terms of actual code, and the alternative to unify/generalize has also overhead complicating matters. If you know an easy way to deduplicate this logic without introducing extra complexity I would love to hear
* Currently, the eta/destination is copied from one Visit/Voyage to the next. I expect this will give issues when the eta is no longer updated, then you carry on an old ETA forever. I created a separate card to think that through: [https://trello.com/c/04SzN95F/8530-do-not-copy-eta-and-destination-from-a-previous-visit-voyage-to-a-next-one-when-outdated](https://trello.com/c/04SzN95F/8530-do-not-copy-eta-and-destination-from-a-previous-visit-voyage-to-a-next-one-when-outdated)
* Currently the eta/destination on a Visit is not visible in the frontend. I created a separate card for that: [https://trello.com/c/wE6K765j/8529-2-show-destination-eta-of-visits-in-the-frontend-where-applicable](https://trello.com/c/wE6K765j/8529-2-show-destination-eta-of-visits-in-the-frontend-where-applicable)
* I’ve added eta and destination in the unit tests, so it’s quite thoroughly tested. I would love to refactor the unit tests though to make these tests explicit \(currently, in the unit tests, the defined visits/voyages are reused in multiple tests, and copied and adjusted here and there, but this is now a bit messy\). Will also address that later
* I’ve also removed the restriction that you cannot deploy a feature branch in CircleCI \(was limited to `master` and `develop` branch before\)



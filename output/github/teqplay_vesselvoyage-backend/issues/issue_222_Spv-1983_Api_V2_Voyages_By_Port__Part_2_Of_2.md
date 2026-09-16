---
id: github:teqplay/vesselvoyage-backend:issue:222
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 222
title: Spv-1983 Api V2 Voyages By Port (Part 2 Of 2)
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/222
labels: []
explicit_links: []
---
# Issue #222: Spv-1983 Api V2 Voyages By Port (Part 2 Of 2)

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/222  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [4e506181a156...0874b61da2ab](https://github.com/teqplay/vesselvoyage-backend/compare/4e506181a156...0874b61da2ab)
**Merge commit:** [0874b61da2ab](https://github.com/teqplay/vesselvoyage-backend/commit/0874b61da2ab)
**Author:** Leon Joosse
**Reviewers:** Darius Wattimena
**Approvers:** Former user
**Source Branch:** [SPV-1983-api-v2-voyages-by-port](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1983-api-v2-voyages-by-port)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-05-07T08:52:02.684299+00:00
**Status:** MERGED

* Add `NewVoyage.origin` and `NewVoyage.destination`, and populate them in their respective create/resume/finish methods
* Add endpoint for querying voyage by origin and/or destination
* Rename `pomaId` to `areaId`. 
* Use `Instant`s instead of `ZonedDateTime`


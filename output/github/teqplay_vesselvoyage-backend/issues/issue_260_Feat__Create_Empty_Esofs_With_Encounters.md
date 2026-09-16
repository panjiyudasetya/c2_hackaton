---
id: github:teqplay/vesselvoyage-backend:issue:260
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 260
title: 'Feat: Create Empty Esofs With Encounters'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/260
labels: []
explicit_links:
- jira:SPV-2198
---
# Issue #260: Feat: Create Empty Esofs With Encounters

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/260  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [647da79d0d23...bf50a0d7d201](https://github.com/teqplay/vesselvoyage-backend/compare/647da79d0d23...bf50a0d7d201)
**Merge commit:** [bf50a0d7d201](https://github.com/teqplay/vesselvoyage-backend/commit/bf50a0d7d201)
**Author:** Former user
**Reviewers:** Leon Joosse, Darius Wattimena
**Approvers:** Leon Joosse
**Source Branch:** [SPV-2198-merge-encounters-into-new-esofs](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2198-merge-encounters-into-new-esofs)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-06-26T12:15:05.633458+00:00
**Status:** MERGED

We’ll be running \(r\)events to generate VesselVoyage V2 entries without encounters. Since we’d start with the encounters from event-history we need a way to get these into new ESoFs.
This PR implements a way to generate new ESoFs for given `entries` and `encounters`, populating only the `NewESoF.encounters`.
A subsequent PR will do the requesting of event-history, calling this method and storing the data.


---
id: github:teqplay/vesselvoyage-backend:issue:204
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 204
title: Spv-2029 Persist Esof
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/204
labels: []
explicit_links: []
---
# Issue #204: Spv-2029 Persist Esof

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/204  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [c63dcb157722...b7cebab9b119](https://github.com/teqplay/vesselvoyage-backend/compare/c63dcb157722...b7cebab9b119)
**Merge commit:** [b7cebab9b119](https://github.com/teqplay/vesselvoyage-backend/commit/b7cebab9b119)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Former user
**Source Branch:** [SPV-2029-persist-esof](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2029-persist-esof)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-04-10T08:28:02.836360+00:00
**Status:** MERGED

When checking all on DEV I noticed the esof wasn’t persisted. This PR does the following:
* Split the NewChange model, so it is split into VisitChange, VoyageChange and ESoFChange
* Update the persisting of the processing results to now use the new model and also persist the esof change
* Adjust existing processors to be using this new change model
* Fixed an issue on the Encounter processor so it can return an update on the Visit/Voyage while having a create for the esof when applicable
* Adjust the dry-run mechanism that revents uses so it still works as expected


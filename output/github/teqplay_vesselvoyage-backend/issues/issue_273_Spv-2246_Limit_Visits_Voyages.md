---
id: github:teqplay/vesselvoyage-backend:issue:273
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 273
title: Spv-2246 Limit Visits Voyages
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/273
labels: []
explicit_links: []
---
# Issue #273: Spv-2246 Limit Visits Voyages

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/273  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [50ba0a87396c...0347dcee5dfe](https://github.com/teqplay/vesselvoyage-backend/compare/50ba0a87396c...0347dcee5dfe)
**Merge commit:** [0347dcee5dfe](https://github.com/teqplay/vesselvoyage-backend/commit/0347dcee5dfe)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Former user
**Source Branch:** [SPV-2246-limit-visits-voyages](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2246-limit-visits-voyages)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-10T09:44:11.368002+00:00
**Status:** MERGED

* Adjusted visit and voyage model to include a field that indicates if the entry is limited in some way
* Added logic to limit event processing when we have more than 100 ongoing activities in one of the area activities or in the stops
* Removed some unneeded configuration
* Removed old migration which doesn't run when having an empty database
* Removed unused imports


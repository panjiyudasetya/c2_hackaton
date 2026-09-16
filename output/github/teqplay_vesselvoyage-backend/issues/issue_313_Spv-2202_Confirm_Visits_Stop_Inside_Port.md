---
id: github:teqplay/vesselvoyage-backend:issue:313
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 313
title: Spv-2202 Confirm Visits Stop Inside Port
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/313
labels: []
explicit_links:
- jira:SPV-2202
---
# Issue #313: Spv-2202 Confirm Visits Stop Inside Port

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/313  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [e7f0180ec0f1...f87673e43134](https://github.com/teqplay/vesselvoyage-backend/compare/e7f0180ec0f1...f87673e43134)
**Merge commit:** [f87673e43134](https://github.com/teqplay/vesselvoyage-backend/commit/f87673e43134)
**Author:** Darius Wattimena
**Reviewers:** Michel Wilson, Leon Joosse
**Approvers:** Leon Joosse
**Source Branch:** [SPV-2202-confirm-visits-stop-inside-port](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2202-confirm-visits-stop-inside-port)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-08-09T08:27:10.321927+00:00
**Status:** MERGED

* Changed confirmed behaviour to also base it on if we stopped inside a port
* Adjusted how port area activities are moved to the next visit when having 0-second voyages
* Adjusted existing test to support the new behaviour of passing over the other ongoing port area activities


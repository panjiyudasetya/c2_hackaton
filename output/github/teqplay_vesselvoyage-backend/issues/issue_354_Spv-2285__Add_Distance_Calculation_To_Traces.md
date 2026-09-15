---
id: github:teqplay/vesselvoyage-backend:issue:354
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 354
title: 'Spv-2285: Add Distance Calculation To Traces'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/354
labels: []
explicit_links: []
---
# Issue #354: Spv-2285: Add Distance Calculation To Traces

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/354  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [1bf9c043a372...7be15a65fa74](https://github.com/teqplay/vesselvoyage-backend/compare/1bf9c043a372...7be15a65fa74)
**Merge commit:** [7be15a65fa74](https://github.com/teqplay/vesselvoyage-backend/commit/7be15a65fa74)
**Author:** Leon Joosse
**Reviewers:** Michel Wilson, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-2283-travel-distance](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2283-travel-distance)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-11-08T09:08:10.204092+00:00
**Status:** MERGED

This PR adds distance calculation to traces.
I put it in a separate class, to not further pollute `ProcessingTraceService` with implementation, and for easier unit testing.


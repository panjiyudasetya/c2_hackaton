---
id: github:teqplay/vesselvoyage-backend:issue:208
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 208
title: Spv-2052 New Trace Support
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/208
labels: []
explicit_links: []
---
# Issue #208: Spv-2052 New Trace Support

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/208  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [8110fb54fafb...52987549f184](https://github.com/teqplay/vesselvoyage-backend/compare/8110fb54fafb...52987549f184)
**Merge commit:** [52987549f184](https://github.com/teqplay/vesselvoyage-backend/commit/52987549f184)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Former user
**Source Branch:** [SPV-2052-new-trace-support](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2052-new-trace-support)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-04-15T12:21:05.339151+00:00
**Status:** MERGED

NOTE: This PR doesn’t add support for reading NATS diff messages or getting it via ShipHistory to save the new Trace.  
This is only focusing on the actual logic part of how the traces are updated and build upon, and how they are merged when canceling a Visit


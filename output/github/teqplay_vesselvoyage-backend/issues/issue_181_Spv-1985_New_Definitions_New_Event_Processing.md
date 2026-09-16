---
id: github:teqplay/vesselvoyage-backend:issue:181
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 181
title: Spv-1985 New Definitions New Event Processing
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/181
labels: []
explicit_links:
- jira:SPV-1985
---
# Issue #181: Spv-1985 New Definitions New Event Processing

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/181  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [8667359d40df...ebe769b20bd6](https://github.com/teqplay/vesselvoyage-backend/compare/8667359d40df...ebe769b20bd6)
**Merge commit:** [ebe769b20bd6](https://github.com/teqplay/vesselvoyage-backend/commit/ebe769b20bd6)
**Author:** Darius Wattimena
**Reviewers:** Joost Laurman, Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [SPV-1985-new-definitions-new-event-processing](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1985-new-definitions-new-event-processing)
**Destination Branch:** [SPV-1985-new-definitions](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1985-new-definitions)
**Closed On:** 2024-03-25T08:48:26.886601+00:00
**Status:** MERGED

In this PR the following is addressed:
* Internal ShipStateService is adjusted to allow for the new Visit/Voyage state classes.
* The event processors have now support for adjusting the `NewShipStatus` into the `NewEventProcessingResult`.
I don’t think a session is needed to talk about this PR as it is pretty straight forward, but please let me know if needed so we can sit for ~15 minutes.
NOTE: This PR doesn’t touch on the new definitions being implemented, this will come in the next one.


---
id: github:teqplay/vesselvoyage-backend:issue:190
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 190
title: Spv-2025 New Definitions Encounter Events
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/190
labels: []
explicit_links:
- jira:SPV-2025
- jira:SPV-1985
---
# Issue #190: Spv-2025 New Definitions Encounter Events

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/190  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [4b83299be9d4...581df63650f8](https://github.com/teqplay/vesselvoyage-backend/compare/4b83299be9d4...581df63650f8)
**Merge commit:** [581df63650f8](https://github.com/teqplay/vesselvoyage-backend/commit/581df63650f8)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop
**Approvers:** Former user
**Source Branch:** [SPV-2025-new-definitions-encounter-events](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2025-new-definitions-encounter-events)
**Destination Branch:** [SPV-1985-new-definitions](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1985-new-definitions)
**Closed On:** 2024-08-26T07:49:35.887787+00:00
**Status:** MERGED

* Adjust the NewChange model to also include the updated esof
* Added a helper function to replace the first item with a replacement
* Added a start event id to the encounter model to match on
* Implemented the new encounter logic which adjusts the esof of the ongoing visit or voyage
* Added test case to ensure the encounter logic is working as intended


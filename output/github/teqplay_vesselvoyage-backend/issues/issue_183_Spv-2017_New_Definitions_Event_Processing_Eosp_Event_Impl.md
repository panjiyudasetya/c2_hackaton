---
id: github:teqplay/vesselvoyage-backend:issue:183
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 183
title: Spv-2017 New Definitions Event Processing Eosp Event Impl
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/183
labels: []
explicit_links:
- jira:SPV-1985
---
# Issue #183: Spv-2017 New Definitions Event Processing Eosp Event Impl

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/183  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [ebe769b20bd6...8af039b97e9d](https://github.com/teqplay/vesselvoyage-backend/compare/ebe769b20bd6...8af039b97e9d)
**Merge commit:** [8af039b97e9d](https://github.com/teqplay/vesselvoyage-backend/commit/8af039b97e9d)
**Author:** Darius Wattimena
**Reviewers:** Joost Laurman, Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [SPV-1985-new-definitions-event-processing-impl](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1985-new-definitions-event-processing-impl)
**Destination Branch:** [SPV-1985-new-definitions](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1985-new-definitions)
**Closed On:** 2024-03-25T08:50:25.880021+00:00
**Status:** MERGED

* Added support for processing end of sea passage events to result in a basic Visit/Voyage structure
* Added support to create a Visit when having no state for the ship when receiving a end of sea passage start event
* Adjusted testing constants to be using strings of numbers for MMSIs and IMOs
* Added test cases to ensure all different flows are handled as expected
* Fixed an issue where a visit would not be added as a pass through of the voyage when exiting the end of sea passage


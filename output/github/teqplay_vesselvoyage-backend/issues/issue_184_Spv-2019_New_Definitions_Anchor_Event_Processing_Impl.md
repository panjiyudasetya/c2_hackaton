---
id: github:teqplay/vesselvoyage-backend:issue:184
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 184
title: Spv-2019 New Definitions Anchor Event Processing Impl
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/184
labels: []
explicit_links:
- jira:SPV-2019
- jira:SPV-1985
---
# Issue #184: Spv-2019 New Definitions Anchor Event Processing Impl

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/184  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [8af039b97e9d...23a672ff4905](https://github.com/teqplay/vesselvoyage-backend/compare/8af039b97e9d...23a672ff4905)
**Merge commit:** [23a672ff4905](https://github.com/teqplay/vesselvoyage-backend/commit/23a672ff4905)
**Author:** Darius Wattimena
**Reviewers:** Joost Laurman, Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [SPV-2019-new-definitions-anchor-event-processing-impl](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2019-new-definitions-anchor-event-processing-impl)
**Destination Branch:** [SPV-1985-new-definitions](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1985-new-definitions)
**Closed On:** 2024-03-25T08:50:39.656888+00:00
**Status:** MERGED

* Added implementation to add support for creating anchor area activities on a start event
* Moved some logic to the base class and make sure on voyage and initial status we ignore the event
* Moved the check if the event has a valid area id to the base processor
* Added implementation for th anchor end event
* Moved processing issue descriptions to consts
* Adjusted tests to be easier to extend
* Moved issue description to consts
* Added extra test cases to ensure anchor start and end events are not processed on voyage and initial status
* Added test cases to ensure anchor area activities are added correctly when in visit status
* Added extra test cases that should ignore the provided anchor event
* Code cleanup


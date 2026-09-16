---
id: github:teqplay/vesselvoyage-backend:issue:166
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 166
title: Spv-1296 Springify Processing
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/166
labels: []
explicit_links:
- jira:SPV-1296
---
# Issue #166: Spv-1296 Springify Processing

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/166  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [e4d4889470cf...e7ac13c2fffa](https://github.com/teqplay/vesselvoyage-backend/compare/e4d4889470cf...e7ac13c2fffa)
**Merge commit:** [e7ac13c2fffa](https://github.com/teqplay/vesselvoyage-backend/commit/e7ac13c2fffa)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop
**Approvers:** Former user
**Source Branch:** [SPV-1296-springify-processing](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1296-springify-processing)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-02-21T11:05:37.296056+00:00
**Status:** MERGED

* Added basic structure for event processing
* Changed processing so they make use of the new EventProcessingService
* implemented destination changed event processor
* Changed event classes by introducing the StartEndEvent base class
* Adjusted existing processing to also return the new ship status
* Added a new event processor used for start end events
* Adjusted interface to instead return the result directly to make it easier to use
* Added logic to process an anchor event
* Added logic to process an encounter event
* Added logic to process an eta event
* Adjusted encounter event processing to be using the new ESofEventProcessor
* Added movement event processor
* Added port event processor
* Added status changed event processor
* Added unique berth event processor
* Code cleanup
* Fixed processing issues
* Adjust event processing to support not getting the event trace when doing it afterwards
* Adjusted port processing to not call the trace service when it has been turned off
* Enabled trace calculations by default
* ktlint
* Adjusted some compile issues for the tests after making the config changes


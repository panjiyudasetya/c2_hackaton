---
id: github:teqplay/vesselvoyage-backend:pr:402
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 402
title: 'SPV-2489: fix: other main port eosp end fires when ship status is already
  in voyage'
author: leonjoosse
state: closed
date: '2025-01-28'
merged_at: '2025-01-31'
base_branch: develop
head_branch: SPV-2489-other-mainport-eosp-end-in-voyage
url: https://github.com/teqplay/vesselvoyage-backend/pull/402
labels: []
linked_issues: []
explicit_links: []
---
# PR #402: SPV-2489: fix: other main port eosp end fires when ship status is already in voyage

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/402  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `SPV-2489-other-mainport-eosp-end-in-voyage`  
**Created:** 2025-01-28  
**Merged:** 2025-01-31  

## Description

When exiting multiple EOSPs of main ports at the same time (event on same AIS point), then one of these ‘other ongoing main port eosp’ stays open forever. This is caused by the ‘other ongoing main port eosp' 

Example: 

1. visit is for port A. Port B is listed as ‘other ongoing main port eosp’. 
2. The EOSP end event for A is provided, visit is ended, voyage is created. B stays as ‘other ongoing main port eosp’ on A.
3. The EOSP end event for B is provided, but the ship status is now voyage, so the event is discarded. The next visit will take over B as ‘other ongoing main port eosp’ (as the end event was not processed, VV assumes it continues).  

Expected behavior:

In the above example, when the EOSP end event for B is provided, the end processor should not ignore this event in getResultOnVoyage. Instead: port B is removed from ‘other ongoing main port eosp’ list in A and put on the pass through list of A.





## Commits

- `17ec66d8` **leonj** (2025-01-24): When in a voyage, allow processing EOSP end event if that specifically is in the previousVisit.otherOngoingMainPortEosp list. It is then moved to the previousVisit.passthrough list. (test still wip)
- `364d8413` **leonj** (2025-01-27): Move test to correct class

## Reviews

### TeqJoostD — COMMENTED (2025-01-30)

_No comment._

### TeqJoostD — COMMENTED (2025-01-30)

_No comment._

### TeqJoostD — APPROVED (2025-01-30)

_No comment._

## Review Comments

### TeqJoostD — 2025-01-30 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageEndProcessor.kt`

What is the reason we compare the previous visit end time and the EOSP event time? Won't this always be different since the events are fired after the voyage has ended? Or are they fired at the same time but just received later.

### TeqJoostD — 2025-01-30 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/EventProcessingServiceTest.kt`

Is this always the case? That an EOSP event occurs when the visit ends?

---
id: github:teqplay/vesselvoyage-backend:pr:430
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 430
title: SPV-2545 fix on missing eosp end
author: Darius-Wattimena
state: closed
date: '2025-02-24'
merged_at: '2025-02-25'
base_branch: develop
head_branch: SPV-2545-fix-on-missing-eosp-end
url: https://github.com/teqplay/vesselvoyage-backend/pull/430
labels: []
linked_issues: []
explicit_links: []
---
# PR #430: SPV-2545 fix on missing eosp end

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/430  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `SPV-2545-fix-on-missing-eosp-end`  
**Created:** 2025-02-24  
**Merged:** 2025-02-25  

## Description

_No description._

## Commits

- `5a1387c3` **Darius Wattimena** (2025-02-21): Extended the eosp logic so we can set a fallback when we miss an end event
- `8572fc98` **Darius Wattimena** (2025-02-24): Added a first test case to ensure we can handle missing an EOSP event
- `b571b887` **Darius Wattimena** (2025-02-24): Made it so we never provide the area id when finishing a visit but instead let it be set by the new visit that is provided
- `2f61a7d6` **Darius Wattimena** (2025-02-24): Added a test case for the more complex usecase where we can have other ongoing EOSPs that need to become the new visit, moved to still ongoing or marked as pass-through
- `2835dd1f` **Darius Wattimena** (2025-02-24): Adjusted logic to fully work as expected when having ongoing eosps
- `2ea77f32` **Darius Wattimena** (2025-02-24): code cleanup
- `1f124b17` **Darius Wattimena** (2025-02-24): Added test cases to ensure fallback end times can be overwritten from previous visits
- `a02786a0` **Darius Wattimena** (2025-02-24): Extended logic to support overwriting end times when getting the end time while already being in the next visit or voyage
- `f4175ea7` **Darius Wattimena** (2025-02-25): Merge branch 'refs/heads/develop' into SPV-2545-fix-on-missing-eosp-end

## Reviews

### leonjoosse — COMMENTED (2025-02-25)

LGTM, but do have some questions

### Darius-Wattimena — COMMENTED (2025-02-25)

_No comment._

### Darius-Wattimena — COMMENTED (2025-02-25)

_No comment._

### leonjoosse — APPROVED (2025-02-25)

_No comment._

## Review Comments

### leonjoosse — 2025-02-25 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageEndProcessor.kt`

Hmm, how sure are we that the corrected voyage start is still before voyage.end?

### leonjoosse — 2025-02-25 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageEndProcessor.kt`

Same as comment earlier in this file (Hmm, how sure are we that the corrected voyage start is still before voyage.end?)

### leonjoosse — 2025-02-25 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageStartProcessor.kt`

Just a thought: should we transform the area already before putting the port in the cache?

### Darius-Wattimena — 2025-02-25 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageEndProcessor.kt`

I don't think we will ever trigger that issue besides maybe the EOSP being edited, already updated on the VesselVoyage cache, but the area monitor still uses the old definition.

If that is the case then it could be possible that this happens:
1. We get an EOSP start event with the OLD definition
2. Someone updates the definition of the EOSP
3. VesselVoyage updates their cache
4. We receive an EOSP start event for a different port and mark this one as "missed"
5. The AreaMonitor updates their cache + end event is triggered because ship is now outside the EOSP
6. VesselVoyage receives an EOSP end which is later than the current Visit start and the 0-second Voyage that was created

Do you think we should be prepared for situation like that? Because to me it feels like something that would rarely happen.

### Darius-Wattimena — 2025-02-25 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageStartProcessor.kt`

We are currently caching the Poma model. It might be good to create our own light-weight model that just contains the things that VesselVoyage needs? Will create a card.

### leonjoosse — 2025-02-25 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageEndProcessor.kt`

Yes, does feel very edge-casey. And I don't think we should accommodate for that.

---
id: github:teqplay/vesselvoyage-backend:issue:258
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 258
title: Spv-2076 Merging V2 Logic
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/258
labels: []
explicit_links:
- jira:SPV-2076
- jira:SPV-2032
- jira:SPV-2086
- jira:SPV-2100
- jira:SPV-2059
---
# Issue #258: Spv-2076 Merging V2 Logic

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/258  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [9ecac8479b00...2faa7cf085b9](https://github.com/teqplay/vesselvoyage-backend/compare/9ecac8479b00...2faa7cf085b9)
**Merge commit:** [2faa7cf085b9](https://github.com/teqplay/vesselvoyage-backend/commit/2faa7cf085b9)
**Author:** Former user
**Reviewers:** 
**Approvers:** 
**Source Branch:** [SPV-2076-merging-v2-logic](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2076-merging-v2-logic)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-06-19T12:18:43.660465+00:00
**Status:** MERGED

* Merged in SPV-2076-merging-v2-logic-extract-v1 \(pull request #220\)
    chore: extract V1 definition from merging logic

    * chore: extract V1 definition from merging logic
    * chore: extract V1 specific usage of startPortIds & endPortIds
    * chore: update docstring
    
    Approved-by: Leon Joosse

* Merged in SPV-2076-merging-v2-logic-implement-v2 \(pull request #222\)
    SPV-2076: implement merging V2

    * feat: merging V2
    * fix: include merging of ESOF
    * chore: update .circleci/config.yml
    * fix: allow disabling event-stream consumer
    * fix: ensure \_type is serialized
    
    Approved-by: Leon Joosse

* Merged in SPV-2076-merging-v2-logic-perform-merge \(pull request #223\)
    SPV-2076 merging v2 logic perform merge

    * feat: use V2 merging upon scenario completion
    * feat: allow running V1/V2/V1&V2 when creating a scenario
    * feedback
    
    Approved-by: Darius Wattimena

* Merged in SPV-2032-allow-merge-when-missing-structure \(pull request #224\)
    SPV-2032 allow merge when missing structure at the front

    * feat: allow merging when data is missing on the left of the visit/voyage structure
    * fix: don't allow merging when missing data at the end for now
    * chore: remove redundant notes
    * chore: cleanup
    * chore: simplify & don't allow nullable end
    * Merged SPV-2076-merging-v2-logic into SPV-2032-allow-merge-when-missing-structure
    
    Approved-by: Darius Wattimena

* Merged in SPV-2086-ensure-locking-is-used-when-merging \(pull request #226\)
    fix: ensure merge happens while under lock & current status is refreshed

    * fix: ensure merge happens while under lock & current status is refreshed
    
    Approved-by: Darius Wattimena

* Merged in SPV-2100-perform-enlarging-of-time-window-for-v2 \(pull request #231\)
    SPV-2100 perform enlarging of time window for v2

    * chore: only allow running one guarantee from the API
    * feat: enlarge V2 TimeWindow separately & consolidate skeleton TimeWindow and Instant usage
    * feedback: undo \_startTime
    
    Approved-by: Leon Joosse

* Merged in SPV-2059-ensure-merge-consistency-on-missing-start-and-begins-with-visit \(pull request #234\)
    fix: ensure merge consistency on missing start and beginning with a visit

    * fix: ensure merge consistency on missing start and beginning with a visit
    
    Approved-by: Darius Wattimena

* chore: add missing fields
* chore: add missing fields


---
id: github:teqplay/vesselvoyage-backend:issue:202
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 202
title: Switch Ais And Event Processing To Use Nats
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/202
labels: []
explicit_links:
- jira:SPV-1992
- jira:SPV-1946
- jira:SPV-2029
---
# Issue #202: Switch Ais And Event Processing To Use Nats

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/202  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [507b7dd6a6f8...d85403cf7767](https://github.com/teqplay/vesselvoyage-backend/compare/507b7dd6a6f8...d85403cf7767)
**Merge commit:** [d85403cf7767](https://github.com/teqplay/vesselvoyage-backend/commit/d85403cf7767)
**Author:** Darius Wattimena
**Reviewers:** 
**Approvers:** 
**Source Branch:** [feat/switch-to-ais-engine](https://github.com/teqplay/vesselvoyage-backend/tree/feat/switch-to-ais-engine)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-04-15T07:54:21.053399+00:00
**Status:** MERGED

* Merged in SPV-1992-consume-ship-history-from-nats-instead-of-rabbit-mq \(pull request #184\)
    feat\(trace\): use ais-stream:history for traces

    * feat\(trace\): use ais-stream:history for traces
    * chore: rename to 'aisWrapper' & add tests
    
    Approved-by: Darius Wattimena

* Merged in SPV-1946-events-via-nats \(pull request #209\)
    SPV-1946 events via nats

    * Merge branch 'SPV-2029-presist-new-visit-voyages' into SPV-1946-events-via-nats
    * Changed event history processing to use NATS instead to consume events
    * Hook in event processing
    * Adjusted health actuator result to support event processing
    * ktlint
    * Add mocking so the profile tests work again
    * Instead of keeping the thread alive interrupt it when calling shutdown
    * Removed unused properties and unneeded health check
    * fix: ensure consumer is drained to stop event processing
    * fix: reset running state when calling startup\(\) after shutdown\(\)
    
    Approved-by: Maurice van Veen Approved-by: Leon Joosse



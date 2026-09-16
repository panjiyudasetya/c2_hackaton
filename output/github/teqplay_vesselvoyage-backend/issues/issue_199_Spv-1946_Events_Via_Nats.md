---
id: github:teqplay/vesselvoyage-backend:issue:199
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 199
title: Spv-1946 Events Via Nats
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/199
labels: []
explicit_links: []
---
# Issue #199: Spv-1946 Events Via Nats

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/199  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [5236a83475c9...79bd81325d94](https://github.com/teqplay/vesselvoyage-backend/compare/5236a83475c9...79bd81325d94)
**Merge commit:** [79bd81325d94](https://github.com/teqplay/vesselvoyage-backend/commit/79bd81325d94)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Leon Joosse, Former user
**Source Branch:** [SPV-1946-events-via-nats](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1946-events-via-nats)
**Destination Branch:** [feat/switch-to-ais-engine](https://github.com/teqplay/vesselvoyage-backend/tree/feat/switch-to-ais-engine)
**Closed On:** 2024-04-08T09:16:23.741672+00:00
**Status:** MERGED

* Added a feature flag so we can enable processing of the new definition
* Added event processing when the feature flag is enabled
* Adjusted tests to have the new future flag set
* Changed event history processing to use NATS instead to consume events
* Hook in event processing
* Adjusted health actuator result to support event processing
* ktlint


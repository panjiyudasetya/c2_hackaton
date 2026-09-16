---
id: github:teqplay/vesselvoyage-backend:issue:167
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 167
title: Spv-1987 Remove Old Processing Logic
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/167
labels: []
explicit_links: []
---
# Issue #167: Spv-1987 Remove Old Processing Logic

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/167  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [e7ac13c2fffa...10654d3032b8](https://github.com/teqplay/vesselvoyage-backend/compare/e7ac13c2fffa...10654d3032b8)
**Merge commit:** [10654d3032b8](https://github.com/teqplay/vesselvoyage-backend/commit/10654d3032b8)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop
**Approvers:** Former user
**Source Branch:** [SPV-1987-remove-old-processing-logic](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1987-remove-old-processing-logic)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-02-21T11:06:14.385232+00:00
**Status:** MERGED

* Removed base processing logic class
* Changed anchor event processing test to use new logic
* Changed destination changed event processing test to use new logic
* Changed encounter event processing test to use new logic
* Adjusted main processing event class where the function would still be used
* Changed eta event processing test to use the new logic
* Changed movement event processing test to use the new logic
* Changed port event processing test to use the new logic
* Changed status changed event processing test to use the new logic
* Adjusted processing to match all test cases
* Return an empty result when an ETA is provided instead of throwing an exception
* Adjusted port logic to make sure unknown ports don't create a visit
* make sure the infra service is correctly mocked when testing stops with a trace found
* Code cleanup


---
id: github:teqplay/vesselvoyage-backend:issue:250
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 250
title: Spv-2126 Overrule Fallbacks With Real Value
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/250
labels: []
explicit_links: []
---
# Issue #250: Spv-2126 Overrule Fallbacks With Real Value

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/250  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [fe296056071c...f217be3b9b9a](https://github.com/teqplay/vesselvoyage-backend/compare/fe296056071c...f217be3b9b9a)
**Merge commit:** [f217be3b9b9a](https://github.com/teqplay/vesselvoyage-backend/commit/f217be3b9b9a)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Leon Joosse
**Source Branch:** [SPV-2126-overrule-fallbacks-with-real-value](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2126-overrule-fallbacks-with-real-value)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-06-07T11:41:23.328692+00:00
**Status:** MERGED

* Adjusted the area activities to be overwritten for the previous visit when a fallback was used
* Adjusted stop end event logic to also suppose overriding of the end time when a fallback is used
* Corrected the tests to ensure the new logic is being executed for all area activities that can potentially be ended by the fallback
* Adjusted area activity tests to make sure they are properly overridden when a fallback is used
* Added a test case to ensure we don't process start events when dealing with previous visits
* Added two more test cases where we don't want to process the area event when missing the area id or when no matching activity is found
* Correct the processing error message


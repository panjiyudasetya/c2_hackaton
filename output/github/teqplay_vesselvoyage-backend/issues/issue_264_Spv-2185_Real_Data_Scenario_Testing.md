---
id: github:teqplay/vesselvoyage-backend:issue:264
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 264
title: Spv-2185 Real Data Scenario Testing
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/264
labels: []
explicit_links:
- jira:SPV-2185
---
# Issue #264: Spv-2185 Real Data Scenario Testing

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/264  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [1f8ddd1c451b...c20efec139fd](https://github.com/teqplay/vesselvoyage-backend/compare/1f8ddd1c451b...c20efec139fd)
**Merge commit:** [c20efec139fd](https://github.com/teqplay/vesselvoyage-backend/commit/c20efec139fd)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Leon Joosse, Former user
**Source Branch:** [SPV-2185-real-data-scenario-testing](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2185-real-data-scenario-testing)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-02T07:33:04.302633+00:00
**Status:** MERGED

* Adjusted test class so it is more clear what they test
* Moved the base functionality of the testing classes to an abstract one so they can be reused
* Added dsl builders for creating visits and voyages
* Added a new scenario testing class with some dummy code to test the dsl like visits and voyages
* Added a test scenario covering a basic visit with berth stops
* Adjusted code so it is easier to test with
* Added a new test case
* Adjusted testing scenario to match actual expected outcome


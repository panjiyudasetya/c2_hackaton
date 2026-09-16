---
id: github:teqplay/vesselvoyage-backend:issue:301
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 301
title: Spv-2202 Fix Visit Confirming
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/301
labels: []
explicit_links: []
---
# Issue #301: Spv-2202 Fix Visit Confirming

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/301  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [48e5ea27792e...1deda6b7aef5](https://github.com/teqplay/vesselvoyage-backend/compare/48e5ea27792e...1deda6b7aef5)
**Merge commit:** [1deda6b7aef5](https://github.com/teqplay/vesselvoyage-backend/commit/1deda6b7aef5)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Leon Joosse
**Source Branch:** [fix-visit-confirming](https://github.com/teqplay/vesselvoyage-backend/tree/fix-visit-confirming)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-30T09:02:55.271891+00:00
**Status:** MERGED

* Fixed an issue where confirming visits wouldn't work correctly when the berth has a sub-port as their first port and cases where ids or unlocodes were inconsistently provided
* Adjusted test scenarios to correctly confirm
* Added tests to ensure the main port is always resolved via unlocode or id


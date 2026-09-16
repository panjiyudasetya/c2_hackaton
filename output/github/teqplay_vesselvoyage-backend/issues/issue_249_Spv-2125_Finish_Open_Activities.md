---
id: github:teqplay/vesselvoyage-backend:issue:249
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 249
title: Spv-2125 Finish Open Activities
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/249
labels: []
explicit_links: []
---
# Issue #249: Spv-2125 Finish Open Activities

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/249  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [7a4ea9d2ea15...fe296056071c](https://github.com/teqplay/vesselvoyage-backend/compare/7a4ea9d2ea15...fe296056071c)
**Merge commit:** [fe296056071c](https://github.com/teqplay/vesselvoyage-backend/commit/fe296056071c)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Leon Joosse
**Source Branch:** [SPV-2125-finish-open-activities](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2125-finish-open-activities)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-06-07T11:41:09.712192+00:00
**Status:** MERGED

* Adjusted EOSP end event processing when finishing a visit to also end all possible ongoing stops and area activities
* Changed the test cases to ensure the new fallback flag is set on the end location time when the EOSP end event is used


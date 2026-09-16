---
id: github:teqplay/vesselvoyage-backend:issue:212
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 212
title: 'Spv-2076: Implement Merging V2'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/212
labels: []
explicit_links:
- jira:SPV-2076
- github:teqplay/vesselvoyage-backend:issue:222
- github:teqplay/vesselvoyage-backend:issue:220
---
# Issue #212: Spv-2076: Implement Merging V2

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/212  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [7086b3e63ad4...369785c1b121](https://github.com/teqplay/vesselvoyage-backend/compare/7086b3e63ad4...369785c1b121)
**Merge commit:** [369785c1b121](https://github.com/teqplay/vesselvoyage-backend/commit/369785c1b121)
**Author:** Former user
**Reviewers:** Leon Joosse, Darius Wattimena
**Approvers:** Leon Joosse
**Source Branch:** [SPV-2076-merging-v2-logic-implement-v2](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2076-merging-v2-logic-implement-v2)
**Destination Branch:** [SPV-2076-merging-v2-logic](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2076-merging-v2-logic)
**Closed On:** 2024-04-17T10:20:32.484410+00:00
**Status:** MERGED

To preface this.. looking at the total lines changed it seems like a huge PR. It’s mostly about a filename change that’s not recognized as such, see also:  
[https://github.com/teqplay/vesselvoyage-backend/issues/222#comment-493049721](https://github.com/teqplay/vesselvoyage-backend/issues/222#comment-493049721) 
Apart from that file and ignoring the content that was moved from `EntriesMergeV1ServiceTest`, these changes remain:
```
 api/src/main/kotlin/nl/teqplay/vesselvoyage/model/v2/NewEntry.kt                   |    9 +-
 api/src/main/kotlin/nl/teqplay/vesselvoyage/model/v2/NewVisit.kt                   |    6 +-
 api/src/main/kotlin/nl/teqplay/vesselvoyage/model/v2/NewVoyage.kt                  |    7 +-
 src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewESoFDataSource.kt            |    5 +
 src/main/kotlin/nl/teqplay/vesselvoyage/service/merge/EntriesMergeService.kt       |    9 +-
 src/main/kotlin/nl/teqplay/vesselvoyage/service/merge/EntriesMergeV1Service.kt     |   12 +-
 src/main/kotlin/nl/teqplay/vesselvoyage/service/merge/EntriesMergeV2Service.kt     |  169 ++++++++++
 src/test/kotlin/nl/teqplay/vesselvoyage/service/merge/EntriesMergeV1ServiceTest.kt |   64 ++++
 src/test/kotlin/nl/teqplay/vesselvoyage/service/merge/EntriesMergeV2ServiceTest.kt |  292 ++++++++++++++++
 9 files changed, 562 insertions(+), 11 deletions(-)
```

The idea behind this PR, and the previous one [https://github.com/teqplay/vesselvoyage-backend/issues/220](https://github.com/teqplay/vesselvoyage-backend/issues/220) , is to reuse as much logic as possible. Reusing most of the tests that were available for V1 as well.
Please contact me if you’d like to go through it together.


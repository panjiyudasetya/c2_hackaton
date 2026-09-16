---
id: github:teqplay/vesselvoyage-backend:issue:209
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 209
title: 'Spv-1983 Api V2: Entry Controller'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/209
labels: []
explicit_links:
- jira:SPV-1983
---
# Issue #209: Spv-1983 Api V2: Entry Controller

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/209  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [8334d0ee31b1...d0438190dfcb](https://github.com/teqplay/vesselvoyage-backend/compare/8334d0ee31b1...d0438190dfcb)
**Merge commit:** [d0438190dfcb](https://github.com/teqplay/vesselvoyage-backend/commit/d0438190dfcb)
**Author:** Leon Joosse
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena, Former user
**Source Branch:** [SPV-1983-api-v2-entries](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1983-api-v2-entries)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-04-16T09:15:07.924390+00:00
**Status:** MERGED

This adds the V2 entries endpoints:
**By id**
```
GET /v2/entry/{id}
POST /v2/entry/ids
[ "visit1", ... ]
```
**By imo**
```
GET /v2/entry/byImo/{imo}
POST /v2/entry/byImo
[
  // using start/end time window
  {
    "imo": "12345678",
    "start": ..,
    "end": ..
  },
  // using last X number of entries
  {
    "imo": "12345678",
    "last": 10
  }
]
```

Noteworthy:
* Add mapstruct dependency \(1.5.5.Final\)
* Extend Visit and Voyage from an Entry interface
* Add mapstruct mapper for internal → api objects


---
id: github:teqplay/vesselvoyage-backend:issue:217
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 217
title: Spv-1983 Api V2 Visits
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/217
labels: []
explicit_links:
- jira:SPV-1983
---
# Issue #217: Spv-1983 Api V2 Visits

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/217  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [4b857f887603...8f3bfe9ccf71](https://github.com/teqplay/vesselvoyage-backend/compare/4b857f887603...8f3bfe9ccf71)
**Merge commit:** [8f3bfe9ccf71](https://github.com/teqplay/vesselvoyage-backend/commit/8f3bfe9ccf71)
**Author:** Leon Joosse
**Reviewers:** Darius Wattimena
**Approvers:** Former user
**Source Branch:** [SPV-1983-api-v2-visits](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1983-api-v2-visits)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-04-24T10:09:55.120111+00:00
**Status:** MERGED

Add visit endpoints
```
GET  /v2/visit/{id}
POST /v2/visit/ids
[ "visit1", "visit2", ... ]
GET  /v2/visit/byImo?start=&end=
GET  /v2/visit/byImo?last=
POST /v2/visit/byImo
[ 
  { "imo": "1234567", "start": "...", "end": "..." },
  { "imo": "1234567", "last": 10 },
]
GET  /v2/visit/byPort?unlocode=&start=&end=
GET  /v2/visit/byPort?pomaId=&start=&end=
POST /v2/visit/byPort
[
  { "unlocode": "NLRTM", "start": "..", "end": ".." },
  { "pomaId": "..", "start": "..", "end": ".." }
]
```

Also refactored request/response classes a bit to make it more generic.


---
id: github:teqplay/vesselvoyage-backend:issue:218
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 218
title: Spv-1983 Api V2 Voyages (Part 1 Of 2)
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/218
labels: []
explicit_links: []
---
# Issue #218: Spv-1983 Api V2 Voyages (Part 1 Of 2)

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/218  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [87dbff68b8f4...7ba4aea8ecf5](https://github.com/teqplay/vesselvoyage-backend/compare/87dbff68b8f4...7ba4aea8ecf5)
**Merge commit:** [7ba4aea8ecf5](https://github.com/teqplay/vesselvoyage-backend/commit/7ba4aea8ecf5)
**Author:** Leon Joosse
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena, Former user
**Source Branch:** [SPV-1983-api-v2-voyages](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1983-api-v2-voyages)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-08-26T07:49:35.769859+00:00
**Status:** MERGED

Add Voyage endpoints
```
GET  /v2/voyage/{id}
POST /v2/voyage/ids
[ "voyage1", "voyage2", ... ]
GET  /v2/voyage/byImo?start=&end=
GET  /v2/voyage/byImo?last=
POST /v2/voyage/byImo
[ 
  { "imo": "1234567", "start": "...", "end": "..." },
  { "imo": "1234567", "last": 10 },
]
```
Endpoints for querying by `origin` and/or `destination` will follow in the next PR. Adding those fields generates some changes that would pollute this PR too much.


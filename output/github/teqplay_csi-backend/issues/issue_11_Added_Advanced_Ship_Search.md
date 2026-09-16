---
id: github:teqplay/csi-backend:issue:11
source: github
type: issue
repo: teqplay/csi-backend
number: 11
title: Added Advanced Ship Search
author: jbugella
state: closed
date: '2025-01-07'
url: https://github.com/teqplay/csi-backend/issues/11
labels: []
explicit_links: []
---
# Issue #11: Added Advanced Ship Search

**Repo:** teqplay/csi-backend  
**URL:** https://github.com/teqplay/csi-backend/issues/11  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-07  
**Closed:** 2025-01-07  

## Description

**Full diff:** [7e9033cf029b...1720cdeb4972](https://github.com/teqplay/csi-backend/compare/7e9033cf029b...1720cdeb4972)
**Merge commit:** [1720cdeb4972](https://github.com/teqplay/csi-backend/commit/1720cdeb4972)
**Author:** Former user
**Reviewers:** Michel Wilson
**Approvers:** Michel Wilson
**Source Branch:** [paginatedShips](https://github.com/teqplay/csi-backend/tree/paginatedShips)
**Destination Branch:** [develop](https://github.com/teqplay/csi-backend/tree/develop)
**Closed On:** 2019-07-19T11:33:48.768768+00:00
**Status:** MERGED

Added `/v1/shipRegister/search/advanced` to be able to have an advanced search on ships from the database.  
  
The frontend is able to create filters and sorts via the following input model:

```
{
  "filters": [
    {
      "fieldType": "TEQPLAY_ID",
      "filter": "IS_NULL",
      "value": {}
    }
  ],
  "sort": [
    {
      "fieldType": "TEQPLAY_ID",
      "sort": "ASCENDING"
    }
  ]
}
```

With an `offset` and `amount` to let the results of ships be paginated.



`fieldType` = any field in the ship model

`filter` = any item from: `IS_NULL, IS_NOT_NULL, EQUALS, NOT_EQUALS, REGEX, LOWER_THAN, LOWER_THAN_EQUALS, GREATER_THAN, GREATER_THAN_EQUALS`

`sort` = any item from: `ASCENDING, DESCENDING`



PS. I also changed the location of some helper functions that were previously in the tickets controller. Felt like it was not logical to have it there, so moved those functions to a helper controller.


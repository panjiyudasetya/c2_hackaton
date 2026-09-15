---
id: github:teqplay/vesselvoyage-backend:issue:338
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 338
title: Spv-2333 Allow Public Calls On Api Endpoints
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/338
labels: []
explicit_links: []
---
# Issue #338: Spv-2333 Allow Public Calls On Api Endpoints

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/338  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [3348e6e186c8...e9c1a6a964ad](https://github.com/teqplay/vesselvoyage-backend/compare/3348e6e186c8...e9c1a6a964ad)
**Merge commit:** [e9c1a6a964ad](https://github.com/teqplay/vesselvoyage-backend/commit/e9c1a6a964ad)
**Author:** Darius Wattimena
**Reviewers:** Michel Wilson, Leon Joosse
**Approvers:** Michel Wilson
**Source Branch:** [SPV-2333-allow-public-calls-on-api-endpoints](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2333-allow-public-calls-on-api-endpoints)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-09-03T15:17:36.932053+00:00
**Status:** MERGED

I first wanted to fix this on the side of the internal/external API, however, cors errors can only be fixed in the target backend themself and fully disabling them and handling them on the internal/external API is not a very nice option


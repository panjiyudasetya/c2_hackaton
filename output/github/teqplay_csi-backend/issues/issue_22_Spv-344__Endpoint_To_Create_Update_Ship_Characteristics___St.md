---
id: github:teqplay/csi-backend:issue:22
source: github
type: issue
repo: teqplay/csi-backend
number: 22
title: 'Spv-344: Endpoint To Create/Update Ship Characteristics & Storing Of Characteristics
  History'
author: jbugella
state: closed
date: '2025-01-07'
url: https://github.com/teqplay/csi-backend/issues/22
labels: []
explicit_links: []
---
# Issue #22: Spv-344: Endpoint To Create/Update Ship Characteristics & Storing Of Characteristics History

**Repo:** teqplay/csi-backend  
**URL:** https://github.com/teqplay/csi-backend/issues/22  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-07  
**Closed:** 2025-01-07  

## Description

**Full diff:** [7eaf78b113de...4d07d69a9968](https://github.com/teqplay/csi-backend/compare/7eaf78b113de...4d07d69a9968)
**Merge commit:** [4d07d69a9968](https://github.com/teqplay/csi-backend/commit/4d07d69a9968)
**Author:** Former user
**Reviewers:** Jos de Jong
**Approvers:** Jos de Jong
**Source Branch:** [feature/SPV-344-synchronize-how-to-keep-calculat](https://github.com/teqplay/csi-backend/tree/feature/SPV-344-synchronize-how-to-keep-calculat)
**Destination Branch:** [develop](https://github.com/teqplay/csi-backend/tree/develop)
**Closed On:** 2021-12-01T08:45:43.603724+00:00
**Status:** MERGED

In a previous PR, [https://github.com/teqplay/csi-backend/issues/22](https://github.com/teqplay/csi-backend/issues/22), ship characteristics were added. Meanwhile the frontend can also display those, but no way to update those values yet. That’s where this PR comes in!

Adding an endpoint to create/update ship characteristics and also storing the change history of that.

\(also removed some dead code paths\)


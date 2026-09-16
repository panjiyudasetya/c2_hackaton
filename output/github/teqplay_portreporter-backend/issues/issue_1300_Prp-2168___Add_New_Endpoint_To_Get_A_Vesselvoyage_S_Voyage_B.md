---
id: github:teqplay/portreporter-backend:issue:1300
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1300
title: 'Prp-2168 : Add New Endpoint To Get A Vesselvoyage''S Voyage By It''S Id. Also
  Extend Vesselvoyagevisit Model With Previousentryid And Nextentryid.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1300
labels: []
explicit_links:
- jira:PRP-2168
---
# Issue #1300: Prp-2168 : Add New Endpoint To Get A Vesselvoyage'S Voyage By It'S Id. Also Extend Vesselvoyagevisit Model With Previousentryid And Nextentryid.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1300  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [e6a68b61059e...e8a04b7512cc](https://github.com/teqplay/portreporter-backend/compare/e6a68b61059e...e8a04b7512cc)
**Merge commit:** [e8a04b7512cc](https://github.com/teqplay/portreporter-backend/commit/e8a04b7512cc)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Darius Wattimena, Shan Minh Nguyen
**Approvers:** Shan Minh Nguyen
**Source Branch:** [feat/PRP-2168/add_vesselvoyage_endpoint_to_retrieve_voyage_by_id](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-2168/add_vesselvoyage_endpoint_to_retrieve_voyage_by_id)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-06-28T13:26:53.332242+00:00
**Status:** MERGED

Changes:
1. Restoring the deleted endpoint \(and its logic\) `/v1/vesselvoyage/voyage/{id}`
2. Extending `VesselVoyageVisit` model with `nextEntryId` and `previousEntryId`.


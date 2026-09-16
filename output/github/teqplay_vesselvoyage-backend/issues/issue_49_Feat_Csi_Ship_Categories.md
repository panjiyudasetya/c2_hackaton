---
id: github:teqplay/vesselvoyage-backend:issue:49
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 49
title: Feat/Csi Ship Categories
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/49
labels: []
explicit_links: []
---
# Issue #49: Feat/Csi Ship Categories

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/49  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [eb794d47c6cd...a43c3e42dc84](https://github.com/teqplay/vesselvoyage-backend/compare/eb794d47c6cd...a43c3e42dc84)
**Merge commit:** [a43c3e42dc84](https://github.com/teqplay/vesselvoyage-backend/commit/a43c3e42dc84)
**Author:** Jos de Jong
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena, Former user
**Source Branch:** [feat/csi_ship_categories](https://github.com/teqplay/vesselvoyage-backend/tree/feat/csi_ship_categories)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-01-31T13:52:07.121948+00:00
**Status:** MERGED

Use the new CSI endpoint to get all ship categories

* load all ship categories from CSI upfront using the new endpoint
* replace method usage of getShipDetailsByIMO by using getShipCategoryByIMO

This is not yet a full move to the CSI ship categories. Still to address in followup PR's:

* Use CSI ShipCategory for the Visit and Voyage query pages
* Change all port/statistics queries into querying a filtered list with imos instead of filtering the query results by category
* Save a copy of the fetched data of platform/poma/CSI on disk, and use that on system load to speed up and be more resilient.



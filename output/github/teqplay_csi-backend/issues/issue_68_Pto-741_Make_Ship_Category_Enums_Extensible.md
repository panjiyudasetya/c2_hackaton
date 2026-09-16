---
id: github:teqplay/csi-backend:issue:68
source: github
type: issue
repo: teqplay/csi-backend
number: 68
title: Pto-741 Make Ship Category Enums Extensible
author: jbugella
state: closed
date: '2025-01-07'
url: https://github.com/teqplay/csi-backend/issues/68
labels: []
explicit_links:
- jira:PTO-741
---
# Issue #68: Pto-741 Make Ship Category Enums Extensible

**Repo:** teqplay/csi-backend  
**URL:** https://github.com/teqplay/csi-backend/issues/68  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-07  
**Closed:** 2025-01-07  

## Description

**Full diff:** [891727455d22...0854c8bf5353](https://github.com/teqplay/csi-backend/compare/891727455d22...0854c8bf5353)
**Merge commit:** [0854c8bf5353](https://github.com/teqplay/csi-backend/commit/0854c8bf5353)
**Author:** Pim van den Toorn
**Reviewers:** Maryam Tavakoli
**Approvers:** Maryam Tavakoli, Pim van den Toorn, Former user
**Source Branch:** [PTO-741-make-ship-category-enums-extensible](https://github.com/teqplay/csi-backend/tree/PTO-741-make-ship-category-enums-extensible)
**Destination Branch:** [develop](https://github.com/teqplay/csi-backend/tree/develop)
**Closed On:** 2024-05-15T07:22:21.092850+00:00
**Status:** MERGED

ShipCategoryV3 is added, a Data Transfer Object version is made of the ShipRegisterInfo, which only holds the ShipCategoryV3. For the DTO a ShipRegisterControllerV2 and a TicketsControllerV2 were made. 
New enums could be added to the ShipCategoryV3 in the future.

* Added ShipRegisterInfoDbObject, ShipCategoryV3, ShipCategoriesV3 and ShipRegisterInfoV3DTO, added ShipCategoryV2.toV3\(\)
* Added ShipCategoryV3 to the original ShipCategories, removed the ShipCategoriesV3, added UNKNOWN to ShipCategoryV3 and made it the JsonEnumDefaultValue, added ShipCategoryV3 to the ShipFieldType
* Deleted the ShipRegisterInfoDbObject, added a function to mask the ShipCategoryV3 for the old endpoint, added \_id to DTO and removed V3 from the name
* Added ShipRegisterControllerV2 and the extension, masked all outputs on the V1, toDTO on every endpoint in V2,
* Removed teqplayId from ShipIdentifiers, removed ShipRegisterDisabledController
* Split the TicketsController and -service into V1 and V2, with V2 using the ShipRegisterInfoDTO


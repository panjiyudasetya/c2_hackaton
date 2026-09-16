---
id: github:teqplay/csi-backend:issue:73
source: github
type: issue
repo: teqplay/csi-backend
number: 73
title: Release 28-08-2024
author: jbugella
state: closed
date: '2025-01-07'
url: https://github.com/teqplay/csi-backend/issues/73
labels: []
explicit_links: []
---
# Issue #73: Release 28-08-2024

**Repo:** teqplay/csi-backend  
**URL:** https://github.com/teqplay/csi-backend/issues/73  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-07  
**Closed:** 2025-01-07  

## Description

**Full diff:** [62d6d480be47...f53dea79a7a6](https://github.com/teqplay/csi-backend/compare/62d6d480be47...f53dea79a7a6)
**Merge commit:** [f53dea79a7a6](https://github.com/teqplay/csi-backend/commit/f53dea79a7a6)
**Author:** Jamie de Leest
**Reviewers:** 
**Approvers:** 
**Source Branch:** [develop](https://github.com/teqplay/csi-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/csi-backend/tree/master)
**Closed On:** 2024-08-28T08:30:07.132800+00:00
**Status:** MERGED

* removing kmongo from csi
* Added ShipRegisterInfoDbObject, ShipCategoryV3, ShipCategoriesV3 and ShipRegisterInfoV3DTO, added ShipCategoryV2.toV3\(\)
* Added ShipCategoryV3 to the original ShipCategories, removed the ShipCategoriesV3, added UNKNOWN to ShipCategoryV3 and made it the JsonEnumDefaultValue, added ShipCategoryV3 to the ShipFieldType
* Deleted the ShipRegisterInfoDbObject, added a function to mask the ShipCategoryV3 for the old endpoint, added \_id to DTO and removed V3 from the name
* Added ShipRegisterControllerV2 and the extension, masked all outputs on the V1, toDTO on every endpoint in V2,
* Removed teqplayId from ShipIdentifiers, removed ShipRegisterDisabledController
* Split the TicketsController and -service into V1 and V2, with V2 using the ShipRegisterInfoDTO
* Added ShipCategoryV3DTO and the conversion to and from the db version
* Removed TicketPublicDTO and the accompanying controller
* Validate IMO and MMSI on ticket completion
    Generate Tickets For invalid IMOs and MMSIs

* added a duplicate imo check to ship validation
    enforced validation in ShipRegisterInfoService

* Applied maurice feedback INVALID\_DATA source instead of INVALID\_MMSI and INVALID\_IMO sources
* Applied feedback maurice/ richard changes postConstruct to and endpoint for manual use
* allow for the TEU and classification to be edited by the user


---
id: github:teqplay/csi-backend:issue:6
source: github
type: issue
repo: teqplay/csi-backend
number: 6
title: Added Platform Compatible /Ship/Static Endpoints
author: jbugella
state: closed
date: '2025-01-07'
url: https://github.com/teqplay/csi-backend/issues/6
labels: []
explicit_links: []
---
# Issue #6: Added Platform Compatible /Ship/Static Endpoints

**Repo:** teqplay/csi-backend  
**URL:** https://github.com/teqplay/csi-backend/issues/6  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-07  
**Closed:** 2025-01-07  

## Description

**Full diff:** [33c4deae1acd...265984551e4a](https://github.com/teqplay/csi-backend/compare/33c4deae1acd...265984551e4a)
**Merge commit:** [265984551e4a](https://github.com/teqplay/csi-backend/commit/265984551e4a)
**Author:** Former user
**Reviewers:** Michel Wilson, Vasyl Pidlisniak
**Approvers:** Michel Wilson
**Source Branch:** [shiptypesCompatible](https://github.com/teqplay/csi-backend/tree/shiptypesCompatible)
**Destination Branch:** [develop](https://github.com/teqplay/csi-backend/tree/develop)
**Closed On:** 2024-08-26T07:49:41.606315+00:00
**Status:** MERGED

The following endpoints from the platform to request static ship info have been added:

* **GET**`/ship/static` Retrieve the static ship information for all ships known by the platform
* **GET**`/ship/static/{shipImo}` Retrieve the static ship information for specific IMO number
* **POST**`/ship/static/imolist` Retrieve the static ship information for the provided list of IMO's
* **GET**`/ship/static/search` Find static ship information by IMO or name

Two endpoints however, haven’t been added:

* **POST**`/ship/static/add` Create a new StaticShipInfo
* **PUT**`/ship/static/{shipMmsi}` Update \(overwrite all values\) an existing Ship Information object based on AIS inputs



The `/ship/static/add` endpoint hasn’t been added because it would most likely break when used in parallel with the CSI endpoint to add ships.

The `/ship/static/{shipMmsi}` hasn’t been added because it will defeat the purpose of having tickets to change fields on ship info. However, maybe this could be an input to create tickets when changes in fields are detected. @{5ac28650c6c77f18e6de9696} , could that maybe be an automatic resource as well?


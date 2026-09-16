---
id: github:teqplay/portreporter-backend:issue:797
source: github
type: issue
repo: teqplay/portreporter-backend
number: 797
title: Portbase
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/797
labels: []
explicit_links: []
---
# Issue #797: Portbase

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/797  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [3f7ac544c54c...910b73ca3c86](https://github.com/teqplay/portreporter-backend/compare/3f7ac544c54c...910b73ca3c86)
**Merge commit:** [910b73ca3c86](https://github.com/teqplay/portreporter-backend/commit/910b73ca3c86)
**Author:** Former user
**Reviewers:** Shravan Shetty, Joost Laurman
**Approvers:** Shravan Shetty
**Source Branch:** [portbase](https://github.com/teqplay/portreporter-backend/tree/portbase)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2024-08-26T07:49:41.400239+00:00
**Status:** MERGED

* Add support for Portbase
* Added saving created orders for Portbase
* Prune old files
* Create orders: added documentation, improvements & disable portbase for now
* Portcall Order: Model improvements
* Added precondition checks for user permissions & added dependent on ship to model
* Ignore linked agency checks if user role equals ADMIN
* Add addon feature to company level & some small improvements



There are some TODOs still for the Portbase integration, this is both because the patching of visits in Portbase doesn’t work yet and there is still an open point that has already been asked in an email.


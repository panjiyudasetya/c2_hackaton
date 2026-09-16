---
id: github:teqplay/portreporter-backend:issue:893
source: github
type: issue
repo: teqplay/portreporter-backend
number: 893
title: Smartfleet Company
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/893
labels: []
explicit_links: []
---
# Issue #893: Smartfleet Company

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/893  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [2b88f677ad08...493c83f596b1](https://github.com/teqplay/portreporter-backend/compare/2b88f677ad08...493c83f596b1)
**Merge commit:** [493c83f596b1](https://github.com/teqplay/portreporter-backend/commit/493c83f596b1)
**Author:** Former user
**Reviewers:** Shravan Shetty
**Approvers:** Shravan Shetty
**Source Branch:** [smart-fleet-company](https://github.com/teqplay/portreporter-backend/tree/smart-fleet-company)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2024-08-26T07:49:40.327014+00:00
**Status:** MERGED

Related card:  
[https://trello.com/c/yuG7WZQg/8593-24-add-the-type-smartfleet-or-portcall-to-the-company-information](https://trello.com/c/yuG7WZQg/8593-24-add-the-type-smartfleet-or-portcall-to-the-company-information)
This PR adds a SmartFleet company and contains the following:
* user roles for `SMART_FLEET_ADMIN` and `SMART_FLEET_USER`
* auth intercepting on those roles
* the SmartFleet company itself, and links to this on the `UserProfile.smartFleetIds`
* a controller to perform actions on a SmartFleet company
* on the `Company` level a field is added that actually determines if it’s a portcall or SmartFleet type, namely in the `Company.kind` field. To do this a `CompanyKind` enum is added, which is either `PORTCALL` or `SMART_FLEET`


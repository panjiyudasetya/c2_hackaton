---
id: github:teqplay/portreporter-backend:issue:923
source: github
type: issue
repo: teqplay/portreporter-backend
number: 923
title: 5.0.0 Merge
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/923
labels: []
explicit_links: []
---
# Issue #923: 5.0.0 Merge

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/923  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [fed37e2dc087...9a02ca8e0a59](https://github.com/teqplay/portreporter-backend/compare/fed37e2dc087...9a02ca8e0a59)
**Merge commit:** [9a02ca8e0a59](https://github.com/teqplay/portreporter-backend/commit/9a02ca8e0a59)
**Author:** Shravan Shetty
**Reviewers:** Joaquin Marquez Bugella
**Approvers:** Former user
**Source Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/portreporter-backend/tree/master)
**Closed On:** 2021-08-03T10:06:41.417354+00:00
**Status:** MERGED

* update: hybrid user
* frontend requested this DashboardColumn type to be a String instead of an enum so they can do frontend changes without backend changes
* give agencies, terminals, shippingCompanies, smartFLeetCompanies in different properties
* \[https://trello.com/c/s7LpTCoU\] extend PortCall search by adding a search all Active Portcalls at a certain timestamp and Port
* update: return usermetadata in user controllers
* fix: ignore portcall.finished for all ports
* \[https://trello.com/c/n7iqUZUt\] : Default case \(NoDuration --> PT3H\) included.
* \[https://trello.com/c/n7iqUZUt\] UnitTests for implicit duration in PORT\_ETA\_OFFICIAL\_REPORTING\_CONFIGURABLE
* Support Column Configuration per fleet
* Manage SmartFleet company fleet filters
* De-duplicate endpoints
* SmartFleet fleet settings: enable/disable predictions
* admin can read all shipRegistries
* SmartFleet: process anchorages
* SmartFleet: CSV export of Visits and Voyages
* SmartFleet: also expose fleet settings
* fix-unitTest: additional testCases for the method UserProfile.reMapRoles\(\)
* Dashboard configuration: improve swagger for optional fleetId
* \[https://trello.com/c/ES1YDyrj\] logging any CUD operations via the API on Subscriptions and SubscriptionProfiles



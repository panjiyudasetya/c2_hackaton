---
id: github:teqplay/portreporter-backend:issue:964
source: github
type: issue
repo: teqplay/portreporter-backend
number: 964
title: Bugfix/Spv-221 Listing Of Fleets Is Slow
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/964
labels: []
explicit_links:
- jira:SPV-221
---
# Issue #964: Bugfix/Spv-221 Listing Of Fleets Is Slow

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/964  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [0f0d01b217bf...986c7d772a74](https://github.com/teqplay/portreporter-backend/compare/0f0d01b217bf...986c7d772a74)
**Merge commit:** [986c7d772a74](https://github.com/teqplay/portreporter-backend/commit/986c7d772a74)
**Author:** Former user
**Reviewers:** Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [SPV-221-listing-of-fleets-is-slow](https://github.com/teqplay/portreporter-backend/tree/SPV-221-listing-of-fleets-is-slow)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2021-10-13T08:37:38.784328+00:00
**Status:** MERGED

Jira issue:  
[https://teqplaybv.atlassian.net/browse/SPV-221](https://teqplaybv.atlassian.net/browse/SPV-221)

In SmartFleet the `fleet.relevantVoyages.shipIds` is being deprecated, and this nested field is moved to the root object when fetching a specific fleet.

The actual removal of the deprecated code will be done once the frontend supports this new field.


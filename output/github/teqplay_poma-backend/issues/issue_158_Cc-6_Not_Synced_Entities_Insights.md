---
id: github:teqplay/poma-backend:issue:158
source: github
type: issue
repo: teqplay/poma-backend
number: 158
title: Cc-6 Not Synced Entities Insights
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/158
labels: []
explicit_links: []
---
# Issue #158: Cc-6 Not Synced Entities Insights

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/158  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [0cb2f1d8917d...6821d1ef8f13](https://github.com/teqplay/poma-backend/compare/0cb2f1d8917d...6821d1ef8f13)
**Merge commit:** [6821d1ef8f13](https://github.com/teqplay/poma-backend/commit/6821d1ef8f13)
**Author:** Pim van den Toorn
**Reviewers:** Darius Wattimena, Joost Dambrink
**Approvers:** Darius Wattimena, Pim van den Toorn
**Source Branch:** [CC-6-which-not-synced](https://github.com/teqplay/poma-backend/tree/CC-6-which-not-synced)
**Destination Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Closed On:** 2024-09-23T09:58:20.145566+00:00
**Status:** MERGED

The sync endpoints will now return the differences and only synchronize if specified through a request parameter.
Added a dedicated difference endpoint.
Removed whitelist syncing as the whitelist is being deprecated.

* Added RestTemplate.get and .post functions
* Added endpoint to check the differences with another database
* Changed: when updating a model, also update source and sourceType instead of ignoring the new version
* Default to only show the difference when syncing, split the difference into port- and portInfraDifferences, added differences for not in local or not in other database
* Prints the source if it's an illegal source
* getAll in the differences now has validated = null to actually get all
* Removed the whitelist syncing, as the whitelist is being integrated into port
* Added comments and changed the boolean onlyDifference to synchronize in the SyncController
* Now deletes local entries on sync if they're not in the response, added name to InfrastructureModel


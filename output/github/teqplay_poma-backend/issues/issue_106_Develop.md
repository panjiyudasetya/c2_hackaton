---
id: github:teqplay/poma-backend:issue:106
source: github
type: issue
repo: teqplay/poma-backend
number: 106
title: Develop
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/106
labels: []
explicit_links: []
---
# Issue #106: Develop

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/106  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [db2bf668522e...d595352423ad](https://github.com/teqplay/poma-backend/compare/db2bf668522e...d595352423ad)
**Merge commit:** [d595352423ad](https://github.com/teqplay/poma-backend/commit/d595352423ad)
**Author:** Maryam Tavakoli
**Reviewers:** Wouter Naloop, Darius Wattimena
**Approvers:** Wouter Naloop, Former user
**Source Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/poma-backend/tree/master)
**Closed On:** 2023-10-20T08:38:03.037346+00:00
**Status:** MERGED

* SPV-1585: Add a simple way of adding the 3 envisioned databases \(original, merged and external\) for the world of ports data.
* SPV-1585: make the custom area ports non unique
* SPV-1585: ktlint
* SPV-1625: initial simple merge strategy
* removing the database variables which are there for copy paste purposes
* SPV-1625: change the merge logic to accept any difference in percentage of more than 50% overlap as the same, change all the forgotten annotations to the correct ones, set the base db names in the properties
* SPV-1625: fix the overlap method
* SPV-1625: WIP: new mergestrategy
* SPV-1625: Make the process of the merges more testable, include tests, give the list of locations names that are relatable to the real world
* SPV-1585: typo
* SPV-1625: add an override option from the database to always take Teqplay ports if we put them in the whitelist
* SPV-1625: corrected the tags and endpoints of the allmodels controller and whitelist controllers, Made the mergeModels use the generic T, added unit tests for the overlap code
* SPV-1625: clarifying my comments a bit
* SPV-1625: reducing the work by only calculating the intersecting area once. This is important because we don't control how many points that intersection is created with, so it could be a heavy operation
* SPV-1585: resolve merge conflicts
* add an endpoint to detect overlapping berths for a port or the entire world
* use the percentage overlap instead of the union areas method
* make sure every entry is there only once
* adding the berth itself also to the list of overlaps, otherwise you don't know with which berth it overlaps
* convert world of port model to poma model
* convert world of port model to poma model
* wop data conversion
* wop data conversion
* Make sure the scheduled tasks play nicely with the new database selection code
* wop data conversion
* wop data conversion
* ktlint
* add merge EventListener
* Changing names
* Changing names
* remove the security role for ROLE\_EXTERNAL\_VIEW
* changing scheduled time
* SPV-1627: filter out duplicates from the teqplay models db, and use the externalModels ones
* SPV-1627: remove unnecessary parenthesis
* SPV-1627: woops wrong set operation
* SPV-1627: don't insert if the list is empty
* SPV-1627: remove the rights from the statistics endpoints
* SPV-1627: ktlint
* SPV-1627: remove the access check and use the datasource you have access to
* add log history and slack notification add user role for scheduled job some property update in wop data
* conflict on application.properties
* apply reviews
* ktlint!
* extract anchorage info from berth and terminal in wop data
* convert anchorages from WOP and merging
* apply reviews
* Ktlint!
* add comments
* search with id instead of uniqueId
* convert terminals as anchorages
* remove merging anchorages
* set user validated to true
* merge conflict
* ktlint
* fix the global controller
* imports...
* fix terminalservice test
* properties
* fix authentication error and change merging strategy
* change merging strategy fix authentication error fix percentageAreaOverlap null pointer exception
* test failure
* revert
* revert
* merge conflict
* Merged develop with branch and fixed merge conflicts with unit tests. First version of triggers for setting main port of berths and terminals.
* KTlint commit of shame. Forgetfullness.
* add endpoints to manually update and convert data from WOP also increase the memory due to the heap memory shortage
* add extra regex escape
* ktlint did not like my quick fix
* Refactored unit tests and feedback implemented.
* DEV-251: Updated CI script to make use of new namespace on develop and sandbox env
* apply reviews
* revert namespace changes
* changing conversion order after all wop raw data persisted, then start the conversion
* more logging messages added to slack. scheduled job user's role changed.
* Fixed merging develop into branch and fixed unit tests.
* KTLint commit of shame.


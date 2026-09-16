---
id: github:teqplay/portreporter-backend:issue:1261
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1261
title: Feature/Prp-1492 Added Timestamp Check For Pilotavailability Events
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1261
labels: []
explicit_links: []
---
# Issue #1261: Feature/Prp-1492 Added Timestamp Check For Pilotavailability Events

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1261  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [8ffdb96c4540...dc89b1526de5](https://github.com/teqplay/portreporter-backend/compare/8ffdb96c4540...dc89b1526de5)
**Merge commit:** [dc89b1526de5](https://github.com/teqplay/portreporter-backend/commit/dc89b1526de5)
**Author:** Shan Minh Nguyen
**Reviewers:** Joost Laurman, Wouter Naloop, Joaquin Marquez Bugella
**Approvers:** Former user
**Source Branch:** [feature/PRP-1492_added_timestamp_check_for_pilotavailability_events](https://github.com/teqplay/portreporter-backend/tree/feature/PRP-1492_added_timestamp_check_for_pilotavailability_events)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-05-05T08:39:32.767266+00:00
**Status:** MERGED

* Added a timestamp to the existing equals check when comparing PilotAvailabilityChange objects so same subject in messages but different timestamp can fire notifications.
* Fixed a unit test, filled in timestamp to make unit test work as intended.


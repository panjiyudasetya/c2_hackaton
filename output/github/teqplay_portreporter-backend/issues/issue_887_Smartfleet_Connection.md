---
id: github:teqplay/portreporter-backend:issue:887
source: github
type: issue
repo: teqplay/portreporter-backend
number: 887
title: Smartfleet Connection
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/887
labels: []
explicit_links: []
---
# Issue #887: Smartfleet Connection

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/887  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [4e018c19015a...d5d88e808963](https://github.com/teqplay/portreporter-backend/compare/4e018c19015a...d5d88e808963)
**Merge commit:** [d5d88e808963](https://github.com/teqplay/portreporter-backend/commit/d5d88e808963)
**Author:** Former user
**Reviewers:** Shravan Shetty, Wouter Naloop
**Approvers:** Shravan Shetty
**Source Branch:** [smart-fleet-connection](https://github.com/teqplay/portreporter-backend/tree/smart-fleet-connection)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2021-05-06T13:08:21.491609+00:00
**Status:** MERGED

Related card:  
[https://trello.com/c/K3cqzZSH/8477-86-replace-mock-endpoints-in-portreporter-with-real-requests-to-smartfleet-platform-etc](https://trello.com/c/K3cqzZSH/8477-86-replace-mock-endpoints-in-portreporter-with-real-requests-to-smartfleet-platform-etc)

This PR removes the mock data from the endpoints and makes real requests to SmartFleet and platform to fetch the data.

Lot’s of conversion happens between the SmartFleet data and what is exposed to a PortReporter user, this is mainly to extend imo and unlocode info with full models gathered from platform.


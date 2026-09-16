---
id: github:teqplay/portreporter-backend:issue:1291
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1291
title: Prp-2099 Make Sf Notifications Send Messages Per Port On Events
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1291
labels: []
explicit_links: []
---
# Issue #1291: Prp-2099 Make Sf Notifications Send Messages Per Port On Events

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1291  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [40a8f96e43f4...79096f48d628](https://github.com/teqplay/portreporter-backend/compare/40a8f96e43f4...79096f48d628)
**Merge commit:** [79096f48d628](https://github.com/teqplay/portreporter-backend/commit/79096f48d628)
**Author:** Shan Minh Nguyen
**Reviewers:** Joost Laurman, Wouter Naloop, Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [feature/PRP-2099_make_sf_notifications_send_message_every_port_per_sf_event](https://github.com/teqplay/portreporter-backend/tree/feature/PRP-2099_make_sf_notifications_send_message_every_port_per_sf_event)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-06-21T07:17:57.694280+00:00
**Status:** MERGED

These changes will make it so that each SF event will send 1 to N notifications depending on the ports attached to the event.  
In case of anchor up/down this is the case for now as we are looking through poma and then fetching possible 1 to N ports.


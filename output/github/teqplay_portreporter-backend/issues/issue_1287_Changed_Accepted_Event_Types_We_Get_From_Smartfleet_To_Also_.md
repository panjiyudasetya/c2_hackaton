---
id: github:teqplay/portreporter-backend:issue:1287
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1287
title: Changed Accepted Event Types We Get From Smartfleet To Also Include The Portataatdevent
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1287
labels: []
explicit_links: []
---
# Issue #1287: Changed Accepted Event Types We Get From Smartfleet To Also Include The Portataatdevent

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1287  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [01011d1f335a...d026781553cb](https://github.com/teqplay/portreporter-backend/compare/01011d1f335a...d026781553cb)
**Merge commit:** [d026781553cb](https://github.com/teqplay/portreporter-backend/commit/d026781553cb)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop, Joaquin Marquez Bugella
**Approvers:** Wouter Naloop
**Source Branch:** [new_area_monitor_events_prep](https://github.com/teqplay/portreporter-backend/tree/new_area_monitor_events_prep)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-06-26T08:37:07.600401+00:00
**Status:** MERGED

This change is needed as the new AreaMonitor doesn’t create `ExtendedTeqplayLocationBasedEvent` anymore but just `PortAtaAtdEvent`.


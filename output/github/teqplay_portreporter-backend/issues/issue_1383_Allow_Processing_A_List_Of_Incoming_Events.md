---
id: github:teqplay/portreporter-backend:issue:1383
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1383
title: Allow Processing A List Of Incoming Events
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1383
labels: []
explicit_links: []
---
# Issue #1383: Allow Processing A List Of Incoming Events

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1383  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [d88ad3de9fa4...d5c0ad34c8c5](https://github.com/teqplay/portreporter-backend/compare/d88ad3de9fa4...d5c0ad34c8c5)
**Merge commit:** [d5c0ad34c8c5](https://github.com/teqplay/portreporter-backend/commit/d5c0ad34c8c5)
**Author:** Michel Wilson
**Reviewers:** Darius Wattimena, Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [event-list](https://github.com/teqplay/portreporter-backend/tree/event-list)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2024-09-10T13:27:02.441404+00:00
**Status:** MERGED

This adds the ability to deserialize a list of incoming events. We need to have this functionality to be able to better handle portcalls for the Schelde ports: in portreporter-monitor it is sometimes hard to determine to which portcall we should attribute an event, if the true destination is not known or does not match any of the events generated. Portreporter should be able to make a more informed decision, and this process is going to be much easier if all the events arrive as a group. This is the first step needed in this process.


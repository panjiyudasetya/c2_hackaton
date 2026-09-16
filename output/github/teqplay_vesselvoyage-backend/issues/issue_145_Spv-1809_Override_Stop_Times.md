---
id: github:teqplay/vesselvoyage-backend:issue:145
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 145
title: Spv-1809 Override Stop Times
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/145
labels: []
explicit_links: []
---
# Issue #145: Spv-1809 Override Stop Times

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/145  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [bd64f694542a...03f40d28bd02](https://github.com/teqplay/vesselvoyage-backend/compare/bd64f694542a...03f40d28bd02)
**Merge commit:** [03f40d28bd02](https://github.com/teqplay/vesselvoyage-backend/commit/03f40d28bd02)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [SPV-1809_override_stop_times](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1809_override_stop_times)
**Destination Branch:** [SPV-1656_stop_improvements](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1656_stop_improvements)
**Closed On:** 2023-09-26T16:02:45.060702+00:00
**Status:** MERGED

* Save the stop detection info besides the berth event info on a Stop
* Override the stop time when we've matched a berth event to the stop


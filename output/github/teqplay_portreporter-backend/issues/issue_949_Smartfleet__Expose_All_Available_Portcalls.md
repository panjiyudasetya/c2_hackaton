---
id: github:teqplay/portreporter-backend:issue:949
source: github
type: issue
repo: teqplay/portreporter-backend
number: 949
title: 'Smartfleet: Expose All Available Portcalls'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/949
labels: []
explicit_links:
- jira:SPV-98
---
# Issue #949: Smartfleet: Expose All Available Portcalls

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/949  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [41493d9493ff...b03cb2d1cffe](https://github.com/teqplay/portreporter-backend/compare/41493d9493ff...b03cb2d1cffe)
**Merge commit:** [b03cb2d1cffe](https://github.com/teqplay/portreporter-backend/commit/b03cb2d1cffe)
**Author:** Former user
**Reviewers:** Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [SPV-98-expose-all-available-portcalls-in](https://github.com/teqplay/portreporter-backend/tree/SPV-98-expose-all-available-portcalls-in)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2021-09-23T14:07:23.044125+00:00
**Status:** MERGED

Related issue:  
[https://teqplaybv.atlassian.net/browse/SPV-98](https://teqplaybv.atlassian.net/browse/SPV-98)

Previously only the portcalls related to the departure and arrival port were exposed.

This PR changes this to expose all available portcalls instead. It matches the portcalls of a ship to the departure port, arrival port, planned visit or historic visit.


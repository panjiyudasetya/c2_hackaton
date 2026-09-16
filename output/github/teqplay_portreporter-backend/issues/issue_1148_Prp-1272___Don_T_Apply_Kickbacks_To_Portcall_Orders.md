---
id: github:teqplay/portreporter-backend:issue:1148
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1148
title: 'Prp-1272 : Don''T Apply Kickbacks To Portcall Orders.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1148
labels: []
explicit_links:
- jira:PRP-1272
---
# Issue #1148: Prp-1272 : Don'T Apply Kickbacks To Portcall Orders.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1148  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [6b2d3084b8a9...4d849eda5265](https://github.com/teqplay/portreporter-backend/compare/6b2d3084b8a9...4d849eda5265)
**Merge commit:** [4d849eda5265](https://github.com/teqplay/portreporter-backend/commit/4d849eda5265)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [feat/PRP-1272/dont_apply_kickbacks_to_portcall_orders](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-1272/dont_apply_kickbacks_to_portcall_orders)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-09-01T10:40:33.303296+00:00
**Status:** MERGED

Last minute request to exclude the kickback appliance from PORTCALL\_ORDERs.

Meaning correcting the way the kickback is calculated \(by filtering\) and removing unneeded functionality \(for addons management\).


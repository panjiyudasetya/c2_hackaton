---
id: github:teqplay/poma-backend:issue:57
source: github
type: issue
repo: teqplay/poma-backend
number: 57
title: 'Prp-1891 : Adding New Endpoint To Get Ports With Mapped Berths. Additionaly,
  Removed A Blocking And Unused Berth''S Endpoint.'
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/57
labels: []
explicit_links: []
---
# Issue #57: Prp-1891 : Adding New Endpoint To Get Ports With Mapped Berths. Additionaly, Removed A Blocking And Unused Berth'S Endpoint.

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/57  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [0522ff119cf5...dbe7e07c2738](https://github.com/teqplay/poma-backend/compare/0522ff119cf5...dbe7e07c2738)
**Merge commit:** [dbe7e07c2738](https://github.com/teqplay/poma-backend/commit/dbe7e07c2738)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Wouter Naloop, Gavin den Hollander
**Approvers:** Wouter Naloop
**Source Branch:** [feat/PRP-1891/new_endpoint_to_get_ports_with_mapped_berths](https://github.com/teqplay/poma-backend/tree/feat/PRP-1891/new_endpoint_to_get_ports_with_mapped_berths)
**Destination Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Closed On:** 2023-05-08T12:27:09.522080+00:00
**Status:** MERGED

For the purpose, I go through all berths, get their ports UNLOCODE and obtain the full ports by them.
To do this, I’ve got to use BerthService in the PortService, but PortService was already used in BerthService \(for an endpoint that was not used\).
So, to not introduce a circular dependency, I removed second link to introduce the first.


---
id: github:teqplay/portreporter-backend:issue:1297
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1297
title: 'Prp-2133 : Enrich Vesselvoyagevisits With Matching Portcalls (When They Exist)
  And Supply With The New Endpoint /V1/Vesselvoyage/Visitsaroundportcall.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1297
labels: []
explicit_links: []
---
# Issue #1297: Prp-2133 : Enrich Vesselvoyagevisits With Matching Portcalls (When They Exist) And Supply With The New Endpoint /V1/Vesselvoyage/Visitsaroundportcall.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1297  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [d026781553cb...9bd4f6fae7d2](https://github.com/teqplay/portreporter-backend/compare/d026781553cb...9bd4f6fae7d2)
**Merge commit:** [9bd4f6fae7d2](https://github.com/teqplay/portreporter-backend/commit/9bd4f6fae7d2)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Wouter Naloop, Darius Wattimena
**Approvers:** Wouter Naloop
**Source Branch:** [feature/PRP-2133/extend_vessel_voyage_endpoints_with_matching_portcallId](https://github.com/teqplay/portreporter-backend/tree/feature/PRP-2133/extend_vessel_voyage_endpoints_with_matching_portcallId)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-06-27T15:09:14.492636+00:00
**Status:** MERGED

In here I aim to:
1. Provide with the endpoint `/v1/vesselvoyage/visitsAroundPortcall`, similar to `/v1/vesselvoyage/visitsAround`, but centered in a portcallId.
2. Enrich `VesselVoyageVisit` model with linked `PortcallId`.


---
id: github:teqplay/vesselvoyage-backend:issue:270
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 270
title: 'Chore: Upgrade Ais-Engine'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/270
labels: []
explicit_links: []
---
# Issue #270: Chore: Upgrade Ais-Engine

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/270  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [e0e5c22d66db...364e664db56c](https://github.com/teqplay/vesselvoyage-backend/compare/e0e5c22d66db...364e664db56c)
**Merge commit:** [364e664db56c](https://github.com/teqplay/vesselvoyage-backend/commit/364e664db56c)
**Author:** Former user
**Reviewers:** Leon Joosse, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [upgrade-ais-engine](https://github.com/teqplay/vesselvoyage-backend/tree/upgrade-ais-engine)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-08T07:11:22.116288+00:00
**Status:** MERGED

Upgrading ais-engine version, since \(r\)events libraries got an update to handle batch timestamps. Those are required for VesselVoyage to know when it has received a batch of an hour, and it can sort and start processing the data.


---
id: github:teqplay/vesselvoyage-backend:issue:23
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 23
title: Feature/Poma Keycloak
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/23
labels: []
explicit_links: []
---
# Issue #23: Feature/Poma Keycloak

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/23  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [db6e6ff18595...2d67ceeab544](https://github.com/teqplay/vesselvoyage-backend/compare/db6e6ff18595...2d67ceeab544)
**Merge commit:** [2d67ceeab544](https://github.com/teqplay/vesselvoyage-backend/commit/2d67ceeab544)
**Author:** Darius Wattimena
**Reviewers:** Jos de Jong
**Approvers:** Jos de Jong
**Source Branch:** [feature/poma_keycloak](https://github.com/teqplay/vesselvoyage-backend/tree/feature/poma_keycloak)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2021-10-29T10:24:39.778044+00:00
**Status:** MERGED

Adds support to m2m to PoMa via KeyCloak.  
  
Setting `keycloak.enabled` to false will make it use the old `Auth0S2SClientWrapper` instead.


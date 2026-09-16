---
id: github:teqplay/vesselvoyage-backend:issue:15
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 15
title: Feat/Keycloak
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/15
labels: []
explicit_links: []
---
# Issue #15: Feat/Keycloak

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/15  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [fdc69615ad08...3ca51a1a8d9d](https://github.com/teqplay/vesselvoyage-backend/compare/fdc69615ad08...3ca51a1a8d9d)
**Merge commit:** [3ca51a1a8d9d](https://github.com/teqplay/vesselvoyage-backend/commit/3ca51a1a8d9d)
**Author:** Darius Wattimena
**Reviewers:** Jos de Jong
**Approvers:** Jos de Jong
**Source Branch:** [feat/keycloak](https://github.com/teqplay/vesselvoyage-backend/tree/feat/keycloak)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2021-09-23T08:25:01.686694+00:00
**Status:** MERGED

Adds new env variables which should be set:

```
auth-credentials-keycloak-s2s.domain=
auth-credentials-keycloak-s2s.realm=
auth-credentials-keycloak-s2s.audience=
auth-credentials-keycloak-s2s.salt= 
```

DEV already has them set up, and can be run side by side with auth0


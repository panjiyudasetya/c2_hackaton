---
id: github:teqplay/vesselvoyage-backend:pr:848
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 848
title: 'TCC-1171: add Keycloak frontend/user login support'
author: Darius-Wattimena
state: closed
date: '2026-08-07'
merged_at: '2026-08-07'
base_branch: develop
head_branch: TCC-1171-keycloak-frontend-login
url: https://github.com/teqplay/vesselvoyage-backend/pull/848
labels: []
linked_issues: []
explicit_links:
- jira:TCC-1171
---
# PR #848: TCC-1171: add Keycloak frontend/user login support

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/848  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-1171-keycloak-frontend-login`  
**Created:** 2026-08-07  
**Merged:** 2026-08-07  

## Description

Add auth-credentials-keycloak-user alongside Auth0 so the vesselvoyage-frontend Keycloak client can be used for user login, mirroring teqplay/csi-backend#144. Excludes the new auto-config for the revents profile (no UserDataSource bean there) and in tests (the token verifier eagerly fetches JWKS over the network).

## Commits

- `68a9b1f5` **Darius Wattimena** (2026-08-07): TCC-1171: add Keycloak frontend/user login support
  Add auth-credentials-keycloak-user alongside Auth0 so the vesselvoyage-frontend
  Keycloak client can be used for user login, mirroring teqplay/csi-backend#144.
  Excludes the new auto-config for the revents profile (no UserDataSource bean
  there) and in tests (the token verifier eagerly fetches JWKS over the network).

## Reviews

### damon02 — APPROVED (2026-08-07)

LGTM maar ik ben geen backender

### augmentcode[bot] — COMMENTED (2026-08-07)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

## Comments

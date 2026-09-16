---
id: github:teqplay/vesselvoyage-backend:pr:468
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 468
title: DEV-452 Spring Boot 3.1 Upgrade
author: Darius-Wattimena
state: closed
date: '2025-03-31'
merged_at: '2025-04-02'
base_branch: develop
head_branch: DEV-452-spring-boot-3
url: https://github.com/teqplay/vesselvoyage-backend/pull/468
labels: []
linked_issues: []
explicit_links: []
---
# PR #468: DEV-452 Spring Boot 3.1 Upgrade

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/468  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `DEV-452-spring-boot-3`  
**Created:** 2025-03-31  
**Merged:** 2025-04-02  

## Description

I still have to check:
- If all Kubernetes things run
- If all works with the revents profile when running inside a job

But locally everything runs fine.

## Commits

- `2d0471c0` **Darius Wattimena** (2025-03-31): Upgraded VesselVoyage to spring boot 3.1 and a bunch of other libraries to a compatible version
- `2647862e` **Darius Wattimena** (2025-03-31): Upped the version of AisEngine with clients that do work with Spring Boot 3
- `e8ebe493` **Darius Wattimena** (2025-03-31): ktlint
- `21193181` **Darius Wattimena** (2025-03-31): Cleanup
- `9de91e6a` **Darius Wattimena** (2025-04-01): Make sure the clients also make use of the spring boot 3 compatible code
- `a0a68b08` **Darius Wattimena** (2025-04-01): Added spring profile groups
- `d9370c1a` **Darius Wattimena** (2025-04-01): Updated helm values to reflect the new expected profiles to be active

## Reviews

### TeqJoostD — DISMISSED (2025-04-01)

_No comment._

### Darius-Wattimena — COMMENTED (2025-04-01)

_No comment._

### leonjoosse — DISMISSED (2025-04-01)

_No comment._

### TeqJoostD — APPROVED (2025-04-02)

_No comment._

## Review Comments

### TeqJoostD — 2025-04-01 on `src/test/resources/application.properties`

Amazing

### Darius-Wattimena — 2025-04-01 on `src/test/resources/application.properties`

Yes the secret now needs to be a certain amount of bytes long. So do keep in mind once this is merged that you also need to change this

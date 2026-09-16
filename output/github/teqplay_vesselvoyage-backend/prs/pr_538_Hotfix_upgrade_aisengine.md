---
id: github:teqplay/vesselvoyage-backend:pr:538
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 538
title: Hotfix upgrade aisengine
author: Darius-Wattimena
state: closed
date: '2025-06-17'
merged_at: '2025-06-17'
base_branch: develop
head_branch: hotfix-upgrade-aisengine
url: https://github.com/teqplay/vesselvoyage-backend/pull/538
labels: []
linked_issues: []
explicit_links: []
---
# PR #538: Hotfix upgrade aisengine

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/538  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `hotfix-upgrade-aisengine`  
**Created:** 2025-06-17  
**Merged:** 2025-06-17  

## Description

_No description._

## Commits

- `e93f8950` **Darius Wattimena** (2025-06-16): Adjusted ID generation for all stops and encounters to be based on visit id + the id of said activity to avoid id duplication on split stops or encounters
- `060a314b` **Darius Wattimena** (2025-06-16): Adjusted existing test cases to ensure the ids are generated as expected
- `29ba3248` **Darius Wattimena** (2025-06-16): code cleanup
- `8f26169b` **Darius Wattimena** (2025-06-16): Merge pull request #537 from teqplay/develop
  Release 16 Jun 2025
- `f138f81b` **Darius Wattimena** (2025-06-16): Merge branch 'master' into TCC-209-fix-sof-ids
- `976c2d18` **Darius Wattimena** (2025-06-16): Adjust scheduling code to be taking into account all post-processable visits and voyages not only finished
- `24b4d0a1` **Darius Wattimena** (2025-06-17): Merge pull request #536 from teqplay/TCC-209-fix-sof-ids
  TCC-209 fix sof ids
- `1293bf0a` **Darius Wattimena** (2025-06-17): Up direct memory buffer to new default value
- `c6cdfc21` **Darius Wattimena** (2025-06-17): Upgrade AisEngine dependencies to ensure we don't load in netty and instead use Tomcat

## Reviews

### TeqJoostD — APPROVED (2025-06-17)

_No comment._

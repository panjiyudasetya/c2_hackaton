---
id: github:teqplay/vesselvoyage-backend:pr:410
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 410
title: 'SPV-2508: Add previous port area to PTO SOF'
author: leonjoosse
state: closed
date: '2025-02-06'
merged_at: '2025-02-13'
base_branch: develop
head_branch: SPV-2508-sof-previous-port
url: https://github.com/teqplay/vesselvoyage-backend/pull/410
labels: []
linked_issues: []
explicit_links: []
---
# PR #410: SPV-2508: Add previous port area to PTO SOF

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/410  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `SPV-2508-sof-previous-port`  
**Created:** 2025-02-06  
**Merged:** 2025-02-13  

## Description

_No description._

## Commits

- `34f6d55c` **leonj** (2025-02-06): Add previous port area to PTO SOF
- `9e7c31d9` **leonj** (2025-02-11): Merge branch 'develop' into SPV-2508-sof-previous-port
  # Conflicts:
  #	api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/sof/PtoStatementOfFactsView.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGenerator.kt
  #	src/test/kotlin/nl/teqplay/vesselvoyage/ApplicationTest.kt
  #	src/test/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGeneratorTest.kt
- `c7f54cdb` **leonj** (2025-02-11): Fix merge conflicts

## Reviews

### Darius-Wattimena — DISMISSED (2025-02-06)

_No comment._

### Darius-Wattimena — APPROVED (2025-02-11)

LGTM, I accidentally deployed your branches when I frustrated deploying to production, so ignore the failed build

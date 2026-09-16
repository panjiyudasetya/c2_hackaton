---
id: github:teqplay/vesselvoyage-backend:pr:485
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 485
title: 'PRP-2675: Replacing the @Configuration annotation by the correct @AutoConfiguration,
  so to make it autodiscoverable when booting.'
author: jbugella
state: closed
date: '2025-04-24'
merged_at: '2025-04-28'
base_branch: develop
head_branch: maintenance/prp-2675/fixClientConfiguration
url: https://github.com/teqplay/vesselvoyage-backend/pull/485
labels: []
linked_issues: []
explicit_links: []
---
# PR #485: PRP-2675: Replacing the @Configuration annotation by the correct @AutoConfiguration, so to make it autodiscoverable when booting.

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/485  
**State:** closed | **Author:** jbugella  
**Base ← Head:** `develop` ← `maintenance/prp-2675/fixClientConfiguration`  
**Created:** 2025-04-24  
**Merged:** 2025-04-28  

## Description

Otherwise it won't be automatically instantiated when booting the project that want to use the clients.

## Commits

- `7fe1d7b0` **Bugella** (2025-04-24): PRP-2675: Replacing the @Configuration annotation by the correct @AutoConfiguration, so to make it autodiscoverable when booting.

## Reviews

### TeqJoostD — APPROVED (2025-04-28)

_No comment._

### leonjoosse — APPROVED (2025-04-28)

_No comment._

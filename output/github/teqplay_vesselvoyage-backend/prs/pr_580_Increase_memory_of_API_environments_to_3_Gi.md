---
id: github:teqplay/vesselvoyage-backend:pr:580
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 580
title: Increase memory of API environments to 3 Gi
author: Darius-Wattimena
state: closed
date: '2025-07-31'
merged_at: '2025-07-31'
base_branch: develop
head_branch: increase-api-memory
url: https://github.com/teqplay/vesselvoyage-backend/pull/580
labels: []
linked_issues: []
explicit_links: []
---
# PR #580: Increase memory of API environments to 3 Gi

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/580  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `increase-api-memory`  
**Created:** 2025-07-31  
**Merged:** 2025-07-31  

## Description

_No description._

## Commits

- `58a1a163` **Darius Wattimena** (2025-07-31): Increase memory of API environments to 3 Gi

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-31)

## Pull Request Overview

This PR increases the memory allocation for API environments from 2Gi to 3Gi in both development and production configurations. The change addresses resource requirements by updating both memory requests and limits consistently across environments.

- Memory requests increased from 2Gi to 3Gi
- Memory limits increased from 2Gi to 3Gi
- Changes applied to both dev and prod environments

### Reviewed Changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated no comments.

| File | Description |
| ---- | ----------- |
| helm/values.api-prod.yaml | Updates production API memory allocation to 3Gi |
| helm/values.api-dev.yaml | Updates development API memory allocation to 3Gi |

### Joost1991 — APPROVED (2025-07-31)

_No comment._

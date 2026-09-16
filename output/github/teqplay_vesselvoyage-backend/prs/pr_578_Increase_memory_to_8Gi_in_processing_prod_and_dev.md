---
id: github:teqplay/vesselvoyage-backend:pr:578
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 578
title: Increase memory to 8Gi in processing prod and dev
author: Darius-Wattimena
state: closed
date: '2025-07-23'
merged_at: '2025-07-23'
base_branch: develop
head_branch: increase-memory
url: https://github.com/teqplay/vesselvoyage-backend/pull/578
labels: []
linked_issues: []
explicit_links: []
---
# PR #578: Increase memory to 8Gi in processing prod and dev

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/578  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `increase-memory`  
**Created:** 2025-07-23  
**Merged:** 2025-07-23  

## Description

_No description._

## Commits

- `575adc2f` **Darius Wattimena** (2025-07-23): Increase memory to 8Gi in processing prod and dev

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-23)

## Pull Request Overview

This PR increases the memory allocation for the processing service from 6Gi to 8Gi across both production and development environments to address resource constraints or performance requirements.

- Memory requests and limits increased from 6Gi to 8Gi
- Changes applied consistently to both production and development configurations

### Reviewed Changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated no comments.

| File | Description |
| ---- | ----------- |
| helm/values.processing-prod.yaml | Updates memory requests and limits to 8Gi for production environment |
| helm/values.processing-dev.yaml | Updates memory requests and limits to 8Gi for development environment |

### TeqJoostD — APPROVED (2025-07-23)

_No comment._

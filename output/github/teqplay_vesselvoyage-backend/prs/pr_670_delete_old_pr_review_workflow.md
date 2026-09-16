---
id: github:teqplay/vesselvoyage-backend:pr:670
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 670
title: delete old pr review workflow
author: Jamie-de-Leest
state: closed
date: '2025-11-24'
merged_at: '2025-11-25'
base_branch: develop
head_branch: delete-old-pr-review
url: https://github.com/teqplay/vesselvoyage-backend/pull/670
labels: []
linked_issues: []
explicit_links: []
---
# PR #670: delete old pr review workflow

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/670  
**State:** closed | **Author:** Jamie-de-Leest  
**Base ← Head:** `develop` ← `delete-old-pr-review`  
**Created:** 2025-11-24  
**Merged:** 2025-11-25  

## Description

_No description._

## Commits

- `89bcfa01` **Jamie de Leest** (2025-11-24): delete old pr review workflow

## Reviews

### Darius-Wattimena — APPROVED (2025-11-24)

_No comment._

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-11-24)

## Pull request overview

This PR removes the old standalone PR review workflow file (`basic-pr-review.yml`) as the repository has migrated to using a centralized reusable workflow from `teqplay/actions`. The existing `pr-review.yml` file already uses the reusable workflow pattern with a "backend" preset that likely encapsulates the same or similar guidelines that were explicitly defined in the deleted workflow.

### Key Changes
- Deleted the `basic-pr-review.yml` workflow file which contained inline custom guidelines for Kotlin development, testing standards, and code quality requirements
- This cleanup aligns with the repository's use of centralized workflow management via `teqplay/actions/.github/workflows/augment-pr-review.yml@master`

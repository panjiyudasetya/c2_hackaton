---
id: github:teqplay/poma-backend:pr:217
source: github
type: pull_request
repo: teqplay/poma-backend
number: 217
title: 'DEV-1282: Add augment PR review workflow'
author: Jamie-de-Leest
state: closed
date: '2025-11-21'
merged_at: '2025-11-21'
base_branch: develop
head_branch: DEV-1282-add-augment-pr-review
url: https://github.com/teqplay/poma-backend/pull/217
labels: []
linked_issues: []
explicit_links: []
---
# PR #217: DEV-1282: Add augment PR review workflow

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/217  
**State:** closed | **Author:** Jamie-de-Leest  
**Base ← Head:** `develop` ← `DEV-1282-add-augment-pr-review`  
**Created:** 2025-11-21  
**Merged:** 2025-11-21  

## Description

This PR adds the pr-review.yml workflow.

## Commits

- `eed98c4d` **Jamie de Leest** (2025-11-21): DEV-1282: Add pr-review workflow

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-11-21)

## Pull Request Overview

This PR introduces a GitHub Actions workflow for automated PR reviews using Augment's review functionality. The workflow is triggered on pull request creation and synchronization events.

Key changes:
- Adds a new reusable workflow that calls the Augment PR review service with backend guidelines preset
- Configures authentication via repository secrets





---

💡 <a href="/teqplay/poma-backend/new/develop/.github/instructions?filename=*.instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add Copilot custom instructions</a> for smarter, more guided reviews. <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn how to get started</a>.

### github-actions[bot] — COMMENTED (2025-11-21)

Workflow configuration looks good overall. I've identified a few minor issues that should be addressed for better reliability and consistency.

### PimTeqplay — APPROVED (2025-11-21)

_No comment._

## Review Comments

### Copilot — 2025-11-21 on `.github/workflows/pr-review.yml`

The `run-name` key has an extra space after the colon. It should be `run-name:` without a space before the colon for consistency with other YAML keys in this file.
```suggestion
run-name: ${{ github.event.head_commit.message }}
```

### Copilot — 2025-11-21 on `.github/workflows/pr-review.yml`

[nitpick] The workflow references `@master` branch which can lead to unexpected changes if the master branch is updated. Consider pinning to a specific version tag or commit SHA for more predictable and stable behavior (e.g., `@v1.0.0` or `@abc123`).
```suggestion
    uses: teqplay/actions/.github/workflows/augment-pr-review.yml@v1.0.0
```

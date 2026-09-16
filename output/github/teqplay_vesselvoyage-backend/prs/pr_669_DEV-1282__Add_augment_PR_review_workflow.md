---
id: github:teqplay/vesselvoyage-backend:pr:669
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 669
title: 'DEV-1282: Add augment PR review workflow'
author: Jamie-de-Leest
state: closed
date: '2025-11-21'
merged_at: '2025-11-21'
base_branch: develop
head_branch: DEV-1282-add-augment-pr-review
url: https://github.com/teqplay/vesselvoyage-backend/pull/669
labels: []
linked_issues: []
explicit_links: []
---
# PR #669: DEV-1282: Add augment PR review workflow

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/669  
**State:** closed | **Author:** Jamie-de-Leest  
**Base ← Head:** `develop` ← `DEV-1282-add-augment-pr-review`  
**Created:** 2025-11-21  
**Merged:** 2025-11-21  

## Description

This PR adds the pr-review.yml workflow.

## Commits

- `09458a75` **Jamie de Leest** (2025-11-21): DEV-1282: Add pr-review workflow

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-11-21)

## Pull Request Overview

This PR adds a new GitHub Actions workflow (`pr-review.yml`) that integrates Augment's automated PR review functionality into the repository. The workflow is triggered on pull request events (opened and synchronized) and uses a reusable workflow from the `teqplay/actions` repository with a "backend" guidelines preset.

### Key Changes
- New workflow file that calls the Augment PR review reusable workflow
- Configured to trigger on PR open and synchronize events
- Uses backend-specific code review guidelines preset

### github-actions[bot] — COMMENTED (2025-11-21)

Review completed. Found several issues that should be addressed for better workflow reliability and consistency.

### PimTeqplay — APPROVED (2025-11-21)

_No comment._

## Review Comments

### Copilot — 2025-11-21 on `.github/workflows/pr-review.yml`

Secret name case mismatch: The workflow expects the secret `AUGMENT_SESSION_AUTH` (uppercase) but references `secrets.augment_session_auth` (lowercase). GitHub secrets are case-sensitive. This should be `${{ secrets.AUGMENT_SESSION_AUTH }}` to match the secret name on line 14, or the secret should be defined as lowercase if that's the actual secret name in the repository settings.
```suggestion
      AUGMENT_SESSION_AUTH: ${{ secrets.AUGMENT_SESSION_AUTH }}
```

### Copilot — 2025-11-21 on `.github/workflows/pr-review.yml`

The file contains a BOM (Byte Order Mark) character at the beginning. This invisible character can cause parsing issues with some tools. Remove the BOM by re-saving the file with UTF-8 encoding without BOM, or use a command like `sed -i '1s/^\xEF\xBB\xBF//' .github/workflows/pr-review.yml` to strip it.
```suggestion
name: pr-review
```

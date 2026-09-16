---
id: github:teqplay/vesselvoyage-backend:pr:712
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 712
title: Fix deployment
author: Darius-Wattimena
state: closed
date: '2026-02-16'
merged_at: '2026-02-17'
base_branch: develop
head_branch: fix-deployment
url: https://github.com/teqplay/vesselvoyage-backend/pull/712
labels: []
linked_issues: []
explicit_links: []
---
# PR #712: Fix deployment

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/712  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `fix-deployment`  
**Created:** 2026-02-16  
**Merged:** 2026-02-17  

## Description

_No description._

## Commits

- `cbb56c77` **Darius Wattimena** (2026-01-20): Merge pull request #699 from teqplay/develop
  Release 20 Jan 2026
- `c4e047a1` **Joost Dambrink** (2026-01-23): Merge pull request #702 from teqplay/develop
  Release 23/01/2026
- `6774bb57` **Joost Dambrink** (2026-02-10): Merge pull request #707 from teqplay/develop
  Release 04/02/2025
- `ec9b55b8` **Michel Wilson** (2026-02-12): Merge pull request #711 from teqplay/develop
  Release PR for library dependency fix
- `69919f31` **Jamie de Leest** (2026-02-13): chore: update Spring Boot version to 3.4.12 and add Docker builder configuration
- `8e2a2378` **Darius Wattimena** (2026-02-16): Remove unneeded builder

## Reviews

### TeqJoostD — APPROVED (2026-02-16)

_No comment._

### github-actions[bot] — COMMENTED (2026-02-16)

Review completed. The Spring Boot version update from 3.4.4 to 3.4.12 looks straightforward and consistent across all three build files. No suggestions at this time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-02-16)

## Pull request overview

This pull request updates the Spring Boot version from 3.4.4 to 3.4.12 across the multi-module Gradle project to fix deployment issues.

**Changes:**
- Spring Boot version bumped from 3.4.4 to 3.4.12 in all three build.gradle files

### Reviewed changes

Copilot reviewed 2 out of 3 changed files in this pull request and generated no comments.

| File | Description |
| ---- | ----------- |
| build.gradle | Updated spring_boot_version to 3.4.12 in root module |
| api/build.gradle | Updated spring_boot_version to 3.4.12 in api module |
| client/build.gradle | Updated spring_boot_version to 3.4.12 in client module |

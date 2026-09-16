---
id: github:teqplay/poma-backend:pr:214
source: github
type: pull_request
repo: teqplay/poma-backend
number: 214
title: TCC-442 Fix an issue in Poma DATA where the Display Name of a port is always
  blank
author: Jamie-de-Leest
state: closed
date: '2025-09-29'
merged_at: '2025-09-29'
base_branch: develop
head_branch: TCC-442-Fix-an-issue-in-Poma-DATA-where-the-Display-Name-of-a-port-is-always-blank
url: https://github.com/teqplay/poma-backend/pull/214
labels: []
linked_issues: []
explicit_links: []
---
# PR #214: TCC-442 Fix an issue in Poma DATA where the Display Name of a port is always blank

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/214  
**State:** closed | **Author:** Jamie-de-Leest  
**Base ← Head:** `develop` ← `TCC-442-Fix-an-issue-in-Poma-DATA-where-the-Display-Name-of-a-port-is-always-blank`  
**Created:** 2025-09-29  
**Merged:** 2025-09-29  

## Description

_No description._

## Commits

- `6e7744c6` **Jamie de Leest** (2025-09-26): fix: add bulk update method and endpoint to fill display names for WOP ports

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-09-29)

## Pull Request Overview

This PR fixes an issue where the Display Name of ports in Poma DATA is always blank by implementing a bulk update mechanism to populate display names from the main datasource to the external datasource.

- Adds a new `bulkUpdate` method to the `DataSource` class to support bulk MongoDB update operations
- Implements a new service method `fillDisplayNamesForWopPorts` to copy display names from the Teqplay datasource to the external datasource
- Exposes an admin-only endpoint to trigger the display name population process

### Reviewed Changes

Copilot reviewed 3 out of 3 changed files in this pull request and generated 2 comments.

| File | Description |
| ---- | ----------- |
| DataSource.kt | Adds `bulkUpdate` method and necessary imports for bulk update operations |
| PortService.kt | Implements logic to copy display names from main to external datasource using bulk updates |
| PortController.kt | Adds admin endpoint to trigger the display name population process |





---

<sub>**Tip:** Customize your code reviews with copilot-instructions.md. <a href="/teqplay/poma-backend/new/develop/.github?filename=copilot-instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Create the file</a> or <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">learn how to get started</a>.</sub>

### michel-teqplay — APPROVED (2025-09-29)

Looks fine to me :) the "logic inverted" comment Copilot did seems wrong to me. As for the return value, I don't think this matters a lot, as this is likely an endpoint that won't be called very often.

### Darius-Wattimena — APPROVED (2025-09-29)

_No comment._

## Review Comments

### Copilot — 2025-09-29 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortService.kt`

The logic is inverted - ports with blank display names should be updated, not ports that already have display names. This will only update ports that already have display names, which contradicts the PR's purpose of fixing blank display names.

### Copilot — 2025-09-29 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortService.kt`

The function always returns `true` regardless of whether any updates were performed or if the bulk operation succeeded. Consider returning the number of updated records or a more meaningful result.

---
id: github:teqplay/poma-backend:pr:210
source: github
type: pull_request
repo: teqplay/poma-backend
number: 210
title: TCC-403 update getByMainPort endpoint to search by portID and unlocode
author: Jamie-de-Leest
state: closed
date: '2025-09-11'
merged_at: '2025-09-15'
base_branch: develop
head_branch: TCC-403-Update-the-getByMainport-endpoint-to-search-by-unlocode-and-portid
url: https://github.com/teqplay/poma-backend/pull/210
labels: []
linked_issues: []
explicit_links: []
---
# PR #210: TCC-403 update getByMainPort endpoint to search by portID and unlocode

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/210  
**State:** closed | **Author:** Jamie-de-Leest  
**Base ← Head:** `develop` ← `TCC-403-Update-the-getByMainport-endpoint-to-search-by-unlocode-and-portid`  
**Created:** 2025-09-11  
**Merged:** 2025-09-15  

## Description

_No description._

## Commits

- `1dd539f1` **Jamie de Leest** (2025-09-11): fix: update getByMainPort endpoint to search by port ID if available
- `4c930571` **Jamie de Leest** (2025-09-12): chore: update getByMainPort endpoint documentation to include Port ID

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-09-11)

## Pull Request Overview

Updates the `getByMainPort` endpoint to support searching both by port ID and UN/LOCODE, enhancing the search functionality to be more flexible.

### Key Changes
- Modified `getByMainPort` method to first attempt port lookup by UN/LOCODE
- Added fallback logic to search by the original UN/LOCODE string if no port is found
- Enhanced search capability to work with both port IDs and UN/LOCODE values





---

<sub>**Tip:** Customize your code reviews with copilot-instructions.md. <a href="/teqplay/poma-backend/new/develop/.github?filename=copilot-instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Create the file</a> or <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">learn how to get started</a>.</sub>

### TeqJoostD — APPROVED (2025-09-12)

_No comment._

## Review Comments

### TeqJoostD — 2025-09-12 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortService.kt`

Would add a comment that the unlocode can be either an areaId or unlocode and would change the name of the parameter.

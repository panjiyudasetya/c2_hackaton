---
id: github:teqplay/poma-backend:pr:233
source: github
type: pull_request
repo: teqplay/poma-backend
number: 233
title: Mapping status hotfix
author: TeqJoostD
state: closed
date: '2026-02-16'
merged_at: '2026-02-16'
base_branch: develop
head_branch: mapping-status-hotfix
url: https://github.com/teqplay/poma-backend/pull/233
labels: []
linked_issues: []
explicit_links: []
---
# PR #233: Mapping status hotfix

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/233  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `mapping-status-hotfix`  
**Created:** 2026-02-16  
**Merged:** 2026-02-16  

## Description

_No description._

## Commits

- `b2e4af1c` **TeqJoostD** (2026-02-16): fix
- `9db0e653` **TeqJoostD** (2026-02-16): ktlint
- `fe2f4db1` **TeqJoostD** (2026-02-16): fix pt 2

## Reviews

### Darius-Wattimena — APPROVED (2026-02-16)

_No comment._

### github-actions[bot] — COMMENTED (2026-02-16)

Review completed. The changes correctly fix the mapping status aggregation by aligning the field name with MongoDB's output format. The hotfix appears functional and addresses the immediate issue.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-02-16)

## Pull request overview

This PR fixes a bug in the mapping status aggregation functionality where the data model field name didn't match MongoDB's aggregation output format. When MongoDB's `$group` aggregation is used, it always returns the grouped-by field as `_id`, not as a custom field name. This hotfix corrects the field name from `status` to `_id` in the `MappingStatusCount` data class and updates all references accordingly.

**Changes:**
- Fixed `MappingStatusCount` data class to use `_id` field name to match MongoDB aggregation output
- Updated `MappingService` to access the renamed field
- Modified aggregation query in `AbstractPortDatasource` to use string literal instead of `mongoVar` helper

### Reviewed changes

Copilot reviewed 3 out of 3 changed files in this pull request and generated 1 comment.

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/poma/model/aggregation/MappingStatusCount.kt | Renamed field from `status` to `_id` to match MongoDB's aggregation result structure |
| src/main/kotlin/nl/teqplay/poma/feature/mapping/MappingService.kt | Updated field access from `it.status` to `it._id` to match the renamed field |
| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/AbstractPortDatasource.kt | Changed from `mongoVar(Model::expectedMappingStatus)` to string literal `"$expectedMappingStatus"` |





---

💡 <a href="/teqplay/poma-backend/new/develop/.github/instructions?filename=*.instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add Copilot custom instructions</a> for smarter, more guided reviews. <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn how to get started</a>.

## Review Comments

### Copilot — 2026-02-16 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/AbstractPortDatasource.kt`

Using a string literal instead of `mongoVar(Model::expectedMappingStatus)` removes type safety. The codebase convention in similar code (e.g., AbstractTerminalDatasource.kt lines 85-90) uses `mongoVar` with property references to maintain type safety and allow refactoring tools to track field usage. Consider reverting to `id = mongoVar(Model::expectedMappingStatus)` to maintain consistency with the rest of the codebase.

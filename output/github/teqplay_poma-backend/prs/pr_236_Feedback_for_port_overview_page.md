---
id: github:teqplay/poma-backend:pr:236
source: github
type: pull_request
repo: teqplay/poma-backend
number: 236
title: Feedback for port overview page
author: TeqJoostD
state: closed
date: '2026-02-19'
merged_at: '2026-02-19'
base_branch: develop
head_branch: port-overview-fix
url: https://github.com/teqplay/poma-backend/pull/236
labels: []
linked_issues: []
explicit_links: []
---
# PR #236: Feedback for port overview page

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/236  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `port-overview-fix`  
**Created:** 2026-02-19  
**Merged:** 2026-02-19  

## Description

_No description._

## Commits

- `694404b8` **TeqJoostD** (2026-02-19): Feedback for port overview page
- `b3a093f2` **TeqJoostD** (2026-02-19): fix tests
- `a1bc8e41` **TeqJoostD** (2026-02-19): formatting
- `e99187fd` **TeqJoostD** (2026-02-19): fix test
- `0b249389` **TeqJoostD** (2026-02-19): Additional feedback
- `47be201c` **TeqJoostD** (2026-02-19): test fix
- `a9ab360f` **TeqJoostD** (2026-02-19): Align getCount function
- `5347590d` **TeqJoostD** (2026-02-19): KTLINT
- `9396711a` **TeqJoostD** (2026-02-19): Fix for missing cargoType

## Reviews

### github-actions[bot] — COMMENTED (2026-02-19)

Review completed. The changes look good overall, with proper alignment between getAll and getCount methods for search functionality.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2026-02-19)

Review completed. The changes look good overall - the field name correction from `cargoType` to `cargoCategoryType` in the validator aligns with the Terminal model structure, and the search pattern support has been properly added to the count method.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2026-02-19)

Review completed. Found one potential bug related to null handling in filter construction.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-02-19)

## Pull request overview

This PR addresses feedback for the port overview page by enhancing search and filtering capabilities, and fixing a validation bug. The changes add support for search pattern filtering in port count queries and correct terminal validation to check the appropriate cargo field.

**Changes:**
- Added `searchPattern` parameter to `PortService.getCount()` to enable text search filtering in count queries
- Fixed terminal validation to check `cargoCategoryType` instead of `cargoType` field
- Refactored `PortService.getCount()` query building to use a list-based filter pattern for adding dynamic search filters

### Reviewed changes

Copilot reviewed 4 out of 4 changed files in this pull request and generated 2 comments.

| File | Description |
| ---- | ----------- |
| MappingService.kt | Added `validated` and `searchPattern` parameters to port filtering calls to support enhanced filtering in the port overview page |
| PortModelValidatorService.kt | Fixed terminal validation to check `cargoCategoryType` instead of incorrect `cargoType` field |
| PortService.kt | Added `searchPattern` parameter and refactored query building to support dynamic search filtering in count operations |





---

💡 <a href="/teqplay/poma-backend/new/develop/.github/instructions?filename=*.instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add Copilot custom instructions</a> for smarter, more guided reviews. <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn how to get started</a>.

### github-actions[bot] — COMMENTED (2026-02-19)

Review completed. The existing review comments have already identified the key issues with this PR. No additional suggestions at this time.

### github-actions[bot] — COMMENTED (2026-02-19)

The PR refactors validation logic and adds search pattern support to the port count method. I found one potential bug related to null handling in filter construction that should be addressed.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2026-02-19)

Review completed. I've identified one potential bug related to null handling in filter construction that could cause runtime issues with MongoDB queries.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2026-02-19)

Review completed. Found one potential bug related to null handling in filter construction. Please review the inline comment.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### Darius-Wattimena — DISMISSED (2026-02-19)

_No comment._

### github-actions[bot] — COMMENTED (2026-02-19)

Review completed. Found one potential bug related to null handling in filter construction.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### Darius-Wattimena — APPROVED (2026-02-19)

_No comment._

## Review Comments

### Copilot — 2026-02-19 on `src/main/kotlin/nl/teqplay/poma/feature/mapping/MappingService.kt`

The `validated` parameter should be explicitly passed to `getCount` to match the call to `getAll` on line 64. Currently, `getAll` is called with `validated = null`, but `getCount` uses the default value of `validated = true`. This inconsistency will cause the count to not match the actual number of items returned, leading to incorrect pagination.
```suggestion
                searchPattern = searchPattern,
                validated = null,
```

### Copilot — 2026-02-19 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortService.kt`

The mutableListOf() initialization includes potentially null elements. When parameters like `validated`, `expectedMappingStatus`, or `countryCode` are null, the corresponding `?.let` expressions return null, which gets added to the filters list. The `and()` function from MongoDB may not handle null elements properly.

Following the pattern used in DataSource.kt lines 205-210, the filters list should be initialized as empty and elements should be conditionally added using `filters.add()` instead. For example:
```kotlin
val filters = mutableListOf<Bson>()
validated?.let { filters.add(Model::validatedByUser eq validated) }
mappingStatusEnum?.let { filters.add(Model::expectedMappingStatus eq mappingStatusEnum) }
countryCode?.let { filters.add(Model::country / Country::code eq countryCode) }
filters.addAll(getDataSource().extraFilters(searchPattern))
```
```suggestion
        val filters = mutableListOf<Bson>()

        validated?.let { filters.add(Model::validatedByUser eq it) }
        mappingStatusEnum?.let { filters.add(Model::expectedMappingStatus eq it) }
        countryCode?.let { filters.add(Model::country / Country::code eq it) }
```

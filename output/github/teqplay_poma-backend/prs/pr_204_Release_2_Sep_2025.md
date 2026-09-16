---
id: github:teqplay/poma-backend:pr:204
source: github
type: pull_request
repo: teqplay/poma-backend
number: 204
title: Release 2 Sep 2025
author: Darius-Wattimena
state: closed
date: '2025-09-02'
merged_at: '2025-09-02'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/poma-backend/pull/204
labels: []
linked_issues: []
explicit_links: []
---
# PR #204: Release 2 Sep 2025

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/204  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2025-09-02  
**Merged:** 2025-09-02  

## Description

_No description._

## Commits

- `1c0a7bdb` **Darius Wattimena** (2025-08-08): Remove unused WOP code
- `db28137a` **Darius Wattimena** (2025-08-08): Adjusted webclients to instead make use of resttemplates and no more webflux to avoid loading netty
- `fece4ffb` **Darius Wattimena** (2025-08-08): ktlint
- `a83a288d` **Darius Wattimena** (2025-08-22): Merge pull request #201 from teqplay/no-more-reactive
  No more reactive
- `8fd2cdca` **Darius Wattimena** (2025-08-27): Up skeleton version and add slack report on failure dependency
- `3124f02e` **Darius Wattimena** (2025-08-27): Added annotations on scheduled tasks to ensure we report failed
- `6cdd6181` **Darius Wattimena** (2025-08-29): Attempt to fix an issue where the UserService would not be loaded in correctly
- `fe25f775` **Darius Wattimena** (2025-09-01): Fix an issue where the userService could be null because it was not open
- `536b63f8` **Darius Wattimena** (2025-09-01): Merge pull request #202 from teqplay/TCC-53
  TCC-53
- `f552649b` **Darius Wattimena** (2025-09-02): Fixed issue where we potentially could crash the syncing mechanism when corrupt data is provided by a different source
- `b836e05e` **Darius Wattimena** (2025-09-02): Fix confusing comment
- `2330f2bb` **Darius Wattimena** (2025-09-02): Merge pull request #203 from teqplay/fix-sync
  Fix broken Poma sync

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-09-02)

## Pull Request Overview

This PR contains a release for September 2, 2025 that includes several significant code changes and refactoring efforts. The main focus appears to be deprecating World of Ports functionality, replacing WebClient with RestTemplate for HTTP communications, and improving dependency injection patterns.

Key changes include:
- Deprecation of World of Ports (WOP) functionality with removal of import capabilities
- Migration from WebClient to RestTemplate for HTTP client operations
- Refactoring infrastructure controllers to use constructor injection instead of field injection
- Improvements to data synchronization and collection replacement logic

### Reviewed Changes

Copilot reviewed 25 out of 26 changed files in this pull request and generated 1 comment.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/test/kotlin/nl/teqplay/poma/generics/DataSourceTest.kt | Updated test to use `drop()` instead of `deleteMany()` and improved test assertions |
| src/main/resources/application.yml | Removed WOP configuration properties and added Slack webhook configuration |
| src/main/kotlin/nl/teqplay/poma/generics/InfrastructureService.kt | Enhanced merge logic with performance optimizations and improved duplicate detection |
| src/main/kotlin/nl/teqplay/poma/generics/InfrastructureController.kt | Converted from field injection to constructor injection pattern |
| src/main/kotlin/nl/teqplay/poma/generics/DataSource.kt | Improved collection replacement logic with better error handling |
| src/main/kotlin/nl/teqplay/poma/feature/worldofports/WopService.kt | Deprecated and removed WOP import functionality |
| src/main/kotlin/nl/teqplay/poma/feature/worldofports/WopRawDatasource.kt | Added deprecation annotation |
| src/main/kotlin/nl/teqplay/poma/feature/worldofports/WopController.kt | Added deprecation annotation and removed import endpoints |
| src/main/kotlin/nl/teqplay/poma/feature/synchronize/SyncService.kt | Added deduplication logic and exception reporting |
| Multiple infrastructure controllers | Converted from field injection to constructor injection |
| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/berth/BerthService.kt | Migrated from WebClient to RestTemplate |
| src/main/kotlin/nl/teqplay/poma/feature/connection/SlackService.kt | Migrated from WebClient to RestTemplate |
| src/main/kotlin/nl/teqplay/poma/config/RestTemplateConfiguration.kt | Replaced WebClient configuration with RestTemplate configuration |
| src/main/kotlin/nl/teqplay/poma/config/Config.kt | Removed WOP properties configuration |
</details>






---

<sub>**Tip:** Customize your code reviews with copilot-instructions.md. <a href="/teqplay/poma-backend/new/develop/.github?filename=copilot-instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Create the file</a> or <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">learn how to get started</a>.</sub>

## Review Comments

### Copilot — 2025-09-02 on `src/main/kotlin/nl/teqplay/poma/generics/DataSource.kt`

This line attempts to rename a collection that may not exist anymore. If the original collection was successfully renamed to the old namespace in line 114, then `collection` now points to a non-existent collection. This should likely be `database.getCollection(oldNamespace.collectionName, modelClass).renameCollection(currentNamespace)` to restore from the backup.
```suggestion
            database.getCollection(oldNamespace.collectionName, modelClass).renameCollection(currentNamespace)
```

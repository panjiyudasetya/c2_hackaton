---
id: github:teqplay/vesselvoyage-backend:pr:583
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 583
title: Clean up
author: Darius-Wattimena
state: closed
date: '2025-08-06'
merged_at: '2025-08-07'
base_branch: develop
head_branch: clean-up
url: https://github.com/teqplay/vesselvoyage-backend/pull/583
labels: []
linked_issues: []
explicit_links: []
---
# PR #583: Clean up

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/583  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `clean-up`  
**Created:** 2025-08-06  
**Merged:** 2025-08-07  

## Description

Made it so we don't create the data source when not enabled

## Commits

- `9291615e` **Darius Wattimena** (2025-08-06): Made it so we don't create the data source when not enabled
- `cde3fd36` **Darius Wattimena** (2025-08-06): removed unused imports

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-08-06)

## Pull Request Overview

This PR optimizes the ProcessorLogDatasource by making it conditionally loaded only when processor logging is enabled. The changes prevent unnecessary initialization and reduce resource usage when the processor logging feature is disabled.

Key changes:
- Added conditional component loading based on configuration property
- Removed unused query methods to simplify the datasource
- Cleaned up unused imports

### TeqJoostD — APPROVED (2025-08-06)

_No comment._

## Review Comments

### Copilot — 2025-08-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/ProcessorLogDatasource.kt`

The ConditionalOnProperty annotation should specify the `havingValue` parameter to make the condition explicit. Consider using `@ConditionalOnProperty(value = "processor-logs.log-results", havingValue = "true")` to clearly indicate when this component should be loaded.
```suggestion
@ConditionalOnProperty(value = "processor-logs.log-results", havingValue = "true")
```

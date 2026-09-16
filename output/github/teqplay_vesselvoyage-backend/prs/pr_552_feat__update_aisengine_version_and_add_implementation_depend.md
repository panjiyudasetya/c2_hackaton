---
id: github:teqplay/vesselvoyage-backend:pr:552
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 552
title: 'feat: update aisengine version and add implementation dependency'
author: TeqJoostD
state: closed
date: '2025-07-04'
merged_at: null
base_branch: develop
head_branch: master-ais-increase
url: https://github.com/teqplay/vesselvoyage-backend/pull/552
labels: []
linked_issues: []
explicit_links: []
---
# PR #552: feat: update aisengine version and add implementation dependency

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/552  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `master-ais-increase`  
**Created:** 2025-07-04  

## Description

_No description._

## Commits

- `43cc3fd4` **TeqJoostD** (2025-07-04): feat: update aisengine version and add implementation dependency
- `1dab1761` **TeqJoostD** (2025-07-04): Merge branch 'develop' into master-ais-increase
  # Conflicts:
  #	api/build.gradle

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-04)

## Pull Request Overview

This PR updates the AIS engine version constant and adds a new implementation dependency on the AIS engine models (excluding the vesselvoyage API).

- Introduce `aisengine_version` in the buildscript `ext` block.
- Add `implementation` dependency for `nl.teqplay.aisengine:models` with an exclusion.

### Darius-Wattimena — DISMISSED (2025-07-04)

_No comment._

## Review Comments

### Copilot — 2025-07-04 on `api/build.gradle`

[nitpick] The quotation style is inconsistent with other version declarations (which use single quotes). Consider using single quotes for `aisengine_version = 'master-2.3.0'` for consistency.
```suggestion
        aisengine_version = 'master-2.3.0'
```

### Copilot — 2025-07-04 on `api/build.gradle`

[nitpick] Remove the extra space before the parentheses to match typical Gradle DSL style: `implementation("nl.teqplay.aisengine:models:$aisengine_version") {`
```suggestion
    implementation("nl.teqplay.aisengine:models:$aisengine_version") {
```

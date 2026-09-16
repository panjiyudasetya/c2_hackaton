---
id: github:teqplay/vesselvoyage-backend:pr:710
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 710
title: Fix transitive swagger/springdoc dependencies
author: michel-teqplay
state: closed
date: '2026-02-12'
merged_at: '2026-02-12'
base_branch: develop
head_branch: fix-swagger-deps
url: https://github.com/teqplay/vesselvoyage-backend/pull/710
labels: []
linked_issues: []
explicit_links: []
---
# PR #710: Fix transitive swagger/springdoc dependencies

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/710  
**State:** closed | **Author:** michel-teqplay  
**Base ← Head:** `develop` ← `fix-swagger-deps`  
**Created:** 2026-02-12  
**Merged:** 2026-02-12  

## Description

_No description._

## Commits

- `551257bb` **Michel Wilson** (2026-02-12): Fix transitive swagger/springdoc dependencies

## Reviews

### Darius-Wattimena — APPROVED (2026-02-12)

_No comment._

### github-actions[bot] — COMMENTED (2026-02-12)

Review completed. I've identified a potential version mismatch issue that could lead to dependency conflicts.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-02-12)

## Pull request overview

This PR adjusts OpenAPI-related dependencies to avoid pulling SpringDoc artifacts transitively into the `:api` module, while still providing OpenAPI annotation types needed by the codebase.

**Changes:**
- Add a dedicated `swagger_version` version constant in the root `build.gradle`.
- Replace `springdoc-openapi-starter-common` in `api/build.gradle` with a Swagger v3 dependency.

### Reviewed changes

Copilot reviewed 1 out of 2 changed files in this pull request and generated 2 comments.

| File | Description |
| ---- | ----------- |
| build.gradle | Introduces `swagger_version` for Swagger dependency pinning. |
| api/build.gradle | Swaps SpringDoc common dependency for a Swagger v3 artifact to provide OpenAPI annotations. |

## Review Comments

### Copilot — 2026-02-12 on `api/build.gradle`

`swagger_version` is referenced here but is not defined anywhere in `api/build.gradle` (and it is not coming from `gradle.properties`). This will fail the Gradle configuration phase with an unknown property error. Define `swagger_version` in this module’s `buildscript { ext { ... } }` (or reference the root property explicitly, e.g. `rootProject.ext.swagger_version`, if that’s the intended source).

### Copilot — 2026-02-12 on `api/build.gradle`

This module appears to only use OpenAPI annotation types (e.g., `io.swagger.v3.oas.annotations.*`) and not `swagger-core`/model classes. Depending on `swagger-core-jakarta` pulls in extra transitive runtime dependencies; consider using the narrower `io.swagger.core.v3:swagger-annotations-jakarta` (same version) instead to keep the API artifact lighter and reduce dependency conflicts.
```suggestion
    implementation "io.swagger.core.v3:swagger-annotations-jakarta:$swagger_version"
```

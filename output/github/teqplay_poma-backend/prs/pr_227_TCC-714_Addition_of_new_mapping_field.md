---
id: github:teqplay/poma-backend:pr:227
source: github
type: pull_request
repo: teqplay/poma-backend
number: 227
title: TCC-714 Addition of new mapping field
author: TeqJoostD
state: closed
date: '2026-02-09'
merged_at: '2026-02-11'
base_branch: develop
head_branch: TCC-714
url: https://github.com/teqplay/poma-backend/pull/227
labels: []
linked_issues: []
explicit_links:
- jira:TCC-714
---
# PR #227: TCC-714 Addition of new mapping field

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/227  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-714`  
**Created:** 2026-02-09  
**Merged:** 2026-02-11  

## Description

_No description._

## Commits

- `bb6daf6c` **TeqJoostD** (2026-02-06): add mapping status field to port model
- `7375c273` **TeqJoostD** (2026-02-06): Add bistatus field and add mapping for fields
- `ef9444df` **TeqJoostD** (2026-02-09): Remove bistatus-field
- `eb8abf85` **TeqJoostD** (2026-02-10): Rename mapping field and change documentation

## Reviews

### github-actions[bot] — COMMENTED (2026-02-09)

Review completed. Found a few issues related to consistency and code quality.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-02-09)

## Pull request overview

Adds BI-specific metadata to the Port domain model and exposes it through the v1 API, including parsing/validation when converting API models to infrastructure models.

**Changes:**
- Introduces `mappingStatus` (enum) and `biStatus` (boolean) on the `Port` base model.
- Extends API v1 `Port` with `mappingStatus` and `biStatus`.
- Updates `PortService` conversions and adds a new `getMappingStatus` parsing helper.

### Reviewed changes

Copilot reviewed 4 out of 4 changed files in this pull request and generated 3 comments.

| File | Description |
| ---- | ----------- |
| `src/main/kotlin/nl/teqplay/poma/util/InfrastructureUtils.kt` | Adds `getMappingStatus` helper to parse/validate mapping status input. |
| `src/main/kotlin/nl/teqplay/poma/model/basemodels/Port.kt` | Extends the Port persistence/domain model with BI-related fields and a new enum. |
| `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortService.kt` | Maps the new fields between API and infrastructure models. |
| `api/src/main/kotlin/nl/teqplay/poma/api/v1/Port.kt` | Exposes the new fields in the public API contract. |





---

💡 <a href="/teqplay/poma-backend/new/develop/.github/instructions?filename=*.instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add Copilot custom instructions</a> for smarter, more guided reviews. <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn how to get started</a>.

### github-actions[bot] — COMMENTED (2026-02-09)

The PR adds a new `mappingStatus` field to track port mapping status as defined by the BI Team. The implementation looks good overall with proper handling in the API layer, service layer, and utility functions.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### Darius-Wattimena — CHANGES_REQUESTED (2026-02-10)

_No comment._

### TeqJoostD — COMMENTED (2026-02-10)

_No comment._

### TeqJoostD — COMMENTED (2026-02-10)

_No comment._

### TeqJoostD — COMMENTED (2026-02-10)

_No comment._

### TeqJoostD — COMMENTED (2026-02-10)

_No comment._

### github-actions[bot] — COMMENTED (2026-02-10)

The PR adds a new `expectedMappingStatus` field to track port mapping completeness. The implementation is mostly consistent, but there is a critical bug in the `convertWopPortToPort` function (line 386-414) that is not visible in the diff.

**Critical Issue**: The `convertWopPortToPort` function creates Port instances using the secondary constructor but is missing the new required `mappingStatus` parameter. This will cause a compilation error when WOP ports are imported. The function needs to be updated to include `mappingStatus = Port.MappingStatus.NOT_MAPPED` (or another appropriate default) in the Port constructor call at line 392.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### TeqJoostD — COMMENTED (2026-02-11)

_No comment._

### Darius-Wattimena — APPROVED (2026-02-11)

_No comment._

## Review Comments

### Copilot — 2026-02-09 on `src/main/kotlin/nl/teqplay/poma/util/InfrastructureUtils.kt`

In `getMappingStatus`, the local variable is named `source`, but it actually holds a `MappingStatus`. This is misleading (especially next to `getSource`/`getSourceType`) and makes the code harder to follow. Rename it to something like `mappingStatus` (or return the expression directly) to match the function semantics.

### Copilot — 2026-02-09 on `src/main/kotlin/nl/teqplay/poma/model/basemodels/Port.kt`

`enum class MappingStatus()` doesn’t take constructor parameters, so the parentheses are unnecessary. Removing them avoids style warnings and matches typical Kotlin enum declarations.
```suggestion
    enum class MappingStatus {
```

### Copilot — 2026-02-09 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortService.kt`

The new `mappingStatus`/`biStatus` fields are now mapped in both conversion directions, but there’s no test coverage asserting the round-trip behavior (including defaulting when `apiModel.mappingStatus` is null/blank). Extend/add tests in `PortServiceTest` to verify these fields are preserved via `convertToApiModel`/`convertToInfrastructureModel`.

### Darius-Wattimena — 2026-02-10 on `api/src/main/kotlin/nl/teqplay/poma/api/v1/Port.kt`

Comment is wrong, this is not provided by the BI team?

Would say something along the following
> The expected mapping level this port should be ...

### Darius-Wattimena — 2026-02-10 on `api/src/main/kotlin/nl/teqplay/poma/api/v1/Port.kt`

Are we sure about making this a String and not an `Enum`?

I also wouldn't make `null` the default value but make it `NOT_MAPPED`?

### Darius-Wattimena — 2026-02-10 on `src/main/kotlin/nl/teqplay/poma/model/basemodels/Port.kt`

Would add a jackson annotation making `NOT_MAPPED` the default

### Darius-Wattimena — 2026-02-10 on `src/main/kotlin/nl/teqplay/poma/model/basemodels/Port.kt`

Same here

### Darius-Wattimena — 2026-02-10 on `src/main/kotlin/nl/teqplay/poma/model/basemodels/Port.kt`

Actually thinking about this, doesn't `expectedMappingLevel` not make more sense as a name?

### TeqJoostD — 2026-02-10 on `api/src/main/kotlin/nl/teqplay/poma/api/v1/Port.kt`

This is the API model, all enums are strings in the api model

### TeqJoostD — 2026-02-10 on `api/src/main/kotlin/nl/teqplay/poma/api/v1/Port.kt`

Conversion to base model makes it NOT_MAPPED in the DTO

### TeqJoostD — 2026-02-10 on `src/main/kotlin/nl/teqplay/poma/model/basemodels/Port.kt`

no, its not expected mapping level its what the current mapping status is right?

### TeqJoostD — 2026-02-10 on `src/main/kotlin/nl/teqplay/poma/model/basemodels/Port.kt`

i misunderstood what the value is



### TeqJoostD — 2026-02-11 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortService.kt`

sure buddy

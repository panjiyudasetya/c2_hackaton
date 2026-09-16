---
id: github:teqplay/vesselvoyage-backend:pr:621
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 621
title: TCC-469 add ETA to visit and voyage models
author: Jamie-de-Leest
state: closed
date: '2025-10-03'
merged_at: '2025-10-03'
base_branch: develop
head_branch: TCC-469-add-eta-to-visit-and-voyage-models
url: https://github.com/teqplay/vesselvoyage-backend/pull/621
labels: []
linked_issues: []
explicit_links: []
---
# PR #621: TCC-469 add ETA to visit and voyage models

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/621  
**State:** closed | **Author:** Jamie-de-Leest  
**Base ← Head:** `develop` ← `TCC-469-add-eta-to-visit-and-voyage-models`  
**Created:** 2025-10-03  
**Merged:** 2025-10-03  

## Description

_No description._

## Commits

- `4e6a3062` **Jamie de Leest** (2025-10-03): feat: add ETA to visit and voyage models
- `e9236384` **Jamie de Leest** (2025-10-03): chore: clean up comments

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-03)

## Pull Request Overview

This PR adds an ETA (Estimated Time of Arrival) field to the vessel voyage tracking system by introducing a `destinationPortEta` property to both visit and voyage models.

- Added `destinationPortEta` field as an optional `Instant` property to the base `Entry` interface
- Updated both `Visit` and `Voyage` data classes to implement the new ETA field with default null values
- Configured mapper to ignore the ETA field during API conversion (temporarily set to ignore)

### Reviewed Changes

Copilot reviewed 4 out of 4 changed files in this pull request and generated 2 comments.

| File | Description |
| ---- | ----------- |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/Entry.kt | Added destinationPortEta property to base Entry interface |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/Visit.kt | Implemented destinationPortEta field in Visit data class |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/Voyage.kt | Implemented destinationPortEta field in Voyage data class |
| src/main/kotlin/nl/teqplay/vesselvoyage/mapper/EntryV2Mapper.kt | Added mapping configuration to ignore destinationPortEta during conversion |

### Darius-Wattimena — APPROVED (2025-10-03)

_No comment._

## Review Comments

### Copilot — 2025-10-03 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/Entry.kt`

Inconsistent comment formatting - extra space before closing delimiter.
```suggestion
     */
```

### Copilot — 2025-10-03 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/Voyage.kt`

Inconsistent comment formatting - extra space before closing delimiter.
```suggestion
     */
```

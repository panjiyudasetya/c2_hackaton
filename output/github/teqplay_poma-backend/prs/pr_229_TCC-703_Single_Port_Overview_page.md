---
id: github:teqplay/poma-backend:pr:229
source: github
type: pull_request
repo: teqplay/poma-backend
number: 229
title: TCC-703 Single Port Overview page
author: TeqJoostD
state: closed
date: '2026-02-13'
merged_at: '2026-02-16'
base_branch: develop
head_branch: TCC-703
url: https://github.com/teqplay/poma-backend/pull/229
labels: []
linked_issues: []
explicit_links:
- jira:TCC-703
- jira:TCC-705
---
# PR #229: TCC-703 Single Port Overview page

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/229  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-703`  
**Created:** 2026-02-13  
**Merged:** 2026-02-16  

## Description

_No description._

## Commits

- `6357259e` **TeqJoostD** (2026-02-13): Add support for Single Port Overview page
- `6e5ef07e` **TeqJoostD** (2026-02-13): Add support for category overview page
- `4af93ce7` **TeqJoostD** (2026-02-13): KTLINT FORMAT
- `060cbf41` **TeqJoostD** (2026-02-13): Merge branch 'TCC-703' into TCC-705
- `710845ba` **TeqJoostD** (2026-02-16): remove false documentation
- `b0455c98` **TeqJoostD** (2026-02-16): feedback
- `d4b4dfa2` **TeqJoostD** (2026-02-16): Merge branch 'develop' into TCC-703
- `31e7dff8` **TeqJoostD** (2026-02-16): Merge branch 'TCC-703' into TCC-705
- `3cfe49b8` **TeqJoostD** (2026-02-16): Merge branch 'develop' into TCC-703
- `d9f03148` **TeqJoostD** (2026-02-16): Merge branch 'TCC-703' into TCC-705
- `6b668053` **TeqJoostD** (2026-02-16): feedback
- `3ff1c268` **TeqJoostD** (2026-02-16): Feedback
- `9f17d1ae` **TeqJoostD** (2026-02-16): Merge branch 'TCC-703' into TCC-705
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/poma/feature/mapping/MappingService.kt
- `33d3d0d7` **Joost Dambrink** (2026-02-16): Merge pull request #230 from teqplay/TCC-705
  TCC-705 Category Overview Page

## Reviews

### github-actions[bot] — COMMENTED (2026-02-13)

Review completed. I've identified one potential bug related to the mapping status field.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2026-02-13)

Review completed. I found one potential semantic issue regarding the `mappingStatus` field that may need clarification.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-02-13)

## Pull request overview

This PR implements a new endpoint for retrieving detailed port mapping overview information. It introduces a Single Port Overview page feature that provides comprehensive validation status for a port and all its associated infrastructure entities (terminals, berths, anchorages, and pilot boarding places).

**Changes:**
- Added new `PortMappingOverview` API model with nested `Entity` type to represent aggregated validation data
- Added GET endpoint `/mapping/port/{portId}/summary` to retrieve port mapping overview
- Refactored `PortModelValidatorService` to include infrastructure service dependencies and added new methods: `validate(port)` and `validateAndReturnEntities(port)`
- Simplified `MappingService` by removing infrastructure service dependencies (moved to `PortModelValidatorService`)
- Added comprehensive unit tests for the new `getPortMappingOverview` functionality

### Reviewed changes

Copilot reviewed 6 out of 6 changed files in this pull request and generated 8 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |

| ---- | ----------- |

| api/src/main/kotlin/nl/teqplay/poma/api/v1/PortMappingOverview.kt | New API model for port mapping overview with entity validation data |

| src/main/kotlin/nl/teqplay/poma/feature/mapping/MappingController.kt | Added new endpoint for retrieving detailed port mapping overview |

| src/main/kotlin/nl/teqplay/poma/feature/mapping/MappingService.kt | Implemented getPortMappingOverview method and buildEntityList helper, removed infrastructure service dependencies |

| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/PortModelValidatorService.kt | Added constructor dependencies for infrastructure services, new validate and validateAndReturnEntities methods |

| src/test/kotlin/nl/teqplay/poma/feature/mapping/MappingServiceTest.kt | New comprehensive test suite for MappingService.getPortMappingOverview |

| src/test/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/PortModelValidatorServiceTest.kt | Updated to mock new constructor dependencies |
</details>






---

💡 <a href="/teqplay/poma-backend/new/develop/.github/instructions?filename=*.instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add Copilot custom instructions</a> for smarter, more guided reviews. <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn how to get started</a>.

### TeqJoostD — COMMENTED (2026-02-16)

_No comment._

### github-actions[bot] — COMMENTED (2026-02-16)

Review completed. No suggestions at this time.

### github-actions[bot] — COMMENTED (2026-02-16)

Review completed. The implementation looks solid with good test coverage and clear documentation. I found one minor issue regarding redundant null-checking that could be simplified.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### TeqJoostD — COMMENTED (2026-02-16)

_No comment._

### github-actions[bot] — COMMENTED (2026-02-16)

Review completed. The implementation looks solid with good test coverage and clean refactoring. No critical issues found.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### Darius-Wattimena — CHANGES_REQUESTED (2026-02-16)

_No comment._

### TeqJoostD — COMMENTED (2026-02-16)

_No comment._

### github-actions[bot] — COMMENTED (2026-02-16)

Review completed. No suggestions at this time.

### Darius-Wattimena — DISMISSED (2026-02-16)

_No comment._

### github-actions[bot] — COMMENTED (2026-02-16)

Review completed. Found one issue related to documentation/implementation mismatch.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### Darius-Wattimena — APPROVED (2026-02-16)

_No comment._

## Review Comments

### Copilot — 2026-02-13 on `api/src/main/kotlin/nl/teqplay/poma/api/v1/PortMappingOverview.kt`

The EntityType enum ordering (TERMINAL, BERTH, PORT, PILOT_BOARDING_PLACE, ANCHORAGE) is inconsistent with the InfrastructureModelType enum which has PORT first. For consistency and logical hierarchy, consider reordering to: PORT, TERMINAL, BERTH, ANCHORAGE, PILOT_BOARDING_PLACE, which places the parent entity (PORT) first followed by child entities.
```suggestion
        PORT, TERMINAL, BERTH, ANCHORAGE, PILOT_BOARDING_PLACE
```

### Copilot — 2026-02-13 on `src/main/kotlin/nl/teqplay/poma/feature/mapping/MappingService.kt`

The buildEntityList method contains significant code duplication across the four entity types (terminals, berths, anchorages, pilot boarding places). Consider extracting a helper function to reduce repetition and improve maintainability. For example: createEntityGroup(entities, reports, type, idPrefix) that handles the common pattern of counting valid/invalid items, finding the latest entity, and creating the Entity object.

### Copilot — 2026-02-13 on `src/main/kotlin/nl/teqplay/poma/feature/mapping/MappingService.kt`

The implementation documentation claims the portId parameter can accept both port ID and UN/LOCODE, but the service method only calls portService.get() which uses findOneById and only works with IDs. If UN/LOCODE support is intended, consider using a method that can handle both (e.g., getByUnLoCode when get returns null), or update the documentation to clarify only port IDs are supported.

### Copilot — 2026-02-13 on `src/main/kotlin/nl/teqplay/poma/feature/mapping/MappingService.kt`

The mappingStatus field is incorrectly set to port.expectedMappingStatus, but according to the API documentation it should represent "The current mapping status" not the expected one. The current mapping status should be calculated based on the validation report: NOT_MAPPED if nothing is valid, BASIC_MAPPED if the port itself is valid, and FULLY_MAPPED if everything is valid. Consider adding logic similar to what's done in getMappingStatus() method but returning the actual MappingStatus enum value instead of a boolean.

### TeqJoostD — 2026-02-16 on `api/src/main/kotlin/nl/teqplay/poma/api/v1/PortMappingOverview.kt`

jeez who CARES

### TeqJoostD — 2026-02-16 on `src/main/kotlin/nl/teqplay/poma/feature/mapping/MappingService.kt`

Needed for null safety, dont care about the duplication tbh

### Darius-Wattimena — 2026-02-16 on `src/test/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/PortModelValidatorServiceTest.kt`

Just import `mock`?

### Darius-Wattimena — 2026-02-16 on `src/main/kotlin/nl/teqplay/poma/feature/mapping/MappingService.kt`

The ID is not really unique this way, I would adjust it to `${port._id}.terminals`?
If the frontend uses the id as is, then it will just clash and potentially result in rendering issues.

(Same for other entities)

### TeqJoostD — 2026-02-16 on `src/test/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/PortModelValidatorServiceTest.kt`

meh

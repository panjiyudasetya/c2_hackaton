---
id: github:teqplay/vesselvoyage-backend:pr:489
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 489
title: SPV-2564 add support for including historic data when recalculating
author: TeqJoostD
state: closed
date: '2025-04-30'
merged_at: '2025-05-16'
base_branch: develop
head_branch: SPV-2564
url: https://github.com/teqplay/vesselvoyage-backend/pull/489
labels: []
linked_issues: []
explicit_links: []
---
# PR #489: SPV-2564 add support for including historic data when recalculating

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/489  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `SPV-2564`  
**Created:** 2025-04-30  
**Merged:** 2025-05-16  

## Description

_No description._

## Commits

- `8dfe1070` **TeqJoostD** (2025-04-30): feat: add support for including historic data when recalculating
- `af933d41` **TeqJoostD** (2025-04-30): fix: tests
- `d68e53cb` **TeqJoostD** (2025-04-30): fix: tests
- `f7c27a3e` **TeqJoostD** (2025-04-30): fix
- `a96fd31e` **TeqJoostD** (2025-04-30): fix gradl
- `32b1a98b` **TeqJoostD** (2025-05-01): Merge branch 'develop' into SPV-2564
- `c1923801` **Joost Dambrink** (2025-05-13): Merge branch 'develop' into SPV-2564

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-04-30)

## Pull Request Overview

This PR adds support for including historic data in recalculation requests. It updates service methods, conversion requests, and controller endpoints to accept and handle an includeHistoricData flag.
- Updated recalculation service methods to propagate the includeHistoricData parameter.
- Modified conversion service methods to adjust scenario settings based on the historic data flag.
- Enhanced controller endpoints to accept a new query parameter for historic data inclusion.

### Reviewed Changes

Copilot reviewed 3 out of 3 changed files in this pull request and generated no comments.

| File                                                                                         | Description                                                            |
| -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationService.kt | Added includeHistoricData parameter to recalculation functions.        |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsConversionService.kt     | Updated conversion service to accept and use includeHistoricData flag. |
| src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingRecalculateV2Controller.kt | Added query parameter and passed includeHistoricData to service layer.   |

### leonjoosse — APPROVED (2025-05-06)

LGTM

---
id: github:teqplay/vesselvoyage-backend:pr:496
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 496
title: SPV-2573 Add support for categorizing AnchorStops
author: TeqJoostD
state: closed
date: '2025-05-13'
merged_at: '2025-06-17'
base_branch: develop
head_branch: SPV-2573
url: https://github.com/teqplay/vesselvoyage-backend/pull/496
labels: []
linked_issues: []
explicit_links: []
---
# PR #496: SPV-2573 Add support for categorizing AnchorStops

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/496  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `SPV-2573`  
**Created:** 2025-05-13  
**Merged:** 2025-06-17  

## Description

_No description._

## Commits

- `d0f977f8` **TeqJoostD** (2025-05-13): Add support for categorizing AnchorStops
- `d82e3238` **TeqJoostD** (2025-05-20): Merge branch 'develop' into SPV-2573
  # Conflicts:
  #	api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/sof/pto/PtoStatementOfFactsView.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/mapper/PtoStatementOfFactsMapper.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGenerator.kt
  #	src/test/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGeneratorTest.kt
- `8730fc8f` **TeqJoostD** (2025-05-20): fix: merge conflicts
- `740a82b4` **TeqJoostD** (2025-06-12): Merge branch 'develop' into SPV-2573
  # Conflicts:
  #	src/test/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGeneratorTest.kt

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-05-13)

## Pull Request Overview

This PR adds support for categorizing AnchorStops by refactoring the existing slow moving periods functionality into a more generic categorization mechanism using the new CategorizedPeriods type. Key changes include:
- Updating test cases and expected types to use CategorizedPeriods for both slow moving periods and anchor stops.
- Refactoring functions (e.g. renaming determineSlowMovingInPortBoundaries to determinePortBoundaries and introducing a generic categorizePeriods method).
- Adding new mapping methods for categorized anchor stops in the mapper and updating the API view model accordingly.

### Reviewed Changes

Copilot reviewed 5 out of 5 changed files in this pull request and generated 2 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGeneratorTest.kt | Updated tests to work with CategorizedPeriods and added tests for AnchorStop categorization. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGenerator.kt | Introduced generic categorization functions and a new categorizeAnchorStops method. |
| src/main/kotlin/nl/teqplay/vesselvoyage/mapper/PtoStatementOfFactsMapper.kt | Added mapping functions for categorized slow moving periods and anchor stops. |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/sof/PtoStatementOfFactsView.kt | Updated the model to deprecate the legacy anchorStops field and replace slowMovingPeriods with CategorizedPeriods. |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/SlowMovingPeriod.kt | Added a new id field to the SlowMovingPeriod model. |
</details>



<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGenerator.kt:735**
* The renaming from determineSlowMovingInPortBoundaries to determinePortBoundaries is clear; however, consider updating the inline documentation to mention that this method is now used for both slow moving periods and anchor stops for better clarity.
```
private fun determinePortBoundaries(
```
</details>

### TeqJoostD — COMMENTED (2025-05-13)

_No comment._

### Darius-Wattimena — DISMISSED (2025-05-16)

_No comment._

### Darius-Wattimena — DISMISSED (2025-06-03)

_No comment._

### Darius-Wattimena — APPROVED (2025-06-17)

_No comment._

## Review Comments

### Copilot — 2025-05-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGenerator.kt`

[nitpick] Consider expanding the documentation for categorizeAnchorStops to clearly explain the influence of pilot and port boundaries on the categorization logic, especially for edge cases such as empty anchorStops.
```suggestion
     * Categorizes anchor stops in the [CategorizedPeriods] periods.
     *
     * This function uses pilot and port boundaries to determine whether an anchor stop
     * falls within the port area or outside of it. The boundaries are calculated using
     * the [determinePortBoundaries] function, which considers the start and end times
     * of pilot activities (inbound and outbound) and port area activities.
     *
     * @param anchorStops A list of [AnchorStopInfo] objects representing anchor stops to be categorized.
     * @param pilotInbound The inbound pilot activity, used to determine the start boundary of the port area.
     * @param pilotOutbound The outbound pilot activity, used to determine the end boundary of the port area.
     * @param portAreaActivities A list of [AreaActivity] objects representing activities within the port area.
     * @return A [CategorizedPeriods] object containing the categorized anchor stops.
     *
     * Edge case: If the `anchorStops` list is empty, the function returns an empty [CategorizedPeriods] object.
     * This ensures that the function handles such cases gracefully without throwing errors.
```

### Copilot — 2025-05-13 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/SlowMovingPeriod.kt`

[nitpick] Consider updating the class documentation to include details about the new 'id' field in SlowMovingPeriod to assist frontend developers in understanding its purpose.

### TeqJoostD — 2025-05-13 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/SlowMovingPeriod.kt`

ID = Identification

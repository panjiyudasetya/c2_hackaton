---
id: github:teqplay/vesselvoyage-backend:pr:674
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 674
title: TCC-458 etd predictions
author: Darius-Wattimena
state: closed
date: '2025-12-02'
merged_at: '2025-12-04'
base_branch: develop
head_branch: TCC-458-etd-predictions
url: https://github.com/teqplay/vesselvoyage-backend/pull/674
labels: []
linked_issues: []
explicit_links: []
---
# PR #674: TCC-458 etd predictions

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/674  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-458-etd-predictions`  
**Created:** 2025-12-02  
**Merged:** 2025-12-04  

## Description

While this adjusts the internal model with this change, an additional PR will follow later to update the API implementation so the ETD is actually exposed in the Visit and Journal models.

## Commits

- `84e91d3c` **Darius Wattimena** (2025-12-01): Up ETA predictor models to latest develop release
- `ed8dcbc8` **Darius Wattimena** (2025-12-01): Extend internal esof model to include a new field for port ETDs
- `4e1239b1` **Darius Wattimena** (2025-12-01): Rework eta processor to not make use of any generics and adjust logic to also process ETD predictions
- `bcfa133f` **Darius Wattimena** (2025-12-02): Enhance TrueDestinationEtaProcessor to handle broken predictions and improve validation logic for ETA and ETD
- `a9239c5c` **Darius Wattimena** (2025-12-02): Add test for port visit segment without arrival time in TrueDestinationEtaProcessor
- `9792e998` **Darius Wattimena** (2025-12-03): Adjusted existing tests and added tests to make sure ETD processing works as expected
- `f07fe6fa` **Darius Wattimena** (2025-12-03): Align ETD processing with expectations
- `2960c0dc` **Darius Wattimena** (2025-12-03): Refactor status update logic in TrueDestinationEtaProcessor for clarity
- `ba851d07` **Darius Wattimena** (2025-12-04): ktlint

## Reviews

### github-actions[bot] — COMMENTED (2025-12-02)

Review completed. Found one critical bug in the ETD processing logic that needs to be addressed.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-12-02)

## Pull request overview

This PR adds support for ETD (Estimated Time of Departure) predictions to complement the existing ETA (Estimated Time of Arrival) functionality. The changes introduce a new `currentPortEtd` field in the `NewESoF` model and refactor the `TrueDestinationEtaProcessor` to handle both prediction types. The etapredictor library is also updated to version `develop-2025-12-01-b138.1` which includes the `PortVisitResultSegment` type needed for ETD predictions.

Key changes:
- Adds `currentPortEtd` field to the NewESoF model for storing departure time predictions
- Refactors TrueDestinationEtaProcessor to extract and apply both ETA and ETD predictions
- Adds validation for broken predictions (when arrivalTime is null)
- Adds test coverage for the error case when port visit segments lack arrival times

### Reviewed changes

Copilot reviewed 3 out of 4 changed files in this pull request and generated 6 comments.

| File | Description |
| ---- | ----------- |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/model/v2/NewESoF.kt | Adds `currentPortEtd` field to store ETD predictions, documented as always null during voyages |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eta/TrueDestinationEtaProcessor.kt | Major refactoring to support ETD predictions: adds prediction extraction, validation, and application logic through new helper methods |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/eta/TrueDestinationEtaProcessorTest.kt | Adds test for port visit segments without arrival time; updates assertion message for travel segment error case |
| build.gradle | Updates etapredictor library from version `develop-2025-10-08-b123.1` to `develop-2025-12-01-b138.1` |

### github-actions[bot] — COMMENTED (2025-12-03)

Review completed. The ETD prediction implementation looks solid overall with good test coverage. Found one potential issue with null safety that should be addressed.

### github-actions[bot] — COMMENTED (2025-12-03)

Review completed. The ETD prediction implementation is well-structured with comprehensive test coverage. The logic correctly handles different ship statuses and the null safety checks are appropriate. No suggestions at this time.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2025-12-03)

Review completed. No suggestions at this time.

### michel-teqplay — DISMISSED (2025-12-04)

_No comment._

### github-actions[bot] — COMMENTED (2025-12-04)

Review completed. The ETD prediction implementation looks well-structured with comprehensive test coverage. The logic correctly handles different ship status types and properly manages ETD assignments based on visit vs voyage states.

### michel-teqplay — APPROVED (2025-12-04)

_No comment._

## Review Comments

### Copilot — 2025-12-02 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eta/TrueDestinationEtaProcessor.kt`

[nitpick] The comment "not both are null so reset" is slightly unclear. It would be clearer to say "at least one prediction exists, so reset both to null" or "remove predictions since we no longer receive them".
```suggestion
                // At least one prediction exists, so reset both to null
```

### Copilot — 2025-12-02 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eta/TrueDestinationEtaProcessor.kt`

The variable name `visitEsofWithEtd` suggests this is for a visit esof, but this function can be called with a voyage esof as the `currentEsof` parameter (from line 130 in `getResultOnVoyage`). The variable should be named more generically, e.g., `updatedEsof` or `esofWithEtd`, to avoid confusion about its purpose.
```suggestion
            val esofWithEtd = currentEsof.copy(
                trueDestinationEta = etdPrediction.arrivalTime,
                updatedAt = updateTime
            )

            previousEntryEsof to esofWithEtd
```

### Copilot — 2025-12-02 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eta/TrueDestinationEtaProcessor.kt`

The `applyEtdPrediction` function has a critical bug: it's setting `trueDestinationEta` instead of `currentPortEtd`. This function is supposed to apply ETD (Estimated Time of Departure) predictions, not ETA predictions.

The correct implementation should be:
```kotlin
val visitEsofWithEtd = currentEsof.copy(
    currentPortEtd = etdPrediction.arrivalTime,
    updatedAt = updateTime
)
```

Additionally, based on the documentation for `currentPortEtd` in NewESoF.kt which states "This is always null when in a voyage", when this function is called from `getResultOnVoyage`, the ETD should likely be applied to the previous visit (the port just departed from), not the current voyage. The return statement should probably be:
```kotlin
val updatedPreviousEsof = previousEntryEsof?.copy(
    currentPortEtd = etdPrediction.arrivalTime,
    updatedAt = updateTime
)
updatedPreviousEsof to currentEsof
```

### Copilot — 2025-12-02 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/eta/TrueDestinationEtaProcessorTest.kt`

The new test only verifies the error case when `arrivalTime` is null, but doesn't test the happy path where the ETD prediction is successfully applied. There should be a test that verifies:
1. When a PortVisitResultSegment with a valid `arrivalTime` is provided, the `currentPortEtd` field is set on the esof
2. The `currentPortEtd` is set to the correct value from `etdPrediction.arrivalTime`
3. When in Voyage status, the ETD is applied to the correct esof (likely the previous visit, not the current voyage)

### Copilot — 2025-12-02 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eta/TrueDestinationEtaProcessor.kt`

The logic for updating the status when resetting predictions is incorrect. When `updatedPreviousEsof` is null (which happens in Visit status where there's no previous visit), the code returns the original `status` unchanged (line 276), even though `updatedEsof` with reset predictions was created.

The correct logic should update the status regardless of whether `updatedPreviousEsof` is null:
```kotlin
val updatedStatus = when (status) {
    is NewVisitShipStatus -> status.copy(
        visit = status.visit.copy(esof = updatedEsof)
    )
    is NewVoyageShipStatus -> status.copy(
        voyage = status.voyage.copy(esof = updatedEsof),
        previousVisit = status.previousVisit?.copy(esof = updatedPreviousEsof)
    )
    else -> status
}
```
```suggestion
                // Always update the status with the new ESoF, regardless of previous visit existence
                val updatedStatus = when (status) {
                    is NewVisitShipStatus -> status.copy(
                        visit = status.visit.copy(esof = updatedEsof)
                    )
                    is NewVoyageShipStatus -> status.copy(
                        voyage = status.voyage.copy(esof = updatedEsof),
                        previousVisit = status.previousVisit?.copy(esof = updatedPreviousEsof)
                    )
                    else -> status
```

### Copilot — 2025-12-02 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eta/TrueDestinationEtaProcessor.kt`

[nitpick] The error message refers to "No ETD time found in prediction" but it's checking `etdPrediction.arrivalTime`. While `arrivalTime` might be the correct field name in the PortVisitResultSegment from the external library, the error message could be clearer by specifying what field is missing, e.g., "No arrival time found in ETD prediction (PortVisitResultSegment)". However, if `arrivalTime` in the context of a PortVisitResultSegment represents the departure time, this is a confusing API design from the external library that should be documented here.

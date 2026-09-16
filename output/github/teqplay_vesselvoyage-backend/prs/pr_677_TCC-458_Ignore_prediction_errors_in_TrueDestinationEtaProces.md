---
id: github:teqplay/vesselvoyage-backend:pr:677
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 677
title: TCC-458 Ignore prediction errors in TrueDestinationEtaProcessor
author: Darius-Wattimena
state: closed
date: '2025-12-04'
merged_at: '2025-12-04'
base_branch: develop
head_branch: TCC-458-ignore-prediction-errors
url: https://github.com/teqplay/vesselvoyage-backend/pull/677
labels: []
linked_issues: []
explicit_links: []
---
# PR #677: TCC-458 Ignore prediction errors in TrueDestinationEtaProcessor

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/677  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-458-ignore-prediction-errors`  
**Created:** 2025-12-04  
**Merged:** 2025-12-04  

## Description

_No description._

## Commits

- `0501a0c2` **Darius Wattimena** (2025-12-04): Don't throw an error when eta and etd are null or no arrival time is provided
- `8ec9edf6` **Darius Wattimena** (2025-12-04): Update comment to make sense

## Reviews

### github-actions[bot] — COMMENTED (2025-12-04)

Review completed. The error handling implementation looks correct and follows existing patterns in the codebase. No suggestions at this time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-12-04)

## Pull request overview

This PR adds error handling to the `TrueDestinationEtaProcessor` to gracefully ignore predictions that contain errors from the predictor service. When prediction errors are present, the processor now returns early with an unchanged status and no changes or issues, rather than attempting to process potentially invalid prediction data.

**Key Changes:**
- Added early-return error checks in both `getResultOnVisit` and `getResultOnVoyage` methods
- Predictions with errors are now silently ignored, returning the status unchanged

### github-actions[bot] — COMMENTED (2025-12-04)

Review completed. The changes appropriately handle prediction errors by silently ignoring them rather than creating processing issues, which aligns with the PR title and intent.

### github-actions[bot] — COMMENTED (2025-12-04)

Review completed. The changes appropriately simplify error handling by ignoring invalid predictions rather than creating issues. The logic is sound and test coverage is maintained.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### michel-teqplay — APPROVED (2025-12-04)

_No comment._

### github-actions[bot] — COMMENTED (2025-12-04)

Review completed. No suggestions at this time.

## Review Comments

### Copilot — 2025-12-04 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eta/TrueDestinationEtaProcessor.kt`

Prediction errors are being silently ignored without any logging. This could make debugging difficult when predictions fail. Consider adding logging to track when predictions are ignored due to errors. The codebase uses KotlinLogging (see `EtaProcessor.kt` line 33 for example).

Example:
```kotlin
if (input.errors.isNotEmpty()) {
    log.warn { "Ignoring prediction for IMO $imo due to ${input.errors.size} error(s): ${input.errors}" }
    return PredictionProcessingResult(
        status = status,
        changes = emptyList(),
        issues = emptyList()
    )
}
```

### Copilot — 2025-12-04 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eta/TrueDestinationEtaProcessor.kt`

This new error handling behavior lacks test coverage. The test file `TrueDestinationEtaProcessorTest.kt` contains 13 test cases but none test the scenario where `input.errors` is not empty. Consider adding test cases for both `getResultOnVisit` and `getResultOnVoyage` to verify that predictions with errors are properly ignored.

Example test:
```kotlin
@Test
fun `visit - ignore prediction when errors present`() {
    val status = newVisitStatus()
    val input: PredictionResult = mock()
    whenever(input.errors).thenReturn(listOf("Error message"))
    
    val result = processor.getProcessingResult(status, input, updateTime, 999)
    
    assertEquals(status, result.status)
    assertTrue(result.changes.isEmpty())
    assertTrue(result.issues.isEmpty())
}
```

### Copilot — 2025-12-04 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eta/TrueDestinationEtaProcessor.kt`

This error handling logic is duplicated in both `getResultOnVisit` and `getResultOnVoyage` methods (lines 29-36 and 100-107). Consider extracting this into a private helper method to reduce code duplication and improve maintainability.

```kotlin
private fun handlePredictionErrors(
    input: PredictionResult,
    status: NewShipStatus
): PredictionProcessingResult? {
    return if (input.errors.isNotEmpty()) {
        PredictionProcessingResult(
            status = status,
            changes = emptyList(),
            issues = emptyList()
        )
    } else {
        null
    }
}
```

Then use it as:
```kotlin
handlePredictionErrors(input, status)?.let { return it }
```

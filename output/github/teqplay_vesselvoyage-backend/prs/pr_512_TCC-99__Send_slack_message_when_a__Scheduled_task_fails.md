---
id: github:teqplay/vesselvoyage-backend:pr:512
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 512
title: 'TCC-99: Send slack message when a @Scheduled task fails'
author: leonjoosse
state: closed
date: '2025-05-23'
merged_at: '2025-05-26'
base_branch: develop
head_branch: TCC-99-notify-on-failing-scheduled-tasks
url: https://github.com/teqplay/vesselvoyage-backend/pull/512
labels: []
linked_issues: []
explicit_links: []
---
# PR #512: TCC-99: Send slack message when a @Scheduled task fails

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/512  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `TCC-99-notify-on-failing-scheduled-tasks`  
**Created:** 2025-05-23  
**Merged:** 2025-05-26  

## Description

_No description._

## Commits

- `5e9c42ff` **leonj** (2025-05-23): Send slack message when a @Scheduled task fails. This only happens when the processing profile is enabled (because the SlackMessageService is only available under the processing profile

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-05-23)

## Pull Request Overview

This PR adds Slack notification functionality to various scheduled tasks across the services and tests for when tasks fail. The key changes include the addition of a slackMessageService parameter (or null in tests) and wrapping scheduled task logic in try/catch blocks that send Slack messages on exceptions.

### Reviewed Changes

Copilot reviewed 13 out of 13 changed files in this pull request and generated 1 comment.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationServiceTest.kt | Updated test constructor parameters to include slackMessageService as null |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/TraceServiceTest.kt | Updated test constructor parameters to include slackMessageService as null |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/ProcessingTraceServiceTest.kt | Updated test constructor parameters to include slackMessageService as null |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/InfraServiceTest.kt | Updated test constructor parameters to include slackMessageService as null |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/ProcessingTraceService.kt | Added slackMessageService injection and Slack notification logic in generateTraces() scheduled task |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationService.kt | Added slackMessageService injection and Slack notification logic in checkScenarioProgress() scheduled task |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/AutomaticRecalculationService.kt | Added slackMessageService injection and Slack notification logic to scheduled tasks recalculateBatch() and refreshTrackedShips() |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/TraceService.kt | Added slackMessageService injection and Slack notification logic in persistOngoingTraces() scheduled task |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/StaticShipInfoService.kt | Wrapped onShipRefresh() in try/catch to add Slack notification on failure |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/SnapshotRecalculationService.kt | Added slackMessageService usage to snapshotRecalculationJob() scheduled task |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/RecalculationService.kt | Added Slack notifications in scheduled tasks recalculateNextShip() and refreshRecalculableShips() |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt | Added slackMessageService injection and Slack notification logic in post-processing scheduled task |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/InfraCacheService.kt | Added slackMessageService injection and Slack notification logic in onCronInfraRefresh() scheduled task |
</details>



<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/AutomaticRecalculationService.kt:128**
* In the recalculateBatch() scheduled task, the Slack alert title 'persistOngoingTraces' does not match the task's context. Please update the title to accurately reflect the recalculateBatch task to avoid confusion.
```
title = "Scheduled task failed: persistOngoingTraces",
```
</details>

### Darius-Wattimena — APPROVED (2025-05-23)

_No comment._

## Review Comments

### Copilot — 2025-05-23 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/ProcessingTraceService.kt`

[nitpick] The generateTraces() scheduled task swallows exceptions (only logging and notifying via Slack) whereas other scheduled tasks rethrow exceptions after notification. Consider reviewing and standardizing the exception handling strategy across scheduled tasks to ensure consistent task recovery behavior.

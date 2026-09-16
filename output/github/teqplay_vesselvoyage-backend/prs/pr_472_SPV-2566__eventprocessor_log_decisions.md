---
id: github:teqplay/vesselvoyage-backend:pr:472
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 472
title: 'SPV-2566: eventprocessor log decisions'
author: leonjoosse
state: closed
date: '2025-04-11'
merged_at: '2025-05-01'
base_branch: develop
head_branch: SPV-2566-eventprocessor-log-decisions
url: https://github.com/teqplay/vesselvoyage-backend/pull/472
labels: []
linked_issues: []
explicit_links: []
---
# PR #472: SPV-2566: eventprocessor log decisions

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/472  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `SPV-2566-eventprocessor-log-decisions`  
**Created:** 2025-04-11  
**Merged:** 2025-05-01  

## Description

_No description._

## Commits

- `a40d66a1` **leonj** (2025-04-07): WIP. Add decision logging for EndOfSeaPassageEndProcessors. Attach the origin event to the NewProcessingResult.
- `3f4ed4f6` **leonj** (2025-04-08): Added decisions for Stop processors
- `baf68d34` **leonj** (2025-04-08): Log event processor decision and origin of the event. Adjust EventProcessingServiceTests to ignore the debug fields
- `b57eff68` **leonj** (2025-04-08): Enhance logging
- `57f1b0fa` **leonj** (2025-04-08): Enhance logging: do not print full port
- `46b8600f` **leonj** (2025-04-11): Log when the result.status.[visit|voyage] and the last related change (same id) do not match. This may help locate where a discrepancy starts to exist with duplicate entry inserts
- `e04f6e74` **leonj** (2025-04-11): Do nothing when evaluating logs for inequality
- `d0610707` **leonj** (2025-04-14): Only log when the squashed visit actually has a value
- `9112dc8c` **leonj** (2025-04-14): Log more stuff on switching main ports, seems to go south there
- `a2ceef7c` **leonj** (2025-04-14): Merge branch 'develop' into SPV-2566-eventprocessor-log-decisions
- `952f8348` **leonj** (2025-04-23): Add processing logs to the database, so we can query it easier than log files
- `01fd9df3` **leonj** (2025-04-24): Fix profile for ProcessorLogDatasource
- `4809aeb7` **leonj** (2025-04-24): Merge branch 'develop' into SPV-2566-eventprocessor-log-decisions
- `1df49ef1` **leonj** (2025-04-24): Add flag to enable event processing logs (default=false), as this may result in a big database collection
- `8df54ace` **leonj** (2025-04-24): Merge remote-tracking branch 'origin/blacklist' into SPV-2566-eventprocessor-log-decisions
- `be610ff4` **leonj** (2025-04-24): Fix insert of log
- `09c73ff9` **leonj** (2025-04-30): Merge branch 'develop' into SPV-2566-eventprocessor-log-decisions
- `844e19d9` **Leon Joosse** (2025-05-01): Merge branch 'develop' into SPV-2566-eventprocessor-log-decisions
- `2d433341` **leonj** (2025-05-01): Fix import

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-04-11)

Copilot reviewed 9 out of 9 changed files in this pull request and generated no comments.


<details>
<summary>Comments suppressed due to low confidence (2)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopBaseProcessor.kt:203**
* [nitpick] The decision message uses an informal and unprofessional tone ("Bleep bloop: error"). Consider replacing it with a clear and formal error message, e.g., 'Error: stop port not entered'.
```
decision = "Bleep bloop: error. We never entered the port of this stop!"
```
**src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageStartProcessor.kt:426**
* [nitpick] The decision message contains informal language ('Whoohoo!'), which might be unsuitable for production logging. Consider using a more neutral tone, for example, 'Initial visit created for this ship'.
```
decision = "Initial visit for this ship! Whoohoo!"
```
</details>

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-04-24)

## Pull Request Overview

This PR updates the event processing logic to log explicit decision messages and integrate a processor log datasource while harmonizing test expectations regarding debug fields. Key changes include:
- Adding explicit decision and origin fields to the NewEventProcessingResult in various processors.
- Integrating ProcessorLogDatasource into service and test classes to persist processor log entries.
- Updating tests to ignore debug fields by copying result objects with decision and origin set to null.

### Reviewed Changes

Copilot reviewed 16 out of 16 changed files in this pull request and generated no comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/EventProcessingServiceTest.kt | Update tests to ignore debug fields by zeroing out decision and origin |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/EventBufferScenarioTest.kt | Inject ProcessorLogDatasource mock in the event buffer scenario |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/BaseEventProcessingTest.kt | Add ProcessorLogDatasource dependency to the service constructor |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopStartProcessor.kt, StopEndProcessor.kt, StopBaseProcessor.kt | Add decision messages to stop processors to improve logging clarity |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageStartProcessor.kt, EndOfSeaPassageEndProcessor.kt | Add extended decision messages for EOSP event processing cases |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/EventProcessor.kt, EventProcessingService.kt | Update event processing to append origin logging using decision messages and persist logs |
| src/main/kotlin/nl/teqplay/vesselvoyage/model/ProcessorLog.kt and datasource | Introduce ProcessorLog model and corresponding datasource for processor logging |
</details>



<details>
<summary>Comments suppressed due to low confidence (2)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopBaseProcessor.kt:203**
* [nitpick] The decision message 'Bleep bloop: error...' is unprofessional and may confuse users or developers; consider replacing it with a more descriptive and formal error message.
```
decision = "Bleep bloop: error. We never entered the port of this stop!"
```
**src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageStartProcessor.kt:427**
* [nitpick] The decision message contains informal language; consider using a tone that is consistent with production logging standards.
```
decision = "Initial visit for this ship! Whoohoo!"
```
</details>

### TeqJoostD — DISMISSED (2025-04-28)

_No comment._

### Darius-Wattimena — APPROVED (2025-05-01)

_No comment._

## Comments

### leonjoosse — 2025-04-24

Adding JoostD as Darius is on holiday

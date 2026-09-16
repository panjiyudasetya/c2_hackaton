---
id: github:teqplay/vesselvoyage-backend:pr:668
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 668
title: Add slack logging for berth.start > berth.end
author: TeqJoostD
state: closed
date: '2025-11-19'
merged_at: '2025-11-19'
base_branch: develop
head_branch: TCC-326
url: https://github.com/teqplay/vesselvoyage-backend/pull/668
labels: []
linked_issues: []
explicit_links: []
---
# PR #668: Add slack logging for berth.start > berth.end

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/668  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-326`  
**Created:** 2025-11-19  
**Merged:** 2025-11-19  

## Description

_No description._

## Commits

- `b534b2b4` **TeqJoostD** (2025-11-19): Add slack logging for weird berth thingies
- `fab26090` **TeqJoostD** (2025-11-19): Autowire to prevent generic hell
- `d03a98e7` **TeqJoostD** (2025-11-19): Add nullability for autowire to prevent throwing exceptions

## Reviews

### michel-teqplay — DISMISSED (2025-11-19)

_No comment._

### github-actions[bot] — COMMENTED (2025-11-19)

This PR introduces a breaking change that will prevent the code from compiling. All subclasses of ActivityEventProcessor need to be updated to pass the SlackMessageService parameter.

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-11-19)

## Pull Request Overview

This PR adds Slack logging to detect and report when a berth end time is set to a value before the start time, which indicates a data integrity issue.

Key changes:
- Adds validation in `updateEndOfMatchingActivity` to check if end time is before start time
- Introduces `slackError` method to send error notifications to Slack with event details
- Adds `SlackMessageService` as a required constructor parameter to `ActivityEventProcessor`

### github-actions[bot] — COMMENTED (2025-11-19)

Review completed. The refactoring from constructor injection to field injection for SlackMessageService is functionally correct and simplifies subclass constructors. One minor suggestion provided for improved null safety.

### github-actions[bot] — COMMENTED (2025-11-19)

The changes correctly implement optional dependency injection for SlackMessageService. The implementation follows Spring best practices and handles the null case appropriately.

### michel-teqplay — APPROVED (2025-11-19)

_No comment._

## Review Comments

### Copilot — 2025-11-19 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/ActivityEventProcessor.kt`

Adding a required constructor parameter to an abstract class is a breaking change. All subclasses (AnchorBaseProcessor, AnchorAreaBaseProcessor, ApproachAreaBaseProcessor, UniqueBerthBaseProcessor, LockAreaBaseProcessor, PilotAreaBaseProcessor, PortBaseProcessor, TerminalMooringAreaBaseProcessor) must be updated to provide this parameter. Since only ActivityEventProcessor.kt is modified in this PR, the code will not compile. Either include updates to all subclasses in this PR, or make this parameter optional with a default value (e.g., nullable with default null and add null checks before calling slackError).
```suggestion
    private val slackMessageService: SlackMessageService? = null
```

### Copilot — 2025-11-19 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/ActivityEventProcessor.kt`

[nitpick] The condition uses nullable safe access `updatedAreaActivity.end?.time` in both the null check and the comparison. This can be simplified using Kotlin's `let` or by storing the end time in a variable to avoid redundant nullable access and improve readability. For example: `updatedAreaActivity.end?.time?.let { endTime -> if (updatedAreaActivity.start.time > endTime) { slackError(event, visit._id) } }`
```suggestion
        updatedAreaActivity.end?.time?.let { endTime ->
            if (updatedAreaActivity.start.time > endTime) {
                slackError(event, visit._id)
            }
```

### Copilot — 2025-11-19 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/ActivityEventProcessor.kt`

Creating a new Jackson ObjectMapper instance on every error occurrence is inefficient. ObjectMapper creation is expensive and the instance is thread-safe. Consider creating a companion object with a shared mapper instance: `companion object { private val mapper = jacksonObjectMapper() }` and reuse it in the slackError function.

### Copilot — 2025-11-19 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/ActivityEventProcessor.kt`

The error message is generic and refers to 'berth' specifically, but ActivityEventProcessor is used for multiple activity types (anchor, berth, port, pilot, lock, approach, etc.). The message should be more generic or include the activity type. Consider: 'Trying to set activity end which is before the start' or include context about which activity type this relates to.

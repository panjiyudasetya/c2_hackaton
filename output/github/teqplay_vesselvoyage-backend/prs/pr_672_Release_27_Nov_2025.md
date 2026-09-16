---
id: github:teqplay/vesselvoyage-backend:pr:672
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 672
title: Release 27 Nov 2025
author: Darius-Wattimena
state: closed
date: '2025-11-27'
merged_at: '2025-11-27'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/672
labels: []
linked_issues: []
explicit_links: []
---
# PR #672: Release 27 Nov 2025

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/672  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2025-11-27  
**Merged:** 2025-11-27  

## Description

Review completed. No suggestions at this time.

## Commits

- `4b7b99d6` **Pim van den Toorn** (2025-11-04): Added Slack deployment notifications
- `b534b2b4` **TeqJoostD** (2025-11-19): Add slack logging for weird berth thingies
- `fab26090` **TeqJoostD** (2025-11-19): Autowire to prevent generic hell
- `d03a98e7` **TeqJoostD** (2025-11-19): Add nullability for autowire to prevent throwing exceptions
- `d346d8b7` **Joost Dambrink** (2025-11-19): Merge pull request #668 from teqplay/TCC-326
  Add slack logging for berth.start > berth.end
- `74ad272f` **PimTeqplay** (2025-11-20): Merge pull request #667 from teqplay/slack-deploy-notification
  Added Slack deployment notifications
- `09458a75` **Jamie de Leest** (2025-11-21): DEV-1282: Add pr-review workflow
- `3dbf766c` **jamie-teqplay** (2025-11-21): Merge pull request #669 from teqplay/DEV-1282-add-augment-pr-review
  DEV-1282: Add augment PR review workflow
- `89bcfa01` **Jamie de Leest** (2025-11-24): delete old pr review workflow
- `e9f95ec7` **jamie-teqplay** (2025-11-25): Merge pull request #670 from teqplay/delete-old-pr-review
  delete old pr review workflow
- `b7c4eaca` **Darius Wattimena** (2025-11-27): Up AisEngine version to 2.7.0
- `c6715402` **Darius Wattimena** (2025-11-27): Merge branch 'develop' into fix-ais-engine-version
- `bcf7df3b` **Darius Wattimena** (2025-11-27): Merge pull request #671 from teqplay/fix-ais-engine-version
  Up AisEngine version to 2.7.0

## Reviews

### michel-teqplay — APPROVED (2025-11-27)

_No comment._

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-11-27)

## Pull request overview

This release updates the AIS Engine dependency version and adds error detection for invalid activity time ordering. The primary change is in the event processing layer where a new Slack notification is added to alert when an area activity's end time is set before its start time, indicating a potential data quality issue.

- Updated `aisengine_version` from `master-2.3.1` to `master-2.7.0` across build files
- Added error detection and Slack alerting for invalid activity time ordering in `ActivityEventProcessor`
- Replaced old PR review workflow with new unified workflow configuration
- Enhanced CI/CD workflow with additional Slack channel configuration and health check URLs

### Reviewed changes

Copilot reviewed 5 out of 6 changed files in this pull request and generated 4 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/ActivityEventProcessor.kt | Adds Slack error notification when area activity end time is before start time, includes field injection setup and helper function |
| build.gradle | Updates aisengine_version dependency from master-2.3.1 to master-2.7.0 |
| api/build.gradle | Updates aisengine_version dependency to match main build file |
| .github/workflows/pr-review.yml | Introduces new PR review workflow using teqplay/actions template |
| .github/workflows/main.yml | Adds Slack channel IDs and health check URLs for dev/prod environments |
| .github/workflows/basic-pr-review.yml | Removes old custom PR review workflow in favor of centralized template |
</details>

## Review Comments

### Copilot — 2025-11-27 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/ActivityEventProcessor.kt`

Field injection with `@Autowired` will not work in this abstract class because `ActivityEventProcessor` is not a Spring-managed bean. The concrete implementations (e.g., `AnchorStartProcessor`, `BerthStartProcessor`) are instantiated directly in their respective processor services (e.g., `AnchorProcessor`), not by Spring's dependency injection container.

To fix this, you should:
1. Add `slackMessageService: SlackMessageService?` as a constructor parameter to `ActivityEventProcessor`
2. Pass it through from the concrete processor services which are Spring beans (e.g., `AnchorProcessor`, `BerthProcessor`, etc.)

This will ensure the service is properly injected and available when needed.

### Copilot — 2025-11-27 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/ActivityEventProcessor.kt`

Consider using the existing `globalObjectMapper` instead of creating a new `jacksonObjectMapper()` instance on each call. Creating a new ObjectMapper instance is expensive and the global one is already configured with the necessary modules (JavaTimeModule, etc.).

Replace:
```kotlin
val mapper = jacksonObjectMapper()
val json = mapper.writeValueAsString(event)
```

With:
```kotlin
val json = globalObjectMapper.writeValueAsString(event)
```

You'll need to add the import:
```kotlin
import nl.teqplay.vesselvoyage.util.globalObjectMapper
```

### Copilot — 2025-11-27 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/ActivityEventProcessor.kt`

The error message "Trying to set berth end which is before the start" is misleading because `ActivityEventProcessor` is an abstract base class used for multiple area types (berths, anchors, ports, locks, terminals, etc.). The hardcoded "berth" reference doesn't accurately describe the error when this code is executed for other activity types.

Consider making the message generic:
```kotlin
slackMessageService?.sendMessage("Trying to set area activity end which is before the start", "event: $json \n visit: $visitId", SLACK_COLOR_RED)
```

Or, if you need to be specific about the area type, pass the activity type as a parameter or derive it from the event.
```suggestion
        slackMessageService?.sendMessage("Trying to set area activity end which is before the start", "event: $json \n visit: $visitId", SLACK_COLOR_RED)
```

### Copilot — 2025-11-27 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/ActivityEventProcessor.kt`

The new error detection logic (lines 299-301) that checks for invalid time ordering lacks test coverage. Given that this repository has comprehensive test coverage for event processing (see `EventProcessingServiceTest.kt` with 4449 lines), this new behavior should be tested.

Consider adding test cases that:
1. Verify the slack message is sent when an end time is before the start time
2. Verify normal processing continues correctly after the slack notification
3. Test edge cases like when `end?.time` is null (which is already handled by the null check)

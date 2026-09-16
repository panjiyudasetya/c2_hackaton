---
id: github:teqplay/vesselvoyage-backend:pr:711
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 711
title: Release PR for library dependency fix
author: michel-teqplay
state: closed
date: '2026-02-12'
merged_at: '2026-02-12'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/711
labels: []
linked_issues: []
explicit_links: []
---
# PR #711: Release PR for library dependency fix

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/711  
**State:** closed | **Author:** michel-teqplay  
**Base ← Head:** `master` ← `develop`  
**Created:** 2026-02-12  
**Merged:** 2026-02-12  

## Description

_No description._

## Commits

- `5cecb5bd` **Michel Wilson** (2026-02-11): Process bunker encounters both ways
- `e3f828d4` **Michel Wilson** (2026-02-11): Also honor blacklist and barges property for other vessel
- `551257bb` **Michel Wilson** (2026-02-12): Fix transitive swagger/springdoc dependencies
- `262df93c` **Michel Wilson** (2026-02-12): Merge pull request #710 from teqplay/fix-swagger-deps
  Fix transitive swagger/springdoc dependencies
- `489bae3f` **Michel Wilson** (2026-02-12): Merge pull request #709 from teqplay/TCC-710_bunker-encounters
  Process bunker encounters both ways

## Reviews

### Darius-Wattimena — APPROVED (2026-02-12)

_No comment._

### github-actions[bot] — COMMENTED (2026-02-12)

Review completed. Found one critical issue with partial failure handling that could lead to data loss.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-02-12)

## Pull request overview

This PR is titled "Release PR for library dependency fix" but contains two distinct sets of changes: a dependency migration from SpringDoc to Swagger Core, and a significant new feature for processing bunker encounter events bidirectionally.

**Changes:**
- Migrated API documentation dependency from `springdoc-openapi-starter-common` to `swagger-core-jakarta`
- Implemented bidirectional processing for bunker encounter events (both main ship and bunker vessel)
- Added comprehensive test coverage for the new bunker encounter processing logic

### Reviewed changes

Copilot reviewed 3 out of 4 changed files in this pull request and generated 5 comments.

| File | Description |
| ---- | ----------- |
| build.gradle | Added swagger_version variable (2.2.29) to support the dependency migration |
| api/build.gradle | Replaced springdoc dependency with swagger-core-jakarta for API annotations |
| EventsDefaultMessageProcessor.kt | Added logic to process bunker encounters for both vessels involved, with separate locking per ship |
| EventsDefaultMessageProcessorTest.kt | Added three new test cases covering bidirectional bunker processing and single-ship non-bunker processing scenarios |

## Review Comments

### Copilot — 2026-02-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessor.kt`

Critical issue: The message is acknowledged (line 105) even if processing fails for one or more ships. If an exception occurs during processing (caught at line 101-103), the message will still be acknowledged, potentially leading to data loss. 

In the previous implementation, the message was acknowledged inside the try-catch block, ensuring it was only acknowledged if processing succeeded. Now, if processing the main ship succeeds but processing the bunker vessel fails (or vice versa), the message is still acknowledged.

Consider tracking whether any processing succeeded and only acknowledging if at least one ship was processed successfully, or rethrow the exception after processing all ships if any failed.

### Copilot — 2026-02-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessor.kt`

When an exception occurs during event processing, the error is logged but no metrics are updated to reflect the failure. The eventDroppedCount metric is not incremented, making it difficult to monitor and detect processing failures in production.

Consider incrementing eventDroppedCount when an exception is caught, so that monitoring systems can alert on processing failures.
```suggestion
                log.error(ex) { "Failed to process event, dropping message $event" }
                // Increment dropped count so failures during processing are visible in metrics.
                eventDroppedCount.incrementAndGet()
```

### Copilot — 2026-02-12 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessorTest.kt`

The test setup doesn't configure the enableBarges property on the EventProcessingProperties mock. When the production code checks processingProperties.enableBarges (line 79 in EventsDefaultMessageProcessor.kt), it will return the default mock value.

For the bunker encounter tests, this could affect whether the otherShip is processed. Consider explicitly configuring enableBarges in the test setup to ensure consistent and predictable test behavior.

### Copilot — 2026-02-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessor.kt`

There is a significant discrepancy between the PR title "Release PR for library dependency fix" and the actual code changes. While the PR does include a dependency change (springdoc to swagger-core), it also introduces a substantial new feature: processing bunker encounter events for both the main ship and the bunker vessel.

This is more than just a dependency fix - it's a behavior change that affects how bunker encounters are recorded. Consider updating the PR title and description to accurately reflect the scope of changes, or splitting this into separate PRs for the dependency fix and the feature addition.

### Copilot — 2026-02-12 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessorTest.kt`

The new bunker encounter processing logic introduces several error scenarios that are not covered by tests:

1. What happens when processing succeeds for the main ship but fails for the bunker vessel (or vice versa)?
2. What happens when both ships fail to process?
3. How are metrics updated in these failure scenarios?

Consider adding test cases that verify the behavior when exceptions are thrown during processing, particularly around message acknowledgment and metric updates.

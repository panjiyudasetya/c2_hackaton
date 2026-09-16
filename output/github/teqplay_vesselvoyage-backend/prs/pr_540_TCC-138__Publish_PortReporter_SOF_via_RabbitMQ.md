---
id: github:teqplay/vesselvoyage-backend:pr:540
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 540
title: 'TCC-138: Publish PortReporter SOF via RabbitMQ'
author: leonjoosse
state: closed
date: '2025-06-18'
merged_at: '2025-06-27'
base_branch: develop
head_branch: TCC-138-prp-sof-rabbitmq
url: https://github.com/teqplay/vesselvoyage-backend/pull/540
labels: []
linked_issues: []
explicit_links: []
---
# PR #540: TCC-138: Publish PortReporter SOF via RabbitMQ

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/540  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `TCC-138-prp-sof-rabbitmq`  
**Created:** 2025-06-18  
**Merged:** 2025-06-27  

## Description

This PR enables publishing the `PortReporterStatementOfFactsView` via the `ChangesPublisherService`. Before, the system only published the PTO SOF view. 

The routing key for the PTO sof was just `sof`. That does not leave room for expansion. The routing keys for RabbitMQ are therefore updated: 

`SOF.{imo}.{action}` --> `SOFVIEW.{viewname}.{imo}.{action}`, where `viewname` is either `PTO` or `PORTREPORTER`.

Note that `SOF.{imo}.{action}` is not used anymore for publishing after merging this PR, so adjustments to the queue bindings must be made. This is already applied on dev. On prod, this should be looked after **before deploying**.

## Commits

- `8b8477a1` **leonj** (2025-06-18): Publish PortReporter SOFView via RabbitMQ in the ChangesPublisherService.
- `0dc98465` **leonj** (2025-06-20): Give our RabbitMQ outgoing change sender a more descriptive name
- `bc1f6a67` **leonj** (2025-06-20): Merge branch 'develop' into TCC-138-prp-sof-rabbitmq
- `254abf3b` **Leon Joosse** (2025-06-20): Merge branch 'develop' into TCC-138-prp-sof-rabbitmq
- `d8bcb2aa` **Leon Joosse** (2025-06-25): Merge branch 'develop' into TCC-138-prp-sof-rabbitmq

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-06-18)

## Pull Request Overview

This PR enhances the messaging functionality by enabling the publication of PortReporterStatementOfFactsView, in addition to the PTO view. Key changes include:
- Switching the RabbitMQ event sender in tests to CustomRabbitMqEventSender.
- Updating the routing key format to "SOFVIEW.{viewname}.{imo}.{action}" in ChangesPublisherService.
- Publishing both PTO and PORTREPORTER statement-of-facts for NewVisit events.

### Reviewed Changes

Copilot reviewed 4 out of 4 changed files in this pull request and generated 1 comment.

| File | Description |
| ---- | ----------- |
| src/test/kotlin/nl/teqplay/vesselvoyage/ApplicationTest.kt | Updated test configuration to use CustomRabbitMqEventSender and removed references to the old PTO generator. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/publisher/CustomRabbitMqEventSender.kt | Added new wrapper component for sending RabbitMQ events with a custom implementation. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/publisher/ChangesPublisherService.kt | Updated routing key format and enhanced logic to publish both PTO and PORTREPORTER SOF messages. |


<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/service/publisher/ChangesPublisherService.kt:254**
* [nitpick] Add an inline comment to clarify why both PTO and PORTREPORTER SOF changes are published during a NewVisit event.
```
            outgoingChanges.add(OutgoingSofChange(action, esofV2Service.produce(PORTREPORTER, entry, esof)))
```
</details>

### leonjoosse — COMMENTED (2025-06-18)

_No comment._

### Darius-Wattimena — COMMENTED (2025-06-20)

_No comment._

### Darius-Wattimena — CHANGES_REQUESTED (2025-06-20)

_No comment._

### leonjoosse — COMMENTED (2025-06-20)

_No comment._

### leonjoosse — COMMENTED (2025-06-20)

_No comment._

### Darius-Wattimena — APPROVED (2025-06-20)

_No comment._

## Review Comments

### Copilot — 2025-06-18 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/publisher/ChangesPublisherService.kt`

Typo in default IMO value. Consider changing 'UNKOWN_IMO' to 'UNKNOWN_IMO'.
```suggestion
                        imo = value.ship.imo ?: "UNKNOWN_IMO"
```

### leonjoosse — 2025-06-18 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/publisher/CustomRabbitMqEventSender.kt`

I added this wrapper for publishing to RabbitMQ, otherwise it was too much shenanigans to make comparison work in the tests.

### Darius-Wattimena — 2025-06-20 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/publisher/ChangesPublisherService.kt`

Yes please fix this typo :)

### Darius-Wattimena — 2025-06-20 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/publisher/ChangesPublisherService.kt`

```suggestion
                        imo = value.ship.imo ?: "UNKNOWN_IMO"
```
Isn't `imo` here nullable as well? Would be nice to do the same code here as the PTO view?

### Darius-Wattimena — 2025-06-20 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/publisher/CustomRabbitMqEventSender.kt`

Would rename this class to something like `RabbitMqOutgoingChangeSender` or something like that?

### leonjoosse — 2025-06-20 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/publisher/ChangesPublisherService.kt`

It's indeed non-null. Could do the same as in PTO SOF, but we made a wrong choice in PTO SOF to use the ShipDetails class to represent the ship, that is actually exposing too much information. Also it would be weird to have a SOF without imo, because we're targeting imo only...
So I think no change necessary here

### leonjoosse — 2025-06-20 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/publisher/CustomRabbitMqEventSender.kt`

Yes, that makes sense, will do

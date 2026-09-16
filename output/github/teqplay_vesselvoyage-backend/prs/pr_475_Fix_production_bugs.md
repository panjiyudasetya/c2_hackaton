---
id: github:teqplay/vesselvoyage-backend:pr:475
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 475
title: Fix production bugs
author: Darius-Wattimena
state: closed
date: '2025-04-15'
merged_at: '2025-04-15'
base_branch: develop
head_branch: fix-processing-configmap-loading-prod
url: https://github.com/teqplay/vesselvoyage-backend/pull/475
labels: []
linked_issues: []
explicit_links: []
---
# PR #475: Fix production bugs

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/475  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `fix-processing-configmap-loading-prod`  
**Created:** 2025-04-15  
**Merged:** 2025-04-15  

## Description

_No description._

## Commits

- `e0ce679e` **Darius Wattimena** (2025-04-14): Merge pull request #473 from teqplay/develop
  Release 14-04-2025
- `9e8a8b8c` **Darius Wattimena** (2025-04-15): Disable profile-specific sources to prevent loading of API configmap in processing component
- `21715ad1` **Darius Wattimena** (2025-04-15): Add event type tag to metric registry in ShipToShipTransferProcessor to fix an issue

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-04-15)

Copilot reviewed 1 out of 2 changed files in this pull request and generated no comments.

<details>
<summary>Files not reviewed (1)</summary>

* **src/main/resources/application.properties**: Language not supported
</details>

<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/shiptoship/ShipToShipTransferProcessor.kt:22**
* Ensure that the changes to MetricRegistry instantiation are covered by tests to validate that metrics are tagged appropriately.
```
metricRegistry = MetricRegistry(ShipToShipTransferProcessor::class, meterRegistry, listOf(TAG_EVENT_TYPE_KEY))
```
</details>

### michel-teqplay — APPROVED (2025-04-15)

_No comment._

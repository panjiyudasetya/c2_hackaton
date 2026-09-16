---
id: github:teqplay/vesselvoyage-backend:pr:617
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 617
title: TCC-422 Eta predictions implementation
author: Darius-Wattimena
state: closed
date: '2025-09-29'
merged_at: '2025-10-02'
base_branch: develop
head_branch: TCC-422-eta-predictions
url: https://github.com/teqplay/vesselvoyage-backend/pull/617
labels: []
linked_issues: []
explicit_links: []
---
# PR #617: TCC-422 Eta predictions implementation

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/617  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-422-eta-predictions`  
**Created:** 2025-09-29  
**Merged:** 2025-10-02  

## Description

Tests will follow in the last PR given that splitting this up was otherwise way too hard.

That said, this PR contains all the logic needed to process the ETA's from the new ETA predictor NATS KV.

## Commits

- `6679d7d4` **Darius Wattimena** (2025-09-15): Adjusted processing code so it is reusable in preparation for the ETA predictions
- `36fb237c` **Darius Wattimena** (2025-09-18): Add ETA prediction feature with configuration and processing logic
- `c7b45a8b` **Darius Wattimena** (2025-09-18): Merge branch 'develop' into TCC-422-eta-predictions
- `4b2df814` **Darius Wattimena** (2025-09-18): Add createNewESoF utility and integrate into EndOfSeaPassage processors to make sure ETA predictions get provided to the next visit or voyage
- `047bc195` **Darius Wattimena** (2025-09-18): Improve how we process ETA predictions so they follow the VesselVoyage processing pattern
- `2dbea26e` **Darius Wattimena** (2025-09-18): ktlint
- `e57f7df7` **Darius Wattimena** (2025-09-18): Added missing code to update the status of a ship when processing ETAs
- `cb1558bb` **Darius Wattimena** (2025-09-29): Merge branch 'develop' into TCC-422-eta-predictions
- `268ac03c` **Darius Wattimena** (2025-09-30): Also update the updatedAt when processing an ETA
- `2fbf25d9` **Darius Wattimena** (2025-09-30): Simplify message consumption in EtaPredictionMessageHandler and added missing try catch which could result in the thread currently crashing
- `7dda3ec0` **Darius Wattimena** (2025-10-02): fix: assign subscriber in startup method
- `7b38ae81` **Darius Wattimena** (2025-10-02): Add unit tests for EtaPredictionMessageHandler and TrueDestinationEtaProcessor
- `9c1f7deb` **Darius Wattimena** (2025-10-02): ktlint please

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-09-29)

## Pull Request Overview

This PR introduces ETA (Estimated Time of Arrival) prediction functionality by implementing a system to consume predictions from a NATS key-value bucket. The implementation adds the ability to process true destination ETA predictions and integrate them into the vessel voyage tracking system.

Key changes:
- Added ETA prediction message handler to consume from NATS KV store
- Created TrueDestinationEtaProcessor for processing prediction data
- Extended ESoF model to include true destination ETA field
- Refactored processor interfaces to support generic input processing

### Reviewed Changes

Copilot reviewed 41 out of 42 changed files in this pull request and generated 3 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/EtaPredictionMessageHandler.kt` | New message handler for consuming ETA predictions from NATS KV |
| `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eta/TrueDestinationEtaProcessor.kt` | Core processor for handling ETA prediction logic |
| `src/main/kotlin/nl/teqplay/vesselvoyage/config/EtaPredictionConfiguration.kt` | Configuration for NATS KV bucket connection |
| `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/Processor.kt` | New generic processor interface |
| `api/src/main/kotlin/nl/teqplay/vesselvoyage/model/v2/NewESoF.kt` | Extended ESoF model with trueDestinationEta field |
| Multiple processor files | Refactored to implement new Processor interface and remove config parameter |
</details>

### michel-teqplay — DISMISSED (2025-10-02)

_No comment._

### michel-teqplay — DISMISSED (2025-10-02)

_No comment._

### michel-teqplay — APPROVED (2025-10-02)

_No comment._

## Review Comments

### Copilot — 2025-09-29 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/EtaPredictionMessageHandler.kt`

This busy-wait loop consumes CPU unnecessarily. Consider adding a small sleep interval (e.g., Thread.sleep(100)) or use a proper blocking mechanism to wait for messages.
```suggestion
                    // Wait for messages
                    Thread.sleep(100)
```

### Copilot — 2025-09-29 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eta/TrueDestinationEtaProcessor.kt`

The NewESoF constructor is missing the shipToShipTransfers parameter. This should be included for consistency, even if it's an empty list.
```suggestion
                    slowMovingPeriods = null,
                    shipToShipTransfers = emptyList()
```

### Copilot — 2025-09-29 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eta/TrueDestinationEtaProcessor.kt`

The NewESoF constructor is also missing the updatedAt parameter. This should be included with the updateTime value for proper tracking.

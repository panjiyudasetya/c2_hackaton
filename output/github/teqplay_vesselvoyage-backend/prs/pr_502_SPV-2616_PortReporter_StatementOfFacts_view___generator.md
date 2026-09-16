---
id: github:teqplay/vesselvoyage-backend:pr:502
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 502
title: SPV-2616 PortReporter StatementOfFacts view + generator
author: leonjoosse
state: closed
date: '2025-05-15'
merged_at: '2025-05-19'
base_branch: develop
head_branch: SPV-2616-portreporter-sof-view
url: https://github.com/teqplay/vesselvoyage-backend/pull/502
labels: []
linked_issues: []
explicit_links: []
---
# PR #502: SPV-2616 PortReporter StatementOfFacts view + generator

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/502  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `SPV-2616-portreporter-sof-view`  
**Created:** 2025-05-15  
**Merged:** 2025-05-19  

## Description

Implements the PortReporterStatementOfFactsView, the underlying models and the generator.
Stuff for the API and client will be done in separate PRs (although some stuff works out of the box because of the SOFView interface).

## Commits

- `5d8f5f52` **leonj** (2025-05-15): Add DTO objects to collect info to build the PortReporterStatementOfFactsView
- `dcb4f203` **leonj** (2025-05-15): Add PortReporterStatementOfFactsView
- `cfa8d457` **leonj** (2025-05-15): Add PortReporterStatementOfFactsViewGenerator. Add test. Separate test helper functions for PTO and PortReporter SOF view
- `2d68b059` **leonj** (2025-05-15): Fix PtoStatementOfFactsMapperTest
- `d7c15446` **leonj** (2025-05-15): Enhance documentation on PortReporterStatementOfFactsView and its underlying models
- `f6cd18a0` **leonj** (2025-05-16): Do not expose ShipDetails model (which is internal to VV), instead use the Ship model
- `af2f31bb` **Leon Joosse** (2025-05-19): Merge branch 'develop' into SPV-2616-portreporter-sof-view

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-05-15)

## Pull Request Overview

Implements the PortReporter-specific StatementOfFacts view and its generator, including new data models, a MapStruct mapper, and API types. Test helpers have been refactored into distinct objects for PTO and PortReporter.

- Added `PortReporterSofHelperFunctions` alongside existing `PtoSofHelperFunctions`
- Introduced new model classes under `model/esof/portreporterview`
- Created `PortReporterStatementOfFactsMapper` and API view classes, plus updated JSON subtype registration

### Reviewed Changes

Copilot reviewed 19 out of 19 changed files in this pull request and generated no comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/test/kotlin/nl/teqplay/vesselvoyage/util/SofHelperFunctions.kt | Removed obsolete shared test helper |
| src/test/kotlin/nl/teqplay/vesselvoyage/util/PtoSofHelperFunctions.kt | Extracted PTO-specific helper functions |
| src/test/kotlin/nl/teqplay/vesselvoyage/util/PortReporterSofHelperFunctions.kt | Added PortReporter-specific helper functions |
| src/main/kotlin/nl/teqplay/vesselvoyage/model/esof/portreporterview/*.kt | Added duplicate data classes for PortReporter view |
| src/main/kotlin/nl/teqplay/vesselvoyage/mapper/PortReporterStatementOfFactsMapper.kt | Implemented MapStruct mappings for PortReporter SOF |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/sof/portreporter/PortReporterStatementOfFactsView.kt | Defined API view data classes |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/sof/StatementOfFactsView.kt | Registered PortReporter view in JSON subtypes |
</details>

### jbugella — COMMENTED (2025-05-16)

_No comment._

### Darius-Wattimena — COMMENTED (2025-05-16)

_No comment._

### Darius-Wattimena — CHANGES_REQUESTED (2025-05-16)

_No comment._

### leonjoosse — COMMENTED (2025-05-19)

_No comment._

### Darius-Wattimena — DISMISSED (2025-05-19)

_No comment._

### Darius-Wattimena — APPROVED (2025-05-19)

_No comment._

## Review Comments

### jbugella — 2025-05-16 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/sof/portreporter/PortReporterStatementOfFactsView.kt`

Why is the area nullable?

### Darius-Wattimena — 2025-05-16 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/sof/portreporter/PortReporterStatementOfFactsView.kt`

If we delete the port in Poma, then it could be possible that we still have the visit data, but no reference anymore to the port information.

### Darius-Wattimena — 2025-05-16 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/sof/portreporter/PortReporterStatementOfFactsView.kt`

Wasn't the conclusion of our discussions that we don't need those references anymore for the PortReporter view?

### leonjoosse — 2025-05-19 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/sof/portreporter/PortReporterStatementOfFactsView.kt`

We did indeed discuss to move it out, but in the end decided to leave it in

## Comments

### leonjoosse — 2025-05-16

Noticed that the `PortReporterStatementOfFactsView.ship` uses model `ShipDetails`, which is internal to VV. Therefore replacing it with the `Ship` model, tailored to the SOF view.

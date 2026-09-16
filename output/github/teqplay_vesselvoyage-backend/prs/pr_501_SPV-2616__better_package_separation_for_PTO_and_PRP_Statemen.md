---
id: github:teqplay/vesselvoyage-backend:pr:501
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 501
title: 'SPV-2616: better package separation for PTO and PRP StatementOfFactsView'
author: leonjoosse
state: closed
date: '2025-05-15'
merged_at: '2025-05-19'
base_branch: develop
head_branch: SPV-2616-sof-view-prepare-for-portreporter
url: https://github.com/teqplay/vesselvoyage-backend/pull/501
labels: []
linked_issues: []
explicit_links: []
---
# PR #501: SPV-2616: better package separation for PTO and PRP StatementOfFactsView

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/501  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `SPV-2616-sof-view-prepare-for-portreporter`  
**Created:** 2025-05-15  
**Merged:** 2025-05-19  

## Description

Prepare for the PortReporterStatementOfFactsView: move pto classes to their own `pto` package, to prevent mixup with PRP. 
This also makes the next PR with the actual PRP implementation better readable.

## Commits

- `28cf7689` **leonj** (2025-05-15): Move PtoStatementOfFactsView to its own sub package, to later add another subpackage for PortReporterStatementOfFactsView
  Move all internal SOF info objects for PTO to their own subpackage, as we'll duplicate them later on for PortReporter in another subpackage

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-05-15)

## Pull Request Overview

This PR reorganizes PTO-related classes into their own `pto` package to prepare for the upcoming PRP implementation and prevent mix-ups.

- Updated all import paths in service, mapper, and test files to point to `apiv2.model.sof.pto`
- Moved `PtoStatementOfFactsView` into the new `pto` package and adjusted its package declaration and imports
- Added the new `pto` subtype import in the Jackson polymorphic base class

### Reviewed Changes

Copilot reviewed 8 out of 8 changed files in this pull request and generated no comments.

<details>
<summary>Show a summary per file</summary>

| File                                                                                  | Description                                             |
|---------------------------------------------------------------------------------------|---------------------------------------------------------|
| src/test/kotlin/.../PtoStatementOfFactsViewGeneratorTest.kt                           | Updated imports for PTO model classes to `sof.pto`      |
| src/test/kotlin/.../PtoStatementOfFactsMapperTest.kt                                   | Updated imports for PTO model classes to `sof.pto`      |
| src/main/kotlin/.../service/publisher/ChangesPublisherService.kt                      | Updated `PtoStatementOfFactsView` import to `sof.pto`   |
| src/main/kotlin/.../service/api/PtoStatementOfFactsViewGenerator.kt                   | Updated imports for PTO model classes to `sof.pto`      |
| src/main/kotlin/.../service/api/EsofV2Service.kt                                      | Updated `PtoStatementOfFactsView` import to `sof.pto`   |
| src/main/kotlin/.../mapper/PtoStatementOfFactsMapper.kt                                | Updated imports for all PTO model classes to `sof.pto`  |
| api/src/main/kotlin/.../apiv2/model/sof/pto/PtoStatementOfFactsView.kt                | Changed package to `sof.pto`, added import of base view|
| api/src/main/kotlin/.../apiv2/model/sof/StatementOfFactsView.kt                       | Added import for the relocated `PtoStatementOfFactsView`|
</details>



<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/sof/StatementOfFactsView.kt:6**
* Verify that the @JsonSubTypes annotation in this file has been updated to reference the new `nl.teqplay.vesselvoyage.apiv2.model.sof.pto.PtoStatementOfFactsView` class. If the subtype mapping wasn’t adjusted, Jackson deserialization for the PTO variant will fail.
```
import nl.teqplay.vesselvoyage.apiv2.model.sof.pto.PtoStatementOfFactsView
```
</details>

### Darius-Wattimena — APPROVED (2025-05-16)

_No comment._

---
id: github:teqplay/poma-backend:pr:234
source: github
type: pull_request
repo: teqplay/poma-backend
number: 234
title: TCC-749 Addition of alternative names field
author: TeqJoostD
state: closed
date: '2026-02-16'
merged_at: '2026-02-17'
base_branch: develop
head_branch: TCC-749
url: https://github.com/teqplay/poma-backend/pull/234
labels: []
linked_issues: []
explicit_links: []
---
# PR #234: TCC-749 Addition of alternative names field

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/234  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-749`  
**Created:** 2026-02-16  
**Merged:** 2026-02-17  

## Description

_No description._

## Commits

- `00141779` **TeqJoostD** (2026-02-16): Addition of alternative names field

## Reviews

### github-actions[bot] — COMMENTED (2026-02-16)

The addition of the `alternativeNames` field is well-structured and properly integrated into the data models and conversion methods shown in this PR.

However, I noticed that the `convertWopBerthToBerth` method in `BerthService.kt` (not modified in this PR) doesn't map the `alternativeName` field from `BerthData` to the new `alternativeNames` field. The `BerthData` class has an `alternativeName: String?` field that should be converted to a list when importing berth data from World of Ports. Consider adding `alternativeNames = listOfNotNull(berth.alternativeName),` after line 577 in that method to ensure WOP imports capture alternative names.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-02-16)

## Pull request overview

This pull request adds an `alternativeNames` field to the Berth model to support storing multiple names by which a berth may be known. The implementation follows a clean three-layer architecture pattern: base model, service layer, and API model.

**Changes:**
- Added `alternativeNames` field to the Berth base model with documentation
- Updated BerthService to sanitize alternativeNames to uppercase and handle model conversions
- Added alternativeNames field to the API Berth model with matching documentation

### Reviewed changes

Copilot reviewed 3 out of 3 changed files in this pull request and generated 2 comments.

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/poma/model/basemodels/Berth.kt | Added alternativeNames field to primary constructor and updated secondary constructor to include the new parameter |
| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/berth/BerthService.kt | Added sanitization logic to uppercase alternativeNames and included the field in model conversion methods |
| api/src/main/kotlin/nl/teqplay/poma/api/v1/Berth.kt | Added alternativeNames field to API model with consistent documentation |





---

💡 <a href="/teqplay/poma-backend/new/develop/.github/instructions?filename=*.instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add Copilot custom instructions</a> for smarter, more guided reviews. <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn how to get started</a>.

### michel-teqplay — APPROVED (2026-02-16)

_No comment._

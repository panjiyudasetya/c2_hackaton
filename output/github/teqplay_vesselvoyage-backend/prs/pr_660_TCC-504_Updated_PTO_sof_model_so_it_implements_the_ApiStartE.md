---
id: github:teqplay/vesselvoyage-backend:pr:660
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 660
title: TCC-504 Updated PTO sof model so it implements the ApiStartEnd for all fields
author: Darius-Wattimena
state: closed
date: '2025-11-07'
merged_at: '2025-11-07'
base_branch: develop
head_branch: TCC-504-fix-api-models
url: https://github.com/teqplay/vesselvoyage-backend/pull/660
labels: []
linked_issues: []
explicit_links: []
---
# PR #660: TCC-504 Updated PTO sof model so it implements the ApiStartEnd for all fields

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/660  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-504-fix-api-models`  
**Created:** 2025-11-07  
**Merged:** 2025-11-07  

## Description

_No description._

## Commits

- `e7c0bda6` **Darius Wattimena** (2025-11-07): Updated PTO sof model so it implements the ApiStartEnd for all fields

## Reviews

### TeqJoostD — APPROVED (2025-11-07)

_No comment._

### github-actions[bot] — COMMENTED (2025-11-07)

Review completed. No suggestions at this time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-11-07)

## Pull Request Overview

This PR adds the `ApiStartEnd` interface implementation to three data classes in the PTO Statement of Facts view model. The changes bring consistency to the model by ensuring all time-based entities implement the same interface.

- Adds `ApiStartEnd` interface implementation to `UnclassifiedStop`, `ApproachAreaVisit`, and `ShipToShipTransfer`
- Marks `start` and `end` properties as `override` for these classes

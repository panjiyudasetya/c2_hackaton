---
id: github:teqplay/poma-backend:pr:207
source: github
type: pull_request
repo: teqplay/poma-backend
number: 207
title: 'FIX: add polygon validation'
author: TeqJoostD
state: closed
date: '2025-09-04'
merged_at: '2025-09-04'
base_branch: develop
head_branch: polygon-validation
url: https://github.com/teqplay/poma-backend/pull/207
labels: []
linked_issues: []
explicit_links: []
---
# PR #207: FIX: add polygon validation

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/207  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `polygon-validation`  
**Created:** 2025-09-04  
**Merged:** 2025-09-04  

## Description

_No description._

## Commits

- `25f04c97` **TeqJoostD** (2025-09-04): add polygon validation
- `7dcc5ffb` **TeqJoostD** (2025-09-04): fix: ktlint

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-09-04)

## Pull Request Overview

This PR adds polygon validation to the InfrastructureController to ensure that geographic areas meet basic geometric requirements for valid polygons. The validation checks that polygons have sufficient points, are properly closed, and contain enough unique vertices.

- Adds polygon validation for ApiInnerArea and ApiOuterArea models
- Implements validation rules for minimum points, closure, and unique vertices
- Integrates validation into all model modification endpoints





---

<sub>**Tip:** Customize your code reviews with copilot-instructions.md. <a href="/teqplay/poma-backend/new/develop/.github?filename=copilot-instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Create the file</a> or <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">learn how to get started</a>.</sub>

### Darius-Wattimena — APPROVED (2025-09-04)

_No comment._

## Review Comments

### Copilot — 2025-09-04 on `src/main/kotlin/nl/teqplay/poma/generics/InfrastructureController.kt`

The validation logic uses instanceof checks which can become difficult to maintain as new area types are added. Consider using polymorphism by adding a validation method to the model interfaces or using a when expression for better type safety.
```suggestion
        model.validatePolygons()
    }

    companion object {
        fun validatePolygonList(area: List<Location>, fieldName: String) {
            if (area.isEmpty()) return // empty areas are allowed; skip validation
            if (area.size < 4) {
                throw BadRequestException("$fieldName must have at least 4 points (3 unique vertices plus the closing point)")
            }
            if (area.first() != area.last()) {
                throw BadRequestException("$fieldName must be closed: first point must equal last point")
            }
            val uniqueVertices = area.dropLast(1).distinct()
            if (uniqueVertices.size < 3) {
                throw BadRequestException("$fieldName must contain at least 3 unique vertices before the closing point")
            }
        }
```

### Copilot — 2025-09-04 on `src/main/kotlin/nl/teqplay/poma/generics/InfrastructureController.kt`

The validation performs multiple list operations that could be optimized. The `area.first()`, `area.last()`, `area.dropLast(1).distinct()` operations each iterate through the list. Consider combining these checks or using more efficient approaches for large polygon datasets.

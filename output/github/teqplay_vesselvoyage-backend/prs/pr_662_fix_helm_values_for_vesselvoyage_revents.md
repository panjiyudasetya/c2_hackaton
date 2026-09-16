---
id: github:teqplay/vesselvoyage-backend:pr:662
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 662
title: fix helm values for vesselvoyage revents
author: Jamie-de-Leest
state: closed
date: '2025-11-07'
merged_at: '2025-11-07'
base_branch: develop
head_branch: fix-vesselvoyage-helm-values
url: https://github.com/teqplay/vesselvoyage-backend/pull/662
labels: []
linked_issues: []
explicit_links: []
---
# PR #662: fix helm values for vesselvoyage revents

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/662  
**State:** closed | **Author:** Jamie-de-Leest  
**Base ← Head:** `develop` ← `fix-vesselvoyage-helm-values`  
**Created:** 2025-11-07  
**Merged:** 2025-11-07  

## Description

_No description._

## Commits

- `6b4b3c82` **Jamie de Leest** (2025-11-07): fix helm values for vesselvoyage revents
- `70c59649` **Jamie de Leest** (2025-11-07): chore: cleanup
- `00a5d07e` **Jamie de Leest** (2025-11-07): helm value fixes

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-11-07)

## Pull Request Overview

This PR introduces configuration changes for Helm values files across development and production environments. The main change involves removing the `storageClass` configuration from production and adding a complete dev environment configuration file.

- Removes `storageClass` configuration from production environment
- Adds complete Helm values configuration for development environment including MongoDB, ingress, and resource settings

### Reviewed Changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated no comments.

| File | Description |
| ---- | ----------- |
| helm/values.revents-prod.yaml | Removes the MongoDB persistence storageClass configuration |
| helm/values.revents-dev.yaml | Adds new complete configuration file for dev environment with MongoDB, ingress, resources, and Atlas settings |


<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**helm/values.revents-dev.yaml:15**
* Inconsistent naming convention for storage class configuration. The production file uses `storageClass` (camelCase), but this dev file uses `storageclass` (lowercase). Use `storageClass` to maintain consistency across environments.
</details>

### Darius-Wattimena — CHANGES_REQUESTED (2025-11-07)

_No comment._

### github-actions[bot] — COMMENTED (2025-11-07)

Review completed. Found several configuration issues that should be addressed:

## Issues Identified:

### 1. storageClass Casing Issue (helm/values.revents-dev.yaml, line 15)
The property name should be `storageClass` (with capital C) to match Kubernetes conventions and other files in this repository. Currently it's `storageclass` (lowercase).

### 2. Production Environment Configuration (helm/values.revents-prod.yaml)
The production configuration appears to be using development environment settings:
- `hostedzone: dev.teqplay.dev` (line 15) - should likely be a production domain
- `group: eks-dev` (line 19) - should likely be `eks-prod` or similar for production

### 3. Storage Class Inconsistency
The production file had `storageClass` removed while the development file includes it (with incorrect casing). Consider whether both environments should have consistent storage class configuration.

These issues should be addressed to ensure proper environment separation and consistency with existing configuration patterns.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on this comment to provide feedback on its usefulness.*

### Darius-Wattimena — CHANGES_REQUESTED (2025-11-07)

_No comment._

### github-actions[bot] — COMMENTED (2025-11-07)

Review completed. Found several configuration inconsistencies that should be addressed for proper deployment.

### github-actions[bot] — COMMENTED (2025-11-07)

The changes correctly fix the storageClass typo and remove dev-specific configuration from prod. However, the prod file is missing some standard production configurations.

### Darius-Wattimena — APPROVED (2025-11-07)

_No comment._

## Review Comments

### Darius-Wattimena — 2025-11-07 on `helm/values.revents-dev.yaml`

```suggestion
    storageClass: gp3-retained
```

### Darius-Wattimena — 2025-11-07 on `helm/values.revents-prod.yaml`

```suggestion
  hostedzone: teqplay.dev
```

### Darius-Wattimena — 2025-11-07 on `helm/values.revents-prod.yaml`

also wrong should be prod things not DEV?

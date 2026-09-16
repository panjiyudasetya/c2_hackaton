---
id: github:teqplay/vesselvoyage-backend:pr:653
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 653
title: Migrate VesselVoyage to new dev cluster
author: Joost1991
state: closed
date: '2025-10-28'
merged_at: '2025-10-28'
base_branch: develop
head_branch: migrate/vesselvoyage
url: https://github.com/teqplay/vesselvoyage-backend/pull/653
labels: []
linked_issues: []
explicit_links: []
---
# PR #653: Migrate VesselVoyage to new dev cluster

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/653  
**State:** closed | **Author:** Joost1991  
**Base ← Head:** `develop` ← `migrate/vesselvoyage`  
**Created:** 2025-10-28  
**Merged:** 2025-10-28  

## Description

_No description._

## Commits

- `0acd6eed` **Joost Laurman** (2025-10-27): Migration to new dev cluster
- `9665dbe9` **Joost Laurman** (2025-10-28): Actions branch merged, so moving to master branch again

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-28)

## Pull Request Overview

This PR migrates the VesselVoyage application to a new development cluster by updating Helm configuration values. The migration removes the global namespace and storage class overrides in favor of environment-specific ingress and MongoDB configurations.

Key changes:
- Replaces global cluster configuration with explicit ingress settings including AWS certificate ARN, security groups, and subnets
- Updates MongoDB persistence settings with new storage class and hosted zone configuration for the processing environment

### Reviewed Changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated 1 comment.

| File | Description |
| ---- | ----------- |
| helm/values.processing-dev.yaml | Adds new cluster ingress configuration and updates MongoDB persistence settings with gp3-retained storage class and hosted zone |
| helm/values.api-dev.yaml | Adds new cluster ingress configuration matching the processing environment setup |

### TeqJoostD — APPROVED (2025-10-28)

_No comment._

## Review Comments

### Copilot — 2025-10-28 on `helm/values.processing-dev.yaml`

The field name 'hostedzone' should be 'hostedZone' to follow camelCase naming convention consistently used in Kubernetes/Helm configurations.
```suggestion
  hostedZone: dev.teqplay.dev
```

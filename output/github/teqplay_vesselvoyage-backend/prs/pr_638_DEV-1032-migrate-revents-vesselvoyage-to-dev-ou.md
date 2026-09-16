---
id: github:teqplay/vesselvoyage-backend:pr:638
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 638
title: DEV-1032-migrate-revents-vesselvoyage-to-dev-ou
author: Jamie-de-Leest
state: closed
date: '2025-10-15'
merged_at: '2025-10-20'
base_branch: develop
head_branch: DEV-1032-migrate-revents-vesselvoyage-to-dev-ou
url: https://github.com/teqplay/vesselvoyage-backend/pull/638
labels: []
linked_issues: []
explicit_links: []
---
# PR #638: DEV-1032-migrate-revents-vesselvoyage-to-dev-ou

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/638  
**State:** closed | **Author:** Jamie-de-Leest  
**Base ← Head:** `develop` ← `DEV-1032-migrate-revents-vesselvoyage-to-dev-ou`  
**Created:** 2025-10-15  
**Merged:** 2025-10-20  

## Description

_No description._

## Commits

- `7f606b15` **Jamie de Leest** (2025-10-15): feat: update github actions workflow and helm values for revents migration to dev ou

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-15)

## Pull Request Overview

This PR migrates the vesselvoyage application from the revents environment to a dev organizational unit, restructuring Helm configuration files and GitHub workflow secrets to support the new deployment environment.

- Removed global configuration from base values files and distributed it to environment-specific files
- Added new ingress configuration and storage settings for the revents environment
- Updated GitHub workflow to include new AWS credentials for the develop cluster

### Reviewed Changes

Copilot reviewed 8 out of 8 changed files in this pull request and generated 2 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| helm/values.yaml | Removed global storageClass and namespaceOverride configuration |
| helm/values.revents.yaml | Removed global namespace override, added ingress and storage configuration |
| helm/values.processing-prod.yaml | Added global storageClass and namespaceOverride configuration |
| helm/values.processing-dev.yaml | Added global storageClass and namespaceOverride configuration |
| helm/values.processing-data.yaml | Added global storageClass and namespaceOverride configuration |
| helm/values.api-prod.yaml | Added global storageClass and namespaceOverride configuration |
| helm/values.api-dev.yaml | Added global storageClass and namespaceOverride configuration |
| .github/workflows/main.yml | Added new AWS credentials for develop cluster deployment |
</details>

### Joost1991 — CHANGES_REQUESTED (2025-10-20)

Probably this is already deployed and it might be too late, but have a look if the applications are running `gp3` disks.

### Jamie-de-Leest — COMMENTED (2025-10-20)

_No comment._

### Joost1991 — APPROVED (2025-10-20)

_No comment._

## Review Comments

### Copilot — 2025-10-15 on `helm/values.revents.yaml`

The storage class has been changed from 'gp2' to 'gp3-retained' only for the revents environment while all other environments still use 'gp2'. This inconsistency could lead to confusion and maintenance issues. Consider documenting why revents requires a different storage class or standardizing across environments.
```suggestion
    storageClass: gp2
```

### Copilot — 2025-10-15 on `helm/values.revents.yaml`

[nitpick] The 'hostedzone' field appears to be a configuration value but lacks context. Consider adding a comment explaining its purpose or moving it to a more appropriate section alongside related DNS/ingress configuration.
```suggestion


ingress:
  certificateArn: arn:aws:acm:eu-west-1:704630444514:certificate/715d1cb6-0c1a-4717-8cf1-38afb68b9fd6
  group: eks-dev
  scheme: internet-facing
  securityGroups: sg-0d26e09d2ee59f8c6,sg-09a7040413dd11218
  subnets: subnet-030ca4bb313172e24,subnet-0a8c44f920ea72840
  hostedzone: dev.teqplay.dev
```

### Joost1991 — 2025-10-20 on `helm/values.processing-dev.yaml`

These values shouldn't be in DEV, since we want to use gp3 and the `global` tags should not be used anymore.


### Joost1991 — 2025-10-20 on `helm/values.api-dev.yaml`

These values shouldn't be in DEV, since we want to use gp3 and the `global` tags should not be used anymore.


### Jamie-de-Leest — 2025-10-20 on `helm/values.processing-dev.yaml`

also in the old dev?
because these values where never overwritten from the values.yaml
and because this was only for the revents part i though i should not change the other helm values

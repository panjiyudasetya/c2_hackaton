---
id: github:teqplay/poma-backend:pr:213
source: github
type: pull_request
repo: teqplay/poma-backend
number: 213
title: New cluster
author: Joost1991
state: closed
date: '2025-09-24'
merged_at: '2025-09-26'
base_branch: develop
head_branch: new-cluster
url: https://github.com/teqplay/poma-backend/pull/213
labels: []
linked_issues: []
explicit_links: []
---
# PR #213: New cluster

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/213  
**State:** closed | **Author:** Joost1991  
**Base ← Head:** `develop` ← `new-cluster`  
**Created:** 2025-09-24  
**Merged:** 2025-09-26  

## Description

Changes required for the new dev cluster

## Commits

- `39587355` **Pim van den Toorn** (2025-09-23): Updated the workflow file and helm values for the new cluster
- `916b9e43` **Joost Laurman** (2025-09-24): Change back to master branch for Github Actions

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-09-24)

## Pull Request Overview

This PR configures infrastructure settings for a new development cluster deployment. It adds AWS ingress configuration and storage class settings across sandbox and dev environments, along with updated GitHub Actions credentials for the new cluster.

- Adds ingress configuration with AWS ALB settings for both sandbox and dev environments
- Updates MongoDB storage configuration to use `gp3-retained` storage class in sandbox
- Introduces new AWS credential secrets for the development cluster deployment

### Reviewed Changes

Copilot reviewed 3 out of 3 changed files in this pull request and generated 2 comments.

| File | Description |
| ---- | ----------- |
| helm/values.sandbox.yaml | Adds gp3-retained storage class for MongoDB and AWS ingress configuration |
| helm/values.dev.yaml | Adds AWS ingress configuration matching sandbox settings |
| .github/workflows/main.yml | Adds new AWS credential secrets for development cluster |





---

<sub>**Tip:** Customize your code reviews with copilot-instructions.md. <a href="/teqplay/poma-backend/new/develop/.github?filename=copilot-instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Create the file</a> or <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">learn how to get started</a>.</sub>

## Review Comments

### Copilot — 2025-09-24 on `helm/values.sandbox.yaml`

The AWS resource IDs (certificate ARN, security groups, subnets) are hardcoded across multiple files. Consider extracting these values into a shared configuration or using environment-specific variables to avoid duplication and make maintenance easier.
```suggestion
  certificateArn: {{ requiredEnv "CERTIFICATE_ARN" }}
  group: eks-dev
  scheme: internet-facing
  securityGroups: {{ requiredEnv "SECURITY_GROUPS" }}
  subnets: {{ requiredEnv "SUBNETS" }}
```

### Copilot — 2025-09-24 on `helm/values.dev.yaml`

The ingress configuration is identical between sandbox and dev environments. This duplication makes updates error-prone. Consider using a base configuration with environment-specific overrides or validating that these environments should indeed share the same AWS resources.
```suggestion
# Ingress configuration is inherited from helm/values.base.yaml to avoid duplication.
# Add environment-specific overrides below if needed.
```

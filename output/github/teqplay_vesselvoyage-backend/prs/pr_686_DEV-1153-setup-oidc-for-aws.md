---
id: github:teqplay/vesselvoyage-backend:pr:686
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 686
title: DEV-1153-setup-oidc-for-aws
author: Jamie-de-Leest
state: closed
date: '2025-12-18'
merged_at: '2025-12-19'
base_branch: develop
head_branch: DEV-1153-setup-oidc-for-aws
url: https://github.com/teqplay/vesselvoyage-backend/pull/686
labels: []
linked_issues: []
explicit_links: []
---
# PR #686: DEV-1153-setup-oidc-for-aws

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/686  
**State:** closed | **Author:** Jamie-de-Leest  
**Base ← Head:** `develop` ← `DEV-1153-setup-oidc-for-aws`  
**Created:** 2025-12-18  
**Merged:** 2025-12-19  

## Description

_No description._

## Commits

- `b667f0f5` **Jamie de Leest** (2025-12-18): refactor: update AWS authentication method in build.gradle and related files
- `bd342447` **Jamie de Leest** (2025-12-18): added dev account secret

## Reviews

### github-actions[bot] — COMMENTED (2025-12-18)

Review completed. No suggestions at this time.

### github-actions[bot] — COMMENTED (2025-12-18)

Review completed. The migration from static AWS credentials to OIDC-based authentication appears consistent and complete across all configuration files. No suggestions at this time.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-12-18)

## Pull request overview

This PR migrates AWS authentication from static access keys to OIDC (OpenID Connect) for improved security. The changes remove hardcoded AWS credentials in favor of IAM role-based authentication.

- Replaces `AwsCredentials` with `AwsImAuthentication` in all Gradle build files
- Updates GitHub Actions workflows to use `aws_account_id` secret instead of static access keys
- Removes references to multiple AWS credential pairs (production and development)

### Reviewed changes

Copilot reviewed 5 out of 6 changed files in this pull request and generated 8 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| settings.gradle | Migrates Maven repository authentication from AWS credentials to IAM authentication |
| client/build.gradle | Updates repository and publishing authentication to use IAM instead of credentials |
| build.gradle | Migrates repository authentication from AWS credentials to IAM authentication |
| api/build.gradle | Updates repository and publishing authentication to use IAM instead of credentials |
| .github/workflows/main.yml | Replaces AWS access key/secret key secrets with single account ID for OIDC |
| .github/workflows/coverage.yml | Replaces AWS access key/secret key secrets with single account ID for OIDC |
</details>

### Darius-Wattimena — APPROVED (2025-12-19)

_No comment._

### Joost1991 — APPROVED (2025-12-19)

_No comment._

## Review Comments

### Copilot — 2025-12-18 on `settings.gradle`

The authentication type name appears to have a typo. It should be "awsIam" (AWS Identity and Access Management) instead of "awsIm". The correct Gradle authentication type for AWS IAM roles is "AwsImAuthentication" which stands for IAM, not "Im".

### Copilot — 2025-12-18 on `settings.gradle`

The authentication type name appears to have a typo. It should be "awsIam" (AWS Identity and Access Management) instead of "awsIm". The correct Gradle authentication type for AWS IAM roles is "AwsImAuthentication" which stands for IAM, not "Im".

### Copilot — 2025-12-18 on `client/build.gradle`

The authentication type name appears to have a typo. It should be "awsIam" (AWS Identity and Access Management) instead of "awsIm". The correct Gradle authentication type for AWS IAM roles is "AwsImAuthentication" which stands for IAM, not "Im".

### Copilot — 2025-12-18 on `client/build.gradle`

The authentication type name appears to have a typo. It should be "awsIam" (AWS Identity and Access Management) instead of "awsIm". The correct Gradle authentication type for AWS IAM roles is "AwsImAuthentication" which stands for IAM, not "Im".

### Copilot — 2025-12-18 on `client/build.gradle`

The authentication type name appears to have a typo. It should be "awsIam" (AWS Identity and Access Management) instead of "awsIm". The correct Gradle authentication type for AWS IAM roles is "AwsImAuthentication" which stands for IAM, not "Im".

### Copilot — 2025-12-18 on `api/build.gradle`

The authentication type name appears to have a typo. It should be "awsIam" (AWS Identity and Access Management) instead of "awsIm". The correct Gradle authentication type for AWS IAM roles is "AwsImAuthentication" which stands for IAM, not "Im".

### Copilot — 2025-12-18 on `api/build.gradle`

The authentication type name appears to have a typo. It should be "awsIam" (AWS Identity and Access Management) instead of "awsIm". The correct Gradle authentication type for AWS IAM roles is "AwsImAuthentication" which stands for IAM, not "Im".

### Copilot — 2025-12-18 on `api/build.gradle`

The authentication type name appears to have a typo. It should be "awsIam" (AWS Identity and Access Management) instead of "awsIm". The correct Gradle authentication type for AWS IAM roles is "AwsImAuthentication" which stands for IAM, not "Im".
```suggestion
                        awsIam(AwsIamAuthentication)
```

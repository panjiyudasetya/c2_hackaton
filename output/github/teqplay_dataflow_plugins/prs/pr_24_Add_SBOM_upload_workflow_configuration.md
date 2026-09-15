---
id: github:teqplay/dataflow_plugins:pr:24
source: github
type: pull_request
repo: teqplay/dataflow_plugins
number: 24
title: Add SBOM upload workflow configuration
author: Jamie-de-Leest
state: closed
date: '2025-12-15'
merged_at: '2025-12-15'
base_branch: develop
head_branch: sbom-upload-workflow
url: https://github.com/teqplay/dataflow_plugins/pull/24
labels: []
linked_issues: []
explicit_links: []
---
# PR #24: Add SBOM upload workflow configuration

**Repo:** teqplay/dataflow_plugins  
**URL:** https://github.com/teqplay/dataflow_plugins/pull/24  
**State:** closed | **Author:** Jamie-de-Leest  
**Base ← Head:** `develop` ← `sbom-upload-workflow`  
**Created:** 2025-12-15  
**Merged:** 2025-12-15  

## Description

_No description._

## Commits

- `aa146aa7` **Jamie de Leest** (2025-12-15): Add SBOM upload workflow configuration

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-12-15)

## Pull request overview

This PR adds a new GitHub Actions workflow to automate Software Bill of Materials (SBOM) generation and upload for the dataflow-plugins Python project. The workflow integrates with a centralized SBOM management system using a reusable workflow from the teqplay/actions repository.

**Key changes:**
- Adds automated SBOM upload workflow triggered on pushes to master and develop branches
- Integrates with teqplay's centralized workflow infrastructure for Python SBOM generation
- Configures DT_API_KEY secret for authentication with the SBOM upload service





---

💡 <a href="/teqplay/dataflow_plugins/new/develop/.github/instructions?filename=*.instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add Copilot custom instructions</a> for smarter, more guided reviews. <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn how to get started</a>.

### panjiyudasetya — APPROVED (2025-12-15)

LGTM!

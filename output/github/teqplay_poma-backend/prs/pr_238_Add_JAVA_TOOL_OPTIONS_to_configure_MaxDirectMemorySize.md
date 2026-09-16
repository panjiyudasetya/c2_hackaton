---
id: github:teqplay/poma-backend:pr:238
source: github
type: pull_request
repo: teqplay/poma-backend
number: 238
title: Add JAVA_TOOL_OPTIONS to configure MaxDirectMemorySize
author: Darius-Wattimena
state: closed
date: '2026-02-20'
merged_at: '2026-02-20'
base_branch: develop
head_branch: direct-memory-buffer
url: https://github.com/teqplay/poma-backend/pull/238
labels: []
linked_issues: []
explicit_links: []
---
# PR #238: Add JAVA_TOOL_OPTIONS to configure MaxDirectMemorySize

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/238  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `direct-memory-buffer`  
**Created:** 2026-02-20  
**Merged:** 2026-02-20  

## Description

_No description._

## Commits

- `8d276cd8` **Darius Wattimena** (2026-02-20): Add JAVA_TOOL_OPTIONS to configure MaxDirectMemorySize

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-02-20)

## Pull request overview

This PR adds JVM configuration to limit the maximum direct memory size for the Java/Kotlin Spring Boot application running in Kubernetes. The change sets the `JAVA_TOOL_OPTIONS` environment variable with `-XX:MaxDirectMemorySize=512m` through the Helm values configuration.

**Changes:**
- Adds `env` section to helm/values.yaml with JAVA_TOOL_OPTIONS environment variable configuring MaxDirectMemorySize to 512m





---

💡 <a href="/teqplay/poma-backend/new/develop/.github/instructions?filename=*.instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add Copilot custom instructions</a> for smarter, more guided reviews. <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn how to get started</a>.

### TeqJoostD — APPROVED (2026-02-20)

_No comment._

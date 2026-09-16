---
id: github:teqplay/vesselvoyage-backend:pr:547
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 547
title: GitHub instructions
author: TeqJoostD
state: closed
date: '2025-07-02'
merged_at: '2025-07-02'
base_branch: develop
head_branch: github-instructions
url: https://github.com/teqplay/vesselvoyage-backend/pull/547
labels: []
linked_issues: []
explicit_links: []
---
# PR #547: GitHub instructions

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/547  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `github-instructions`  
**Created:** 2025-07-02  
**Merged:** 2025-07-02  

## Description

_No description._

## Commits

- `62fb3221` **TeqJoostD** (2025-07-02): feat: add copilot instructions
- `7df6a48b` **TeqJoostD** (2025-07-02): Merge remote-tracking branch 'origin/develop' into develop

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-02)

## Pull Request Overview

This PR adds a new Markdown file defining standardized Copilot code review guidelines across clarity, naming, error handling, performance, security, testing, logging, modularity, and API practices.

- Introduces high-level sections on code readability, naming conventions, error handling, and performance.
- Defines testing, logging, and modularity best practices.
- Specifies API standards for empty fields, date formats, and not-found responses.


<details>
<summary>Comments suppressed due to low confidence (3)</summary>

**.github/copilot-instructions.md:1**
* [nitpick] The main header is ambiguous—consider renaming to 'GitHub Copilot Code Review Guidelines' to clarify the affiliation.
```
# Copilot Code Review Guidelines
```
**.github/copilot-instructions.md:43**
* [nitpick] Consider clarifying how serializers in different languages handle `undefined` fields—some frameworks may omit them automatically, others may require explicit omit configurations.
```
Empty fields should not be returned through the endpoint. Always leave them undefined so they are not included in the response.  
```
**.github/copilot-instructions.md:54**
* Recommend specifying that APIs should return a proper HTTP 404 status code (with optional error body) rather than a literal string '404: Not Found' to align with common REST practices.
```
- If searching for a single item and nothing is found, return `404: Not Found`.
```
</details>

### leonjoosse — DISMISSED (2025-07-02)

_No comment._

### Darius-Wattimena — APPROVED (2025-07-02)

_No comment._

## Review Comments

### leonjoosse — 2025-07-02 on `.github/copilot-instructions.md`

Huh? I thought we do return fields that are empty / null?

### leonjoosse — 2025-07-02 on `.github/copilot-instructions.md`

Null or 0 could mean something, it is not necessarily 'empty'. For example, a speed of 0...

### leonjoosse — 2025-07-02 on `.github/copilot-instructions.md`

Should we make this explicit with `java.time.Instant`?

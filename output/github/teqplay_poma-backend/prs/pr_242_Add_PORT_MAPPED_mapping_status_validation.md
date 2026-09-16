---
id: github:teqplay/poma-backend:pr:242
source: github
type: pull_request
repo: teqplay/poma-backend
number: 242
title: Add PORT_MAPPED mapping status validation
author: TeqJoostD
state: closed
date: '2026-03-19'
merged_at: '2026-03-23'
base_branch: develop
head_branch: port-mapped-status-update
url: https://github.com/teqplay/poma-backend/pull/242
labels: []
linked_issues: []
explicit_links: []
---
# PR #242: Add PORT_MAPPED mapping status validation

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/242  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `port-mapped-status-update`  
**Created:** 2026-03-19  
**Merged:** 2026-03-23  

## Description

## Summary
- add the shared `PORT_MAPPED` mapping status value after `BASIC_MAPPED`
- update `PortModelValidatorService` thresholds for `PORT_MAPPED`, `BASIC_MAPPED`, and `FULLY_MAPPED`
- make `PORT_MAPPED` require valid required port fields, `area`, `outerArea`, and existing `eosAreaValidity`
- expose `outerArea` in the port validation report where needed by the follow-up
- add regression coverage for mapping-status behavior and edge cases

## Verification
- `export JAVA_HOME=$(/usr/libexec/java_home -v 17) && export PATH="$JAVA_HOME/bin:$PATH" && ./gradlew test --tests nl.teqplay.poma.feature.infrastructure.port.validation.PortModelValidatorServiceTest`
- `export JAVA_HOME=$(/usr/libexec/java_home -v 17) && export PATH="$JAVA_HOME/bin:$PATH" && ./gradlew test --tests nl.teqplay.poma.feature.mapping.MappingServiceTest`
- `export JAVA_HOME=$(/usr/libexec/java_home -v 17) && export PATH="$JAVA_HOME/bin:$PATH" && ./gradlew ktlintCheck`
- `export JAVA_HOME=$(/usr/libexec/java_home -v 17) && export PATH="$JAVA_HOME/bin:$PATH" && ./gradlew ktlintFormat`

## Notes
- In this workspace the default shell JDK is 21, so Gradle verification was run with JDK 17 to avoid the local JVM target mismatch (`compileJava` 21 vs `compileKotlin` 17).
- `BASIC_MAPPED` still relies on `portCompleteValid`, so it does not newly require `outerArea`.

## Commits

- `66c779da` **Augment Test** (2026-03-19): Add PORT_MAPPED mapping status
  Agent-Id: agent-302914ba-1850-4e40-9e12-096a219c8004
- `afef472b` **Augment Test** (2026-03-19): Require outerArea and eosArea for PORT_MAPPED
  Agent-Id: agent-302914ba-1850-4e40-9e12-096a219c8004
- `acc43cb2` **TeqJoostD** (2026-03-23): Add new status to mapping overview

## Reviews

### augmentcode[bot] — COMMENTED (2026-03-19)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fpoma-backend%2Fpull%2F242%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### Darius-Wattimena — APPROVED (2026-03-23)

_No comment._

## Review Comments

## Comments

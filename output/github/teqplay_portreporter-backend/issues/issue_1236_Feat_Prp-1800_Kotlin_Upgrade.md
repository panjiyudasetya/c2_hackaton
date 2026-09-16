---
id: github:teqplay/portreporter-backend:issue:1236
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1236
title: Feat/Prp-1800/Kotlin Upgrade
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1236
labels: []
explicit_links: []
---
# Issue #1236: Feat/Prp-1800/Kotlin Upgrade

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1236  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [527a8d5b321d...289e06963b6c](https://github.com/teqplay/portreporter-backend/compare/527a8d5b321d...289e06963b6c)
**Merge commit:** [289e06963b6c](https://github.com/teqplay/portreporter-backend/commit/289e06963b6c)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Wouter Naloop, Shan Minh Nguyen
**Approvers:** Wouter Naloop
**Source Branch:** [feat/PRP-1800/kotlin_upgrade](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-1800/kotlin_upgrade)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-03-16T14:29:41.051656+00:00
**Status:** MERGED

**Changes:**
* **First commit:** Minimal changes to upgrade kotlin to 1.8. It requires IntelliJ 2022.3.3 or the Kotlin 1.8 plugin installed in a compatible IntelliJ version.
* Next 2 commits: Some unneeded libraries got remove: kotlin-stdlib and kotlin-reflect.
* **Last commit**: included in the minimal changes, but discovered afterwards: springboot needed to be upgraded.
**Note** that the following 4 files were automatically updated by the command `./gradlew wrapper --gradle-version 8.0`, so don’t waste your time :slight_smile: :
* `gradle/wrapper/gradle-wrapper.jar`
* `gradle/wrapper/gradle-wrapper.properties`
* `gradlew`
* `gradle.bat`
Thanks in advance


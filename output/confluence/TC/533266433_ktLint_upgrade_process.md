---
id: confluence:533266433
source: confluence
type: page
space: TC
title: ktLint upgrade process
author: Joost Laurman
date: '2024-12-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/533266433
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/533266433
---
# ktLint upgrade process

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/533266433  

## Content

This guide will take you into the process of upgrading ktLint to the newest version.

The `.editorconfig` can be found [here](https://bitbucket.org/teqplay/cargooptima-backend/src/f6a77d70c0334e1847f091964f1287d3cba1a654/.editorconfig).

1. Upgrade ktlint dependency to `12.1.2`
2. Add this to the gradle build file, below the `apply plugin: "org.jlleitschuh.gradle.ktlint"` line.  
     
   **Groovy**

ktlint {
version("1.3.1")
}

**Kotlin**

configure<org.jlleitschuh.gradle.ktlint.KtlintExtension> {
version.set("1.3.1")
}

3. If you have problems with caching, add this instead:

   // Hotfix for bug in ktlint where cached files in buildSrc modules are being checked
   configure<org.jlleitschuh.gradle.ktlint.KtlintExtension> {
   version.set("1.3.1")
   enableExperimentalRules.set(true)
   filter {
   exclude { element ->
   val path = element.file.path
   path.contains("\\build\\") || path.contains("/build/")
   }
   }
   }
4. Add the `.editorconfig` to the root of the project. This file will update the ruleset that the linter uses.
5. Do a `gradle ktlintCheck` in the terminal or IDE
6. Fix the issues, that you are encountering because of the new rules, in a seperate branch

   1. If you are using `_id`, add this annotation to it: `@Suppress("ktlint:standard:property-naming")`
7. Make someone else review it and merge
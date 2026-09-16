---
id: confluence:816775170
source: confluence
type: page
space: TC
title: TP Authorization
author: Joaquin Marquez Bugella
date: '2025-08-01'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/816775170
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/816775170
---
# TP Authorization

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/816775170  

## Content

Terminal planner’s authorization is based on the Spring annotation `@PreAuthorize` **applied on the Controller** layer, where the logic is defined in the class `AuthorizationConfiguration`, using a ***permissions map*** defined in the `Resource` object (in the `Role.kt` file).

Thus, the execution of a controller depends on:

* the **user roles**,
* type of **target object** to act
* the **type of operation** (CRUD)
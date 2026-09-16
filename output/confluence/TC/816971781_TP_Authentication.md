---
id: confluence:816971781
source: confluence
type: page
space: TC
title: TP Authentication
author: Joaquin Marquez Bugella
date: '2025-08-01'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/816971781
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/816971781
---
# TP Authentication

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/816971781  

## Content

Currently, users authenticates via **Platform** with a shared token mechanism.

It is implemented in the `AuthenticationService` by using the `PlatformRestTemplate` and `SharedSecretTokenService` from the skeleton plugin libraries.

**Note** that a plan to use Keycloak is being designed to replace Platform by Keycloak.

Users must be created in both: Platform authentication service and Terminal Planner `users_v2` collection, where users and their roles are defined.
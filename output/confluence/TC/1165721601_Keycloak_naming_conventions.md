---
id: confluence:1165721601
source: confluence
type: page
space: TC
title: Keycloak naming conventions
author: Joost Laurman
date: '2026-03-27'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1165721601
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1165721601
---
# Keycloak naming conventions

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1165721601  

## Content

Always name the *clientId* after the service you are going to use it for. So, if you are creating a client to connect from VesselVoyage to CSI, you are naming the client `vesselvoyage`. It will be granted access to the `csi` application.

**Never** use the `vesselvoyage` client in any other project.

## Local development

For **local** development, please use the `local` prefix. So for your own local account it will be `local-<name>` to indicate this key is only used for local development purposes.
---
id: confluence:192315393
source: confluence
type: page
space: TC
title: Keycloak user-based authentication proposal
author: Darius Wattimena
date: '2023-07-07'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/192315393
explicit_links: []
---
# Keycloak user-based authentication proposal

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/192315393  

## Content

This proposal will describe how user-based authentication will be done using Keycloak. We currently use Auth0 for most front-end applications to authenticate. (With some exceptions using the Authenticator of Platform like PortReporter and TerminalPlanner)

# Authentication

1. Credentials never go through our internal API, external API or backends directly. Instead, it will be handled and go through Keycloak.
2. As a starting point: no unauthorized calls (are needed) in the API.
3. The token will be validated twice (API + backend). Accepted minimum overhead. Security has priority.
4. End-user applications (initially) do not have to go through the API.

Front-end authentication flow with Keycloak

# Authorization

On the side of the API, we will check the following:

1. Is the provided valid token valid?
2. Is the user allowed to access the requested service with the given token?

When the target application is an end-user application:

1. The detailed authorization will be done internally.

When the target application is a core service:

1. Is the provided valid token valid?
2. Is the user allowed to access the requested service with the given token?

   1. On audience level
   2. On scope level, for more fine-grained permissions

Keycloak authorization flow with token

# Data augmentation

1. Core services cannot depend on other core services to provide their primary activity.
2. We could add facilitation services on top of core services to do so.

   1. Latency, hops and dependencies should be taken into account when doing so.
   2. For example, ShipHistory can contain an endpoint to retrieve the current ship data with ship roles from CSI.
3. Be pragmatic: Facilitating on top of the core services is allowed IF it does not interfere with rule nr. 1.

Data flow, timeline asking core services for data

Data flow, timeline asking core service for facilitating endpoint
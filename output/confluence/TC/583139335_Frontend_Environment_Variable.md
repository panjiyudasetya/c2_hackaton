---
id: confluence:583139335
source: confluence
type: page
space: TC
title: Frontend Environment Variable
author: Fauzan Rifqy
date: '2025-01-03'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/583139335
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/583139335
---
# Frontend Environment Variable

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/583139335  

## Content

### DOMAIN\_URI

| Example Value | Description |
| --- | --- |
| `https://routescoutv2.teqplay.dev` | Application's domain for Route Scout v2. |
| `https://routescoutv2dev.teqplay.dev` | Development domain URI for Route Scout v2. |

#### Description

The `DOMAIN_URI` variable specifies the base URI for your application. This is used to define the application's main domain for API calls, redirects, or other domain-specific configurations. Ensure the URI matches your deployment environment (e.g., production, staging, or local development).

---

### SENTRY\_DSN

| Example Value | Description |
| --- | --- |
| `https://95f9b7c594217f5e05411c881ba846fe@o126205.ingest.us.sentry.io/4506903449894912` | Sentry DSN used on timeline-public. |
| `https://207eece7377b9703c547f4aea8cb8225@o126205.ingest.us.sentry.io/4508560620191744` | Sentry DSN used on react-boilerplate. |
| `https://9b13a8ac70b545304f307cdf23362058@o126205.ingest.us.sentry.io/4508572847636480` | Sentry DSN used on poma-v2 |

#### Description

The `SENTRY_DSN` variable holds the Sentry Data Source Name (DSN). This is required for integrating Sentry's error tracking and performance monitoring. Use different DSN values for production and testing environments to segregate error reporting.

#### How to obtain a Sentry DSN

1. Visit the Sentry Website  
   Go to [sentry.io](https://sentry.io).
2. Log in  
   Sign in using developer account credentials. (use bitwarden)
3. Create a New Project

   * Once logged in, navigate to the "Projects" section.
   * Click **Create Project** and enter your project name.
4. Follow the Setup Instructions

   * During the setup process, you will receive your **DSN URL**. Copy it for use in your project.

---

### KEYCLOAK\_AUTH\_URL

| Example Value | Description |
| --- | --- |
| `https://keycloakdev.teqplay.nl/auth/realms/dev` | Keycloak authentication server URL for development. |

#### Description

The `KEYCLOAK_AUTH_URL` variable defines the URL of the Keycloak authentication server. This URL is used by the application to authenticate users and obtain tokens for secure access.

---

### KEYCLOAK\_CLIENT\_ID

| Example Value | Description |
| --- | --- |
| `routescout` | Client ID for Route Scout v2. |
| `react-boilerplate` | Client ID for react-boilerplate. |
| `poma-v2` | Client ID for POMA v2 |

#### Description

The `KEYCLOAK_CLIENT_ID` variable specifies the Keycloak Client ID associated with the application. This is required for the app to communicate with the Keycloak authentication server and authorize users.

#### How to obtain Keycloak Client ID

Reach out:
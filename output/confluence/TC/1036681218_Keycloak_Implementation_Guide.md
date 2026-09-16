---
id: confluence:1036681218
source: confluence
type: page
space: TC
title: Keycloak Implementation Guide
author: Michel Wilson
date: '2025-12-17'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1036681218
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1036681218
---
# Keycloak Implementation Guide

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1036681218  

## Content

# Architecture overview

The system revolves around a single Keycloak realm that serves as the identity and authorization provider for all applications. Users authenticate against this realm and receive tokens that the various applications—both frontends and backends—use to establish who the user is and which parts of the system they may access.

The frontend landscape consists entirely of React single-page applications. Each frontend authenticates users using the Authorization Code Flow with PKCE and receives ID, access, and refresh tokens that allow the application to operate without persistent full-page reloads or repeated logins.

Behind the scenes, several Kotlin-based backend services act as resource servers. They consume the access tokens issued to frontends or to other backend systems and validate them using Keycloak’s public keys. These backends enforce both high-level, app-wide access control (e.g., “may this user access Application 1 at all?”) and their own fine-grained domain authorization rules (e.g., “may this user update this particular resource?”).

Both frontends and backends share the same user accounts because everything lives inside a single Keycloak realm. Backends can also read certain user attributes—such as application-specific metadata or identifiers—from tokens or from a local profile database keyed by the user’s Keycloak subject (`sub`), giving each service the freedom to enrich user data with whatever it needs.

# Realm and Client Setup

The Keycloak installation is split across two separate instances: one for development and one for production. Each environment has its own realm containing the same structural configuration—roles, clients, scopes, and mappers—ensuring predictable behavior regardless of the environment.

Within each realm, every application is represented as one or more clients, of different types: one frontend client type, and two different backend client types.

* Frontends appear as **public clients**. These clients do not have secrets, rely on PKCE for security, and define redirect URIs and Web Origins that match the frontends hosting environment. They are configured to use refresh tokens, allowing seamless token renewal within the browser.
* The first backend client type is a **bearer-only client** that represents the API resource server. This client cannot perform login flows; instead, it simply validates incoming access tokens.
* The second backend client type is an optional **confidential client**—only needed for backends that must call other backends. These confidential clients hold client secrets, have service accounts enabled, and use the client credentials flow to obtain machine-to-machine tokens.

To avoid token bloat or cross-application leakage, Keycloak uses **client scopes** to shape tokens. Each application receives its own client scope (for example, `app-1-access` or `app-2-access`). These scopes determine which roles and audiences will appear in tokens issued to each application. Only the scopes explicitly assigned to a frontend or backend contribute to token content.

# User Model and Profiles

All users exist as single entries within the realm. Every frontend and backend uses the same user identity, which enables single sign-on and a unified view of the user across applications. When a user logs into one SPA, other SPAs can rely on the existing Keycloak SSO session to authenticate the user without prompting again.

Keycloak holds only essential identity data—name, email, username, and any shared attributes you choose to store. Backends can choose to maintain their own richer user profiles. These profiles should use the Keycloak `sub` claim as the stable identifier and contain domain-specific information such as internal permissions, organization membership, or user preferences. This approach keeps Keycloak clean while giving services maximum flexibility.

For authorization, realm roles such as `app-1-user` or `app-2-user` are defined. These roles directly encode access to applications and are the main switch that determines which SPAs and backends a user may interact with. Groups in Keycloak may be used to organize users into categories or to assign roles in bulk.

The information in the Keycloak user profile is mapped into the ID token and Access Token in the following way:

* ID Token (used in the frontend only)

  + identity data (name, email)
  + possible future global user data
* Access token (used in the backend)

  + `sub` containing the id of the user
  + `aud` containing the audience of the token
  + a list of one or more roles

Each application’s client scope maps its corresponding role into the access token’s roles claim and also sets the appropriate audience. This ensures that each token contains only the roles and authorization information relevant to the specific application.

# Application-Level Authorization

At a high level, access to an application is controlled by realm roles. If the roles claim of a user’s token contains `app-1-user`, they are allowed to use Application 1. If not, the application should refuse access.

SPAs enforce this by examining the roles claim after login. Even if a user successfully authenticates, they may still lack the correct role. In such cases, rather than loading the full application, the SPA simply displays a “no access” message or a minimal page explaining the restriction. This avoids coupling UI-level access with backend checks and gives users immediate clarity about their permissions.

Backends enforce the same rule server-side. Spring Security takes the roles from the token, maps them into authorities, and verifies them via annotations like:

wide760@PreAuthorize("hasRole('app-1-user')")

Before Spring can evaluate this expression correctly, a small piece of configuration ensures that Keycloak’s `realm_access.roles` (or other role claims) are converted into Spring’s expected `ROLE_...` authorities.

Alternatively, an authentication filter can be added ensuring that every request to the application contains the correct role for that application.

Client scopes make sure that only the appropriate roles and audiences appear in a token. The scope for Application 1 maps the `app-1-user` role into the token and sets the audience field so that only Backend 1 will accept the token. Applications do not leak each other’s roles unless explicitly configured to do so.

# Fine-Grained Authorization in Backends

Keycloak is deliberately not used to express domain-level rules. Those belong in the backends, where they can be implemented using the backend’s database and business logic. The token simply tells the backend who the caller is, what application-level roles they hold, and any shared identity attributes the system decided to include.

Backends validate tokens automatically through Spring Security, then enforce app-level access through the `@PreAuthorize` annotation. Once that gate is passed, each service uses its own logic—typically based on a user profile retrieved via the user identifier stored in the token’s `sub` claim—to decide what the user can do. This might involve checking ownership of data, validating membership in a project, or consulting permissions stored in the application’s own user profile record.

This approach keeps Keycloak configuration small and stable while letting each backend evolve at its own pace.

# Machine-to-Machine Authorization

Some backends need to call each other. Instead of impersonating users or storing passwords, Keycloak provides service accounts and the client credentials flow. When a backend needs to call another backend, it authenticates using its confidential client credentials and receives an access token.

Service accounts receive roles just like human users. If Backend 1 needs to call Backend 2, you assign the `app-2-user` role to Backend 1’s service account. This ensures consistency: both human users and machine callers must have the same application-level role to access a backend.

The resulting token includes only the roles and audiences relevant to the target backend. Backend 2 then authorizes the request using exactly the same logic it applies to user tokens. This eliminates “special cases” for machines—everything follows one coherent model.

Secrets used for M2M flows should be stored securely (environment variables or secret stores) and rotated periodically. Tokens should remain short-lived, as the cost of refreshing them on the server side is minimal.

# Selective Audiences and Backend Enforcement

The audience claim (`aud`) in the access token identifies which backend(s) the token is meant for. Backends must check this claim explicitly. Even if a token contains the correct roles, it should be rejected if the audience does not include the backend’s client ID.

Client scopes again handle this elegantly. Each application’s scope contains the appropriate audience mappers so that tokens for Application 1 contain only `backend-1` as their audience, unless the app genuinely needs access to additional backends. This ensures tokens remain small and that backends cannot be tricked into accepting tokens meant for other services.

On the backend side, Spring Security is extended with a simple validator that checks that the backend’s client ID appears in the token’s audience list. Combined with role checks and domain logic, this enforces clear separation between applications.

# End-to-End Examples

To illustrate how the pieces fit together, consider a user navigating to SPA 1. The SPA detects no valid tokens and redirects the user to Keycloak. After authenticating, Keycloak issues tokens that contain `app-1-user` (if the user has that role) and declare `backend-1` as the intended audience. SPA 1 inspects the roles claim and decides whether to load the full application or show an access-denied page. When the user interacts with the app, SPA 1 calls Backend 1 using the access token, and Backend 1 validates both the audience and the role before serving the request.

The same user can navigate to SPA 2 and, due to Keycloak’s SSO session, may not need to log in again. SPA 2 receives a new set of tokens tailored to Application 2, containing `app-2-user` and `backend-2` where relevant. Backend 2 authorizes the user using exactly the same mechanisms as Backend 1 but with different roles and audiences.

In an M2M scenario, Backend 1 requests an access token using its client secret. This token contains `app-2-user`—because Backend 1’s service account holds that role—and `backend-2` as the audience. Backend 2 receives the call, validates the token, and enforces access rules exactly as it does for user-based requests.
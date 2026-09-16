---
id: confluence:1084391426
source: confluence
type: page
space: TC
title: 'Proposal: Centralized Developer Access Control for MongoDB Community'
author: Jamie de Leest
date: '2026-02-10'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1084391426
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1084391426
---
# Proposal: Centralized Developer Access Control for MongoDB Community

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1084391426  

## Content

## 1. Objective

The objective of this proposal is to implement a **secure, centralized, and auditable access control model** for MongoDB Community deployments that:

* Eliminates shared or static developer credentials
* Centralizes identity and authentication
* Enforces least-privilege and time-bound access
* Enables fast provisioning and reliable de-provisioning
* Provides full auditability of database access

---

## 2. Scope

This proposal applies to:

* All MongoDB Community clusters used by the organization
* All **human (developer and operator)** access to MongoDB

Out of scope:

* Application and service accounts, which are managed separately per application and database

---

## 3. Constraints

* MongoDB Community Edition does **not** support external identity providers (OIDC, LDAP, SAML)
* MongoDB authentication relies solely on **local users**
* Centralized access control must therefore be implemented **outside MongoDB**

---

## 4. High-Level Architecture

### Components

**Keycloak (Identity Provider)**

* System of record for user identities
* Handles authentication, MFA, and group membership
* Manages onboarding, role changes, and offboarding

**HashiCorp Vault (Access & Secrets Broker)**

* Authenticates users via Keycloak using OIDC
* Authorizes access using Vault policies
* Issues short-lived, dynamic MongoDB credentials
* Sole system permitted to manage MongoDB users

**MongoDB Community Clusters**

* Use local MongoDB users only
* All human users are dynamically created and revoked by Vault
* No manual user management

---

## 5. Access Control Model

### Identity

* Users exist only in **Keycloak**
* Access intent is expressed via Keycloak groups, e.g.:

  + `mongo-readonly`
  + `mongo-readwrite`
  + `mongo-admin`

### Authorization

* Vault maps Keycloak group claims to Vault roles and policies
* Vault policies define:

  + Which MongoDB roles can be requested
  + Which databases can be accessed
  + Credential TTLs

Mapping model:

wide760Keycloak group → Vault role → Vault policy → MongoDB role

MongoDB roles are:

* Scoped to specific databases
* Limited to explicit permissions
* Preferably custom-defined to enforce least privilege

---

## 6. Credential Issuance and Revocation

### Dynamic Credentials

When a user requests access:

1. User authenticates to Vault via Keycloak (OIDC)
2. Vault evaluates group claims
3. Vault generates a **unique MongoDB user** with:

   * Random username
   * High-entropy password
   * Scoped database role
   * Short TTL (between 1 hour and 6 months, tbd)
4. Credentials are returned to the user

### Revocation

* Credentials are automatically revoked when TTL expires
* If the credentials have a longer lifetime, a revocation mechanism is also needed.
* If a user is removed from Keycloak or relevant groups:

  + Vault login is no longer possible
  + No new database credentials can be issued

This guarantees timely access termination.

---

## 7. MongoDB Administrative Credentials

### Vault MongoDB Admin User

* Vault uses a **dedicated MongoDB admin user** (not root)
* This user has only the permissions required to:

  + Create, update, and delete MongoDB users
* Credentials are stored inside Vault
* Vault automatically rotates this password on a defined schedule

No humans or external systems use this account.

---

### MongoDB Root Credentials (Break-Glass)

* MongoDB root credentials are stored in a **Kubernetes Secret** on Initial creation afterwards they are managed by vault
* Access is strictly limited to:

  + DevOps

Root credentials are:

* Used only for bootstrapping, disaster recovery, or emergencies
* Never used for day-to-day access
* Rotated on a scheduled basis and after suspected compromise

---

## 8. Credential Management and Rotation

* All human MongoDB credentials are:

  + Short-lived
  + Dynamically generated
  + Automatically revoked
* Password rotation is implicit through TTL expiration
* Vault-managed admin credentials are rotated automatically
* Root credentials are rotated via controlled operational procedures

---

## 9. Auditing and Compliance

Audit coverage includes:

* **Keycloak**: authentication events and group membership
* **Vault**: credential requests, role usage, issuance, and revocation
* **MongoDB**: user creation, deletion, and database access

This provides end-to-end traceability from identity to database access and supports SOC 2 and similar compliance requirements.

---

## 10. Change Management

* All access changes occur through:

  + Keycloak group membership updates
  + Vault policy or role configuration
* No manual changes are permitted directly in MongoDB
* Vault configuration and policies are version-controlled and reviewed

---

## 11. Summary

This approach:

* Compensates for MongoDB Community’s lack of native identity federation
* Eliminates shared and static developer credentials
* Enforces least-privilege, time-bound access
* Centralizes identity in Keycloak and authorization in Vault
* Provides strong auditability and operational safety

It delivers a secure, scalable, and maintainable access control model aligned with modern security best practices.
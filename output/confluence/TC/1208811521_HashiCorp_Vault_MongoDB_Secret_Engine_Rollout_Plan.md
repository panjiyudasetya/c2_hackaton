---
id: confluence:1208811521
source: confluence
type: page
space: TC
title: HashiCorp Vault MongoDB Secret Engine Rollout Plan
author: Jamie de Leest
date: '2026-05-15'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1208811521
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1208811521
---
# HashiCorp Vault MongoDB Secret Engine Rollout Plan

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1208811521  

## Content

# HashiCorp Vault MongoDB Secret Engine Rollout Plan

## Goal

Roll out the HashiCorp Vault MongoDB Secret Engine across all MongoDB instances to provide:

* Dynamic MongoDB credentials
* Centralized access management
* Automatic credential rotation and revocation

---

# Architecture Decisions

## Separate Secret Engines Per Team

We will create a dedicated MongoDB secret engine per team:

* `mongo-core-components`
* `mongo-project`
* `mongo-data-engineering`
* `mongo-devops`

### Reasoning

Vault policies can only scope ACL permissions cleanly at the secret engine path level. By separating engines per team we achieve:

* Strong logical separation
* Simpler policy management
* Reduced risk of accidental cross-team access
* Easier auditing
* Clear ownership boundaries

Example:

| Team | Secret Engine |
| --- | --- |
| Core Components | `mongo-core-components/` |
| Project | `mongo-project/` |
| Data Engineering | `mongo-data-engineering/` |
| DevOps | `mongo-devops/` |

---

# MongoDB Access Model

## Instance-Wide Roles

Access will be granted at the MongoDB instance level rather than per database.

This means:

* A generated user receives permissions across all databases on the Mongo instance
* No database-scoped roles will be created
* Simpler operational model
* Consistent developer experience

---

# Required MongoDB Roles

The following Vault-managed roles will be available per MongoDB instance.

## Read-Only Role

bashwide760vault write database/roles/<role-name> \
db\_name="<connection-name>" \
creation\_statements='[{"db":"admin","roles":[{"role":"readAnyDatabase","db":"admin"}]}]' \
credential\_type="password" \
default\_ttl="60" \
max\_ttl="60" \
revocation\_statements='[{"db":"admin"}]'

### Purpose

* Read access to all databases
* Analytics
* Debugging
* Reporting

---

## Read/Write Role

bashwide760vault write database/roles/<role-name> \
db\_name="<connection-name>" \
creation\_statements='[{"db":"admin","roles":[{"role":"readWriteAnyDatabase","db":"admin"}]}]' \
credential\_type="password" \
default\_ttl="60" \
max\_ttl="60" \
revocation\_statements='[{"db":"admin"}]'

### Purpose

* Application development
* Standard engineering workflows
* Full read/write access across the instance

---

# MongoDB Requirements

## Vault Admin User

Each MongoDB instance must contain a dedicated Vault administration account.

This account will be used by Vault to dynamically create and revoke MongoDB users.

vault will rotated the credentials automatically for this Vault admin account

### Required Permissions

The Vault admin account must be able to:

* Create users
* Delete users
* Manage roles
* Operate across all databases

Recommended MongoDB role:

* `userAdminAnyDatabase`

for new MongoDB instances this will be created on initial startup

---

# Vault MongoDB Connection Configuration

bashwide760vault write database/config/<connection-name> \
plugin\_name="mongodb-database-plugin" \
connection\_url="mongodb://{{username}}:{{password}}@<mongo-host>:27017/admin?authSource=admin" \
username\_template="{{.DisplayName}}\_{{.RoleName}}\_{{timestamp \"2006-01-02T15:04:05Z\"}}" \
username="<vault-admin-username>" \
password="<vault-admin-password>"

---

# Vault Policy Structure

Policies will be scoped to the team-specific secret engine.

Example for a user allowed to use all roles inside the `mongo-test` secret engine:

hclwide760path "mongo-test/creds/\*" {
capabilities = ["read"]
}
path "mongo-test/roles/\*" {
capabilities = ["read"]
}
path "mongo-test/roles" {
capabilities = ["list"]
}

---

# Recommended Naming Convention

## Secret Engines

textwide760mongo-<team>

Examples:

* `mongo-core-components`
* `mongo-project`
* `mongo-data-engineering`
* `mongo-devops`

---

## Connections

textwide760<instance-name>

Examples:

* `poma-dev`
* `customer-apps-dev`

---

## Roles

textwide760<instance>-<access-level>

Examples:

* `poma-dev-read`
* `customer-apps-dev-readwrite`
* `poma-dev-root`
* `customer-apps-dev-useradmin`

---

# Rollout Phases

## Phase 1 — Preparation

### Tasks

* Inventory all MongoDB instances
* Define ownership per team
* Create Vault admin users on MongoDB instances
* Validate network connectivity from Vault to MongoDB
* Define Vault namespaces/policies if applicable

### Deliverables

* MongoDB inventory
* Ownership mapping
* Vault admin credentials securely stored

---

## Phase 2 — Secret Engine Creation

### Tasks

* Enable one MongoDB secret engine per team
* Configure team-specific Vault ACL policies
* Configure authentication mappings (OIDC, LDAP, etc.)

### Deliverables

* Functional isolated secret engines
* Team policy assignments

---

## Phase 3 — MongoDB Connection Onboarding

### Tasks

* Configure Vault database connections per Mongo instance
* Validate revocation flows

### Deliverables

* Operational dynamic credentials
* Successful automated user lifecycle management

---

## Phase 4 — Role Creation

### Tasks

Create standardized roles for every Mongo instance:

* Read
* ReadWrite
* Root
* UserAdmin

### Deliverables

* Consistent role model across all environments
* Validate credential generation

---

# Security Considerations

## TTL Strategy

Current example TTLs:

time in seconds

textwide760default\_ttl = 60
max\_ttl = 60

This should be reviewed before production rollout.

Recommended:

| Access Type | Suggested TTL |
| --- | --- |
| Read | 1h–8h |
| ReadWrite | 1h–4h |
| UserAdmin | 15m–1h |
| Root | 5m–15m |

# Authorization Matrix

| Team | Namespace | Mongo Instance | Access |
| --- | --- | --- | --- |
| tech-support | all | all databases | read/write |
| core-components | ais-core | `ais-stream-dev-mongodb` | read/write |
| core-components | ais-processing | `ais-diff-dev-mongodb` | read/write |
| core-components | ais-processing | `ais-rabbitmq-dev-mongodb` | read/write |
| core-components | ais-processing | `area-monitor-dev-mongodb` | read/write |
| core-components | ais-processing | `event-history-processor-dev-mongodb` | read/write |
| core-components | ais-processing | `ship-history-processor-dev-mongodb` | read/write |
| core-components | core-service | `customereventpublisher-dev-mongodb` | read/write |
| core-components | core-service | `mongodb-core-service-dev` | read/write |
| core-components | core-service | `poma-dev-mongodb` | read/write |
| core-components | core-service | `poma-sandbox-mongodb` | read/write |
| core-components | core-service | `routescout-graph-dev-mongodb` | read/write |
| core-components | revents-core | `revents-engine-api-mongodb` | read/write |
| core-components | voyage | `vesselvoyage-dev-mongodb` | read/write |
| projects | bunkerplanner | `bunkerplanner-dev-mongodb` | read/write |
| projects | bunkerplanner | `bunkerplanner-test-mongodb` | read/write |
| projects | customer-apps | `mongodb-customer-apps-dev` | read/write |
| projects | customer-apps | `sednaintegration-dev-mongodb` | read/write |
| projects | customer-apps | `vesselcompliance-dev-mongodb` | read/write |
| projects | customer-apps | `vesselcompliance-poc-mongodb` | read/write |
| projects | customer-apps | `vesselcompliance-staging-mongodb` | read/write |
| projects | customer-apps | `vesselmatcher-dev-mongodb` | read/write |
| projects | general-service | `mongodb-general-service-dev` | read/write |
| projects | portcall | `mongodb-portcall-dev` | read/write |
| projects | portcall | `portreporter-testing-mongodb` | read/write |
| projects | portcallone | `portcallone-dev-mongodb` | read/write |
| projects | students | `pdatool-dev-mongodb` | read/write |
| projects | voyage | `smartfleet-dev-mongodb` | read/write |
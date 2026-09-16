---
id: confluence:1180991489
source: confluence
type: page
space: TC
title: Secret Migration Plan
author: Joost Laurman
date: '2026-04-10'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1180991489
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1180991489
---
# Secret Migration Plan

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1180991489  

## Content

## Secret Migration Plan

**Scope:** MongoDB credential management (first), with Keycloak OIDC for Vault access

none

---

### Phase 1 — Vault Infrastructure

This phase is about setting up the initial Hashicorp Vault infrastructure.

* Deploy Vault self-hosted on EKS via Helm, 3-node HA
* AWS KMS key for auto-unseal (to make sure it’s encrypted)
* IRSA role for Vault pods to authenticate to KMS
* Enable audit logging, Kubernetes auth method, and KV v2 secrets engine  
    
  **Proof of concept:**
* Vault is reachable, unseals automatically after a pod restart, and you can read/write a test secret

**DoD:**

* Vault is running in HA mode with 3 healthy nodes
* Vault auto-unseals after a pod restart without manual intervention
* Audit logging is active and writing to a verifiable destination

---

### Phase 2 — Keycloak OIDC Integration

This phase is about connecting Vault towards our existing Keycloak infrastructure.

* Register Vault as an OIDC client in Keycloak
* Enable JWT/OIDC auth method in Vault
* Map Keycloak groups to Vault policies  
    
  **Proof of concept:**
* A team member logs into the Vault UI with their Keycloak account and can only access what their group policy allows

**DoD:**

* All team members can log into Vault UI via Keycloak — no local Vault users
* Group-based policies are enforced and verified (a developer cannot access ops-level paths)
* No static Vault tokens are in use for human access

---

### Phase 3 — MongoDB Dynamic Secrets Setup

This phase is about hooking setting up all the tools required to let Vault manage the MongoDB credentials. Also it’s about trying out TTLs, rotating keys automatically and generating username/password combinations when a developer wants to access the DB.

* Create `vault-admin` MongoDB user via init script
* Enable Database secrets engine and connect Vault to a MongoDB instance
* Define a test role and policy  
    
  **Proof of concept:**
* Manually request dynamic credentials from Vault, verify the user appears in MongoDB, verify it disappears after TTL expiry
* Manually trigger a credential rotation and verify the old credentials are immediately revoked and new ones are issued
* Let a credential reach its TTL naturally and verify MongoDB access with the expired credentials fails

**DoD:**

* Vault can generate dynamic credentials for each MongoDB instance
* Generated users are visible in MongoDB during their TTL and automatically revoked after expiry
* Manual credential rotation works and immediately invalidates the previous credentials
* Each application has its own Vault role with least-privilege MongoDB permissions
* Audit log captures every credential issuance, rotation, and revocation

---

### Phase 4 — Incremental Service Migration

This phase is all about using the External Secret Operator to sync secrets

* Deploy **Vault Secrets Operator (VSO)** — a Kubernetes operator that watches for `ExternalSecret` custom resources and syncs secrets from external sources (in this case Vault) into native Kubernetes Secrets. This means your applications don't need any Vault-specific code — they just read a K8s Secret as they normally would
* Connect VSO to Vault via Kubernetes auth  
    
  **Proof of concept:**
* Spin up a new MongoDB test instance, run a full end-to-end test covering:

  + Vault generates dynamic credentials for the test instance
  + VSO syncs those credentials into a K8s Secret
  + A test service pod uses the synced K8s secret
  + Verify the full chain in the audit log

**DoD:**

* All MongoDB instances using Vault-issued dynamic credentials
* Zero static MongoDB credentials remain in ConfigMaps or Secrets
* Each service uses K8s Secrets synced from the Vault
* Traceability is confirmed — every DB connection can be traced to a specific service in the audit log

---

### Phase 5 — Hardening & Future Expansion

This phase is about developing new documentation for authorization and initial setups and workflows.

* Define **TTLs** and rotation schedules
* Develop an **authorization matrix** — a structured overview of which teams/roles can access which Vault paths, MongoDB instances, and operations. This becomes the source of truth for Vault policy management and maps directly to Keycloak group membership
* Write a **developer runbook for new MongoDB instances** — documenting the end-to-end process of provisioning a new DB from now on, covering: creating the MongoDB instance, provisioning the `vault-admin` user, configuring the Database secrets engine in Vault, defining roles and policies, and setting up the VSO `ExternalSecret` in the service chart
* Write document on how to expand to other secret types beyond MongoDB

**DoD:**

* TTLs are defined and enforced for all dynamic credentials
* Authorization matrix is documented, reviewed by the team, and reflected in actual Vault policies and Keycloak groups
* Developer runbook is written, reviewed, and accessible to the team
* A runbook exists for Vault operations (restart, upgrade, unsealing failure)
* The team has agreed on a process for expanding Vault usage to new secret types
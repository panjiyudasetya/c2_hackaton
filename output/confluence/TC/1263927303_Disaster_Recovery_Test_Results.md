---
id: confluence:1263927303
source: confluence
type: page
space: TC
title: Disaster Recovery Test Results
author: Jamie de Leest
date: '2026-07-02'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1263927303
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1263927303
---
# Disaster Recovery Test Results

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1263927303  

## Content

## Objective

The purpose of this test was to validate the disaster recovery procedure by restoring the Kubernetes cluster and its workloads from AWS Backup and identifying any manual intervention required to fully recover the environment.

---

# Test Summary

| Test Item | Result | Notes |
| --- | --- | --- |
| Restore EKS cluster resources from AWS Backup | ✅ Success | Cluster resources were successfully restored. |
| Persistent Volume restoration | ✅ Success (manual adjustment required) | Volume type must be changed from GP2 to GP3 while preserving the original size. |
| Availability Zone configuration | ✅ Success | Availability Zone had to be manually set to `eu-west-1a`. |
| Worker node provisioning | ✅ Success (configuration issue) | Nodes were created but attached to the wrong security group. |
| Core workloads restored | ⚠️ Partial | Most workloads restored but could not fully start. |
| Vault-dependent applications | ❌ Failed | Vault namespace was not restored, causing missing secrets. |
| OIDC provider restoration | ❌ Failed | OIDC providers (Keycloak integration) were not restored. |
| Services and Ingress resources | ❌ Failed | These resources were missing after restoration. |
| Application accessibility | ❌ Failed | Load Balancer Controller was missing, preventing Service creation. |

---

# Detailed Findings

## 1. Persistent Volume Restoration

### Result

AWS Backup automatically restores Persistent Volumes using the original size.

However:

* The restore process defaults the storage class to **GP2**.
* When changing the storage class to **GP3**, AWS automatically resets the volume size to **100 GB**.

### Resolution

Before changing the storage class:

1. Record the original volume size.
2. Change the storage class to GP3.
3. Manually restore the original volume size.

### Improvement

Document this as a required manual recovery step or automate it if supported by the restore workflow.

---

## 2. Availability Zone

### Result

The restore process requires manually selecting the Availability Zone.

The correct zone is:

wide760eu-west-1a

### Improvement

Include the required Availability Zone in the disaster recovery runbook.

---

## 3. Security Group Configuration

### Result

The restored worker nodes were assigned the security group from the source cluster:

wide760eks-cluster-sg-develop

instead of

wide760eks-cluster-sg-<new-cluster-name>

This causes networking inconsistencies.

this seems to be to be a issue on the side of AWS Backup because this is not something you can manage this is automatically set when creating a cluster and node groups

### Resolution

Update the EKS cluster security group to match the new cluster.

### Improvement

Look into if this is a know bug and if not “Update how we use security groups for our clusters”

---

## 4. Restore Duration

### Result

The full restoration of the core-service namespace required approximately:

> **1 hour**

### Improvement

Communicate the expected recovery time in disaster recovery documentation.

---

## 5. OIDC Provider

### Result

OIDC providers were **not restored**.

This affects authentication integrations such as Keycloak.

### Impact

Keycloak authentication is not available on initial creation of the new cluster but keycloak itself would also be unavailable.

You can still login via AWS is you have the admin role

---

## 6. Vault Secrets

### Result

Most applications failed to start because Vault secrets were unavailable.

This was expected because the Vault namespace was intentionally not restored.

### Impact

Pods entered crash loops or remained unready due to missing secrets.

---

## 7. Missing Services and Ingresses

### Result

Service and Ingress resources were not restored.

Attempting to redeploy them using a Helm upgrade failed.

The following error occurred:

textwide760Error: UPGRADE FAILED: failed to create resource:
Internal error occurred: failed calling webhook "mservice.elbv2.k8s.aws":
failed to call webhook:
Post "https://aws-load-balancer-webhook-service.kube-system.svc:443/mutate-v1-service?timeout=10s":
service "aws-load-balancer-webhook-service" not found

### Root Cause

The AWS Load Balancer Controller was not installed because its not part of the core service namespace.

Without this controller:

* LoadBalancer Services cannot be created.
* Ingress resources cannot be provisioned.

---

# Conclusion

The disaster recovery test successfully restored the core Kubernetes infrastructure and persistent storage, demonstrating that AWS Backup can recover the primary cluster resources. However, several manual recovery steps were required before applications could become fully operational. Key gaps included missing OIDC providers, Services and Ingresses.
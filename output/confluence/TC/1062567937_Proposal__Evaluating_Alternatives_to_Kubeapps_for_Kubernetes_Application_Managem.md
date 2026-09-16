---
id: confluence:1062567937
source: confluence
type: page
space: TC
title: 'Proposal: Evaluating Alternatives to Kubeapps for Kubernetes Application Management'
author: Jamie de Leest
date: '2025-12-24'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1062567937
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1062567937
---
# Proposal: Evaluating Alternatives to Kubeapps for Kubernetes Application Management

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1062567937  

## Content

## **1. Background & Context**

We currently use **Kubeapps** as a UI for managing Kubernetes applications deployed via Helm.  
The **primary reason** for adopting Kubeapps was **not just Helm support**, but the ability to:

> **Clearly see which application version is deployed, whether updates are available, and safely update applications while preserving existing Helm values, including seeing a diff of what would change before applying the update.**

This significantly reduced deployment risk and improved transparency during upgrades.

As we consider replacing Kubeapps, it is critical that this **core value is preserved or improved**.

---

## **2. Core Requirements (Based on Kubeapps Usage)**

Any alternative must meet the following **key requirements**:

### **Functional Requirements**

* Clear visibility of **currently deployed application and Helm chart versions**
* Visibility into **available updates**
* Ability to **upgrade Helm releases while preserving existing values**
* **Diff view** of configuration / values before applying updates
* Rollback support

### **Non-Functional Requirements**

* Intuitive and accessible UI
* Strong RBAC and team isolation
* Low operational overhead
* Suitable for production environments

---

## **3. Alternatives Evaluated**

### **3.1 Portainer (Primary Candidate)**

**Category:** Kubernetes & Container Management Platform  
**License:** Open Source core, Enterprise extensions available

#### **Why Portainer aligns with our Kubeapps use case**

Portainer directly supports **Helm-based application lifecycle management** and provides the **same core benefits that made Kubeapps valuable**:

✔ Clear overview of **deployed applications and versions**  
✔ Visibility into **available Helm chart updates**  
✔ **Safe Helm upgrades** that retain existing values  
✔ Ability to **review configuration changes before deployment**  
✔ Rollback support for Helm releases

This makes Portainer a **functional equivalent (or improvement)** over Kubeapps for our main use case.

#### **Additional Benefits**

* Multi-cluster management
* Fine-grained RBAC
* Broader cluster visibility (pods, services, volumes, etc.)
* Easy deployment and maintenance
* Mature ecosystem and strong adoption

#### **Considerations**

* Some advanced enterprise features require a license
* Less “Helm-centric” branding than Kubeapps, but comparable functionality

**Conclusion:**  
➡ **Portainer preserves the most critical Kubeapps functionality: version insight, safe upgrades, and change transparency.**

**Resources:**

<https://www.portainer.io/resources/get-started/install><https://docs.portainer.io/user/kubernetes/applications/inspect-helm><https://docs.portainer.io/start/install-ce/server/kubernetes/baremetal>

---

### **3.2 Devtron**

**Category:** Kubernetes Application Delivery Platform  
**License:** Licensed (free tier + paid enterprise features)

#### **Strengths**

* Helm-based deployments
* Version tracking and rollbacks
* Diff visibility for configuration changes
* Strong RBAC and auditability
* Integrated CI/CD pipelines

#### **Limitations**

* Larger and more complex platform than required for our primary use case
* Higher operational overhead
* Licensing cost for enterprise features

**Conclusion:**  
➡ Devtron is a powerful platform but may be **overkill** if our main focus is application versioning and safe Helm upgrades.

**Resources:**

<https://devtron.ai/open-source>

---

### **3.3 Cozystrack**

**Category:** Kubernetes application tracking

#### **Strengths**

* Lightweight approach
* Focus on application visibility

#### **Limitations**

* Limited evidence of Helm value diff support
* Smaller community and ecosystem
* Less production maturity

**Conclusion:**  
➡ Currently **does not fully cover** the key reasons we adopted Kubeapps.

**Resources:**

<https://github.com/cozystack/cozystack>

---

## **4. Supporting (Non-UI) Tools**

While not replacements for Kubeapps, the following tools can **complement** our application management strategy:

* **Pluto** – Detects deprecated Kubernetes APIs before upgrades
* **Silver Surfer** – Assists with safe Kubernetes cluster upgrades

These tools improve upgrade safety but **do not replace** the need for a UI that manages Helm releases and value diffs.

Resources:

<https://github.com/FairwindsOps/pluto><https://github.com/devtron-labs/silver-surfer>

---

## **5. Recommendation**

### **Primary Recommendation: Portainer**

Portainer best satisfies the **original motivation for using Kubeapps**:

* Clear insight into application versions
* Visibility into available updates
* Safe Helm upgrades with existing values preserved
* Ability to review changes before applying them

Additionally, it provides broader Kubernetes management capabilities with minimal added complexity.

### **Secondary Option: Devtron**

Devtron is a strong alternative **if** we want to expand toward a more opinionated DevOps and CI/CD platform, but it exceeds current requirements.

---

## **6. Proposed Next Steps**

1. Deploy **Portainer** in a staging environment
2. Perform a Helm upgrade scenario:

   * Preserve existing values
   * Review configuration diff
3. Compare workflow against current Kubeapps experience
4. Collect feedback from users
5. Make final decision
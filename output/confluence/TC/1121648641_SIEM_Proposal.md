---
id: confluence:1121648641
source: confluence
type: page
space: TC
title: SIEM Proposal
author: Jamie de Leest
date: '2026-02-12'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1121648641
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1121648641
---
# SIEM Proposal

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1121648641  

## Content

## Wazuh and OpenSearch as a SIEM Solution

### What is Wazuh

Wazuh is an open-source security platform focused on threat detection, security monitoring, and incident response. It operates primarily as a host-based intrusion detection system (HIDS) and security analytics engine. Wazuh agents are installed on endpoints such as servers, virtual machines, or containers, where they collect security-relevant data including logs, file integrity changes, configuration assessments, vulnerability information, and system activity.

This data is then forwarded to a central Wazuh manager, where it is analyzed using rules, decoders, and correlation logic to identify potential security threats. Wazuh supports compliance monitoring (e.g. PCI DSS, GDPR, CIS benchmarks), vulnerability detection, malware detection, and active response actions, making it a broad and versatile security monitoring tool.

### What is OpenSearch

OpenSearch is an open-source search and analytics engine designed for storing, indexing, and querying large volumes of data in near real time. It is commonly used for log analytics, metrics, and observability use cases. OpenSearch includes OpenSearch Dashboards, a visualization layer that enables users to explore data through dashboards, charts, and alerts.

In a SIEM context, OpenSearch acts as the data storage and analytics backend. It allows security teams to efficiently search through large amounts of security logs, correlate events over time, and visualize trends or anomalies across systems.

### Why Wazuh and OpenSearch Are a Good SIEM Combination

Together, Wazuh and OpenSearch form a powerful and cost-effective SIEM solution. Wazuh provides the security intelligence layer by collecting, normalizing, and analyzing security events, while OpenSearch provides scalable storage, fast search capabilities, and rich visualizations.

Key advantages of this combination include:

* **Open-source and cost-effective**  
  Both Wazuh and OpenSearch are open-source, making them attractive alternatives to commercial SIEM solutions that often come with high licensing and ingestion costs.
* **Scalability and performance**  
  OpenSearch is designed to handle large volumes of log data, making it suitable for environments ranging from small infrastructures to large, distributed systems.
* **Real-time threat detection**  
  Wazuh continuously analyzes incoming data and can detect security incidents in near real time, enabling faster response to threats.
* **Extensive visibility**  
  By combining endpoint data from Wazuh agents with centralized log analysis in OpenSearch, organizations gain deep visibility into system behavior, user activity, and potential attack vectors.
* **Custom dashboards and alerts**  
  OpenSearch Dashboards allows security teams to build tailored dashboards and alerts that match their specific monitoring and incident response needs.
* **Flexibility and integration**  
  The solution integrates well with cloud, on-premise, and containerized environments, and can be extended with additional data sources or custom detection rules.

### Conclusion

Wazuh and OpenSearch together provide a robust, flexible, and transparent SIEM solution. They offer many of the core capabilities expected from modern SIEM platforms—such as log aggregation, threat detection, correlation, and visualization—while remaining accessible and customizable due to their open-source nature. This makes them a strong choice for organizations seeking effective security monitoring without the complexity or cost of proprietary SIEM products.

---

## Evaluation of Alternative SIEM Solutions

Several SIEM platforms were evaluated before selecting Wazuh and OpenSearch. The comparison focused on cost, deployment complexity, scalability, cloud compatibility, and suitability for the project’s requirements.

### Splunk

Splunk is a widely adopted commercial SIEM known for its powerful search and analytics capabilities.

**Limitations:**

* High licensing and data ingestion costs.
* Proprietary ecosystem with vendor lock-in.
* Less suitable for cost-sensitive or educational environments.

**Why Wazuh + OpenSearch was preferred:**  
The open-source nature of Wazuh and OpenSearch provides similar log analysis and visualization capabilities without licensing costs, while allowing full control over data and configuration.

---

### Elastic SIEM (Elastic Stack / Elastic Security)

Elastic SIEM offers strong log analytics, dashboards, and detection rules based on the Elastic Stack.

**Limitations:**

* Advanced SIEM features require commercial licenses.
* Licensing model has become more restrictive over time.
* Less transparent separation between open-source and paid features.

**Why Wazuh + OpenSearch was preferred:**  
OpenSearch remains fully open-source, and Wazuh provides built-in security detections without feature gating, ensuring long-term flexibility and predictability.

---

### Graylog

Graylog is an open-source log management platform with alerting and dashboard capabilities.

**Limitations:**

* Primarily focused on log aggregation rather than security detection.
* Lacks native host-based intrusion detection and compliance monitoring.
* Requires additional tools to function as a full SIEM.

**Why Wazuh + OpenSearch was preferred:**  
Wazuh provides native security analytics and endpoint visibility, making the combined solution closer to a complete SIEM rather than a log management system.

---

### QRadar

IBM QRadar is a mature enterprise SIEM with strong correlation and compliance features.

**Limitations:**

* Expensive licensing and infrastructure requirements.
* Complex deployment and maintenance.
* Less flexibility for custom or experimental setups.

**Why Wazuh + OpenSearch was preferred:**  
The project favors a lightweight, flexible solution that can be adapted and extended without enterprise-level costs or operational overhead.

---

### Microsoft Sentinel

Microsoft Sentinel is a cloud-native SIEM tightly integrated with Azure.

**Limitations:**

* Strong dependency on the Azure ecosystem.
* Ongoing ingestion and query costs.
* Less suitable for multi-cloud or on-premise environments.

**Why Wazuh + OpenSearch was preferred:**  
Wazuh and OpenSearch are platform-agnostic and can be deployed on-premise, in the cloud, or in hybrid environments without vendor lock-in.

---

### Security Onion

Security Onion excels at network security monitoring and deep packet inspection.

**Limitations:**

* Requires access to raw network traffic.
* Resource-intensive due to packet capture and analysis.
* Less practical in cloud or container-based environments.

**Why Wazuh + OpenSearch was preferred:**  
The project prioritizes endpoint visibility and log-based detection over network traffic analysis, making Wazuh a better functional match.

---

### On AWS-Native Option

An AWS-native approach using GuardDuty, Security Hub, CloudTrail, and CloudWatch Logs is viable and offers deep integration with AWS networking components (VPC, Subnets, IAM, WAF, etc.). However, it does not provide host-based intrusion detection, file integrity monitoring, or customizable cross-system correlation between application logs, identity providers, and VPN authentication events.

For infrastructure-only visibility, AWS-native tooling is strong. For application-layer and endpoint-level detection, Wazuh offers broader coverage.

---

### On Reusing Grafana and Prometheus

Prometheus is a metrics collection system and is not suitable for log-based security event ingestion or SIEM functionality. It does not support full-text search, event correlation, or log normalization.

However, Grafana can be reused as the visualization and alerting layer by connecting it to OpenSearch as a datasource. This allows us to:

* Keep existing tooling
* Centralize monitoring
* Avoid introducing a second dashboard system
* Still maintain full SIEM capability via Wazuh

Wazuh requires an indexing backend:

* OpenSearch or Elasticsearch

You cannot:

* Store SIEM-scale logs in Prometheus
* Use Grafana alone without a log backend

OpenSearch Dashboards:

* Built-in Wazuh app plugin
* Prebuilt security dashboards
* Tight integration with Wazuh alerts

Grafana:

* More generic
* You must build dashboards yourself
* Slightly more work upfront

Although Grafana supports OpenSearch as a data source, I would still recommend using OpenSearch Dashboards for visualization. Since OpenSearch is already required as the indexing and storage backend, using its native visualization layer ensures tighter integration and leverages tooling specifically designed for log analytics and security event exploration.

---

## Summary of Key Selection Criteria

Wazuh and OpenSearch were selected based on the following criteria:

* Fully open-source with no licensing costs
* Strong host-based intrusion detection and log analysis
* Cloud, container, and hybrid environment compatibility
* Modular and scalable architecture
* Lower operational complexity and resource requirements
* High transparency and customization of detection logic

## Final Justification

Compared to commercial and alternative open-source SIEM solutions, Wazuh combined with OpenSearch provides the best balance between functionality, flexibility, cost efficiency, and maintainability. It delivers essential SIEM capabilities while remaining accessible, extensible, and well-suited to modern infrastructure environments.

---

## 1. Environment Assumptions

**Kubernetes (Primary)**

* Keycloak (in-cluster)
* Internal APIs
* External APIs
* Application configuration services (e.g. Portreporter)

**Outside Kubernetes**

* Auth0 (SaaS)
* OpenVPN (EC2)

---

## 2. Final Architecture (Phase 1)

wide760KUBERNETES CLUSTER
────────────────────────────────
[ Keycloak Pod Logs ] ─┐
[ API Pods Logs ] ├──> Fluent Bit DaemonSet
[ App Config Logs ] ─┘
↓
[ Wazuh Manager ]
↓
[ OpenSearch ]
↓
[ Dashboards + Alerts ]
OUTSIDE CLUSTER
────────────────────────────────
[ Auth0 Logs ] ───────> HTTPS → Wazuh
[ OpenVPN (EC2) ] ────> Wazuh Agent or Syslog

**Design principle**

* Fluent Bit is used **only for Kubernetes-native log collection**
* Wazuh performs **parsing, normalization, correlation, and alerting**
* OpenSearch provides **search, dashboards, and visualization**

---

## 3. Logging Strategy (JSON-First, Parser-Fallback)

### Priority Order

1. **Native JSON logging** (preferred)
2. **Structured key-value logs** (acceptable fallback)
3. **Plain text logs** (supported via custom parsers/decoders)

This approach minimizes operational risk while enabling gradual improvement.

---

## 4. Kubernetes Log Collection (Fluent Bit)

### Deployment Model

* **Fluent Bit as a DaemonSet**
* Reads:

  + `/var/log/containers/*.log`
  + Structured JSON logs from apps
* Enriches logs with:

  + Namespace
  + Pod
  + Container
  + Labels (env, app, team)

---

### Fluent Bit Inputs (K8s)

iniwide760[INPUT]
Name tail
Path /var/log/containers/\*.log
Parser cri
Tag kube.\*

---

## 5. Keycloak (K8s)

### Log Types Collected

* Login success/failure
* MFA failures
* Role & permission changes
* Admin actions

### Keycloak Configuration

* Enable **Event Listener → JSON logging**
* Write to stdout → picked up by Fluent Bit
* Optional:

  + Separate audit log stream

### Detection Coverage

* Repeated login failures
* Unexpected login locations
* Authorization changes

---

## 6. Parsing & Normalization Strategy (Wazuh)

| Source | Format | Parsing Method |
| --- | --- | --- |
| Keycloak | JSON | Native JSON decoder |
| APIs | Key-value / text | Custom decoders |
| Auth0 | JSON | Native JSON decoder |
| OpenVPN | Text | Built-in decoders |

Normalization maps all events to common fields:

* user
* source.ip
* service
* event.type
* outcome

---

## 7. Internal & External APIs (K8s)

### What We Detect

* High 401/403 per user/token/IP
* High 404/500 per endpoint
* High traffic from single IP
* Endpoint enumeration patterns

Fluent Bit automatically tags logs with:

* Namespace (prod/staging)
* Service name
* Version label (useful for detecting bad deploys)

---

## 8. Auth0 (SaaS)

### Ingestion Method

* **Auth0 Log Streaming**
* Stream to:

  + HTTPS endpoint exposed by Wazuh
  + OR AWS EventBridge → Lambda → Wazuh

### Events Used

* Failed logins
* MFA failures
* Suspicious IPs
* Admin changes

Auth0 acts as an **external identity signal**, correlated with Keycloak events.

---

## 9. OpenVPN (EC2)

### Option A (Preferred)

* Install **Wazuh Agent** on EC2
* Native VPN auth rules
* Lower effort

### Option B

* Syslog → Wazuh
* Fluent Bit *not needed* here

### Events

* Failed VPN auth
* New device/IP connections
* Long-lived sessions

---

## 10. Alert Definitions (MVP)

### P1 – Critical (Immediate)

* MFA failures
* Login from new country/ASN
* Role/permission changes
* VPN login from new geo/IP

---

### P2 – Suspicious

* High 401/403 rate (API abuse)
* High 404/500 rate (probing / bad deploy)
* High traffic from single IP

---

### P3 – Audit

* Application config changes
* Billing/authorization changes (Portreporter)

---

## 11. Dashboards (OpenSearch)

### Dashboard 1 – Identity Security

* Keycloak + Auth0 failures
* MFA failures
* Geo map

### Dashboard 2 – API Abuse & Health

* Status code breakdown
* Error spikes per service
* Top IPs

### Dashboard 3 – Audit & Change Tracking

* Role changes
* Config changes
* Admin actions

---

## 12. Phase 2 – Expand to “Everything”

Because this is K8s-native:

* Add new namespaces → auto-covered
* Add infra logs (CloudTrail, EKS control plane)
* Add CI/CD logs
* Add runtime security (Falco → Fluent Bit)

No architecture change needed.
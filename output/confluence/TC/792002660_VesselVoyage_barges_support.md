---
id: confluence:792002660
source: confluence
type: page
space: TC
title: VesselVoyage barges support
author: Darius Wattimena
date: '2025-07-07'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/792002660
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/792002660
---
# VesselVoyage barges support

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/792002660  

## Content

Envision date:

Participants:



---

## Goal

Currently, VesselVoyage only supports data from sea-going vessels. As a result, when running a PTO port that primarily handles barges, the report may display berths as completely empty-leading to misleading or incomplete insights into port activity.

By adding support for barges, VesselVoyage can evolve into a more comprehensive solution-capturing not just sea-vessel movements but any cargo transfer occurring via ship. This enhancement would make it a foundational tool for any kind of vessel that does cargo operations.

## Challenges

**Identifier Limitations**: VesselVoyage currently relies exclusively on IMO numbers, which are only assigned to sea-going vessels. Barges typically only have MMSI numbers and exhibit significantly different behavioural patterns, such as frequent long port stays and operations within inland waterways.

**Data Model Constraints**: The current design of the **Visit–Voyage** structure assumes visits and voyages can be stored within a single MongoDB document. This model doesn't scale well for vessels such as barges. Those type of ships can remain in port for extended periods, causing data size and performance issues.

---

## **Envisioned Tasks**

### **Add Support for CSI Identifiers**

* Investigate the mutability of CSI identifiers and implement safeguards to prevent changes.
* Enable tracking of vessels that lack IMO numbers, particularly barges.

### **Extend CSI to Support Barges**

* Collaborate with the ContextMapping team to ensure CSI receives data for barges operating in targeted ports.

### **Define Supported Barge Categories**

* Identify and prioritise initial barge types to support (e.g., tank barges, push barges).
* Exclude unsupported categories to optimize data ingestion and reduce noise.

### **Add Support for Revents**

* Extend system logic to recognise and handle revent events specific to barge operations.

### **Maintain Consistent Logic for Barges and Sea Vessels**

* Reuse and adapt existing business and processing logic from sea vessels.
* Ensure consistency with core system design while addressing barge-specific behaviour.

### **Check System Performance with Barge Inclusion**

* Validate system performance after integrating barge data.
* Monitor for degradation and make necessary performance optimisations.
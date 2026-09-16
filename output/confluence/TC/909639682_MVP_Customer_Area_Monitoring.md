---
id: confluence:909639682
source: confluence
type: page
space: TC
title: MVP Customer Area Monitoring
author: Darius Wattimena
date: '2025-10-10'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/909639682
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/909639682
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/whiteboard/910065667
---
# MVP Customer Area Monitoring

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/909639682  

## Content

# **Customer Request**

UAB Online has requested an **area monitoring feature** around the terminal — similar to the terminal mooring area, but on a more flexible scale. The customer must be able to **create and manage their own areas** and **register ships** for those areas.

Our system will then generate and **push AreaEvents** (via a message broker, e.g., RabbitMQ) related to the customer-defined areas and ships.

## Goals

* Allow customers to define and manage their own monitoring areas.
* Enable registration of ships per customer area.
* Generate and publish area-related events for customer-monitored ships.
* Deliver these events to customers through a new publishing service.

## High-Level System Design

| Component | Description | Change Summary |
| --- | --- | --- |
| **Poma** | Base system that stores area configurations | Extend with **Customer Areas** (area + customer ID) |
| **AreaMonitor** | Handles area logic and events | Extend to support **Customer Areas** and update **AreaType** enum with new value: `CUSTOMER` |
| **EventHistory** | Stores event data | Save **Customer Area Events**, but **do not expose** them via existing API endpoints |
| **Other AreaEvent consumers** | Left over AisEngine components that consume area events | Update to recognize the new **CUSTOMER** AreaType |
| **CustomerEventPublisher** *(new)* | Publishes Customer Area Events | New component to publish customer events via RabbitMQ. Maintains customer–ship–area interest mappings. |
| **External API** | Exposes public endpoints | Add routing to **CustomerEventPublisher** for event subscription and configuration |

## Component Details

### **1. Poma**

* Extend to support *Customer Areas* (area + `customer_id`)
* Maintain consistency with standard area structures
* Estimate: **3 days**

### **2. AreaMonitor**

* Extend AreaEvent model to include a new `CUSTOMER` area type
* Update logic to handle `CUSTOMER` area type
* Update integration with Poma to retrieve customer areas
* Estimate: **1 day**

### **3. EventHistory**

* Store Customer Area Events internally
* Ensure these events are **always** **excluded from API queries**
* Estimate: **3 days**

### **4. Other AreaEvent consumers**

* Update all event consumers to include the `CUSTOMER` AreaType logic
* Ensure compatibility with AreaMonitor changes
* The following components need to be adjusted:

  + BerthMonitor
  + AnchorMonitor
  + PortReporterMonitor
  + ShipHistory
  + EventConverter
  + VesselVoyage
* Estimate: **2 days**

### **5. CustomerEventPublisher (NEW)**

* Core logic for **publishing Customer Area Events**
* Manages customer area/ship interest mappings

  + When creating an area, registers area in Poma
* Manages event publishing to customer
* Estimate: **10 days**

### **6. External API**

* Add new routing layer for:

  + Customer area/ship registration
  + Event subscription management
* Forwards requests to **CustomerEventPublisher**
* Estimate: **1 day**

## Diagram with system overview

<https://teqplaybv.atlassian.net/wiki/spaces/TC/whiteboard/910065667>

## Estimated Time Summary

| Component | Estimated Time |
| --- | --- |
| Poma | 3 days |
| AreaMonitor | 1 day |
| EventHistory | 3 days |
| Other AreaEvent consumers | 2 days |
| CustomerEventPublisher | 10 days |
| External API | 1 day |
| **Total** | **20 days** |
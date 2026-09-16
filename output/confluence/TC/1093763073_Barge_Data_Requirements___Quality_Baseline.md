---
id: confluence:1093763073
source: confluence
type: page
space: TC
title: Barge Data Requirements & Quality Baseline
author: Darius Wattimena
date: '2026-01-27'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1093763073
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1093763073
---
# Barge Data Requirements & Quality Baseline

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1093763073  

## Content

## Purpose

To align stakeholders on which barge data is required, how it will be used, and what level of quality is needed to support commercial and operational insights from 2025 onwards.

## Stakeholders

* Sales
* PTO team
* Projects team

## Key Questions to Resolve

* Which barge data points are required to support Sales use cases?
* Which data points are **critical** versus **optional**?
* What level of data accuracy and completeness is “good enough” for these use cases?

## Relevant Barge Behaviour Examples

* **Barge doing operations in multiple ports**  
  Illustrates port-to-port movement.  
  Example link (dev):  
  <https://vesselvoyagedev.teqplay.nl/#/ships/8a683edf-7cda-4187-9073-ae4d3359831c/story/6ed86708-a0e8-4d85-b597-07b800a90b57.VISIT?mode=period&months=3>
* **Barges remaining in a single port for long periods**  
  Highlights waiting, idle time, and prolonged visits.  
  Example link (dev):  
  <https://vesselvoyagedev.teqplay.nl/#/ships/466e30bf-edfb-46ef-914a-0fb77fc97a9d/story/75a674d9-107f-4847-be41-a30773e60a53.VISIT?mode=period&months=3>

## Priority Use Cases & Data Needs

**High Priority (Sales-Relevant):**

* **Waiting time at berth (terminal level)**  
  Key input for commercial discussions with terminals.
* **Movement within the terminal**  
  Ability to track berth-to-berth movements (e.g. berth 1 → berth 2).
* **Berth occupancy**

  Primarily relevant for PTO. (Not in scope of core team, but for PTO team).

**Lower Priority / Contextual:**

* **Other waiting (non-berth related)**  
  Less relevant from a terminal perspective.

**Time Scope:**

* Focus on **2025 and onwards**.

## Barge Ship Data

All barges are available for ARA region, no further action required.

Needed data:

* Ship name
* Ship category (if available)
* MMSI
* Vessel length

## Data Quality

Based on the metrics, the current data quality is considered **sufficient (“fit for purpose”)** to support the use cases from 2025 onwards.

The following known data issues are still to be picked up by the Core team to improve the completeness in barge data:

* Vessels that never entered the EOSP, resulting in missing Visit records.
* Visits that are currently capped at 50 because the ships stay for a long duration in the same port.
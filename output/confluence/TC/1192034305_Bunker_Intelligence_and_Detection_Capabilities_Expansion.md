---
id: confluence:1192034305
source: confluence
type: page
space: TC
title: Bunker Intelligence and Detection Capabilities Expansion
author: Darius Wattimena
date: '2026-05-19'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1192034305
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1192034305
---
# Bunker Intelligence and Detection Capabilities Expansion

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1192034305  

## Content

## Purpose

This document captures and structures ideas from a brainstorm session around expanding bunker-related detection capabilities. The goal is to evolve these ideas into a more detailed feature set that can later be prioritised and translated into a product roadmap over the coming quarters.

## Scope Overview

We divide the opportunity space into four main domains:

1. **Bunker Event Detection**
2. **Bunker / Loading Details**
3. **Operational Functionalities**
4. **Bunker Intelligence**

---

# 1. Bunker Event Detection

## 1.1 Stable Bunker Event Detection

**Description**  
Detect bunker events in a *robust and stable way*, minimizing interruptions caused by AIS jitter.

**Requirement**

* Events should not “break” due to AIS jittering

**Value**

* Reliable foundation for all downstream features
* Prevents false positives / fragmented events

---

## 1.2 Hose Connection / Disconnection Estimation

**Description**  
Estimate the moment when bunker hoses are:

* Connected (start of actual fuel transfer)
* Disconnected (end of transfer, before departure)

**Approach**

* Use time offset from detected bunker encounter

  + *X minutes after start → connection*
  + *Y minutes before end → disconnection*
* Determine values based on historical information

**Important**

* This is an **estimate**, not a ground truth

**Value**

* Enables:

  + SOF pre-fill
  + More precise bunkering timelines
  + Operational insights

**Open Questions**

* Is this offset dynamic per vessel type?
* Does the size of the vessel bring in a factor how fast the hoses are connected/disconnected?

---

## 1.3 Discharge / Loading Event Detection

**Description**  
Detect fuel transfer events beyond bunkering:

* At **terminals**
* At **floaters** (stationary offshore storage, similar to Ship-to-ship, but non-moving)

**Approach**

* ?

**Value**

* Expands coverage beyond bunkering
* Enables broader fuel movement tracking

---

# 2. Bunker / Loading Details

## 2.1 Fuel Type Identification

**Description**  
Determine which fuel type is likely being bunkered.

**Approach**

* Extend CSI (internal ship database) with:

  + Supported fuel types per vessel
  + Ship can use multiple type of fuels
* Combine with:

  + Bunker vessel type

**Value**

* Enables insight in which flues were potentially used during a bunkering operation between 2 vessels

**Limitations**

* Not always certain which fuel was bunkered when multiple are possible

---

## 2.2 Fuel Volume Estimation

**Description**  
Estimate the amount of fuel transferred during a bunkering event.

**Approach (future-oriented)**

* Based on:

  + Vessel size/type
  + Duration of operation
  + Historical patterns

**Value**

* Key for:

  + Market demand estimation
  + Competitive intelligence

**Open Questions**

* Should this be fully based on the bunker vessel behaviour or does the receiving vessel also have any impact as well?

---

# 3. Operational Functionalities

## 3.1 SOF (Statement of Facts) Pre-Fill

**Description**  
Provide timestamps that customers can use to pre-fill SOF documents.

**Data Points**

* Arrival
* Start of bunkering (estimated hose connection)
* End of bunkering (estimated disconnection)
* Departure

**Value**

* Reduces manual work
* Improves operational efficiency for customers

---

## 3.2 ETA Predictions (Bunker & Receiving Vessels)

**Description**  
Predict arrival times at the decided destination for:

* Bunker vessels
* Receiving vessels

**Value**

* Planning & coordination
* Operational visibility

---

## 3.3 Bunker Notifications

**Description**  
Provide notifications related to bunker events.

**Example Use Case**

* A bunker trader hires a delivery party and wants status updates

**Type of Notifications**

* Start/end of bunkering
* Delays or anomalies
* Vessel arrival

---

## 3.4 Retrieval of Last Bunkering Event

**Description**  
Quickly retrieve the most recent bunkering event of a vessel.

**Value**

* Enables identification of:

  + “Thirsty vessels” (vessels likely needing fuel soon)

**Future Opportunity**

* Build targeting tools for bunker providers:

  + Identify vessels likely needing bunkering
  + Track incoming demand in a region

---

# 4. Bunker Intelligence

## 4.1 Bunker Provider Performance

**Description**  
Analyse performance of bunker providers.

**Value**

* Benchmarking
* Transparency in the market

---

## 4.2 Competitor Analysis

**Description**  
Compare bunker providers within a port or region.

**Insights**

* Activity levels
* Coverage
* Trends over time

---

## 4.3 “Who Won the Auction?”

**Description**  
Infer which bunker provider serviced a vessel when a provider lost a bid.

**Approach**

* Detect which bunker vessel interacted with target vessel

**Value**

* Market transparency
* Competitive awareness

---

## 4.4 Demand & Supply Estimation

**Description**  
Estimate bunker demand and supply dynamics.

**Inputs**

* Number of bunkering events
* Vessel traffic
* Estimated fuel volumes

**Value**

* Strategic insights
* Market trend analysis

---

## 4.5 Fleet Grouping & Market Share

**Description**  
Group bunker providers by fleet and estimate market share.

**Approach**

* Cluster vessels by operator/provider
* Aggregate activity

**Value**

* High-level market overview
* Competitive positioning

---

## Priority for Q2 2026

With the main focus to support Ofiniti the following priority has been set out:

1. Stable bunker encounters (Encounter monitor + VesselVoyage improvements).
2. Quick insight when each ship last had a bunker operation (thirsty vessels).
3. Terminal floater support.
4. Bunker-to-bunker encounters.
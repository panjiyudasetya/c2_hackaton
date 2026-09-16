---
id: confluence:865042434
source: confluence
type: page
space: TC
title: Timestamp Quality Validation Process
author: Darius Wattimena
date: '2025-09-16'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/865042434
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/865042434
---
# Timestamp Quality Validation Process

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/865042434  

## Content

## Overview

The **Timestamp Quality Validation Process** ensures accuracy and reliability of VesselVoyage timestamps across multiple ship categories and ports. The process provides regular reporting, monitoring, and issue resolution to support the Core Components team to improve the timestamp quality.

---

## Report Generation

* Generate a **VesselVoyage timestamp quality report** from current input data.
* For each category, mark timestamps as:

  + **1** = accurate
  + **0** = inaccurate
* Expected timestamps are defined per vessel visit.
* Output formats:

  + **Excel report** (preferred for wider usage)
  + **JSON response** (alternative, for automation)

### Endpoint

* Provide an endpoint to return the **total accuracy score** of all visits checked.
* This score feeds directly into the Obeya “timestamp quality” metric.
* Metrics to expose:

  + **Last month quality**
  + **All-time quality**

---

## Validation Process

### Frequency

* **Every 2 weeks**, aligned with the Obeya performance meeting.

### Sampling Method

* Select **10 ships in total** per cycle:

  + **2 ships** from each of **5 different mapped ports.** Currently we will focus on getting a good coverage for the most important ports for us: NLRTM, SGSIN, USHOU, USCRP and BEANR. In the future more ports from the mapped port list will be added. A complete list of mapped ports can be found here

### Ship Categories

* **BULK CARRIER**→ NLRTM, SGSIN, USHOU, USCRP, BEANR
* **GENERAL CARGO** → NLRTM, SGSIN, USHOU, USCRP, BEANR
* **CONTAINER** → NLRTM, SGSIN, USHOU, BEANR
* **TANKER** → NLRTM, SGSIN, USHOU, USCRP, BEANR
* **OTHER** → These categories are not that important for the bussiness, but if needed we can select some different types and add them to the list.

> Note: Ship categories rotate each cycle to ensure diverse coverage and a large dataset over time.

---

## Inaccuracy Review & Resolution

For each **inaccurate visit**:

1. **Validation check**

   * Confirm manually by looking the actual and expected timestamps in Vessel Voyage and compare them with timeline.
2. **Resolution path**

   * **Data issue** → Create a bug card for backlog and refine in the refinement meeting.
   * **Context mapping issue** → Raise to the ContextMapping team.
   * **False positive** → Adjust expected timestamps.

### Potential Adjustment

* Once dataset stabilises and accuracy improves, reduce the sample to **5 ships per cycle**.
* Decision to adjust will depend on observed stability of results.

---

## Next Steps

* Expose timestamp quality results in the **VesselVoyage frontend** (pending David’s return).
* TBD…
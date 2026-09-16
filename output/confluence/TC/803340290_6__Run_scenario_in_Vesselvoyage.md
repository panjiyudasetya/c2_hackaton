---
id: confluence:803340290
source: confluence
type: page
space: TC
title: 6. Run scenario in Vesselvoyage
author: Panji Y. Wiwaha
date: '2026-08-26'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/803340290
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/803340290
---
# 6. Run scenario in Vesselvoyage

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/803340290  

## Content

### **Recalculating Historic Data in Vesselvoyage**

When a **port** or **CSI** change affects our monitoring / context-mapping setup, we must **recompute historic data in VesselVoyage before back-filling the Data Mart**.

Follow the steps below to run a safe and efficient recalculation.

---

#### **1 · Choose the Correct Environment**

| **Environment** | **Purpose** | **Notes** |
| --- | --- | --- |
| **vesselvoyage-dev** | Development sandbox to test newly developed code or unusual scenarios. | Safe for experimentation. |
| **vesselvoyage-data** | Staging / integration environment, used for end-to-end tests and context-mapping validation. | Mirrors production closely. |
| **vesselvoyage-prod** | **Live production**. Updates are visible to customers. | Use only after validating in *data* or *dev*. |

---

#### **2 · Create a Recalculation Scenario**

1. Open **VesselVoyage → Scenarios**.
2. Click **Add new**.

You now decide **how** to recalculate:

| **Option** | **When to Use** |
| --- | --- |
| **By Port Area** | Multiple vessels affected by a *POMA* or port-related change. |
| **By Ship** | A single vessel affected by one CSI or minor change. |

---

##### **A. Recalculate by Port Area**

1. **Select Port UN/LOCODE**.
2. **Define the date range** (*Start* → *End*).

   * For low-coverage ports, enable **Include historic data**.
3. Click **Create** and wait — large ranges can take **several hours**.

##### **B. Recalculate by Ship**

1. **Search for the vessel** (IMO or name).
2. **Select the voyage start date** (system auto-expands for optimal merging).
3. Click **Create** and wait — processing may take **several hours**.

> **Tip:** Keep the range as tight as possible. VesselVoyage already expands dates internally; longer periods = longer wait times.

---

#### **3 · Monitor the Scenario**

* **Status: Processing…** – normal.
* **Status stuck in Processing** – the task likely crashed.

  *➡ Notify the **Core Components** team to investigate.*

---

#### **Key Takeaways**

* **Always recalculate in dev or data first**; promote to *prod* only after validation.
* **Choose the smallest practical scope** (port or vessel & period).
* **Expect hours of processing time** and monitor statuses.
* **Escalate stalled scenarios** to Core Components promptly.
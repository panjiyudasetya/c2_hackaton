---
id: confluence:929202177
source: confluence
type: page
space: TC
title: Speed Selection Logic - Platform
author: Rowdey Goos
date: '2025-10-21'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/929202177
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/929202177
---
# Speed Selection Logic - Platform

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/929202177  

## Content

## **Overview**

Speed determination follows a strict priority order:

1. **Manual speed** — overrides all other sources.
2. **If starting at the ship’s current position (dynamic mode):**

   * Use **Prediction Speed Model** (if enabled).
   * Fallback: **Current SpeedOverGround (SOG)** from AIS.
3. **If not dynamic (no recent position data):**

   * Use **Static average speed** from the ship register (if available).
   * Fallback: **Default heuristic speed** from `PredictionUtils.getDefaultInKnots()`.

---

## **Minimum Speed Handling**

* **Sea ships:** must have speed ≥ **5.0 kn**
* **Other ships:** must have speed ≥ **4.0 kn**

If `fallbackWhenBelowMinimumSpeed = true`:

* Any speed source returning too-low values is **skipped**.
* The system tries the next available source before defaulting.

If the **final chosen speed** is still below the minimum:

* The voyage step is **marked as an error** (`TOO_LOW_SPEED`).
* **No route** is computed.

---

## **Prediction Speed Model**

### **Data Source and Cache**

**Inputs:**

* AIS SOG (knots) data points for a vessel, keyed by **MMSI**.

**Behavior (if enabled):**

* Maintains a **per-vessel cache** of `[time, speed]` points.

  + Sorted **old → recent**.
  + Continuously updated from the internal AIS event bus.
* On each request:

  + Ensures the cache has a **recent 30-minute slice**.
  + If a vessel is not cached, fetches the **last 30 minutes of AIS history**.
* **Cache cleanup (every 5 minutes):**

  + Removes vessels not requested for **30 minutes**.
  + Discards AIS points older than **30 minutes**.

**If disabled:**

* Fetches the **last 30 minutes of history on demand**.

**If subsystem disabled or vessel not found:**

* Returns `null`.

---

### **Averaging Window and Sampling**

* **Window:** Last **30 minutes** (up to *now*, or a provided timestamp for historical queries).
* **Sampling step:** Every **1 minute** within the window.

**For each sample:**

1. If an **exact AIS match** exists → use its speed.
2. Else, take the **average** of the nearest AIS points **before and after** the timestamp.
3. If no nearby points exist → sample returns `null` (ignored).

---

### **Acceleration Bias Logic**

* **Window split:**

  + **First 2/3** → older segment.
  + **Last 1/3** → recent segment.

**Calculations:**

* `totalAverage` = average over all valid samples in the full window.
* `secondAverage` = average over the last 1/3 of samples.

**Decision rule:**

* If `(secondAverage / totalAverage) > 1.3` → vessel accelerating → **return** `secondAverage`.
* Else → **return** `totalAverage`.

**Units:** knots.

---

### **Outputs**

Returns:

wide760PredictionSpeed(timestamp=now, speed=calculatedKnots)

or `null` if no usable data points exist
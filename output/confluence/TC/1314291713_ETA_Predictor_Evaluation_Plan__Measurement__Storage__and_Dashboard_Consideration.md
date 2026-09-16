---
id: confluence:1314291713
source: confluence
type: page
space: TC
title: 'ETA Predictor Evaluation Plan: Measurement, Storage, and Dashboard Considerations'
author: Darius Wattimena
date: '2026-08-25'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1314291713
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1314291713
---
# ETA Predictor Evaluation Plan: Measurement, Storage, and Dashboard Considerations

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1314291713  

## Content

## 1. What do we measure against?

The reference point ("ground truth") for comparing an ETA prediction:

| Situation | Reference ATA |
| --- | --- |
| Port has a pilot boarding place | **Pilot boarding place ATA** |
| Port has no pilot boarding place | **Port ATA** |

---

## 2. Lead times and buckets

We evaluate predictions at fixed lead times before arrival:

* 7 days
* 48 hours
* 24 hours
* 12 hours
* 8 hours
* 4 hours
* 2 hours
* 1 hour

Predictions are grouped into **buckets** based on their lead time: `0–1h`, `1–2h`, `2–4h`, … up to a final bucket of **7 days or more**.

### Continuous measurement

We want to measure the outgoing predictions **continuously**, not only at the bucket boundaries.

**Decision:** when looking back in time for a comparison, we use the **exact moment the prediction was made**, not the nominal bucket time. Snapping to bucket times would bias the results.

---

## 3. What do we store?

### 3.1 As discussed in the meeting (aggregated)

Store a delta record with:

* Unlocode
* Ship category
* Lead time bucket
* Prediction creation day
* Delta sum
* Counter: total number of predictions
* Sea vessel or barge indication
* Source (ETA Predictor / AIS ETA / Agent ETA / etc.)

This aggregate is enough to build a **histogram** of prediction error.

### 3.2 Follow-up: store per prediction instead of aggregating

After the meeting we reconsidered aggregating errors across ships. The conclusion: **don't aggregate — store one record per prediction.**

Reasoning:

* With the setup described above, keeping every record amounts to only **a few GB per year**, which is entirely manageable.
* Keeping individual records lets us also record the **MMSI** of the vessel. Not as a tag/dimension for the metric, but as a field we can filter and search on — which should be very useful as a debugging aid.
* Any aggregate (delta sum, counters, histograms) can still be derived from the raw records; the reverse is not true.

> **To confirm:** whether we replace 3.1 with 3.2 entirely, or keep a rolled-up table alongside the raw records for fast dashboard queries.

---

## 4. Where to store the data

**Prometheus is not suitable** — it does not handle high-cardinality time series data.

Decided to use InfluxDB 3, to be synced with DevOps team to see what is possible and how we want to have this set up.

---

## 5. Obeya metric

Show the **average over a couple of lead times** rather than every lead time separately.

What we currently use for the Obeya Metric

Doing something similar would be ideal here, having 2 bars each measure time:

* Within 12 hours of arrival
* More than 12 hours before arrival
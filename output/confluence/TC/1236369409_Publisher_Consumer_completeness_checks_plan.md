---
id: confluence:1236369409
source: confluence
type: page
space: TC
title: Publisher/Consumer completeness checks plan
author: Panji Y. Wiwaha
date: '2026-06-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1236369409
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1236369409
---
# Publisher/Consumer completeness checks plan

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1236369409  

## Content

# Cross-Collaboration Team Discussion Report

**Topic:** Data Streaming Completeness  
**Status:** In Progress  
**Participants:** Core Component Team · Data Platform Team  
**Date:** 2026-06-04

---

## **Identified Issues**

### **1. Completed Messages Not Always Received by Consumer**

Completed messages published to the queue are not consistently received on the consumer side, resulting in data gaps that are currently difficult to quantify or trace.

### **2. Messages Stall in Queue Due to High Volume from Re-Events**

Completed messages are being published successfully, but remain backlogged in the queue. The assumption is that the consumer cannot keep up with the consumption rate when a large number of messages are triggered by re-events, leading to continuous growth in the queue depth.

| **Date** | **Topic** | **Owner** |
| --- | --- | --- |
| 2026-05-02 | [Data stream consumption - completeness test report (1st check)](https://docs.google.com/spreadsheets/d/1Nv1G2RLtPxGHMbJSDdsDeBE-u6Gi8Zh4cTgODguCpKM/edit?gid=1940093519#gid=1940093519) | Consumer/ Data Platform |
| 2026-05-12 | [Publisher patch for publishing completed messages is now in production](https://teqplaydev.slack.com/archives/C04DLAXFVCG/p1778570452385099?thread_ts=1778059456.405549&cid=C04DLAXFVCG) | Publisher/ Core Team |
| 2026-05-20 | [Data stream consumption - completeness test report (2nd check)](https://docs.google.com/spreadsheets/d/1-EzVQHnsOdmRV1K286Yy5sasOetSqSL0/edit?gid=1569150821#gid=1569150821) | Consumer/ Data Platform |

## **What Has Been Done**

### **Publisher**

1. **Backfill of missing completed messages** — The publisher has re-published completed messages from all previously missing points using the same queue name.  
   Confirmed by  on [Slack](https://teqplaydev.slack.com/archives/C04DLAXFVCG/p1778570452385099?thread_ts=1778059456.405549&cid=C04DLAXFVCG).

   **Known Issue:** Re-event triggers cause a spike in the number of queued messages.
2. **Verified message publication correctness** — Following a joint discussion with the consumer team ( / ), the publisher has confirmed that all completed messages are being published correctly and should be available in the queue.

### **Consumer**

1. **Implement message consumption traceability** — The consumer records all incoming messages and their processing states in the database.  
   **Outcome:** [Grafana dashboard](https://grafana.teqplay.nl/d/ff3wg1zj4qosge/airflow-metrics?orgId=1&from=now-30d&to=now&timezone=browser&var-unlocode=$__all) monitoring data streaming consumption and processing.
2. **Attempted batch size increase to 10,000 messages** — The consumer tested processing up to 10K messages per batch.

   **Outcome:** *This did not improve throughput*. Increasing the batch size linearly increased database write time, preventing the consumer from catching up.
3. **Enabled 2 parallel tasks with 1,500 messages per batch** — This configuration was identified as a sweet spot for stable processing.

   **Limitation:** While this improved throughput, *it does not fully resolve the low consumption rate issue*. The total volume of messages during re-event scenarios remains unpredictable and unmeasurable at present.

## **What Can Be Done Differently**

### **Cross-Collaboration (Publisher + Consumer)**

1. **Implement end-to-end message traceability** — Both teams must establish a mechanism to track completed messages broadcast and consumed, including their current state, supported by observable evidence.

   This enables side-by-side completeness comparisons based on **actual data** rather than assumptions. For example, if a re-event partially fails, it should be possible to trace which `visit_id`s were published successfully and which failed.

### **Consumer**

1. **Increase the number of parallel processing tasks/workers on the same topic** — Scaling the number of parallel consumers could improve throughput during high-volume periods.

   **Pre-requisite:** This action requires an estimation of the average number of completed messages produced when re-events are triggered, to right-size the configuration.
2. **Narrow down the streaming issue** — Temporarily ingest specific data streams (i.e., **NLRTM** and **USCRP**) to determine whether completed messages are lost or remain queued due to high publish rates during re-events.
3. **Manual run One DAG ingestions** — For re-event cases, we suggest handling them via manual One DAG Ingestions instead of the streaming pipeline, using specific times and unlocodes related to re-events.

### **Publisher**

1. **Introduce a rate limiter for re-event-triggered completed messages** — Apply a controlled broadcast rate (e.g., **1,000 completed messages/min**) specifically for completed messages produced by re-events.

   **Rationale:** Completed messages from re-events are not real-time events tied to a specific point in time — they are recalculated data. A controlled broadcast rate is preferable to unbounded publishing, which overwhelms the consumer.
2. **Route re-event-produced completed messages to a separate queue** — Isolating re-event messages from the main real-time queue would prevent re-event spikes from impacting normal real-time message consumption, and would allow independent scaling and monitoring of each stream. Proposed by [Richard on Slack](https://teqplaydev.slack.com/archives/C04DLAXFVCG/p1779949987652059?thread_ts=1779943797.540809&cid=C04DLAXFVCG).
3. **Do not add the newly re-event data to the queue** — The consumer needs to manually run an Airflow DAG that queries the VV API for specific times and related UN/LOCODEs.

## **Summary Table**

| **Area** | **Action** | **Owner** | **Status** |
| --- | --- | --- | --- |
| Completeness traceability | Track broadcasted/consumed messages with state evidence | Both | 🟡 Partially implemented (consumer only) |
| Batch processing | Tested 10K batch size | Consumer | 🔴 Not effective |
| Parallel processing | 2 parallel tasks @ 1,500 msg/batch | Consumer | 🟡 Partially improved |
| Focus testing on two ports | Ingest data streams from NLRTM and USCRP only | Consumer | 🟡 Ongoing (result will be available on June 6, 2026) |
| Message backfill | Re-published all missing completed messages | Publisher | 🟢 Done |
| Publication verification | Claimed that completed messages publish correctly | Publisher | 🟢 Done |
| Parallel scaling | Estimate re-event volume, increase parallel workers | Consumer | 🔵 Proposed |
| Rate limiting | Limit re-event completed messages to ~1,000 msg/min | Publisher | 🔵 Proposed |
| Queue separation | Separate queue for re-event completed messages | Publisher | 🔵 Proposed |
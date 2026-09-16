---
id: confluence:591757315
source: confluence
type: page
space: TC
title: Service Vessels Architecture overview
author: Milzam Abi Karami
date: '2025-04-22'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/591757315
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/591757315
---
# Service Vessels Architecture overview

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/591757315  

## Content

none

## Components

*1. NATS Queue*

·      The message broker for real-time event ingestion.

*2. Data Ingestion Service*

·      Reads events from NATS.

·      Parses and validates event messages.

*3. Internal Queue*

·      Acts as a buffer between the Data Ingestion and Activity Aggregation Service

*4.  Activity Aggregation Service*

·      Fetch new incoming events from Internal Queue

·      Fetch available data and last status from temporary storage.

·      Processes events to identify and classify activities.

·      Aggregates activities with relevant metadata (e.g., start time, end time).

*5.  Data Matching Service*

·      Matches aggregated activities to visit data using VesselVoyage API.

·      Enriches activities with details and PTT stage (Steaming In, Shifting, Steaming Out).

*6.  Output Generation Service*

·      Generating an `EnrichedActivityRecord`.

·      Writes activity records to RabbitMQ.

*7.  RabbitMQ*

·      The queue for downstream consumption.

*8.  Internal Cache*

·      Temporary storage for static data.

*9.  MongoDB*

·      We need some type of persistency to store the stream of events ingest from Nats.

10. *VesselVoyage API*

·      External API to fetch visit information.

## Data Models

## Workflow

### **1. Data Ingestion**

* **Input**: Real-time events from NATS.
* **Flow**:

  + Subscribe to relevant topics in the NATS queue.
  + Parse incoming messages and validate fields.
  + Store parsed `Event` objects in internal storage.
* **Output**: Validated events stored in internal storage.

### **2. Activity Aggregation**

* **Input**: Event objects from internal cache.
* **Flow**:

  + triggers based on the new events.
  + Fetch all events for a specific vessel from Internal storage.
  + Fetch last activity from either internal storage.
  + Sort events by timestamp.
  + Group events into activities based on:

    - Status changes (e.g., `Idle`, `Tugging`, `Transit`).
    - Time gaps or movement between locations.
  + Calculate metadata:

    - Start time, end time, and location.

o   Delete the old events from internal storage

* Store aggregated `ActivityRecord` objects in internal storage.
* **Output**: Aggregated activity records in Internal storage.

**Update:** This implementation section is combined with the **Data Ingestion** workflow as it is more convenient in doing it and there is no visible and no immediate drawback.

### **3. Data Matching**

a

* **Input**: ActivityRecord objects and VesselVoyage data.
* **Flow**:

  + Match `ActivityRecord` objects with:

    - visit ID from VesselVoyage API.
  + Determine PTT stage:

    - **Steaming In**: Cargo vessel is entering the port.
    - **Alongside**: Cargo vessel is alongside the berth.
    - **Shifting**: Cargo vessel is moving between berths.
    - **Steaming Out**: Cargo vessel is leaving the port.
  + Create enriched `EnrichedActivityRecord` objects.
* **Output**: Enriched activity records with detailed metadata.

**Update:** This implementation section is combined with the **Output Generation** workflow as it is more convenient in doing it and there is no visible and no immediate drawback.

### **4. Output Generation**

* **Input**: EnrichedActivityRecord objects.
* **Flow**:

  + Publishes the `EnrichedActivityRecord` to the RabbitMQ queue.

## Monitoring Goals

1. ***System Health Monitoring**:* Track uptime and resource usage of all system components.
2. ***Message Flow Monitoring**:* Monitor the rate of events ingested from NATS, processed through the pipeline, and published in RabbitMQ.
3. ***Error Tracking**:* Capture and analyze errors in event ingestion, processing, and data matching.
4. ***Performance Metrics**:* Measure processing times for activities like event ingestion, aggregation, and data matching.
5. ***Alerting**:* Notify operators of issues like service downtime, slow processing, or high error rates.
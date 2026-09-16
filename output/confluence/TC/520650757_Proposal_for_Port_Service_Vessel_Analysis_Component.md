---
id: confluence:520650757
source: confluence
type: page
space: TC
title: Proposal for Port Service Vessel Analysis Component
author: Maryam Tavakoli (Unlicensed)
date: '2024-11-21'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/520650757
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/520650757
---
# Proposal for Port Service Vessel Analysis Component

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/520650757  

## Content

**Project Overview**

This project aims to develop a **Port Service Vessel Analysis Component** that will analyze and track the journeys and activities of service vessels (starting with tugboats) within the port. The component will take historical events (event history or “revent”) as input data to reconstruct a comprehensive sequence of voyages and activities for each service vessel while within the port.

The output of this component will be a structured timeline of activities for each tug vessel, allowing us to associate each activity with specific port visits of cargo vessels. For the Minimum Viable Product (MVP), this component will focus specifically on **tug vessels** and their associated activities.

Given the frequent updates to port infrastructure (such as POMA), revent data is preferred due to its stability and accuracy in capturing events. The component does not require real-time analysis at this stage.

**Objectives**

1. **Event Aggregation**: Use historical event data to map the full journey of each tug vessel.
2. **Activity Analysis**: Analyze the activities of tug vessels within the port, grouping them into distinct voyages and activities.
3. **Visit Matching**: Match each identified tug activity with the cargo vessel visit data managed by the existing **VesselVoyage component**.

**Scope of MVP**

For the MVP, the component will specifically focus on:

* **Tug Vessels**: Analyzing the voyages and activities related to tugboats within the port, as tug operations represent a significant subset of port service vessel activities.

**Features**

The following features are required for the MVP:

1. **Tug Status Tracking**:

   * Record the **status** of the tug vessel at any given time, with possible statuses including:

     + **Idle**: Tug is stationary and not in service.
     + **Tugging**: Tug is actively assisting a cargo vessel.
     + **Transit**: Tug is moving between locations within the port.
2. **Time Stamping**:

   * Capture the **start time**, **end time**, and **duration** of each status.
   * This will enable the calculation of active and idle periods for each tug vessel.
3. **Port and Berth Visit References**:

   * Reference to **Berth Visit ID** and **Port Visit ID**, allowing integration with the cargo vessel data.
   * This will facilitate linking each tug activity to specific visits of cargo vessels within the port.
4. **Cargo Vessel Identification**:

   * Identify the **ID of the cargo vessel** being served by the tug during tugging activities.
   * This is essential for tracking and associating each tug activity with the corresponding cargo vessel.
5. **PTT (Port Turnaround Time) Stage Tracking**:

   * Capture the **PTT stage** of the cargo vessel being served, which can be in one of the following stages:

     + **Steaming In**: The cargo vessel is entering the port.
     + **Shifting**: The cargo vessel is moving between berths within the port.
     + **Steaming Out**: The cargo vessel is leaving the port.

**Technical Approach**

1. **Data Ingestion**:

   * Ingest historical event data (event history) as the primary data source.
2. **Activity Aggregation**:

   * Process and analyze the events to aggregate them into coherent journeys for each tug vessel.
   * Identify start and end points of each activity and categorize the activities based on their status (idle, tugging, transit).

**Idle**: Tug is stationary and not in service.  
 - start time  
 - end time  
 - duration  
 - location info  
**Tugging**: Tug is actively assisting a cargo vessel.  
 - start time  
 - end time  
 - duration  
 - other ship identifier  
 - start location  
 - end location  
 - (travel distance)  
**Transit**: Tug is moving between locations within the port.  
 - start time  
 - end time  
 - duration  
 - start location  
 - end location  
 - (travel distance)

3. **Data Matching**:

   * Match each activity record with the appropriate port and berth visit IDs to create a link between tug activities and cargo vessel visits.
   * Use the cargo vessel ID and PTT stage information to ensure accurate association with the cargo vessel's port visit stages.
4. **Output Generation:**  
   classify stages based on Vessel voyage to:

   * STEAMING IN
   * SHIFTING
   * STEAMING OUT

**Future Enhancements**

Upon successful completion of the MVP, future phases could expand the component to support:

* **Other Service Vessels**: Analysis of additional port service vessels beyond tugboats.
* **Real-Time Capabilities**: Adding real-time processing capabilities if operational needs evolve.
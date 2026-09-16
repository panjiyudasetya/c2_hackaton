---
id: confluence:285868041
source: confluence
type: page
space: TC
title: Cargo Operational Data (Moves Data)
author: Maryam Tavakoli (Unlicensed)
date: '2024-02-22'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/285868041
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/285868041
---
# Cargo Operational Data (Moves Data)

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/285868041  

## Content

Cargo-related information can be acquired from two sources:

* JOC
* WOD (Weekly Operational Data)

In the JOC file, we have access to:

* Timeframe
* Terminal name
* Cargo operational info

In the WOD file, we have access to:

* Ship name
* Terminal name
* Timeframe
* Cargo operational info

**IMO – Timeframe Mapping:**

This mapping is generated within the Data Warehouse (DWH) report and includes:

* Imo

* Timeframe

* VisitId

**MoveID – Timeframe Mapping:**

This information is extracted from the JOC file upon uploading it to the Python project. The mapping includes:

* MoveId

* Strat Time

* End Time

**MoveId-Imo-timeframe Mapping**:

This mapping is established upon uploading the WOD file to the Python Project and comprises:

* MoveId
* Imo

* Start Time

* End Time

**Python Project (matching script):**  
The matching process to link Cargo Operational data with its corresponding visit occurs here:

* For JOC files, we request a list of visits from the DWH based on the timeframe and terminal, perform the matching, and store MoveID, IMO, and timeframe in the database.

* For WOD files, we request a list of visits from the DWH based on the timeframe, IMO, and terminal ID, perform the matching, and store MoveID, IMO, and timeframe in the database.

**Transformation Component:**

When importing data from DWH to DM, for each visit, we request Cargo Operational data from the Python project by VisitID, then store the enhanced information in DM.
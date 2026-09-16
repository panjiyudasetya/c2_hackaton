---
id: confluence:931627009
source: confluence
type: page
space: TC
title: Context Mapping & Port Validation Process (updated)
author: astri
date: '2026-08-20'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/931627009
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/931627009
---
# Context Mapping & Port Validation Process (updated)

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/931627009  

## Content

This document contains the full context mapping and validation process (additional and detailed information of <https://teqplaybv.atlassian.net/wiki/x/AwA7Fw> & <https://teqplaybv.atlassian.net/wiki/x/AYD4GQ> ).

Context Mapping and Port Validation Process

| **Step** | **Tool / System** | **Description** | **Notes / Dependencies** |
| --- | --- | --- | --- |
| **Mapping Port in POMA** | <https://pomadata.teqplay.nl/> | Step where ports, terminals, berths, and related areas are mapped or updated to ensure accurate data. | * Ensure port, terminal, berth, and other infrastructure are filled completely (e.g., cargo category, vessel type). * Validate with the latest external references or IHS. * Required before **VesselVoyage recalculation** can begin (Adding the port to whitelist after validation) |
| **Recalculation (Revents Monitoring) in VV** | <https://vesselvoyagedata.teqplay.nl/> | Performs recalculation of vessel visit data (Revents) based on updated port mappings. This aligns timestamps and event logic. | * Depends on updated **port mapping** from POMA. * Output used for **Airflow ETL** process. |
| **Datawarehouse & Datamart Building in Airflow** | [*Airflow*](https://airflowdata.teqplay.dev/) | Orchestrates ETL pipelines to build and update datawarehouse and datamart tables. | Ingest data from VesselVoyage, POMA, and CSI. |
| **Datamart Import to BI** | [Power BI](https://app.powerbi.com/groups/c378e258-c3ea-418c-8447-78d9b6cd726c/datasets/5202703a-b079-44d7-a077-0ed299cba73c/details?experience=power-bi) | Imports datamart for Data Validation dashboard | Uses Airflow outputs as input source. |
| **Validation in BI** | [Power BI](https://app.powerbi.com/groups/c378e258-c3ea-418c-8447-78d9b6cd726c/reports/8f4b484b-12b0-4907-b842-8eb6fac297d4/ad07c67d890e7eb2d334?experience=power-bi) | Validating port using Data Validation dashboards. | Findings from BI validation often led to adjustments in **POMA** (mapping) or **CSI** (ship information update/correction).  Typically, 1 - 3 rounds of validation are required. |
| **Update CSI Data** | <https://csidata.teqplay.nl/> | The CSI (Central Ship Information) layer stores ship metadata ([detailed CSI document](https://teqplaybv.atlassian.net/wiki/x/BgBPLw)). This step verifies that the ship information for visits to the selected port is correct. | * Check for duplicate IMO records or missing ship information (Category V2, LoA, Beam, DWT, etc.). * Airflow’s DAG which related to ship and ship mapping need to re-run |
| **Update in Issue Tracker** | [Pto result issue mapping](https://docs.google.com/spreadsheets/d/1ol5ySXlJrFKRsuBCFduRxA-xsINbvp19cv82Q7isO7Y/edit?gid=743392294#gid=743392294) | Document identified issues related to VesselVoyage data. | * Depends on **BI validation results**. * Ensures feedback loop to VesselVoyage/core components team |

# Mapping Port in POMA

## 1. Compare Current Mapping (Teqplay DB) with External Database

Compare the existing mapping with the external database. Verify if the berth, terminal, or port information in the external database adds relevant value to the Teqplay data. Select the most complete and current data before detailed mapping and validation process. **This step is only for “Not Mapped” port. Eg:**

## 2. Select and Import Port from External Database

* Select the relevant **Port** from the external database.
* Verify that the external database reference is the more complete and latest update
* Click **Import and overwrite port data** to bring it into Teqplay DB.
* **Never import and overwrite port data for “Fully Mapped” & “Basic Mapped” ports.**
* The mapping will automatically adjust to align with imported data.

## 3. Port Infrastructure Mapping

Defining all key infrastructure and operational areas of a port such as terminals, berths, and navigational zones in POMA. The following steps outline the port mapping procedure:

* If terminals are already mapped, update them as needed, ensuring that the cargo type matches the relevant category.
* If berths are already mapped, update them as needed, ensuring that the cargo type matches the relevant category, and link each berth to the correct terminal.
* **Map any unmapped areas**

### 3.1 Terminal Mapping

Identifying a terminal from satellite image:

* Look for long quays with berthing lines and loading/unloading equipment (cranes, jetties).
* Identify storage areas such as container yards, tanks, or warehouses indicate terminal types.
* Match visual boundaries with official information from port authority maps or external databases.

Below is **Berth & Terminal Visual Reference Table** to help identify port infrastructure/features when mapping in POMA.

| **Terminal/Berth Type** | **Key Visual** | **Operations / Cargo** | **Example Image from POMA** |
| --- | --- | --- | --- |
| **Container** | Large gantry cranes, container stacks, and wide paved storage yards. | Containerized cargo (standardized containers). |  |
| **Dry Bulk** | Open storage areas with large stockpiles, hoppers, and conveyor belts. | Bulk commodities like coal, ore, grain, or cement. |  |
| **Breakbulk** | Warehouses, sheds, or covered storage nearby; uses mobile or jib cranes. | General cargo, steel products, woods, machinery, project cargo. |  |
| **Wetbulk** | Pipelines, manifolds, and tank farms connected to jetties or dolphin structures. | Oil, chemicals, LPG/LNG, and other liquid bulk cargo. |  |
| **Ro-Ro** | Sloped ramps or linkspans connecting directly to shore or terminals. May have adjacent vehicle staging areas. | Roll-on/roll-off  cargo such as cars, trucks, and trailers. |  |
| **Passenger** | Terminal buildings, parking areas, and access roads for buses and cars. | Cruise ships or ferry operations. |  |

Add terminal in POMA:

* Click **“+”** (upper right corner) → select **Terminal**
* Fill in required fields:

  + **Name and Display Name**
  + **Linked Port** (confirm it’s correct)
  + **Cargo Category Type** – e.g., containers, liquid bulk, dry bulk, passengers.
* Check the **User Validated** field.
* Map or modify the Terminal **Area** (polygon or shape representing the terminal boundaries).

### 3.2 Berth Mapping

Identifying the berth structure from satellite image:

* Look for **long straight edges** along the waterfront (**quay or piers** where ships moor).
* Berths are often **lined with cranes, bollards, or fenders** visible from satellite imagery.
* Each berth is usually separated by a **small gap, loading area, or mooring section**.
* Check for operational clues (see Berth & Terminal Visual Reference Table)

Add berth in POMA:

* Click **“+”** (upper right corner) → select **Berth**
* Fill in required fields:

  + **Name, Name Long, Display Name**
  + **Cargo Category Type**
  + **Vessel Type Allowed**
* **Confirm the berth is linked to the correct port and terminal**
* Check the **User Validated** field.
* Map or modify the Berth Area (polygon or shape representing the terminal boundaries) and save changes

### 3.3 Port Area Mapping

Port area defines the overall administrative boundary of the port. Used to identify the geographic scope of port operations and jurisdiction. **The information of port boundaries can be obtained from** [**IHS**](https://teqplaybv.atlassian.net/wiki/pages/resumedraft.action?draftId=933330966&draftShareId=8af9c746-ed0a-43a1-b971-de6d39f162b9)**, the official port website, or nautical charts.**

* To define port area in POMA, select the port and select **Location.**

* Map or modify the **Port Area** (polygon or shape representing the port boundaries) and save changes

### 3.4 Anchorage Area Mapping

Anchorage area represents areas where vessels anchor temporarily before entering the port or waiting berth assignment. How to find and map anchorage area:

* Locate anchorages in [OpenSeaMap](https://map.openseamap.org/) **or any nautical chart** (e.g., [MarineTraffic: Global Ship Tracking Intelligence | AIS Marine Traffic](https://www.marinetraffic.com/en/ais/home/centerx:-46.276/centery:-24.162/zoom:12))

  Vessels anchored before entering the port of Santos in Anchorage No.4 (eg:

  [LITO | Timeline](https://timeline.teqplay.nl/636015548?from=1750468524000&to=1751787545000&URL=https%3A%2F%2Fapi.teqplay.nl%2Fv0&selectedTime=1750942324487))

  Aransas Pass anchorage area of Port of Corpus Christi outlined in purple dash line

* Looking in **VesselVoyage** where vessels layed still before entering the port

  The nodes represent anchorage area

Anchorage area checking from available SOF in VesselVoyage

* Use <https://onthemap.teqplay.nl> or check the **anchor event** in the <https://timelinedev.teqplay.nl/>

  The vessel anchored in this area, indicated by status and speed shown in the timeline
* Check **IHS (Navigation menu).** For most ports, IHS provides location coordinates.

* To add anchorage area in POMA, click **“+”** (upper right corner) → select **Anchorage.**

* Map or modify the **anchorage area** and save changes.

  Anchorages mapped in POMA (green) and anchorage area symbols from the OpenSea map layer (purple)

### 3.5 Pilot Boarding Place Mapping

The **Pilot Boarding Place** is the area where maritime pilots board incoming vessels to guide them safely into port.

* Locate pilot areas in [OpenSeaMap](https://map.openseamap.org/) **or any nautical chart** (e.g.,[MarineTraffic: Global Ship Tracking Intelligence | AIS Marine Traffic](https://www.marinetraffic.com/en/ais/home/centerx:-46.337/centery:-24.009/zoom:17), event example: [timeline](https://timelinedev.teqplay.nl/))

“Pilot Mass” is a pilot boarding place. It represented by a circle containing a vertical symbol in nautical charts.

* Check **pilot behaviour or pilot encounters event** in the <https://timelinedev.teqplay.nl/>

The green dot in timeline indicates pilot encounters

* Check **IHS (Navigation menu).** For most ports, IHS provides location coordinates.

* To add pilot boarding place in POMA, click **“+”** (upper right corner) → select **Pilot boarding place.**

* Map or modify the **Pilot Boarding Place** and save changes.

  PBP mapped in POMA (blue circles)

### 3.6 Lock Mapping (if applicable)

Locks are structures used to **raise and lower vessels** between stretches of water of different levels within a port or canal system. Only applicable to ports with internal waterways. They are easy to find, as shown in the example below.

* To add lock in POMA, click **“+”** (upper right corner) → select **Lock**
* Map or modify the **lock** and save changes.

Locks represent with pale pink rectangular in POMA

### 3.7 Approach Area Mapping

Often called as “point of no return,” this is the area where ships move from open sea into the protected waters of the harbor. It marks the start of the safe navigation route that vessels follow when entering the port.

* To add approach area in POMA, click **“+”** (upper right corner) → select **Approach area**
* Map or modify the **approach area** and save changes.

The yellow rectangle indicates the approach area. In Port of Santos, it marks the final part of the pilot boarding place.

### 3.8 Breakwater Area Mapping (if applicable)

The Breakwater Area refers to the zone defined by protective barriers that shield the port from strong waves, currents, and coastal erosion, creating calm waters inside the harbor for safe vessel berthing and maneuvering.

The small red circle marks the artificial breakwater area, while the large red circle represents the entire breakwater area.

For example, an article on converting the current natural breakwater area into an artificial breakwater area at the Port of Santos:

[Port of Santos Breakwater Area - Ponta de Praia](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.transnav.eu%2Ffiles%2FAlternative_study_for_the_Nautical_and_Shore_Protection_Structures_in_the_Estuary_of_Santos_Brazil%2C822.pdf&psig=AOvVaw280jBdxArdQvEtdcdGcclX&ust=1760473441301000&source=images&cd=vfe&opi=89978449&ved=0CBkQ3YkBahcKEwjYz5_1gKKQAxUAAAAAHQAAAAAQCw)

* To add breakwater area in POMA, click **“+”** (upper right corner) → select **Breakwater area**
* Map or modify the **breakwater area** and save changes.

Breakwater area mapped in POMA

### 3.9 EOS Area (automatically added)

The **End of Sea area** represents the **outer boundary of the port’s maritime zone**, where the port’s jurisdiction or operational responsibility ends and open sea begins. It is automatically added in POMA when creating port areas, anchorage areas, and PBPs.

* At first, the EOS area is automatically assigned when the port already has complete infrastructure (port area, anchorage area, pbp area).
* To modify the EOS area, select the port, then choose **Location**, and update **End of sea passage**.
* When we modify the port area, anchorage area, or PBP area, the EOS area does not automatically update to reflect those changes. We need to update it manually by deleting all JSON values in the box and then saving the changes.

EOS area mapped in POMA

## 4. Validate and Finalize

Use the **Guided Completion** feature to check for:

* Missing **Cargo Category Types**
* Missing **Vessel Category Types**

Make sure we know what terminal the customer is mapping (if applicable) to what terminal in POMA and validate proper naming.

Guided Completion for Cargo Category Type

Guided Completion for Vessel Type Allowed

**After all infrastructure has been mapped, click “Add to Whitelist” so that the port appears in VesselVoyage.**

## 5. Merge and Synchronize POMA live with POMA data

* Push **Merge** button (at the top right corner) to consolidate all updates.
* **Sync** the changes in POMA **Live** (**make sure to select only ports that have been recently fully mapped and validated in BI**)

  example: sync PACTB only

## 6. Final Checklist

Do final checklist in POMAdata and POMAlive:

* All ports, terminals, and berths mapped and validated.
* All relevant areas (anchorage, approach, breakwater, etc.) are defined.
* No missing cargo or vessel types.
* Confirm which terminal the customer maps to in POMA and validate its name

# Recalculation in VesselVoyage

* Open VesselVoyage data and select **“Scenarios”**
* Create a new scenario for Port by selecting the port name/UNLOCODE and date
* The recalculation in VV is only for whitelisted ports in POMA

* **Once recalculation finishes, the event status shows “PARTIALLY\_FAILED”**

## Datawarehouse and Datamart Building in Airflow

* Check the **Teqplay ETL Pipeline** process here: <https://teqplaybv.atlassian.net/wiki/x/AoAjKg>
* **The data engineers have provided one DAG for all in the Airflow to run ETL Pipeline; just click trigger for this DAG: start\_etl\_pipeline.**
* If the process fails (Airflow DAG failure), handle it manually by referring to this document: <https://teqplaybv.atlassian.net/wiki/x/AYAiNQ>
* Once it finishes, the notification will appear in the Slack channel <https://teqplaydev.slack.com/archives/C094ULG53TQ>

## Datamart Import to BI

Refresh **PTO Ports semantic model** in Development workspace [Power BI](https://app.powerbi.com/groups/c378e258-c3ea-418c-8447-78d9b6cd726c/datasets/5202703a-b079-44d7-a077-0ed299cba73c/details?experience=power-bi)

## Validation in BI

Open [Data Validation - Power BI](https://app.powerbi.com/groups/c378e258-c3ea-418c-8447-78d9b6cd726c/reports/8f4b484b-12b0-4907-b842-8eb6fac297d4?experience=power-bi) in Development workspace. Below are items to check:

| **Category** | **Check Item** | **Description / Validation Notes** |
| --- | --- | --- |
| **Ship** | **No TEU / Vessel Category** | Ensure the **Category v2**, **LOA**, **Beam**, and **DWT** fields are filled and correct. TEU should not be missing for container vessels. |
|  | **Wrong Ship Type** | Verify the **ship type** is accurate and matches the operational data (e.g., tanker, bulk carrier, container ship). Correct mismatched ship classifications in CSI. |
| **Terminal & Berth** | **Wrong Terminal or Berth Type** | Confirm that each terminal and berth is assigned the correct type (e.g., liquid bulk, dry bulk, container). |
| **Anchorage** | **Missing Linked Anchorages** | Check for all anchorage areas that vessels visiting the port have used |
| **PTT Stages** | **Anchor** | Verify that the anchoring event is correctly recorded and anchor duration is accurate. |
|  | **Steaming In** | Ensure steaming in duration is is accurate. |
|  | **Berth Stay** | Confirm berth stay durations are correct and non-negative. |
|  | **Shifting** | Validate shifting events between berths or terminals are correct. |
|  | **Steaming Out** | Check that steaming out duration is correct and timestamps are consistent. |
| **Nautical Services** | **Towage Activities** | Confirm towage activity exist and the timestamp is correct. |
|  | **Bunkering Activities** | Verify bunkering activities are recorded in VV where applicable. |
|  | **Pilotage Activities** | Ensure pilotage events (pilot onboard/disembarked) are recorded and the timestamp is correct |
| **Negative Values** | **Duration Check** | Review all duration fields to ensure **no negative values** exist. Negative durations indicate incorrect timestamp in VV. |
| **Random Ship Checks** | **Timestamp Validation** | Select **10 random ships** and verify that all key timestamps are correct and ordered (arrival, pilot on board, berthing, departure). |
| **Multiple IMO Records** | **Duplicate IMO Numbers** | Check the CSI for vessels with **duplicate or conflicting IMO records**. Resolve any overlapping entries. |
| **Timestamp Completeness** | **Event Timestamp** | Ensure each visit includes: **EOS Entry**, **EOS Exit**, **Pilot Onboard**, and **Pilot Disembarked** events. |
|  | **Duplicate Visits** | Verify that there are **no duplicated** port, terminal, or berth visits recorded for the same vessel. |

## Update Issue Tracker

[Pto result issue mapping - Google Sheets](https://docs.google.com/spreadsheets/d/1ol5ySXlJrFKRsuBCFduRxA-xsINbvp19cv82Q7isO7Y/edit?gid=743392294#gid=743392294)
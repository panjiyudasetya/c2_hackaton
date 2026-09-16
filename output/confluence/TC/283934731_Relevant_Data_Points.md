---
id: confluence:283934731
source: confluence
type: page
space: TC
title: Relevant Data Points
author: Joost Dambrink (Unlicensed)
date: '2024-03-19'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/283934731
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/283934731
---
# Relevant Data Points

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/283934731  

## Content

All of the data-points available in the Statement of Facts (SOF) documents relevant to the SOF OCR Project ranked with priority. The document has been divided into sections present in the SOF document.

26falselistfalse

## Guide

| **Priority** | **Description** |
| --- | --- |
| MustRed | Must be available in the SOF document. Will be a show-stopper if not. |
| EssentialYellow | Is essential for the project to retrieve |
| NTHGreen | Nice-to-have, not required |
| SUPPORTBlue | Support field used to retrieve another field. |

| **Priority** | **Name** | **Definition** | **Usage** |
| --- | --- | --- | --- |
| EssentialYellow | The name of the data point | The definition of the data point | List of synonyms that are used to refer to this data point in the SOF document |

## Header

| **Priority** | **Name** | **Definition** | **Usage** | **Remarks** |
| --- | --- | --- | --- | --- |
| MustRed | **Vessel Name** | The name of the vessel that is loading/discharging cargo | * Vessel * Ship * Ship Name |  |
| SUPPORTBlue | **Voyage Number** | Identifier used for the current voyage of the vessel | * Voyage No. * Voy | Supports Vessel Name field |
| EssentialYellow | **Loading/ Discharging** | Field to state if the document is about loading or discharging | * Loading/Discharging | Can also be stated in the title of the SOF |
| EssentialYellow | **Cargo Type** | The type of cargo | * Cargo Type * Cargo |  |
| SUPPORTBlue | **Cargo Operation** | More specified information about the cargo operation | * Cargo Operation * Operation |  |
| EssentialYellow | **Cargo Total** | The amount of cargo that is being loading/discharged | * Quantity as per Bill of Lading * Quantity as per Mate’s Receipt * Total Cargo Discharge * Quantity On arrival | The different usages can mean different things |
| EssentialYellow | **Cargo Reference** | The order number of the cargo (reference number) | * Reference Number |  |
| SUPPORTBlue | **Shipper Name** | Company of the ship | * Shipper |  |
| SUPPORTBlue | **Port Office** | Name of the port office the loading/discharging is happening in | * Port Office |  |
| EssentialYellow | **Terminal** | The terminal where the cargo operation is happening | * Terminal * Terminal Name |  |
| SUPPORTBlue | **Berth** | The berth where the cargo operation is happening | * Berth * Name of Berth | Supports the terminal field |
| SUPPORTBlue | **Last Port** | The last port visited by the ship. | * From * Last Port |  |
| SUPPORTBlue | **Next Port** | The port the ship is travelling to after the cargo operations. | * Next Port * Next |  |
| SUPPORTBlue | **From/To** | The port the ships comes from and the port the ship is travelling to after cargo operations | * From/To |  |
| MustRed | **Port** | The port the cargo operations are taking place in | * Port Of Service * Port Of Loading * Port Of Discharge |  |
|  | **Call Number** | Not sure what this means |  |  |
| EssentialYellow | **Date** | Can mean multiple things:   * The date range of the cargo operations (e.g. 12 - 13 december) * The date the documents was filled-in/signed | * Date |  |
| EssentialYellow | **Local Time** | The local time zone of the port the cargo operations are happening in. | * Local Time * Timezone |  |

## Timestamps - Vessel Arrival

| **Priority** | **Name** | **Definition** | **Synonyms** | **Remarks** |
| --- | --- | --- | --- | --- |
| EssentialYellow | End of Sea Passage | The time the ships arrives at pilot station, anchorage area or waiting area of a port | * End of Sea Passage * EOSP * Arrived [port] EOSP |  |
| EssentialYellow | NOR Tendered | The time the Notice of Readiness document is tendered | * NOR Tendered |  |
| EssentialYellow | NOR Re-Tendered | The time a Notice of Readiness document is re-tendered | * NOR Re-Tendered |  |
| EssentialYellow | Anchor Up | The time the ship droppen the anchor | * Anchor Up * Anchor Heaved * Anchored Aweigh |  |
| EssentialYellow | Anchor Down | The time the ship heaved the anchor | * Anchor Down * Anchor Dropped * Anchored |  |
| EssentialYellow | Pilot on Board | The time the pilot has entered the ship | * POB * Pilot on Board * Pilot Boarded |  |
| EssentialYellow | Free pratique granted | The ship is given permission by the port to enter because it has been certified free of infectious disease | * Free pratique granted |  |
| EssentialYellow | Entered Port | When the ship has entered the port | * Entered Port |  |
| EssentialYellow | First Line | Not 100% sure | * First Line * First Line Ashore |  |
| EssentialYellow | All Fast | Not 100% sure | * Last Line * All Fast * All Fast alongside |  |
| EssentialYellow | NOR (re-tendered) Received | When the NOR is received at the terminal | * NOR Received |  |
| EssentialYellow | NOR (re-tendered) Accepted | When the NOR is accepted by the terminal | * NOR Accepted |  |
| EssentialYellow | Gangway down | When the ship has lowered the gangway | * Gangway Down |  |
| EssentialYellow | Pilot Disembarked | When the pilot has left the ship | * Pilot Off * Pilot Disembarked |  |

## Timestamps - Cargo Operation

| **Priority** | **Name** | **Definition** | **Synonyms** | **Remarks** |
| --- | --- | --- | --- | --- |
| EssentialYellow | Surveyor On Board | The surveyor has entered the ship | * Surveyor On Board |  |
| EssentialYellow | Surveyor Off Board | The surveyor has left the ship | * Surveyor Off Board |  |
| EssentialYellow | Sampling Started | Sampling of the cargo has started | * Sampling Started | Only when Discharging |
| EssentialYellow | Sampling Completed | Sampling of the cargo is completed | * Sampling Completed | Only when Discharging |
| EssentialYellow | Commenced Tank Inspection | The inspection of the ship’s tanks has commenced | * Commenced Tank Inspection * Tank Inspection |  |
| EssentialYellow | Completed Tank Inspection | The inspection of the ship’s tanks has completed | * Cargo Tanks Inspected * Completed Inspections |  |
|  | Calculations Started | Not 100% sure | * Calculations started | Only when Discharging |
|  | Calculations Completed | Not 100% sure | * Calculations completed | Only when Discharging |
| EssentialYellow | Hoses / Arms Connected | The hoses / arms for loading / discharging have been connected | * Hoses / Arms Connected | Depends if Liquid/Bulk |
| EssentialYellow | Commenced Discharging / Loading | The discharging / loading has started | * Commenced Discharging / Loading | Depends on the cargo operation type |
| EssentialYellow | Stoppage Discharging / Loading | The discharging / loading has been temporarily stopped | * Stoppage Discharging / Loading |  |
| EssentialYellow | Completed Discharging / Loading | The discharging / loading has completed | * Completed Discharging / Loading |  |
| EssentialYellow | Hoses Disconnected | The hoses/arms for loading/discharging have been disconnected | * Hoses/Arms Disconnected | Depends if Liquid/Bulk |
| EssentialYellow | Documents on Board | Not 100% sure | * Documents on Board * DOB |  |

## Timestamps - Vessel Departure

| **Priority** | **Name** | **Definition** | **Synonyms** | **Remarks** |
| --- | --- | --- | --- | --- |
| NTHGreen | Pilot on Board | Pilot has boarded the ship | * POB * Pilot on Board * Pilot Boarded |  |
| EssentialYellow | Vessel Left Berth / Terminal | Vessel has left the Berth / Terminal | * Vessel left berth * Vessel left terminal |  |
| NTHGreen | Last Line Released | Last line of the ship has been released | * Last Line * All Fast * All Fast alongside |  |
| NTHGreen | Gangway Down/Up | Gangway on the ship has been lowered so the pilot can leave | * Gangway Down |  |
| NTHGreen | Pilot Disembarked | Pilot leaves the ship | * Pilot Off * Pilot Disembarked |  |
| NTHGreen | Completion Tug | Tugging by tugboats has been completed | * Completion Tug * Tug finish |  |
| EssentialYellow | Vessel Sailed | The vessel has left the port and is sailing to the next port | * Start of Sea Passage * Vessel Sailed |  |
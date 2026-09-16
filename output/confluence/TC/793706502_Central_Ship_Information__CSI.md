---
id: confluence:793706502
source: confluence
type: page
space: TC
title: Central Ship Information (CSI)
author: astri
date: '2025-07-11'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/793706502
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/793706502
---
# Central Ship Information (CSI)

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/793706502  

## Content

**Central Ship Information (CSI)** is Teqplay’s internal ship information database that includes all ships that records by AIS in our system.

## **CSI Features**

### **1. Ship search**

We can search ship by MMSI, IMO. ENI, Name, and Flag. The list of ships that match with filters will appear on the right side. To show the ship details, double click the ship row.

### **2. Tickets**

The **Tickets** tab displays all open tickets or change requests. It lists ships with changes in fields such as name, category, call sign, and others. From here, we can review each change and choose to approve or delete it. ***Tickets are added automatically by system every Thursday, with around 200 - 300 open tickets generated weekly.***

Example of “name & IMO changes” ticket:

We need to check and verify the updated information for this ship (in this case: IMO & Name) by comparing it with external sources such as [MarineTraffic](https://www.marinetraffic.com/) and [VesselFinder](https://www.vesselfinder.com/), and also reviewing the AIS information. Then, we can approve/reject the change and close the ticket.

On average, we can process approximately 70-100 tickets per hour depending on how much change is required for each ticket.

### **3. Create ticket**

The selected ship can be linked to marine traffic, AIS data, Q88, and display the ship image when the toggle switch is turned on.

### **4. IMO/MMSI Mapping**

The IMO/MMSI Mapping tab will show a list of ships that has open IMO/MMSI Mapping ticket to review, approve, or delete them.

#### IMO Number:

* Permanent Ship Identifier issued by International Maritime Organization
* Even if the ship changes name, flag state, etc, the **IMO number is fixed** (stays the same for regulatory purpose)

#### MMSI Number:

* **MMSI number is changeable** when there are updates in flag state/ship switch flag states, radio communication equipment, having multiple communication systems

#### **IMO/MMSI Mapping Tickets**

***Tickets are added automatically by system each day, with around 40–60 open tickets generated daily. The same ship often reappears on the following day or a few days later.*** Each IMO/MMSI mapping ticket takes longer to process than the normal ticket. In average, we can process approximately 30-40 IMO/MMSI tickets per hour.

**There are 4 different types of IMO/MMSI mapping tickets in CSI:**

* **MMSI Changed Already**

  + **The ship’s MMSI may have changed either before or early in the observation period.** To determine the exact time of the change, click the **timeline** button. In the timeline view, an MMSI change is typically indicated by a change in the ship’s color. We can identify the exact time of the change by checking the timestamp (shown in the orange box in the timeline screenshot below) and filling in the **time** field in the ticket using the `selectedTime` value from the URL. If there is no MMSI change detected after we check and verify, we can click “DO NOTHING” option in “Resolve strategy” field. Once all fields are correctly filled in, we can save and close the ticket. Example:

    - [ASTRO SCULPTOR | Timeline](https://timeline.teqplay.nl/636025118,412203630?from=1751155200000&to=1751760000000&selectedTime=1751461026310&URL=https%3A%2F%2Fapi.teqplay.nl%2Fv0), **MMSI have been changed since Jul 2nd while the observation period is Jul 5-6th. So, we can fill the time with Jul 2nd (1751461026310).**
* **MMSI Changed**

  + It displays **ships that have changed their MMSI during the observation period.** To verify whether the recorded time of the MMSI change is correct, click the **timeline** button and follow the same steps as above. Example:

    - [GREEN ATLANTIC | Timeline](https://timeline.teqplay.nl/306425000,511101711?from=1751324400000&to=1751763600000&selectedTime=1751700318704&URL=https%3A%2F%2Fapi.teqplay.nl%2Fv0), MMSI changed from 306425000 to 511101711 on 05/07/2025, 14:02:16 (1751698936649)
* **MMSI Gets Set**

  + It displays ships that have been assigned a fixed MMSI. This usually occurs for ships that previously had an IMO number but didn't have MMSI information in CSI. The "To MMSI" field is blank by default, so we need to fill it in using the MMSI from the "ratio" information or with the correct MMSI.
* **Multiple MMSI**

  + Multiple MMSI tickets appear when our system/AIS detect > 1 MMSI in ship with the same IMO
  + The "ignored MMSI" information typically appears in "MULTIPLE MMSI" tickets, where a ship has >1 MMSI, and we need to select the recent/correct one MMSI.
  + When a recent/correct MMSI is selected, CSI ignores all other MMSIs that associated with the ship except the selected one.
  + Example:

    - [OCEAN BEGONIA | Timeline](https://timeline.teqplay.nl/636025266,538008143?from=1751587200000&to=1751760000000&selectedTime=1751587200000&URL=https%3A%2F%2Fapi.teqplay.nl%2Fv0). When the ship enters Singapore, it temporarily uses multiple MMSI (538008143 & 636025266). However, once it leaves Singapore, it reverts to the previous MMSI (636025266), which is then set as the current MMSI, and ignore 538008143.

### **5. Add ship**

In case there are new ship release that not yet available in CSI, we can add it manually.

## Reoccurring IMO/MMSI Mapping Tickets

Based on our observation, reoccurring tickets mostly happened for **Multiple MMSI & MMSI Changed Already** tickets. We can check the reoccurring IMO/MMSI mapping tickets here: [CSI Ticket Check (IMO/MMSI only)](https://docs.google.com/spreadsheets/d/1wSBr44rNjtZ_lp8ICNcYiHGilbMOVcRCisMgqWSKpS8/edit?gid=0#gid=0).
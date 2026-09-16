---
id: confluence:405012483
source: confluence
type: page
space: TC
title: Original Process developed for APMT
author: Richard van Klaveren
date: '2024-07-15'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/405012483
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/405012483
---
# Original Process developed for APMT

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/405012483  

## Content

The original process as developed and applied for APMT ports looked like:

 With the following sub-steps: (also located in spreadsheet [here](https://docs.google.com/spreadsheets/d/1UserXpiJbc5E1wkb6S0G8AOZJZFpLqdnADQReZ-qZFk/edit?gid=0#gid=0))

|  |  |  |  |
| --- | --- | --- | --- |
| **1** | **Add initial context information on the relevant port** |  |  |
| 1.1 |  | POMA: Check if the Berth / Terminal / Port information in WOP is adding relevant value to the Teqplay data, if is: |  |
| 1.1.1 |  |  | Import the WOP data into the Teqplay layer in POMA |
| 1.1.2 |  |  | Remove the terminals and berths at open sea (if any) |
| 1.1.3 |  |  | Update all berths where needed (make sure cargoType is set to the relevant category for all berths) |
| 1.1.4 |  |  | Update all terminals where needed, and make sure the berths are linked to the relevant terminal |
| 1.2 |  | POMA: Lookup anchorages and pilot areas and add them to POMA |  |
| 1.2.1 |  |  | Find anchorages in openSeaMap, any nautical Map, looking in vv where vessels layed still before entering the port, use onthemap, check IHS |
| 1.2.2 |  |  | Find pilot areas in openSeaMap, any Nautical map, any pilot vessel behavious, check IHS |
| 1.3 |  | CSI / Shipmapper: Identiy the vessels with a relevant role in the port (pilot, tugs, bunker, waste, water, boatman, ....) |  |
| 1.4 |  | POMA: Make sure we know what terminal the customer is mapping to what terminal in Poma, and validate proper naming |  |
| 1.5 |  | POMA: check via terminal website / Google maps / photo footage what part of the terminal is used for what (in case of general purpose terminal) and update berth and cargo category mapping |  |
| **2** | **Make POMA data available to end-user applications** |  |  |
| 2.1 |  | POMA: Add the port to the 'whitelist' in the db so that Teqplay information will always be used for the merge instead of WOP data |  |
| 2.2 |  | POMA: Trigger a merge |  |
| 2.3 |  | Share the GeoBoundingboxes with the customer to validate the context used is as expected |  |
| **3** | **Generate validation data** |  |  |
| 3.1 |  | PTO: Update the POMA and CSI cache in PTO as applicable |  |
| 3.2 |  | PTO: Run a report per port involved and download the resulting Audit-report and Excel Report |  |
| **4** | **Do an initial validation of the data in PTO context per port involved** |  |  |
| 4.1 |  | Validate the report on the following steps, and mark the ones that are ok, and the ones that need further validation: |  |
| 4.1.1 |  |  | no TEU / Vessel category |
| 4.1.2 |  |  | Unmatching anchor up/down |
| 4.1.3 |  |  | Top 10 Shortest anchor duration |
| 4.1.4 |  |  | Top 10 Longest anchor duraiton |
| 4.1.5 |  |  | Top 10 shortest berth duration |
| 4.1.6 |  |  | Top 10 Longest berth duration |
| 4.1.7 |  |  | 10 random ships |
| 4.1.8 |  |  | 10 large time differences between acnhor-up and pilot inbound |
| **5** | **Validate failures and decide what issues need fixes** |  |  |
| 5.1 |  | Validate the ones that are marked for further validation and generate results into Context mapping updates, CSI updates or bug reports |  |
| 5.2 |  | Mark those ports in the database of PTO that need vesselvoyage recalculate |  |
| **6** | **Fix bugs detected during the validation phase (step 3)** |  |  |
| 6.1 |  | Analyze |  |
| 6.2 |  | Fix |  |
| 6.3 |  | Deploy in dev |  |
| 6.4 |  | Test in dev |  |
| 6.5 |  | Deploy in live |  |
| **7** | **Generate the target data into the DWH and datamart** |  |  |
| 7.1 |  | PTO: Update the POMA and CSI cache in PTO as applicable |  |
| 72 |  | PTO: Run the report from the UI with 'update datamart' enabled |  |
| 7.3 |  | Download the final Excel report and do a check on negative values, missing data and glance over the diagrams |  |
| **8** | **Validate Resulting Reports before updating the customer** |  |  |
| 8.1 |  | Load the data into the Test environment of PowerBI |  |
| 8.2 |  | On the Terminals configuration workbook, |  |
| 8.2.1 |  |  | Add the terminal of the customer on the Terminal Focus sheet |
| 8.2.2 |  |  | Add the benchmark terminals on the Benchmark Pairs sheet (make sure the terminal IDs are matching PTO) |
| 8.3 |  | Make the terminal name based on APM / JOC |  |
| 8.4 |  | Run the moves script |  |
| 8.4.1 |  |  | Export PTO data (at the moment, this is done using DAX Studio from Power BI) |
| 8.4.2 |  |  | Update the paths to most recent APM / JOC files on the moves script |
| 8.4.3 |  |  | Run the script |
| 8.5 |  | Upload output Moves worksheet on drive |  |
| 8.6 |  | Refresh Moves table on Power BI |  |
| 8.7 |  | Validate the quality of the data through the TEST dashboard |  |
| **9** | **Deliver to the customer** |  |  |
| 9.1 |  | Update the live dashboard |  |
| 9.2 |  | Notify the customer |  |
|  |  |  |  |
|  | **Legend:** |  |  |
|  | Context mapping Team (Pam, Joris) |  |  |
|  | Yaren |  |  |
|  | Dev Team (Maryam, Wouter [Maurice]) |  |  |
|  | Richard |  |  |
---
id: confluence:389742595
source: confluence
type: page
space: TC
title: PTO Steps to add a validated port to the process
author: Richard van Klaveren
date: '2024-07-15'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/389742595
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/389742595
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/405012483
---
# PTO Steps to add a validated port to the process

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/389742595  

## Content

The process as executed during the APMT project for the majority part of the globalisation phase had a lot of dependencies between different groups / people within the Teqplay team. Therefore, we try to identify ways to get this process as automated as possible and reducing the amount of single-person dependencies and handover points between different people. The original process is [documented here](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/405012483):

The improved process looks like:

With the following sub-steps (see [spreadsheet](https://docs.google.com/spreadsheets/d/1UserXpiJbc5E1wkb6S0G8AOZJZFpLqdnADQReZ-qZFk/edit?gid=116919477#gid=116919477)):

| **1** | **Add initial context information on the relevant port & terminal** | | |
| --- | --- | --- | --- |
| 1.1 |  | POMA: Check if the Berth / Terminal / Port information in EXTERNAL DB is adding relevant value to the Teqplay data, if is: | |
| 1.1.1 |  |  | Import the EXTERNAL DB data into the Teqplay layer in POMA |
| 1.1.2 |  |  | Remove the terminals and berths at open sea (if any) |
| 1.1.3 |  |  | Update all berths where needed (make sure cargoType is set to the relevant category for all berths) |
| 1.1.4 |  |  | Update all terminals where needed, and make sure the berths are linked to the relevant terminal |
| 1.2 |  | POMA: Lookup anchorages and pilot areas and add them to POMA | |
| 1.2.1 |  |  | Find anchorages in openSeaMap, any nautical Map, looking in vv where vessels layed still before entering the port, use onthemap, check IHS |
| 1.2.2 |  |  | Find pilot areas in openSeaMap, any Nautical map, any pilot vessel behavious, check IHS |
| 1.3 |  | POMA: Mark the port to use Teqplay data instead of EXTERNAL DB data | |
| 1.4 |  | CSI / Shipmapper: Identiy the vessels with a relevant role in the port (pilot, tugs, bunker, waste, water, boatman, ....) | |
| 1.5 |  | POMA: Make sure we know what terminal the customer is mapping to what terminal in Poma, and validate proper naming | |
| 1.6 |  | POMA: check via terminal website / Google maps / photo footage what part of the terminal is used for what (in case of general purpose terminal) and update berth and cargo category mapping | |
| 1.7 |  | POMA: Trigger a POMA merge | |
| 1.8 | \* | PTO: Add the focus and benchmark terminals in the PTO Tool (is this possible, or should it stay in PowerBI? | |
| 1.9 | \* | PTO: Update the terminal name based on APM / JOC | |
| **2** | **Generate validation data in DEV DWH & Datamart** | | |
| 2.1 |  | PTO: Update the POMA and CSI cache in PTO as applicable | |
| 2.2 |  | PTO: Run a dataset of at least a year per port involved and update the PowerBI validation environment | |
| 2.3 |  | PTO: Upload JOC & Weekly Operational Data sheet | |
| 2.4 |  | PTO: Update Datamart / refresh PowerBI data | |
| **3** | **Do an initial validation of the data in PTO context per port involved** | | |
| 3.1 |  | PowerBI: Validate the PowerBI dashboard on the following steps, and mark the ones that are ok, and the ones that need further validation: | |
| 3.1.1 |  |  | no TEU / Vessel category (make sure vessel category v2, length, width and DWT are properly set) |
| 3.1.2 |  |  | Unmatching anchor up/down or anchor up before anchor down. |
| 3.1.3 |  |  | Validate that top 10 shortest anchor durations are correct |
| 3.1.4 |  |  | Validate that top 10 longest anchor durations are correct |
| 3.1.5 |  |  | Validate that top 10 shortest berth durations are correct |
| 3.1.6 |  |  | Validate that top 10 longest berth durations are correct |
| 3.1.7 |  |  | Select 10 random ships and validate all timestamps to be properly measured |
| 3.1.8 |  |  | Validate Anchor times and pilot on board times of 10 large time differences between anchor-up and pilot inbound |
| 3.1.9 |  |  | Verify if any negative values are mentioned in durations |
| **4** | **Decision what issues needs fixes** | | |
| 4.1 |  | Validate the ones that are marked for further validation and generate results into Context mapping updates, CSI updates or bug reports | |
| **5** | **Fix bugs detected during the validation phase (step 3)** | | |
| 5.1 |  | Analyze | |
| 5.2 |  | Fix | |
| 5.3 |  | Deploy in dev | |
| 5.4 |  | Test in dev | |
| 5.5 |  | Deploy in live | |
| **6** | **Generate the target data into the PROD DWH and datamart** | | |
| 6.1 |  | POMA + CSI + PTO: Import contextual knowledge from DEV to LIVE environment | |
| 6.2 |  | PTO: Update the POMA and CSI cache in PTO as applicable | |
| 6.3 |  | PTO: Run the report from the UI | |
| 6.4 | \* | PTO: Upload JOC & Weekly Operational Data sheet | |
| 6.5 |  | PTO: Update Datamart / refresh PowerBI TEST data | |
| **7** | **Final Validation & Release to the customer** | | |
| 6.1 |  | Final validation of the TEST PowerBI Dashboard | |
| 6.2 |  | Update of the PROD PowerBI Dashboard | |
| 6.2 | \* | Share the GeoBoundingboxes with the customer to validate the context used is as expected | |
| 6.3 |  | Notify the customer | |
|  |  |  |  |
|  |  |  |  |
|  | Context mapping Team (Pam, Joris) | | |
|  | PTO Team | | |
|  | Technical product owner | | |
|  | \* | APMT specific | |
|  | Changes need to be applied | | |

Issues addressed in the improved process:

* Data context mapping team only enters data into the develop environment, removing the risk data in poma/csi impacts the live operations before validations
* Minimal single person responsibilities
* Minimize handover points to reduce dependencies and waiting times. Since amount of algorithm changes are expected to be minimal in the future, data context mapping team can execute almost the full validation.
* No contextual data is added at the end of the process (like terminal mappings based on customer data), all is focused at the start of the process.
* Get rid of the Excel spreadsheet dependencies and do the validation fully from PowerBI
* Process is still working per full port, so that a full port can be added to the ‘validated’ list.
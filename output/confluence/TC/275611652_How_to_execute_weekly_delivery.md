---
id: confluence:275611652
source: confluence
type: page
space: TC
title: How to execute weekly delivery
author: Yaren Aslan
date: '2024-07-12'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/275611652
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/275611652
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/212762671/Data+Mart#How-to-start-using-it
---
# How to execute weekly delivery

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/275611652  

## Content

# Timeline

Automated, Manual Step, Wait

* **Monday:**

1
complete
PTO reports run to generate visits in the last 2 weeks (at the moment only for USNYC, MAPTM and INNSA)

2
complete
Wait for report completion (est. 1 hour)

3
complete
~~Download JOC from the link (received by email from~~ [~~dataprocessing@joc.com~~](mailto:dataprocessing@joc.com) ~~via~~ [~~maersk.onmicrosoft.com~~](http://maersk.onmicrosoft.com)~~)~~ 

* ~~For the most recent version and the archive,~~ [~~JOC - Teqplay Ops - Google Drive~~](https://drive.google.com/drive/folders/1ULSdFLXA9u-JCI9l10zPKvyGoGkvDOHQ)

4
complete
~~Upload to~~ [~~PTO~~](https://pto.teqplay.nl/) ~~using JOC Update sheet upload button on Settings~~

5
complete
~~Wait for moves matching completion (est. 3-4 hours for 2 years of data)~~

* **Wednesday:**

6
incomplete
~~Download weekly operational data (received by email via alias:~~ [~~apmtplanning@teqplay.nl~~](mailto:apmtplanning@teqplay.nl)~~)~~

* ~~For the most recent version and the archive,~~ [~~Weekly Operational Data - Teqplay Ops - Google Drive~~](https://drive.google.com/drive/folders/1hmLbZA00CV3Jzy25erKqIb-pb9GTWHPc)

7
incomplete
~~Upload to~~ [~~PTO~~](https://pto.teqplay.nl/) ~~using WOD Update sheet upload button on Settings~~

8
incomplete
~~Wait for moves matching completion (est. 5-10 minutes)~~

9
incomplete
~~Trigger Datamart refresh~~

10
incomplete
~~Wait for Datamart refresh completion (est. 3 hours for all APM related ports)~~

* **Thursday/Friday**

11
incomplete
Go to [Semantic Model of APMT Dashboard on Test](https://app.powerbi.com/groups/115af9f0-d218-4aa0-9efd-186c3c807af7/datasets/05e85159-6e83-4570-961c-541dc3572d5f/details?experience=power-bi), click Refresh now

12
incomplete
Wait for completion (est. 5-10 minutes) (might need to refresh the page to see if refresh is completed)

13
incomplete
Use the monitoring dashboards to compare live data with test data 

* Both of these dashboards are located in Test Workspace, under the folder Monitoring Dashboards:

  + [Live- Monitoring Dashboard](https://app.powerbi.com/groups/115af9f0-d218-4aa0-9efd-186c3c807af7/reports/5ac566ce-a0b8-41e6-94f7-2f937158b0ad/ReportSection1177b369a936ed8be73a?experience=power-bi)
  + [Test- Monitoring Dashboard](https://app.powerbi.com/groups/115af9f0-d218-4aa0-9efd-186c3c807af7/reports/7be8160e-01fd-46db-83fb-b5d4a39d8d6f/ReportSection1177b369a936ed8be73a?experience=power-bi)
  + Optionally, use the Reset filters button to ensure they are in the initial state (no filters impacting)

14
incomplete
Take a look at the number of visits, PTT average, % fallbacks, % estimated

* % unknown should always be zero, moves should be estimated if they are not matched with JOC or WOD

15
incomplete
To proceed with weekly delivery, go to [Semantic Model of APMT Dashboard on Live](https://app.powerbi.com/groups/068140c4-e38a-4ae7-8a3e-322a7a3b46a9/datasets/08d93ea5-eb78-413a-a3f7-a689978b3349/details?experience=power-bi), click Refresh now

At the end of each month, we receive a new JOC file. When JOC is received or to be rerun:

16
incomplete
Download JOC from the link (received by email from [dataprocessing@joc.com](mailto:dataprocessing@joc.com) via [maersk.onmicrosoft.com](http://maersk.onmicrosoft.com))

* Upload to [JOC - Teqplay Ops - Google Drive](https://drive.google.com/drive/folders/1ULSdFLXA9u-JCI9l10zPKvyGoGkvDOHQ) for archive keeping

17
incomplete
Upload to [PTO](https://pto.teqplay.nl/) using JOC Update sheet upload button on Settings

18
incomplete
Wait for moves matching completion (est. 3-4 hours for 2 years of data)

19
incomplete
Trigger Datamart refresh

20
incomplete
Wait for Datamart refresh completion (est. 3 hours for all APM related ports)

# How to refresh data

There are two ways to refresh data in PBI:

## 1. PBI Service

(In case gateway and database connection is already configured)

1. Go to the semantic model that you wish to refresh
2. Click Refresh now

## 2. PBI Desktop (Old)

### Setting up

1. Download PBI Desktop ([official download link](https://powerbi.microsoft.com/en-us/downloads/))
2. Open the semantic model (.pbix file) of the dashboard. Semantic models published in Teqplay BI are kept in Teqplay Ops\3. Internal components\Teqplay BI
3. Follow the steps from <https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/212762671/Data+Mart#How-to-start-using-it> to connect the semantic model to data mart

### Refreshing data

Recommended flow includes the steps with *(test)* label.

1. ***(test)***pbix files keep the corresponding data. So, to make sure that the current state is not lost, copy the file and rename the copied version.
2. Open the original file
3. Make sure you are connected to VPN
4. Click refresh on the Home tab under Queries. Data refresh might take a few minutes.
5. ***(test)***Publish the report to [Test: Teqplay BI](https://app.powerbi.com/groups/115af9f0-d218-4aa0-9efd-186c3c807af7/list?experience=power-bi) workspace

   1. Click Publish on the Home tab under Share.
   2. You might be asked to save your changes. Click save.
   3. Select Test: Teqplay BI workspace
   4. Dashboard becomes available in [Test: Teqplay BI](https://app.powerbi.com/groups/115af9f0-d218-4aa0-9efd-186c3c807af7/list?experience=power-bi) workspace
6. ***(test)*** Compare the values with the most recent publication in [Teqplay BI](https://app.powerbi.com/groups/068140c4-e38a-4ae7-8a3e-322a7a3b46a9/list?experience=power-bi) workspace
7. ***(test)***When you are confident with the dashboard, go back to the semantic model (.pbix file)
8. Publish the report [Teqplay BI](https://app.powerbi.com/groups/068140c4-e38a-4ae7-8a3e-322a7a3b46a9/list?experience=power-bi) workspace. (See the items a, b, c, d of Step 5)
9. ***(test)*** Delete or archive the copied version from Step 1.
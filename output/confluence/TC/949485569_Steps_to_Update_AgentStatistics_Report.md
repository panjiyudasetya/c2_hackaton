---
id: confluence:949485569
source: confluence
type: page
space: TC
title: Steps to Update AgentStatistics Report
author: astri
date: '2026-02-12'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/949485569
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/949485569
---
# Steps to Update AgentStatistics Report

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/949485569  

## Content

\*\*This document was originally created by Richard ([Steps to update AgentStatistics - Google Docs](https://docs.google.com/document/d/1HoODOJxzcwUgBQWPvNza_YV9kHB21rsVunh_uvdbLaE/edit?tab=t.0)). Add to confluence after adding the details.

## How to Update AgentStatistics Report

AgentStatistic report has to be updated and sent on the 1st day of the month or the 1st working day of the month. Below is how to update the excel reports:

### 1. Collect new data from [PortReporter](https://portreporter.teqplay.nl/)

Use a REST client to get the new Excel spreadsheet mailed to you: ‘<https://backendportreporter.teqplay.nl/v2/portcalls/requestAgentReport?ports=NLAMS&ports=NLRTM&ports=BEANR&ports=BEGNE&ports=NLVLI&ports=NLTNZ&from=2025-08-01T00:00:00.000Z&to=2025-09-01T00:00:00.000Z>’ to collect all data for e.g. October 2025 for all ports and store as a  file in the drive.

For this, you will need to go to the calls made by PortReporter, select one call and copy the ‘Authorization’ header value, and pass it as a Authorization header value in PostMan / your REST HTTP Client.

Set the "from & to" parameters, for example, for the October 2025 report:

Click send and wait for the Excel spreadsheet emailed by the port reporter:

### 2. Use the [Overview Agencies](https://docs.google.com/spreadsheets/d/1FPXYyG33oIKVpj72DjkauULr0VWcP2JKIuhUkkFGgRg/edit?gid=1305269643#gid=1305269643) sheet or below screenshot to see which report should get what data

In total, we have four Excel reports (1 for each agency).

***\*\*Update: since Feb 2026 we no longer provide S5 report***

### 3. Create a new folder, e.g. 2025\_11\_01 for the reports of October 2025. Then do per report in [the Google Drive](https://drive.google.com/drive/u/0/folders/1bbtc2m3SK2la-wrle5N2FT7tRj3Yqim2):

* Make a copy
* Remove the oldest 1-month of data
* Filter the ports in the original dataset (data from portreporter) based on “Overview Agencies” table above
* Append the 1-month of filtered data from the portreporter spreadsheet to the “Main portcall data” sheet in each Excel report
* Refresh and verify that the graphs for **Wilhelmsen display data from Jan 2024** and **S5, Oudkerk, and Jordex reports display 12 months of data**

### 4. Final check & file naming

The folder will contain 5 files, for example:

*\*\*the last file is basically the report sent by PortReporter by email, we only need to rename it.*
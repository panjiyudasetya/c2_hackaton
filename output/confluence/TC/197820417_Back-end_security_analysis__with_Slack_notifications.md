---
id: confluence:197820417
source: confluence
type: page
space: TC
title: Back-end security analysis (with Slack notifications)
author: Leon Joosse (Unlicensed)
date: '2023-07-17'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/197820417
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/197820417
---
# Back-end security analysis (with Slack notifications)

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/197820417  

## Content

The [backend-security-analysis](https://bitbucket.org/teqplay/backend-security-analysis) project scans all Teqplay back-end projects for vulnerabilities in its dependencies. The script outputs a report with a list of vulnerabilities per project. The report also shows any increase or decrease in vulnerabilities.

In 2023, the project is extended to monitor amount of unresolved vulnerabilities, along with a notification in the projects Slack channel, to remind the developer there’s unresolved vulnerabilities.

This document outlines how the 2023 extension integrates with a Google Sheet per project (via Google Cloud auth) and Slack.

16falselistfalse

## Flow

1. The analysis runs
2. Per project:

   1. The existing list of vulnerabilities is retrieved from the Google Sheet
   2. The new list of analyzed vulnerabilities is compared to the existing list
   3. If any new or unresolved vulnerabilities, send a Slack notification

## How to add a new back-end project

1. Add project to analysis script
2. Create and/or configure a Google Sheet
3. Configure to notify a Slack channel

### Add to analysis script

In <https://bitbucket.org/teqplay/backend-security-analysis/src/master/src/sources.ts>, add an entry for your project:

json {
name: "VesselVoyage",
branch: "master",
repository: "vesselvoyage-backend",
buildFile: "build.gradle"
}

Some projects have multiple Gradle modules, see the sources.ts file for an example.

### Create Google Sheet

1) Create the Google Sheet, preferably in a folder dedicated to that project. Looking at Chorus for an example, the sheet it stored in Teqplay Ops → Products → Bunkerplanner → Chorus.

2) Add a sheet named `back-end`. This is where the analysis script will read/write vulnerabilities. Add the following headers (and a filter for convenience):

3) Add another sheet named `constants`. Add the following values:

4) Optional, but recommended:

In the `back-end` sheet, configure the data validation for the ‘Triage’ column, to show a dropdown from the Classification values.

The script assumes an empty ‘Triage’ cell as an unresolved vulnerability and a non-empty cell as resolved.

5) Add [sec-vuln-detectinator@prismatic-rock-377209.iam.gserviceaccount.com](mailto:sec-vuln-detectinator@prismatic-rock-377209.iam.gserviceaccount.com) as **Editor**

6) Copy the sheet id from the URL, we need it in the next step

### Configure the Slack notifier

You need access to the **Security Vulnerability Notifier** Slack app in Teqplay workspace to add this.

Contact LeonJ or Michel to add you as a collaborator, so you can add webhooks.

Create a Slack webhook:

1. Go to <https://api.slack.com/apps/A04SXF34Y3U/incoming-webhooks>
2. Use ‘Add New Webhook to Workspace’ button at the page bottom
3. Choose the channel of your project (this is the default channel, and the script will post to this channel)
4. Copy the webhook URL and use it in the next bit

In <https://bitbucket.org/teqplay/backend-security-analysis/src/master/slack/projects.json>, add an entry for your project:

 {
"name": "VesselVoyage",
"sheet": "1SE2lWqLbEtNDbf6oOm90Lmo8QP5xi0....",
"webhook": "https://hooks.slack.com/services/T08PPBR1B/B04....."
}

The `name` property in `sources.ts` and `projects.json` must be equal!

The Slack notifier reads the vulnerabilities from a file with that name.

Use the sheet id from the URL

### And now we wait

Now wait until the next run is done on Monday morning

It is recommended to not run the analysis on your own, this would screw up the stats for the report in #backend channel.

## Technicalities

### Google Cloud Service Account (to access Sheets)

The analysis script needs to read and write data from/to the Google Sheet. A Google Cloud ‘Service Account’ (SA) is created to facilitate this. This SA is added as ‘Editor’ to the Google Sheet.

The project is filed under ‘Teqplay’ and is named [Security vulnerabilities](https://console.cloud.google.com/welcome?project=prismatic-rock-377209). The Google Cloud shorthand is ‘prismatic-rock-377209’. The project is owned by LeonJ and Michel. The project is only accessible through your @teqplay.nl/com account, ask LeonJ or Michel to get access (or through a Teqplay admin that can override).

The project has a Service Account (SA), see IAM & Admin → Service Accounts. The SA has an email address to add it to the Google Sheet: [sec-vuln-detectinator@prismatic-rock-377209.iam.gserviceaccount.com](mailto:sec-vuln-detectinator@prismatic-rock-377209.iam.gserviceaccount.com).

IAM & Admin → Service accounts list

The analysis project needs a key of the service account to use the Google Sheets API. The keys are located in IAM & Admin → Service Accounts → account details → Keys.

A key is not simply a String, it is a JSON file with a key inside, along with other API information. Make sure to place the JSON file in the analysis project!
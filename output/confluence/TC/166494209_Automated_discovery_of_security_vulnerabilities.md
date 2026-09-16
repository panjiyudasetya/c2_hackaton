---
id: confluence:166494209
source: confluence
type: page
space: TC
title: Automated discovery of security vulnerabilities
author: Leon Joosse (Unlicensed)
date: '2023-02-09'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/166494209
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/166494209
---
# Automated discovery of security vulnerabilities

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/166494209  

## Content

As a back-end developer, I want to be **notified of newly discovered security vulnerabilities in my project**, so we can patch these vulnerabilities in a timely manner, keeping the application safe.

# Functional explanation

A script discovers new CVEs in the dependencies of the project. The CVE list is kept in a Google Sheet, where the developer can classify each CVE: *not affected* or *resolved*. Any unclassified CVE is reported the next time the tool runs. There is no ‘fix on the way’ status on purpose. That prevents a CVE from ending in limbo as a developer may forget about completing the fix. Once a CVE is classified, it stays in the sheet.

Example sheet. CVE 01 is classified, CVE 02 is not

An empty **Classification** cell means unclassified, any value means classified.

## Process

1. The `backend-security-analysis` tool analyses the back-end project for known security vulnerabilities in its dependencies.
2. The resulting JSON document is uploaded to an S3 bucket. It contains per project a list of:

   1. CVE number
   2. Dependency name and version
   3. CVSS score
3. A lambda runs to process the uploaded list of CVEs per project:

   1. The current list of CVEs is retrieved from the project’s Google Sheet and compared to the new list
   2. New CVEs are added to the list
   3. Unclassified CVE entries in the sheet are reported to the slack channel of the project.

# Technical notes

## Analysis script on CircleCI

## Auth for Google Sheet

The lambda accesses the project vulnerability sheets. Google requires a ‘service account’ to access a sheet. This account needs a Google Cloud project in our workspace.

The existing project is here: <https://console.cloud.google.com/home/dashboard?project=prismatic-rock-377209>

In case we need to create a new project:

1. Go to [https://console.cloud.google.com/](https://console.cloud.google.com/welcome)
2. Create the project

   1. Open the project selector menu and hit ‘New Project’.
   2. Fill in the details and create
3. Enable access to Google Sheets API

   1. Go to APIs & Services
   2. Enable the Google Sheets API
4. Create a service account for authentication

   1. On the APIs & Services page, go to the ‘Credentials’ tab.
   2. Create a new service account.
   3. The account gets its own email address in the project.
   4. You will be the ‘owner’ of the service account. It is wise to assign other people as owner, so access does not get lost: Go to IAM & Admin → Service Accounts → your account → Permissions. Add other existing Teqplay users with role ‘Owner’
5. Add a key, so the script can authenticate

   1. Go to IAM & Admin → Service Accounts → your account → Keys
   2. Hit Add key, use the JSON format. The key is downloaded to your machine in JSON or P12 format
   3. The key is of course only generated one time, and not retrievable afterwards.
   4. Upload the key to the scripts location (see elsewhere in the docs for the exact place/folder)
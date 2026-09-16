---
id: confluence:628523009
source: confluence
type: page
space: TC
title: How to Set Up a Data Gateway for Power BI on an AWS EC2 Machine with ODBC Connection
author: Maryam Tavakoli (Unlicensed)
date: '2025-02-13'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/628523009
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/628523009
---
# How to Set Up a Data Gateway for Power BI on an AWS EC2 Machine with ODBC Connection

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/628523009  

## Content

## Prerequisites

* An AWS EC2 instance (Windows Server recommended)
* Power BI service account with admin rights
* ODBC driver for your data source installed on the EC2 instance
* Necessary credentials for the data source
* RDP access to the EC2 instance

## Step 1: Launch and Configure the EC2 Instance

1. Log in to AWS Management Console.
2. Navigate to EC2 and launch a new instance.
3. Choose a Windows Server AMI (Amazon Machine Image).
4. Select an instance type (t3.medium or larger recommended).
5. Configure security groups
6. Launch the instance and connect via Remote Desktop.

## Step 2: Install Power BI Data Gateway

1. Open a web browser on the EC2 instance and download the Power BI Data Gateway installer from [Microsoft](https://www.microsoft.com/en-us/download/details.aspx?id=53127).
2. Run the installer and follow the setup wizard:

   * Choose "On-premises data gateway (recommended)."
   * Accept terms and conditions.
   * Complete the installation.
3. Sign in with your Power BI account.
4. Name your gateway and provide a recovery key (save this securely).
5. Finish the setup and verify the gateway appears in Power BI Service (<https://app.powerbi.com> ).

## Step 3: Install and Configure ODBC Driver

1. Download the PostgreSQL ODBC driver.
2. Open "ODBC Data Source Administrator" on Windows.
3. Add a new System DSN:

   * Select the installed driver.
   * Configure the connection settings (server, database, credentials, etc.).
   * Test the connection to ensure it works.

## Step 4: Configure the Data Gateway in Power BI

1. Open Power BI Service (<https://app.powerbi.com> ).
2. Go to "Settings" > "Manage Connections and Gateways" > ”on-premises data gateways”
3. Select the newly installed gateway.
4. make sure on the status column is online

## See also:

How to Set Up Power BI Gateway   
How to publish a new report and connect it to datasource with gateway
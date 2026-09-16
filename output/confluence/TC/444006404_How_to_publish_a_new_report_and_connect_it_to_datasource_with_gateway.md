---
id: confluence:444006404
source: confluence
type: page
space: TC
title: How to publish a new report and connect it to datasource with gateway
author: Yaren Aslan
date: '2025-04-17'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/444006404
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/444006404
---
# How to publish a new report and connect it to datasource with gateway

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/444006404  

## Content

*Make sure to have the Power BI Desktop app installed. Follow the steps from* [*Get Power BI Desktop - Power BI | Microsoft Learn*](https://learn.microsoft.com/en-us/power-bi/fundamentals/desktop-get-the-desktop) *to download and launch the app.*

*Teqplay’s Power BI files (pbix) are kept in our shared drive, on G:\Shared drives\Teqplay Ops\3. Internal components\Teqplay BI. Power BI Service can also be used to download the underlying Power BI file (pbix) of a specific dashboard. Click on the Semantic model, and Download this file.*

|  |  |
| --- | --- |
|  |  |

1. Open the pbix file that you wish to publish. This will launch Power BI Desktop

2. Click Publish

*Note: You will need to sign in to your Microsoft account to publish.*

|  |  |
| --- | --- |
|  |  |

3. Select the workspace you want to publish to, and wait (it might take a few minutes)

*Note: If there is already a semantic model published on the selected workspace, you will encounter a popup to confirm replacing.*

4. Click Open data settings to go to Power BI Service to connect with gateway. Alternatively, clicking the Refresh button on the Semantic Model would take you to the same page.

5. Find Gateway and cloud connections. Select the right connection and click Apply.

   1. (Note that if this connection has not been established before, you might need to create it first. Follow the suggestion in the screen to Add a connection in that case.)

6. You can now Refresh or Schedule refresh with this semantic model

See also How to Set Up Power BI Gateway and How to Set Up a Data Gateway for Power BI on an AWS EC2 Machine with ODBC Connection.
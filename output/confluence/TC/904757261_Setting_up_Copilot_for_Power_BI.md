---
id: confluence:904757261
source: confluence
type: page
space: TC
title: Setting up Copilot for Power BI
author: Yaren Aslan
date: '2025-10-08'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/904757261
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/904757261
---
# Setting up Copilot for Power BI

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/904757261  

## Content

Follow the steps from the walkthrough video: [Create your first Microsoft Fabric Capacity](https://www.youtube.com/watch?v=YnAMpCoK-TQ)

# Step 1: Start Azure subscription

[Create Your Azure Free Account Or Pay As You Go | Microsoft Azure](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account?icid=portal)

# Step 2: Create a Resource Group

[Resource Manager - Microsoft Azure](https://portal.azure.com/?l=en.en-us#view/HubsExtension/ServiceMenuBlade/~/resourcegroups/extension/Microsoft_Azure_Resources/menuId/ResourceManager/itemId/resourcegroups)

# Step 3: Create Fabric Capacity in the Resource group

Go to the Resource group you have created in Step 2. Click on the name, and click Create new resource.

This will take you to the Marketplace. Find and select Microsoft Fabric.

Proceed with creating the Microsoft Fabric capacity.

You will be required to select the Region and Size. For Size, if you do not have any other hard requirement, F2 will suffice for making Copilot available in Power BI (<https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction#:~:text=You%20need%20to%20have%20an%20F2%20capacity%20or%20above%20to%20be%20able%20to%20use%20Copilot.>).

Fabric capacity is now available on [teqplayfabriccapacity - Microsoft Azure](https://portal.azure.com/?l=en.en-us#@teqplaybv.onmicrosoft.com/resource/subscriptions/381e6eac-90d3-4197-a2a9-646e6397442f/resourceGroups/ResourceGroup/providers/Microsoft.Fabric/capacities/teqplayfabriccapacity/overview):

# Step 4: Give users access to capacity

Observe that Fabric capacity is available in [Fabric](https://app.fabric.microsoft.com/admin-portal/capacities/capacitiesList/dc?language=en-US&experience=fabric-developer).

Click on the capacity name to manage settings. Make sure that the users that require Copilot have access to Copilot capacity, and have Contributor permissions. You can also setup notifications to be alerted when usage exceeds certain thresholds (for instance, 50%).

# Step 5: Enjoy Copilot in Power BI!

# Note

Remember to pause capacity from [teqplayfabriccapacity](https://portal.azure.com/?l=en.en-us#@teqplaybv.onmicrosoft.com/resource/subscriptions/381e6eac-90d3-4197-a2a9-646e6397442f/resourceGroups/ResourceGroup/providers/Microsoft.Fabric/capacities/teqplayfabriccapacity/overview) when it is not used.
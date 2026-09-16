---
id: confluence:725745665
source: confluence
type: page
space: TC
title: How to share a dashboard with customer
author: Yaren Aslan
date: '2025-10-02'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/725745665
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/725745665
---
# How to share a dashboard with customer

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/725745665  

## Content

Following four steps needs to be followed to onboard a new customer.

1. **Identify and invite users on** [**Microsoft Entra admin center**](https://entra.microsoft.com/#view/Microsoft_AAD_UsersAndTenants/UserManagementMenuBlade/~/AllUsers/menuId/)

This process requires close collaboration with the customer to identify relevant users. Once the list is determined, bulk Invite can be used with the CSV template available in admin center. See External user management in Microsoft Entra ID for more details.

2. **Create and assign groups on** [**Microsoft Entra admin center**](https://entra.microsoft.com/#view/Microsoft_AAD_IAM/GroupsManagementMenuBlade/~/Overview/menuId/Overview) **for new members**

For every customer organization, a new Security group should be created. This Security group can later be used for managing access to Power BI reports and dashboards. Bulk group import can be used, using the CSV template available in admin center. Ensure that the list used for this step is identical to the one used for inviting users. See External user management in Microsoft Entra ID for more details.

3. **Update** [**Power BI**](https://app.powerbi.com/groups/068140c4-e38a-4ae7-8a3e-322a7a3b46a9/list?experience=power-bi) **app to give the group access to their report**

[Apps in Power BI](https://learn.microsoft.com/en-us/power-bi/consumer/end-user-apps) enable organized distribution of the content to a broad audience. Apps are collection of dashboards and reports that can be distributed it to the entire community, to organization, or to specific people or groups.

Every workspace can have one app. Once your report is published in the workspace, you can Update the app to include this new content.

In Setup tab, you can change the name and description of the app, logo and color, contact information, and some other settings. You can also Copy the app link.

Content tab is where the reports shared with customers should be added within the scope of the app.

Use Add content button to select relevant reports, dashboard, or links.

Audience tab is where the match between content and audience takes place. For every new customer, you should create a New Audience. On the left side, using the eye icon, view or hide the reports based on the audience. On the right side, add the Security group you had defined in step 2.

Once the changes are finalized, Update the app.

4. **Share the link with the customer**

Once the update is finished, you can copy the link and share it with the customer.

The customer will see a screen as follows, where the content made available for them is on the left side.

You can consider sharing a dashboard guide as the following:

Notes:

* Keep in mind that this flow is for dashboards without roles. In case roles are defined for the dashboard, you need to assign roles.
* About steps 1 and 2, refer to <https://teqplaybv.atlassian.net/wiki/x/AoD7Kg> for responsibilities.
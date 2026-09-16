---
id: confluence:721125378
source: confluence
type: page
space: TC
title: External user management in Microsoft Entra ID
author: Yaren Aslan
date: '2025-05-02'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/721125378
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/721125378
---
# External user management in Microsoft Entra ID

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/721125378  

## Content

Microsoft Entra ID is Microsoft's identity and access management solution. External guest users need to be invited in Microsoft Entra ID to enable sharing of Power BI reports and dashboards. We defined the following roles and processes for external user management.

## Roles

| **Role** | **Description & Responsibilities** |
| --- | --- |
| Functional owner  () | * Identifies and invites users on [Microsoft Entra admin center](https://entra.microsoft.com/#view/Microsoft_AAD_UsersAndTenants/UserManagementMenuBlade/~/AllUsers/menuId/) (can use Bulk Invite) * Creates and assigns groups on [Microsoft Entra admin center](https://entra.microsoft.com/#view/Microsoft_AAD_IAM/GroupsManagementMenuBlade/~/Overview/menuId/Overview) for new members (can use Bulk Group Import) * Deletes external users and groups for which contracts are expired (can use Bulk Delete) * If needed, buys and allocates Power BI licences in communication with management |
| SecOps owner  ( ) | * Regularly (once a quarter) executes a check-up and determines if everything is in order |
| Facilitator  ( ) | * Facilitates to improve processes when needed |

## Processes

1. ***(Functional owner)*** **Identifying and inviting users on** [**Microsoft Entra admin center**](https://entra.microsoft.com/#view/Microsoft_AAD_UsersAndTenants/UserManagementMenuBlade/~/AllUsers/menuId/)

This process requires close collaboration with the customer to identify relevant users. Once the list is determined, bulk Invite can be used with the CSV template available in admin center.

2. ***(Functional owner)*** **Creating and assigning groups on** [**Microsoft Entra admin center**](https://entra.microsoft.com/#view/Microsoft_AAD_IAM/GroupsManagementMenuBlade/~/Overview/menuId/Overview) **for new members**

For every customer organization, a new Security group should be created. This Security group can later be used for managing access to Power BI reports and dashboards. Bulk group import can be used, using the CSV template available in admin center. Ensure that the list used for this step is identical to the one used for inviting users.

3. ***(Functional owner)*** **Deleting external users and groups for which contracts are expired**

Bulk Delete can be used, using the CSV template available in admin center. Note that you must have at least the User Administrator role assignment to delete users in your organization.

4. ***(Functional owner)*** **Buying and assigning Power BI licences**

Users need Power BI Pro licenses to access Power BI reports and dashboards. If the customers need Power BI Pro licenses assigned, Functional owner should ensure that Teqplay buys and assigns the licenses.

5. ***(SecOps owner)*** **Executing a regular check-up and determining if everything is in order**

Regular checks will be done by the SecOps owner to ensure that all the users and groups are relevant.

6. ***(Facilitator)*** **Facilitating to improve processes when needed**

If the process requires too many manual steps or is unclear, Functional owner or SecOps owner might get in contact with the Facilitator to rethink the plan.

## Other decisions

* Deleting users and revoking their licenses for leaving employees becomes part of the offboarding process.
* Licence purchase decisions should be made in communication with management team. A channel in Slack will be created as the initial form of communication.
* to be updated: We will investigate how to check whether contracts are expired. For now, Functional owner will schedule a time to check once a quarter, and will collect the information per customer.
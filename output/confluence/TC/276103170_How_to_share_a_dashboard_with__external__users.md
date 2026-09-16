---
id: confluence:276103170
source: confluence
type: page
space: TC
title: How to share a dashboard with (external) users
author: Yaren Aslan
date: '2024-12-12'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/276103170
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/276103170
---
# How to share a dashboard with (external) users

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/276103170  

## Content

Make sure that the users to be granted access are within the organization. See How to add an external user in the organization for external users.

There are two ways to provide access to an (external) user:

## a. Access to workspace

In PBI Service, dashboards are published in workspaces. These are essentially folders that keep the semantic models and corresponding reports. New workspaces can be added upon requirements.

There are two main workspaces maintained: [Teqplay BI](https://app.powerbi.com/groups/068140c4-e38a-4ae7-8a3e-322a7a3b46a9/list?experience=power-bi) and [Test: Teqplay BI](https://app.powerbi.com/groups/115af9f0-d218-4aa0-9efd-186c3c807af7/list?experience=power-bi). [Teqplay BI](https://app.powerbi.com/groups/068140c4-e38a-4ae7-8a3e-322a7a3b46a9/list?experience=power-bi) holds the dashboards that are shared/ready to be shared externally, whereas [Test: Teqplay BI](https://app.powerbi.com/groups/115af9f0-d218-4aa0-9efd-186c3c807af7/list?experience=power-bi) serves internal testing purposes. New people or groups can be added in workspaces. The advantage/disadvantage of this approach is that members of the workspace have access to all the dashboards shared in the workspace. In case Row Level Security is in place for a dashboard, members of the workspace are automatically granted admin access.

## b. Access to a specific dashboard

Alternatively, you can provide access to a specific dashboard.

First, you need to decide whether you wish user to receive an automated notification from Microsoft.

**To avoid automated notification from Microsoft**

1. Go to the dashboard you wish to share.
2. Click Share button on the upper ribbon.
3. Click … (More Options), and then Manage permissions

4. Click … (Manage permissions)

5. Enter name or email address that you want to add, click Save

Note that with that approach, user does not get notified. Share the link with them the way preferred.

**To let Microsoft send an automated notification**

1. Go to the dashboard you wish to share.
2. Click Share button on the upper ribbon.
3. Click “People in your organization with the link can view and share“ to see other sharing options.
4. Click “Specific people“ and Apply.
5. Enter a name or email address, add an message optionally.
6. Click send

***What does the user receive?***

Without an optional message:

With an optional message:

## For b, do not forget to assign roles if needed!

If the dashboard has Row Level Security (RLS), take the following steps to prevent the following error:

1. Go to the workspace where the dashboard is hosted. For corresponding semantic model of the dashboard, click “More options“ button (•••).
2. Click “Security“.
3. Add users in the role that they belong to

## Dashboard access guide

When sharing the link with the external user, guide below can be a useful attachment. It walks the user through the steps from receiving the link to getting started with the dashboard. In case of “Permission required” error, it advises a Refresh.
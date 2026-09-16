---
id: confluence:443547683
source: confluence
type: page
space: TC
title: How to start displaying a new field in the dashboard?
author: Yaren Aslan
date: '2024-08-23'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/443547683
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/443547683
---
# How to start displaying a new field in the dashboard?

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/443547683  

## Content

A quick way to start displaying a new field in the dashboard is to edit predefined list of parameters. Currently, it can be used for

* Fields on Berth Visit table: Berth Visit Level KPIs (displayed on Visit Details page in a table),
* Fields on Terminal Visit table: General Port Visit Information and Durations (displayed in tables on every page of the dashboard)

1. Go to the semantic model, click Open data model

2. Select the list of parameters you wish to edit

A list of parameters hold the display name of the field (`"PMPH"`), reference to the field in datamodel (`NAMEOF('Berth Visit'[PMPH of Berth Visit (moves/hr)])`), order of the field when this list is used (`9`)

*Observe that variables defined in Berth Visit Level KPI are being used in the table on Visit Details page in the dashboard:*

3. Edit the list of parameters to include the new fields you wanted to add

*Observe that variables defined in Berth Visit Level KPI are being used in the table on Visit Details page in the dashboard:*
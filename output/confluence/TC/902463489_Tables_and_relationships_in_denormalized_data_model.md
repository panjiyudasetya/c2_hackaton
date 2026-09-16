---
id: confluence:902463489
source: confluence
type: page
space: TC
title: Tables and relationships in denormalized data model
author: Yaren Aslan
date: '2025-10-07'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/902463489
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/902463489
---
# Tables and relationships in denormalized data model

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/902463489  

## Content

# Star Schema for Berth Visit Table

Theoretically, this is a snowflake and not star schema, given that there are multiple layers of dimension tables due to Berth-Port table separation. This structure is kept to ensure that filters on the Port level impact all the fact tables.

Berth visit table is also filtered by a number of calculated tables following the convention Bins (<selected> duration)

# Star Schema for Ship to Ship Table

Ship to Ship table also gets filtered by a number of dimension tables, which are overlapping with those that filter the Berth Visit table.

Good to note is that Ship to Ship table also has an inactive relationship with the Berth Visit table, which is invoked for some measures such as `STS found for Visit`, `Number of Ship to Ship Transfers`.

# Star Schema for Other Tables

1-many relationships with dimension tables are also maintained for other fact tables, namely: Anchorage Activities, Pilot Activities, Bunkering Activities and Towage Activities.
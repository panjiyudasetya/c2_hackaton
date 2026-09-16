---
id: confluence:899612674
source: confluence
type: page
space: TC
title: Steps of denormalizing
author: Yaren Aslan
date: '2025-10-06'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/899612674
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/899612674
---
# Steps of denormalizing

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/899612674  

## Content

# Berth Visit table

Berth Visit table is taken as the basis granularity for denormalizing.

## **1) Merged Queries terminal\_visit**

Left Join (all from Berth Visit table, only matching from Terminal Visit table)

* What it means: Berth Visit table is extended with Terminal Visit data. Berth visits are kept regardless of whether a corresponding Terminal Visit is found or not (Terminal Visit related fields remain empty if not). Terminal Visits are discarded if a corresponding Berth Visit is not found.

> = Table.NestedJoin(<previous step>, {"terminal\_visit\_id"}, fact\_terminal\_visit, {"terminal\_visit\_id"}, "fact\_terminal\_visit", JoinKind.LeftOuter)

## **2) Merged Queries port\_visit**

Outer Join (all from Berth Visit and Port Visit tables)

* What it means: Berth Visit table is extended with Port Visit data. Berth visits are kept regardless of whether a corresponding Port Visit is found or not (Port Visit related fields remain empty if not). Additionally, rows are added for Port Visits without Berth Visits. Berth Visit and Terminal Visit remain empty for these new rows.

> = Table.NestedJoin(<previous step>, {"visit\_id"}, fact\_port\_visit, {"visit\_id"}, "fact\_port\_visit", JoinKind.FullOuter)

# Berth table

## **Merged Queries terminal**

Left Join (all from Berth table, only matching from Terminal table)

* What it means: Berth table is extended with Terminal data. Berths are kept regardless of whether a corresponding Terminal is found or not (Terminal related fields remain empty if not). Terminals are discarded if a corresponding Berth is not found.

> = Table.NestedJoin(<previous step>, {"Terminal ID"}, Terminal, {"id"}, "Terminal", JoinKind.LeftOuter)
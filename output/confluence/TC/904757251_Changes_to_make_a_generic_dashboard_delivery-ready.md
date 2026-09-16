---
id: confluence:904757251
source: confluence
type: page
space: TC
title: Changes to make a generic dashboard delivery-ready
author: Yaren Aslan
date: '2025-11-19'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/904757251
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/904757251
---
# Changes to make a generic dashboard delivery-ready

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/904757251  

## Content

# Changes on the interface

1. Remove port slicer
2. Change background with the logo of the customer (if needed)

# Changes on the data

On Power Query editor, change the following parameters (values for POCCA are given as an example):

## Database connection

connection\_string760

dsn=NewMARTProd

database760

NEW-ETL-MART

## Data

selected\_port (this should be " " when all data is to be imported)760

USCRP

berths\_filtered (to make sure that the list of barge only berths are filtered out)760

TRUE

waitingCutoff (the threshold above which a vessel is considered "waited")760

4

vesselvoyage\_link760

[https://vesselvoyage.teqplay.nl/](https://vesselvoyagedata.teqplay.nl/)

## Time conversion

WinterTimeUTCDiff760

-05:00:00

SummerTimeUTCDiff760

-06:00:00

WinterTimeStartWeek760

45

SummerTimeStartWeek760

11

TimeOfDayForTimeSwitch760

08:00:00

You can use <https://time.is/> for determining these values.
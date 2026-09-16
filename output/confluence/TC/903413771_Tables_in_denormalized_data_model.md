---
id: confluence:903413771
source: confluence
type: page
space: TC
title: Tables in denormalized data model
author: Yaren Aslan
date: '2025-10-07'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/903413771
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/903413771
---
# Tables in denormalized data model

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/903413771  

## Content

# Tables imported from Datamart

## Fact tables

Berth Visit760

Major changes in Power Query:

* expanded to hold data from fact\_terminal\_visit and fact\_port\_visit tables (see Steps of denormalizing for more details),
* added columns for bins
* converted datetimes, added separated date and time fields after conversion
Anchorage Activities760

Limited changes in Power Query: converted datetimes

Ship to Ship760

Limited changes in Power Query: converted datetimes

Many new calculated columns are added in DAX to meet customer requirements with limited development.

Pilot Activities760

Limited changes in Power Query: converted datetimes

Bunkering Activities760

Limited changes in Power Query: converted datetimes

Towage Activities760

Limited changes in Power Query: converted datetimes

## Dimension tables

Berth760

Significant changes in Power Query: joined with Terminal table, filtered on barge only, values made more user-friendly

Port760

Limited changes in Power Query: Formatted text (added spaces, capitalized etc.)

Previous Port760

Copy of Port table

Ship760

Limited changes in Power Query: Formatted text (added spaces, capitalized etc.)

Service Vessel760

Copy of Ship table

Date760

Limited changes in Power Query: Added custom user-friendly columns (quarter, weekday, …)

Time760

Limited changes in Power Query: Added custom user-friendly column Time String

In addition to the tables we import from datamart (these could be tables imported without transformation, or tables that are transformed such as denormalizing), there are some entities that we see under the Data tab.

These are Tables calculated in Power Query (**green**), Tables calculated in DAX (**red**). Field parameters (**blue**) or Calculation groups (**orange**). Some examples:

# Tables calculated in Power Query

* Bins (Berth stay duration)
* Bins (Moored duration)
* Bins (Shifting)
* Bins (Steaming in)
* Bins (Steaming out)
* Bins (Waiting before arrival duration)
* Bins (Waiting duration)
* Bins (Waiting during visit duration)
* Weather

# Tables calculated in DAX

* Assumptions
* Contact Details
* Dry Bulk Category Classifications
* Liquid Bulk Category Classifications
* Weather code

# Field parameters

> *Fields parameters is a feature that allows users to choose which column to use to slice and dice values in a Power BI visual. By creating a fields parameter you can very easily build a report where the user can slice by Brand and Category, as in the following figure.*
>
> [*Fields parameters in Power BI - SQLBI*](https://www.sqlbi.com/articles/fields-parameters-in-power-bi/)

* Category
* Category for STS
* Category for visits with STS
* Duration Selected for Page
* Durations
* General Port Visit Information
* Histograms
* KPI
* Over Time

# Calculation groups

> *Calculation groups can significantly reduce the number of redundant measures you have to create, by allowing you define DAX expressions as calculation items that apply to the existing measures in your model.*
>
> [*Create calculation groups in Power BI - Power BI | Microsoft Learn*](https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups)

Note that calculation groups can be created and edited on Tabular Editor, an [free external tool](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-external-tools#:~:text=Business%20Ops.-,Tabular%20Editor,-Model%20creators%20can) for more advanced development and management of tabular models.

## Calculation group: Formatting Calculation

Calculation group that holds the different formatting types. At the moment, it has only one item: time, which formats numeric values as h:mm with the following calculation:

wide760VAR DecimalValue =
SELECTEDMEASURE ()
VAR HrValue =
INT ( DecimalValue )
VAR MinValue =
ROUND ( ( DecimalValue - HrValue ) \* 60, 0 )
RETURN
IF (
ISBLANK ( DecimalValue ),
"",
IF ( HrValue > 0, HrValue & "h", "" )
& IF ( MinValue > 0, MinValue & "m", "" )
)

## Calculation group: Comparison with same period last year

Calculation group that enables comparing selected period vs. same period shifted by one year. It has two items:

1. This Year

Returns the value without any alteration.

wide760SELECTEDMEASURE()

2. Previous Year

Returns the value after shifting the Date by one year, using SAMEPERIODLASTYEAR.

wide760CALCULATE(
SELECTEDMEASURE(),
SAMEPERIODLASTYEAR('Date'[Date])
)
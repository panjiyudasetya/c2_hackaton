---
id: confluence:416317444
source: confluence
type: page
space: TC
title: 1. Envision a way to structure data mart answer
author: Panji Y. Wiwaha
date: '2025-04-17'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/416317444
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/416317444
---
# 1. Envision a way to structure data mart answer

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/416317444  

## Content

# **Goals**

* Envision the structure of the PTO data mart on the terminal level.

# **Questions**

* What’s the average time for “**terminal X**” in a specific “**time frame**”for a ship with “**deadweight-tonnage**”?

# **Structure of the data mart**

The image below shows a higher-level overview of the data mart structure for the terminal level using the STAR schema.

Data mart illustration of the terminal time using STAR schema

* The `TerminalTime` fact table stores the average time that is spent by a particular ship when it enters and leaves the terminal.
* The `Port` dimension table stores information about the ports that are visited by a particular ship during the terminal’s visitations.
* The `Terminal` dimension table stores information about the terminals that are visited by a particular ship.
* The `Ship` dimension table stores information about the ship that visits particular terminals.
* The `Date` dimension table stores the derivative dates of the timestamp when the ship visits a terminal, such as a `day`, `month`, `year`, `week_number`, `month_full_name`, `month_short_name`, etc.
* The `Time` dimension table stores the derivative time of the timestamp when the ship visits a terminal, such as an `hour`, `minute`, `second`, etc.

# **Models definition**

fact\_terminal\_time

| **Column name** | **Type** | **Explanation** |
| --- | --- | --- |
| `id` | `PrimaryKey(string)` | The identifier of the terminal time. |
| `terminal_id` | `ForeignKey(DimTerminal)` | The identifier of the visited terminal. |
| `port_id` | `ForeignKey(DimPort)` | The identifier of the visited port. |
| `ship_id` | `ForeignKey(DimShip)` | The identifier of the ship. |
| `terminal_visit_` `start_time_iso_date_id` | `ForeignKey(DimDate)` | The date identifier refers to when the ship visits the terminal. |
| `terminal_visit_` `start_time_iso_time_id` | `ForeignKey(DimTime)` | The time identifier refers to when the ship visits the terminal. |
| `terminal_visit_` `end_time_iso_date_id` | `ForeignKey(DimDate)` | The date identifier refers to when the ship leaves the terminal. |
| `terminal_visit_` `end_time_iso_time_id` | `ForeignKey(DimTime)` | The time identifier refers to when the ship leaves the terminal. |
| `terminal_visit_` `average_time_duration` | `double` | The ship’s average time spent in the terminal. |
| `berths_time_duration` | `double` | Total duration needed by the ship on particular berths within the terminal. |
| `berths_visit_count` | `int` | Total berths' visitations within the terminal. |

dim\_port

| **Column name** | **Type** | **Explanation** |
| --- | --- | --- |
| `id` | `PrimaryKey(string)` | The identifier of the visited port. |
| `unlocode` | `Unique(string)` | A unique string that refers to the UN/LOCODE of the visited port. |
| `name` | `string` | Name of the visited port. |

dim\_terminal

| **Column name** | **Type** | **Explanation** |
| --- | --- | --- |
| `id` | `PrimaryKey(string)` | The identifier of the visited terminal. |
| `name` | `string` | Name of the visited terminal. |

dim\_ship

| **Column name** | **Type** | **Explanation** |
| --- | --- | --- |
| `id` | `PrimaryKey(string)` | The identifier of the ship. |
| `dwt` | `string` | A deadweight tonnage of the ship. |
| `dwt_category` | `string` | A deadweight tonnage category. |

dim\_date

| **Column name** | **Type** | **Explanation** |
| --- | --- | --- |
| `id` | `PrimaryKey(string)` | The identifier of the date visitation. |
| `iso_date` | `Unique(string)` | A unique string referring to the date of terminal visitation in the following format: `DD/MM/YYYY`.  i.e., `29/07/2024` |
| `day` | `int` | Day of the month. It’s taken from the `iso_date` value. |
| `month` | `int` | Month number. It’s taken from the `iso_date` value. |
| `month_short_name` | `string` | The short name of the month. It’s taken from the `iso_date` value. i.e., `Jan`, `Feb`, and so on. |
| `month_full_name` | `string` | The full name of the month. It’s taken from the `iso_date` value. i.e., `January`, `February`, and so on. |
| `week_of_year` | `int` | Week number of the year. It’s taken from the `iso_date` value. |
| `year` | `int` | Year number. It’s taken from the `iso_date` value. |

dim\_time

| **Column name** |  | **Explanation** |
| --- | --- | --- |
| `id` | `PrimaryKey(string)` | The identifier of the time visitation. |
| `iso_time` | `Unique(string)` | A unique string referring to the time of terminal visitation in the following format: `HH:MM:SS`.  i.e., `20:10:05` |
| `hour` | `int` | Hour(s) number. It’s taken from the `iso_time` value. |
| `minute` | `int` | Minute(s) number. It’s taken from the `iso_time` value. |
| `second` | `int` | Second(s) number. It’s taken from the `iso_time` value. |
| `timezone` | `string` | Optional, the default UTC. |

# **Topics**

#### What is the “*time*” in a terminal?

In general, the time at terminals refers to the accumulation time of all activities within the terminal when cargo enters and leaves the berth (including cargo operations).

#### How to calculate the average “*time*” in a terminal?

With the assumption a ship can visit one or multiple berths in one terminal, then the calculation formula for the average “time” is:

average\_terminal\_time\_duration = berths\_time\_duration / berths\_visit\_count

The `berths_time_duration` is the cumulative duration of all visited berths in a terminal, where the time duration in each berth is calculated with this formula:

berth\_time\_duration = berth\_end\_time - berth\_start\_time

#### What kind of the “*time frame*” is needed?

In most cases, we calculate the average terminal time using a monthly period. However, a weekly period might also be needed for some cases.

#### What is the “*deadweight-tonnage*”?

In general, it measures the total contents of a ship, including cargo, fuel, crew, passengers, food, and water, aside from boiler water.

#### How do we classify the “*deadweight-tonnage*” of a ship?

Wet bulk category classifications

| **DWT** | **Category** |
| --- | --- |
| `null` | None |
| `0 - 10,000` | Barge |
| `10,001 - 24,999` | General Purpose (GP) |
| `25,000 - 44,999` | Medium Range (MR) |
| `45,000 - 79,999` | Large Range 1 (LR1) |
| `80,000 - 119,999` | Aframax / Large Range 2 (LR2) |
| `>= 160,000` | Ultra Large Crude Carrier (ULCC) |
| Otherwise | None |

Dry bulk category classifications

| **DWT** | **Category** |
| --- | --- |
| `null` | None |
| `0 - 15,000` | Mini Bulk |
| `15,001 - 40,000` | Handy Size |
| `40,001 - 60,000` | Supramax |
| `60,001 - 100,000` | Panamax |
| `100,001 - 200,000` | Cape |
| `>= 200,001` | Ultra Cape |
| Otherwise | None |
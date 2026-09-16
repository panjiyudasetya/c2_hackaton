---
id: confluence:275054602
source: confluence
type: page
space: TC
title: How to change the configuration of the focus and benchmark terminal set
author: Yaren Aslan
date: '2024-08-23'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/275054602
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/275054602
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/edit-v2/275054602#Tables
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/edit-v2/275054602#Tip
---
# How to change the configuration of the focus and benchmark terminal set

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/275054602  

## Content

# Steps

1. Navigate to the Semantic Model of the dashboard you wish to change the configuration of.

There are two tables that you need to change Terminal Focus and Benchmark Pairs. Refer to [Tables](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/edit-v2/275054602#Tables) for more detail about these tables. To observe the actual data on the table in your semantic model, use the [Tip to observe the tables](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/edit-v2/275054602#Tip).

2. On the Semantic Model, click Open Data model

3. On the list of table on the right, find and click Terminal Focus

4. On the white area, adjust/replace the existing values according to the new configuration. Refer to [Tables](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/edit-v2/275054602#Tables) for the order and description of the fields.

When you click enter, or move to the next step, you will encounter a loading pop-up.

5. On the list of table on the right, find and click Benchmark Pairs. Edit accordingly.

6. When you validated the change on the Test environment and are comfortable to add external users, copy the Report on our Teqplay BI live environment.

To share the report with external users, refer to <https://teqplaybv.atlassian.net/wiki/x/BQCUE> and <https://teqplaybv.atlassian.net/wiki/x/AgB1E>.

# Tables

1. Terminal Focus

This table is to define the list of Terminals that the users would see as the main terminal for them.

|  |  |
| --- | --- |
| **Field** | **Description** |
| Port | UNLOCODE of the port where the terminal is located |
| Portfolio | (optional) Portfolio of the terminal, used for clustering the terminals if needed. |
| Terminal Focus | Name of the terminal |
| Terminal ID | ID of the terminal. It can be found on PTO, Poma or datamart. |
| Max PTT | Maximum foreseen value for PTT. To be used for scaling gauges/bar charts. Decide according to the norms of the terminal. |
| Max Waiting | Maximum foreseen value for Waiting. To be used for scaling gauges/bar charts. |
| Max Steaming In | Maximum foreseen value for Steaming In. To be used for scaling gauges/bar charts. |
| Max Berth Stay | Maximum foreseen value for Berth Stay. To be used for scaling gauges/bar charts. |
| Max Steaming Out | Maximum foreseen value for Steaming Out. To be used for scaling gauges/bar charts. |
| Waited cut-off | Threshold for waiting duration (hour) above which a visiting vessel is considered to be waited. |
| Link | (optional) Reference to the page in dashboard where the terminal is selected as focus. |
| Bounding Boxes | (optional) Reference to the Confluence page where port and terminal boundaries are documented. |

2. Benchmark Pairs

This table is to define relationships between the selected terminal and the shown terminals. The terminal itself and the benchmark competition terminals should be listed on this table for every Focus Terminal. There is a one-to-many relationship between Terminal Focus[Terminal ID] table and Benchmark Pairs[Terminal Selection ID].

|  |  |
| --- | --- |
| Field | Description |
| Terminal Selection | Name of the focus terminal (same value as Terminal Focus[Terminal Focus]) |
| Terminal Selection ID | ID of the focus terminal (same value as Terminal Focus[Terminal ID]) |
| Terminal Shown | Name of the benchmark (competition) terminal |
| Terminal | Abbreviation for the benchmark terminal |
| Color | Integer from 0 to 6. The focus terminal should be given 0, the competition terminals should get unique values from 1 to 6. |
| Terminal Shown ID | ID of the benchmark (competition) terminal. It can be found on PTO, Poma or datamart. |
| Batch | (optional) Batch where the terminal was dellivered. |
| Waited cut-off | Threshold for waiting duration (hour) above which a visiting vessel is considered to be waited. |

# Tip to observe the tables

To see the content of the tables, you can use the list of tables on the right hand side. Scroll down if needed and click on the box next to the name of the Table.
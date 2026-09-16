---
id: confluence:576028676
source: confluence
type: page
space: TC
title: PTO-1466 Compare on mart level to understand the difference between Old and
  New PTO Architecture
author: Panji Y. Wiwaha
date: '2025-04-17'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/576028676
explicit_links:
- jira:PTO-1466
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/576028676
---
# PTO-1466 Compare on mart level to understand the difference between Old and New PTO Architecture

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/576028676  

## Content

Terminal Visit

|  | **OLD** | **NEW** |
| --- | --- | --- |
| table name | terminal\_visit | fact\_terminal\_visit |
| notes | the old terminal visit table has more columns than the new one. Also the data is more than the new one. | need to complete more column and confirm the column mapping from the new vs the old one. |
| what’s in there | first bunker (departure and arrival), terminal reason, first lift, port drifting ( inside eos, outside eos), moored, mooring duration, port anchor, terminal moves, port moves, terminal visit time, pilot onboard, pilot disembarked, terminal visit positions, terminal anchor duration, port total waiting time (inside, outside, voyage), port total cargo and non cargo ops, | terminal visit positions, mooring duration, turn around time duration, berth cargo and non cargo ops durations, |
| what’s next |  | ingest more data and calculate some durations, waiting time, |

Port Visit

|  | **OLD** | **NEW** |
| --- | --- | --- |
| table name | port\_visit | fact\_port\_visit |
| notes | the old port visit table has more columns than the new one. Also the data is more than the new one. | need to complete more column and confirm the column mapping from the new vs the old one. |
| what’s in there | reason arrival & departure, first & last lift date, moves (count, source, crane), drifting (inside or outside eos), pilot inbound & outbound, bunker arrival first & last, eos entry & exit, anchor up & down, total time (mooring, unmooring, waiting inside & outside), total cargo & non cargo ops, | cargo and non cargo ops duration, pilot inbound and outbound, turn around time, berth and terminal visit count, total mooring duration |
| what’s next |  | ingest more data and calculate some durations, waiting time, |
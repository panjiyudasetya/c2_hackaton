---
id: confluence:222953473
source: confluence
type: page
space: TC
title: (R)events benchmark
author: Former user (Deleted)
date: '2023-11-03'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/222953473
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/222953473
---
# (R)events benchmark

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/222953473  

## Content

|  | **Description** | **Scenario ID** | **Node index** | **Duration** **avg mps** | **Graph** |
| --- | --- | --- | --- | --- | --- |
| 1 | before, all events | `7dc533a4-3b2f-4faa-b11f-187b78a0f107` | 3 | 25m 14s  28k mps |  |
| 2 | before, no encounter events | `7e94d621-8130-4b1d-bde0-0f4515db0435` | 2 | 11m 24s  30/31k mps |  |
| 3 | + specific interest/service events  all events | `cadd1be9-73f7-4dc0-8707-76fa16b9b996` | 0 | 17m 24s  31k mps (encounter)  23k mps (diff/area) |  |
| 4 | + specific interest/service events  no encounter events | `3f305ecb-b795-476c-b8bd-9521a180666a` | 1 | 11m 30s  30/31k mps |  |
| 5 | + specific interest/service events  + parallel message handling  all events | `b0e02575-b839-4d3a-85bf-d89be292cc9f` | 0 | ~22m  23k mps (encounter)  18k mps (diff/area) |  |
| 6 | + specific interest/service events  + parallel message handling  no encounter events | `28656340-e674-4378-977a-858a638b072b` | 1 | ~same as prev wo/ encounter  32k mps |  |
---
id: confluence:769523733
source: confluence
type: page
space: TC
title: '[DM] Data validity checks'
author: Panji Y. Wiwaha
date: '2025-06-24'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/769523733
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/769523733
---
# [DM] Data validity checks

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/769523733  

## Content

# Definition

Data are valid if it conforms to the syntax (format, type, range) of its definition.

# Non-empty duration check

Any duration fields should not be empty (NULL). When it does, the value must be equal to 0.

| **Scope** | **Table Name** | **Fields to check** |
| --- | --- | --- |
| **Fact port visits** | fact\_port\_visit | [any]\_duration |
| **Fact terminal visits** | fact\_terminal\_visit | [any]\_duration |
| **Fact berth visits** | fact\_berth\_visit | [any]\_duration |
| **Fact bunkering** | fact\_bunkering | [any]\_duration |
| **Fact service vessel** | fact\_service\_vessel | [any]\_duration |
| **Fact ship-to-ship transfers** | fact\_ship\_to\_ship\_transfers | [any]\_duration |
| **Fact tugs** | fact\_tug | [any]\_duration |
| **Fact anchorages** | fact\_anchor | [any]\_duration |
| add more… | add more… | add more… |

# Non-negative value check

Any duration fields should not be negative.

| **Scope** | **Table Name** | **Fields to check** |
| --- | --- | --- |
| **Fact port visits** | fact\_port\_visit | [any]\_duration |
| **Fact terminal visits** | fact\_terminal\_visit | [any]\_duration |
| **Fact berth visits** | fact\_berth\_visit | [any]\_duration |
| **Fact bunkering** | fact\_bunkering | [any]\_duration |
| **Fact service vessel** | fact\_service\_vessel | [any]\_duration |
| **Fact ship-to-ship transfers** | fact\_ship\_to\_ship\_transfers | [any]\_duration |
| **Fact tugs** | fact\_tug | [any]\_duration |
| **Fact anchorages** | fact\_anchor | [any]\_duration |
| add more… | add more… | add more… |

# Existence check

* The number of inserted records must be equal to the number of payload data.

* The number of updated records must be equal to the number of payload data (if the records are not identical to the payload data).

| **Scope** | **Table Name** |
| --- | --- |
| **Fact port visits** | fact\_port\_visit |
| **Fact terminal visits** | fact\_terminal\_visit |
| **Fact berth visits** | fact\_berth\_visit |
| **Fact bunkering** | fact\_bunkering |
| **Fact service vessel** | fact\_service\_vessel |
| **Fact ship-to-ship transfers** | fact\_ship\_to\_ship\_transfers |
| **Fact tugs** | fact\_tug |
| **Fact anchorages** | fact\_anchor |
| **Fact pilots** | fact\_pilot |
| **Fact port calls** | fact\_port\_calls fact\_port\_calls\_by\_terminal |
| **Fact standard deviations of the terminal visit time** | fact\_stdev\_time\_terminal\_visit fact\_stdev\_time\_terminal\_visit\_monthly |
| **Fact voyages** | fact\_voyage fact\_voyage\_summary\_quarterly |
| add more… | add more… |
---
id: confluence:342458372
source: confluence
type: page
space: TC
title: 'VesselVoyage: Definition Fallbacks'
author: Leon Joosse (Unlicensed)
date: '2024-12-02'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/342458372
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/342458372
---
# VesselVoyage: Definition Fallbacks

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/342458372  

## Content

| **Labels** | **Meaning** |
| --- | --- |
| Real-timeGreen | When handling the events in VesselVoyage in real time. |
| afterwardsYellow | Running the fallback afterwards when the Visit or Voyage is finished.  This also indicates that something can run in the background without blocking event processing. |
| SUB-PORTBlue | This only applies if we are talking about a sub-port (e.g. NLVLA, not NLRTM) |

| **Scenario** | **Trigger** | **Type** | **Fallback** | **Note** |
| --- | --- | --- | --- | --- |
| Missing EOSP Start | When receiving one of the following events:   1. Anchor 2. Pilot Encounter 3. Main Port Inner/Outer 4. Sub Port EOSP 5. Sub Port Inner/Outer | Real-timeGreen | The first available event inside the EOSP area of the missing EOSP start event:   1. Anchor start 2. Anchor end 3. Pilot start 4. Port start 5. Berth start |  |
| When receiving the EOSP end event | afterwardsYellow |  |
| Missing EOSP End | Scheduled task checking all ongoing Visits with all   1. Port activities finished 2. Anchor activities finished   Trigger when the matching ship is outside the EOSP of the main Port. | afterwardsYellow | Determine by trace?  No timestamp would make sense here to fall back on | This should be checked for both the current Visit EOSP and all other main Port EOSP that are used for overlap checking. |
| Missing Port Start | When entering the infra inside the Port’s inner area, The first :   1. Anchor 2. Pilot Encounter or Pilot Area 3. Lock 4. Berth | Real-timeGreen | Time and location of start event of entered infra |  |
| 1. When receiving Port End 2. When finishing Visit | afterwardsYellow | Determine by trace | This should only happen when entering the Port but never entering something else inside the Port, which is very unlikely. |
| Missing Port End | 1. When entering or exiting the anchor area outside the Port 2. sub-portBlue When exiting the main Port 3. When exiting the EOSP | Real-timeGreen | Time and location of the trigger |  |
| When finishing the Visit | afterwardsYellow | Determine by trace | This should only be needed if we missed the EOSP end as well. |
| Missing UniqueBerth Start | When receiving the end event for the same berth | Real-timeGreen | Determine by trace |  |
| When finishing the Visit | afterwardsYellow |  |
| Missing UniqueBerth End | 1. When exiting the Port of the berth 2. When starting anchor 3. When exiting anchor 4. When exiting the EOSP | Real-timeGreen | Time and location of the trigger |  |
| When finishing the Visit | afterwardsYellow | Determine by trace |  |
| Missing Pilot Inbound | When entering the main Port | Real-timeGreen | The latest pilot area before entering the main Port.  When pilot area duration is smaller than 15 minutes:  Start of fallback = Pilot area end. End of fallback = ^ same we use a 0 duration.  Otherwise: Start of fallback = Pilot area start + 15 minutes. End of fallback = Pilot area end. |  |
| Missing Pilot Outbound | When exiting the main Port EOSP | Real-timeGreen | The first pilot area after leaving the main Port.  When pilot area duration is smaller than 15 minutes:  Start of fallback = Pilot area end. End of fallback = ^ same we use a 0 duration.  Otherwise: Start of fallback = Pilot area start + 15 minutes. End of fallback = Pilot area end. |  |
| Missing Anchor Down | When processing Anchor up | Real-timeGreen | Anchor area start event |  |
| When finishing Visit | afterwardsYellow | Determine by trace. The first AIS point slower than 1.0 knots |  |
| Missing Anchor Up | When entering Port | Real-timeGreen | Anchor area end event |  |
|  | When finishing Visit | afterwardsYellow | 1. Main port enter when anchor outside port boundaries 2. First berth enter when anchor inside port boundaries 3. Determine by trace. The first AIS point slower than 1.0 knots |  |
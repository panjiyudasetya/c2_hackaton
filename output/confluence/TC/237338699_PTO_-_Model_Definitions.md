---
id: confluence:237338699
source: confluence
type: page
space: TC
title: PTO - Model Definitions
author: Wouter Naloop (Unlicensed)
date: '2024-04-24'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/237338699
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/237338699
---
# PTO - Model Definitions

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/237338699  

## Content

Within the PTO Data model, the following definitions are being used for data fields defining the Port Turnaround Optimization data:

Terminal Visit DataMart model

|  | Field | Description |
| --- | --- | --- |
| 1 | id | A unique identifier |
| 2 | portVisitId | The identifier of the port visit this I linked to |
| 3 | terminalVisitStart | The time the ship arrived at the first berth of a terminal |
| 4 | terminalVisitEnd | The time the ship left the last berth of a terminal, all berth visits count if the ship has not left the terminal area |
| 5 | terminal | The related terminal |
| 6 | port | The related port |
| 7 | ship | The related ship |
| 8 | previousPort | The previous port the ship visited |
| 9 | portEosEntry | The first time the ship entered the port EOS area since leaving the previous port |
| 10 | portEosExit | The last time the ship exited the port EOS area before entering the next port |
| 11 | portPilotOnBoardInbound | The pilot that goes on board before entering the first berth and after leaving the anchorage |
| 12 | portPilotOnBoardInboundType | A description of which fallback has been used in case we couldn't find a pilot ship near the ship |
| 13 | portPilotDisembarkedOutbound | The pilot that goes off board when the ship is sailing out of the port |
| 14 | portPilotDisembarkedOutboundType | A description of which fallback has been used in case we couldn't find a pilot ship near the ship |
| 15 | portAnchorDown | The first time the ship dropped the anchor before entering the port |
| 16 | portAnchorDownType | A description of which fallback has been used in case we detected the ship heaving the anchor but did not find the dropping of the anchor |
| 17 | portAnchorUp | The last time the ship heaved the anchor before entering the port |
| 18 | portAnchorUpType | A description of which fallback has been used in case we detected the ship dropping the anchor but did not find the heaving of the anchor |
| 19 | portStartDriftingInsideEos | First time we detect that the ship is sailing slowly outside of the port boundries after the portEosEntry |
| 20 | portEndDriftingInsideEos | Last time we detect that the ship is sailing slowly outside of the port boundries before the portPilotOnBoardInbound |
| 21 | portStartDriftingOutsideEos | First time we detect that the ship is sailing slowly outside of the port boundries before the portEosEntry |
| 22 | portEndDriftingOutsideEos | Last time we detect that the ship is sailing slowly outside of the port boundries before the portEosEntry |
| 23 | portTotalMooringDuration | The total time the ship spent moving into a berth after being in the mooring area of the terminal |
| 24 | portTotalUnmooringDuration | The total time the ship spent moving out of a berth till moving out of the mooring area of the terminal |
| 25 | portAnchorDuration | The time spent in anchorage this does not include sailing between anchorage if that is detected |
| 26 | portPilotToPilotDuration | The time between portPilotOnBoardInbound and portPilotDisembarkedOutbound |
| 27 | portAnchorToPilotDuration | The time between portAnchorDown and portPilotDisembarkedOutbound |
| 28 | portAnchorToPilotOnBoardDuration | The time between portAnchorDown and portPilotOnBoardInbound |
| 29 | portInboundTravelDuration | The sailing time from portPilotOnBoardInbound till the first berth |
| 30 | portOutboundTravelDuration | The sailing time from the last berth till portPilotDisembarkedOutbound |
| 31 | portShiftingBetweenTerminalsDuration | The total sailing time between terminal visits |
| 32 | portShiftingWithinTerminalsDuration | The total sailing time from berth visit to berth visit within a terminal visit |
| 33 | portTotalWaitingTimeInsidePortDuration | All time spend laying still inside a port that was not related to a cargo operation, this includes layby, anchorage, unknown waiting |
| 34 | portTotalWaitingTimeOutsidePortDuration | All time spend laying still outside the port, this includes anchorage, unknown waiting, drifting |
| 35 | portTotalWaitingTimeVoyageDuration | All time spend laying still outside the eos area, this includes anchorage, unknown waiting, drifting |
| 36 | portTotalCargoOperationDuration | All time spent in a cargo operation berths in the port visit |
| 37 | portTotalNonCargoOperationDuration | All time spent in a non cargo operation berths in the port visit |
| 38 | portTotalMooredDuration | All time spent in berths in the port visit |
| 39 | portTerminalVisitCount | The amount of terminals visited in the port call |
| 40 | portStopsCount | The amount of times the ship was detected to have stopped in the port call |
| 41 | portPilotEventCount | The amount of pilot events detected in the inbound or outbound process |
| 42 | portCargoOperationBerthVisitCount | The amount of cargo operation berths visited in the port call |
| 43 | portBerthVisitCount | The amount of berths visited in the port call |
| 44 | terminalFirstBunkerArrival | The first bunker vessel to come alongside during the terminal visit |
| 45 | terminalLastBunkerArrival | The last bunker vessel to come alongside during the terminal visit |
| 46 | terminalAnchorDuration | The amount of anchorage time spent before the terminal visit. |
| 47 | terminalWaitingTimeVoyageDuration | Only assigned to the first terminal visit and equal to portTotalWaitingTimeVoyageDuration |
| 48 | terminalWaitingTimeOutsidePortDuration | Only assigned to the first terminal visit and equal to portTotalWaitingTimeOutsidePortDuration |
| 49 | terminalVisitPosition | The index of the terminal visit when looking at all terminal visits as a list |
| 50 | terminalMooredDuration | The amount of time spent in berth |
| 51 | terminalCargoDuration | The amount of time spent in cargo operation berths |
| 52 | terminalNonCargoDuration | The amount of time spent in non cargo operation berths |
| 53 | terminalInboundTravelDuration | The amount of time spent sailing from the previous terminal visit end time or portPilotOnBoardInbound till terminalVisitStart |
| 54 | terminalOutboundTravelDuration | Only assigned to the last terminal visit and equal to portOutboundTravelDuration |
| 55 | terminalBunkerCount | The amount of bunker vessels detected alongside in the terminal visit |
| 56 | terminalInboundWaitingDuration | All time spend laying still before the terminal visit started that was not related to a cargo operation, this includes layby, anchorage, unknown waiting |
| 57 | terminalShiftingWaitingDuration | All time spend laying still during the terminal visit started that was not related to a cargo operation, this includes layby, anchorage, unknown waiting |
| 58 | terminalCargoOperationBerthVisitCount | The amount of cargo operation berths visited in the terminal visit |
| 59 | terminalBerthVisitCount | The amount of berths visited in the terminal visit |
| 60 | terminalOrderDescriptor | This describes where in the port visit the terminal visit occured |
| 61 | terminalGroupingOrderDescriptor | This describes where in the port visit the terminal group occured |
| 62 | isValid | Is the port visit verified by us |
| 63 | reportStartDate | The time the report was run that resulted in the related port visit |

Berth Visit DataMart model

|  | Field | Description |
| --- | --- | --- |
| 1 | berthVisitId | The unique id of this berth visit |
| 2 | terminalVisitId | The unique id of the terminal visit this berth visit is related to |
| 3 | terminalGroupId | The unique id of the terminal group this berth visit is related to |
| 4 | visitId | The unique id of the port visit this berth visit is related to |
| 5 | berth | The related berth information |
| 6 | ship | The related ship information |
| 7 | port | The related port information |
| 8 | berthStart | the start time of the berth visit |
| 9 | berthEnd | the start time of the berth visit |
| 10 | berthStartMooring | The time entering the mooring area of the terminal |
| 11 | berthEndUnmooring | The time leaving the mooring area of the terminal after the berth visit |
| 12 | berthAllFast | The last tug leaving after tugging the vessel |
| 13 | berthFirstTugArrivedDeparture | The time the first tug arrived at the vessel that was also afterwards involved in the tugging on berth departure |
| 14 | berthLastTugArrivedDeparture | The time the last tug arrived at the vessel that was also afterwards involved in the tugging on berth departure |
| 15 | berthUniqueTugsArrivalCount | The amount of tugs used in the arrival process |
| 16 | berthUniqueTugsDepartureCount | The amount of tugs used in the departure process |
| 17 | berthVisitPosition | The index of the berth visit when looking at all berth visits as a list |
| 18 | berthBunkersCount | The amount of bunkers alongside |
| 19 | berthMooringDuration | The amount of time spent between berthStartMooring and berthStart |
| 20 | berthUnmooringDuration | The amount of time spent between berthEnd and berthEndUnmooring |
| 21 | berthMooredDuration | The amount of time spent between berthStart and berthEnd |
| 22 | berthIsCargoOperation | If we deem this berth a cargo operation berth for this ship type |
| 23 | isValid | Is the port visit verified by us |
| 24 | reportStartDate | The time the report was run that resulted in the related port visit |

Port Visit DataMart model

|  | Field | Description |
| --- | --- | --- |
| 1 | visitId | The unique id of the port visit |
| 2 | port | The related port information |
| 3 | ship | The related ship information |
| 4 | previousPort | The previous port visited |
| 5 | eosEntryDate | The first time the ship entered the port EOS area since leaving the previous port |
| 6 | eosExitDate | The last time the ship exited the port EOS area before entering the next port |
| 7 | startDriftingInsideEosDate | First time we detect that the ship is sailing slowly outside of the port boundries after the portEosEntry |
| 8 | endDriftingInsideEosDate | Last time we detect that the ship is sailing slowly outside of the port boundries before the portPilotOnBoardInbound |
| 9 | startDriftingOutsideEosDate | First time we detect that the ship is sailing slowly outside of the port boundries before the portEosEntry |
| 10 | endDriftingOutsideEosDate | Last time we detect that the ship is sailing slowly outside of the port boundries before the portEosEntry |
| 11 | pilotOnBoardInboundDate | The pilot that goes on board before entering the first berth and after leaving the anchorage |
| 12 | pilotOnBoardInboundType | A description of which fallback has been used in case we couldn't find a pilot ship near the ship |
| 13 | pilotDisembarkedOutboundDate | The pilot that goes off board when the ship is sailing out of the port |
| 14 | pilotDisembarkedOutboundType | A description of which fallback has been used in case we couldn't find a pilot ship near the ship |
| 15 | anchorDownDate | The first time the ship dropped the anchor before entering the port |
| 16 | anchorDownType | A description of which fallback has been used in case we detected the ship heaving the anchor but did not find the dropping of the anchor |
| 17 | anchorUpDate | The last time the ship heaved the anchor before entering the port |
| 18 | anchorUpType | A description of which fallback has been used in case we detected the ship dropping the anchor but did not find the heaving of the anchor |
| 19 | firstBunkerArrivalDate | The first bunker vessel to come alongside during the port visit |
| 20 | lastBunkerArrivalDate | The last bunker vessel to come alongside during the port visit |
| 21 | totalWaitingTimeInsidePortDuration | All time spend laying still inside a port that was not related to a cargo operation, this includes layby, anchorage, unknown waiting |
| 22 | totalWaitingTimeOutsidePortDuration | All time spend laying still outside the port, this includes anchorage, unknown waiting, drifting |
| 23 | totalWaitingTimeVoyageDuration | All time spend laying still outside the eos area, this includes anchorage, unknown waiting, drifting |
| 24 | sailingBetweenBerthsDuration | The amount of time spent shifting from one berth to another |
| 25 | inboundTravelDuration | The sailing time from portPilotOnBoardInbound till the first berth |
| 26 | outboundTravelDuration | The sailing time from the last berth till portPilotDisembarkedOutbound |
| 27 | shiftingBetweenTerminalsDuration | The total sailing time between terminal visits |
| 28 | shiftingWithinTerminalsDuration | The total sailing time from berth visit to berth visit within a terminal visit |
| 29 | totalCargoOperationDuration | All time spent in a cargo operation berths |
| 30 | totalNonCargoOperationDuration | All time spent in a non cargo operation berths |
| 31 | totalMooredDuration | All time spent in berths |
| 32 | cargoOperationBerthVisitCount | The amount of cargo operation berths visited in the port call |
| 33 | totalMooringDuration | The total time the ship spent moving into a berth after being in the mooring area of the terminal |
| 34 | totalUnmooringDuration | The total time the ship spent moving out of a berth till moving out of the mooring area of the terminal |
| 35 | anchorDuration | The time spent in anchorage this does not include sailing between anchorage if that is detected |
| 36 | pilotToPilotDuration | The time between portPilotOnBoardInbound and portPilotDisembarkedOutbound |
| 37 | anchorToPilotDuration | The time between portAnchorDown and portPilotDisembarkedOutbound |
| 38 | anchorToPilotOnBoardDuration | The time between portAnchorDown and portPilotOnBoardInbound |
| 39 | stopsCount | The amount of times the ship was detected to have stopped in the port call |
| 40 | berthVisitCount | The amount of berths visited in the port call |
| 41 | terminalVisitCount | The amount of terminals visited in the port call |
| 42 | pilotEventCount | The amount of pilot events detected in the inbound or outbound process |
| 43 | isValid | Is the port visit verified by us |
| 44 | reportStartDate | The time the report was run that resulted in the related port visit |

To visually link these definitions to a visit structure, the following diagram shows the interrelation between elements in the waiting times:

Similarly the following diagram explains the linkages between the travel times in port, again with below the line all related timestamps and above the line all related durations:

With the details around a specific terminal visit, and the behavior of alongside services around that indicated below in this diagram:

Those diagrams can all be edited in [this draw.io file](https://app.diagrams.net/#G1PA8TJ1dYSJ7bSEzvD9SpDgapcJT_TV_o).

The Terminal Visit model follows a slightly different visit structure, the structure is described in the following diagram.   
The difference is that anything that happens before a Terminal Visit starts is assigned to that terminal visit.   
This ensures that a second terminal visit does not have the waiting time accounted to it that was due to the first terminal visit

This diagram can all be edited in [this draw.io file](https://app.diagrams.net/#G1f7AWXY8GDQS096DcbDLrGYjy4JB-AXCs#%7B%22pageId%22%3A%225zA9AX0Iml47TL5kfOTT%22%7D).
---
id: confluence:943685634
source: confluence
type: page
space: TC
title: PTO-2306 List of calculated columns that are still needed
author: Yaren Aslan
date: '2025-11-12'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/943685634
explicit_links:
- jira:PTO-2306
- jira:PTO-2354
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/943685634
---
# PTO-2306 List of calculated columns that are still needed

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/943685634  

## Content

61falsedefaultlisttrue

# Calculations that can be moved to Datamart

## Outlier detection

| **Table** | **Column** | **Note** |
| --- | --- | --- |
| Port | Moored Avg for Outlier Detection | **total\_moored\_duration** |
| Port | Moored Std for Outlier Detection | **total\_moored\_duration** |
| Port | Shifting Avg for Outlier Detection | **shifting\_between\_terminals + shifting\_inside\_terminals** |
| Port | Shifting Std for Outlier Detection | **shifting\_between\_terminals + shifting\_inside\_terminals** |
| Port | SteamingIn Avg for Outlier Detection | **port\_inbound\_travel\_duration** |
| Port | SteamingIn Std for Outlier Detection | **port\_inbound\_travel\_duration** |
| Port | SteamingOut Avg for Outlier Detection | **port\_outbound\_travel\_duration** |
| Port | SteamingOut Std for Outlier Detection | **port\_outbound\_travel\_duration** |
| Port | WaitDuringVisit Avg for Outlier Detection | **during\_visit\_anchor\_duration + total\_slowmoving\_duration\_inport** |
| Port | WaitDuringVisit Std for Outlier Detection | **during\_visit\_anchor\_duration + total\_slowmoving\_duration\_inport** |
| Port | WaitBeforeArrival Avg for Outlier Detection | **before\_visit\_anchor\_duration + total\_slowmoving\_duration\_arrival** |
| Port | WaitBeforeArrival Std for Outlier Detection | **before\_visit\_anchor\_duration + total\_slowmoving\_duration\_arrival** |
| Port Visit | MooredWithinRangeColMooredWithinRangeCol = VAR \_Avg = RELATED(Port[Moored Avg for Outlier Detection]) VAR \_Std = RELATED(Port[Moored Std for Outlier Detection]) VAR mult = 5 RETURN IF( 'Berth Visit'[Total Moored Duration] <= (\_Avg + mult \* \_Std) && 'Berth Visit'[Total Moored Duration] >= (\_Avg - mult \* \_Std) && 'Berth Visit'[Total Moored Duration]>= 0, 1, 0 ) | Check if **total\_moored\_duration** of the visit is within (mean + 5 \* std). |
| Port Visit | ShiftingWithinRangeColShiftingWithinRangeCol = VAR \_Avg = RELATED(Port[Shifting Avg for Outlier Detection]) VAR \_Std = RELATED(Port[Shifting Std for Outlier Detection]) VAR mult = 5 RETURN IF( 'Berth Visit'[Shifting Duration] <= (\_Avg + mult \* \_Std) && 'Berth Visit'[Shifting Duration] >= (\_Avg - mult \* \_Std) && 'Berth Visit'[Shifting Duration]<= 48, 1, 0 ) | Check if **(shifting\_between\_terminals + shifting\_inside\_terminals)** of the visit is within (mean + 5 \* std).  There is an additional check here, which imposes a hardcoded upper bound as 48 hours. |
| Port Visit | SteamingInWithinRangeColSteamingInWithinRangeCol = VAR \_Avg = RELATED(Port[SteamingIn Avg for Outlier Detection]) VAR \_Std = RELATED(Port[SteamingIn Std for Outlier Detection]) VAR mult = 5 RETURN IF( 'Berth Visit'[Steaming in] <= (\_Avg + mult \* \_Std) && 'Berth Visit'[Steaming in] >= (\_Avg - mult \* \_Std), 1, 0 ) | Check if **port\_inbound\_travel\_duration** of the visit is within (mean + 5 \* std). |
| Port Visit | SteamingOutWithinRangeColSteamingOutWithinRangeCol = VAR \_Avg = RELATED(Port[SteamingOut Avg for Outlier Detection]) VAR \_Std = RELATED(Port[SteamingOut Std for Outlier Detection]) VAR mult = 5 RETURN IF( 'Berth Visit'[Steaming out] <= (\_Avg + mult \* \_Std) && 'Berth Visit'[Steaming out] >= (\_Avg - mult \* \_Std), 1, 0 ) | Check if **port\_outbound\_travel\_duration** of the visit is within (mean + 5 \* std). |
| Port Visit | WaitDuringVisitWithinRangeColWaitDuringVisitWithinRangeCol = VAR \_Avg = RELATED(Port[WaitDuringVisit Avg for Outlier Detection]) VAR \_Std = RELATED(Port[WaitDuringVisit Std for Outlier Detection]) VAR mult = 5 RETURN IF(         'Berth Visit'[Waiting During Visit Duration] <= (\_Avg + mult \* \_Std) &&         'Berth Visit'[Waiting During Visit Duration] >= (\_Avg - mult \* \_Std),         1,         0     ) | Check if **port\_outbound\_travel\_duration** of the visit is within (mean + 5 \* std). |
| Port Visit | WaitBeforeArrivalWithinRangeColWaitBeforeArrivalWithinRangeCol = VAR \_Avg = RELATED(Port[WaitBeforeArrival Avg for Outlier Detection]) VAR \_Std = RELATED(Port[WaitBeforeArrival Std for Outlier Detection]) VAR mult = 5 RETURN IF(         'Berth Visit'[Waiting Before Arrival Duration] <= (\_Avg + mult \* \_Std) &&         'Berth Visit'[Waiting Before Arrival Duration] >= (\_Avg - mult \* \_Std),         1,         0     ) | Check if **(before\_visit\_anchor\_duration + total\_slowmoving\_duration\_arrival)** of the visit is within (mean + 5 \* std). |
| Port Visit | Outlier showing preferenceOutlier showing preference = VAR WithinRange = IF(         ISBLANK('Berth Visit'[pilot\_onboard\_timestamp])=FALSE() &&         'Berth Visit'[WaitOutWithinRangeCol] <> 0 &&         'Berth Visit'[WaitInWithinRangeCol] <> 0 &&         'Berth Visit'[SteamingInWithinRangeCol] <> 0 &&         'Berth Visit'[MooredWithinRangeCol] <> 0 &&         'Berth Visit'[ShiftingWithinRangeCol] <> 0 &&         'Berth Visit'[SteamingOutWithinRangeCol] <> 0 &&         'Berth Visit'[# Berth Visits in Port] < 8         ,         "Exclude outliers",         "Show outliers"     ) RETURN WithinRange | Based on the checks on moored duration, shifting, steaming in, steaming out, waiting during visit and waiting before arrival, label the visit as outlier (if any of the conditions do not hold).  There are two additional checks in this step:   * Is pilot\_onboard\_timestamp available? * Does the port visit have fewer than 8 berth visits? |

## Duration calculations

| **Table** | **Column** | **Note** |
| --- | --- | --- |
| Port Visit | Port Turnaround Time'Berth Visit'[Waiting Duration] + 'Berth Visit'[Steaming in] + 'Berth Visit'[Total Moored Duration] + 'Berth Visit'[Shifting Duration] + 'Berth Visit'[Steaming out] | Waiting duration is the sum of Waiting Before Arrival and During Visit |
| Port Visit | Waiting Duration [Port Visit.total\_waiting\_time\_during\_visit] + [Port Visit.total\_waiting\_time\_before\_arrival] | PQ. |
| Port Visit | total\_waiting\_time\_before\_arrival [total\_slowmoving\_duration\_arrival] + [before\_visit\_anchor\_duration] | PQ. for both PTO Ports & data validation dashboards, waiting before arrival is more useful than waiting outside port (which also includes after visit). Changing the calculation and keeping the column would suffice. |
| Port Visit | total\_waiting\_time\_during\_visit [total\_slowmoving\_duration\_inport] + [during\_visit\_anchor\_duration] | PQ. I would have expected this to be the same as inside\_port waiting, but it returns different results, not sure why. |
| Port Visit | Shifting Duration [Port Visit.shifting\_between\_terminals\_duration] + [Port Visit.shifting\_inside\_terminals\_duration] |  |
| Port Visit | Duration between EOS entry and POB Duration.TotalHours([pilot\_onboard\_inbound\_timestamp]-[eos\_entry\_timestamp]) | Used for data validation. |
| Port Visit | Duration between PDK and EOS exit Duration.TotalHours([eos\_exit\_timestamp]-[pilot\_disembarked\_outbound\_timestamp]) | Used for data validation. |

---

# Calculations that can stay in Power Query/DAX

## Ship to ship table

Aggregation and matching logic on ship to ship table.

## Identifiers

| **Table** | **Column** | **Note** |
| --- | --- | --- |
| Berth Visit | Berth Visit 'Berth Visit'[Berth Visit Position] + 1 & IF ( 'Berth Visit'[Berth Visit Position] = 0, "st", IF ( 'Berth Visit'[Berth Visit Position] = 1, "nd", IF ( 'Berth Visit'[Berth Visit Position] = 2, "rd", "th" ) ) ) & " (" & RELATED ( Berth[Berth Name] ) & "- " & RELATED ( Berth[Port] ) & ")" & " (" & FORMAT ( [Berth Start Datetime], "mmm d hh:mm" ) & "-" & FORMAT ( [Berth End Datetime], "mmm d hh:mm" ) & ")" |  |
| Terminal Visit | Terminal Visit Identifier 'Berth Visit'[Terminal Visit.terminal\_visit\_position] + 1 & IF('Berth Visit'[Terminal Visit.terminal\_visit\_position] = 0, "st", IF('Berth Visit'[Terminal Visit.terminal\_visit\_position] = 1, "nd", IF('Berth Visit'[Terminal Visit.terminal\_visit\_position] = 2, "rd","th" ) ) ) & " (" & RELATED(Berth[Terminal Name]) & "- " & RELATED(Berth[Port]) & ")" // & " (" & // FORMAT('Berth Visit'[Terminal Visit.start\_timestamp], "mmm d hh:mm") & "-" & // FORMAT('Berth Visit'[Terminal Visit.end\_timestamp], "mmm d hh:mm") & ")" |  |
| Port Visit | Visit Identifier -- Formatting logic VAR StartDateTime = 'Berth Visit'[pilot\_onboard\_timestamp] VAR EndDateTime = [pilot\_disembarked\_outbound\_date] -- Extract date and time components VAR StartYear = YEAR(StartDateTime) VAR EndYear = YEAR(EndDateTime) VAR StartMonth = FORMAT(StartDateTime, "MMM") VAR EndMonth = FORMAT(EndDateTime, "MMM") VAR StartDay = DAY(StartDateTime) VAR EndDay = DAY(EndDateTime) -- Formatting logic VAR Result = IF ( StartDateTime = EndDateTime, StartMonth & " " & StartDay & ", " & StartYear, IF ( StartYear <> EndYear, StartMonth & " " & StartDay & ", " & StartYear & "-" & EndMonth & " " & EndDay & ", " & EndYear, IF ( StartMonth <> EndMonth, StartMonth & " " & StartDay & "-" & EndMonth & " " & EndDay & ", " & StartYear, IF ( StartDay <> EndDay, StartMonth & " " & StartDay & "-" & EndDay & ", " & StartYear, StartMonth & " " & StartDay & ", " & StartYear ) ) ) ) RETURN RELATED(Ship[Ship Name]) & " (" & Result & ")" |  |

## Data validation

| **Table** | **Column** | **Note** |
| --- | --- | --- |
| Berth | Berth received visitCALCULATE (     COUNTROWS ( 'Berth Visit' ),     FILTER ( 'Berth Visit', 'Berth Visit'[Berth ID] = Berth[ID] ) ) | to filter out those w/o visit |
| Berth Visit | Berth ID found in Berth table 'Berth Visit'[Berth ID] in VALUES(Berth[ID]) | - deleted |
| Berth Visit | Berth and Port visit unlocode matchingOR ( 'Berth Visit'[Port] = 'Berth Visit'[UNLOCODE], 'Berth Visit'[Main Port UNLOCODE] = 'Berth Visit'[UNLOCODE] ) | - deleted |

## Custom histograms

| **Table** | **Column** | **Note** |
| --- | --- | --- |
| Berth Visit | Berth stay duration (4 hr bins lb) | PQ |
| Berth Visit | Moored duration (4 hr bins lb) | PQ |
| Berth Visit | Shifting duration (0.5 hr bins lb) | PQ |
| Berth Visit | Berth stay duration (4 hr bins lb) | PQ |
| Berth Visit | Steaming in duration (0.5 hr bins lb) | PQ |
| Berth Visit | Steaming out duration (0.5 hr bins lb) | PQ |
| Berth Visit | Waiting duration (4 hr bins lb) | PQ |
| Berth Visit | Waiting before arrival duration (4 hr bins lb) | PQ |
| Berth Visit | Waiting during visit duration (4 hr bins lb) | PQ |

Also, corresponding dimension tables that give the user the option to change bin size easily, with custom bin labels.

Example:

## Time zone

For every timestamp field, convert time zone using the following fields:

| **Parameter** | **Explanation** |
| --- | --- |
| WinterTimeUTCDiff | Difference between local time and UTC in winter (hours). |
| SummerTimeUTCDiff | Difference between local time and UTC in summer (hours). |
| WinterTimeStartWeek | Week of the year in which switch to winter time takes place. |
| SummerTimeStartWeek | Week of the year in which switch to summer time takes place. |
| TimeOfDayForTimeSwitch | Time of the day when switch takes place (in corresponding UTC) |

Note that any date and time columns are also recalculated after changing the time zone. Thus, the values in datamart are not used at this point.

## Formatting and other transformations

| **Table** | **Column** | **Note** |
| --- | --- | --- |
| Berth | Berth Type let berthType = Text.Replace(  Text.Replace(  Text.Replace([#"Berth Type (original)"],  ",OTHER", ""),  "OTHER,", ""),  "WET", "LIQUID") in Text.Replace(Text.Proper(berthType), "bulk", " Bulk") | PQ |
| Berth | Length (ft) [#"Length (m)"]\* 3.2808399 | PQ. could be a parameter |
| Berth | Terminal Owner (POCCA/Private) if [Terminal Owner]="POCCA" then "Public" else "Private" | PQ. |
| Berth | Berth Name let longName= [#"Berth Name (long)"] in if (longName is null or longName="" or longName="UNKNOWN") then [#"Berth Name (short)"] else longName | PQ |
| Berth Visit | Previous Port let prevPort = [Port Visit.prev\_port\_unlocode] in  if prevPort is null then [port\_unlocode] else prevPort | PQ |
| Port Visit | BunkeringVAR visitID='Berth Visit'[Visit ID] VAR bunkerCount = CALCULATE(     COUNTROWS('Bunkering Activities'),     FILTER(ALL('Bunkering Activities'), 'Bunkering Activities'[Visit ID]=visitID) ) RETURN IF(bunkerCount>0, "Bunkered", "-") |  |
| Port Visit | Port Rotation Type IF ( 'Berth Visit'[# Berth Visits in Port] = 1, "1 Berth Visited", "Multiple Berths Visited" ) |  |
| Terminal | name #"Replaced Value","\_"," ",Replacer.ReplaceText,{"name"} | transformation |
| Terminal | name\_with\_port #"Replaced Value","\_"," ",Replacer.ReplaceText,{"name\_with\_port"} | transformation |
| Port | display\_name {"display\_name", Text.Proper, type text} | transformation (Capitalize each word) |
| Port | main\_port let mainPort = [main\_port] in if mainPort is null then [unlocode] else mainPort | transformation. if main port field is empty, fill with unlocode. |
| Port | Main Port Latitude `Main Port Latitude = LOOKUPVALUE(Port[Latitude], Port[UNLOCODE], Port[Main Port UNLOCODE])` | Builds on main\_port |
| Port | Main Port Longitude `Main Port Longitude = LOOKUPVALUE(Port[Longitude], Port[UNLOCODE], Port[Main Port UNLOCODE])` | Builds on main\_port |
| Port | GroupVAR cluster1 = "Texas Energy Ports" VAR cluster2 = "Atlantic Gateway Ports" VAR cluster3 = "Mississippi River Ports" RETURN     IF(Port[Main Port UNLOCODE]="USHOU", cluster1,     IF(Port[Main Port UNLOCODE]="USCRP", cluster1,     IF(Port[Main Port UNLOCODE]="USBPT", cluster1,     IF(Port[Main Port UNLOCODE]="USNYC", cluster2,     IF(Port[Main Port UNLOCODE]="USSAV", cluster2,     IF(Port[Main Port UNLOCODE]="USLUA", cluster3,     IF(Port[Main Port UNLOCODE]="USMSY", cluster3,     IF(Port[Main Port UNLOCODE]="USPLQ", cluster3,     IF(Port[Main Port UNLOCODE]="USBTR", cluster3,     BLANK()         ))))))))) | Used for benchmarking. should stay in PBI |
| Port | Port NameVAR PortName = LOOKUPVALUE(Port[Port Name (Detailed)], Port[UNLOCODE], Port[Main Port UNLOCODE]) RETURN IF(PortName="Port Of Houston", "Port Houston", IF(PortName="Baton Rouge La", "Port of Greater Baton Rouge", IF(PortName="Beaumont Tx", "Port of Beaumont", IF(PortName="South Louisiana", "Port of South Louisiana", IF(PortName="Port of New York", "Port of New York and New Jersey", IF(PortName="Port of Plaquemines", "Louisiana Gateway Port", SUBSTITUTE(PortName, " Of ", " of ") )))))) | official names of some ports are fixed in this column. should be in POMA instead. |
| Ship | dry\_bulk\_category Dry Bulk Category Capitalized Each Word  Dry Bulk Category Replaced \_ |  |
| Ship | wet\_bulk\_category Liquid Bulk Category Capitalized Each Word  Liquid Bulk Category Replaced \_ |  |
| Ship | ship\_category Ship Category Capitalized Each Word  Ship Category Replaced \_ |  |
| Ship | Ship ClassificationVAR beam = Ship[Beam] RETURN IF(     Ship[Ship Type] = "Tanker",     IF(beam=0, "LB: Unknown Size",     IF(beam<=32.3, "LB: 1) Panamax",     IF(beam<=47.2, "LB: 2) Aframax",     IF(beam<=53, "LB: 3) Suezmax",     "LB: 4) VLCC")))),     Ship[Ship Type] ) | to correspond to POCCA’s definition |
| Ship | Ship Size Class Lower Bound (DWT)Ship Size Class Lower Bound (DWT) = VAR classSize = 50000 VAR shipSizeCorrected = IF(OR(Ship[DWT]>600000, ISBLANK(Ship[DWT])), 50000, Ship[DWT]) VAR lowerBound = int(shipSizeCorrected/classSize)\*classSize RETURN lowerBound |  |
| Ship | Ship Size Class (DWT) Ship Size Class (DWT) = VAR classSize = 50000 VAR shipSizeCorrected = IF(OR(Ship[DWT]>600000, ISBLANK(Ship[DWT])), 50000, Ship[DWT]) VAR lowerBound = int(shipSizeCorrected/classSize)\*classSize VAR upperBound = lowerBound + classSize VAR numberFormat = "#,0,.0#K" RETURN lowerBound/1000 & "-" & upperBound/1000 & "K tonnes" |  |

## Waiting experience

| **Table** | **Column** | **Note** |
| --- | --- | --- |
| Port Visit | Waiting During Visit % [Port Visit.total\_waiting\_time\_during\_visit] > waitingCutoff | If waiting in is higher than a certain threshold (4 hours by default) |
|  | Waiting Before Arrival % [Port Visit.total\_waiting\_time\_before\_arrival]>waitingCutoff | PQ |
| Port Visit | Waiting % [#"Waiting Duration"]>waitingCutoff | PQ |
| Port Visit | Waiting Experience if [#"Waiting Before Arrival %"]=false and [#"Waiting During Visit %"]=false  then  "Did not wait (waiting<=" & Text.From(waitingCutoff) & "hr)"  else  if [#"Waiting Before Arrival %"] and [#"Waiting During Visit %"]  then "Waited both before arrival & during visit"  else  if [#"Waiting Before Arrival %"]  then "Waited before arrival" else  "Waited during visit" | PQ. |

## Additional information

| **Table** | **Column** | **Note** |
| --- | --- | --- |
| Berth Visit | Berth occupancy at EOS VAR eosEntry = 'Berth Visit'[eos\_entry] VAR eosEntryTrimmed = DATEVALUE ( eosEntry ) + TIME ( HOUR ( eosEntry ), 0, 0 ) VAR berthOcc = CALCULATE ( [Berth Occupancy at time for selected berth visit], Weather[Date (UTC)] = eosEntryTrimmed ) RETURN IF ( berthOcc > 0, "Berth occupied at time of arrival", "Berth available at time of arrival" ) |  |
| Port Visit | Timeline Link ColumnVAR eosEntryDateTime = [EOS Entry Datetime] VAR anchorDownDateTime = [Anchor Down Datetime] VAR pilotOnboardTime = [Pilot Onboard Datetime] VAR pilotDisembarkedTime = [Pilot Disembarked Datetime] VAR vesselIMO = LOOKUPVALUE(Ship[IMO], Ship[Ship ID], 'Berth Visit'[Ship ID]) VAR beginningDate = IF( YEAR(eosEntryDateTime)>2010, eosEntryDateTime, IF(YEAR(anchorDownDateTime)>2010, anchorDownDateTime, pilotOnboardTime)) VAR beginningFormatted = FORMAT(beginningDate, "yyyy-mm-ddThh%3Ann") & "%3A00.000Z" VAR endingDate = pilotDisembarkedTime VAR endingFormatted = FORMAT(endingDate, "yyyy-mm-ddThh%3Ann") & "%3A00.000Z" RETURN [Timeline basis URL] & vesselIMO & "?start=" & beginningFormatted & "&end=" & endingFormatted |  |
| Port Visit | VesselVoyage Link Column "https://vesselvoyage.teqplay.nl/#/ships/" & LOOKUPVALUE ( Ship[IMO], Ship[Ship ID], 'Berth Visit'[Ship ID] ) & "/story/" & 'Berth Visit'[Visit ID] |  |
|  |  |  |

---

# Other ideas

* Might be interesting to have the ability to calculate the Gantt chart in datamart.

Gantt chart760Gantt chart =
VAR WIDTH = 700
VAR DistanceRequired = 30
VAR SelectedVisit = SELECTEDVALUE('Berth Visit'[Visit ID])
VAR CountBerthVisits = SELECTEDVALUE('Berth Visit'[Terminal Visit.terminal\_total\_berth\_visit])
VAR DateFormat = "mmm d" -- "dd/mm/yyyy"
VAR fontFamily = "Segoe UI"
-- The values that are once per visit
VAR PrevPort = SELECTEDVALUE('Berth Visit'[Previous Port])
VAR POB = [Pilot Onboard Datetime]
VAR PD = [Pilot Disembarked Datetime]
VAR AnchorDown = [Anchor Down Datetime]
VAR AnchorUp = [Anchor Up Datetime]
VAR EOSEntry = [EOS Entry Datetime]
VAR EOSExit = [EOS Exit Datetime]
VAR FirstPoint = IF(YEAR(EOSEntry)>2010, EOSEntry, IF(YEAR(AnchorDown)>2010, AnchorDown, POB))
VAR LastPoint = [EOS Exit Datetime]
VAR DistanceFirstLast = LastPoint-FirstPoint
VAR colorBunker = [Color: Sunset]
VAR colorSTS = "#FFC800"
VAR colorSTSLighter = "#FFF1BF"
VAR colorTug = "#65DBBE"
VAR colorAnchor = "#081957"
-- The values that are once per visit
VAR BerthVisitsOfPortVisit = ADDCOLUMNS(
    FILTER('Berth Visit', 'Berth Visit'[Visit ID]=SelectedVisit),
    "Berth Stay",
    "<rect id='track' x='"& WIDTH\*([Berth Start Datetime]-FirstPoint)/(DistanceFirstLast) &"' y='2' width='"&
    WIDTH\*([Berth End Datetime]-[Berth Start Datetime])/(DistanceFirstLast) &"' height='18' fill='" & IF('Berth Visit'[Is Cargo Operation], "#4FA0D7", "#081957") & "'/>",
    "Berth Start",
    IF(
        WIDTH\*([Berth End Datetime]-[Berth Start Datetime])/(DistanceFirstLast)>DistanceRequired,
        -- Normal case where we have space to write it regularly
        "<rect id='marker' x='"& WIDTH\*([Berth Start Datetime]-FirstPoint)/(DistanceFirstLast) &"' y='"& -5 + 10\* MOD('Berth Visit'[Berth Visit Position], 2) &"' width='2' height='20' fill='" & IF('Berth Visit'[Is Cargo Operation], "#4FA0D7", "#081957") & "'></rect>" &
        "<text x='"& WIDTH\*([Berth Start Datetime]-FirstPoint)/(DistanceFirstLast) &"' y='"& -18 + 52\* MOD('Berth Visit'[Berth Visit Position], 2) &"' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& FORMAT([Berth Start Datetime], DateFormat)&"</text> " &
        "<text x='"& WIDTH\*([Berth Start Datetime]-FirstPoint)/(DistanceFirstLast) &"' y='"& -8 + 52\* MOD('Berth Visit'[Berth Visit Position], 2) &"' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& FORMAT([Berth Start Datetime], "hh:mm")&"</text> ",
        -- Case where we need to shift up the Berth Visit Start to eliminate overlapping text
        "<rect id='marker' x='"& WIDTH\*([Berth Start Datetime]-FirstPoint)/(DistanceFirstLast) &"' y='"& -25 + 30\* MOD('Berth Visit'[Berth Visit Position], 2) &"' width='2' height='40' fill='" & IF('Berth Visit'[Is Cargo Operation], "#4FA0D7", "#081957") & "'></rect>" &
        "<text x='"& WIDTH\*([Berth Start Datetime]-FirstPoint)/(DistanceFirstLast) &"' y='"& -38 + 92\* MOD('Berth Visit'[Berth Visit Position], 2) &"' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& FORMAT([Berth Start Datetime], DateFormat)&"</text> " &
        "<text x='"& WIDTH\*([Berth Start Datetime]-FirstPoint)/(DistanceFirstLast) &"' y='"& -28 + 92\* MOD('Berth Visit'[Berth Visit Position], 2) &"' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& FORMAT([Berth Start Datetime], "hh:mm")&"</text> "
    )
   
    ,
    "Berth End",
    "<rect id='marker' x='"& WIDTH\*([Berth End Datetime]-FirstPoint)/(DistanceFirstLast) - 2 &"' y='"& -5 + 10\* MOD('Berth Visit'[Berth Visit Position], 2) &"' width='2' height='20' fill='" & IF('Berth Visit'[Is Cargo Operation], "#4FA0D7", "#081957") & "'></rect>" &
    "<text x='"& WIDTH\*([Berth End Datetime]-FirstPoint)/(DistanceFirstLast) &"' y='"& -18 + 52\* MOD('Berth Visit'[Berth Visit Position], 2) &"' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& FORMAT([Berth End Datetime], DateFormat)&"</text> " &
    "<text x='"& WIDTH\*([Berth End Datetime]-FirstPoint)/(DistanceFirstLast) &"' y='"& -8 + 52\* MOD('Berth Visit'[Berth Visit Position], 2) &"' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& FORMAT([Berth End Datetime], "hh:mm")&"</text> "
    )
-- From anchorage activities table
VAR AnchorageOfPortVisit = ADDCOLUMNS(
    FILTER('Anchorage activities', 'Anchorage Activities'[Visit ID]=SelectedVisit),
    "Anchorage",
    "<rect id='track' x='"& WIDTH\*([Anchorage Start Datetime]-FirstPoint)/(DistanceFirstLast) &"' y='2' width='"& WIDTH\*([Anchorage End Datetime]-[Anchorage Start Datetime])/(DistanceFirstLast) &"' height='18' fill='" & colorAnchor & "'/>" &
    -- Anchor Down
    "<rect id='marker' x='"& WIDTH\*([Anchorage Start Datetime]-FirstPoint)/(DistanceFirstLast) &"' y='1' width='2' height='20' fill='" & colorAnchor & "'></rect>" &
    -- Anchor Up
    "<rect id='marker' x='"& WIDTH\*([Anchorage End Datetime]-FirstPoint)/(DistanceFirstLast) &"' y='1' width='2' height='20' fill='" & colorAnchor & "'></rect>" &
    IF(
        OR(
        FORMAT([Anchorage Start Datetime], DateFormat) = FORMAT([Anchorage End Datetime], DateFormat),
        WIDTH\*([Anchorage End Datetime]-[Anchorage Start Datetime])/(DistanceFirstLast)<100
        )
        ,
    "<text x='"& WIDTH\*(([Anchorage Start Datetime]+[Anchorage End Datetime])/2-FirstPoint)/(DistanceFirstLast) &"' y='-8' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& "⚓" &"</text> "
    ,
    "<text x='"& WIDTH\*(([Anchorage Start Datetime]+[Anchorage End Datetime])/2-FirstPoint)/(DistanceFirstLast) &"' y='-28' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& "Anchorage" &"</text> " &
    "<text x='"& WIDTH\*(([Anchorage Start Datetime]+[Anchorage End Datetime])/2-FirstPoint)/(DistanceFirstLast) &"' y='-18' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& FORMAT([Anchorage Start Datetime], DateFormat & ", hh:mm -")&"</text> " &
    "<text x='"& WIDTH\*(([Anchorage Start Datetime]+[Anchorage End Datetime])/2-FirstPoint)/(DistanceFirstLast) &"' y='-8' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& FORMAT([Anchorage End Datetime], DateFormat & ", hh:mm")&"</text> "
    )
)
-- From fact\_bunkering table
VAR BunkersOfPortVisit = ADDCOLUMNS(
    FILTER('Bunkering Activities', 'Bunkering Activities'[Visit ID]=SelectedVisit),
    "Bunker",
    "<rect id='track' x='"& WIDTH\*([Bunkering Start Datetime]-FirstPoint)/(DistanceFirstLast) &"' y='-14' width='"&
    WIDTH\*([Bunkering End Datetime]-[Bunkering Start Datetime])/(DistanceFirstLast) &"' height='16' fill='" & colorBunker & "'/>" &
    "<text x='"& WIDTH\*(([Bunkering Start Datetime] + [Bunkering End Datetime] )/2-FirstPoint)/(DistanceFirstLast) &"' y='-18' font-family='" & fontFamily & "' font-size= 'xx-small' fill='" & colorBunker & "' text-anchor='left'>"& [Selected Service Vessel Name] &"</text> "
    )
-- From fact\_tug table
VAR TugsIfPortVisit = ADDCOLUMNS(
    FILTER('Towage Activities', 'Towage Activities'[Visit ID]=SelectedVisit),
    "Tug",
    "<rect id='track' x='"& WIDTH\*([Towage Start Datetime]-FirstPoint)/(DistanceFirstLast) &"' y='-6' width='"&
    WIDTH\*([Towage End Datetime]-[Towage Start Datetime])/(DistanceFirstLast) &"' height='8' fill='" & colorTug & "'/>"
    // "<text x='"& WIDTH\*([First start date of Ship to Ship]-FirstPoint)/(DistanceFirstLast) &"' y='-12' font-family='" & fontFamily & "' font-size= 'xx-small' fill='" & colorTug & "' text-anchor='left'>"& IF('Ship to Ship'[First ship\_to\_ship\_encounter]>0, 'Ship to Ship'[ship\_name], "") &"</text> "
    )
-- From ship to ship table
VAR stsOfPortVisit = ADDCOLUMNS(
    FILTER(ALL('Ship to Ship'), 'Ship to Ship'[visit\_id]=SelectedVisit),
    "STS",
    "<rect id='track' x='"& WIDTH\*([First start date of Ship to Ship]-FirstPoint)/(DistanceFirstLast) &"' y='-6' width='"&
    WIDTH\*([Last end date of Ship to Ship]-[First start date of Ship to Ship])/(DistanceFirstLast) &"' height='8'  style='fill:" & colorSTSLighter & "'/>" &
    "<text x='"& WIDTH\*([First start date of Ship to Ship]-FirstPoint)/(DistanceFirstLast) &"' y='-12' font-family='" & fontFamily & "' font-size= 'xx-small' fill='" & colorSTSLighter & "' text-anchor='left'>"& IF('Ship to Ship'[First ship\_to\_ship\_encounter]>0, 'Ship to Ship'[ship\_name], "") &"</text> "
    )
VAR SelectedSTSOfPortVisit = ADDCOLUMNS(
    FILTER('Ship to Ship', 'Ship to Ship'[visit\_id]=SelectedVisit),
    "STS",
    "<rect id='track' x='"& WIDTH\*([First start date of Ship to Ship]-FirstPoint)/(DistanceFirstLast) &"' y='-6' width='"&
    WIDTH\*([Last end date of Ship to Ship]-[First start date of Ship to Ship])/(DistanceFirstLast) &"' height='8' fill='" & colorSTS & "'/>" &
    "<text x='"& WIDTH\*([First start date of Ship to Ship]-FirstPoint)/(DistanceFirstLast) &"' y='-12' font-family='" & fontFamily & "' font-size= 'xx-small' fill='" & colorSTS & "' text-anchor='left'>"& IF('Ship to Ship'[First ship\_to\_ship\_encounter]>0, 'Ship to Ship'[ship\_name], "") &"</text> "
    )
VAR ConcatenatedBerthStay = CONCATENATEX(BerthVisitsOfPortVisit, [Berth Stay], " ")
VAR ConcatenatedBerthVisitStart = CONCATENATEX(BerthVisitsOfPortVisit, [Berth Start], " ")
VAR ConcatenatedBerthVisitEnd = CONCATENATEX(BerthVisitsOfPortVisit, [Berth End], " ")
VAR ConcatenatedAnchorage = CONCATENATEX(AnchorageOfPortVisit, [Anchorage], " ")
VAR ConcatenatedTugArrival= CONCATENATEX(TugsIfPortVisit, [Tug], " ")
VAR ConcatenatedBunkers= CONCATENATEX(BunkersOfPortVisit, [Bunker], " ")
VAR ConcatenatedSTS = CONCATENATEX(stsOfPortVisit, [STS], " ")
VAR ConcatenatedSelectedSTS = CONCATENATEX(SelectedSTSOfPortVisit, [STS], " ")
// VAR ConcatenatedBunkerArrival = CONCATENATEX(TerminalVisitsOfPortVisit, [Arrival Bunker], " ")
RETURN
IF(HASONEVALUE('Berth Visit'[Visit Identifier]),
"data:image/svg+xml;utf8," &
    "<svg width='"& WIDTH & "' height='"& WIDTH/3 &"' viewBox='-40 -50 " & WIDTH+70 & " "& WIDTH/3 &"' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' overflow='visible'>
        <text x='-20' y='10' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& PrevPort &"</text>
        <text x='-20' y='20' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& "🡢" &"</text>
        <rect id='track' x='0' y='2' width='"&WIDTH&"' height='18' fill='#B9D9EF'/>" &
       
        -- If EOS entry date is found
        if(YEAR(EOSEntry)>2010,
        "<rect id='marker' x='0' y='1' width='2' height='20' fill='#081957'></rect>" &
        "<text x='0' y='30' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& "EOS" &"</text> " &
        "<text x='0' y='40' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& FORMAT(EOSEntry, DateFormat)&"</text> " &
        "<text x='0' y='50' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& FORMAT(EOSEntry, "hh:mm")&"</text> "
        , "") &
        -- If EOS exit date is found
        if(YEAR(EOSExit)>2010,
        "<rect id='marker' x='"&WIDTH&"' y='1' width='2' height='20' fill='#081957'></rect>" &
        "<text x='"&WIDTH&"' y='30' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& "EOS" &"</text> " &
        "<text x='"&WIDTH&"' y='40' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& FORMAT(EOSExit, DateFormat)&"</text> " &
        "<text x='"&WIDTH&"' y='50' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& FORMAT(EOSExit, "hh:mm")&"</text> "
        , "") &
        -- Pilot onboard
        IF(
            AND(AND(WIDTH\*(POB-AnchorUp)/(DistanceFirstLast)> DistanceRequired, WIDTH\*(POB-[EOS Entry Datetime])/(DistanceFirstLast)> DistanceRequired), TRUE()), -- WIDTH\*(FirstBerthVisitStart-POB)/(DistanceFirstLast)> DistanceRequired
            "<rect id='marker' x='"& WIDTH\*(POB-FirstPoint)/(DistanceFirstLast) &"' y='1' width='2' height='20' fill='#36407E'></rect>" &
            "<text x='"& WIDTH\*(POB-FirstPoint)/(DistanceFirstLast) &"' y='30' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& "POB" &"</text> " &
            "<text x='"& WIDTH\*(POB-FirstPoint)/(DistanceFirstLast) &"' y='40' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& FORMAT(POB, DateFormat)&"</text> " &
            "<text x='"& WIDTH\*(POB-FirstPoint)/(DistanceFirstLast) &"' y='50' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& FORMAT(POB, "hh:mm")&"</text> ",
            "<rect id='marker' x='"& WIDTH\*(POB-FirstPoint)/(DistanceFirstLast) &"' y='1' width='2' height='47' fill='#36407E'></rect>" &
            "<text x='"& WIDTH\*(POB-FirstPoint)/(DistanceFirstLast) &"' y='60' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& "POB" &"</text> " &
            "<text x='"& WIDTH\*(POB-FirstPoint)/(DistanceFirstLast) &"' y='70' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& FORMAT(POB, DateFormat)&"</text> " &
            "<text x='"& WIDTH\*(POB-FirstPoint)/(DistanceFirstLast) &"' y='80' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& FORMAT(POB, "hh:mm")&"</text> "
        )
        &
        ConcatenatedBerthStay & ConcatenatedAnchorage & ConcatenatedTugArrival & ConcatenatedBerthVisitStart & ConcatenatedBerthVisitEnd & ConcatenatedBunkers &
        ConcatenatedSTS & ConcatenatedSelectedSTS &
        -- Pilot disembarked CountBerthVisits
        "<rect id='marker' x='"& WIDTH\*(PD-FirstPoint)/(DistanceFirstLast) &"' y='1' width='2' height='20' fill='#36407E'></rect>" &
        "<text x='"& WIDTH\*(PD-FirstPoint)/(DistanceFirstLast) &"' y='" & -24 + 54\* MOD(CountBerthVisits, 2) & "' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& "PDK" &"</text> " &
        "<text x='"& WIDTH\*(PD-FirstPoint)/(DistanceFirstLast) &"' y='" & -14 + 54\* MOD(CountBerthVisits, 2) & "' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& FORMAT(PD, DateFormat)&"</text> " &
        "<text x='"& WIDTH\*(PD-FirstPoint)/(DistanceFirstLast) &"' y='" & -4 + 54\* MOD(CountBerthVisits, 2) & "' font-family='" & fontFamily & "' font-size= 'xx-small' text-anchor='middle'>"& FORMAT(PD, "hh:mm")&"</text> " &
    "</svg>", BLANK())

* For the time values, it is actually sufficient to have the detail on minute level, seconds are not necessary. This could help with data size (Time table, values in fact tables)
* [Relationship between port and other fact tables](https://teqplaybv.atlassian.net/browse/PTO-2354) are worth discussing.
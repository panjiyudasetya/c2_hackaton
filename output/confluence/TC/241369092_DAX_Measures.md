---
id: confluence:241369092
source: confluence
type: page
space: TC
title: DAX Measures
author: Yaren Aslan
date: '2023-12-13'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/241369092
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/241369092
---
# DAX Measures

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/241369092  

## Content

*To be completed.*

| **Home Table** | **Measure** | **Description** |
| --- | --- | --- |
| Berth | Sum of Moves Sum of Moves = SUMX (  'Berth',  CALCULATE (  SUM ( Moves[Moves] ),  FILTER ( ALLSELECTED ( 'Berth Visit' ), 'Berth'[ID] = 'Berth Visit'[Berth ID] )  ) ) | Sum of moves for the selected berth. |
| Berth Visit | # All Berth Visits Competition # All Berth Visits Competition =  VAR \_SelectedTerminal = [Selected Terminal] VAR \_CountAll =  CALCULATE (  IF ( ISEMPTY ( 'Berth Visit' ), 0, COUNTROWS ( 'Berth Visit' ) ),  FILTER ( 'Port Visit', [Is Shown] > 0 )  ) RETURN  COUNTX (  FILTER (  ALLSELECTED ( 'Berth Visit' ),  'Berth Visit'[Terminal Name] <> \_SelectedTerminal  ),  \_CountAll  ) | Returns the number of all selected berth visits of the competition. Used for % calculation. |
| Berth Visit | # All Berth Visits Focus # All Berth Visits Focus =  VAR \_SelectedTerminal = [Selected Terminal] VAR \_CountAll =  CALCULATE (  IF ( ISEMPTY ( 'Berth Visit' ), 0, COUNTROWS ( 'Berth Visit' ) ),  FILTER ( 'Port Visit', [Is Shown] > 0 )  ) RETURN  COUNTX (  FILTER (  ALLSELECTED ( 'Berth Visit' ),  'Berth Visit'[Terminal Name] = \_SelectedTerminal  ),  \_CountAll  ) | Same formulation as # All Berth Visits Competition except requiring Terminal Name to be equal to Selected Terminal instead of the opposite. |
| Berth Visit | # Berth Visits Competition # Berth Visits Competition =  VAR \_SelectedTerminal = [Selected Terminal] VAR \_CountAll =  CALCULATE (  IF ( ISEMPTY ( 'Berth Visit' ), 0, COUNTROWS ( 'Berth Visit' ) ),  FILTER ( 'Port Visit', [Is Shown] > 0 ),  FILTER ( 'Berth Visit', 'Berth Visit'[Terminal Name] <> \_SelectedTerminal )  ) RETURN  \_CountAll | Returns the number of berth visits of the competition for given context filters. For instance, per container category, moves count. |
| Berth Visit | # Berth Visits Focus # Berth Visits Focus =  VAR \_SelectedTerminal = [Selected Terminal] VAR \_CountAll =  CALCULATE (  IF ( ISEMPTY ( 'Berth Visit' ), 0, COUNTROWS ( 'Berth Visit' ) ),  FILTER ( 'Port Visit', [Is Shown] > 0 ),  FILTER ( 'Berth Visit', 'Berth Visit'[Terminal Name] = \_SelectedTerminal )  ) RETURN  \_CountAll | Same formulation as # Berth Visits Competition except requiring Terminal Name to be equal to Selected Terminal instead of the opposite. |
| Berth Visit | # Berth Visits in Scope # Berth Visits in Scope =  VAR \_CountAll =  CALCULATE (  IF ( ISEMPTY ( 'Berth Visit' ), 0, COUNTROWS ( 'Berth Visit' ) ),  FILTER ( 'Port Visit', [Is Shown] > 0 )  ) RETURN  \_CountAll | Same formulation as # Berth Visits Competition except not having any requirement for Terminal Name. |
| Berth Visit | % Berth Visits Competition % Berth Visits Competition = DIVIDE ( [# Berth Visits Competition], [# All Berth Visits Competition] ) | # Berth Visits Competition/ # All Berth Visits Competition |
| Berth Visit | % Berth Visits Focus % Berth Visits Focus = DIVIDE ( [# Berth Visits Focus], [# All Berth Visits Focus] ) | # Berth Visits Focus/ # All Berth Visits Focus |
| Berth Visit | Avg. Berth Stay (hrs) Avg. Berth Stay (hrs) = CALCULATE (  AVERAGE ( 'Berth Visit'[Berth Stay Duration] ),  FILTER ( 'Port Visit', [Is Shown] > 0 ),  FILTER ( 'Port Visit', [Port Visit in Scope] > 0 ) ) | Returns average of Berth Stay Duration for Port Visits in scope. |
| Berth Visit | Avg. Berth Stay Competition Avg. Berth Stay Competition = VAR \_SelectedTerminal = [Selected Terminal] RETURN  CALCULATE (  AVERAGE ( 'Berth Visit'[Berth Stay Duration] ),  FILTER ( 'Port Visit', [Is Shown] > 0 ),  FILTER ( 'Berth Visit', 'Berth Visit'[Terminal Name] <> \_SelectedTerminal )  ) | Returns average of Berth Stay Duration for Berth Visits for competition (the cases where Terminal Name is not equal to the selected terminal). |
| Berth Visit | Avg. Berth Stay Focus Avg. Berth Stay Focus = VAR \_SelectedTerminal = [Selected Terminal] RETURN  CALCULATE (  AVERAGE ( 'Berth Visit'[Berth Stay Duration] ),  FILTER ( 'Port Visit', [Is Shown] > 0 ),  FILTER ( 'Berth Visit', 'Berth Visit'[Terminal Name] = \_SelectedTerminal )  ) | Returns average of Berth Stay Duration for Berth Visits for the focus terminal (the cases where Terminal Name is equal to the selected terminal). |
| Berth Visit | Avg. Moves Avg. Moves = CALCULATE (  AVERAGE ( Moves[Moves] ),  FILTER ( 'Port Visit', [Is Shown] > 0 ),  FILTER ( 'Port Visit', [Port Visit in Scope] > 0 ) ) | Average of moves for the cases where the port visit is shown and is within scope. |
| Berth Visit | Avg. Moves Competition Avg. Moves Competition = VAR \_SelectedTerminal = [Selected Terminal] RETURN  CALCULATE (  AVERAGE ( Moves[Moves] ),  FILTER ( 'Port Visit', [Is Shown] > 0 ),  FILTER ( 'Berth Visit', 'Berth Visit'[Terminal Name] <> \_SelectedTerminal )  ) | Average of moves for the cases where the port visit is shown and Berth Visit is of competition (the cases where Terminal Name is not equal to the selected terminal). |
| Berth Visit | Avg. Moves Focus Avg. Moves Focus = VAR \_SelectedTerminal = [Selected Terminal] RETURN  CALCULATE (  AVERAGE ( Moves[Moves] ),  FILTER ( 'Port Visit', [Is Shown] > 0 ),  FILTER ( 'Berth Visit', 'Berth Visit'[Terminal Name] = \_SelectedTerminal )  ) | Average of moves for the cases where the port visit is shown and Berth Visit is of focus (the cases where Terminal Name is equal to the selected terminal). |
| Berth Visit | Avg. Productivity (Moves/hrs) Avg. Productivity (Moves/hrs) = DIVIDE ( [Avg. Moves], [Avg. Berth Stay (hrs)] ) | [Avg. Moves] / [Avg. Berth Stay (hrs)] |
| Berth Visit | Avg. Productivity Competition (Moves/hrs) Avg. Productivity Competition (Moves/hrs) = DIVIDE ( [Avg. Moves Competition], [Avg. Berth Stay Competition] ) | [Avg. Moves Competition] / [Avg. Berth Stay Competition] |
| Berth Visit | Avg. Productivity Focus (Moves/hrs) Avg. Productivity Focus (Moves/hrs) = DIVIDE ( [Avg. Moves Focus], [Avg. Berth Stay Focus] ) | [Avg. Moves Focus] / [Avg. Berth Stay Focus] |
| Berth Visit | Note on Shown Berth Values Note on Shown Berth Values = VAR CountWithMoves =  CALCULATE (  IF ( ISEMPTY ( Moves ), 0, COUNTROWS ( Moves ) ),  FILTER ( 'Port Visit', [Is Shown] > 0 )  ) VAR CountShown =  CALCULATE (  IF ( ISEMPTY ( Moves ), 0, COUNTROWS ( 'Berth Visit' ) ),  FILTER ( 'Port Visit', [Is Shown] > 0 )  ) VAR CountAll =  IF ( ISEMPTY ( Moves ), 0, COUNTROWS ( 'Berth Visit' ) ) RETURN  IF (  SELECTEDVALUE ( 'Shown Values'[Shown Values] ) = "All",  "All " & FORMAT ( CountAll, "0" ) & " berth visits are shown",  FORMAT ( CountShown, "0" ) & " out of "  & FORMAT ( CountAll, "0" ) & " berth visits are shown"  ) & " from " & [Date Range] & ". "  & IF ( CountWithMoves = CountShown, "All", FORMAT ( CountWithMoves, "0" ) ) & " have moves associated. All dates and times are in UTC." | Note to be displayed on the upper right corner of the Cargo-Ops page. Gives information about number of berth visits shown, number of moves associated. |
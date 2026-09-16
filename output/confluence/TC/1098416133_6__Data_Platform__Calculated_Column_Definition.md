---
id: confluence:1098416133
source: confluence
type: page
space: TC
title: '6. Data Platform: Calculated Column Definition'
author: Ryan Kharisma Rakhmat
date: '2026-02-12'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1098416133
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1098416133
---
# 6. Data Platform: Calculated Column Definition

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1098416133  

## Content

Use this template to define, validate, and govern calculated columns across your data platforms. Keep sections concise and link to sources and specs where applicable.

## Purpose

Summarise why this calculated column exists and what business question it answers. Include key stakeholders and expected usage contexts.

1. **Performance Analytics in Port**

For the analytical purposes we are setting up some metric to calculate the performance of the ports. In short we are focus on the six metric as described below:

* **Moored** - Time vessels spend tied up at berths performing cargo operations or waiting
* **Shifting** - Time vessels spend moving between different berths or terminals within the port
* **Steaming In** - Time vessels spend traveling from the Pilot Onboard to their first berth
* **Steaming Out** - Time vessels spend traveling from their last berth to the Pilot Disembarked
* **Wait During Visit** - Time vessels spend waiting (anchored or slow-moving) while between Pilot Onboard and Pilot Disembarked
* **Wait Before Arrival** - Time vessels spend waiting (anchored or slow-moving) outside the port before getting the pilot onboard

The `metric_type` columns are contains the name of the metric then we are focusing on the calculations of the `average_value` and `standard_deviation` value.

### Source Mapping

List all upstream sources and also the formula of the calculations.

| **Source table [field(s)]** | **Metric** | **Average** | **Standard Deviation** |
| --- | --- | --- | --- |
| **fact\_port\_visit** [total\_moored\_duration] | **Moored** | AVG(*total\_moored\_duration*) | STDDEV(*total\_moored\_duration*) |
| **fact\_port\_visit** [shifting\_between\_terminals\_duration, shifting\_inside\_terminals\_duration] | **Shifting** | AVG(*shifting\_between\_terminals\_duration **+** shifting\_inside\_terminals\_duration*) | STDDEV(*shifting\_between\_terminals\_duration **+** shifting\_inside\_terminals\_duration*) |
| **fact\_port\_visit** [port\_inbound\_travel\_duration] | **Steaming In** | AVG(*port\_inbound\_travel\_duration*) | STDDEV(*port\_inbound\_travel\_duration*) |
| **fact\_port\_visit** [port\_outbound\_travel\_duration] | **Steaming Out** | AVG(*port\_outbound\_travel\_duration*) | STDDEV(*port\_outbound\_travel\_duration*) |
| **fact\_port\_visit** [during\_visit\_anchor\_duration, total\_slow\_moving\_duration\_inport] | **Wait During Visit** | AVG(*during\_visit\_anchor\_duration **+** total\_slow\_moving\_duration\_inport*) | STDDEV(*during\_visit\_anchor\_duration **+** total\_slow\_moving\_duration\_inport*) |
| **fact\_port\_visit** [before\_visit\_anchor\_duration, total\_slow\_moving\_duration\_arrival] | **Wait Before Arrival** | AVG(*before\_visit\_anchor\_duration* **+** *total\_slow\_moving\_duration\_arrival*) | STDDEV(*before\_visit\_anchor\_duration* + *total\_slow\_moving\_duration\_arrival*) |

2. **Port Visits Calculated Columns**

These metrics describe the **entire port visit** from arrival to departure:

### 1. **Turn Around Time Duration**

**Business Definition:** The total time a vessel spends in the port from arrival to departure. This is the most important metric for measuring overall port efficiency - shorter turnaround times mean vessels can complete more voyages per year.

**Example:** A container ship arrives at 8:00 AM Monday and departs at 2:00 PM Tuesday = 30 hours turnaround time.

---

### 2. **Shifting Duration**

**Business Definition:** The total time a vessel spends moving between different berths or terminals during its port visit. Frequent shifting indicates inefficient berth allocation and increases costs.

**Example:** A bulk carrier moves from Berth 1 to Berth 3, taking 2 hours for the relocation = 2 hours shifting duration. If Berth 1 and Berth 3 are in the same terminal, this is reported as Shifting Inside Terminal. If they are in different terminals, it is reported as Shifting Between Terminals.

---

### 3. **Total Waiting Time Before Arrival**

**Business Definition:** The total time a vessel spends waiting outside the port (anchored or slow-moving) before getting the pilot onboard. Long waiting times indicate port congestion or poor scheduling.

**Example:** A tanker arrives at the End of Seapassage area at 6:00 AM but must wait at anchor until 2:00 PM for berth availability = 8 hours waiting before arrival.

---

### 4. **Outlier Preference**

**Business Definition:** A classification that identifies whether a vessel's performance metrics (moored time, shifting time, waiting time) are within normal ranges or are statistical outliers. This helps identify unusual visits that may need investigation.

**Values:**

* **"NORMAL"** - All metrics are within expected ranges
* **"OUTLIER"** - One or more metrics are significantly higher or lower than average

**Example:** If most container ships spend 12-18 hours moored, but one ship spends 48 hours, it's flagged as an outlier.

---

### 5. **Outlier Detection Flags**

**Business Definition:** Individual flags that identify which specific metrics are outliers for this visit, where outliers are determined using port-specific norms (averages and standard deviations). This helps pinpoint exactly what was unusual about the visit compared to historical behavior at the same port.

**Flags:**

* **is\_moored\_within\_range** - Is the moored time normal? (true/false)
* **is\_shifting\_within\_range** - Is the shifting time normal? (true/false)
* **is\_wait\_before\_arrival\_within\_range** - Is the waiting time before arrival normal? (true/false)
* **is\_wait\_during\_visit\_within\_range** - Is the waiting time during visit normal? (true/false)
* **is\_steaming\_in\_within\_range** - Is the steaming in time normal? (true/false)
* **is\_steaming\_out\_within\_range** - Is the steaming out time normal? (true/false)

**Example:** A vessel might have normal moored time (true) but abnormal waiting time (false), indicating a congestion issue.

> ***NORMAL*** : the values within five standard deviation of the mean.

---

### 6. **Total Waiting Time During Visit Duration**

**Business Definition:** The total time a vessel spends waiting (anchored or slow-moving) between Pilot Onboard and Pilot Disembarked. This includes waiting between berths or waiting for services like pilots or tugs.

**Example:** A ship waits 3 hours at anchor between leaving Berth 1 and arriving at Berth 2 = 3 hours waiting during visit.

---

### 7. **Between EOS Entry and POB Duration**

**Business Definition:** The time between when a vessel crosses the port entrance boundary (EOS Entry = End Of Seapassage Entry) and when the pilot boards the vessel (POB = Pilot On Board). This measures the efficiency of pilot dispatch services.

**Example:** Vessel enters port limits at 9:00 AM, pilot boards at 9:45 AM = 45 minutes between EOS entry and POB.

---

### 8. **Between PDK and EOS Exit Duration**

**Business Definition:** The time between when the pilot disembarks from the vessel (PDK = Pilot Disembarked) and when the vessel crosses the port exit boundary (EOS Exit = End Of Seapassage Exit). This measures how quickly vessels can leave after pilot services are complete.

**Example:** Pilot disembarks at 3:00 PM, vessel exits port limits at 3:30 PM = 30 minutes between PDK and EOS exit.

---

### 9. **Waiting Duration**

**Business Definition:** A comprehensive measure of all waiting time during the port visit, combining both slow-moving time and anchored time while the vessel is within EOS boundaries.

**Example:** Ship spends 2 hours slow-moving + 4 hours at anchor = 6 hours total waiting duration.

### Source Mapping FACT PORT VISIT:

List all upstream sources and also the formula of the calculations.

| **Calculated Column** | **Source Fields** | **Formula** |
| --- | --- | --- |
| **turn\_around\_time\_duration** | * *waiting\_duration,* * *port\_inbound\_travel\_duration,* * *total\_moored\_duration,* * *shifting\_duration,* * *port\_outbound\_travel\_duration* | *waiting\_duration + port\_inbound\_travel\_duration + total\_moored\_duration + shifting\_duration + port\_outbound\_travel\_duration* |
| **shifting\_duration** | * shifting\_between\_terminals\_duration, * shifting\_inside\_terminals\_duration | shifting\_duration = COALESCE(shifting\_between\_terminals\_duration, 0) + COALESCE(shifting\_inside\_terminals\_duration, 0) |
| **total\_waiting\_time\_before\_arrival\_duration** | * *total\_slowmoving\_duration\_arrival,* * *before\_visit\_anchor\_duration* | total\_waiting\_time\_before\_arrival\_duration = COALESCE(total\_slowmoving\_duration\_arrival, 0) + COALESCE(before\_visit\_anchor\_duration, 0) |
| **outlier\_preference** | * pilot\_onboard\_inbound\_timestamp, * is\_wait\_before\_arrival\_within\_range, * is\_wait\_during\_visit\_within\_range, * is\_steaming\_in\_within\_range , * is\_moored\_within\_range, * is\_shifting\_within\_range, * is\_steaming\_out\_within\_range, * total\_berth\_visit] | outlier\_preference = CASE WHEN pilot\_onboard\_inbound\_timestamp IS NOT NULL AND is\_wait\_before\_arrival\_within\_range = TRUE AND is\_wait\_during\_visit\_within\_range = TRUE AND is\_steaming\_in\_within\_range = TRUE AND is\_moored\_within\_range = TRUE AND is\_shifting\_within\_range = TRUE AND is\_steaming\_out\_within\_range = TRUE AND total\_berth\_visit < 8 THEN 'EXCLUDE\_OUTLIERS' ELSE 'SHOW\_OUTLIERS' END |
| **Outlier Detection Flags** *Outlier flags are calculated using statistical analysis from fact\_port\_performance\_analytics* | is\_moored\_within\_range | is\_moored\_within\_range = CASE WHEN total\_moored\_duration >= 0 AND total\_moored\_duration <= (average\_moored + 5 \* stddev\_moored) AND total\_moored\_duration >= (average\_moored - 5 \* stddev\_moored) THEN TRUE ELSE FALSE END |
| **total\_waiting\_time\_during\_visit\_duration** | * total\_slowmoving\_duration\_inport, * during\_visit\_anchor\_duration | COALESCE(total\_slowmoving\_duration\_inport, 0) + COALESCE(during\_visit\_anchor\_duration, 0) |
| **between\_eos\_entry\_and\_pob\_duration** | * pilot\_onboard\_inbound\_timestamp, * eos\_entry\_timestamp | COALESCE(EXTRACT(EPOCH FROM (pilot\_onboard\_inbound\_timestamp - eos\_entry\_timestamp)) / 3600.0, 0) |
| **between\_pdk\_and\_eos\_exit\_duration** | * eos\_exit\_timestamp, * pilot\_disembarked\_outbound\_timestamp] | COALESCE(EXTRACT(EPOCH FROM (eos\_exit\_timestamp - pilot\_disembarked\_outbound\_timestamp)) / 3600.0, 0) |
| **waiting\_duration** | * total\_slowmoving\_duration\_arrival, * before\_visit\_anchor\_duration, * total\_slowmoving\_duration\_inport, * during\_visit\_anchor\_duration] | COALESCE( total\_slowmoving\_duration\_arrival, 0 ) + COALESCE( before\_visit\_anchor\_duration, 0 ) + COALESCE(total\_slowmoving\_duration\_inport, 0 ) + COALESCE(during\_visit\_anchor\_duration, 0 ) |

3. **Terminal visits calculated columns**

These metrics describe a vessel's visit to a **specific terminal** within the port:

### 1. **Turn Around Time Duration**

**Business Definition:** The total time a vessel spends at a specific terminal from arrival in the first berth to departure from the last.. This measures terminal-specific efficiency.

**Example:** Vessel arrives at Container Terminal A at 10:00 AM and departs at 8:00 PM = 10 hours terminal turnaround time.

---

### 2. **Terminal Cargo Operation Duration**

**Business Definition:** The total time a vessel spends at a berth that is capable of compatible cargo operations.

**Example:** Tanker vessel is berthed at a liquid bulk berth for 6 hours = 6 hours cargo operation duration..

---

### 3. **Terminal Non-Cargo Operation Duration**

**Business Definition:** The total time a vessel spends at berths NOT performing cargo operations (e.g., waiting berths, repair berths, bunkering berths). This is typically non-productive time.

**Example:** Ship spends 2 hours at a waiting berth = 2 hours non-cargo operation duration.

---

### 4. **Terminal Moored Duration**

**Business Definition:** The total time a vessel spends tied up (moored) at all berths within this terminal, including both cargo and non-cargo operations.

**Example:** Ship spends 6 hours at cargo berth + 2 hours at waiting berth = 8 hours total moored duration.

---

### 5. **Terminal Anchor Duration**

**Business Definition:** The total time a ship spent at anchorage specifically during the terminal visit period.

**Example:** Ship waits at anchor in terminal area for 3 hours before berth becomes available = 3 hours terminal anchor duration.

---

### 6. **Waiting Outside Terminal Duration**

**Business Definition:** The time a vessel spends waiting (anchored or slow-moving) before arriving in the terminal.

**Example:** Ship waits 1.5 hours outside terminal entrance = 1.5 hours waiting outside terminal.

---

### 7. **Waiting During Terminal Visit Duration**

**Business Definition:** The total time a vessel spends waiting (anchored or slow-moving) between its arrival at terminal and departure from terminal.

**Example:** Ship spends 2 hours at anchor + 1 hour slow-moving within terminal = 3 hours waiting during terminal visit.

---

### 8. **Steaming In Duration**

**Business Definition:** It is the duration between Pilot Onboard and arrival at the first berth in terminal, if this is the first terminal visited in port. It is 0 if the terminal is visited later in port.

**Example:**

**Terminal A (First Terminal Visited)**

* Pilot Onboard Time: 09:00
* Arrival at First Berth: 09:45
* Steaming In Duration: 45 minutes ✅

  + Calculation: 09:45 - 09:00 = 45 minutes
  + This is the time the vessel spent traveling from the pilot station to the first berth

**Terminal B (Second Terminal Visited)**

* Steaming In Duration: 0 minutes ✅

  + Reason: This is NOT the first terminal visited in the port
  + The vessel is already inside the port, just shifting between terminals
  + The duration between terminals is called "shifting duration", not "steaming in"

---

### 9. **Steaming Out Duration**

**Business Definition:** The time a vessel spends traveling from its last berth in terminal to getting the pilot disembarked, if this is the last terminal visited in port. It is 0 if the vessel visits another terminal before Pilot Disembarked.

**Example:**

### Terminal A (First Terminal - NOT Last)

* Departure from Berth: 12:00
* Steaming Out Duration: 0 minutes ✅

  + Reason: This is NOT the last terminal visited in the port
  + The vessel visits Terminal B after this, so no "steaming out" yet
  + The duration to Terminal B is called "shifting duration", not "steaming out"

### Terminal B (Last Terminal Visited)

* Departure from Berth: 15:00
* Pilot Disembark Time: 15:45
* Steaming Out Duration: 45 minutes ✅

  + Calculation: 15:45 - 15:00 = 45 minutes
  + This is the time the vessel spent traveling from the last berth to the pilot station.

---

### 10. **Anchorage During Terminal Visit Duration**

**Business Definition:** The total time a vessel spends specifically at anchor (not slow-moving) between terminal arrival and departure.

**Example:** Ship visits Berth 1 in Terminal A. Before moving into Berth 2 in Terminal A, it has to anchor for 2 hours. = 2 hours anchorage during terminal visit.

---

### 11. **Slowmoving During Terminal Visit Duration**

**Business Definition:** The total time a vessel spends moving very slowly (below normal speed) between terminal arrival and departure, typically while waiting or maneuvering.

**Example:** Ship visits Berth 1 in Terminal A. Before moving into Berth 2 in Terminal A, it moves slowly for 45 minutes while waiting for Berth 2’s clearance = 45 minutes slowmoving duration.

---

### 12. **Shifting Within Terminal Visit Duration**

**Business Definition:** The time a vessel spends moving between different berths within the same terminal.

**Example:** Ship shifts from Berth 1 to Berth 4 within the same terminal, taking 1.5 hours = 1.5 hours shifting within terminal.

### **Source Mapping FACT TERMINAL VISIT:**

List all upstream sources and also the formula of the calculations.

| **Calculated Column** | **Source (Table and Fields)** | **Formula** |
| --- | --- | --- |
| **turn\_around\_time\_duration** | **fact\_terminal\_visit**   * `end_timestamp` * `start_timestamp` | `CASE WHEN tv.end_timestamp > tv.start_timestamp THEN date_trunc('second', tv.end_timestamp - tv.start_timestamp) END` |
| **terminal\_cargo\_operation\_duration** | **fact\_berth\_visit**   * `moored_duration` (where `is_cargo_operation = true`) | `SUM(moored_duration)` from berth visits with cargo operations |
| **terminal\_non\_cargo\_operation\_duration** | **fact\_berth\_visit**   * `moored_duration` (where `is_cargo_operation = false`) | `SUM(moored_duration)` from berth visits without cargo operations |
| **terminal\_moored\_duration** | **fact\_berth\_visit**   * `moored_duration` | `SUM(moored_duration)` from all berth visits |
| **terminal\_anchor\_duration** | **temp\_timeline\_anchorage\_event\_terminal\_visit**   * `end_timestamp` * `start_timestamp` | `SUM(date_trunc('second', end_timestamp - start_timestamp))` for anchorage events |
| **waiting\_outside\_terminal\_duration** | **Temp Table: Terminal waiting timeline**   * `to_timestamp` * `from_timestamp` | `COALESCE(to_hours_duration(to_timestamp - from_timestamp), 0)` |
| **waiting\_during\_terminal\_visit\_duration** | **temp\_fact\_terminal\_visit\_anchorage\_during\_terminal\_visit** **temp\_fact\_terminal\_visit\_slowmoving\_during\_terminal\_visit**   * `total_anchorage_during_terminal_visit_duration` * `total_slowmoving_during_terminal_visit_duration` | `COALESCE(total_anchorage_during_terminal_visit_duration, 0) + COALESCE(total_slowmoving_during_terminal_visit_duration, 0)` |
| **steaming\_in\_duration** | **Temp Table: Terminal steaming in timeline**   * `to_timestamp` * `from_timestamp` | `COALESCE(to_hours_duration(to_timestamp - from_timestamp), 0)` |
| **steaming\_out\_duration** | **Temp Table: Terminal steaming out timeline**   * `to_timestamp` * `from_timestamp` | `COALESCE(to_hours_duration(to_timestamp - from_timestamp), 0)` |
| **anchorage\_during\_terminal\_visit\_duration** | **ods\_anchor\_stop**   * `end_timestamp` * `start_timestamp`   (filtered by terminal visit timeline) | `SUM(COALESCE(to_hours_duration(oas.end_timestamp - oas.start_timestamp), 0))` where anchor events occur within terminal visit timeline |
| **slowmoving\_during\_terminal\_visit\_duration** | **ods\_slow\_moving\_period**   * `end_timestamp` * `start_timestamp`   (filtered by terminal visit timeline) | `SUM(COALESCE(to_hours_duration(smp.end_timestamp - smp.start_timestamp), 0))` where slow moving periods occur within terminal visit timeline |
| **shifting\_within\_terminal\_visit\_duration** | **fact\_terminal\_visit**   * `turn_around_time_duration` * `terminal_moored_duration` * `waiting_during_terminal_visit_duration` | `COALESCE(round_four_digit_decimal(turn_around_time_duration) - round_four_digit_decimal(terminal_moored_duration) - round_four_digit_decimal(waiting_during_terminal_visit_duration), 0)` |

4. **Berth Visits Calculated Columns**

These metrics describe a vessel's visit to a **specific berth**:

### 1. **Moored Duration**

**Business Definition:** The total time a vessel spends tied up at a specific berth from the moment mooring is complete until unmooring begins.

**Example:** Vessel completes mooring at 2:00 PM and begins unmooring at 8:00 PM = 6 hours moored duration.

---

### 2. **Mooring Duration**

**Business Definition:** The time it takes to secure a vessel to the berth, from when the vessel arrives at the berth until all mooring lines are secured and the vessel is ready for operations.

**Example:** Vessel arrives at berth at 1:45 PM, mooring complete at 2:00 PM = 15 minutes mooring duration.

---

### 3. **Unmooring Duration**

**Business Definition:** The time it takes to release a vessel from the berth, from when unmooring begins until all lines are released and the vessel is free to depart.

**Example:** Unmooring starts at 8:00 PM, vessel free to depart at 8:20 PM = 20 minutes unmooring duration.

---

### 4. **Unique Tugs Arrival Count**

**Business Definition:** The number of different tugboats used to assist the vessel's arrival at this berth. More tugs typically indicate larger vessels or more complex maneuvering.

**Example:** Three tugboats (Tug-A, Tug-B, Tug-C) assist vessel arrival = 3 unique tugs arrival count.

---

### 5. **Unique Tugs Departure Count**

**Business Definition:** The number of different tugboats used to assist the vessel's departure from this berth.

**Example:** Two tugboats (Tug-A, Tug-D) assist vessel departure = 2 unique tugs departure count.

---

### 6. **First Tug Arrived Departure Timestamp**

**Business Definition:** The timestamp when the **first tugboat arrived** at the berth to assist the vessel during berthing operations.

**Example:**

javawide76008:00 - Vessel approaching Pasir Panjang Terminal, Berth 5
08:15 - Tug "PACIFIC STAR" arrives to assist (FIRST TUG ARRIVAL) ✅
08:20 - Tug "OCEAN FORCE" arrives to assist (SECOND TUG ARRIVAL)
08:25 - Tug "HARBOR KING" arrives to assist (THIRD TUG ARRIVAL)

Result: **First Tug Arrived Departure Timestamp**: **08:15** ✅

---

### 7. **Last Tug Arrived Departure Timestamp**

**Business Definition:** The exact date and time when the last tugboat arrives to assist with the vessel's departure. This indicates when all tugs are in position for departure.

**Example:** Last tug arrives at 7:55 PM on June 15, 2024, now all tugs ready for departure.

---

### 8. **Is Cargo Operation**

**Business Definition:** A yes/no indicator showing whether the vessel visited a berth capable of compatible cargo operations.

**Values:**

* **Yes (true)** - Vessel visited a berth capable of compatible cargo operations (e.g. tanker visiting liquid bulk terminal)
* **No (false)** - Vessel visited a berth NOT capable of compatible cargo operations (e.g. waiting berth, repair berth, tanker waiting in dry bulk berth)

**Example:** Container ship at Container Berth 3 = Yes (cargo operation). Same ship at Waiting Berth 1 = No (non-cargo operation).

---

### 9. **Arrival First Bunker Timestamp**

**Business Definition:** The exact date and time when the first bunker vessel (fuel supply ship) arrives to provide fuel to the vessel at this berth.

**Example:** First bunker vessel arrives at 3:00 PM on June 15, 2024 to begin refueling operations.

---

### 10. **Departure Last Bunker Timestamp**

**Business Definition:** The exact date and time when the last bunker vessel departs after completing fuel supply operations.

**Example:** Last bunker vessel completes refueling and departs at 5:30 PM on June 15, 2024.

---

### 11. **Bunkers Count**

**Business Definition:** The total number of bunker vessels (fuel supply ships) that serviced this vessel during its berth visit. Multiple bunkers may indicate large fuel requirements or different fuel types.

**Example:** Two bunker vessels provide fuel during the berth visit = 2 bunkers count.

### Source Mapping FACT BERTH VISIT:

List all upstream sources and also the formula of the calculations.

| **Calculated Column** | **Source Table/Fields** | **Formula** |
| --- | --- | --- |
| **moored\_duration** | **ods\_berth\_visit**   * `end_timestamp` * `start_timestamp` | `CASE WHEN bv.end_timestamp > bv.start_timestamp THEN COALESCE(date_trunc('second', bv.end_timestamp - bv.start_timestamp), interval '0 seconds') END` Converted to hours: `to_hours_duration(moored_duration)` |
| **mooring\_duration** | **ods\_terminal\_visit** **ods\_berth\_visit**   * `tv.mooring_start_timestamp` * `bv.start_timestamp` | `COALESCE(date_trunc('second', bv.start_timestamp - tv.mooring_start_timestamp), interval '0 seconds')` Converted to hours: `to_hours_duration(mooring_duration)` |
| **unmooring\_duration** | **ods\_terminal\_visit** **ods\_berth\_visit**   * `tv.mooring_end_timestamp` * `bv.end_timestamp` | `COALESCE(date_trunc('second', tv.mooring_end_timestamp - bv.end_timestamp), interval '0 seconds')` Converted to hours: `to_hours_duration(unmooring_duration)` |
| **unique\_tugs\_arrival\_count** | **ods\_tug\_event**   * `start_timestamp` (where `type = 'arrival'`) | `COUNT(*)` of unique tug events with type 'arrival' and non-null start\_timestamp |
| **unique\_tugs\_departure\_count** | **ods\_tug\_event**   * `start_timestamp` (where `type = 'departure'`) | `COUNT(*)` of unique tug events with type 'departure' and non-null start\_timestamp |
| **first\_tug\_arrived\_departure\_timestamp** | **ods\_tug\_event**   * `arrival_start_timestamp` (first tug) | `MIN(arrival_start_timestamp)` from first tug arrival event |
| **last\_tug\_arrived\_departure\_timestamp** | **ods\_tug\_event**   * `departure_start_timestamp` (last tug) | `MAX(arrival_start_timestamp)` from last tug arrival event (ordered DESC) |
| **is\_cargo\_operation** | **ods\_ship** **ods\_berth**   * `ship.category` (v3, v2, or v1) * `berth.cargo_category_type` * `berth.function_type` | `CASE WHEN 'WAITING' = ANY(berth.function_type) THEN false ELSE COALESCE(allowed_berth_cargo_types && berth_cargo_types, false) END`  **Logic:**   * If berth function\_type = 'WAITING' → `false` * Otherwise, check if ship's allowed cargo types overlap with berth's cargo types   **Ship-to-Berth Cargo Type Mapping:**   * GENERAL\_CARGO → [BREAKBULK, CONTAINER, DRYBULK] * TANKER → [WETBULK] * CONTAINER → [CONTAINER] * OFFSHORE → [DRYBULK, BREAKBULK] * PASSENGER → [PASSENGER] * BULK\_CARRIER → [DRYBULK] |
| **arrival\_first\_bunker\_timestamp** | **ods\_encounter**   * `start_timestamp` (where `ship_type = 'BUNKER'`) | `MIN(start_timestamp)` from bunker encounters within berth visit timeline |
| **departure\_last\_bunker\_timestamp** | **ods\_encounter**   * `end_timestamp` (where `ship_type = 'BUNKER'`) | `MAX(end_timestamp)` from bunker encounters within berth visit timeline |
| **bunkers\_count** | **ods\_encounter**   * Count of bunker encounters | `COUNT(*)` of encounters where `ship_type = 'BUNKER'` for the visit |

5. **Duration Calculations**

The duration fields are calculated in **hours** using the following formula below:

wide760-- Basic duration calculation
duration = EXTRACT(EPOCH FROM (end\_timestamp - start\_timestamp)) / 3600.0
-- Using the to\_hours\_duration() function
duration = to\_hours\_duration(end\_timestamp - start\_timestamp)

6. **Pilot Calculated Columns**

### a. **Selected Pilot**

**Business Definition:** A yes/no indicator showing whether this pilot was the pilot which is considered primarily for this visit for Pilot Onboard and Pilot Disembarked timestamps.

**Values:**

* **Yes (true)** - This is the primary pilot, either used for steaming in the port for the initial arrival (Pilot Onboard timestamp) or steaming out from the port for the final departure (Pilot Disembarked timestamp).
* **No (false)** - In case of multiple pilot encounters, pilots are labelled with No if the vessel did not use their assistance for steaming in port for the initial arrival or steaming out from the port for the final departure.

**Example:**

Vessel gets a pilot onboard at 9:00 AM, but can not enter the port due to weather disruptions. This is labelled as No.

Another pilot gets on board at 11:00 AM, and the vessel steams in the port after this encounter. This is labelled as Yes.

In case there are other pilot encounters assisting vessel going in and out of the port, but the vessel does not leave the EOS area, these pilot activities are also labelled as No.

Before the vessel leaves the port for its next destination, Pilot gets disembarked at 18:00 PM, this activity is labelled with Yes.

### Source Mapping

List all upstream sources and also the formula of the calculations.

| **Calculated Column** | **Source Table** | **Formula** |
| --- | --- | --- |
| **selected\_pilot** | **ods\_pilot\_event** **ods\_encounter** | `true` if from selected pilot events (ods\_pilot\_event) `false` if from encounter pilot events (ods\_encounter with ship\_type = 'PILOT') |

7. **Tug Calculated Columns**

### a. **Cargo Visit Tugging State**

**Business Definition:** A classification that identifies what phase of the port visit the tugboat assistance occurred in. This helps understand when tugs are needed most.

**Values:**

* **"STEAMING\_IN"** - Tug assisted vessel's arrival at the first berth (entering the port)
* **"STEAMING\_OUT"** - Tug assisted vessel's departure from the last berth (leaving the port)
* **"SHIFTING"** - Tug assisted vessel moving between berths within the port

**Example:**

* Tug helps vessel arrive at Berth 1 (first berth) = STEAMING\_IN
* Tug helps vessel move from Berth 1 to Berth 3 = SHIFTING
* Tug helps vessel depart from Berth 3 (last berth) = STEAMING\_OUT

### Source Mapping

List all upstream sources and also the formula of the calculations.

| **Calculated Column** | **Source Table [Field(s)]** | **Formula** |
| --- | --- | --- |
| **cargo\_visit\_tugging\_state** | **ods\_berth\_visit** **ods\_tug\_event**   * `berth_visit.ref` * `tug_event.type` | `COALESCE(arrival_tugs_steaming_in.cargo_visit_tugging_state, COALESCE(departure_tugs_steaming_out.cargo_visit_tugging_state, 'SHIFTING'))`  **Logic:**   * If tug is arrival type AND berth\_visit.ref = 0 → `'STEAMING_IN'` * If tug is departure type AND berth is last berth → `'STEAMING_OUT'` * Otherwise → `'SHIFTING'` |

8. **PortCall Calculated Columns**

These metrics provide **aggregate statistics** about port activity:

### 1. **Total Port Calls**

**Business Definition:** The total number of vessel visits to the port on a specific date, regardless of vessel type or size. This is the primary measure of port activity.

**Example:** On June 15, 2024, the port received 45 vessel visits = 45 total port calls.

---

### 2. **Ship Category Dry Bulk Total Port Calls**

**Business Definition:** The number of dry bulk carrier visits (ships carrying coal, grain, ore, etc.) to the port on a specific date (e.g on June 15, 2024).

**Example:** On June 15, 2024, the port received 12 dry bulk carriers = 12 dry bulk port calls.

---

### 3. **Ship Category Wet Bulk Total Port Calls**

**Business Definition:** The number of wet bulk carrier visits (tankers carrying oil, chemicals, LNG, etc.) to the port on a specific date.

**Example:** On June 15, 2024, the port received 8 tankers = 8 wet bulk port calls.

---

### 4. **Ship Category TEU Total Port Calls**

**Business Definition:** The number of container ship visits to the port on a specific date. TEU stands for "Twenty-foot Equivalent Unit," the standard measure for container capacity.

**Example:** On June 15, 2024, the port received 18 container ships = 18 TEU port calls.

---

### 5. **Ship Category Unknown Total Port Calls**

**Business Definition:** The number of vessel visits where the ship type could not be determined or classified. This helps identify data quality issues.

**Example:** On June 15, 2024, the port received 7 vessels with unknown ship types = 7 unknown port calls.

---

## Source Mapping

List all upstream sources and also the formula of the calculations.

| **Calculated Column** | **Source Table Fields** | **Formula** |
| --- | --- | --- |
| **total\_port\_calls** | **fact\_port\_visit**   * visit\_id | `COUNT(DISTINCT visit_id)` grouped by port and completion date |
| **ship\_category\_dry\_bulk\_total\_port\_calls** | **fact\_port\_visit**   * visit\_id **dim\_ship** * ship\_category | `COUNT(DISTINCT visit_id)` where ship category is dry bulk |
| **ship\_category\_wet\_bulk\_total\_port\_calls** | **fact\_port\_visit**   * visit\_id **dim\_ship** * ship\_category | `COUNT(DISTINCT visit_id)` where ship category is wet bulk |
| **ship\_category\_teu\_total\_port\_calls** | **fact\_port\_visit**   * visit\_id **dim\_ship** * ship\_category | `COUNT(DISTINCT visit_id)` where ship category is TEU (container) |
| **ship\_category\_unknown\_total\_port\_calls** | **fact\_port\_visit**   * visit\_id **dim\_ship** * ship\_category | `COUNT(DISTINCT visit_id)` where ship category is unknown |

## Changelog

Track material changes with reason, reviewer, and impact.

| **Change summary** | **Author** | **Reviewer** | **Effective date** |
| --- | --- | --- | --- |
| [Initial creation] |  | [Add Reviewer] |  |
| Updated as Reviewed by Yaren. |  |  |  |

## References

* Specifications/tickets: *[Link to requirement or Jira ticket]*
* Data dictionary entries: *Complete Overview for the new Data Platform*
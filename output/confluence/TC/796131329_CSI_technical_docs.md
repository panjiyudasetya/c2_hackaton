---
id: confluence:796131329
source: confluence
type: page
space: TC
title: CSI technical docs
author: Leon Joosse (Unlicensed)
date: '2025-08-01'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/796131329
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/796131329
---
# CSI technical docs

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/796131329  

## Content

# CSI technical documentation

CSI is the source of truth for all seagoing vessels in Teqplay. The system registers all ships with an IMO. Data is entered manually, some information is obtained from AIS messages.

Note that other ship categories sometimes have an IMO set, such as tugs or pilot vessels. These are also registered in the system, as they have an IMO.

## CSI Components

CSI consists of multiple components:

1. **Management interface**: frontend + backend for context mapping team to manage all ships in the registry. Ship details are changed from this system (automatically & manually).
2. **Query service**: highly available service in the Kubernetes cluster to retrieve ship data for other Teqplay components and the external API. The ship register is read-only in this component.
3. **Client**: kotlin library for other Teqplay applications to add as a dependency, supplying helper classes to easily retrieve ship data
4. **API**: kotlin library with model classes in CSI, this is usually included through the `client` library.

Additionally, the CSI query service is spun up in VesselVoyage revents, which is a sealed environment of core-components to generate events and data based on historic AIS data. This runs on-demand and therefore sometimes show up in the K8S cluster.

## Set-up of the GIT repositories

The [CSI back-end repository](https://github.com/teqplay/csi-backend) contains all components of previous chapter:

* `/api`: model classes in CSI
* `/app`

  + `/base`: shared components for sibling modules
  + `/internal`: backend for the management interface
  + `/query`: backend for the highly available query service
* `/client`: kotlin library for Teqplay applications to easily retrieve ship info
* `/lib`: shared components in the whole repo

The [CSI front-end repository](https://github.com/teqplay/csi) contains the front-end for the management interface. There’s no need to explain the contents, as its straightforward as any other front-end repo.

## Features in the management interface back-end

This section describes the features in the management interface back-end.

### Ship register

The ship register all ships registered in CSI. The information is current and expected to be up-to-date. Data is stored in the `shipRegister` database collection.

Updates to the ship register are done through tickets (more info below), never immediately updating the database.

### Tickets

A **ticket** denotes the change of a single field of a single ship in the ship register. For example, its name, category, country flag, etc. The ticket is reviewed by the context mapping team for correctness, following an approval or rejection. Once reviewed, the ticket is applied to the ship in the `shipRegister`.

Tickets are stored in the `ticket` collection, reviewed (approved/rejected) tickets in the `ticketDeleted` collection.

### External tickets

The system allows external users to bring up tickets. This was envisioned for our customers, but never really put to use. These tickets are stored in `ticketExternal`.

### IMO/MMSI mapping tickets

The system has **IMO/MMSI mapping tickets** to track MMSI changes for a ship. An MMSI changes sometimes (e.g. change of owner, country flag), opposed to an IMO that should not change, as the IMO is assigned to the 'steel' of the ship.

CSI subscribes to AIS updates and monitors whether the MMSI number of a ship is different than in the ship register. The IMO number is used as unique value to match the ship, as the system is only interested in such ships. On detecting an MMSI change, the system observes the changing MMSI numbers for a while. When the system is sure enough on the change (conditions described below), an IMO/MMSI mapping ticket is created for the CSI admin to review.

The system considers the following cases:

1. `MMSI_GETS_SET`: the ship’s MMSI changes from `null → mmsiA`
2. `MMSI_CHANGED`: the ship’s MMSI changes from `mmsiA → mmsiB`
3. `MMSI_ALREADY_CHANGED`: the system observes a changing MMSI in AIS messages, but the MMSI was already set in the ship register
4. `MULTIPLE_MMSI`: the system observes multiple MMSIs coming in. There are a lot of possible causes, but most likely it is a spoofer, the ship uses different MMSIs to ‘work around’ regulations (or sometimes multiple AIS transponders on board), the MMSI is fake (e.g. 12345678).

The system has conditions for an MMSI change to be considered. All must be met to create an IMO/MMSI mapping ticket:

* The new MMSI must have occurred at least 200 times in AIS messages, since it was seen for the first time
* In case of observing multiple MMSIs: the new MMSI must be observed at least 10% of the amount of the current MMSI (it’s not fully clear to me what the reason is)
* One of:

  + Observed AIS messages only have the new MMSI
  + Observed AIS messages have the current MMSI and at some point only the new MMSI

## Observing AIS messages to find changing MMSIs

CSI subscribes to AIS updates to observe changing MMSIs, as touched upon in the previous chapter on IMO/MMSI mapping tickets. This chapter explains the process of observing the AIS messages and observing those for sometime, after which the IMO/MMSI mapping tickets are created.

The system is subscribed to the AIS updates on our internal RabbitMQ, coming from ais-engine. Once an AIS message comes, the system checks the validity of the IMO (checksum) and MMSI (length). The MMSI is then stored as `RawImoMapping` in memory in the `ImoMappingDatasource`. This a map of MMSI occurrences per IMO, keeping a count per MMSI per hour.

The system runs the `ShipRegisterMappingScheduleService`, retrieving the aforementioned RawImoMappings and processes them, with one of the outcomes as below (MMSI\_GETS\_SET, MMSI\_CHANGED, MMSI\_CHANGED\_ALREADY, MULTIPLE\_MMSI).

### Processing Thresholds

The system uses several thresholds to ensure ticket quality:

* **minimumTotalMessages**: 200 (ship needs at least 200 AIS messages in the time window)
* **minimumAbsolute**: 100 (MMSI needs 100+ observations to be considered significant)
* **minimumRelative**: 0.1 (10% relative threshold for MMSI changes)
* **precision**: 1 hour (time bucket granularity for grouping RawImoMapping)
* **margin**: 1 day (processing window for analysis)

### 1. MMSI\_GETS\_SET

**Condition**: Ship has no MMSI in ShipRegister (`currentMmsi == null`) but AIS shows consistent MMSI usage.

**Real-world Scenarios**:

* New ship enters service (first time broadcasting AIS)
* Ship was registered with IMO only (MMSI unknown during registration)
* Ship returned to service after extended dry dock (new MMSI assigned)

**Timeline Visualization**:

ShipRegister: IMO=1234567, MMSI=null
AIS Timeline: Hour 1 Hour 2 Hour 3 Hour 4 Hour 5 Hour 6 Hour 7
-------- -------- -------- -------- -------- -------- --------
MMSI 111111111: 32 29 35 31 33 30 32
MMSI 222222222: 0 0 0 0 0 0 0
-------- -------- -------- -------- -------- -------- --------
Total Messages: 32 29 35 31 33 30 32
Analysis: Only MMSI 111111111 observed (222 total messages > 200 threshold)
Ticket Created: ✓ MMSI\_GETS\_SET - Suggest setting MMSI to 111111111

### 2. MMSI\_CHANGED

**Condition**: Ship shows clear transition from one MMSI to another (`suggestion != null`).

**Real-world Scenarios**:

* Ship ownership change (new owner assigns different MMSI)
* Flag state change (ship changes registration country, gets new MMSI assigned)
* Equipment replacement (new AIS transponder with different MMSI)
* Regulatory compliance (“secretly” using another MMSI to stay compliant)

**Example:**

ShipRegister: IMO=1234567, MMSI=111111111
AIS Timeline: Hour 1-4 Hour 5-8 Hour 9-12 Hour 13-16 Hour 17-20 Hour 21-24
-------- -------- --------- --------- --------- ---------
MMSI 111111111: 48 42 28 12 0 0
MMSI 222222222: 0 0 14 35 47 51
-------- -------- --------- --------- --------- ---------
Total Messages: 48 42 42 47 47 51
Analysis: Clear transition from 111111111 to 222222222 around Hour 13-16
Transition Point: ↓ (Hour 13-16)
Ticket Created: ✓ MMSI\_CHANGED - Suggest change from 111111111 to 222222222 at Hour 13

### 3. MMSI\_CHANGED\_ALREADY

**Condition**: ShipRegister shows old MMSI but AIS only shows different MMSI (`!mmsiOccurrences.containsKey(currentMmsi)`).

**Real-world Scenarios**:

* Ship changed MMSI during system downtime (transition missed)
* External MMSI change (updated manually via a regular ticket by a user)
* Data entry lag (change happened but ShipRegister not updated yet)

**Timeline Visualization**:

ShipRegister: IMO=1234567, MMSI=111111111 (outdated)
AIS Timeline: Hour 1 Hour 2 Hour 3 Hour 4 Hour 5 Hour 6 Hour 7
-------- -------- -------- -------- -------- -------- --------
MMSI 111111111: 0 0 0 0 0 0 0 ← Not observed, but is in shipRegister!
MMSI 222222222: 31 33 30 32 29 31 33
-------- -------- -------- -------- -------- -------- --------
Total Messages: 31 33 30 32 29 31 33
Analysis: ShipRegister has 111111111 but AIS only shows 222222222 (219 messages > 200)
Discrepancy: ⚠️ ShipRegister out of sync with reality
Ticket Created: ✓ MMSI\_CHANGED\_ALREADY - Ship already using 222222222, update needed

### 4. MULTIPLE\_MMSI

**Condition**: Ship broadcasts multiple MMSIs simultaneously or has complex usage patterns.

**Real-world Scenarios**:

* Multiple vessels using the same MMSI (is not allowed, but AIS is an open network, any weirdo can transmit AIS messages with any content)
* Ship changes MMSI often for unknown reason
* Invalid MMSIs like 12345678, used for testing

**Example A - Simultaneous Broadcasting**:

ShipRegister: IMO=1234567, MMSI=111111111
AIS Timeline: Hour 1 Hour 2 Hour 3 Hour 4 Hour 5 Hour 6 Hour 7
-------- -------- -------- -------- -------- -------- --------
MMSI 111111111: 12 11 13 12 12 12 11
MMSI 222222222: 11 12 12 13 11 12 12
MMSI 333333333: 1 1 0 0 1 0 1
-------- -------- -------- -------- -------- -------- --------
Total Messages: 24 24 25 25 24 24 24
Analysis: Multiple MMSIs used simultaneously, no clear transition pattern
Pattern: 🔄 Complex/simultaneous usage
Ticket Created: ✓ MULTIPLE\_MMSI - Manual review required for complex MMSI usage

**Example B - Ignored MMSI Handling**:

ShipRegister: IMO=1234567, MMSI=111111111
ShipMapping.ignored: [444444444] ← Previously marked as spam/invalid by data engineer
AIS Timeline: Hour 1 Hour 2 Hour 3 Hour 4 Hour 5 Hour 6 Hour 7
-------- -------- -------- -------- -------- -------- --------
MMSI 111111111: 12 11 13 12 12 12 11
MMSI 444444444: 8 9 7 8 9 8 7 ← Ignored MMSI
MMSI 555555555: 4 5 5 5 4 4 5
-------- -------- -------- -------- -------- -------- --------
Total Messages: 24 25 25 25 25 24 23
Analysis: MMSI 444444444 is ignored (filtered out), but 555555555 creates complexity
Filtering: 444444444 excluded from analysis due to ignore list
Pattern: 🔄 Current MMSI + new MMSI (555555555) without clear transition
Ticket Created: ✓ MULTIPLE\_MMSI - Review needed for 555555555 usage pattern

## When Tickets Are NOT Created

The system filters out low-quality or insignificant changes to prevent noise:

**Example A - Insufficient Total Messages**:

ShipRegister: IMO=1234567, MMSI=null
AIS Timeline: Hour 1 Hour 2 Hour 3 Hour 4 Hour 5 Hour 6 Hour 7
-------- -------- -------- -------- -------- -------- --------
MMSI 111111111: 15 12 18 14 16 13 15
-------- -------- -------- -------- -------- -------- --------
Total Messages: 15 12 18 14 16 13 15
Analysis: Only 103 total messages < 200 threshold
Result: ❌ No ticket created - Insufficient AIS data for reliable analysis

**Example B - MMSI Below Absolute Threshold**:

ShipRegister: IMO=1234567, MMSI=111111111
AIS Timeline: Hour 1 Hour 2 Hour 3 Hour 4 Hour 5 Hour 6 Hour 7
-------- -------- -------- -------- -------- -------- --------
MMSI 111111111: 25 23 26 24 25 24 23
MMSI 222222222: 12 14 11 13 12 11 14 ← Only 87 total
-------- -------- -------- -------- -------- -------- --------
Total Messages: 37 37 37 37 37 35 37
Analysis: MMSI 222222222 has 87 observations < 100 absolute threshold
Result: ❌ No ticket created - New MMSI usage not significant enough

#### Duplicate Prevention

The system prevents duplicate tickets by checking:

1. **Current mappings**: If MMSIs are already in the ship's current mapping or ignored list
2. **Resolved history**: If the same MMSI change was already resolved previously
3. **Time windows**: Processing overlapping time periods to catch all changes

This ensures data entry engineers don't receive the same ticket multiple times for resolved changes.
---
id: confluence:666959873
source: confluence
type: page
space: TC
title: Corpus Christi (POCCA)
author: Joaquin Marquez Bugella
date: '2026-06-25'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/666959873
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/666959873
---
# Corpus Christi (POCCA)

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/666959873  

## Content

#FFF0B3

Work in progress

1
1
incomplete
 to complete when Jira card gets scheduled. 

However, here are some notes:

1. Implemented as a TaskService, hence, following the general ScheduledTask data processing approach.
2. Json files produced by POCCA will be digested as following:

   1. On a frequency of 4 times/hour (every 15')
   2. Files will be exchanged in a configurable s3 repository provided by Teqplay (initially [https://eu-west-1.console.aws.amazon.com/s3/buckets/poccagoanywhere?region=eu-west-1](https://eu-west-1.console.aws.amazon.com/s3/buckets/poccagoanywhere?region=eu-west-1&bucketType=general&tab=objects))
   3. Filenames follow the format `prefix_yyyyMMdd_hhmmss.json`
   4. Files will be deleted after a configurable age of **30 days** after the processing date.
   5. The data model in the json file is [Movement (github link)](https://github.com/teqplay/portcallplus/blob/feat/develop/src/main/kotlin/nl/teqplay/portcallplus/model/data/corpuschristi/Movement.kt).
3. Portcalls will be created or updated with the incoming `Movement` data:
4. A record of the parsing (not processing!) file results is held in the collection `corpusChristiFileParsing`

---

| Field | Kotlin type | Description | Example / Notes |
| --- | --- | --- | --- |
| `dataExportTime` | `Date` | Timestamp when the source system exported this record set. | `2026-05-25 17:08:10.670` |
| `movementId` | `String?` | Unique identifier of the specific vessel movement/job. | `408383` |
| `visitId` | `String?` | Port call identifier for the vessel visit. In code comments, it is distinct from `visitNumber`. | `136233` |
| `visitNumber` | `String` | Alternate/reference number for the same port call/visit. Different from `visitId`. | `299079` |
| `jobType` | `String?` | Type of movement operation. | Seen values: `Arrival`, `Shift`, `Departure` |
| `movement_status_type_id` | `String?` | Upstream numeric status type identifier. Internal/system status code from the source. | Seen values: `725`, `733`, `735`, `736` |
| `jobStatus` | `String?` | Short movement status code. | Seen values in code: `CNF`, `SUB`, `SCH`, `RDY`, `COM`, `CAN` |
| `isCanceledMovement` | `String?` | Boolean-like cancellation flag coming as text, not a real JSON boolean in this model. | Usually `"false"`; code notes uppercase boolean may also appear |
| `vesselIMO` | `String` | IMO number of the vessel. | `9758387` |
| `vesselName` | `String?` | Vessel name. | `INDIGO ACE` |
| `scheduledTime` | `Date?` | Planned/scheduled start time of the movement. | `2026-05-16 22:30:00.000` |
| `underwayTime` | `Date?` | Actual time the vessel movement began / got underway. | `2026-05-16 22:48:24.097` |
| `offTime` | `Date?` | Actual or planned completion time of the movement, depending on status/source behavior. Can be empty if not finished yet. | `2026-05-17 01:30:00.000` or `""` |
| `foreDraft` | `String?` | Forward draft of the vessel, stored as text but representing a numeric depth value. | `15.4100` |
| `aftDraft` | `String?` | Aft draft of the vessel, stored as text but representing a numeric depth value. | `23.0000` |
| `from_stop_location_id` | `String?` | Numeric identifier of the origin location. | `3` |
| `from_stop_location_code` | `String?` | Short code of the origin location. | `SEA`, `C15`, `O04` |
| `from_stop_location` | `String` | Human-readable origin location name. | `SEA`, `PCCA CARGO DOCK #15` |
| `to_stop_location_id` | `String?` | Numeric identifier of the destination location. | `62` |
| `to_stop_location_code` | `String?` | Short code of the destination location. | `C15`, `GV1`, `SEA` |
| `to_stop_location` | `String` | Human-readable destination location name. | `PCCA CARGO DOCK #15`, `GULF COAST GROWTH VENTURES` |
| `movement_agency` | `String` | Name of the vessel/port agency handling the movement. | `Max Shipping, Inc.` |
| `movement_agency_code` | `String?` | Short code or normalized label for the agency. | `MAX SHIP`, `PROMAR` |
| `lineHandler` | `String?` | Company responsible for line handling/mooring operations. May be empty. | `CARLSEN`, `COASTAL BEND MOOR`, `""` |
| `tugName` | `String?` | Despite the field name, code comments say this is actually the towing company, not necessarily a single tug vessel name. | `SUDERMAN AND YOUNG`, `BAY HOUSTON TOWING` |
| `pilotNo` | `String?` | Pilot identifier(s) assigned to the movement. Can contain one or multiple comma-separated values. | `16`, `05`, `01,04,18` |
| `cargo_function` | `String?` | Cargo operation context associated with the movement. | Seen values: `OTHER`, `LOADING`, `STANDBY` |
| `product_code` | `String?` | Product/cargo description associated with the movement. Can be empty, especially for departures/standby. | `NO CARGO`, `CRUDE OIL- LIQUID BULK`, `"` |

---
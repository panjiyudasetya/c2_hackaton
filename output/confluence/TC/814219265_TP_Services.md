---
id: confluence:814219265
source: confluence
type: page
space: TC
title: TP Services
author: Joaquin Marquez Bugella
date: '2025-08-01'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/814219265
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/814219265
---
# TP Services

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/814219265  

## Content

The application has a set of services that can be split into main and auxiliary.

# Quick reference

| **Service** | **Character** | **Remarks** |
| --- | --- | --- |
| `AtaAtdService` | Auxiliary | Used in `MessageHandler` |
| `AuthenticationService` | **Main** | Used to authenticate via Platfrom |
| `BoardBoardService` | Auxiliary | Used in `MessageHandler` |
| `CargillBotlekPlanningExportService` | Auxiliary | Used in `VisitService` |
| `CargoManifestService` | **Main** | Used in:   * `CargoOperationsDetailsCargillController` * `TerminalController` |
| `DateTimeService` | Auxiliary | To return a DataTimeConverter object (it could be done via Spring auto-wired Beans |
| `EtaService` | Auxiliary | A wrapper of **Platform**’s `FutureShipClient`. Used in:   * `PeriodicEtaUpdateService` * `TerminalVisitService` |
| `FavoriteShipService` | **Main** | Used in: `FavoriteShipsController` |
| `LayByBerthService` | **Main** | Used in:   * `LayByBerthController` * `MessageHandler` |
| `LocksService` | Auxiliary | It could have been implemented in VisitService as both use the `terminalConfigurationDataSource` and the purpose is to update the visits related to the lock provided on an incoming message from the queue.  Used in `MessageHandler` |
| `MessageHandler` | **Main** | Async data input to handle messages of the types:   * `TerminalEvent` * `TerminalNearbyEvent` * `CargoBargeEvent` * `TankerBargeEvent` * `ConfirmedBerthEvent` * `LockEvent`   or if the `eventType` is `AREA` |
| `PeriodicEtaUpdateService` | **Main** | Used to regularly update etas via `EtaService` as a Spring Scheduled task. |
| `PersonService` | **~~Main~~** Auxiliary | Used in the `PersonController`. Actually not used (only one Person in the mongo collection). |
| `RelationshipService` | **NOT USED** | Absolutely not used anywhere in the app. Also, no working use-case (scheduled task or indirect use |
| `ShipBookletExportService` | ~~Auxiliary~~ **Main** | To export Cargogil or Yara cargo operations in Excel format. |
| `SlackMessageService` | Auxiliary | To report incorrect situations or data issues |
| `TerminalOccupationService` | **Main** | Only to get data.  Used in `TerminalController` |
| `TerminalPlannerEmailService` | **Main** | To send via email reports to clients and internal operational notifications. It uses Sendgrid as mail provider. |
| `VisitService` | **Main** | Possible, the main/center service. Used widely across the entire application.  **Note** that the filename `TerminalVisitService.kt` is not aligned to the class name `VisitService`. |
| `UserActivityService` | Auxiliary | Service to log on a regular basis the user’s last timestamp activity. |
| `UserManagementService` | Auxiliary | Service to set roles to`TerminalPlannerUser`s via a the `UserManagementController`.  This service and the controller seem unfinished. |
| `UserProfileService` | **Main** | Used to obtain the `UserProfile` and `ProfileSettings` from the authenticated `TerminalPlannerUser` via `UserProfileController`.  Note that, the models `UserProfile`, `UserFeatureSettings` and `ProfileSettings`, seem to follow a relational database model structure – as in not enjoying the non-relational database capabilities. |
| `YaraPlanningExportService` | **Main** | Used to export the Yara Planning for a given terminal (of theirs, of course). |
| `YaraScheduleClient` | Auxiliary | Client (service) to retrieve the Yara’s terminal schedules.  Used by the `SyncService`. |
| `SyncService` | **Main** | Used by `VisitController` and as a Spring Scheduled task to update Yara’s terminal visits. |
| `CargoOperationsDetailsKpiService` | **Main** | Used by the `KpiController`to retrieve a set of defined KPIs |

Notes:

**Authentication** is currently done via Platform and token authentication via `auth-credentials-shared-secret` (by `auth-credentials-refresh-token`) skeleton library.
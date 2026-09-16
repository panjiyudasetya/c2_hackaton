---
id: confluence:493256711
source: confluence
type: page
space: TC
title: 0. Project inventory
author: Joaquin Marquez Bugella
date: '2025-02-27'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/493256711
explicit_links:
- jira:DEV-554
- jira:DEV-553
- jira:DEV-549
- jira:DEV-551
- jira:DEV-552
- jira:DEV-550
- jira:DEV-584
- jira:DEV-580
- jira:DEV-579
- jira:DEV-575
- jira:DEV-571
- jira:DEV-576
- jira:DEV-574
- jira:DEV-564
- jira:DEV-516
- jira:DEV-570
- jira:DEV-578
- jira:DEV-560
- jira:DEV-561
- jira:DEV-562
- jira:DEV-563
- jira:DEV-565
- jira:DEV-566
- jira:DEV-567
- jira:DEV-568
- jira:DEV-569
- jira:DEV-572
- jira:DEV-573
- jira:DEV-577
- jira:DEV-581
- jira:DEV-515
- jira:DEV-518
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/493256711
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/495091714/1.+Code-base+git+migration#Large-files-in-the-repository
---
# 0. Project inventory

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/493256711  

## Content

#FFF0B3

Work in progress

none

# Introduction

Once projects get listed, classified and phases organized (**who** will do **what** and **when**), each agreed candidate can follow the Generic guide can be found in the corresponding sibling pages.

# Inventory, classification and plan

**Project amount:** `360`.

Columns:

* **Relevancy:** Primary, secondary, experimental or student.
* **Audiency:** Internal or customer.
* **Active** (According to the repository activity)**:** yes or no.
* **End type:** backend, frontend, DataEngineering, classic standalone (i.e. bash or python scripts) or other (i.e. configuration files or themes).

1
1
incomplete
 remember group by app (backend and frontend together).

3
3
incomplete
 complete table with this <https://docs.google.com/spreadsheets/d/1RR3TD70hZFpWusEJFRV72ly3VTlb3Lw8ToUD-coOt_0/edit?gid=1670761139#gid=1670761139> 

| **Project** | **Jira** | **Status** | **Phase** | **CICD need** | **Relevancy** | **Audience** | **Active** | **End Type** | **Remarks** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [portlocaltime-backend](https://bitbucket.org/teqplay/portlocaltime-backend) | [DEV-554](https://teqplaybv.atlassian.net/browse/DEV-554) | **Migrated** | 0 | yes | Primary | Internal | YES | Backend | This only has an environment on the production cluster. |
| [scrapeshark-backend](https://bitbucket.org/teqplay/scrapeshark-backend) | [DEV-553](https://teqplaybv.atlassian.net/browse/DEV-553) | **Migrated** | 0 | yes | Primary | Internal | YES | Backend |  |
| [shipsparelogistics-backend](https://bitbucket.org/teqplay/shipsparelogistics-backend) | [DEV-549](https://teqplaybv.atlassian.net/browse/DEV-549) | **Migrated** | 0 | yes | Primary | Customer | YES | Backend | ssl |
| [cargooptima-backend](https://bitbucket.org/teqplay/cargooptima-backend) | [DEV-551](https://teqplaybv.atlassian.net/browse/DEV-551) | **Migrated** | 0 | yes | Secondary | Customer\* | YES | Backend |  |
| [routescout](https://bitbucket.org/teqplay/routescout) | [DEV-552](https://teqplaybv.atlassian.net/browse/DEV-552) | **Migrated** | 0 | yes | Primary | Internal | YES | Backend |  |
| [pdatool](https://bitbucket.org/teqplay/pdatool) | [DEV-550](https://teqplaybv.atlassian.net/browse/DEV-550) | **Migrated** | 0 | yes | Primary | Customer | YES | Backend | It has been renamed to the standards. |
| [etl\_airflow](https://bitbucket.org/teqplay/etl_airflow) | [DEV-584](https://teqplaybv.atlassian.net/browse/DEV-584) | **Migrated** | 1 | ??? | Primary | Customer | YES | DataEngineering |  |
| [vesselvoyage-backend](https://bitbucket.org/teqplay/vesselvoyage-backend) | [DEV-580](https://teqplaybv.atlassian.net/browse/DEV-580) | **Migrated** | 1 | yes | Primary | Internal | YES | Backend |  |
| [vesselmatcher-backend](https://bitbucket.org/teqplay/vesselmatcher-backend) | [DEV-579](https://teqplaybv.atlassian.net/browse/DEV-579) | **Migrated** | 1 | yes | Primary | Customer | YES | Backend |  |
| [skeleton-plugins](https://bitbucket.org/teqplay/skeleton-plugins) | [DEV-575](https://teqplaybv.atlassian.net/browse/DEV-575) | **Migrated** | 1 | yes | Primary | Internal | YES | Backend |  |
| [portcallplus](https://bitbucket.org/teqplay/portcallplus) | [DEV-571](https://teqplaybv.atlassian.net/browse/DEV-571) | **Migrated** | 1 | yes | Primary | Internal | YES | Backend |  |
| [smartfleet](https://bitbucket.org/teqplay/smartfleet) | [DEV-576](https://teqplaybv.atlassian.net/browse/DEV-576) | **Migrated** | 1 | yes | Primary | Customer | YES | Backend | Develop was updated with Master changes. |
| [routescout-v2](https://bitbucket.org/teqplay/routescout-v2) | [DEV-574](https://teqplaybv.atlassian.net/browse/DEV-574) | **Migrated** | 1 | yes | Primary | Internal | YES | Backend | Customer is Platform  snapshot models are not produced, instead, non-master versions are published together in the same S3 path: <https://eu-west-1.console.aws.amazon.com/s3/buckets/repo.teqplay.nl?bucketType=general&prefix=release%2Fnl%2Fteqplay%2Froutescout%2Fmodels%2F&region=eu-west-1&showversions=false#>.  It has a complex ci/cd:   * each environment (`production` and `develop`) consists of two submodules (`graph` and `route-planning`). |
| [csi](https://bitbucket.org/teqplay/csi) | [DEV-564](https://teqplaybv.atlassian.net/browse/DEV-564) | **Migrated** | 1 | yes | Primary | Internal | YES | Backend |  |
| [skeleton-backend](https://bitbucket.org/teqplay/skeleton-backend) | [DEV-516](https://teqplaybv.atlassian.net/browse/DEV-516) | **Migrated** | 1 ~~2~~ | ??? | Secondary | Internal | YES | Backend | It’s the base backend project using the skeleton, starting point of every new project.  Promoted to phase 1 on JoostL request. |
| [poma](https://bitbucket.org/teqplay/poma) | [DEV-570](https://teqplaybv.atlassian.net/browse/DEV-570) | **Migrated** | 1 | yes | Primary | Internal | YES | Frontend |  |
| [vesselcompliance-backend](https://bitbucket.org/teqplay/vesselcompliance-backend) | [DEV-578](https://teqplaybv.atlassian.net/browse/DEV-578) | **Migrated** | 1 | yes | Primary | Customer | YES | Backend |  |
| [ssl](https://bitbucket.org/teqplay/ssl) |  | **Migrated** | 1 | yes | Primary | Customer | YES | Frontend |  |
| [cargooptima](https://bitbucket.org/teqplay/cargooptima) |  | **Migrated** | 1 | yes | Secondary | Customer\* | YES | Frontend |  |
| [ais-engine](https://bitbucket.org/teqplay/ais-engine) | [DEV-560](https://teqplaybv.atlassian.net/browse/DEV-560) | **Migrated** | 1 | yes | Primary | Internal | YES | Backend |  |
| [api](https://bitbucket.org/teqplay/api) | [DEV-561](https://teqplaybv.atlassian.net/browse/DEV-561) | **Migrated** | 1 | yes | Primary | Internal | YES | Backend |  |
| [backendportreporter](https://bitbucket.org/teqplay/backendportreporter) | [DEV-562](https://teqplaybv.atlassian.net/browse/DEV-562) | **Migrated** | 1 | yes | Primary | Customer | YES | Backend |  |
| [chorus-backend](https://bitbucket.org/teqplay/chorus-backend) | [DEV-563](https://teqplaybv.atlassian.net/browse/DEV-563) | **Migrated** | 1 | yes | Primary | Customer | YES | Backend |  |
| [csi-frontend](https://bitbucket.org/teqplay/csi-frontend) |  | **Migrated** | 1 | yes | Primary | Internal | YES | Frontend | Renamed to csi |
| [driftpredictor-backend](https://bitbucket.org/teqplay/driftpredictor-backend) | [DEV-565](https://teqplaybv.atlassian.net/browse/DEV-565) | **Migrated** | 1 | yes | Primary | Internal | YES | Backend |  |
| [fuelboss-backend](https://bitbucket.org/teqplay/fuelboss-backend) | [DEV-566](https://teqplaybv.atlassian.net/browse/DEV-566) | **Migrated** | 1 | yes | Primary | Customer | YES | Backend |  |
| [functionalmonitoring-backend](https://bitbucket.org/teqplay/functionalmonitoring-backend) | [DEV-567](https://teqplaybv.atlassian.net/browse/DEV-567) | **Migrated** | 1 | yes | Primary | Internal**?** | No? | Backend |  |
| [keycloak-theme](https://bitbucket.org/teqplay/keycloak-theme) |  | **Migrated** | 1 | ??? | Primary | Customer | YES | Frontend | Used by PortReporter for the login page theme |
| [nexmoservice](https://bitbucket.org/teqplay/nexmoservice) | [DEV-568](https://teqplaybv.atlassian.net/browse/DEV-568) | **Migrated** | 1 | yes | Primary |  | YES | Backend |  |
| [onthemap](https://bitbucket.org/teqplay/onthemap) |  | **Migrated** | 1 | yes | Primary | Internal | YES | Frontend |  |
| [pdatool-frontend](https://bitbucket.org/teqplay/pdatool-frontend) |  | **Migrated** | 1 | yes | Primary | Customer | YES | Frontend | Renamed to pdatool |
| [platform](https://bitbucket.org/teqplay/platform) | [DEV-569](https://teqplaybv.atlassian.net/browse/DEV-569) | **Migrated** | 1 | yes | Primary | Internal | YES | Backend | It is, we still need to keep this one alive as long as we have backend running. Meaning we need to create a custom CI script for this as this one is very different from the rest… |
| [poma-backend](https://bitbucket.org/teqplay/poma-backend) | [DEV-570](https://teqplaybv.atlassian.net/browse/DEV-570) | **Migrated** | 1 | yes | Primary | Internal | YES | Backend |  |
| [ssl-app](https://bitbucket.org/teqplay/ssl-app) |  | **In progress** | 1 | yes | Primary | Customer | YES | Frontend |  |
| [portmatcher](https://bitbucket.org/teqplay/portmatcher) | [DEV-572](https://teqplaybv.atlassian.net/browse/DEV-572) | **Migrated** | 1 | yes | Primary | Internal | YES | Backend |  |
| [portreporter-frontend](https://bitbucket.org/teqplay/portreporter-frontend) |  | **Migrated** | 1 | yes | Primary | Customer | YES | Frontend |  |
| [pto-etl](https://bitbucket.org/teqplay/pto-etl) | [DEV-573](https://teqplaybv.atlassian.net/browse/DEV-573) | **Migrated** | 1 | yes | Primary | Customer | YES | Backend |  |
| [pto-frontend](https://bitbucket.org/teqplay/pto-frontend) |  | **Migrated** | 1 | yes | Primary | Internal | YES | Frontend | Renamed to pto |
| [riverguide-binnenvaart](https://bitbucket.org/teqplay/riverguide-binnenvaart) |  | **Migrated** | 1 | yes | Primary | Customer | YES | Frontend+ | Frontend + App |
| [riverguide-friesland](https://bitbucket.org/teqplay/riverguide-friesland) |  | **Migrated** | 1 | yes | Primary | Customer | YES | Frontend | Discontinuing… |
| [routescout-v2-frontend](https://bitbucket.org/teqplay/routescout-v2-frontend) |  | **Migrated** | 1 | yes | Primary | Internal | YES | Frontend | Renamed to routescout-v2 |
| [terminal-planner](https://bitbucket.org/teqplay/terminal-planner) |  | **Migrated** | 1 | yes | Primary | Customer | YES | Frontend |  |
| [terminalplanner-backend](https://bitbucket.org/teqplay/terminalplanner-backend) | [DEV-577](https://teqplaybv.atlassian.net/browse/DEV-577) | **Migrated** | 1 | yes | Primary | Customer | YES | Backend |  |
| [timeline](https://bitbucket.org/teqplay/timeline) |  | **Migrated** | 1 | yes | Primary | Internal | YES | Frontend |  |
| [usermanagementdashboard](https://bitbucket.org/teqplay/usermanagementdashboard) |  | **Migrated** | 1 | yes | Primary | Internal | Yes? | Frontend | Gatekeeper, used for Platform (backend). Renamed repo to `gatekeeper` |
| [vessel-compliance](https://bitbucket.org/teqplay/vessel-compliance) |  | **Migrated** | 1 | yes | Primary | Customer | YES | Frontend | Renamed to vesselcompliance to match backend |
| [vesselmatcher](https://bitbucket.org/teqplay/vesselmatcher) |  | **Migrated** | 1 | yes | Primary | Customer | YES | Frontend |  |
| [vesselvoyage](https://bitbucket.org/teqplay/vesselvoyage) |  | **Migrated** | 1 | yes | Primary | Internal | YES | Frontend |  |
| [backendcasey](https://bitbucket.org/teqplay/backendcasey) | [DEV-581](https://teqplaybv.atlassian.net/browse/DEV-581) | **Migrated** | 1 | yes | Primary |  |  |  | **Primary** / Secondary, is operationally being used by Yara |
| [etdpredictor](https://bitbucket.org/teqplay/etdpredictor) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | yes | Primary | Internal |  | Backend |  |
| [aislib](https://bitbucket.org/teqplay/aislib) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | ~~yes~~ | Primary |  | YES |  |  |
| [authenticator](https://bitbucket.org/teqplay/authenticator) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | ~~yes~~ | Primary | Internal | YES | Backend | It doesn’t have CI scripts, AFAIK. |
| [aws-scripts](https://bitbucket.org/teqplay/aws-scripts) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | ~~yes~~ | Primary |  | YES | Backend | It doesn’t have CI scripts, AFAIK. |
| [kubernetes-scripts](https://bitbucket.org/teqplay/kubernetes-scripts) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | No | Primary | DevOps | YES | Other | No CI |
| [ml-driftpredictor](https://bitbucket.org/teqplay/ml-driftpredictor) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | No? | Primary | Internal | YES | Backend | Only contains the machine learning part |
| [dataflow\_dag](https://bitbucket.org/teqplay/dataflow_dag) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | ?? | Primary | Customer | YES | DataEngineering | Python project, does it have a deployment in k8s via circleci? **Not yet used in production …** |
| [dataflow\_plugins](https://bitbucket.org/teqplay/dataflow_plugins) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | ?? | Primary | Customer | YES | DataEngineering |  |
| [dataflow\_stream](https://bitbucket.org/teqplay/dataflow_stream) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Excluded** | 2 | ?? | Primary | Customer | YES | DataEngineering | Panji indicated it wasn't needed. |
| [dataflow\_dag\_pocca](https://bitbucket.org/teqplay/dataflow_dag_pocca) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | ?? | Primary | Customer | YES | DataEngineering | Added on 2025-02-19 |
| [dataflow\_dag\_apmt](https://bitbucket.org/teqplay/dataflow_dag_apmt) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | ?? | Primary | Customer | YES | DataEngineering | Added on 2025-02-19 |
| [datasciencebackend](https://bitbucket.org/teqplay/datasciencebackend) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | No | Primary | Internal | YES | Backend |  |
| [platform-scripts](https://bitbucket.org/teqplay/platform-scripts) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | yes | Primary | DevOps | YES | Other |  |
| [intellij-settings](https://bitbucket.org/teqplay/intellij-settings) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | ??? | Primary |  |  | Other | Do we still use this in the backend??? We use ktlint now for the backend? |
| [iris](https://bitbucket.org/teqplay/iris) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 3 | No | Secondary |  |  |  | Not primary relevant , not operational running and not planning to ever deploy again, only want to keep it for the archive |
| [portpublisher-backend](https://bitbucket.org/teqplay/portpublisher-backend) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | No | Secondary | Internal | YES | Backend | Is not anywhere in development, is deployed but probably can be removed. so could easily be 2nd |
| [pdfrenderer](https://bitbucket.org/teqplay/pdfrenderer) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | No? | Secondary | Internal | YES | Backend | AFAIK only used for the datastore, which is not anywhere in development, so could easily be 2nd. Also in CargoOptima for an experimental feature. |
| [backend-bunkerplanner](https://bitbucket.org/teqplay/backend-bunkerplanner) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | Yes | Secondary |  | NO | Backend | NOT USED ANYMORE CAN STAY |
| [backend-isps](https://bitbucket.org/teqplay/backend-isps) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | No | Secondary |  | NO? | Backend | archive only |
| [bridgepredictor](https://bitbucket.org/teqplay/bridgepredictor) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | No | Secondary |  | No? | Backend | Archive only |
| [datascience-scripts](https://bitbucket.org/teqplay/datascience-scripts) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | No | Secondary | Internal |  | Classic standalone |  |
| [datastore-backend](https://bitbucket.org/teqplay/datastore-backend) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | No | Secondary | Internal | No? | Backend |  |
| [kantoordinator](https://bitbucket.org/teqplay/kantoordinator) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | yes | Secondary |  |  |  |  |
| [lineupcalculator-backend](https://bitbucket.org/teqplay/lineupcalculator-backend) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | No | Secondary | Internal | No? | Backend | Vasyl’s |
| [mailtemplates](https://bitbucket.org/teqplay/mailtemplates) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | ??? | Secondary | Internal | No | Other |  |
| [mongo-exporter](https://bitbucket.org/teqplay/mongo-exporter) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | No | Secondary | Internal | NO? | Backend |  |
| [port-support](https://bitbucket.org/teqplay/port-support) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | No | Secondary |  | No? | Frontend |  |
| [portcallreports](https://bitbucket.org/teqplay/portcallreports) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | No | Secondary | ? | NO |  | Can probably go? @ Richard |
| [portsupport-backend](https://bitbucket.org/teqplay/portsupport-backend) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | No | Secondary | Customer | NO | Backend |  |
| [qa-java-tests](https://bitbucket.org/teqplay/qa-java-tests) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | Yes | Secondary | Internal | YES | Backend | This runs in the develop cluster in the Testing namespace. So no CI needed |
| [timeline-public](https://bitbucket.org/teqplay/timeline-public) |  | **Migrated** | 2 | Yes | Secondary | Customer | YES | Frontend | Still under development no real customers yet |
| [teqplaytools](https://bitbucket.org/teqplay/teqplaytools) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | No | Secondary | Internal | NO? | Backend | Can probably go? @ Richard |
| [terminallineup-backend](https://bitbucket.org/teqplay/terminallineup-backend) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | No | Secondary | Internal | NO | Backend | 2 2 incomplete  check if still in use in PRP. |
| [vertom-backend](https://bitbucket.org/teqplay/vertom-backend) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | No | Secondary |  | No? |  | archive only |
| [web-sdk](https://bitbucket.org/teqplay/web-sdk) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | No | Secondary |  | NO |  |  |
| [backend-security-analysis](https://bitbucket.org/teqplay/backend-security-analysis) | [DEV-515](https://teqplaybv.atlassian.net/browse/DEV-515) | **Migrated** | 2 | ~~Yes~~ (until taken over by depencytrack) | Secondary | Internal | YES | Backend | DependencyTrack will replace the purpose of this repo.  **No CI workflow implemented!** Agreed on this with |
| [~~frontend-security-analysis~~](https://bitbucket.org/teqplay/frontend-security-analysis) |  | **Excluded** | ~~2~~ | ~~No~~ | ~~Secondary~~ | ~~Internal~~ | ~~YES~~ | ~~Frontend~~ | ~~No need for conversion, taken over by DependencyTrack~~ |
| [teqplay-ui](https://bitbucket.org/teqplay/teqplay-ui) |  | **Migrated** | 2 | No | Primary | Internal | YES | Other | Old Teqplay frontend library - only git needed |
| [casey](https://bitbucket.org/teqplay/casey) |  | **Migrated** | 2 | yes | Primary | Customer | NO | Other | **Primary** / Secondary, is operationally being used by Yara |
| [bunkerplanner-frontend](https://bitbucket.org/teqplay/bunkerplanner-frontend) |  | **Migrated** | 2 | yes | Primary |  | YES | Frontend |  |
| [account-portal](https://bitbucket.org/teqplay/account-portal) |  | **Migrated** | 2 | Yes | Secondary | Internal | YES | Frontend |  |
| [chorus-component-library](https://bitbucket.org/teqplay/chorus-component-library) |  | **Migrated** | 2 | Yes | Secondary | Internal | Yes | Other | Library |
| [chorus-utility-library](https://bitbucket.org/teqplay/chorus-utility-library) |  | **Migrated** | 2 | Yes | Secondary | Internal | Yes | Other |  |
| [eta-analysis-tool](https://bitbucket.org/teqplay/eta-analysis-tool) |  | **Migrated** | 2 | Ask Michel | Secondary | Internal | No? | Frontend | archive only |
| [eta-predictor](https://bitbucket.org/teqplay/eta-predictor) |  | **Migrated** | 2 | Ask Michel | Secondary | Internal | NO? | Frontend |  |
| [geolocation-utils](https://bitbucket.org/teqplay/geolocation-utils) |  | **Migrated** | 2 | No | Secondary | Internal | No? | Frontend | Migrate repo |
| [laybyberth](https://bitbucket.org/teqplay/laybyberth) |  | **Migrated** | 2 | No | Experimental | ??? | No | Frontend |  |
| [react-useform](https://bitbucket.org/teqplay/react-useform) |  | **Migrated** | 2 | ??? | Secondary | Internal | No? | Other | Library |
| [riverguide.eu](https://bitbucket.org/teqplay/riverguide.eu) |  | **Migrated** | 2 | Yes | Secondary | Customer | Yes | Frontend | Website |
| [rolemapper-frontend](https://bitbucket.org/teqplay/rolemapper-frontend) |  | **Migrated** | 3 | Yes | Experimental |  |  |  |  |
| [shipmeister](https://bitbucket.org/teqplay/shipmeister) |  | **Migrated** | 2 | Yes | Secondary |  | Yes | Frontend | Website |
| [teqplay-icon-font](https://bitbucket.org/teqplay/teqplay-icon-font) |  | **Migrated** | 2 | ??? | Secondary | Internal |  | Other |  |
| [variance](https://bitbucket.org/teqplay/variance) | [DEV-518](https://teqplaybv.atlassian.net/browse/DEV-518) | **Migrated** | 3 | No | Experimental | Customer | NO? | Backend |  |
| [apigateway-backend](https://bitbucket.org/teqplay/apigateway-backend) | [DEV-518](https://teqplaybv.atlassian.net/browse/DEV-518) | **Migrated** | 3 | No | Experimental |  |  | Backend |  |
| [cargooptima-etl](https://bitbucket.org/teqplay/cargooptima-etl) | [DEV-518](https://teqplaybv.atlassian.net/browse/DEV-518) | **Migrated** | 3 | ??? | Experimental |  | NO |  |  |
| [co2calculations-backend](https://bitbucket.org/teqplay/co2calculations-backend) | [DEV-518](https://teqplaybv.atlassian.net/browse/DEV-518) | **Migrated** | 3 | No | Experimental |  |  |  |  |
| [co2calculations-frontend](https://bitbucket.org/teqplay/co2calculations-frontend) | [DEV-518](https://teqplaybv.atlassian.net/browse/DEV-518) | **Migrated** | 3 | No | Experimental |  |  |  |  |
| [congestion-predictor-backend](https://bitbucket.org/teqplay/congestion-predictor-backend) | [DEV-518](https://teqplaybv.atlassian.net/browse/DEV-518) | **Migrated** | 3 | No | Experimental |  |  |  |  |
| [congestion-predictor-frontend](https://bitbucket.org/teqplay/congestion-predictor-frontend) | [DEV-518](https://teqplaybv.atlassian.net/browse/DEV-518) | **Migrated** | 3 | No | Experimental |  |  |  |  |
| [coroutines\_samples](https://bitbucket.org/teqplay/coroutines_samples) | [DEV-518](https://teqplaybv.atlassian.net/browse/DEV-518) | **Migrated** | 3 | No | Experimental |  |  | Backend |  |
| [eks-workshop](https://bitbucket.org/teqplay/eks-workshop) | [DEV-518](https://teqplaybv.atlassian.net/browse/DEV-518) | **Migrated** | 3 | No | Experimental | Internal | NO | Backend |  |
| [emissioncalculator-backend](https://bitbucket.org/teqplay/emissioncalculator-backend) | [DEV-518](https://teqplaybv.atlassian.net/browse/DEV-518) | **Migrated** | 3 | No | Experimental |  |  |  |  |
| [etl\_project](https://bitbucket.org/teqplay/etl_project) | [DEV-518](https://teqplaybv.atlassian.net/browse/DEV-518) | **Migrated** | 3 | ??? | Experimental | Internal | NO | DataEngineering |  |
| [fleetintel-backend](https://bitbucket.org/teqplay/fleetintel-backend) | [DEV-518](https://teqplaybv.atlassian.net/browse/DEV-518) | **Migrated** | 3 | No | Experimental |  |  |  |  |
| [ghostshiphunter](https://bitbucket.org/teqplay/ghostshiphunter) | [DEV-518](https://teqplaybv.atlassian.net/browse/DEV-518) | **Migrated** | 3 | No | Experimental | ??? | No | Backend |  |
| [ml-portpredictor](https://bitbucket.org/teqplay/ml-portpredictor) | [DEV-518](https://teqplaybv.atlassian.net/browse/DEV-518) | **Migrated** | 3 | No | Experimental | Internal | NO |  |  |
| [smart-tug-detection-analysis](https://bitbucket.org/teqplay/smart-tug-detection-analysis) | [DEV-518](https://teqplaybv.atlassian.net/browse/DEV-518) | **Migrated** | 3 | No | Experimental |  | NO |  |  |
| [smart-tug-detection-backend](https://bitbucket.org/teqplay/smart-tug-detection-backend) | [DEV-518](https://teqplaybv.atlassian.net/browse/DEV-518) | **Migrated** | 3 | No | Experimental |  | NO |  |  |
| [smart-tug-detection-frontend](https://bitbucket.org/teqplay/smart-tug-detection-frontend) | [DEV-518](https://teqplaybv.atlassian.net/browse/DEV-518) | **Migrated** | 3 | No | Experimental |  | NO |  |  |
| [sof-ocr](https://bitbucket.org/teqplay/sof-ocr) | [DEV-518](https://teqplaybv.atlassian.net/browse/DEV-518) | **Migrated** | 3 | No | Experimental | Internal | YES |  |  |
| [teqplay-r-sdk](https://bitbucket.org/teqplay/teqplay-r-sdk) | [DEV-518](https://teqplaybv.atlassian.net/browse/DEV-518) | **Migrated** | 3 | No | Experimental |  |  |  |  |
| [teqplay-ui-tabs](https://bitbucket.org/teqplay/teqplay-ui-tabs) | [DEV-518](https://teqplaybv.atlassian.net/browse/DEV-518) | **Migrated** | 3 | No | Experimental |  | NO |  |  |
| [terminalplannerscriptyara](https://bitbucket.org/teqplay/terminalplannerscriptyara) | [DEV-518](https://teqplaybv.atlassian.net/browse/DEV-518) | **Migrated** | 3 | No | Experimental | Internal | NO |  |  |
| [trang-test-app](https://bitbucket.org/teqplay/trang-test-app) | [DEV-518](https://teqplaybv.atlassian.net/browse/DEV-518) | **Migrated** | 3 | No | Experimental | Internal | NO | Backend |  |
| [vesselmatcher-locations](https://bitbucket.org/teqplay/vesselmatcher-locations) | [DEV-518](https://teqplaybv.atlassian.net/browse/DEV-518) | **Migrated** | 3 | No | Experimental |  |  | Frontend |  |
| [data-store](https://bitbucket.org/teqplay/data-store) |  | **Migrated** | 4 | No |  |  | Yes | Frontend | Was already on GitHub |
| [fleetintel-frontend](https://bitbucket.org/teqplay/fleetintel-frontend) |  | **Migrated** | 4 | No |  |  | NO | Frontend | archive only |
| [isps-frontend](https://bitbucket.org/teqplay/isps-frontend) |  | **Migrated** | 4 | No |  |  | NO? | Frontend | archive only |
| [autonomous-dashboard](https://bitbucket.org/teqplay/autonomous-dashboard) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [foosball-react](https://bitbucket.org/teqplay/foosball-react) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [lineupcalculator-frontend](https://bitbucket.org/teqplay/lineupcalculator-frontend) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [mrn-frontend](https://bitbucket.org/teqplay/mrn-frontend) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [old\_portreporter](https://bitbucket.org/teqplay/old_portreporter) |  | **Migrated** | 4 |  |  |  |  |  | Renamed to portreporter-old |
| [port-oracle-frontend](https://bitbucket.org/teqplay/port-oracle-frontend) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [riverguide](https://bitbucket.org/teqplay/riverguide) |  | **Migrated** | 4 |  |  |  |  |  | Renamed to riverguide-angular for clarity |
| [riverguide-components](https://bitbucket.org/teqplay/riverguide-components) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [riverguide-react](https://bitbucket.org/teqplay/riverguide-react) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [riverguide-recreant](https://bitbucket.org/teqplay/riverguide-recreant) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [riverguide-recreational](https://bitbucket.org/teqplay/riverguide-recreational) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [riverguide-vts](https://bitbucket.org/teqplay/riverguide-vts) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [riverscout-frontend](https://bitbucket.org/teqplay/riverscout-frontend) |  | **Migrated** | 4 |  |  |  |  |  | Renamed to routescout-v1 |
| [seaguide](https://bitbucket.org/teqplay/seaguide) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [viewer](https://bitbucket.org/teqplay/viewer) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [teqplay-wiki](https://bitbucket.org/teqplay/teqplay-wiki) |  | **Migrated** | 4 |  |  |  |  |  | Replaced with confluence mostly. Richard should know more about this. |
| [geowhiteboard](https://bitbucket.org/teqplay/geowhiteboard) |  | **Migrated** | 4 | No | Student |  | No | Frontend |  |
| [adminfrontend](https://bitbucket.org/teqplay/adminfrontend) |  | **Migrated** | 4 | No | Student |  | No? | Frontend |  |
| [portreporter-stats](https://bitbucket.org/teqplay/portreporter-stats) |  | **Migrated** | 4 | No | Obsolete | Internal | NO? | Frontend | Heroku FE that states “There's nothing here, yet.” |
| [acoustic-events](https://bitbucket.org/teqplay/acoustic-events) |  | **Migrated** | 4 | No |  |  | NO? | Frontend | archive only |
| [aisbuddy](https://bitbucket.org/teqplay/aisbuddy) |  | **Migrated** | 4 | No |  |  | No | Frontend | Archive only |
| [portreporter.info](https://bitbucket.org/teqplay/portreporter.info) |  | **Migrated** | 4 | No |  |  | No | Frontend |  |
| [vertom-frontend](https://bitbucket.org/teqplay/vertom-frontend) |  | **Migrated** | 4 | No |  |  |  |  |  |
| [anchorpredictor](https://bitbucket.org/teqplay/anchorpredictor) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [anchorreport](https://bitbucket.org/teqplay/anchorreport) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [android-ar-demo](https://bitbucket.org/teqplay/android-ar-demo) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [apmt\_eta](https://bitbucket.org/teqplay/apmt_eta) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [apmt\_etd\_anchor](https://bitbucket.org/teqplay/apmt_etd_anchor) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [approachroute](https://bitbucket.org/teqplay/approachroute) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [appstore](https://bitbucket.org/teqplay/appstore) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [ar-demo-web](https://bitbucket.org/teqplay/ar-demo-web) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [ar-places](https://bitbucket.org/teqplay/ar-places) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [arduino](https://bitbucket.org/teqplay/arduino) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [areamonitor-cordova](https://bitbucket.org/teqplay/areamonitor-cordova) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [areamonitor-phonegap](https://bitbucket.org/teqplay/areamonitor-phonegap) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [areamonitor-web](https://bitbucket.org/teqplay/areamonitor-web) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [armadareport](https://bitbucket.org/teqplay/armadareport) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [avantimockup](https://bitbucket.org/teqplay/avantimockup) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [barge-dashboard](https://bitbucket.org/teqplay/barge-dashboard) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [bargejourneyanalysis](https://bitbucket.org/teqplay/bargejourneyanalysis) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [berth-monitor-zeeland](https://bitbucket.org/teqplay/berth-monitor-zeeland) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [berthexposer](https://bitbucket.org/teqplay/berthexposer) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [berthexposer2](https://bitbucket.org/teqplay/berthexposer2) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [berths-heatmap](https://bitbucket.org/teqplay/berths-heatmap) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [berthvisits](https://bitbucket.org/teqplay/berthvisits) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [binnenvaart-tijdlijn](https://bitbucket.org/teqplay/binnenvaart-tijdlijn) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [bms-bridgekeepergui](https://bitbucket.org/teqplay/bms-bridgekeepergui) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [boat-assistant](https://bitbucket.org/teqplay/boat-assistant) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [boatway](https://bitbucket.org/teqplay/boatway) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [boatway\_rws](https://bitbucket.org/teqplay/boatway_rws) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [boeidashboard](https://bitbucket.org/teqplay/boeidashboard) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [bridgemanagementsystem](https://bitbucket.org/teqplay/bridgemanagementsystem) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [bridgemonitor](https://bitbucket.org/teqplay/bridgemonitor) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [bunkermonitor](https://bitbucket.org/teqplay/bunkermonitor) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [bunkermonitor-backend](https://bitbucket.org/teqplay/bunkermonitor-backend) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [cargo-amount](https://bitbucket.org/teqplay/cargo-amount) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [cargo-dashboard](https://bitbucket.org/teqplay/cargo-dashboard) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [cargostream](https://bitbucket.org/teqplay/cargostream) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [ciws-rws-demoversion](https://bitbucket.org/teqplay/ciws-rws-demoversion) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [cocap](https://bitbucket.org/teqplay/cocap) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [composedevents](https://bitbucket.org/teqplay/composedevents) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [containerveiligheid](https://bitbucket.org/teqplay/containerveiligheid) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [control-tower](https://bitbucket.org/teqplay/control-tower) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [cranedashboard](https://bitbucket.org/teqplay/cranedashboard) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [crudeoilreport](https://bitbucket.org/teqplay/crudeoilreport) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [dash](https://bitbucket.org/teqplay/dash) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [dashboard\_jorik](https://bitbucket.org/teqplay/dashboard_jorik) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [dashboard\_wouter](https://bitbucket.org/teqplay/dashboard_wouter) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [databricks-proxy](https://bitbucket.org/teqplay/databricks-proxy) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [databricksexport](https://bitbucket.org/teqplay/databricksexport) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [departure-predictor](https://bitbucket.org/teqplay/departure-predictor) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [depth-data-viewer](https://bitbucket.org/teqplay/depth-data-viewer) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [digitwin](https://bitbucket.org/teqplay/digitwin) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [dma-commons](https://bitbucket.org/teqplay/dma-commons) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [dma-developers](https://bitbucket.org/teqplay/dma-developers) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [druktekaart](https://bitbucket.org/teqplay/druktekaart) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [e-navigation](https://bitbucket.org/teqplay/e-navigation) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [eagle-eye-backend](https://bitbucket.org/teqplay/eagle-eye-backend) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [eagle-eye-frontend](https://bitbucket.org/teqplay/eagle-eye-frontend) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [emo\_project](https://bitbucket.org/teqplay/emo_project) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [encounter](https://bitbucket.org/teqplay/encounter) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [etd\_predict](https://bitbucket.org/teqplay/etd_predict) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [etdhouston](https://bitbucket.org/teqplay/etdhouston) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [etdpredictorpython](https://bitbucket.org/teqplay/etdpredictorpython) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [eventexplorer](https://bitbucket.org/teqplay/eventexplorer) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [experiments](https://bitbucket.org/teqplay/experiments) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [fleet-monitor-dashboard](https://bitbucket.org/teqplay/fleet-monitor-dashboard) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [foosball](https://bitbucket.org/teqplay/foosball) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [foosball-backend](https://bitbucket.org/teqplay/foosball-backend) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [fuelconsumptionadvisor-backend](https://bitbucket.org/teqplay/fuelconsumptionadvisor-backend) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [fuelconsumptionadvisor-frontend](https://bitbucket.org/teqplay/fuelconsumptionadvisor-frontend) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [graduate-intern-toolkit](https://bitbucket.org/teqplay/graduate-intern-toolkit) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [graduationbasmeijer](https://bitbucket.org/teqplay/graduationbasmeijer) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [graphhopper](https://bitbucket.org/teqplay/graphhopper) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [gulfofpersia](https://bitbucket.org/teqplay/gulfofpersia) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [hackaton-antwerpen](https://bitbucket.org/teqplay/hackaton-antwerpen) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [helloworld](https://bitbucket.org/teqplay/helloworld) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [hydroetaprediction](https://bitbucket.org/teqplay/hydroetaprediction) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [image-labeler](https://bitbucket.org/teqplay/image-labeler) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [inlineediting-backend](https://bitbucket.org/teqplay/inlineediting-backend) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [inspector](https://bitbucket.org/teqplay/inspector) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [jori-thesis](https://bitbucket.org/teqplay/jori-thesis) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [koerswijzer](https://bitbucket.org/teqplay/koerswijzer) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [lerna-test](https://bitbucket.org/teqplay/lerna-test) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [ligplaatsvrij](https://bitbucket.org/teqplay/ligplaatsvrij) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [lineuppredictor-backend](https://bitbucket.org/teqplay/lineuppredictor-backend) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [lineuppredictor-frontend](https://bitbucket.org/teqplay/lineuppredictor-frontend) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [lng\_flows](https://bitbucket.org/teqplay/lng_flows) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [lockdetection](https://bitbucket.org/teqplay/lockdetection) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [lotfa-chat](https://bitbucket.org/teqplay/lotfa-chat) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [lunch-api](https://bitbucket.org/teqplay/lunch-api) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [manoverboord](https://bitbucket.org/teqplay/manoverboord) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [marketanalysis](https://bitbucket.org/teqplay/marketanalysis) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [ml-event-detection](https://bitbucket.org/teqplay/ml-event-detection) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [moaa-trainer](https://bitbucket.org/teqplay/moaa-trainer) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [monitor](https://bitbucket.org/teqplay/monitor) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [monitoringandcontrol-frontend](https://bitbucket.org/teqplay/monitoringandcontrol-frontend) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [myservices](https://bitbucket.org/teqplay/myservices) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [nei](https://bitbucket.org/teqplay/nei) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [nei-backend](https://bitbucket.org/teqplay/nei-backend) |  | **Migrated** | 4 |  |  |  |  |  | Not running anymore for years |
| [newportprocess](https://bitbucket.org/teqplay/newportprocess) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [node-js-loraserver](https://bitbucket.org/teqplay/node-js-loraserver) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [nomination-mapper-frontend](https://bitbucket.org/teqplay/nomination-mapper-frontend) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [open-boatway](https://bitbucket.org/teqplay/open-boatway) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [panamacanaleta](https://bitbucket.org/teqplay/panamacanaleta) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [pascalvoc-to-image](https://bitbucket.org/teqplay/pascalvoc-to-image) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [patterndetection](https://bitbucket.org/teqplay/patterndetection) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [periodicreport](https://bitbucket.org/teqplay/periodicreport) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [pilotonboard](https://bitbucket.org/teqplay/pilotonboard) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [platformmonitor](https://bitbucket.org/teqplay/platformmonitor) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [port\_oracle](https://bitbucket.org/teqplay/port_oracle) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [port-admin](https://bitbucket.org/teqplay/port-admin) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [port-insight](https://bitbucket.org/teqplay/port-insight) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [port-mapper](https://bitbucket.org/teqplay/port-mapper) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [port-performance-benchmark](https://bitbucket.org/teqplay/port-performance-benchmark) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [port-turnaround-powerbi-dashboard](https://bitbucket.org/teqplay/port-turnaround-powerbi-dashboard) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [port2port](https://bitbucket.org/teqplay/port2port) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [portaiscoverage](https://bitbucket.org/teqplay/portaiscoverage) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [portcall-simulator](https://bitbucket.org/teqplay/portcall-simulator) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [portcallestimator](https://bitbucket.org/teqplay/portcallestimator) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [portmapperanchorareadetection](https://bitbucket.org/teqplay/portmapperanchorareadetection) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [portmapperbackend](https://bitbucket.org/teqplay/portmapperbackend) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [portmapperfrontend](https://bitbucket.org/teqplay/portmapperfrontend) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [portoracle](https://bitbucket.org/teqplay/portoracle) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [portoracle-backend](https://bitbucket.org/teqplay/portoracle-backend) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [portreporter-automated-tests](https://bitbucket.org/teqplay/portreporter-automated-tests) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [portreporter-validator](https://bitbucket.org/teqplay/portreporter-validator) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [portstatistics](https://bitbucket.org/teqplay/portstatistics) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [portturnaround](https://bitbucket.org/teqplay/portturnaround) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [postman\_api\_test](https://bitbucket.org/teqplay/postman_api_test) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [pushbargeushou](https://bitbucket.org/teqplay/pushbargeushou) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [quayplanner](https://bitbucket.org/teqplay/quayplanner) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [raspberry-pi-udp-parser](https://bitbucket.org/teqplay/raspberry-pi-udp-parser) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [rfqoptimizer](https://bitbucket.org/teqplay/rfqoptimizer) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [rg-refactor](https://bitbucket.org/teqplay/rg-refactor) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [rubenmelchers-graduationproject](https://bitbucket.org/teqplay/rubenmelchers-graduationproject) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [rws-kaartdemonstrator](https://bitbucket.org/teqplay/rws-kaartdemonstrator) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [rws-patrol-demo](https://bitbucket.org/teqplay/rws-patrol-demo) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [satellitedetectionapi](https://bitbucket.org/teqplay/satellitedetectionapi) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [satellitedetectiondashboard](https://bitbucket.org/teqplay/satellitedetectiondashboard) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [satelliteexperiment](https://bitbucket.org/teqplay/satelliteexperiment) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [satelliteimageprocessing](https://bitbucket.org/teqplay/satelliteimageprocessing) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [schedules](https://bitbucket.org/teqplay/schedules) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [scraperpocbackend](https://bitbucket.org/teqplay/scraperpocbackend) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [seaguide-register](https://bitbucket.org/teqplay/seaguide-register) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [service-dependencies](https://bitbucket.org/teqplay/service-dependencies) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [ship\_classification](https://bitbucket.org/teqplay/ship_classification) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [ship-insiders](https://bitbucket.org/teqplay/ship-insiders) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [ship-rating](https://bitbucket.org/teqplay/ship-rating) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [ship-status](https://bitbucket.org/teqplay/ship-status) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [ship-tracking](https://bitbucket.org/teqplay/ship-tracking) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [ship2load](https://bitbucket.org/teqplay/ship2load) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [ship2load-frontend](https://bitbucket.org/teqplay/ship2load-frontend) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [shipcategories](https://bitbucket.org/teqplay/shipcategories) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [shipclassifier](https://bitbucket.org/teqplay/shipclassifier) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [shiphappens](https://bitbucket.org/teqplay/shiphappens) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [shiphappens-front-end](https://bitbucket.org/teqplay/shiphappens-front-end) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [shipinfocsvtokml](https://bitbucket.org/teqplay/shipinfocsvtokml) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [shiploading](https://bitbucket.org/teqplay/shiploading) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [shipmodel](https://bitbucket.org/teqplay/shipmodel) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [shipspassingby](https://bitbucket.org/teqplay/shipspassingby) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [singapore-dashboard](https://bitbucket.org/teqplay/singapore-dashboard) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [singaporebunker](https://bitbucket.org/teqplay/singaporebunker) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [sluismonitor](https://bitbucket.org/teqplay/sluismonitor) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [soaproxy](https://bitbucket.org/teqplay/soaproxy) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [sodaq-lora-pilot](https://bitbucket.org/teqplay/sodaq-lora-pilot) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [table-tennis-frontend](https://bitbucket.org/teqplay/table-tennis-frontend) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [tabletennis-backend](https://bitbucket.org/teqplay/tabletennis-backend) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [tabletennis-frontend](https://bitbucket.org/teqplay/tabletennis-frontend) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [tcpdispatcher](https://bitbucket.org/teqplay/tcpdispatcher) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [teqperiment](https://bitbucket.org/teqplay/teqperiment) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [teqplay-sdk](https://bitbucket.org/teqplay/teqplay-sdk) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [teqplay-ui-deprecated](https://bitbucket.org/teqplay/teqplay-ui-deprecated) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [terminal-viewer](https://bitbucket.org/teqplay/terminal-viewer) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [terminalanalysis](https://bitbucket.org/teqplay/terminalanalysis) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [terminalcharacteristics](https://bitbucket.org/teqplay/terminalcharacteristics) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [terminaldetection](https://bitbucket.org/teqplay/terminaldetection) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [terminalpredictor](https://bitbucket.org/teqplay/terminalpredictor) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [test-lerna-gavin](https://bitbucket.org/teqplay/test-lerna-gavin) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [testing](https://bitbucket.org/teqplay/testing) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [timeline-mobile-notificationsapp](https://bitbucket.org/teqplay/timeline-mobile-notificationsapp) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [timelineapp](https://bitbucket.org/teqplay/timelineapp) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [trailerdashboard](https://bitbucket.org/teqplay/trailerdashboard) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [twitterclassifierkotlinbackend](https://bitbucket.org/teqplay/twitterclassifierkotlinbackend) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [twitterclassifierpythonbackend](https://bitbucket.org/teqplay/twitterclassifierpythonbackend) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [usersimulator](https://bitbucket.org/teqplay/usersimulator) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [varenzh](https://bitbucket.org/teqplay/varenzh) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [vattool](https://bitbucket.org/teqplay/vattool) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [vectorfields](https://bitbucket.org/teqplay/vectorfields) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [version-tracker](https://bitbucket.org/teqplay/version-tracker) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [vertomusermanagement](https://bitbucket.org/teqplay/vertomusermanagement) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [voorspellingen-aankomst-front-end](https://bitbucket.org/teqplay/voorspellingen-aankomst-front-end) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [voyage-planner](https://bitbucket.org/teqplay/voyage-planner) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [vts-operators-inzicht-veiligheid](https://bitbucket.org/teqplay/vts-operators-inzicht-veiligheid) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [wakita](https://bitbucket.org/teqplay/wakita) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [wakita-mobile](https://bitbucket.org/teqplay/wakita-mobile) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [watermonitor](https://bitbucket.org/teqplay/watermonitor) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [waterwaysigns](https://bitbucket.org/teqplay/waterwaysigns) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [wiki](https://bitbucket.org/teqplay/wiki) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [woutervolders-graduationproject](https://bitbucket.org/teqplay/woutervolders-graduationproject) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [zabbix](https://bitbucket.org/teqplay/zabbix) |  | **Migrated** | 4 |  |  |  |  |  |  |
| [moaa](https://bitbucket.org/teqplay/moaa) |  | **Migrated** | 4 |  |  |  |  |  | It contained files larger than 100Mb, so <https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/495091714/1.+Code-base+git+migration#Large-files-in-the-repository> was applied. |
| [vaarweggraph](https://bitbucket.org/teqplay/vaarweggraph) |  | **Migrated** | 4 |  |  |  |  |  | It contained files larger than 100Mb, so <https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/495091714/1.+Code-base+git+migration#Large-files-in-the-repository> was applied. |
| [teqplay-ui-v3](https://bitbucket.org/teqplay/teqplay-ui-v3) |  | **Excluded** | 4 |  |  |  | No | Frontend | Completely encapsulated in core-frontend repo |
| [~~newteqplayui~~](https://bitbucket.org/teqplay/newteqplayui) |  | **Excluded** | 4 | ~~No~~ |  |  | ~~NO~~ |  | please, explain here why |
| [graduation-project](https://bitbucket.org/teqplay/graduation-project) |  | **Disappeared** | 4 |  |  |  |  |  | It disappeared from Bitbucket! |
| [voyage-platform](https://bitbucket.org/teqplay/voyage-platform) |  | **Disappeared** | 4 |  |  |  |  |  | It disappeared from Bitbucket! |
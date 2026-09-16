---
id: confluence:715554825
source: confluence
type: page
space: TC
title: Synchronizing MongoDB Databases During Migration
author: Minh Trang Nguyen (Unlicensed)
date: '2025-09-12'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/715554825
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/715554825
---
# Synchronizing MongoDB Databases During Migration

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/715554825  

## Content

Status: work in progress

The purpose of this document is to describe the MongoDB database synchronization process subsequent to a migration to a new Organization Unit (OU). Activation of the MongoDB instance and the related application in the new environment requires updating the DNS domain address. This document details a method for achieving relatively fast data synchronization.

To begin, create an EBS volume snapshot and share it with another OU. Once MongoDB is installed in the target OU, establish a VPC peering connection between the two OUs. This peering will enable you to connect the OUs and synchronize the missing data from the original database to the new MongoDB instance in the other OU. The VPC peering will also provide access to the MongoDB database in the target OU.

## Solution 1

Linear data reads would be relatively time-consuming. This solution focuses on reading data from MongoDB collections in parallel and synchronizing only missing documents in the target database, as well as removing documents absent from the source database.

Establish connectivity between the VPCs and configure the necessary security groups. The VPC peering procedure is not detailed within this document. For each MongoDB, we will run a corresponding source and target database Pod. Manual database synchronization will be required, with databases being migrated individually.

### Pod solution

A Pod is necessary because a Job cannot establish a persistent server to listen for requests. The application connects to both the source and the target databases. In the target VPC, the application efficiently reads the unique IDs of database collections in parallel. These IDs are then stored in a local cache using RocksDB, a persistent key-value database designed to minimize in-memory data usage. RocksDB was chosen over a memory-based cache due to memory limitations.

Upon reading documents, they are hashed, and the resulting hashes are stored in the cache, associated with their unique IDs. Subsequently, the target application compares these cached hashes with hashes of documents in the target database to identify differences. Discrepancies trigger a synchronization of the document from the source database.

The application connected to the target database listens for gRPC requests. Subsequently, the application in the source database sends gRPC requests to the target application to verify the existence of a collection's unique ID. If the UUID is not found in the target database, the corresponding document is inserted.

The application connected to the target database first reads all unique IDs and stores them in a local RocksDB cache. It then iterates through this faster cache, checking if each unique ID exists in the source database. If a unique ID is not found in the source, the corresponding document is removed from the target database.

**Steps**

* **Snapshot and setup:** Create an EC2 snapshot and set up the application in the new OU.
* **Initial synchronization setup (target):** Install the synchronization tool in the target VPC. This tool will read all unique IDs from the database collections.
* **Synchronization wait:** Wait for the synchronization tool to finish reading all records. This could take some time.
* **DNS update:** Update the Route 53 DNS record to point to the load balancer in the target OU.
* **Verification:** The application should now accept requests in the target OU.
* **Final synchronization setup (source):** Once the source MongoDB no longer receives new data, install the synchronization tool in the source VPC.
* **Start synchronization:** Initiate the synchronization process.
* **Cleanup job:** Concurrently, a job can start to identify and remove outdated documents in the target database.

### Remote Procedure Call (gRPC)

The selection of gRPC is driven by its high efficiency, leading to a substantial improvement in communication speed and overall performance.

### Local RabbitMq

RabbitMQ was implemented due to RocksDB's single-threaded nature. The parallel jobs reading from MongoDB needed a mechanism to queue their output. Therefore, these jobs push data to RabbitMQ, and a separate consumer process handles the writing to the local RocksDB cache.

### Application

The application is written in Rust due to its robust memory management and excellent low-level performance.

## Estimated Time for Synchronization

It depends on the computing resources how fast the synchronisation will be.

| **namespace** | **database** | **name** | **size** | **duration** |
| --- | --- | --- | --- | --- |
| ais-core | ais-stream-dev-mongodb | aisstream | 4,50GB | 45 min - 90 min |
| ais-processing | ais-engine-dev-mongodb | aisengine | 0,5GB | 8 min - 16 min |
| ais-processing | ais-rabbitmq-dev-mongodb | aisrabbitmq | 8GB | 80 min - 160min |
| ais-processing | area-monitor-dev-mongodb | area-monitor | 1GB | 10 min - 20 min |
| ais-processing | event-history-processor-dev | event-history | 32GB | 6 hours - 12 hours |
| ais-processing | ship-history-processor-dev-mongodb | ship-history | 300 GB | 50 hours - 100 hours |
| bunkerplanner | bunkerplanner-dev-mongodb | bunkerplanner | 5MB | 5 min - 10 min |
| bunkerplanner | bunkerplanner-test-mongodb | bunkerplanner | 3MB | 5 min - 10 min |
| bunkerplanner | fuelboss-dev-mongodb | fuelboss | 17MB | 5 min - 10 min |
| bunkerplanner | fuelboss-test-mongodb | fuelboss | 100MB | 5 min - 10 min |
| core-service | poma-sandbox-mongodb | poma, poma\_external, poma\_merged | 82MB, 201MB, 26MB | 20 min - 30 min |
| core-service | routescout-graph-dev-mongodb | routescout | 357MB | 5 min - 10 min |
| customer-apps | mongodb-customer-apps | datastore, portsupport, shipsparelogistics, terminalplanner | 1MB, 1MB, 8MB, 212MB | 20 min - 30 min |
| customer-apps | sednaintegration-dev-mongodb | sednaintegration | 1MB | 5 min - 10 min |
| customer-apps | vesselcompliance-demo-charterer-mongodb | vesselcompliance | 0MB | 0 min |
| customer-apps | vesselcompliance-demo-terminal-mongodb | vesselcompliance | 1MB | 5 min - 10 min |
| customer-apps | vesselcompliance-dev-mongodb | vesselcompliance | 100MB | 5 min - 10 min |
| customer-apps | vesselcompliance-poc-mongodb | vesselcompliance | 1MB | 5 min - 10 min |
| customer-apps | vesselcompliance-staging-mongodb | vesselcompliance | 313MB | 5 min - 10 min |
| customer-apps | vesselmatcher-dev-mongodb | vesselmatcher | 17GB | 3 hours - 6 hours |
| general-service | functionalmonitoring-dev-mongodb | functionalmonitoring | 11GB | 2 hours - 4 hours |
| portcall | portreporter-testing-mongodb | portreporter | 3GB | 30 min - 60 min |
| revents-core | revents-engine-api-mongodb | reventsengine | 28GB | 5 hours - 10 hours |
| revents-core | revents-vesselvoyage-mongodb | vesselvoyage | 0MB | 0 min |
| students | pdatool-dev-mongodb | pdatool | 1MB | 5 min - 10 min |
| voyage | cargooptima-dev-mongodb | cargo-optima | 43MB | 5 min - 10 min |
| voyage | cargooptima-staging-mongodb | cargo-optima, cargo-optima\_20240501 | 7MB, 6MB | 5 min - 10 min |
| voyage | smartfleet-dev-mongodb | smartfleet | 1GB | 10 min - 20 min |
| voyage | vesselvoyage-dev-mongodb | vesselvoyage | 240GB | 40 hours - 80 hours |

\*The database sizes were rounded of

## Solution 2

The second solution involves converting the standalone MongoDB database to a Replica Set. The application, running within the source VPC, will then listen for database changes, store them, and apply these changes to the target database once it becomes available. The target MongoDB will stay a standalone database.

The changes will be stored locally and applied as soon as possible.

* Synchronizing of data is relatively fast comparing to solution 1.
* Little downtime, only when switching the DNS address to the target OU.
* Target MongoDB stays in standalone mode.

The application captures stream changes and persists them chronologically in RabbitMQ. A separate task verifies the availability of the standalone database within the target VPC. Upon confirmation, this task publishes the stored changes to RabbitMQ. Finally, an updater service consumes these messages from RabbitMQ and applies the corresponding modifications to the target MongoDB.

As a result, RabbitMQ will not be populated until the target MongoDB is accessible. Event changes are persistently stored on disk, awaiting synchronization with the target database. This architecture provides a performance advantage over solution 1.

Synchronization script small Mongodb databases

## Solution 3

The third solution involves establishing a clean database and application environment within the target OU and allowing it to populate with data. This approach is particularly relevant for large databases such as `shiphistory` and `eventhistory`. These databases are configured to migrate data to S3 upon reaching a defined threshold. Once the databases have reached this threshold, the application will switch the DNS records.

Potential risks exist with this solution:

* We need to establish a peer-to-peer VPC connection to enable the target Kubernetes cluster's access to internal services (e.g., https://internalapidev.teqplay.dev). This new setup will likely require time for configuration and testing.
* There's some uncertainty regarding the switch of the application DNS address in Route 53.

## No synchronisation for all databases

Applying the solution to all databases isn't efficient. Creating a snapshot, sharing it with the other OU, and then starting the database and application there would be faster.

Given that creating a 1GB EBS snapshot in AWS takes approximately one minute, a planned downtime window is required. This means the application in the source VPC will be unavailable and will not process requests during the snapshot creation. The next phase involves generating the snapshot, sharing it with the target OU, and then deploying the application within that OU. We will then update the DNS record in Route53, associating the existing web address with the new load balancer address in the new OU. It's important to note that the `dev.teqplay.com` hosted zone will not be migrated at this stage. The entire hosted zone will be moved once all applications have been migrated.

The databases listed below are not currently utilizing the synchronization tool.

| **namespace** | **database** | **name** |
| --- | --- | --- |
| ais-core | ais-stream-dev-mongodb | aisstream |
| ais-processing | ais-engine-dev-mongodb | aisengine |
| ais-processing | ais-rabbitmq-dev-mongodb | aisrabbitmq |
| ais-processing | area-monitor-dev-mongodb | area-monitor |
| ais-processing | event-history-processor-dev | event-history |
| bunkerplanner | bunkerplanner-dev-mongodb | bunkerplanner |
| bunkerplanner | bunkerplanner-test-mongodb | bunkerplanner |
| bunkerplanner | fuelboss-dev-mongodb | fuelboss |
| bunkerplanner | fuelboss-test-mongodb | fuelboss |
| core-service | poma-sandbox-mongodb | poma, poma\_external, poma\_merged |
| core-service | routescout-graph-dev-mongodb | routescout |
| customer-apps | mongodb-customer-apps | datastore, portsupport, shipsparelogistics, terminalplanner |
| customer-apps | sednaintegration-dev-mongodb | sednaintegration |
| customer-apps | vesselcompliance-demo-charterer-mongodb | vesselcompliance |
| customer-apps | vesselcompliance-demo-terminal-mongodb | vesselcompliance |
| customer-apps | vesselcompliance-dev-mongodb | vesselcompliance |
| customer-apps | vesselcompliance-poc-mongodb | vesselcompliance |
| customer-apps | vesselcompliance-staging-mongodb | vesselcompliance |
| customer-apps | vesselmatcher-dev-mongodb | vesselmatcher |
| general-service | functionalmonitoring-dev-mongodb | functionalmonitoring |
| portcall | portreporter-testing-mongodb | portreporter |
| revents-core | revents-engine-api-mongodb | reventsengine |
| revents-core | revents-vesselvoyage-mongodb | vesselvoyage |
| students | pdatool-dev-mongodb | pdatool |
| voyage | cargooptima-dev-mongodb | cargo-optima |
| voyage | cargooptima-staging-mongodb | cargo-optima, cargo-optima\_20240501 |
| voyage | smartfleet-dev-mongodb | smartfleet |

## Poma cluster

There are a couple of cluster migration solutions. The simplest approach involves stopping the application, creating a database dump, transferring it to the other VPC, and then importing it. To setup a new MongoDB replica cluster, see document MongoDB replica and standalone database .

The more complex approach entails replicating the environment in the other OU's VPC and orchestrating a failover. The significant hurdle is how to effectively utilize the private Route53 address in this alternative OU. This could be very challenging
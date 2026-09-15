---
id: confluence:196313089
source: confluence
type: page
space: TC
title: Network policies EKS + grouping apps
author: Minh Trang Nguyen (Unlicensed)
date: '2024-03-13'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/196313089
explicit_links: []
---
# Network policies EKS + grouping apps

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/196313089  

## Content

**Status: implemented**

To have more secure network communications between pods in the cluster, the CNI (Container Network Interface) Calico (<https://docs.tigera.io/calico/latest/about> ) is installed in the cluster. It’s one of the most used CNI and is easy to use. In this document the network policies are described in details and is necessary to get an understanding of the implementation.

## Grouping applications

Applications will be grouped across several namespaces and are grouped in a way that it’s not needed for pods to communicate directly with each other over namespaces. Some exceptions are allowed, because restricting too much communications could be to hard to realise. The proposed namespaces are:

* ais-core
* ais-processing
* portcall
* voyage
* core-service
* general-service
* customer-apps
* bunkerplanner
* revents-core
* teqplay-api
* teqplay-fun

The namespace `ais-core` is the starting point where data is flown into and distributed across others services in the cluster. The next namespace which are using the data from `ais-core` is `ais-usage`. Services in `ais-usage` are using the data from `ais-core`.

**namespace ais-core**

| **apps** |
| --- |
| ais-stream |

**namespace ais-processing**

| **apps** |
| --- |
| ais-diff |
| ais-rabbitmq |
| anchor-monitor |
| area-monitor |
| berth-monitor |
| encounter-monitor |
| ship-history |
| ship-history-processor |
| event-converter |
| event-history |
| event-history-processor |

**namespace portcall**

| **apps** |
| --- |
| portcall+ |
| portreporter-monitor |
| portpublisher |
| portreporter |

**namespace pto**

| **apps** |
| --- |
| hydra-encrypted-postgresql |
| pto-etl |

**namespace voyage**

| **apps** |
| --- |
| vesselvoyage |
| smartfleet |
| cargo optima |

**namespace core-service**

| **apps** |
| --- |
| csi |
| emissioncalculator |
| nexmoservice |
| poma |
| portlocaltime |
| portmatcher |
| predictions |
| routescout |

**namespace general-service**

| **apps** |
| --- |
| datascience |
| functional-monitoring |
| nexmo |
| pdf-renderer |
| scrapeshark |
| terminal-lineup |

**namespace customer-apps**

The applications in this namespace aren’t allowed to communicate with each other.

| **apps** |
| --- |
| casey |
| datastore |
| isps |
| ship-spare-logistics |
| terminal-planner |
| vesselcompliance |
| vesselmatcher |

**namespace bunkerplanner**

| **apps** |
| --- |
| bunkerplanner |
| fuelboss |

**namespace revents-core**

| **apps** |
| --- |
| revents-engine-api |
| revents-engine-orchestrator |

**namespace teqplay-api**

| **apps** |
| --- |
| external-api |
| internal-api |

## **Namespaces**

The tables show the namespaces, which have access to other namespaces.

| **Namespace** | kube-system | brokers |
| --- | --- | --- |
| ais-core | x | x |
| ais-usage | x | x |
| portcall | x | x |
| voyage | x | x |
| core-service | x | x |
| general-service | x | x |
| customer-apps | x | x |
| bunkerplanner | x |  |
| teqplay-api | x |  |
| teqplay-fun |  |  |

The various namespaces requires to have access to at least the three namespaces mentioned in the table to work properly.

| **Namespace** | **all namespaces** |
| --- | --- |
| monitoring | x |
| calico-system | x |
| velero | x |
| tigera-operator | x |

## Security tiers

Network policies are associated with pods, thereby restricting both incoming and outgoing ports. Following extensive testing, it has been observed that the implementation of security tiers effectively hinders developers' workflow. The collaborative implementation of RBAC (Role-Based Access Control) and network policy rules is designed to effectively prevent unauthorised users from gaining access.

## Reorganizing apps

To realise the namespaces and grouping of services in the namespaces, services needs to be migrated to the various namespaces. This means downtime for applications. There are two solutions to migrate the applications.

1. Velero backup and restore

For applications which are using a persistent storage, a backup needs to be created first. This means the application needs to be shutdown first and a backup can be made. No new data is allowed to be written to the persistent storage. Particularly, for storage exceeding 200GB, this backup process may extend up to one hour, resulting in a minimum downtime of one hour. Subsequently, the restore process for the persistent storage is relatively swift.

Upon completion of these backup and restore procedures, the Helm chart must be installed in the new namespace. Potential obstacles should be addressed preemptively, especially when the application encounters difficulties in rolling out to the new namespace. While this solution has undergone testing, it was not entirely successful, as the application failed to attain the Ready status. Certain adjustments were required for the solution to function correctly. Unfortunately, this proved impractical due to the extended duration required to transfer storage data.

2. Custom migration scripts

The migration script will change the `ReclaimPolicy` for some persistent volumes from `Delete` to `Retain`. The claim needs to be moved to the new namespace. Before moving the claim, the claim reference of the persistent volume needs to removed, so it can be used in another namespace. This process could mean a downtime of at least 1 minute, depending on the application.

As in solution 1 the Helm chart needs to be installed into the new namespace. This solution was also tested and worked without any problems.
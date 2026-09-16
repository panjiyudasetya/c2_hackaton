---
id: confluence:807043081
source: confluence
type: page
space: TC
title: Migration to new DEV cluster
author: Joost Laurman
date: '2025-11-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/807043081
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/807043081
---
# Migration to new DEV cluster

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/807043081  

## Content

After a period of extensive preparations and setting-up we are starting the migration of the current DEV cluster to the new DEV cluster, which is hosted in a different AWS Organizational Unit (OU). Why?

* Increase security (minimize risk intrusion in DEV to compromise PROD)
* Increase maintainability
* Increase cost spit insights

Basically we are moving from this architecture with only one AWS Organizational unit, one VPC and thus also one VPN to access all:

into this architecture, where the DEV domain has a separate AWS Organizational Unit, its own VPC and thus also its own VPN.

To make the architecture fully balanced again, we would need to do the same step with the Production domain, but since this is not adding relevant additional security and costing a pretty significant investment, we did not decide to make that move yet.

What will be the impact on you?

* Next to your AWS access to Teqplay, you will soon see also the Develop OU

* You will receive a second VPN account, allowing you to connect to the new DEV VPC
* In the next few weeks, we will migrate all DEV applications from the old DEV cluster to the new DEV cluster. At the moment things have moved, you are expected to make future deployments also in the new cluster. The movement will be done per namespace, starting with the BROKERS namespace.
* We will start with moving the BROKERS namespace. As soon as this is done, we will start moving individual applications per namespace. The brokers will run, from that moment on, solely in the new DEV VPC.
* Current status can be found in table below

|  |  |  |
| --- | --- | --- |
| **Status** | **Activity** | **Date Completed** |
| done | Design and document all steps to setup new cluster | 01-07 |
| done | Setup AWS DEV OU and DEV cluster including keycloak and all security related setups | 22-07 |
| done | Setup a connection between old DEV and new DEV cluster | 15-07 |
| done | Design and document all steps for data migration | 22-07 |
| done | Test migration scripts | 05-08 |
| done | Setup NATS in new cluster and reroute all traffic via the NATS in new DEV cluster | 05-09 |
| done | Setup RabbitMQ in new cluster and reroute all traffic via the new DEV cluster | 04-09 |
| done | Move namespace AIS-CORE all applications and databases | 14-10 |
| done | Move namespace AIS PROCESSING all applications and databases | 24-10 |
| done | Move namespace PORTCALL all applications and databases | 22-09 |
| done | Move namespace VOYAGE all applications and databases | 27-10 |
| done | Move namespace BUNKERPLANNER all applications and databases | 7-10 |
| done | Move namespace REVENTS-CORE all applications and databases | 23-10 |
| done | Move namespace REVENTS-JOBS all applications and databases | 23-10 |
| done | Move namespace CUSTOMER-APPS all applications and databases | 23-09 |
| done | Move namespace DATA ENGINEERING all applications and databases | 03-11 |
|  | Move namespace MONITORING all applications and databases |  |
| done | Move namespace TEQPLAY-API all applications and databases | 03-11 |
|  |  |  |
---
id: confluence:1124040705
source: confluence
type: page
space: TC
title: Airflow Pocca Live Streaming data with RabbitMQ
author: Ryan Kharisma Rakhmat
date: '2026-02-11'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1124040705
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1124040705
---
# Airflow Pocca Live Streaming data with RabbitMQ

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1124040705  

## Content

# Backgrounds

We need a streaming data platform that always subscribe data from RabbitMQ Queue.

# Configurations

There are 2 configs here needs to update in helmchart.

Secrets → users that registered in RabbitMQ

Config Maps → some connections from Airflow to RabbitMQ

| `RABBITMQ_VESSEL_VOYAGE_HOSTNAME` | `RABBITMQ_VESSEL_VOYAGE_QUEUE_NAME` | `RABBITMQ_VESSEL_VOYAGE_VHOST` | `RABBITMQ_VESSEL_VOYAGE_MSG_COUNT` | `RABBITMQ_VESSEL_VOYAGE_PORT` |
| --- | --- | --- | --- | --- |
| `rabbitmq.teqplay.nl` | `VesselVoyage-PTO-pocca` | `VesselVoyage` | 1000 | 5672 |

# Related DAGS

| **No** | **DAG NAME** | **DESCRIPTIONS** |
| --- | --- | --- |
| 1 | rabbitmq\_sof\_subscriber\_deferrable | subscriber dags for sof data with deferrable |
| 2 | rabbitmq\_sof\_updated\_handler | update the staging tables |
| 3 | rabbitmq\_sof\_deleted\_handler | delete the staging tables |
| 4 | ods\_sof\_\_streaming\_updated | updated streaming data transformed into ods |
| 5 | ods\_sof\_\_streaming\_deleted | deleted streaming data is deleted in ODS |
| 6 | fact\_sof\_\_streaming\_updated | updated streaming data transformed into fact |
| 7 | fact\_sof\_\_streaming\_deleted | deleted streaming data is deleted in FACT |

# Screenshot

airflow:

rabbitmq:

lens:
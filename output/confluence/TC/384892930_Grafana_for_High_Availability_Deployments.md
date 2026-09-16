---
id: confluence:384892930
source: confluence
type: page
space: TC
title: Grafana for High Availability Deployments
author: Minh Trang Nguyen (Unlicensed)
date: '2024-06-24'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/384892930
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/384892930
---
# Grafana for High Availability Deployments

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/384892930  

## Content

Grafana functions as an instrumental platform for generating alerts when resource usage reaches specified thresholds, and for the graphical visualization of metrics. The deployment of Grafana has been architected with a focus on high availability. This configuration significantly diverges from the standalone version due to the incorporation of additional components. This configuration is designed to ensure uninterrupted alerting and metrics display, even during cluster upgrades.

## Setup

* Grafana
* AWS S3 for plugins
* Postgres database (RDS)
* Redis Sentinel cluster
* OIDC via Keycloak

AWS S3 is utilized for the retrieval of Grafana plugins, as the use of Grafana's persistent disk is not feasible. The plugins are fetched during the initialization of the instances.

The employment of a Postgres database facilitates the use of multiple Grafana instances. This Postgres database is housed within AWS RDS, specifically within the `support-apps-dev` and `support-apps` databases, where the Grafana database is established. The `support-apps` database is specifically tailored for smaller applications that do not necessitate substantial resources.

The Redis Sentinel cluster plays a crucial role in Grafana alerts, maintaining a record of all processed alerts across the various Grafana instances.

User authentication in Grafana is managed through Keycloak. A user's permissions within Grafana are contingent upon the group to which they are assigned.

## Configuration

The configuration settings for the Grafana application can be found in the `grafana-dev-config` or `grafana-config` configmaps, located within the `monitoring` namespace. The `auth.generic_oauth` section specifically houses the settings for Keycloak OIDC.

Alerting is activated through `unified_alerting`, while the default `alerting` system, which is now deprecated, has been disabled. Within that section, the Redis address is also configured.

## Secrets

The secrets for the database are stored in the `grafana-database` secret. These include the database name, user, and password, which are generated through the command line and subsequently added to the secret.

**Example: steps to create database, user and permissions.**

CREATE ROLE grafana\_dev LOGIN NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
CREATE DATABASE grafana\_dev;
ALTER DATABASE grafana\_dev OWNER TO grafana\_dev;
ALTER USER grafana\_dev WITH PASSWORD '<RANDOM GENERATED PASSWORD>';
GRANT USAGE, SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO grafana\_dev;
GRANT USAGE, SELECT, UPDATE ON ALL SEQUENCES IN SCHEMA public TO grafana\_dev;

The host endpoint is situated within Amazon Web Services' Relational Database Service (AWS RDS).

The Grafana setup for the DEVELOP cluster does not include Priority 1 alerts, as it is not deemed critical to disturb individuals during off-hours for this particular cluster.
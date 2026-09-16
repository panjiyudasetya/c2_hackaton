---
id: confluence:576913411
source: confluence
type: page
space: TC
title: Dora Metrics via DevLake
author: Jamie de Leest
date: '2024-12-17'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/576913411
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/576913411
---
# Dora Metrics via DevLake

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/576913411  

## Content

16falsedisclisttrue

## DevGuide

To correctly measure metrics for DORA and engineering throughput, our tools need to be used in a specific way:

* Jira

  + Create JIRA tickets with “Incident” issue type (custom) when there is a code related incident that requires code to be resolved.
  + Make sure that tickets are moved to done and are indicated as resolved. Some boards may not support this so check if there is a green check in the ticket, next to the status button.
* GitHub

  + When starting to Review a pull request, add a comment to indicate you are starting the review.

## Apache DevLake

### Introduction

Apache DevLake is a tool for aggregating, analyzing, and visualizing data across various development platforms, enabling teams to gain actionable insights and improve productivity. This proposal outlines the setup and integration of Apache DevLake, connecting it to GitHub and Jira, and the utilization of Grafana dashboards to monitor and analyze development metrics. Our focus will be on measuring DORA metrics, which can identify bottlenecks in the technology value stream.

The open-source tool is a system made up of several components, which are explained in the architecture section of the [documentation](https://devlake.apache.org/docs/v1.0/Overview/Architecture/). In short, the system contains the following parts:

* **Config UI:** A user interface for configuring connections
* **API Server:** The main programmatic interface of DevLake**.**
* **Runner:** The runner does all the heavy-lifting for executing tasks
* **Database:** The database stores both DevLake's metadata and user data collected by data pipelines
* **Plugins:** Plugins enable DevLake to collect and analyze dev data
* **Dashboards:** Dashboards deliver data and insights to DevLake users via grafana.

### Deployment

Apache DevLake recommends two ways of deployment:

* with the use of a [docker-compose](https://devlake.apache.org/docs/v1.0/GettingStarted/DockerComposeSetup)
* with the use of [helm](https://devlake.apache.org/docs/v1.0/GettingStarted/HelmSetup)

In our case, since we use Kubernetes, I would suggest using the Helm approach.

You can also choose to connect DevLake to your own [external Grafana](https://devlake.apache.org/docs/v1.0/GettingStarted/DockerComposeSetup#can-i-use-an-external-grafana-instead-of-running-grafana-in-docker). The documentation explains how to do this with Docker Compose, but I believe it should also be possible with Helm.

### Customization & extensibility

Apache DevLake is highly customizable in its configuration, its start with the connections Devlake can connect to multiple git, ci/cd  and issue tools for collecting metrics.

each connection has a different configuration, one thing that is the same is that you need to select a data scope, a data scope is a repository for a git connection or a pipeline for ci/cd tools or finally a project board for your project management tool

For more information about customization or specific information about a connection, please refer to the [documentation](https://devlake.apache.org/docs/Config%20UI).

#### Github Connection

For measuring metrics for development and deployments we will be using a connection with GitHub.

The connection with GitHub is handled by Personal Access Tokens(PATs), there are two kinds of tokens: classic or a fine-grained token.  The classic token gives full access to the repositories but has better performance because it can be used with GraphQL, the fine-grained token you can give read only tokens but it's slower.

for more information about PATs refer to the [documentation](https://devlake.apache.org/docs/Configuration/GitHub#personal-access-tokens).

After establishing a connection you can add your data scopes and associate scope config

Here, you can select the existing scope config or create a new config. It is good practice to separate the config for backend and frontend projects, because they use different steps in the deployment process

The GitHub connection offers the most options because GitHub can be used for repositories, CI/CD, and issue tracking. In our case, we use Jira for issue tracking, so that can be excluded from the GitHub configuration.

When creating a scope config you will first need to select the Data Entities you want to collect. in our example we don't need Issue tracking for our GitHub scope

After selecting your data entities, you will be given a few options for how the data will be transformed to compare metrics. In our case, we only need to configure what counts as a deployment. For this, you can either track GitHub Deployments and match them to an environment, or convert a successful workflow into a deployment by matching the name of the workflow or one of its jobs.

For more information about configuring a github connection, please refer to the [documentation](https://devlake.apache.org/docs/Configuration/GitHub).

#### Jira Connection

For measure metrics about Change Failure Rate (CFR) and Median Time Till Restore (MTTR) we will be using a connection to Jira

The connection with Jira is handled by Atlassian account API token, this token has the same access as your account and can also be used for the confluence api.

to learn about how to create an API token, please refer to the [documentation](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/).

After establishing a connection you can add your data scopes and associate scope config

Here, you can select the existing scope config or create a new config. These configurations depends on the issue types on the project boards

When creating a scope config you will first need to select the Data Entities you want to collect. In our example use Issue tracking and cross domain (cross domain is used to connect issues to commits).

After selecting your data entities, you will be given a few options for how the data will be transformed to compare metrics. In our case for dora metrics, we only need to configure what type of jira issue counts as an incident, for some extra metrics you can also assign types for Requirements, bugs and Story Points for some extra insight. for linking commits to issues you'll need to setup cross-domain via the development panel

For the MTTR metrics a incident issue needs to be tagged we the [resolved status](https://confluence.atlassian.com/cloudkb/best-practices-on-using-the-resolution-field-968660796.html)

For more information about configuring a jira connection, please refer to the [documentation](https://devlake.apache.org/docs/Configuration/Jira/).

#### Project setup

To use your connections you'll need to create projects. In here you can group je data scopes i would recommend to group frontend and backend in one project.

In the project you can also specify the syncing policy.

And you can also see the status of the data collection and transformation.

### Metrics Dashboards

For Displaying the metrics DevLake uses Grafana, this can be its own instance or it can be integrated in your Grafana setup. DevLake offers a lot of premade Dashboards.

Some notable dashboards:

Dora Metrics:

Weekly Bug Retro:

Engineering Throughput and Cycle Time:
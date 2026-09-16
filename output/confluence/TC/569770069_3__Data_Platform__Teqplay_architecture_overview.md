---
id: confluence:569770069
source: confluence
type: page
space: TC
title: '3. Data Platform: Teqplay architecture overview'
author: Panji Y. Wiwaha
date: '2025-04-17'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/569770069
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/569770069
---
# 3. Data Platform: Teqplay architecture overview

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/569770069  

## Content

# Introduction

Figure 1 provides a higher-level overview of the Teqplay data platform architecture. It shows that the platform consists of three main components: Teqplay Airflow, Dataflow Plugins, and Dataflow Dags.

Figure 1 - Teqplay Data Platform Architecture

## Teqplay Airflow

In Teqplay, we use Airflow to express and execute ETL workflows as *Directed Acyclic Graphs* (DAG). It includes utilities for scheduling tasks, monitoring task progress, and handling task dependencies. We chose [the Airflow package from Bitnami](https://bitnami.com/stack/apache-airflow) because it is easy to manage, deploy, and upgrade to the latest version on the cloud.

Bitnami chart bootstraps an [Apache Airflow](https://github.com/bitnami/containers/tree/main/bitnami/airflow) deployment on a [Kubernetes](https://kubernetes.io/) cluster using the [Helm](https://helm.sh/) package manager. Therefore, it can be used with [Kubeapps](https://kubeapps.dev/) to deploy and manage Helm Charts in clusters. Apart from that, they also provide us a sidecar to pull our dags from git repositories whenever we push changes to a specific branch.

Airflow has five core components, which are:

* 𝗪𝗲𝗯 𝗦𝗲𝗿𝘃𝗲𝗿: Airflow UI where we can monitor and manage DAGs, variables, connections, and checks logs. It provides a dashboard that helps us visualize our data workflows and their progress and troubleshoot any issues.
* 𝗦𝗰𝗵𝗲𝗱𝘂𝗹𝗲𝗿: This component is responsible for managing task execution. It monitors the DAGs and schedules tasks based on their dependencies and timing configurations. It ensures that tasks are executed in the right order and at the right time.
* 𝗘𝘅𝗲𝗰𝘂𝘁𝗼𝗿: The Executor’s primary role involves executing tasks actively. It interacts with the Scheduler to obtain task details and initiates the required processes or containers for task execution.
* 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 **Queue**: We use the Celery Executor for task delegations and Redis for the message broker. This broker acts as a middleman between the Scheduler and the Workers. It ensures smooth communication by passing task details from the Scheduler to the Workers, ensuring tasks are executed reliably and efficiently across the distributed system.
* 𝗪𝗼𝗿𝗸𝗲𝗿: The Worker is a component that performs any tasks the Executor assigns. Depending on the chosen Executor, it can be a separate process or container. Workers are responsible for executing the code or scripts defined in your tasks and reporting their status to the Executor.

However, in general, we use Airflow to:

* Ingest data periodically from Teqplay Apps (CSI, POMA, Vessel Voyage) and store them in the Teqplay data warehouse.
* Read data from the Teqplay data warehouse, transform it into the STAR Schema, and periodically store it in the Teqplay data mart.
* Consume stream messages from Vessel voyage, pick the necessary messages, and process them by running the corresponding DAGs.

## Dataflow Plugins

Plugins are a set of pre-defined variables or functions (**macros**) that can be used in our DAG definitions. Plugins can also be custom web **views** that we want to build on top of the Airflow application.

In our case, we use plugins to decouple a common code base or functions unrelated to the DAG definitions, such as:

* Teqplay or Customer API clients.
* Common or utility functions.

We put our macros in the [dataflow plugins](https://bitbucket.org/teqplay/dataflow_plugins) Bitbucket repository. When we set up Bitnami Airflow on Kubernetes, additional YAML configuration is needed so they can pull them.

git:
plugins:
enabled: true
repositories:
- branch: develop
name: dataflow\_plugins
path: ""
repository: https://x-token-auth:{TOKEN\_AUTH}@bitbucket.org/teqplay/dataflow\_plugins.git

You can find the `{TOKEN_AUTH}` on the vault warden by searching vault item with the name `Bitbucket:dataflow_plugins`.

Also, we need to register the path of our plugins to the Python path as follows on the YAML configuration:

extraEnvVars:
- name: PYTHONPATH
value: ${PYTHONPATH}:/opt/bitnami/airflow/plugins/git\_dataflow-plugins

## Dataflow DAGs

DAG is a collection of the tasks we want to run, organized in a way that can reflect their relationships and dependencies. In Teqplay, we define the ETL workflows by keeping this mindset in mind:

* SQL is a universal language used to perform data ingestion, transformations, and data loading.
* If we can’t do ETL with SQL, use the data frame processing, such as Pandas, Polars, or Dask.
* If it’s not enough, use any Python packages that can help you with your specific workflow.

Keeping that mindset is important for maintainability and makes them open for any collaborations with external teams, such as data scientists or ML engineers. We put our DAG definitions in the [dataflow dag](https://bitbucket.org/teqplay/dataflow_dag) Bitbucket repository.

Our dags divided into two categories, which are:

1. Mart DAGs—The DAGs define an ETL workflow that can run in batch at a specific time/event or periodically. Following the STAR Schema modeling, the workflow transforms the Teqplay operational data source into dimension and fact tables.
2. Warehouse DAGs—The DAGs define an ETL workflow to pull (ingest) Teqplay data through the APIs (POMA API, CSI API, Vessel Voyage API), transform it into relational models, and then load it into a data warehouse as a Teqplay operational data source.  
   Some of the warehouse DAG listen to Teqplay events published by specific apps, such as VesselVoyage. Once the particular events that we need are acknowledged, another DAG will be run to process incoming messages from those events.

Additional YAML configuration is needed when we set up Bitnami Airflow on Kubernetes.

git:
dags:
enabled: true
repositories:
- branch: develop
name: dataflow\_dag
path: ""
repository: https://x-token-auth:{TOKEN\_AUTH}@bitbucket.org/teqplay/dataflow\_dag.git

You can find the `{TOKEN_AUTH}` on the vault warden by searching vault item with the name `Bitbucket:dataflow_dag`.

Similarly with plugins, we also need to register the path of our plugins to the Python path as follows on the YAML configuration:

extraEnvVars:
- name: PYTHONPATH
value: ${PYTHONPATH}:/opt/bitnami/airflow/plugins/git\_dataflow-dag

For further explanation of how Teqplay data is being processed, check out this article.

## Complete YAML configuration

### Development

* Environment variables

extraEnvVars:
- name: AIRFLOW\_\_WEBSERVER\_\_EXPOSE\_CONFIG
value: "true"
- name: AIRFLOW\_\_CORE\_\_MAX\_MAP\_LENGTH
value: "6144"
- name: AIRFLOW\_\_CORE\_\_TEST\_CONNECTION
value: Enabled
- name: AIRFLOW\_\_CORE\_\_FERNET\_KEY
value: MzA1MEdqWW9DUEljemc1UXJoaGd3RUZSQzZ6QzVvcDE=
- name: AIRFLOW\_\_CORE\_\_INTERNAL\_API\_SECRET\_KEY
value: 5W5QEvuHzJHv9vUljjQngw==
- name: AIRFLOW\_\_WEBSERVER\_\_SECRET\_KEY
value: MktrNWxpU2VEVmNLNnd5Zm0zTzRFN1JqR0dtcmtmcW8=
- name: PYTHONPATH
value: ${PYTHONPATH}:/opt/bitnami/airflow/dags/git\_dataflow-dag:/opt/bitnami/airflow/plugins/git\_dataflow-plugins
- name: ETL\_ENV
value: dev
- name: S2S\_API\_CLIENT\_ID
value: {FIND-IT-ON-VAULT-WARDEN}
- name: S2S\_API\_CLIENT\_SECRET
value: {FIND-IT-ON-VAULT-WARDEN}
- name: RABBITMQ\_DEV\_USER
value: {FIND-IT-ON-VAULT-WARDEN}
- name: RABBITMQ\_DEV\_PWD
value: {FIND-IT-ON-VAULT-WARDEN}

* Airflow variables

| **Key** | **Value** | **Description** |
| --- | --- | --- |
| DATAFLOW\_LOG\_FOLDER | /opt/bitnami/airflow/logs | Base directory for the Airflow log folder. |
| DATAFLOW\_MAX\_LOG\_ AGE\_IN\_DAYS | 14 | Maximum age of the log files in days. |
| STAGING\_SOF\_\_BACKFILL\_ SCHEDULE | @daily | @weekly | @monthly | Backfill schedule for the staging statement of facts. |
| STAGING\_SOF\_\_BACKFILL\_ START\_DATE | YYYY-MM-DD | The start date of the backfill schedule is for the staging statement of facts. |
| STAGING\_SOF\_\_SQL\_FILTER\_\_BACKFILL\_UNLOCODES | NLRTM,NLAMS | List of port unlocodes to be backfilled, separated with a comma. |
| STAGING\_VOYAGE\_\_ BACKFILL\_SCHEDULE | @daily | @weekly | @monthly | Backfill schedule for the voyage. |
| STAGING\_VOYAGE\_\_ BACKFILL\_START\_DATE | YYYY-MM-DD | Start date of the backfill schedule for the voyage. |
| STAGING\_VOYAGE\_\_ SQL\_FILTER\_\_BACKFILL\_ UNLOCODES | NLRTM,NLAMS | List of port unlocodes to be backfilled, separated with comma. |

# Resources

* [Architecture Design on Draw.io](https://drive.google.com/file/d/18JtOI3uhOraoArLw5gYaSWBCM6XhOu-d/view?usp=sharing)
* [Airflow - Plugins documentation](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/plugins.html#plugins-as-python-packages)
* [Bitnami - Plugins config documentation](https://docs.vmware.com/en/VMware-Tanzu-Application-Catalog/services/apps/GUID-apps-airflow-index.html#loading-plugins-9)
* [Bitnami - Dags config documentation](https://docs.vmware.com/en/VMware-Tanzu-Application-Catalog/services/apps/GUID-apps-airflow-index.html#load-dag-files-8)
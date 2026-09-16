---
id: confluence:571801614
source: confluence
type: page
space: TC
title: '4. Data Platform: Multiple customers architecture overview'
author: Panji Y. Wiwaha
date: '2025-04-17'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/571801614
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/571801614
---
# 4. Data Platform: Multiple customers architecture overview

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/571801614  

## Content

# Introduction

This document envisions how we want to handle different ETL workflows for multiple customers. This topic is indeed an interesting problem to solve, and several people in the Airflow community have also discussed it. For example, we may use [different git repositories](https://github.com/apache/airflow/discussions/19381#discussioncomment-2509788) or even [leverage git submodules](https://github.com/apache/airflow/discussions/35673) to handle specific customers' ETL workflows. This means there is no definitive answer since the answer could be highly opinionated and might also be relative to the project's needs.

However, based on Airflow's built-in features and Bitnami's capabilities, we have at least two options for managing DAGs on specific customers.

## Mono repository

This approach uses a single repository to manage different ETL workflows for multiple customers and leverages Airflow’s built-in features to load specific DAGs within a code repository. At this point, the Teqplay data engineering team is fully responsible for managing the repository. We separate Teqplay DAGs from customers' DAGs by putting them in a different module, as shown in Figure 1.

Figure 1 - Mono repo architecture

Assuming we have APMT in our customer list, Figure 1 shows that even though the Teqplay DAG Module is present in Bitbucket, we can tell Airflow to ignore that module through the environment variable like this:

AIRFLOW\_\_CORE\_\_DAGS\_FOLDER='{AIRFLOW-HOME}/dags/apmt\_module'

Airflow uses the `AIRFLOW__CORE__DAGS_FOLDER` variable to load ETL workflow only on a specific subfolder within a code repository. Hence, in the illustration above, the Teqplay module is grayed out since it won't be included in the Airflow DAGs module.

### Pros

* It's easy to manage. We only need to maintain two repositories: one for plugins and one for the DAGs.
* CI/CD pipeline is easy to manage.

### Cons

* Code bloat. If we have more customers, Airflow might suffer from code bloat due to the memory space reserved for unused code.

## Multiple repositories

This approach uses multiple repositories to manage different ETL workflows for each customer and leverages Bitnami Airflow’s functionalities to load DAGs from multiple repositories. At this point, we might allow our customers / different teams to be involved in managing the customer repository, as shown in Figure 2.

Figure 2 - Multiple repos architecture

Assuming we have APMT in our customer list, then what we could do is we can configure YAML configuration when deploying Airflow like these:

git:
dags:
enabled: true
repositories:
- branch: develop
name: dataflow\_dag\_apmt
path: ""
repository: https://x-token-auth:{TOKEN\_AUTH}@bitbucket.org/teqplay/dataflow\_dag\_apmt.git

Bitnami provides the git configuration above, which we can use to pull customer-specific DAGs from particular git repositories. It is quite useful if we want to completely separate our ETL code base from one to another and involve more customer/team members to collaborate.

Using the configuration above, we don’t even need to modify the `AIRFLOW__CORE__DAGS_FOLDER` variable. And if, at some point, we have a common workflow needed by both Teqplay and APMT, we can move it within shared plugins.

### Pros

* Open for collaboration to both Teqplay and customer’s team members.

### Cons

* More repositories to manage.
* More CI/CD pipelines to manage.

# Questions

### Multiple repositories

* *Assume we have ETL DAGs that are common to Teqplay and its customers. Can the customer reuse that common code base when we decide to put them in different repositories?*

  + We can’t reuse tasks belonging to a specific DAG in other DAGs. However, since we do the ETL processing mostly in SQL, we can share the SQL file if it’s common to Teqplay and its customers.  
    If we have any code that is common to anyone, such as API clients, utility functions, custom operators, etc., we only need to add them to the Airflow plugins.
  + **Precondition**

    - We need to add the path of the common DAGs to the Python path, i.e.:

      ENV PYTHONPATH "${PYTHONPATH}:/opt/airflow/dags/dataflow\_dag\_common"
      ENV PYTHONPATH "${PYTHONPATH}:/opt/airflow/dags/dataflow\_dag\_apmt"
    - We need to use absolute import to use it on the customer dag file, i.e.:

      pyfrom airflow.operators.python import PythonOperator
      from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
      from dags.common.warehouse.vessel\_voyage.ods import sql
      with DAG(dag\_id='customer\_dag', ...) as dag:
      start = ...
      end = ...
      sql\_path = \_get\_path(sql)
      load\_teqplay\_berth\_visits = SQLExecuteQueryOperator(
      task\_id='load\_teqplay\_berth\_visits',
      conn\_id='AIRFLOW\_CONN\_ETL\_WAREHOUSE\_TEQPLAY',
      sql=f'{sql\_path}/load\_berth\_visits.sql',
      )
      # Express the data flow from top to bottom (down streaming)
      start >> load\_teqplay\_berth\_visits >> end
* *Can we extend and alter a specific ETL DAG workflow defined in the common repository from the customer repository?*

  + By default, no. DAG is used as a wrapper for the collection of tasks that we want to run in a way that reflects their relationship and dependencies.
  + If we want to alter the data flow of a specific DAG, we need to split the task execution into a few DAGs. Let’s take an example where we need to add specific customer data within a specific common DAG, as shown in Figure 3.

    Figure 3 - Illustration of when an additional step is needed within the common DAG
  + We must decouple the DAG into two parts instead of modifying the task flow within the `mart_berth_visits_dag`, and then add the customer-specific DAG in between, as shown in Figure 4.

    Figure 4 - Common DAGs and the customer-specific DAG dependency
* *Can the DAGs exchange information (data) across repositories?*

  + Yes, they can. Even though the code base lives in a different repository, once it is imported into the Airflow app, any information produced by the DAG or the tasks inside of it will be stored in the Airflow database. Therefore, we can make use of it whenever it’s needed.
* *Can the customer DAG execution that is hosted on a different Airflow domain triggered whenever a specific Teqplay DAG is completed?*

  + Yes, we can do it through the Airflow REST API.

# Conclusion

* and me agreed to use the second approach.

# References

* [Airflow - DAGs folder configuration](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#dags-folder)
* [Bitnami - Dags config documentation](https://hub.docker.com/r/bitnamicharts/airflow)
---
id: confluence:608436225
source: confluence
type: page
space: TC
title: Setup Airflow environments
author: Joost Laurman
date: '2025-11-12'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/608436225
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/608436225
---
# Setup Airflow environments

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/608436225  

## Content

Current bitnami chart version: 19.0.10

This is for setting up an environment in the `develop` cluster. It can be done for production, but just change some values to match for `production`.

* Copy the existing helm values from the `etl_airflow` project to the customer project
* Inside the `values.dev.yaml` change the `externalDatabase.database` value
* Create inside the PostgresDB a database and a user.
* Call the database `airflow-<<customer>>`

  + Call the user `airflow-dev-<<customer>>` and generate a random password. **Save this password. You need it for the secrets**
* Change the repository inside the `values.dev.yaml`
* Change `git.dags.repositories.name` to the repository for the customer, e.g. `dataflow_dag_pocca`

  + Change `git.dags.repositories.repository` repository url
* Change the hostname inside the `values.dev.yaml`
* Change `ingress.hostname` value to `airflow-<<customer>>-dev.teqplay.nl`
* In `Route53` create an entry for this hostname, pointing to the load balancer
* In the Kubernetes cluster, create a `pvc` (persistent volume claim) for the temporary data, `airflow-<<customer>>-temp-data`. In Lens you can find this under the section `Storage`.

  yamlapiVersion: v1
  kind: PersistentVolumeClaim
  metadata:
  name: airflow-<<customer>>-temp-data
  namespace: data-engineering
  spec:
  accessModes:
  - ReadWriteOnce
  volumeMode: Filesystem
  resources:
  requests:
  storage: 8Gi
  storageClassName: gp3-retained
* Create **configmaps**

  apiVersion: v1
  kind: ConfigMap
  metadata:
  name: airflow-<<customer>>-worker-env
  namespace: data-engineering
  data:
  AIRFLOW\_\_LOGGING\_\_LOGGING\_CONFIG\_CLASS: teqplay.settings.logging.LOGGING\_CONFIGyamlapiVersion: v1
  kind: ConfigMap
  metadata:
  name: airflow-<<customer>>-scheduler-env
  namespace: data-engineering
  data:
  AIRFLOW\_\_LOGGING\_\_LOGGING\_CONFIG\_CLASS: teqplay.settings.logging.LOGGING\_CONFIGyamlapiVersion: v1
  kind: ConfigMap
  metadata:
  name: airflow-<<customer>>-env
  namespace: data-engineering
  data:
  AIRFLOW\_\_CORE\_\_MAX\_MAP\_LENGTH: '6144'
  AIRFLOW\_\_CORE\_\_TEST\_CONNECTION: Enabled
  AIRFLOW\_\_WEBSERVER\_\_BASE\_URL: https://airflow-<customer>>.teqplay.dev
  AIRFLOW\_\_WEBSERVER\_\_EXPOSE\_CONFIG: 'true'
  AIRFLOW\_\_WEBSERVER\_\_WEB\_SERVER\_MASTER\_TIMEOUT: '300'
  CUSTOMER\_METADATA: '{"code":"TEQPLAY","type":"port\_code"}'
  ETL\_ENV: live
  PYTHONPATH: >-
  ${PYTHONPATH}:/opt/bitnami/airflow/dags/git\_dataflow-dag-core:/opt/bitnami/airflow/plugins/git\_dataflow-plugins
  XDG\_CACHE\_HOME: /mnt/datayamlCreate apiVersion: v1
  kind: ConfigMap
  metadata:
  name: airflow-<<customer>>-env
  namespace: data-engineering
  data:
  AIRFLOW\_\_CORE\_\_MAX\_MAP\_LENGTH: '6144'
  AIRFLOW\_\_CORE\_\_TEST\_CONNECTION: Enabled
  AIRFLOW\_\_WEBSERVER\_\_BASE\_URL: <https://airflow-<customer>>>.teqplay.dev
  AIRFLOW\_\_WEBSERVER\_\_EXPOSE\_CONFIG: 'true'
  AIRFLOW\_\_WEBSERVER\_\_WEB\_SERVER\_MASTER\_TIMEOUT: '300'
  CUSTOMER\_METADATA: '{"code":"TEQPLAY","type":"port\_code"}'
  ETL\_ENV: live
  PYTHONPATH: >-
  ${PYTHONPATH}:/opt/bitnami/airflow/dags/git\_dataflow-dag-core:/opt/bitnami/airflow/plugins/git\_dataflow-plugins
  XDG\_CACHE\_HOME: /mnt/data

All **SECRETS** need to be base64 encoded

* Create **secrets**

  yamlapiVersion: v1
  kind: Secret
  metadata:
  name: airflow-<<customer>>-externaldb
  namespace: data-engineering
  data:
  password: <<base64 encoded password of database user>>
  type: OpaqueyamlapiVersion: v1
  kind: Secret
  metadata:
  name: airflow-<<customer>>-env
  namespace: data-engineering
  data:
  AIRFLOW\_\_CORE\_\_INTERNAL\_API\_SECRET\_KEY: <<base64 encoded password>>
  RABBITMQ\_DEV\_PWD: <<base64 encoded password>>
  RABBITMQ\_DEV\_USER: <<base64 encoded password>>
  S2S\_API\_CLIENT\_ID: <<base64 encoded password>>
  S2S\_API\_CLIENT\_SECRET: <<base64 encoded password>>
  redis-password: <<base64 encoded password>>
  type: OpaqueyamlapiVersion: v1
  kind: Secret
  metadata:
  name: airflow-<<customer>>
  namespace: data-engineering
  data:
  airflow-fernet-key: <<base64 encoded password>>
  airflow-password: <<base64 encoded password>>
  airflow-secret-key: <<base64 encoded password>>
  type: Opaque
* In your terminal now do a helm install. This will create the environment in the cluster. From now on, the
* `helm install airflow-<<customer>>-dev bitnami/airflow -f values.yaml -f values.<<customer>>.dev.yaml -n data-engineering --version 19.0.10`
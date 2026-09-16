---
id: confluence:706969602
source: confluence
type: page
space: TC
title: 2. Run Teqplay ETL Pipeline Through the Airflow App
author: Panji Y. Wiwaha
date: '2025-06-24'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/706969602
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/706969602
---
# 2. Run Teqplay ETL Pipeline Through the Airflow App

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/706969602  

## Content

# **Airflow Setup**

### **Initialize Airflow variables**

* Navigate to the “Filter DAGs by tag” input field and fill it with `utility`.
* Enable the DAG choice button to initialize the Airflow Variables.

* Navigate to the **Admin > Variables** and update these variables based on your needs.

  + `DATAFLOW_DATA_INGESTION_FOCUSED_UNLOCODE` → Fill it with the Port UNLOCODE you want to ingest into the data warehouse/datamart.
  + `STAGING_SOF__BACKFILL_UNLOCODES` → Fill it with the list of Port UNLOCODEs you want to back-fill and use a comma to separate the values. If you don’t need this, just set it to an empty string.
  + `STAGING_VOYAGE__BACKFILL_UNLOCODES` → Fill it with the list of Port UNLOCODEs you want to back-fill and use a comma to separate the values. If you don’t need this, just set it to an empty string.

### **Run the file cache cleaner**

* Navigate to the “Filter DAGs by tag” input field and fill it with `utility`.
* Enable the DAG choice button to clean up file caches (by default, it will clean file caches stored on the disk for two days or more).

# **Database Setup**

### **Initialize Teqplay data warehouse**

* Navigate to the “Filter DAGs by tag” input field and fill it with `prepare-tables`.
* Enable the DAG choice button to prepare tables for the **staging data** and wait until it’s done.
* Enable the DAG choice button to prepare tables for the **operational data source (ODS)** and wait until it’s done.

### **Initialize Teqplay data mart**

* Navigate to the “Filter DAGs by tag” input field and type it with `prepare-tables`.
* Enable the DAG choice buttons to prepare tables for the **dimension data** and wait until it’s done.
* Enable the DAG choice buttons to prepare tables for the **fact data** and wait until it’s done.

### **Prepare SQL functions**

* Navigate to the “Filter DAGs by tag” input field and fill it with `prepare-functions`.
* Enable the radio button to create SQL functions on a data warehouse/datamart.

### **Run the schema migrations (optional)**

If the structure of the data tables is changed, please run these migrations DAG.

* Navigate to the “Filter DAGs by tag” input field and fill it with `migrations`.
* Run the appropriate migration DAGs.

  + `migrations_staging_table` → DAG to run schema/data migration on any staging tables.
  + `migrations_ods_table` → DAG to run schema/data migration on any ODS tables.
  + `migrations_dim_table` → DAG to run schema/data migration on any dimension tables.
  + `migrations_fact_table` → DAG to run schema/data migration on any fact tables.

# **Running Teqplay ETL Pipeline**

In a higher-level overview, the ETL pipeline starts with:

Extracts staging data through the API → Transforms them into relational data tables → Converts and loads the relational data table to the Teqplay data mart.

The process above applies to either a batching or a streaming pipeline.

### **Run the ETL pipeline through batching**

We use [data-aware scheduling](https://www.astronomer.io/docs/learn/airflow-datasets/) to process the Teqplay data. It ensures that Airflow will only generate a report from the Teqplay data mart when its operational data tables are ready. The same goes for the operational data tables, Airflow will load them only when the staging data is available.

#### **Enable the data mart transformators**

* Navigate to the “Filter DAGs by tag” input field and fill it with `mart`.
* Enable the dimension and fact DAGs, indicated by the `dim_` and `fact_` prefixes.

#### **Enable the data warehouse transformators**

* POMA

  + Clear the “Filter DAGs by tag” input field and fill it with `poma`.
  + Enable all of the POMA **operational data source** DAGs, indicated by the `ods_` prefixes.
  + Enable all of the POMA **staging** DAGs, indicated by the `staging_` prefixes.
* CSI

  + Clear the “Filter DAGs by tag” input field and fill it with `csi`.
  + Enable all of the CSI **operational data source** DAGs, indicated by the `ods_` prefixes.
  + Enable all of the CSI **staging** DAGs, indicated by the `staging_` prefixes.
* Vessel Voyage

  + Clear the “Filter DAGs by tag” input field and fill it with `vessel-voyage`.
  + Enable all of the Vessel Voyage **operational data source** DAGs, indicated by the `ods_` prefixes.
* Voyage

  + Clear the “Filter DAGs by tag” input field and fill it with `voyage`.
  + Enable all of the Voyage **operational data source** DAGs, indicated by the `ods_` prefixes.
  + Enable all of the Voyage **staging** DAGs, indicated by the `staging_` prefixes.

### **Run the ETL pipeline through streaming**

* Clear the “Filter DAGs by tag” input field and fill it with `data-streaming`.
* Enable all of the data stream handlers.
* Enable all of the data stream subscribers.
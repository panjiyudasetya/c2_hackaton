---
id: confluence:540082177
source: confluence
type: page
space: TC
title: '5. Data Platform: Complete overview for the new dataplatform'
author: ryan (Unlicensed)
date: '2026-01-29'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/540082177
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/540082177
---
# 5. Data Platform: Complete overview for the new dataplatform

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/540082177  

## Content

| **Version** | **Date** | **Author** | **Changes** |
| --- | --- | --- | --- |
| 0.1 | 12 December 2024 |  | First Draft |
| 1.0 | 29 January 2026 |  | Completed Docs |
|  |  |  |  |

Our new data platform here is as the diagram below:

*figure 01: Data Ingestion Process Diagram*

We are using the Airflow for the orchestrations of the tasks that needed for ingestion and ETL process of the data platform. As we see on the diagram above, the data comes from API sources such as POMA, CSI and Vessel Voyage systems.

|  |  |  |
| --- | --- | --- |
| **No.** | **System Name** | **Descriptions** |
| **1** | **POMA** | This system is used for the maritime base asset such as port, berth, terminal, anchorage, quay, area, etc. |
| **2** | **CSI** | This system is used for the Ship or Vessel information, consist of ship, imo, mmsi, ship\_category, deu, teu, etc. |
| **3** | **VESSEL VOYAGE** | This system is used for the vessel voyage data that consist of the visits, voyage, durations and also stops. |

The explanation of the diagram above as below steps:

1. The data that come from various systems is ingested through API in the airflow.
2. The destinations are data warehouse in PostgreSQL.
3. After the data is on the data warehouse we are doing some ETL to ingest to the datamart.

In short data comes from the API then ingest to the data warehouse then ingest to the data mart.

Here are some terminology about the data type that we are ingesting as below:

|  |  |  |
| --- | --- | --- |
| **No.** | **Type of Table** | **Descriptions** |
| **1** | **Staging** | The staging table are temporary table that holds business informations. This table needed after we got data from the API, we store it on this table first as it is. The staging here is non-relational databases. |
| **2** | **ODS** | The Operational Data Store or ODS is a central database that provides a snapshot of the latest data from multiple transactional systems. ODS provides current, clean data from multiple sources in a single place, and the benefits apply primarily to business operations. The ODS here is a relational databases. |
| **3** | **DIM** | Dimension tables, on the other hand, offer context to the data stored in fact tables. They provide descriptive information that helps users understand the “who,” “where,” and “when” aspects of the data. |
| **4** | **FACT** | Fact tables are the heart of a data warehouse. They contain quantitative data, often referred to as measures or metrics, and are the focus of most data analysis. These tables store data related to business transactions and events, such as sales figures, revenue, or quantities sold. In essence, fact tables provide the “what” in data analysis. |

# Data model (stg, ods, dim, fact)

## **Dimensional Modeling**

The data model used to store data in the denormalized form is called ***Dimensional Modelling***. It is the technique of storing data in a Data Warehouse in such a way that enables ***fast query performance*** and ***easy access*** to its business users. It involves creating a set of dimensional tables that are designed to support business intelligence and reporting needs.

The core concept of dimensional modelling is the creation of a star schema. It is called so as the tables are arranged in the form of a star.

## 

*figure 02: Star Schema Diagram*

## Port

A port is a maritime facility comprising one or more wharves or loading areas, where ships load and discharge cargo and passengers.

### Staging Port : (stg\_port)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field name** | **Alias** | **Field Type** | **Descriptions** |
| **1** | id | ID | String | Port Identification |
| **2** | name | Name | String | Name of the Port |
| **3** | display\_name | Display Name | String | Display Name of the Port |
| **4** | unlocode | UNLOCODE | String | United Nations Code for Trade and Transport Locations |
| **5** | country\_code | Country Code | String | Country Code (ISO 3166-1 alpha-2). Country Code in two digit of capital letter, e.g NL for Nedherland, ID for Indonesia. |
| **6** | country | Country | jsonb | Country information where the port is located (name, code) |
| **7** | location | Location | jsonb | Location coordinate information of the port in latitude and longitude format. |
| 8 | area | Area | jsonb | Port area polygon geometry |
| 9 | area\_size\_in\_m2 | Area Size in M2 | bigint | Port area size in square meters |
| 10 | manual\_overridden\_area | Manual Overridden Area | Boolean | Indicates if area was manually overridden |
| 11 | outer\_area | Outer Area | jsonb | Outer boundary area polygon |
| 12 | nm12\_area | 12 NM Area | jsonb | 12 nautical miles area polygon |
| 13 | nm60\_area | 60 NM Area | jsonb | 60 nautical miles area polygon |
| 14 | nm80\_area | 80 NM Area | jsonb | 80 nautical miles area polygon |
| 15 | nm120\_area | 120 NM Area | jsonb | 120 nautical miles area polygon |
| 16 | eos\_area | EOS Area | jsonb | End of Sea (EOS) area polygon |
| 17 | manual\_overridden\_eos\_area | Manual Overridden EOS Area | Boolean | Indicates if EOS area was manually overridden |
| 18 | alternative\_names | Alternative Names | jsonb | Alternative names for the port |
| 19 | destinations | Destinations | jsonb | Destination information |
| 20 | margin | Margin | decimal | Margin value for area calculations |
| 21 | unique\_id | Unique Id | String | Unique identifier |
| 22 | model\_type | Model Type | String | Type of data model |
| 23 | source | Source | String | Data source identifier |
| 24 | source\_type | Source Type | String | Type of data source |
| 25 | validated\_by\_user | Validated by user | Boolean | The Port is already validated by users |
| 26 | main\_port | Main Port | String | Main Port identifier |

### ODS Port : (ods\_port)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field Name** | **Alias** | **Field Type** | **Descriptions** |
| 1 | id | ID | String | Port Identification |
| 2 | latitude | Latitude | String | Port latitude coordinate |
| 3 | longitude | Longitude | String | Port longitude coordinate |
| 4 | name | Name | String | Port name |
| 5 | display\_name | Display Name | String | Display name for the port |
| 6 | unlocode | UNLOCODE | String | United Nations Code for Trade and Transport Locations |
| 7 | country\_code | Country Code | String | Country Code (ISO 3166-1 alpha-2) |
| 8 | country\_name | Country Name | String | Country name |
| 9 | main\_port | Main Port | String | Main port identifier |
| 10 | validated\_by\_user | Validated By User | Boolean | Indicates if validated by users |

### Dim Port : (dim\_port)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field name** | **Alias** | **Field Type** | **Descriptions** |
| **1** | id | ID | String | Port Identification |
| **2** | latitude | Latitude | String | Latitude coordinate of the location |
| **3** | longitude | Longitude | String | Longitude coordinate of the location |
| **4** | name | Name | String | Name of the Port |
| **5** | display\_name | Display Name | String | Display Name of the Port |
| **6** | unlocode | UNLOCODE | String | United Nations Code for Trade and Transport Locations |
| **7** | country\_code | Country Code | String | Country Code in two digit of capital letter, e.g NL for Nedherland, ID for Indonesia. |
| **8** | country\_name | Country | String | Country information where the port is located. |
| **9** | main\_port | Main Port | String | Main Port |

### 

### Airflow DAG related to Port

|  |  |  |  |
| --- | --- | --- | --- |
| **No.** | **DAG Name** | **Schedule** | **Tasks** |
| **1** | staging\_port | daily | extract\_ports\_from\_api  load\_file\_staging\_ports |
| **2** | ods\_port | Dataset | load\_ods\_ports |
| **3** | mart\_maritime\_base | Dataset | load\_dim\_port |

## Terminal

Terminal is a facilities where loading and unloading of people or goods takes place.

### Staging Terminal (stg\_terminal)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field Name** | **Alias** | **Field Type** | **Descriptions** |
| 1 | id | ID | String | Terminal Identification |
| 2 | authority\_id | Authority ID | String | Authority-assigned identifier |
| 3 | unique\_id | Unique ID | String | Unique terminal identifier |
| 4 | name | Name | String | Terminal name |
| 5 | display\_name | Display Name | String | Display name for the terminal |
| 6 | ports | Ports | jsonb | Associated ports information |
| 7 | cargo\_category\_type | Cargo Category Type | jsonb | Cargo category types |
| 8 | cargo\_type | Cargo Type | jsonb | Cargo types handled |
| 9 | location | Location | jsonb | Geographic location |
| 10 | area | Area | jsonb | Terminal area polygon |
| 11 | area\_size\_in\_m2 | Area Size in M2 | bigint | Terminal area size in square meters |
| 12 | manual\_overridden\_area | Manual Overridden Area | Boolean | Indicates if area was manually overridden |
| 13 | mooring\_area | Mooring Area | jsonb | Mooring area polygon |
| 14 | manual\_overridden\_mooring\_area | Manual Overridden Mooring Area | Boolean | Indicates if mooring area was manually overridden |
| 15 | model\_type | Model Type | String | Type of data model |
| 16 | source | Source | String | Data source identifier |
| 17 | source\_type | Source Type | String | Type of data source |
| 18 | validated\_by\_user | Validated by User | Boolean | Indicates if validated by users |
| 19 | port\_city | Port City | String | City where port is located |
| 20 | country | Country | String | Country name |
| 21 | city | City | String | City name |
| 22 | region | Region | String | Region name |
| 23 | max\_length | Max Length | String | Maximum vessel length allowed |
| 24 | max\_width | Max Width | String | Maximum vessel width allowed |
| 25 | max\_draft | Max Draft | String | Maximum vessel draft allowed |
| 26 | capacity | Capacity | String | Terminal capacity |
| 27 | headoffice\_id | Head Office ID | String | Head office identifier |
| 28 | headoffice\_name | Head Office Name | String | Head office name |
| 29 | asset\_type | Asset Type | String | Type of terminal asset |
| 30 | number\_of\_tanks | Number of Tanks | String | Number of storage tanks |
| 31 | has\_lpb\_data | Has LPB Data | String | Indicates if LPB data is available |
| 32 | has\_vcg | Has VCG | String | Indicates if VCG data is available |
| 33 | terminal\_group | Terminal Group | String | Terminal group identifier |

### ODS Terminal (ods\_terminal)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field Name** | **Alias** | **Field Type** | **Descriptions** |
| 1 | id | ID | String | Terminal Identification |
| 2 | latitude | Latitude | String | Terminal latitude coordinate |
| 3 | longitude | Longitude | String | Terminal longitude coordinate |
| 4 | name | Name | String | Terminal name |
| 5 | authority\_id | Authority ID | String | Authority-assigned identifier |
| 6 | unique\_id | Unique ID | String | Unique terminal identifier |
| 7 | ports | Ports | jsonb | Associated ports information |
| 8 | port\_city | Port City | String | City where port is located |
| 9 | cargo\_category\_type | Cargo Category Type | String | Cargo category type |
| 10 | city | City | String | City name |
| 11 | country | Country | String | Country name |
| 12 | region | Region | String | Region name |
| 13 | max\_length | Max Length | String | Maximum vessel length allowed |
| 14 | max\_width | Max Width | String | Maximum vessel width allowed |
| 15 | max\_draft | Max Draft | String | Maximum vessel draft allowed |
| 16 | capacity | Capacity | String | Terminal capacity |
| 17 | asset\_type | Asset Type | String | Type of terminal asset |
| 18 | number\_of\_tanks | Number of Tanks | String | Number of storage tanks |
| 19 | terminal\_company | Terminal Company | String | Terminal operating company |

### DIM Terminal (dim\_terminal)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field Name** | **Alias** | **Field Type** | **Descriptions** |
| **1** | id | ID | String | Terminal Identification |
| **2** | name | Name | String | Name of the Terminal |
| **3** | name\_with\_port | Name with port | String | Name with port |
| 4 | company | Company | String | Company that owns the Terminal |

### Airflow DAG related to Terminal

|  |  |  |  |
| --- | --- | --- | --- |
| **No.** | **DAG Name** | **Schedule** | **Tasks** |
| **1** | staging\_terminal | daily | extract\_terminals\_from\_api  load\_file\_staging\_terminals |
| **2** | ods\_terminal | Dataset | load\_ods\_terminals |
| **3** | mart\_maritime\_base | Dataset | load\_dim\_terminal |

## Berth

A berth is a designated location in a port or harbour used for mooring vessels when they are not at sea. Berth provide a vertical front which allows safe and secure mooring that can then facilitate the unloading or loading of cargo or people from vessels.

### Staging Berth (stg\_berth)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| 1 | unique\_id | Unique ID | String | Unique berth identifier |
| 2 | authority\_id | Authority ID | String | Authority-assigned identifier |
| 3 | name | Name | String | Berth name |
| 4 | display\_name | Display Name | String | Display name for the berth |
| 5 | name\_long | Long Name | String | Full berth name |
| 6 | availability\_type | Availability Type | String | Berth availability status |
| 7 | terminal\_name | Terminal Name | String | Name of the terminal |
| 8 | terminal\_id | Terminal ID | String | Terminal identifier |
| 9 | harbour\_name | Harbour Name | String | Name of the harbour |
| 10 | harbour\_id | Harbour ID | String | Harbour identifier |
| 11 | ports | Ports | jsonb | Associated ports information |
| 12 | length | Length | String | Berth length |
| 13 | width | Width | String | Berth width |
| 14 | draught | Draught | String | Maximum draught allowed |
| 15 | owner | Owner | String | Berth owner |
| 16 | quay\_id | Quay ID | String | Quay identifier |
| 17 | dangerous\_goods\_level | Dangerous Goods Level | String | Dangerous goods handling level |
| 18 | vessel\_type\_allowed | Vessel Type Allowed | jsonb | Allowed vessel types |
| 19 | mooring\_type | Mooring Type | String | Type of mooring |
| 20 | cargo\_category\_type | Cargo Category Type | jsonb | Cargo category types |
| 21 | cargo\_type | Cargo Type | jsonb | Cargo types handled |
| 22 | function\_type | Function Type | jsonb | Berth function types |
| 23 | location | Location | jsonb | Geographic location |
| 24 | area | Area | jsonb | Berth area polygon |
| 25 | area\_size\_in\_m2 | Area Size in M2 | bigint | Berth area size in square meters |
| 26 | manual\_overridden\_area | Manual Overridden Area | Boolean | Indicates if area was manually overridden |
| 27 | model\_type | Model Type | String | Type of data model |
| 28 | source | Source | String | Data source identifier |
| 29 | source\_type | Source Type | String | Type of data source |
| 30 | validated\_by\_user | Validated by User | Boolean | Indicates if validated by users |
| 31 | main\_port | Main Port | String | Main port identifier |

### ODS Berth (ods\_berth)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| 1 | id | ID | String | Berth Identification |
| 2 | latitude | Latitude | String | Berth latitude coordinate |
| 3 | longitude | Longitude | String | Berth longitude coordinate |
| 4 | name | Name | String | Berth name |
| 5 | name\_long | Long Name | String | Full berth name |
| 6 | terminal | Terminal | String | Terminal name |
| 7 | terminal\_id | Terminal ID | String | Terminal identifier |
| 8 | harbour | Harbour | String | Harbour name |
| 9 | harbour\_id | Harbour ID | String | Harbour identifier |
| 10 | quay\_id | Quay ID | String | Quay identifier |
| 11 | cargo\_category\_type | Cargo Category Type | jsonb | Cargo category types |
| 12 | ports | Ports | jsonb | Associated ports information |
| 13 | main\_port | Main Port | String | Main port identifier |
| 14 | length | Length | String | Berth length |
| 15 | width | Width | String | Berth width |
| 16 | draught | Draught | String | Maximum draught allowed |
| 17 | owner | Owner | String | Berth owner |
| 18 | mooring\_type | Mooring Type | String | Type of mooring |
| 19 | function\_type | Function Type | text[] | Berth function types (array): |

**DIM Berth (dim\_berth)**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| **1** | Id | ID | String | PRIMARY KEY (id) |
| **2** | latitude | Latitude | String | Location Latitude of the Berth |
| **3** | longitude | Longitude | String | Location Longitude of the Berth |
| **4** | name | Name | String | Name of the Berth |
| **5** | name\_long | Name Long | String | Name long of the Berth |
| **6** | port | Port | String | Port |
| **7** | port\_display\_name | Port Display Name | String | Port Display Name |
| **8** | port\_name | Port Name | String | Port Name |
| **9** | terminal | Terminal | String | Terminal |
| **10** | terminal\_id | Terminal Id | String | Terminal Identifier |
| **11** | type | Type | String | Type of Berth |
| **12** | length | Length | String | Length of Berth |

### Airflow DAG related to Berth

|  |  |  |  |
| --- | --- | --- | --- |
| **No.** | **DAG Name** | **Schedule** | **Tasks** |
| **1** | staging\_berth | daily | extract\_berths\_from\_api  load\_file\_staging\_berths |
| **2** | ods\_berth | Dataset | load\_ods\_berths |
| **3** | mart\_maritime\_base | Dataset | load\_dim\_berth |

## AREA

### Anchorage

A designated, safe, and sheltered area of water where ships, boats, and vessels can drop anchor stop, wait for port entry, or conduct operations.

### Staging Anchorage (stg\_anchorage)

| **No.** | **Field Name** | **Alias** | **Field Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Anchorage Identification |
| 2 | name | Name | String | Anchorage name |
| 3 | ports | Ports | jsonb | Associated ports information |
| 4 | margin | Margin | String | Margin value for area calculations |
| 5 | owner\_id | Owner ID | String | Owner identifier |
| 6 | max\_length | Max Length | String | Maximum vessel length allowed |
| 7 | location | Location | jsonb | Geographic location |
| 8 | area | Area | jsonb | Anchorage area polygon |
| 9 | area\_size\_in\_m2 | Area Size in M2 | String | Anchorage area size in square meters |
| 10 | manual\_overridden\_area | Manual Overridden Area | Boolean | Indicates if area was manually overridden |
| 11 | human\_readable\_name | Human Readable Name | text | Human-readable anchorage name |
| 12 | unique\_id | Unique ID | String | Unique identifier |
| 13 | model\_type | Model Type | String | Type of data model |
| 14 | source | Source | String | Data source identifier |
| 15 | source\_type | Source Type | String | Type of data source |
| 16 | validated\_by\_user | Validated by User | Boolean | Indicates if validated by users |

### ods\_anchorage

Operational Data Store for anchorage area master data

| No. | Field Name | Alias | Data Type | Descriptions |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Unique identifier (Primary Key) |
| 2 | latitude | Latitude | String | Latitude coordinate |
| 3 | longitude | Longitude | String | Longitude coordinate |
| 4 | name | Name | String | Name |
| 5 | unique\_id | Unique ID | String | Unique identifier |
| 6 | ports | Ports | JSONB | Ports information (JSONB) |
| 7 | owner\_id | Owner ID | String | Owner identifier |
| 8 | max\_length | Max Length | String | Max Length |
| 9 | human\_readable\_name | Human Readable Name | Text | Human-readable name |
| 10 | model\_type | Model Type | String | Type of data model |

## Approach Area

### Staging Approach Area (stg\_approach\_area)

| **No.** | **Field Name** | **Alias** | **Field Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Approach Area Identification |
| 2 | unique\_id | Unique ID | String | Unique approach area identifier |
| 3 | name | Name | String | Approach area name |
| 4 | ports | Ports | jsonb | Associated ports information |
| 5 | margin | Margin | double precision | Margin value for area calculations |
| 6 | location | Location | jsonb | Geographic location |
| 7 | area | Area | jsonb | Approach area polygon |
| 8 | area\_size\_in\_m2 | Area Size in M2 | bigint | Approach area size in square meters |
| 9 | manual\_overridden\_area | Manual Overridden Area | Boolean | Indicates if area was manually overridden |
| 10 | model\_type | Model Type | String | Type of data model |
| 11 | source | Source | String | Data source identifier |
| 12 | source\_type | Source Type | String | Type of data source |
| 13 | validated\_by\_user | Validated by User | Boolean | Indicates if validated by users |

### ods\_approach\_area

Operational Data Store for approach area master data

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Unique identifier (Primary Key) |
| 2 | unique\_id | Unique ID | String | Unique identifier |
| 3 | name | Name | String | Name |
| 4 | margin | Margin | Double | Margin value for area calculations |
| 5 | latitude | Latitude | String | Latitude coordinate |
| 6 | longitude | Longitude | String | Longitude coordinate |
| 7 | area\_size\_in\_m2 | Area Size In M² | BigInt | Area size in square meters |
| 8 | manual\_overridden\_area | Manual Overridden Area | Boolean | Indicates if area was manually overridden |
| 9 | model\_type | Model Type | String | Type of data model |
| 10 | source | Source | String | Data source identifier |
| 11 | source\_type | Source Type | String | Type of data source |
| 12 | validated\_by\_user | Validated By User | Boolean | Indicates if validated by users |

### Lock

### Staging Lock (stg\_lock)

| **No.** | **Field Name** | **Alias** | **Field Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Lock Identification |
| 2 | unique\_id | Unique ID | String | Unique lock identifier |
| 3 | name | Name | String | Lock name |
| 4 | isrs\_code | ISRS Code | String | International Ship Reporting Standard code |
| 5 | ports | Ports | jsonb | Associated ports information |
| 6 | margin | Margin | double precision | Margin value for area calculations |
| 7 | location | Location | jsonb | Geographic location |
| 8 | area | Area | jsonb | Lock area polygon |
| 9 | area\_size\_in\_m2 | Area Size in M2 | bigint | Lock area size in square meters |
| 10 | manual\_overridden\_area | Manual Overridden Area | Boolean | Indicates if area was manually overridden |
| 11 | model\_type | Model Type | String | Type of data model |
| 12 | source | Source | String | Data source identifier |
| 13 | source\_type | Source Type | String | Type of data source |
| 14 | validated\_by\_user | Validated by User | Boolean | Indicates if validated by users |

### ods\_lock

Operational Data Store for lock master data

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Unique identifier (Primary Key) |
| 2 | unique\_id | Unique ID | String | Unique identifier |
| 3 | name | Name | String | Name |
| 4 | isrs\_code | Isrs Code | String | Isrs Code |
| 5 | margin | Margin | Double | Margin value for area calculations |
| 6 | latitude | Latitude | String | Latitude coordinate |
| 7 | longitude | Longitude | String | Longitude coordinate |
| 8 | area\_size\_in\_m2 | Area Size In M² | BigInt | Area size in square meters |
| 9 | manual\_overridden\_area | Manual Overridden Area | Boolean | Indicates if area was manually overridden |
| 10 | model\_type | Model Type | String | Type of data model |
| 11 | source | Source | String | Data source identifier |
| 12 | source\_type | Source Type | String | Type of data source |
| 13 | validated\_by\_user | Validated By User | Boolean | Indicates if validated by users |

## Ship

A vessel larger than a boat for transporting people or goods by sea.

### Staging Ship

**stg\_ship**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field Name** | **Alias** | **Field Type** | **Descriptions** |
| 1 | id | ID | String | Ship Identification |
| 2 | identifiers | Identifiers | jsonb | Ship identifiers (IMO, MMSI, ENI, call sign) |
| 3 | specification | Specification | jsonb | Ship specifications (gross tonnage, DWT, TEU) |
| 4 | categories | Categories | jsonb | Ship categories (v1, v2, v3) |
| 5 | types | Types | jsonb | Ship types and classifications |
| 6 | dimensions | Dimensions | jsonb | Ship dimensions (length, beam, draught, height) |
| 7 | calculated | Calculated | jsonb | Calculated fields (TEU, classification) |
| 8 | metadata | Metadata | jsonb | Metadata information |
| 9 | administration | Administration | jsonb | Administration data (owner, flag, manager) |
| 10 | synced\_at | Synced At | String | Last synchronization timestamp |

### stg\_ship\_mapping

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field Name** | **Alias** | **Field Type** | **Descriptions** |
| 1 | id | ID | String | Ship mapping identification |
| 2 | imo | IMO | String | Ship IMO number |
| 3 | mapping | Mapping | jsonb | MMSI mapping information |
| 4 | ignored | Ignored | jsonb | Ignored MMSI values |
| 5 | state | State | String | Mapping state |
| 6 | updated\_time | Updated Time | String | Last update timestamp |
| 7 | created\_time | Created Time | String | Creation timestamp |

### ODS Ship

**ods\_ship**

| **No.** | **Field Name** | **Alias** | **Field Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Ship Identification |
| 2 | imo | IMO | String | IMO number |
| 3 | mmsi | MMSI | String | Maritime Mobile Service Identity |
| 4 | eni | ENI | String | European Number of Identification |
| 5 | call\_sign | Call Sign | String | Ship call sign |
| 6 | name | Name | String | Ship name |
| 7 | gross\_tonnage | Gross Tonnage | double precision | Gross tonnage |
| 8 | engine\_power\_kw | Engine Power (kW) | integer | Engine power in kilowatts |
| 9 | classification | Classification | String | Ship classification |
| 10 | dwt | DWT | double precision | Deadweight tonnage |
| 11 | bow\_thruster\_equipped | Bow Thruster Equipped | Boolean | Indicates if bow thruster is equipped |
| 12 | teu | TEU | double precision | Twenty-foot Equivalent Unit capacity |
| 13 | role | Role | String | Ship role |
| 14 | hull\_type | Hull Type | String | Type of hull |
| 15 | construction\_year | Construction Year | integer | Year of construction |
| 16 | flag | Flag | String | Ship flag country |
| 17 | flag\_code | Flag Code | String | Ship flag country code |
| 18 | class\_register | Class Register | String | Classification society |
| 19 | owner\_name | Owner Name | String | Ship owner name |
| 20 | owner\_address | Owner Address | String | Ship owner address |
| 21 | owner\_zip\_code | Owner Zip Code | String | Ship owner zip code |
| 22 | owner\_city | Owner City | String | Ship owner city |
| 23 | owner\_country | Owner Country | String | Ship owner country |
| 24 | tech\_manager\_name | Technical Manager Name | String | Technical manager name |
| 25 | tech\_manager\_address | Technical Manager Address | String | Technical manager address |
| 26 | tech\_manager\_zip\_code | Technical Manager Zip Code | String | Technical manager zip code |
| 27 | tech\_manager\_city | Technical Manager City | String | Technical manager city |
| 28 | tech\_manager\_country | Technical Manager Country | String | Technical manager country |
| 29 | ship\_cat | Ship Category | String | Ship category |
| 30 | sub\_cat | Sub Category | String | Ship sub-category |
| 31 | sub\_cat\_code | Sub Category Code | String | Ship sub-category code |
| 32 | synced\_at | Synced At | String | Last synchronization timestamp |
| 33 | category\_v1 | Category V1 | String | Ship category version 1 |
| 34 | category\_v2 | Category V2 | String | Ship category version 2 |
| 35 | category\_v3 | Category V3 | String | Ship category version 3 |
| 36 | dimension\_beam | Beam | double precision | Ship beam (width) |
| 37 | dimension\_length | Length | double precision | Ship length |
| 38 | dimension\_length\_between\_perpendiculars | Length Between Perpendiculars | double precision | Length between perpendiculars |
| 39 | dimension\_height | Height | double precision | Ship height |
| 40 | dimension\_max\_draught | Max Draught | double precision | Maximum draught |
| 41 | dimension\_alternate\_draught | Alternate Draught | double precision | Alternate draught |
| 42 | dimension\_moulded\_depth | Moulded Depth | double precision | Moulded depth |
| 43 | calculated\_teu | Calculated TEU | double precision | Calculated TEU capacity |
| 44 | calculated\_classification | Calculated Classification | String | Calculated ship classification |
| 45 | disabled | Disabled | Boolean | Indicates if ship is disabled |
| 46 | disabled\_date | Disabled Date | date | Date when ship was disabled |
| 47 | disabled\_time | Disabled Time | time | Time when ship was disabled |
| 48 | disabled\_timestamp | Disabled Timestamp | timestamp | Timestamp when ship was disabled |
| 49 | ghost\_ship\_enabled | Ghost Ship Enabled | Boolean | Indicates if ghost ship mode is enabled |
| 50 | ghost\_ship\_enabled\_date | Ghost Ship Enabled Date | date | Date when ghost ship was enabled |
| 51 | ghost\_ship\_enabled\_time | Ghost Ship Enabled Time | time | Time when ghost ship was enabled |
| 52 | ghost\_ship\_enabled\_timestamp | Ghost Ship Enabled Timestamp | timestamp | Timestamp when ghost ship was enabled |
| 53 | created\_date | Created Date | date | Record creation date |
| 54 | created\_time | Created Time | time | Record creation time |
| 55 | created\_timestamp | Created Timestamp | timestamp | Record creation timestamp |
| 56 | created\_by | Created By | String | User who created the record |
| 57 | updated\_date | Updated Date | date | Record update date |
| 58 | updated\_time | Updated Time | time | Record update time |
| 59 | updated\_timestamp | Updated Timestamp | timestamp | Record update timestamp |

**ods\_ship\_mmsi\_mapping**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| **1** | id | ID | String | PRIMARY KEY (id) |
| **2** | ship\_id | SHIP ID | String | Ship Identification |
| **3** | mmsi\_mapping\_id | MMSI Mapping ID | String |  |
| **4** | state | State | String |  |
| **5** | ignored | Ignored | String |  |
| **6** | created\_date | Created Date | date |  |
| **7** | created\_time | Created Time | time |  |
| **8** | created\_timestamp | Created Timestamp | timestamp |  |
| **9** | created\_by | Created By | String |  |
| **10** | updated\_date | Updated Date | date |  |
| **11** | updated\_time | Updated Time | time |  |
| **12** | updated\_timestamp | Updated Timestamp | timestamp |  |

**ods\_mmsi\_mapping**

Operational Data Store for MMSI mapping records

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| 1 | id | ID | String | Unique identifier (Primary Key) |
| 2 | imo | IMO | String | IMO number |
| 3 | mmsi | MMSI | String | Maritime Mobile Service Identity |
| 4 | from\_date | From Date | Date | From Date |
| 5 | from\_time | From Time | Time | From Time |
| 6 | from\_timestamp | From Timestamp | Timestamp | From timestamp |
| 7 | to\_date | To Date | Date | To Date |
| 8 | to\_time | To Time | Time | To Time |
| 9 | to\_timestamp | To Timestamp | Timestamp | To timestamp |
| 10 | margin | Margin | Double | Margin value for area calculations |
| 11 | created\_date | Created Date | Date | Created Date |
| 12 | created\_time | Created Time | Time | Created Time |
| 13 | created\_timestamp | Created Timestamp | Timestamp | Record creation timestamp |
| 14 | updated\_date | Updated Date | Date | Updated Date |
| 15 | updated\_time | Updated Time | Time | Updated Time |
| 16 | updated\_timestamp | Updated Timestamp | Timestamp | Record update timestamp |

**Dim Ship (dim\_ship)**

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Unique identifier (Primary Key) |
| 2 | name | Name | String | Name |
| 3 | imo | IMO | String | IMO number |
| 4 | mmsi | MMSI | String | Maritime Mobile Service Identity |
| 5 | mmsi\_from | MMSI From | Timestamp | MMSI validity start timestamp |
| 6 | mmsi\_to | MMSI To | Timestamp | MMSI validity end timestamp |
| 7 | beam | Beam | Double | Ship beam (width) |
| 8 | draught | Draught | Double | Ship draught |
| 9 | dwt | DWT | Double | Deadweight tonnage |
| 10 | gross\_tonnage | Gross Tonnage | Double | Gross tonnage |
| 11 | length\_over\_all | Length Over All | Double | Ship length over all |
| 12 | shipping\_line | Shipping Line | String | Shipping Line |
| 13 | teu | TEU | Double | Twenty-foot Equivalent Unit capacity |
| 14 | teu\_estimated | TEU Estimated | Double | Estimated TEU capacity |
| 15 | ship\_category | Ship Category | String | Ship category |
| 16 | sub\_cat | Sub Cat | String | Sub Cat |
| 17 | ship\_cat | Ship Cat | String | Ship Cat |
| 18 | ship\_role | Ship Role | String | Ship role |
| 19 | dry\_bulk\_classification | Dry Bulk Classification | String | Dry Bulk Classification |
| 20 | dry\_bulk\_category | Dry Bulk Category | String | Dry Bulk Category |
| 21 | wet\_bulk\_classification | Wet Bulk Classification | String | Wet Bulk Classification |
| 22 | wet\_bulk\_category | Wet Bulk Category | String | Wet Bulk Category |
| 23 | teu\_classification | TEU Classification | String | Teu Classification |
| 24 | teu\_category | TEU Category | String | Teu Category |
| 25 | cargo\_type | Cargo Type | String | Cargo type |
| 26 | type | Type | String | Type |

### Airflow DAG related to Ship

|  |  |  |  |
| --- | --- | --- | --- |
| **No.** | **DAG Name** | **Schedule** | **Tasks** |
| **1** | staging\_ship | daily | load\_staging\_all\_ships |
| **2** | staging\_ship\_mapping | daily | load\_staging\_all\_ship\_mappings |
| **3** | ods\_ship | Dataset | load\_ods\_ships |
| **4** | mart\_maritime\_base | Dataset | load\_dim\_ship |

## SOF Visit

### Staging SOF (stg\_statement\_of\_fact)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field name** | **Alias** | **Field Type** | **Descriptions** |
| 1 | generation\_id | Generation ID | String | Generation identifier for the SOF |
| 2 | version | Version | bigint | Version number of the SOF |
| 3 | entry\_id | Entry ID | String | Unique entry identifier |
| 4 | unlocode | UNLOCODE | String | Port UNLOCODE |
| 5 | view | View | String | View type (e.g., 'PORT', 'TERMINAL') |
| 6 | ship | Ship | jsonb | Ship information (IMO, MMSI, name, type, categories) |
| 7 | start | Start | jsonb | Visit start information (timestamp, location) |
| 8 | end | End | jsonb | Visit end information (timestamp, location) |
| 9 | area | Area | jsonb | Port area information |
| 10 | previous\_port | Previous Port | jsonb | Previous port visit information |
| 11 | port\_areas | Port Areas | jsonb | Port areas visited |
| 12 | berth\_visits | Berth Visits | jsonb | Array of berth visit events |
| 13 | terminal\_visits | Terminal Visits | jsonb | Array of terminal visit events |
| 14 | anchor\_stops | Anchor Stops | jsonb | Array of anchor stop events |
| 15 | unclassified\_stops | Unclassified Stops | jsonb | Array of unclassified stop events |
| 16 | encounters | Encounters | jsonb | Array of ship encounter events |
| 17 | pilot\_inbound | Pilot Inbound | jsonb | Inbound pilot information |
| 18 | pilot\_outbound | Pilot Outbound | jsonb | Outbound pilot information |
| 19 | lock\_stops | Lock Stops | jsonb | Array of lock stop events |
| 20 | approach\_areas | Approach Areas | jsonb | Array of approach area visits |
| 21 | ship\_to\_ship\_transfer\_transfers | Ship-to-Ship Transfers | jsonb | Array of STS transfer events |
| 22 | slow\_moving\_periods | Slow Moving Periods | jsonb | Array of slow-moving period events |
| 23 | vessel\_type | Vessel Type | String | Type of vessel ('SEA\_VESSEL' or 'BARGE') |
| 24 | created\_timestamp | Created Timestamp | timestamp with time zone | Record creation timestamp |
| 25 | updated\_timestamp | Updated Timestamp | timestamp with time zone | Record update timestamp |

### STAGING SOF DELETED (stg\_statement\_of\_fact\_deleted)

**Purpose**: Tracks deleted statement-of-fact records for delete operations and act as a history table.

| No. | Field Name | Alias | Data Type | Descriptions |
| --- | --- | --- | --- | --- |
| 1 | generation\_id | Generation ID | String | Generation identifier |
| 2 | version | Version | BigInt | Version number |
| 3 | entry\_id | Entry ID | String | Entry identifier |
| 4 | unlocode | UNLOCODE | String | United Nations Code for Trade and Transport Locations |
| 5 | view | View | String | View type |
| 6 | ship | Ship | JSONB | Ship information (JSONB) |
| 7 | start | Start | JSONB | Start information (JSONB) |
| 8 | end | End | JSONB | End information (JSONB) |
| 9 | area | Area | JSONB | Area polygon geometry |
| 10 | previous\_port | Previous Port | JSONB | Previous Port |
| 11 | port\_areas | Port Areas | JSONB | Port Areas |
| 12 | berth\_visits | Berth Visits | JSONB | Berth Visits information (JSONB) |
| 13 | terminal\_visits | Terminal Visits | JSONB | Terminal Visits information (JSONB) |
| 14 | anchor\_stops | Anchor Stops | JSONB | Anchor Stops information (JSONB) |
| 15 | unclassified\_stops | Unclassified Stops | JSONB | Unclassified Stops |
| 16 | encounters | Encounters | JSONB | Encounters |
| 17 | pilot\_inbound | Pilot Inbound | JSONB | Pilot Inbound information (JSONB) |
| 18 | pilot\_outbound | Pilot Outbound | JSONB | Pilot Outbound information (JSONB) |
| 19 | lock\_stops | Lock Stops | JSONB | Lock Stops |
| 20 | approach\_areas | Approach Areas | JSONB | Approach Areas |
| 21 | ship\_to\_ship\_transfer\_transfers | Ship To Ship Transfer Transfers | JSONB | Ship To Ship Transfer Transfers |
| 22 | slow\_moving\_periods | Slow Moving Periods | JSONB | Slow Moving Periods information (JSONB) |
| 23 | created\_timestamp | Created Timestamp | Timestamp (TZ) | Record creation timestamp |
| 24 | updated\_timestamp | Updated Timestamp | Timestamp (TZ) | Record update timestamp |
| 25 | vessel\_type | Vessel Type | String | Vessel type |

### ODS SOF

**ods\_anchor\_stop**

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Unique identifier (Primary Key) |
| 2 | port\_visit\_id | Port Visit ID | String | Port visit identifier |
| 3 | visit\_id | Visit ID | String | Visit identifier |
| 4 | unlocode | UNLOCODE | String | United Nations Code for Trade and Transport Locations |
| 5 | view | View | String | View type |
| 6 | port\_area\_ref | Port Area Ref | String | Port Area Ref |
| 7 | area\_id | Area ID | String | Area identifier |
| 8 | area\_name | Area Name | String | Area name |
| 9 | area\_type | Area Type | String | Area type |
| 10 | area\_unlocode | Area UNLOCODE | String | Area Unlocode |
| 11 | start\_location\_lat | Start Location Lat | Double | Start location latitude |
| 12 | start\_location\_lon | Start Location Lon | Double | Start location longitude |
| 13 | start\_date | Start Date | Date | Start Date |
| 14 | start\_time | Start Time | Time | Start Time |
| 15 | start\_timestamp | Start Timestamp | Timestamp | Start timestamp |
| 16 | end\_location\_lat | End Location Lat | Double | End location latitude |
| 17 | end\_location\_lon | End Location Lon | Double | End location longitude |
| 18 | end\_date | End Date | Date | End Date |
| 19 | end\_time | End Time | Time | End Time |
| 20 | end\_timestamp | End Timestamp | Timestamp | End timestamp |
| 21 | version | Version | Integer | Version number |
| 22 | created\_timestamp | Created Timestamp | Timestamp (TZ) | Record creation timestamp |
| 23 | updated\_timestamp | Updated Timestamp | Timestamp (TZ) | Record update timestamp |
| 24 | deleted\_timestamp | Deleted Timestamp | Timestamp (TZ) | Record deletion timestamp (soft delete) |
| 25 | start\_fallback | Start Fallback | String | Start Fallback |
| 26 | end\_fallback | End Fallback | String | End Fallback |

### ods\_encounter

Operational Data Store for vessel encounter events

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Unique identifier (Primary Key) |
| 2 | port\_visit\_id | Port Visit ID | String | Port visit identifier |
| 3 | visit\_id | Visit ID | String | Visit identifier |
| 4 | unlocode | UNLOCODE | String | United Nations Code for Trade and Transport Locations |
| 5 | ship\_imo | Ship IMO | String | Ship Imo |
| 6 | ship\_mmsi | Ship MMSI | String | Ship Mmsi |
| 7 | ship\_type | Ship Type | String | Ship type |
| 8 | start\_location\_lat | Start Location Lat | Double | Start location latitude |
| 9 | start\_location\_lon | Start Location Lon | Double | Start location longitude |
| 10 | start\_date | Start Date | Date | Start Date |
| 11 | start\_time | Start Time | Time | Start Time |
| 12 | start\_timestamp | Start Timestamp | Timestamp | Start timestamp |
| 13 | end\_location\_lat | End Location Lat | Double | End location latitude |
| 14 | end\_location\_lon | End Location Lon | Double | End location longitude |
| 15 | end\_date | End Date | Date | End Date |
| 16 | end\_time | End Time | Time | End Time |
| 17 | end\_timestamp | End Timestamp | Timestamp | End timestamp |
| 18 | port\_area\_ref | Port Area Ref | String | Port Area Ref |
| 19 | berth\_visit\_ref | Berth Visit Ref | String | Berth Visit Ref |
| 20 | terminal\_visit\_ref | Terminal Visit Ref | String | Terminal Visit Ref |
| 21 | created\_timestamp | Created Timestamp | Timestamp (TZ) | Record creation timestamp |
| 22 | updated\_timestamp | Updated Timestamp | Timestamp (TZ) | Record update timestamp |
| 23 | deleted\_timestamp | Deleted Timestamp | Timestamp (TZ) | Record deletion timestamp (soft delete) |

### ods\_lock\_stop

Operational Data Store for lock stop events

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Unique identifier (Primary Key) |
| 2 | port\_visit\_id | Port Visit ID | String | Port visit identifier |
| 3 | visit\_id | Visit ID | String | Visit identifier |
| 4 | lock\_id | Lock ID | String | Lock identifier |
| 5 | start\_location\_lat | Start Location Lat | Double | Start location latitude |
| 6 | start\_location\_lon | Start Location Lon | Double | Start location longitude |
| 7 | start\_date | Start Date | Date | Start Date |
| 8 | start\_time | Start Time | Time | Start Time |
| 9 | start\_timestamp | Start Timestamp | Timestamp | Start timestamp |
| 10 | end\_location\_lat | End Location Lat | Double | End location latitude |
| 11 | end\_location\_lon | End Location Lon | Double | End location longitude |
| 12 | end\_date | End Date | Date | End Date |
| 13 | end\_time | End Time | Time | End Time |
| 14 | end\_timestamp | End Timestamp | Timestamp | End timestamp |
| 15 | area\_id | Area ID | String | Area identifier |
| 16 | area\_name | Area Name | String | Area name |
| 17 | area\_type | Area Type | String | Area type |
| 18 | area\_unlocode | Area UNLOCODE | String | Area Unlocode |
| 19 | port\_area\_ref | Port Area Ref | Integer | Port Area Ref |
| 20 | created\_timestamp | Created Timestamp | Timestamp (TZ) | Record creation timestamp |
| 21 | updated\_timestamp | Updated Timestamp | Timestamp (TZ) | Record update timestamp |
| 22 | deleted\_timestamp | Deleted Timestamp | Timestamp (TZ) | Record deletion timestamp (soft delete) |

### ods\_unclassified\_stop

Operational Data Store for unclassified stop events

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Unique identifier (Primary Key) |
| 2 | port\_visit\_id | Port Visit ID | String | Port visit identifier |
| 3 | visit\_id | Visit ID | String | Visit identifier |
| 4 | unlocode | UNLOCODE | String | United Nations Code for Trade and Transport Locations |
| 5 | view | View | String | View type |
| 6 | port\_area\_ref | Port Area Ref | String | Port Area Ref |
| 7 | start\_location\_lat | Start Location Lat | Double | Start location latitude |
| 8 | start\_location\_lon | Start Location Lon | Double | Start location longitude |
| 9 | start\_date | Start Date | Date | Start Date |
| 10 | start\_time | Start Time | Time | Start Time |
| 11 | start\_timestamp | Start Timestamp | Timestamp | Start timestamp |
| 12 | end\_location\_lat | End Location Lat | Double | End location latitude |
| 13 | end\_location\_lon | End Location Lon | Double | End location longitude |
| 14 | end\_date | End Date | Date | End Date |
| 15 | end\_time | End Time | Time | End Time |
| 16 | end\_timestamp | End Timestamp | Timestamp | End timestamp |
| 17 | version | Version | Integer | Version number |
| 18 | created\_timestamp | Created Timestamp | Timestamp (TZ) | Record creation timestamp |
| 19 | updated\_timestamp | Updated Timestamp | Timestamp (TZ) | Record update timestamp |
| 20 | deleted\_timestamp | Deleted Timestamp | Timestamp (TZ) | Record deletion timestamp (soft delete) |

## BRIDGE TABLE

A bridge table, also known as an *associative entity* or *linking table*, is an intermediate table in a database that resolves many-to-many relationships between two other tables.

**ods\_berth\_visit\_tug\_events**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field name** | **Alias** | **Field Type** | **Descriptions** |
| **1** | id | ID | String | PRIMARY KEY (id) |
| **2** | berth\_visit\_id | Berth Visit ID | String | Visit Identification |
| **3** | tug\_event\_id | Tug Event ID | String | Tug Event Identification |

### ods\_port\_approach\_areas

Relationship table linking ports to approach areas

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field Name** | **Alias** | **Field Type** | **Descriptions** |
| **1** | id | ID | String | PRIMARY KEY (id) |
| **2** | port\_visit\_id | Port Visit ID | String | Port Visit Id |
| **3** | approach\_area\_id | Approach Area ID | String | Approach Area Id |

### ods\_port\_berths

Relationship table linking ports to berths

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | UUID | Unique identifier (Primary Key) |
| 2 | port\_id | Port ID | String | Port identifier |
| 3 | berth\_id | Berth ID | String | Berth identifier |

### ods\_port\_locks

Relationship table linking ports to locks

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | UUID | Unique identifier (Primary Key) |
| 2 | port\_id | Port ID | String | Port identifier |
| 3 | lock\_id | Lock ID | String | Lock identifier |

### ods\_port\_terminals

Relationship table linking ports to terminals

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | UUID | Unique identifier (Primary Key) |
| 2 | port\_id | Port ID | String | Port identifier |
| 3 | terminal\_id | Terminal ID | String | Terminal identifier |

**ods\_port\_visit\_encounters**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field Name** | **Alias** | **Field Type** | **Descriptions** |
| **1** | id | ID | String | PRIMARY KEY (id) |
| **2** | port\_visit\_id | Port Visit ID | String | Port Visit Id |
| **3** | encounter\_id | Encounter ID | String | Encounter Id |

**ods\_port\_visit\_lock\_stops**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field Name** | **Alias** | **Field Type** | **Descriptions** |
| **1** | id | ID | String | PRIMARY KEY (id) |
| **2** | port\_visit\_id | Port Visit ID | String | Port Visit Id |
| **3** | lock\_stop\_id | Lock Stop ID | String | Lock Stop Id |

**ods\_port\_visit\_terminal\_visit**

Relationship table linking port visits to terminal visits

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field Name** | **Alias** | **Field Type** | **Descriptions** |
| **1** | id | ID | String | PRIMARY KEY (id) |
| **2** | port\_visit\_id | Port Visit ID | String | Port Visit Id |
| **3** | terminal\_visit\_id | Terminal Visit ID | String | Terminal Visit Id |

**ods\_port\_visit\_unclassified\_stops**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field Name** | **Alias** | **Field Type** | **Descriptions** |
| **1** | id | ID | String | PRIMARY KEY (id) |
| **2** | port\_visit\_id | Port Visit ID | String | Port Visit Id |
| **3** | stop\_id | Stop ID | String | Stop Id |
| **4** | stops\_count | Stops Count | Integer | Stops count |

**ods\_terminal\_visit\_berth\_visit**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field Name** | **Alias** | **Field Type** | **Descriptions** |
| **1** | id | ID | String | PRIMARY KEY (id) |
| **2** | terminal\_visit\_id | Terminal Visit ID | String | Terminal Visit Id |
| **3** | berth\_visit\_id | Berth Visit ID | String | Berth Visit Id |

## VISIT TABLE

**ods\_port\_visit**

Operational Data Store for port visit transactional data

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Unique identifier (Primary Key) |
| 2 | visit\_id | Visit ID | String | Visit identifier |
| 3 | port\_id | Port ID | String | Port identifier |
| 4 | prev\_port\_id | Prev Port ID | String | Prev Port identifier |
| 5 | view | View | String | View type |
| 6 | ship\_imo | Ship IMO | String | Ship Imo |
| 7 | ship\_mmsi | Ship MMSI | String | Ship Mmsi |
| 8 | ship\_name | Ship Name | String | Ship name |
| 9 | ship\_type | Ship Type | String | Ship type |
| 10 | ship\_category\_v1 | Ship Category V1 | String | Ship Category V1 |
| 11 | ship\_category\_v2 | Ship Category V2 | String | Ship Category V2 |
| 12 | ship\_category\_v3 | Ship Category V3 | String | Ship Category V3 |
| 13 | ship\_length | Ship Length | Double | Ship Length |
| 14 | ship\_beam | Ship Beam | Double | Ship Beam |
| 15 | ship\_max\_draught | Ship Max Draught | Double | Ship Max Draught |
| 16 | pilot\_inbound\_area\_id | Pilot Inbound Area ID | String | Pilot Inbound Area identifier |
| 17 | pilot\_inbound\_area\_name | Pilot Inbound Area Name | String | Pilot Inbound Area name |
| 18 | pilot\_inbound\_area\_type | Pilot Inbound Area Type | String | Pilot Inbound Area Type |
| 19 | pilot\_inbound\_area\_unlocode | Pilot Inbound Area UNLOCODE | String | Pilot Inbound Area Unlocode |
| 20 | pilot\_inbound\_ship\_imo | Pilot Inbound Ship IMO | String | Pilot Inbound Ship Imo |
| 21 | pilot\_inbound\_ship\_mmsi | Pilot Inbound Ship MMSI | String | Pilot Inbound Ship Mmsi |
| 22 | pilot\_inbound\_ship\_type | Pilot Inbound Ship Type | String | Pilot Inbound Ship Type |
| 23 | pilot\_inbound\_start\_date | Pilot Inbound Start Date | Date | Pilot Inbound Start Date |
| 24 | pilot\_inbound\_start\_time | Pilot Inbound Start Time | Time | Pilot Inbound Start Time |
| 25 | pilot\_inbound\_start\_timestamp | Pilot Inbound Start Timestamp | Timestamp | Pilot Inbound Start timestamp |
| 26 | pilot\_inbound\_start\_location\_lat | Pilot Inbound Start Location Lat | Double | Pilot Inbound Start Location Lat |
| 27 | pilot\_inbound\_start\_location\_lon | Pilot Inbound Start Location Lon | Double | Pilot Inbound Start Location Lon |
| 28 | pilot\_inbound\_end\_date | Pilot Inbound End Date | Date | Pilot Inbound End Date |
| 29 | pilot\_inbound\_end\_time | Pilot Inbound End Time | Time | Pilot Inbound End Time |
| 30 | pilot\_inbound\_end\_timestamp | Pilot Inbound End Timestamp | Timestamp | Pilot Inbound End timestamp |
| 31 | pilot\_inbound\_end\_location\_lat | Pilot Inbound End Location Lat | Double | Pilot Inbound End Location Lat |
| 32 | pilot\_inbound\_end\_location\_lon | Pilot Inbound End Location Lon | Double | Pilot Inbound End Location Lon |
| 33 | pilot\_inbound\_fallback\_detection\_type | Pilot Inbound Fallback Detection Type | String | Pilot Inbound Fallback Detection Type |
| 34 | pilot\_outbound\_area\_id | Pilot Outbound Area ID | String | Pilot Outbound Area identifier |
| 35 | pilot\_outbound\_area\_name | Pilot Outbound Area Name | String | Pilot Outbound Area name |
| 36 | pilot\_outbound\_area\_type | Pilot Outbound Area Type | String | Pilot Outbound Area Type |
| 37 | pilot\_outbound\_area\_unlocode | Pilot Outbound Area UNLOCODE | String | Pilot Outbound Area Unlocode |
| 38 | pilot\_outbound\_ship\_imo | Pilot Outbound Ship IMO | String | Pilot Outbound Ship Imo |
| 39 | pilot\_outbound\_ship\_mmsi | Pilot Outbound Ship MMSI | String | Pilot Outbound Ship Mmsi |
| 40 | pilot\_outbound\_ship\_type | Pilot Outbound Ship Type | String | Pilot Outbound Ship Type |
| 41 | pilot\_outbound\_start\_date | Pilot Outbound Start Date | Date | Pilot Outbound Start Date |
| 42 | pilot\_outbound\_start\_time | Pilot Outbound Start Time | Time | Pilot Outbound Start Time |
| 43 | pilot\_outbound\_start\_timestamp | Pilot Outbound Start Timestamp | Timestamp | Pilot Outbound Start timestamp |
| 44 | pilot\_outbound\_start\_location\_lat | Pilot Outbound Start Location Lat | Double | Pilot Outbound Start Location Lat |
| 45 | pilot\_outbound\_start\_location\_lon | Pilot Outbound Start Location Lon | Double | Pilot Outbound Start Location Lon |
| 46 | pilot\_outbound\_end\_date | Pilot Outbound End Date | Date | Pilot Outbound End Date |
| 47 | pilot\_outbound\_end\_time | Pilot Outbound End Time | Time | Pilot Outbound End Time |
| 48 | pilot\_outbound\_end\_timestamp | Pilot Outbound End Timestamp | Timestamp | Pilot Outbound End timestamp |
| 49 | pilot\_outbound\_end\_location\_lat | Pilot Outbound End Location Lat | Double | Pilot Outbound End Location Lat |
| 50 | pilot\_outbound\_end\_location\_lon | Pilot Outbound End Location Lon | Double | Pilot Outbound End Location Lon |
| 51 | pilot\_outbound\_fallback\_detection\_type | Pilot Outbound Fallback Detection Type | String | Pilot Outbound Fallback Detection Type |
| 52 | start\_location\_lat | Start Location Lat | Double | Start location latitude |
| 53 | start\_location\_lon | Start Location Lon | Double | Start location longitude |
| 54 | start\_date | Start Date | Date | Start Date |
| 55 | start\_time | Start Time | Time | Start Time |
| 56 | start\_timestamp | Start Timestamp | Timestamp | Start timestamp |
| 57 | end\_location\_lat | End Location Lat | Double | End location latitude |
| 58 | end\_location\_lon | End Location Lon | Double | End location longitude |
| 59 | end\_date | End Date | Date | End Date |
| 60 | end\_time | End Time | Time | End Time |
| 61 | end\_timestamp | End Timestamp | Timestamp | End timestamp |
| 62 | version | Version | Integer | Version number |
| 63 | created\_timestamp | Created Timestamp | Timestamp (TZ) | Record creation timestamp |
| 64 | updated\_timestamp | Updated Timestamp | Timestamp (TZ) | Record update timestamp |
| 65 | deleted\_timestamp | Deleted Timestamp | Timestamp (TZ) | Record deletion timestamp (soft delete) |
| 66 | visit\_vessel\_type | Visit Vessel Type | String | Visit vessel type |

**ods\_terminal\_visit**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field Name** | **Alias** | **Field Type** |  |
| **1** | id | id | String | PRIMARY KEY (id) |
| **2** | port\_visit\_id | port visit id | String |  |
| **3** | visit\_id | visit id | String |  |
| **4** | terminal\_id | terminal id | String |  |
| **5** | start\_location\_lat | start location lat | double precision |  |
| **6** | start\_location\_lon | start location lon | double precision |  |
| **7** | start\_date | start date | date |  |
| **8** | start\_time | start time | time |  |
| **9** | start\_timestamp | start timestamp | timestamp |  |
| **10** | end\_location\_lat | end location lat | double precision |  |
| **11** | end\_location\_lon | end location lon | double precision |  |
| **12** | end\_date | end date | date |  |
| **13** | end\_time | end time | time |  |
| **14** | end\_timestamp | end timestamp | timestamp |  |
| **15** | mooring\_start\_location\_lat | mooring start location lat | double precision |  |
| **16** | mooring\_start\_location\_lon | mooring start location lon | double precision |  |
| **17** | mooring\_start\_date | mooring start date | date |  |
| **18** | mooring\_start\_time | mooring start time | time |  |
| **19** | mooring\_start\_timestamp | mooring start timestamp | timestamp |  |
| **20** | mooring\_end\_location\_lat | mooring end location lat | double precision |  |
| **21** | mooring\_end\_location\_lon | mooring end location lon | double precision |  |
| **22** | mooring\_end\_date | mooring end date | date |  |
| **23** | mooring\_end\_time | mooring end time | time |  |
| **24** | mooring\_end\_timestamp | mooring end timestamp | timestamp |  |
| **25** | area\_id | area id | String |  |
| **26** | area\_name | area name | String |  |
| **27** | area\_type | area type | String |  |
| **28** | area\_unlocode | area unlocode | String |  |
| **29** | ref | ref | integer |  |
| **30** | port\_area\_ref | port area ref | integer |  |

### ods\_berth\_visit

Operational Data Store for berth visit transactional data

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Unique identifier (Primary Key) |
| 2 | port\_visit\_id | Port Visit ID | String | Port visit identifier |
| 3 | visit\_id | Visit ID | String | Visit identifier |
| 4 | custom\_input\_terminal\_id | Custom Input Terminal ID | String | Custom Input Terminal identifier |
| 5 | berth\_id | Berth ID | String | Berth identifier |
| 6 | start\_location\_lat | Start Location Lat | Double | Start location latitude |
| 7 | start\_location\_lon | Start Location Lon | Double | Start location longitude |
| 8 | start\_date | Start Date | Date | Start Date |
| 9 | start\_time | Start Time | Time | Start Time |
| 10 | start\_timestamp | Start Timestamp | Timestamp | Start timestamp |
| 11 | end\_location\_lat | End Location Lat | Double | End location latitude |
| 12 | end\_location\_lon | End Location Lon | Double | End location longitude |
| 13 | end\_date | End Date | Date | End Date |
| 14 | end\_time | End Time | Time | End Time |
| 15 | end\_timestamp | End Timestamp | Timestamp | End timestamp |
| 16 | all\_fast\_location\_lat | All Fast Location Lat | Double | All Fast Location Lat |
| 17 | all\_fast\_location\_lon | All Fast Location Lon | Double | All Fast Location Lon |
| 18 | all\_fast\_date | All Fast Date | Date | All Fast Date |
| 19 | all\_fast\_time | All Fast Time | Time | All Fast Time |
| 20 | all\_fast\_timestamp | All Fast Timestamp | Timestamp | All Fast timestamp |
| 21 | first\_line\_secured\_location\_lat | First Line Secured Location Lat | Double | First Line Secured Location Lat |
| 22 | first\_line\_secured\_location\_lon | First Line Secured Location Lon | Double | First Line Secured Location Lon |
| 23 | first\_line\_secured\_date | First Line Secured Date | Date | First Line Secured Date |
| 24 | first\_line\_secured\_time | First Line Secured Time | Time | First Line Secured Time |
| 25 | first\_line\_secured\_timestamp | First Line Secured Timestamp | Timestamp | First Line Secured timestamp |
| 26 | last\_line\_released\_location\_lat | Last Line Released Location Lat | Double | Last Line Released Location Lat |
| 27 | last\_line\_released\_location\_lon | Last Line Released Location Lon | Double | Last Line Released Location Lon |
| 28 | last\_line\_released\_date | Last Line Released Date | Date | Last Line Released Date |
| 29 | last\_line\_released\_time | Last Line Released Time | Time | Last Line Released Time |
| 30 | last\_line\_released\_timestamp | Last Line Released Timestamp | Timestamp | Last Line Released timestamp |
| 31 | area\_id | Area ID | String | Area identifier |
| 32 | area\_name | Area Name | String | Area name |
| 33 | area\_type | Area Type | String | Area type |
| 34 | area\_unlocode | Area UNLOCODE | String | Area Unlocode |
| 35 | mooring\_type | Mooring Type | String | Mooring Type |
| 36 | cargo\_category\_type | Cargo Category Type | JSONB | Cargo Category Type |
| 37 | ref | Ref | Integer | Ref |
| 38 | port\_area\_ref | Port Area Ref | Integer | Port Area Ref |
| 39 | terminal\_visit\_ref | Terminal Visit Ref | Integer | Terminal Visit Ref |
| 40 | created\_timestamp | Created Timestamp | Timestamp (TZ) | Record creation timestamp |
| 41 | updated\_timestamp | Updated Timestamp | Timestamp (TZ) | Record update timestamp |
| 42 | deleted\_timestamp | Deleted Timestamp | Timestamp (TZ) | Record deletion timestamp (soft delete) |
| 43 | visit\_vessel\_type | Visit Vessel Type | String | Visit vessel type |

**ods\_tug\_event**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field Name** | **Alias** | **Field Type** | **Descriptions** |
| **1** | id | ID | String | PRIMARY KEY (id) |
| **2** | ship\_imo | Ship IMO | String | IMO of the ship |
| **3** | ship\_mmsi | Ship MMSI | String | MMSI of the ship |
| **4** | ship\_type | Ship Type | String | Type of the ship |
| **5** | start\_location\_lat | Start Location Lat | Double Precision | Start Location Latitude Coordinate |
| **6** | start\_location\_lon | Start Location Lon | Double Precision | Start Location Longitude Coordinate |
| **7** | start\_date | Start Date | date |  |
| **8** | start\_time | Start Time | time |  |
| **9** | start\_timestamp | Start Timestamp | timestamp |  |
| **10** | end\_location\_lat | End Location Lat | Double Precision | End Location Latitude Coordinate |
| **11** | end\_location\_lon | End Location Lon | Double Precision | End Location Longitude Coordinate |
| **12** | end\_date | End Date | date |  |
| **13** | end\_time | End Time | time |  |
| **14** | end\_timestamp | End Timestamp | timestamp |  |
| **15** | type | Type | String |  |

**ods\_unclassified\_stops**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field Name** | **Alias** | **Field Type** | **Descriptions** |
| **1** | id | ID | String | PRIMARY KEY (id) |
| **2** | visit\_id | Visit ID | String | Visit Id |
| **3** | unlocode | UNLOCODE | String | United Nations Code for Trade and Transport Locations |
| **4** | view | View | String | View |
| **5** | start\_location\_lat | Start Location Lat | Double Precision | Start Location Latitude Coordinate |
| **6** | start\_location\_lon | Start Location Lon | Double Precision | Start Location Longitude Coordinate |
| **7** | start\_date | Start Date | date |  |
| **8** | start\_time | Start Time | time |  |
| **9** | start\_timestamp | Start Timestamp | timestamp |  |
| **10** | end\_location\_lat | End Location Lat | Double Precision | End Location Latitude Coordinate |
| **11** | end\_location\_lon | End Location Lon | Double Precision | End Location Longitude Coordinate |
| **12** | end\_date | End Date | date |  |
| **13** | end\_time | End Time | time |  |
| **14** | end\_timestamp | End Timestamp | timestamp |  |
| **15** | version | Version | String |  |

**ods\_visited\_approach\_area**

Operational Data Store for visited approach area events

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Unique identifier (Primary Key) |
| 2 | port\_visit\_id | Port Visit ID | String | Port visit identifier |
| 3 | visit\_id | Visit ID | String | Visit identifier |
| 4 | approach\_area\_id | Approach Area ID | String | Approach Area identifier |
| 5 | start\_location\_lat | Start Location Lat | Double | Start location latitude |
| 6 | start\_location\_lon | Start Location Lon | Double | Start location longitude |
| 7 | start\_date | Start Date | Date | Start Date |
| 8 | start\_time | Start Time | Time | Start Time |
| 9 | start\_timestamp | Start Timestamp | Timestamp | Start timestamp |
| 10 | end\_location\_lat | End Location Lat | Double | End location latitude |
| 11 | end\_location\_lon | End Location Lon | Double | End location longitude |
| 12 | end\_date | End Date | Date | End Date |
| 13 | end\_time | End Time | Time | End Time |
| 14 | end\_timestamp | End Timestamp | Timestamp | End timestamp |
| 15 | area\_id | Area ID | String | Area identifier |
| 16 | area\_name | Area Name | String | Area name |
| 17 | area\_type | Area Type | String | Area type |
| 18 | area\_unlocode | Area UNLOCODE | String | Area Unlocode |
| 19 | port\_area\_ref | Port Area Ref | Integer | Port Area Ref |
| 20 | created\_timestamp | Created Timestamp | Timestamp (TZ) | Record creation timestamp |
| 21 | updated\_timestamp | Updated Timestamp | Timestamp (TZ) | Record update timestamp |
| 22 | deleted\_timestamp | Deleted Timestamp | Timestamp (TZ) | Record deletion timestamp (soft delete) |

### ods\_ship\_to\_ship\_transfers

Operational Data Store for ship-to-ship transfer events

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Unique identifier (Primary Key) |
| 2 | port\_visit\_id | Port Visit ID | String | Port visit identifier |
| 3 | visit\_id | Visit ID | String | Visit identifier |
| 4 | unlocode | UNLOCODE | String | United Nations Code for Trade and Transport Locations |
| 5 | view | View | String | View type |
| 6 | ship\_imo | Ship IMO | String | Ship Imo |
| 7 | ship\_type | Ship Type | String | Ship type |
| 8 | ship\_name | Ship Name | String | Ship name |
| 9 | area\_name | Area Name | String | Area name |
| 10 | area\_type | Area Type | String | Area type |
| 11 | area\_id | Area ID | String | Area identifier |
| 12 | start\_location\_lat | Start Location Lat | Double | Start location latitude |
| 13 | start\_location\_lon | Start Location Lon | Double | Start location longitude |
| 14 | start\_date | Start Date | Date | Start Date |
| 15 | start\_time | Start Time | Time | Start Time |
| 16 | start\_timestamp | Start Timestamp | Timestamp | Start timestamp |
| 17 | start\_fallback | Start Fallback | String | Start Fallback |
| 18 | end\_location\_lat | End Location Lat | Double | End location latitude |
| 19 | end\_location\_lon | End Location Lon | Double | End location longitude |
| 20 | end\_date | End Date | Date | End Date |
| 21 | end\_time | End Time | Time | End Time |
| 22 | end\_timestamp | End Timestamp | Timestamp | End timestamp |
| 23 | end\_fallback | End Fallback | String | End Fallback |
| 24 | created\_timestamp | Created Timestamp | Timestamp (TZ) | Record creation timestamp |
| 25 | updated\_timestamp | Updated Timestamp | Timestamp (TZ) | Record update timestamp |
| 26 | deleted\_timestamp | Deleted Timestamp | Timestamp (TZ) | Record deletion timestamp (soft delete) |

### ods\_slow\_moving\_period

Operational Data Store for slow-moving period events (waiting/idle periods)

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Unique identifier (Primary Key) |
| 2 | port\_visit\_id | Port Visit ID | String | Port visit identifier |
| 3 | start\_location\_lat | Start Location Lat | Double | Start location latitude |
| 4 | start\_location\_lon | Start Location Lon | Double | Start location longitude |
| 5 | start\_date | Start Date | Date | Start Date |
| 6 | start\_time | Start Time | Time | Start Time |
| 7 | start\_timestamp | Start Timestamp | Timestamp | Start timestamp |
| 8 | start\_fallback | Start Fallback | String | Start Fallback |
| 9 | end\_location\_lat | End Location Lat | Double | End location latitude |
| 10 | end\_location\_lon | End Location Lon | Double | End location longitude |
| 11 | end\_date | End Date | Date | End Date |
| 12 | end\_time | End Time | Time | End Time |
| 13 | end\_timestamp | End Timestamp | Timestamp | End timestamp |
| 14 | end\_fallback | End Fallback | String | End Fallback |
| 15 | speed\_min | Speed Min | Double | Speed Min |
| 16 | speed\_max | Speed Max | Double | Speed Max |
| 17 | speed\_avg | Speed Avg | Double | Speed Avg |
| 18 | speed\_count | Speed Count | Integer | Speed count |
| 19 | speed\_last\_speed\_over\_ground | Speed Last Speed Over Ground | Double | Speed Last Speed Over Ground |
| 20 | speed\_duration | Speed Duration | interval | Speed duration in hours |
| 21 | speed\_last\_speed\_over\_ground\_timestamp | Speed Last Speed Over Ground Timestamp | Timestamp | Speed Last Speed Over Ground timestamp |
| 22 | type | Type | String | Type |
| 23 | created\_timestamp | Created Timestamp | Timestamp (TZ) | Record creation timestamp |
| 24 | updated\_timestamp | Updated Timestamp | Timestamp (TZ) | Record update timestamp |
| 25 | deleted\_timestamp | Deleted Timestamp | Timestamp (TZ) | Record deletion timestamp (soft delete) |

## Area Occupancy

### ods\_area\_occupancy

Operational Data Store for area occupancy snapshots

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Unique identifier (Primary Key) |
| 2 | area | Area | String | Area polygon geometry |
| 3 | type | Type | String | Type |
| 4 | occupancy\_date | Occupancy Date | Date | Occupancy Date |
| 5 | occupancy\_time | Occupancy Time | Time | Occupancy Time |
| 6 | occupancy\_timestamp | Occupancy Timestamp | Timestamp | Occupancy timestamp |
| 7 | created\_timestamp | Created Timestamp | Timestamp (TZ) | Record creation timestamp |
| 8 | updated\_timestamp | Updated Timestamp | Timestamp (TZ) | Record update timestamp |

### ods\_area\_occupancy\_ships

Operational Data Store for ships in area occupancy snapshots

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | UUID | Unique identifier (Primary Key) |
| 2 | area\_occupancy\_id | Area Occupancy ID | String | Area Occupancy identifier |
| 3 | ship\_id | Ship ID | String | Ship identifier |
| 4 | fallback\_ship\_id | Fallback Ship ID | String | Fallback Ship identifier |

## Service Vessel

### ods\_service\_vessel

Operational Data Store for service vessel events

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Unique identifier (Primary Key) |
| 2 | service\_vessel\_id | Service Vessel ID | String | Service vessel identifier |
| 3 | service\_vessel\_imo | Service Vessel IMO | String | Service Vessel Imo |
| 4 | service\_vessel\_mmsi | Service Vessel MMSI | String | Service Vessel Mmsi |
| 5 | service\_vessel\_role | Service Vessel Role | String | Service Vessel Role |
| 6 | related\_vessel\_id | Related Vessel ID | String | Related Vessel identifier |
| 7 | related\_vessel\_imo | Related Vessel IMO | String | Related Vessel Imo |
| 8 | related\_vessel\_mmsi | Related Vessel MMSI | String | Related Vessel Mmsi |
| 9 | related\_vessel\_role | Related Vessel Role | String | Related Vessel Role |
| 10 | related\_vessel\_visit\_id | Related Vessel Visit ID | String | Related Vessel Visit identifier |
| 11 | start\_date | Start Date | Date | Start Date |
| 12 | start\_time | Start Time | Time | Start Time |
| 13 | start\_timestamp | Start Timestamp | Timestamp | Start timestamp |
| 14 | start\_location\_lat | Start Location Lat | Double | Start location latitude |
| 15 | start\_location\_lon | Start Location Lon | Double | Start location longitude |
| 16 | end\_date | End Date | Date | End Date |
| 17 | end\_time | End Time | Time | End Time |
| 18 | end\_timestamp | End Timestamp | Timestamp | End timestamp |
| 19 | end\_location\_lat | End Location Lat | Double | End location latitude |
| 20 | end\_location\_lon | End Location Lon | Double | End location longitude |
| 21 | activity\_type | Activity Type | String | Activity Type |
| 22 | ptt\_stage | Ptt Stage | String | Ptt Stage |
| 23 | visit\_id | Visit ID | String | Visit identifier |
| 24 | created\_timestamp | Created Timestamp | Timestamp (TZ) | Record creation timestamp |
| 25 | updated\_timestamp | Updated Timestamp | Timestamp (TZ) | Record update timestamp |

### Airflow DAG related to SOF Visit

|  |  |  |  |
| --- | --- | --- | --- |
| **No.** | **DAG Name** | **Schedule** | **Tasks** |
| **1** | staging\_statement\_of\_fact | daily | extract\_sofs\_from\_api  load\_staging\_softs\_for\_all\_ports  load\_staging\_softs\_by\_port |
| **2** | ods\_statement\_of\_fact | Dataset | load\_ods\_port\_visits  load\_ods\_terminal\_visits  load\_ods\_berth\_visits  load\_ods\_port\_visit\_terminal\_visits  load\_ods\_terminal\_visit\_berth\_visits  load\_ods\_anchor\_stops  load\_ods\_approach\_areas  load\_ods\_encounters  load\_ods\_lock\_stops  load\_ods\_unclassified\_stops  load\_ods\_visited\_approach\_areas  load\_ods\_tug\_events  load\_ods\_berth\_visit\_tug\_events  load\_ods\_port\_visit\_anchor\_stops  load\_ods\_port\_visit\_approach\_areas  load\_ods\_port\_visit\_encounters  load\_ods\_port\_visit\_lock\_stops  load\_ods\_port\_visit\_unclassified\_stops |
| **3** | visit\_summary | Dataset | load\_fact\_berth\_visit  load\_fact\_terminal\_visit  add\_berth\_visit\_summary\_by\_terminal\_visit |

## Voyage

### Staging Voyage (stg\_voyage)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field name** | **Alias** | **Field Type** | **Descriptions** |
| **1** | entry\_id | ID | String | Entry Id |
| **2** | imo | IMO | String | IMO |
| **3** | start\_voyage | Start Voyage | jsonb | Start Voyage |
| **4** | end\_voyage | End Voyage | jsonb | End Voyage |
| **5** | Trace | Trace | jsonb | Trace |
| **6** | Stop | Stop | jsonb | Stop |
| **7** | pass\_through | Pass Through | jsonb | Pass Through |
| **8** | previous\_voyage | Previous Voyage | jsonb | Previous |
| **9** | next\_voyage | Next Voyage | jsonb | Next |
| **10** | destination | Destination | jsonb | Destinations |
| **11** | finished | Finished | boolean | True if the voyages is finished. |

### ODS Voyage

**ods\_voyage**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field Name** | **Alias** | **Field Type** | **Descriptions** |
| **1** | entry\_id | Entry ID | String | PRIMARY KEY (entry\_id) |
| **2** | imo | IMO | String |  |
| **3** | start\_location\_lat | Start Location Lat | Double Precision | Start Location Latitude Coordinate |
| **4** | start\_location\_lon | Start Location Lon | Double Precision | Start Location Longitude Coordinate |
| **5** | start\_date | Start Date | date |  |
| **6** | start\_time | Start Time | time |  |
| **7** | start\_timestamp | Start Timestamp | timestamp |  |
| **8** | end\_location\_lat | End Location Lat | Double Precision | End Location Latitude Coordinate |
| **9** | end\_location\_lon | End Location Lon | Double Precision | End Location Longitude Coordinate |
| **10** | end\_date | End Date | date |  |
| **11** | end\_time | End Time | time |  |
| **12** | end\_timestamp | End Timestamp | timestamp |  |
| **13** | previous\_port | Previous Port | String |  |
| **15** | previous\_entry\_id | Previous Entry Id | String |  |
| **16** | next\_port | Next Port | String |  |
| **17** | next\_entry\_id | Next Entry Id | String |  |
| **18** | destination\_ais | Destination AIS | String |  |
| **19** | destination\_port | Destination Port | String |  |
| **20** | destination\_date | Destination Date | String |  |
| **21** | destination\_time | Destination Time | String |  |
| **22** | destination\_ timestamp | Destination Timestamp | String |  |
| **23** | finished | Finished | Boolean |  |

**ods\_voyage\_stop**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No.** | **Field Name** | **Alias** | **Field Type** | **Descriptions** |
| **1** | id | ID | String | PRIMARY KEY (id) |
| **2** | imo | IMO | String |  |
| **3** | start\_location\_lat | Start Location Lat | Double Precision | Start Location Latitude Coordinate |
| **4** | start\_location\_lon | Start Location Lon | Double Precision | Start Location Longitude Coordinate |
| **5** | start\_date | Start Date | date |  |
| **6** | start\_time | Start Time | time |  |
| **7** | start\_timestamp | Start Timestamp | timestamp |  |
| **8** | end\_location\_lat | End Location Lat | Double Precision | End Location Latitude Coordinate |
| **9** | end\_location\_lon | End Location Lon | Double Precision | End Location Longitude Coordinate |
| **10** | end\_date | End Date | date |  |
| **11** | end\_time | End Time | time |  |
| **12** | end\_timestamp | End Timestamp | timestamp |  |
| **13** | area\_type | Area Type | String |  |
| **14** | area\_id | Area Id | String |  |
| **15** | accuracy | Accuracy | String |  |
| **16** | next\_entry\_id | Next Entry Id | String |  |
| **17** | location\_lat | Location Lat | Double Precision | Location Latitude Coordinate |
| **18** | location\_lon | Location Lon | Double Precision | Location Longitude Coordinate |

### Airflow Voyage

|  |  |  |  |
| --- | --- | --- | --- |
| **No.** | **DAG Name** | **Schedule** | **Tasks** |
| **1** | staging\_voyage | weekly | extract\_voyages\_from\_api  load\_staging\_voyages\_for\_all\_ports  load\_staging\_voyages\_by\_port |
| **2** | ods\_voyage | weekly | load\_ods\_port\_voyages  load\_ods\_voyage\_stops |
| **3** | visit\_summary | weekly | load\_fact\_voyage  load\_fact\_voyage\_summary\_quarterly |

## Service Vessel

### Staging Service Vessel (stg\_service\_vessel)

| **No.** | **Field Name** | **Alias** | **Field Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Service vessel event identification |
| 2 | service\_vessel | Service Vessel | jsonb | Service vessel information (tug, pilot, bunker) |
| 3 | related\_vessel | Related Vessel | jsonb | Related cargo vessel information |
| 4 | related\_vessel\_visit\_id | Related Vessel Visit ID | String | Related vessel's visit identifier |
| 5 | start\_time | Start Time | timestamp | Service start timestamp |
| 6 | end\_time | End Time | timestamp | Service end timestamp |
| 7 | start\_location | Start Location | jsonb | Service start location |
| 8 | end\_location | End Location | jsonb | Service end location |
| 9 | activity\_type | Activity Type | String | Type of service activity |
| 10 | ptt\_stage | PTT Stage | String | Port-to-Terminal stage |
| 11 | visit\_id | Visit ID | String | Visit identifier |
| 12 | additional\_data | Additional Data | jsonb | Additional service data |
| 13 | created\_timestamp | Created Timestamp | timestamp with time zone | Record creation timestamp |
| 14 | updated\_timestamp | Updated Timestamp | timestamp with time zone | Record update timestamp |

## Area Occupancy

### Staging Area Occupancy (stg\_area\_occupancy)

| **No.** | **Field name** | **Alias** | **Field Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Area occupancy identification |
| 2 | area | Area | String | Area identifier |
| 3 | ships | Ships | jsonb | Array of ships in the area |
| 4 | type | Type | String | Area type |
| 5 | timestamp | Timestamp | timestamp | Occupancy snapshot timestamp |
| 6 | created\_timestamp | Created Timestamp | timestamp with time zone | Record creation timestamp |
| 7 | updated\_timestamp | Updated Timestamp | timestamp with time zone | Record update timestamp |

## DATE AND TIME DIMENSION

### dim\_date

Date dimension table for data mart

| No. | Field Name | Alias | Data Type | Descriptions |
| --- | --- | --- | --- | --- |
| 1 | iso\_date | ISO Date | Date | ISO date |
| 2 | day | Day | SmallInt | Day of month |
| 3 | month | Month | SmallInt | Month number |
| 4 | month\_short\_name | Month Short Name | String | Month short name (e.g., Jan, Feb) |
| 5 | month\_full\_name | Month Full Name | String | Month full name (e.g., January, February) |
| 6 | week\_of\_year | Week Of Year | SmallInt | Week of year |
| 7 | year | Year | SmallInt | Year |

### dim\_time

Time dimension table for data mart

| No. | Field Name | Alias | Data Type | Descriptions |
| --- | --- | --- | --- | --- |
| 1 | iso\_time | ISO Time | Time | ISO time |
| 2 | hour | Hour | SmallInt | Hour |
| 3 | minute | Minute | SmallInt | Minute |
| 4 | second | Second | String | Second |

## FACT

### fact\_anchor

**Purpose**: Anchor event fact table **Database**: NEW-ETL-MART

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Unique identifier (Primary Key) |
| 2 | visit\_id | Visit ID | String | Visit identifier |
| 3 | port\_visit\_id | Port Visit ID | String | Port visit identifier |
| 4 | unlocode | UNLOCODE | String | United Nations Code for Trade and Transport Locations |
| 5 | ship\_id | Ship ID | String | Ship identifier |
| 6 | area\_id | Area ID | String | Area identifier |
| 7 | area\_name | Area Name | String | Area name |
| 8 | area\_type | Area Type | String | Area type |
| 9 | start\_location\_lat | Start Location Lat | Double | Start location latitude |
| 10 | start\_location\_lon | Start Location Lon | Double | Start location longitude |
| 11 | start\_date\_iso\_date | Start Date ISO Date | Date | Start date (ISO format) |
| 12 | start\_time\_iso\_time | Start Time ISO Time | Time | Start time (ISO format) |
| 13 | start\_timestamp | Start Timestamp | Timestamp | Start timestamp |
| 14 | end\_location\_lat | End Location Lat | Double | End location latitude |
| 15 | end\_location\_lon | End Location Lon | Double | End location longitude |
| 16 | end\_date\_iso\_date | End Date ISO Date | Date | End date (ISO format) |
| 17 | end\_time\_iso\_time | End Time ISO Time | Time | End time (ISO format) |
| 18 | end\_timestamp | End Timestamp | Timestamp | End timestamp |
| 19 | duration | Duration | Double | Duration in hours |
| 20 | vessel\_type | Vessel Type | String | Vessel type |

### fact\_berth\_visit

**Purpose**: Berth visit fact table to see the berth visit of a vessel **Database**: NEW-ETL-MART

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | port\_visit\_id | Port Visit ID | String | Port visit identifier |
| 2 | visit\_id | Visit ID | String | Visit identifier |
| 3 | port\_unlocode | Port UNLOCODE | String | Port UNLOCODE |
| 4 | ship\_id | Ship ID | String | Ship identifier |
| 5 | terminal\_visit\_id | Terminal Visit ID | String | Terminal visit identifier |
| 6 | terminal\_group\_id | Terminal Group ID | String | Terminal Group identifier |
| 7 | berth\_id | Berth ID | String | Berth identifier |
| 8 | berth\_visit\_id | Berth Visit ID | String | Berth visit identifier |
| 9 | berth\_visit\_position | Berth Visit Position | SmallInt | Berth Visit Position |
| 10 | start\_date\_iso\_date | Start Date ISO Date | Date | Start date (ISO format) |
| 11 | start\_time\_iso\_time | Start Time ISO Time | Time | Start time (ISO format) |
| 12 | start\_timestamp | Start Timestamp | Timestamp | Start timestamp |
| 13 | end\_date\_iso\_date | End Date ISO Date | Date | End date (ISO format) |
| 14 | end\_time\_iso\_time | End Time ISO Time | Time | End time (ISO format) |
| 15 | end\_timestamp | End Timestamp | Timestamp | End timestamp |
| 16 | unique\_tugs\_arrival\_count | Unique Tugs Arrival Count | SmallInt | Unique Tugs Arrival count |
| 17 | unique\_tugs\_departure\_count | Unique Tugs Departure Count | SmallInt | Unique Tugs Departure count |
| 18 | all\_fast\_date\_iso\_date | All Fast Date ISO Date | Date | All Fast date (ISO format) |
| 19 | all\_fast\_time\_iso\_time | All Fast Time ISO Time | Time | All Fast time (ISO format) |
| 20 | all\_fast\_timestamp | All Fast Timestamp | Timestamp | All Fast timestamp |
| 21 | first\_tug\_arrived\_departure\_date\_iso\_date | First Tug Arrived Departure Date ISO Date | Date | First Tug Arrived Departure date (ISO format) |
| 22 | first\_tug\_arrived\_departure\_time\_iso\_time | First Tug Arrived Departure Time ISO Time | Time | First Tug Arrived Departure time (ISO format) |
| 23 | first\_tug\_arrived\_departure\_timestamp | First Tug Arrived Departure Timestamp | Timestamp | First Tug Arrived Departure timestamp |
| 24 | last\_tug\_arrived\_departure\_date\_iso\_date | Last Tug Arrived Departure Date ISO Date | Date | Last Tug Arrived Departure date (ISO format) |
| 25 | last\_tug\_arrived\_departure\_time\_iso\_time | Last Tug Arrived Departure Time ISO Time | Time | Last Tug Arrived Departure time (ISO format) |
| 26 | last\_tug\_arrived\_departure\_timestamp | Last Tug Arrived Departure Timestamp | Timestamp | Last Tug Arrived Departure timestamp |
| 27 | is\_cargo\_operation | Is Cargo Operation | Boolean | Indicates if this is a cargo operation |
| 28 | start\_mooring\_date\_iso\_date | Start Mooring Date ISO Date | Date | Start Mooring date (ISO format) |
| 29 | start\_mooring\_time\_iso\_time | Start Mooring Time ISO Time | Time | Start Mooring time (ISO format) |
| 30 | start\_mooring\_timestamp | Start Mooring Timestamp | Timestamp | Start Mooring timestamp |
| 31 | end\_unmooring\_date\_iso\_date | End Unmooring Date ISO Date | Date | End Unmooring date (ISO format) |
| 32 | end\_unmooring\_time\_iso\_time | End Unmooring Time ISO Time | Time | End Unmooring time (ISO format) |
| 33 | end\_unmooring\_timestamp | End Unmooring Timestamp | Timestamp | End Unmooring timestamp |
| 34 | mooring\_duration | Mooring Duration | Double | Mooring duration in hours |
| 35 | unmooring\_duration | Unmooring Duration | Double | Unmooring duration in hours |
| 36 | moored\_duration | Moored Duration | Double | Moored duration in hours |
| 37 | arrival\_first\_bunker\_timestamp | Arrival First Bunker Timestamp | Timestamp | Arrival First Bunker timestamp |
| 38 | departure\_last\_bunker\_timestamp | Departure Last Bunker Timestamp | Timestamp | Departure Last Bunker timestamp |
| 39 | bunkers\_count | Bunkers Count | SmallInt | Number of bunker operations |
| 40 | visit\_vessel\_type | Visit Vessel Type | String | Visit vessel type |

### fact\_bunkering

**Purpose**: Bunkering service fact table **Database**: NEW-ETL-MART

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Unique identifier (Primary Key) |
| 2 | visit\_id | Visit ID | String | Visit identifier |
| 3 | port\_visit\_id | Port Visit ID | String | Port visit identifier |
| 4 | port\_unlocode | Port UNLOCODE | String | Port UNLOCODE |
| 5 | terminal\_visit\_id | Terminal Visit ID | String | Terminal visit identifier |
| 6 | berth\_visit\_id | Berth Visit ID | String | Berth visit identifier |
| 7 | cargo\_ship\_id | Cargo Ship ID | String | Cargo Ship identifier |
| 8 | service\_ship\_id | Service Ship ID | String | Service Ship identifier |
| 9 | service\_ship\_imo | Service Ship IMO | String | Service Ship Imo |
| 10 | service\_ship\_mmsi | Service Ship MMSI | String | Service Ship Mmsi |
| 11 | start\_date\_iso\_date | Start Date ISO Date | Date | Start date (ISO format) |
| 12 | start\_time\_iso\_time | Start Time ISO Time | Time | Start time (ISO format) |
| 13 | start\_timestamp | Start Timestamp | Timestamp | Start timestamp |
| 14 | end\_date\_iso\_date | End Date ISO Date | Date | End date (ISO format) |
| 15 | end\_time\_iso\_time | End Time ISO Time | Time | End time (ISO format) |
| 16 | end\_timestamp | End Timestamp | Timestamp | End timestamp |
| 17 | duration | Duration | Double | Duration in hours |
| 18 | vessel\_type | Vessel Type | String | Vessel type |

### fact\_pilot

**Purpose**: Pilot service fact table **Database**: NEW-ETL-MART

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Unique identifier (Primary Key) |
| 2 | visit\_id | Visit ID | String | Visit identifier |
| 3 | port\_visit\_id | Port Visit ID | String | Port visit identifier |
| 4 | port\_unlocode | Port UNLOCODE | String | Port UNLOCODE |
| 5 | type | Type | String | Type |
| 6 | date\_iso\_date | Date ISO Date | Date | Date Iso Date |
| 7 | time\_iso\_time | Time ISO Time | Time | Time Iso Time |
| 8 | timestamp | Timestamp | Timestamp | Timestamp |
| 9 | fallback\_type | Fallback Type | String | Fallback Type |
| 10 | vessel\_ship\_id | Vessel Ship ID | String | Vessel Ship identifier |
| 11 | service\_ship\_id | Service Ship ID | String | Service Ship identifier |
| 12 | service\_ship\_imo | Service Ship IMO | String | Service Ship Imo |
| 13 | service\_ship\_mmsi | Service Ship MMSI | String | Service Ship Mmsi |
| 14 | selected\_pilot | Selected Pilot | Boolean | Indicates if this is the selected pilot |
| 15 | vessel\_type | Vessel Type | String | Vessel type |

### fact\_port\_calls

**Purpose**: Port calls aggregation fact table **Database**: NEW-ETL-MART

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | UUID | Unique identifier (Primary Key) |
| 2 | port\_unlocode | Port UNLOCODE | String | Port UNLOCODE |
| 3 | completion\_date\_iso\_date | Completion Date ISO Date | Date | Completion date (ISO format) |
| 4 | total\_port\_calls | Total Port Calls | Integer | Total number of port calls |
| 5 | ship\_classification\_dry\_bulk | Ship Classification Dry Bulk | String | Ship Classification Dry Bulk |
| 6 | ship\_classification\_wet\_bulk | Ship Classification Wet Bulk | String | Ship Classification Wet Bulk |
| 7 | ship\_classification\_teu | Ship Classification TEU | String | Ship Classification Teu |
| 8 | ship\_category\_dry\_bulk | Ship Category Dry Bulk | String | Ship Category Dry Bulk |
| 9 | ship\_category\_dry\_bulk\_total\_port\_calls | Ship Category Dry Bulk Total Port Calls | Integer | Ship Category Dry Bulk Total Port Calls |
| 10 | ship\_category\_wet\_bulk | Ship Category Wet Bulk | String | Ship Category Wet Bulk |
| 11 | ship\_category\_wet\_bulk\_total\_port\_calls | Ship Category Wet Bulk Total Port Calls | Integer | Ship Category Wet Bulk Total Port Calls |
| 12 | ship\_category\_teu | Ship Category TEU | String | Ship Category Teu |
| 13 | ship\_category\_teu\_total\_port\_calls | Ship Category TEU Total Port Calls | Integer | Ship Category Teu Total Port Calls |
| 14 | ship\_category\_unknown\_total\_port\_calls | Ship Category Unknown Total Port Calls | Integer | Ship Category Unknown Total Port Calls |
| 15 | created\_timestamp | Created Timestamp | Timestamp (TZ) | Record creation timestamp |
| 16 | created\_by | Created By | String | User who created the record |

### fact\_port\_calls\_terminal

**Purpose**: Terminal port calls aggregation fact table **Database**: NEW-ETL-MART

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | UUID | Unique identifier (Primary Key) |
| 2 | terminal\_id | Terminal ID | String | Terminal identifier |
| 3 | total\_port\_calls | Total Port Calls | Integer | Total number of port calls |
| 4 | completion\_date\_iso\_date | Completion Date ISO Date | Date | Completion date (ISO format) |
| 5 | created\_timestamp | Created Timestamp | Timestamp (TZ) | Record creation timestamp |
| 6 | created\_by | Created By | String | User who created the record |

### fact\_port\_performance\_analytics

**Purpose**: Port performance analytics fact table **Database**: NEW-ETL-MART

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | UUID | Unique identifier (Primary Key) |
| 2 | port\_unlocode | Port UNLOCODE | String | Port UNLOCODE |
| 3 | metric\_type | Metric Type | String | Metric Type |
| 4 | average\_value | Average Value | Double | Average Value |
| 5 | standard\_deviation | Standard Deviation | Double | Standard Deviation |
| 6 | data\_period\_start | Data Period Start | Date | Data Period Start |
| 7 | data\_period\_end | Data Period End | Date | Data Period End |
| 8 | created\_timestamp | Created Timestamp | Timestamp (TZ) | Record creation timestamp |
| 9 | created\_by | Created By | String | User who created the record |

### fact\_port\_visit

**Purpose**: Port visit fact table with comprehensive metrics **Database**: NEW-ETL-MART

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Unique identifier (Primary Key) |
| 2 | visit\_id | Visit ID | String | Visit identifier |
| 3 | port\_visit\_id | Port Visit ID | String | Port visit identifier |
| 4 | port\_unlocode | Port UNLOCODE | String | Port UNLOCODE |
| 5 | prev\_port\_unlocode | Prev Port UNLOCODE | String | Previous port UNLOCODE |
| 6 | ship\_id | Ship ID | String | Ship identifier |
| 7 | start\_date\_iso\_date | Start Date ISO Date | Date | Start date (ISO format) |
| 8 | start\_time\_iso\_time | Start Time ISO Time | Time | Start time (ISO format) |
| 9 | start\_timestamp | Start Timestamp | Timestamp | Start timestamp |
| 10 | end\_date\_iso\_date | End Date ISO Date | Date | End date (ISO format) |
| 11 | end\_time\_iso\_time | End Time ISO Time | Time | End time (ISO format) |
| 12 | end\_timestamp | End Timestamp | Timestamp | End timestamp |
| 13 | eos\_entry\_date\_iso\_date | EOS Entry Date ISO Date | Date | Eos Entry date (ISO format) |
| 14 | eos\_entry\_time\_iso\_time | EOS Entry Time ISO Time | Time | Eos Entry time (ISO format) |
| 15 | eos\_entry\_timestamp | EOS Entry Timestamp | Timestamp | Eos Entry timestamp |
| 16 | eos\_exit\_date\_iso\_date | EOS Exit Date ISO Date | Date | Eos Exit date (ISO format) |
| 17 | eos\_exit\_time\_iso\_time | EOS Exit Time ISO Time | Time | Eos Exit time (ISO format) |
| 18 | eos\_exit\_timestamp | EOS Exit Timestamp | Timestamp | Eos Exit timestamp |
| 19 | total\_cargo\_operation | Total Cargo Operation | SmallInt | Total number of cargo operations |
| 20 | total\_cargo\_operation\_duration | Total Cargo Operation Duration | Double | Total Cargo Operation duration in hours |
| 21 | total\_non\_cargo\_operation | Total Non Cargo Operation | SmallInt | Total number of non-cargo operations |
| 22 | total\_non\_cargo\_operation\_duration | Total Non Cargo Operation Duration | Double | Total Non Cargo Operation duration in hours |
| 23 | total\_moored\_duration | Total Moored Duration | Double | Total Moored duration in hours |
| 24 | total\_mooring\_duration | Total Mooring Duration | Double | Total Mooring duration in hours |
| 25 | total\_unmooring\_duration | Total Unmooring Duration | Double | Total Unmooring duration in hours |
| 26 | total\_berth\_visit | Total Berth Visit | SmallInt | Total number of berth visits |
| 27 | total\_terminal\_visit | Total Terminal Visit | SmallInt | Total number of terminal visits |
| 28 | drifting\_duration | Drifting Duration | Double | Drifting duration in hours |
| 29 | turn\_around\_time\_duration | Turn Around Time Duration | Double | Turn around time duration in hours |
| 30 | anchor\_down\_date\_iso\_date | Anchor Down Date ISO Date | Date | Anchor Down date (ISO format) |
| 31 | anchor\_down\_time\_iso\_time | Anchor Down Time ISO Time | Time | Anchor Down time (ISO format) |
| 32 | anchor\_down\_timestamp | Anchor Down Timestamp | Timestamp | Anchor Down timestamp |
| 33 | anchor\_up\_date\_iso\_date | Anchor Up Date ISO Date | Date | Anchor Up date (ISO format) |
| 34 | anchor\_up\_time\_iso\_time | Anchor Up Time ISO Time | Time | Anchor Up time (ISO format) |
| 35 | anchor\_up\_timestamp | Anchor Up Timestamp | Timestamp | Anchor Up timestamp |
| 36 | anchor\_duration | Anchor Duration | Double | Anchor duration in hours |
| 37 | pilot\_onboard\_inbound\_date\_iso\_date | Pilot Onboard Inbound Date ISO Date | Date | Pilot Onboard Inbound date (ISO format) |
| 38 | pilot\_onboard\_inbound\_time\_iso\_time | Pilot Onboard Inbound Time ISO Time | Time | Pilot Onboard Inbound time (ISO format) |
| 39 | pilot\_onboard\_inbound\_timestamp | Pilot Onboard Inbound Timestamp | Timestamp | Pilot Onboard Inbound timestamp |
| 40 | pilot\_onboard\_inbound\_type | Pilot Onboard Inbound Type | String | Pilot Onboard Inbound Type |
| 41 | pilot\_disembarked\_outbound\_date\_iso\_date | Pilot Disembarked Outbound Date ISO Date | Date | Pilot Disembarked Outbound date (ISO format) |
| 42 | pilot\_disembarked\_outbound\_time\_iso\_time | Pilot Disembarked Outbound Time ISO Time | Time | Pilot Disembarked Outbound time (ISO format) |
| 43 | pilot\_disembarked\_outbound\_timestamp | Pilot Disembarked Outbound Timestamp | Timestamp | Pilot Disembarked Outbound timestamp |
| 44 | pilot\_disembarked\_outbound\_type | Pilot Disembarked Outbound Type | String | Pilot Disembarked Outbound Type |
| 45 | port\_inbound\_travel\_duration | Port Inbound Travel Duration | Double | Port Inbound Travel duration in hours |
| 46 | port\_outbound\_travel\_duration | Port Outbound Travel Duration | Double | Port Outbound Travel duration in hours |
| 47 | shifting\_between\_terminals\_duration | Shifting Between Terminals Duration | Double | Shifting Between Terminals duration in hours |
| 48 | shifting\_inside\_terminals\_duration | Shifting Inside Terminals Duration | Double | Shifting Inside Terminals duration in hours |
| 49 | total\_ship\_to\_ship\_transfers | Total Ship To Ship Transfers | SmallInt | Total Ship To Ship Transfers |
| 50 | total\_ship\_to\_ship\_transfers\_duration | Total Ship To Ship Transfers Duration | Double | Total Ship To Ship Transfers duration in hours |
| 51 | total\_slowmoving\_duration\_arrival | Total Slowmoving Duration Arrival | Double | Total Slowmoving Duration Arrival |
| 52 | total\_slowmoving\_duration\_inport | Total Slowmoving Duration Inport | Double | Total Slowmoving Duration Inport |
| 53 | total\_slowmoving\_duration\_departure | Total Slowmoving Duration Departure | Double | Total Slowmoving Duration Departure |
| 54 | before\_visit\_anchor\_duration | Before Visit Anchor Duration | Double | Before Visit Anchor duration in hours |
| 55 | during\_visit\_anchor\_duration | During Visit Anchor Duration | Double | During Visit Anchor duration in hours |
| 56 | after\_visit\_anchor\_duration | After Visit Anchor Duration | Double | After Visit Anchor duration in hours |
| 57 | sailing\_in\_duration | Sailing In Duration | Double | Sailing in duration in hours |
| 58 | sailing\_out\_duration | Sailing Out Duration | Double | Sailing out duration in hours |
| 59 | is\_moored\_within\_range | Is Moored Within Range | Boolean | Outlier flag: TRUE if total\_moored\_duration is within 5 standard deviations of port average, FALSE if outlier, NULL if no analytics data |
| 60 | is\_shifting\_within\_range | Is Shifting Within Range | Boolean | Outlier flag: TRUE if total shifting duration is within 5 standard deviations of port average, FALSE if outlier, NULL if no analytics data |
| 61 | is\_steaming\_in\_within\_range | Is Steaming In Within Range | Boolean | Outlier flag: TRUE if port\_inbound\_travel\_duration is within 5 standard deviations of port average, FALSE if outlier, NULL if no analytics data |
| 62 | is\_steaming\_out\_within\_range | Is Steaming Out Within Range | Boolean | Outlier flag: TRUE if port\_outbound\_travel\_duration is within 5 standard deviations of port average, FALSE if outlier, NULL if no analytics data |
| 63 | is\_wait\_during\_visit\_within\_range | Is Wait During Visit Within Range | Boolean | Outlier flag: TRUE if wait during visit duration is within 5 standard deviations of port average, FALSE if outlier, NULL if no analytics data |
| 64 | is\_wait\_before\_arrival\_within\_range | Is Wait Before Arrival Within Range | Boolean | Outlier flag: TRUE if wait before arrival duration is within 5 standard deviations of port average, FALSE if outlier, NULL if no analytics data |
| 65 | outlier\_preference | Outlier Preference | String | Outlier Preference |
| 66 | total\_waiting\_time\_before\_arrival\_duration | Total Waiting Time Before Arrival Duration | Double | Total Waiting Time Before Arrival duration in hours |
| 67 | total\_waiting\_time\_during\_visit\_duration | Total Waiting Time During Visit Duration | Double | Total Waiting Time During Visit duration in hours |
| 68 | waiting\_duration | Waiting Duration | Double | Waiting duration in hours |
| 69 | shifting\_duration | Shifting Duration | Double | Shifting duration in hours |
| 71 | between\_pdk\_and\_eos\_exit\_duration | Between Pdk And EOS Exit Duration | Double | Between Pdk And Eos Exit duration in hours |
| 72 | between\_eos\_entry\_and\_pob\_duration | Between EOS Entry And Pob Duration | Double | Between Eos Entry And Pob duration in hours |
| 73 | visit\_vessel\_type | Visit Vessel Type | String | Visit vessel type |

### fact\_service\_vessel

**Purpose**: Service vessel fact table **Database**: NEW-ETL-MART

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Unique identifier (Primary Key) |
| 2 | service\_vessel\_id | Service Vessel ID | String | Service vessel identifier |
| 3 | service\_vessel\_role | Service Vessel Role | String | Service Vessel Role |
| 4 | related\_vessel\_id | Related Vessel ID | String | Related Vessel identifier |
| 5 | related\_vessel\_role | Related Vessel Role | String | Related Vessel Role |
| 6 | related\_vessel\_visit\_id | Related Vessel Visit ID | String | Related Vessel Visit identifier |
| 7 | start\_date | Start Date | Date | Start Date |
| 8 | start\_time | Start Time | Time | Start Time |
| 9 | start\_timestamp | Start Timestamp | Timestamp | Start timestamp |
| 10 | start\_location\_lat | Start Location Lat | Double | Start location latitude |
| 11 | start\_location\_lon | Start Location Lon | Double | Start location longitude |
| 12 | end\_date | End Date | Date | End Date |
| 13 | end\_time | End Time | Time | End Time |
| 14 | end\_timestamp | End Timestamp | Timestamp | End timestamp |
| 15 | end\_location\_lat | End Location Lat | Double | End location latitude |
| 16 | end\_location\_lon | End Location Lon | Double | End location longitude |
| 17 | duration | Duration | Double | Duration in hours |
| 18 | activity\_type | Activity Type | String | Activity Type |
| 19 | ptt\_stage | Ptt Stage | String | Ptt Stage |
| 20 | visit\_id | Visit ID | String | Visit identifier |
| 21 | created\_timestamp | Created Timestamp | Timestamp (TZ) | Record creation timestamp |
| 22 | updated\_timestamp | Updated Timestamp | Timestamp (TZ) | Record update timestamp |

### fact\_ship\_to\_ship\_transfers

**Purpose**: Ship-to-ship transfer fact table **Database**: NEW-ETL-MART

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Unique identifier (Primary Key) |
| 2 | visit\_id | Visit ID | String | Visit identifier |
| 3 | port\_visit\_id | Port Visit ID | String | Port visit identifier |
| 4 | unlocode | UNLOCODE | String | United Nations Code for Trade and Transport Locations |
| 5 | view | View | String | View type |
| 6 | ship\_imo | Ship IMO | String | Ship Imo |
| 7 | ship\_type | Ship Type | String | Ship type |
| 8 | ship\_name | Ship Name | String | Ship name |
| 9 | area\_name | Area Name | String | Area name |
| 10 | area\_type | Area Type | String | Area type |
| 11 | area\_id | Area ID | String | Area identifier |
| 12 | start\_location\_lat | Start Location Lat | Double | Start location latitude |
| 13 | start\_location\_lon | Start Location Lon | Double | Start location longitude |
| 14 | start\_date\_iso\_date | Start Date ISO Date | Date | Start date (ISO format) |
| 15 | start\_time\_iso\_time | Start Time ISO Time | Time | Start time (ISO format) |
| 16 | start\_timestamp | Start Timestamp | Timestamp | Start timestamp |
| 17 | start\_fallback | Start Fallback | String | Start Fallback |
| 18 | end\_location\_lat | End Location Lat | Double | End location latitude |
| 19 | end\_location\_lon | End Location Lon | Double | End location longitude |
| 20 | end\_date\_iso\_date | End Date ISO Date | Date | End date (ISO format) |
| 21 | end\_time\_iso\_time | End Time ISO Time | Time | End time (ISO format) |
| 22 | end\_timestamp | End Timestamp | Timestamp | End timestamp |
| 23 | end\_fallback | End Fallback | String | End Fallback |
| 24 | duration | Duration | Double | Duration in hours |
| 25 | from\_ship\_id | From Ship ID | String | From Ship identifier |
| 26 | to\_ship\_id | To Ship ID | String | To Ship identifier |
| 27 | vessel\_type | Vessel Type | String | Vessel type |

### fact\_stdev\_time\_terminal\_visit

**Purpose**: Terminal visit standard deviation fact table (daily) **Database**: NEW-ETL-MART

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | UUID | Unique identifier (Primary Key) |
| 2 | visit\_id | Visit ID | String | Visit identifier |
| 3 | port\_unlocode | Port UNLOCODE | String | Port UNLOCODE |
| 4 | terminal\_id | Terminal ID | String | Terminal identifier |
| 5 | stdev\_turn\_around\_time\_duration | Stdev Turn Around Time Duration | Double | Stdev Turn Around Time duration in hours |
| 6 | iso\_date | ISO Date | Date | ISO date |
| 7 | created\_timestamp | Created Timestamp | Timestamp (TZ) | Record creation timestamp |
| 8 | created\_by | Created By | String | User who created the record |

### fact\_stdev\_time\_terminal\_visit\_monthly

**Purpose**: Terminal visit standard deviation fact table (monthly) **Database**: NEW-ETL-MART

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | UUID | Unique identifier (Primary Key) |
| 2 | visit\_id | Visit ID | String | Visit identifier |
| 3 | port\_unlocode | Port UNLOCODE | String | Port UNLOCODE |
| 4 | terminal\_id | Terminal ID | String | Terminal identifier |
| 5 | stdev\_turn\_around\_time\_duration | Stdev Turn Around Time Duration | Double | Stdev Turn Around Time duration in hours |
| 6 | month\_year | Month Year | String | Month and year |
| 7 | created\_timestamp | Created Timestamp | Timestamp (TZ) | Record creation timestamp |
| 8 | created\_by | Created By | String | User who created the record |

### fact\_terminal\_visit

**Purpose**: Terminal visit fact table **Database**: NEW-ETL-MART

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | port\_visit\_id | Port Visit ID | String | Port visit identifier |
| 2 | visit\_id | Visit ID | String | Visit identifier |
| 3 | port\_unlocode | Port UNLOCODE | String | Port UNLOCODE |
| 4 | ship\_id | Ship ID | String | Ship identifier |
| 5 | terminal\_visit\_id | Terminal Visit ID | String | Terminal visit identifier |
| 6 | terminal\_id | Terminal ID | String | Terminal identifier |
| 7 | terminal\_visit\_position | Terminal Visit Position | SmallInt | Terminal Visit Position |
| 8 | start\_date\_iso\_date | Start Date ISO Date | Date | Start date (ISO format) |
| 9 | start\_time\_iso\_time | Start Time ISO Time | Time | Start time (ISO format) |
| 10 | start\_timestamp | Start Timestamp | Timestamp | Start timestamp |
| 11 | end\_date\_iso\_date | End Date ISO Date | Date | End date (ISO format) |
| 12 | end\_time\_iso\_time | End Time ISO Time | Time | End time (ISO format) |
| 13 | end\_timestamp | End Timestamp | Timestamp | End timestamp |
| 14 | turn\_around\_time\_duration | Turn Around Time Duration | Double | Turn around time duration in hours |
| 15 | terminal\_cargo\_operation\_duration | Terminal Cargo Operation Duration | Double | Terminal Cargo Operation duration in hours |
| 16 | terminal\_non\_cargo\_operation\_duration | Terminal Non Cargo Operation Duration | Double | Terminal Non Cargo Operation duration in hours |
| 17 | terminal\_moored\_duration | Terminal Moored Duration | Double | Terminal Moored duration in hours |
| 18 | terminal\_anchor\_duration | Terminal Anchor Duration | Double | Terminal Anchor duration in hours |
| 19 | terminal\_total\_cargo\_operation | Terminal Total Cargo Operation | SmallInt | Terminal Total Cargo Operation |
| 20 | terminal\_total\_non\_cargo\_operation | Terminal Total Non Cargo Operation | SmallInt | Terminal Total Non Cargo Operation |
| 21 | terminal\_total\_berth\_visit | Terminal Total Berth Visit | SmallInt | Terminal Total Berth Visit |
| 22 | waiting\_outside\_terminal\_duration | Waiting Outside Terminal Duration | Double | Waiting Outside Terminal duration in hours |
| 23 | waiting\_during\_terminal\_visit\_duration | Waiting During Terminal Visit Duration | Double | Waiting During Terminal Visit duration in hours |
| 24 | steaming\_in\_duration | Steaming In Duration | Double | Steaming In duration in hours |
| 25 | steaming\_out\_duration | Steaming Out Duration | Double | Steaming Out duration in hours |
| 26 | anchorage\_during\_terminal\_visit\_duration | Anchorage During Terminal Visit Duration | Double | Anchorage During Terminal Visit duration in hours |
| 27 | slowmoving\_during\_terminal\_visit\_duration | Slowmoving During Terminal Visit Duration | Double | Slowmoving During Terminal Visit duration in hours |
| 28 | shifting\_within\_terminal\_visit\_duration | Shifting Within Terminal Visit Duration | Double | Shifting Within Terminal Visit duration in hours |
| 29 | visit\_vessel\_type | Visit Vessel Type | String | Visit vessel type |

### fact\_tug

**Purpose**: Tug service fact table **Database**: NEW-ETL-MART

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | String | Unique identifier (Primary Key) |
| 2 | visit\_id | Visit ID | String | Visit identifier |
| 3 | port\_visit\_id | Port Visit ID | String | Port visit identifier |
| 4 | port\_unlocode | Port UNLOCODE | String | Port UNLOCODE |
| 5 | terminal\_visit\_id | Terminal Visit ID | String | Terminal visit identifier |
| 6 | berth\_visit\_id | Berth Visit ID | String | Berth visit identifier |
| 7 | cargo\_ship\_id | Cargo Ship ID | String | Cargo Ship identifier |
| 8 | service\_ship\_id | Service Ship ID | String | Service Ship identifier |
| 9 | service\_ship\_imo | Service Ship IMO | String | Service Ship Imo |
| 10 | service\_ship\_mmsi | Service Ship MMSI | String | Service Ship Mmsi |
| 11 | start\_date\_iso\_date | Start Date ISO Date | Date | Start date (ISO format) |
| 12 | start\_time\_iso\_time | Start Time ISO Time | Time | Start time (ISO format) |
| 13 | start\_timestamp | Start Timestamp | Timestamp | Start timestamp |
| 14 | end\_date\_iso\_date | End Date ISO Date | Date | End date (ISO format) |
| 15 | end\_time\_iso\_time | End Time ISO Time | Time | End time (ISO format) |
| 16 | end\_timestamp | End Timestamp | Timestamp | End timestamp |
| 17 | duration | Duration | Double | Duration in hours |
| 18 | tugging\_state | Tugging State | String | Tugging State |
| 19 | cargo\_visit\_tugging\_state | Cargo Visit Tugging State | String | Cargo Visit Tugging State |
| 20 | vessel\_type | Vessel Type | String | Vessel type |

### fact\_voyage

**Purpose**: Voyage fact table **Database**: NEW-ETL-MART

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | UUID | Unique identifier (Primary Key) |
| 2 | entry\_id | Entry ID | String | Entry identifier |
| 3 | imo | IMO | String | IMO number |
| 4 | start\_location\_lat | Start Location Lat | Double | Start location latitude |
| 5 | start\_location\_lon | Start Location Lon | Double | Start location longitude |
| 6 | start\_date | Start Date | Date | Start Date |
| 7 | start\_time | Start Time | Time | Start Time |
| 8 | start\_timestamp | Start Timestamp | Timestamp | Start timestamp |
| 9 | end\_location\_lat | End Location Lat | Double | End location latitude |
| 10 | end\_location\_lon | End Location Lon | Double | End location longitude |
| 11 | end\_date | End Date | Date | End Date |
| 12 | end\_time | End Time | Time | End Time |
| 13 | end\_timestamp | End Timestamp | Timestamp | End timestamp |
| 14 | previous\_port | Previous Port | String | Previous Port |
| 15 | previous\_entry\_id | Previous Entry ID | String | Previous Entry identifier |
| 16 | next\_port | Next Port | String | Next Port |
| 17 | next\_entry\_id | Next Entry ID | String | Next Entry identifier |
| 18 | gross\_tonnage | Gross Tonnage | Integer | Gross tonnage |
| 19 | dwt | DWT | Integer | Deadweight tonnage |
| 20 | teu | TEU | Integer | Twenty-foot Equivalent Unit capacity |
| 21 | ship\_category | Ship Category | String | Ship category |
| 22 | created\_timestamp | Created Timestamp | Timestamp (TZ) | Record creation timestamp |
| 23 | created\_by | Created By | String | User who created the record |

### fact\_voyage\_summary\_quarterly

**Purpose**: Voyage summary aggregation fact table (quarterly) **Database**: NEW-ETL-MART

| **No.** | **Field Name** | **Alias** | **Data Type** | **Descriptions** |
| --- | --- | --- | --- | --- |
| 1 | id | ID | UUID | Unique identifier (Primary Key) |
| 2 | voyages\_count | Voyages Count | Integer | Number of voyages |
| 3 | previous\_port | Previous Port | String | Previous Port |
| 4 | next\_port | Next Port | String | Next Port |
| 5 | quarter | Quarter | Integer | Quarter |
| 6 | year | Year | Integer | Year |
| 7 | ship\_category | Ship Category | String | Ship category |
| 8 | created\_timestamp | Created Timestamp | Timestamp (TZ) | Record creation timestamp |
| 9 | created\_by | Created By | String | User who created the record |

## Quality Control Layer

### qc\_accuracy\_report

**Purpose**: Quality control accuracy test results **Database**: NEW-ETL-DWH

| No. | Field Name | Alias | Data Type | Descriptions |
| --- | --- | --- | --- | --- |
| 1 | id | ID | UUID | Unique identifier (Primary Key) |
| 2 | category | Category | String | Category |
| 3 | table\_name | Table Name | String | Table name |
| 4 | title | Title | String | Title |
| 5 | score | Score | Double | Score |
| 6 | details | Details | JSON | Details |
| 7 | testing\_date | Testing Date | Date | Testing Date |
| 8 | start\_date | Start Date | Timestamp | Start Date |
| 9 | end\_date | End Date | Timestamp | End Date |
| 10 | created\_timestamp | Created Timestamp | Timestamp (TZ) | Record creation timestamp |
| 11 | created\_by | Created By | String | User who created the record |

### qc\_completeness\_report

**Purpose**: Quality control completeness test results **Database**: NEW-ETL-DWH

| No. | Field Name | Alias | Data Type | Descriptions |
| --- | --- | --- | --- | --- |
| 1 | id | ID | UUID | Unique identifier (Primary Key) |
| 2 | category | Category | String | Category |
| 3 | table\_name | Table Name | String | Table name |
| 4 | title | Title | String | Title |
| 5 | score | Score | Double | Score |
| 6 | details | Details | JSON | Details |
| 7 | testing\_date | Testing Date | Date | Testing Date |
| 8 | start\_date | Start Date | Timestamp | Start Date |
| 9 | end\_date | End Date | Timestamp | End Date |
| 10 | created\_timestamp | Created Timestamp | Timestamp (TZ) | Record creation timestamp |
| 11 | created\_by | Created By | String | User who created the record |

### qc\_validity\_report

**Purpose**: Quality control validity test results **Database**: NEW-ETL-DWH

| No. | Field Name | Alias | Data Type | Descriptions |
| --- | --- | --- | --- | --- |
| 1 | id | ID | UUID | Unique identifier (Primary Key) |
| 2 | category | Category | String | Category |
| 3 | table\_name | Table Name | String | Table name |
| 4 | title | Title | String | Title |
| 5 | score | Score | Double | Score |
| 6 | details | Details | JSON | Details |
| 7 | testing\_date | Testing Date | Date | Testing Date |
| 8 | start\_date | Start Date | Timestamp | Start Date |
| 9 | end\_date | End Date | Timestamp | End Date |
| 10 | created\_timestamp | Created Timestamp | Timestamp (TZ) | Record creation timestamp |
| 11 | created\_by | Created By | String | User who created the record |

# Code documentations

## Repository

|  |  |  |
| --- | --- | --- |
| **No.** | **Name** | **Descriptions** |
| **1** | dataflow\_ai | The AI repository to playing around with data warehouse and mart also other source of data. The feature include Natural Language Query (NLQ) and some analytics things. |
| **2** | dataflow\_dag | Airflow DAG repository to put all of the data pipeline logic and tasks here. This include the Batching and Streaming pipeline. |
| **3** | dataflow\_plugins | Airflow Plugins repository to put all of the plugins related to data pipeline here. |
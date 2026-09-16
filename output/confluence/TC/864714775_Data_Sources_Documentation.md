---
id: confluence:864714775
source: confluence
type: page
space: TC
title: Data Sources Documentation
author: Ryan Kharisma Rakhmat
date: '2026-02-03'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/864714775
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/864714775
---
# Data Sources Documentation

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/864714775  

## Content

## Overview

The data warehouse ingests data from **three primary external sources** and processes them through a multi-layered architecture:

1. **POMA (Port Operations Management API)** - Port infrastructure and configuration data
2. **CSI (Central Ship Information API)** - Ship registry and vessel information
3. **Vessel Voyage API** - Real-time vessel movement and port visit data

---

## Data Architecture Layers

The data flows through three main layers before reaching the analytical fact tables:

wide760External APIs → Staging Tables → ODS Tables → Fact/Dimension Tables

### **Layer 1: Staging Tables** (`stg_*`)

* **Purpose**: Raw data landing zone from external APIs
* **Retention**: Temporary storage, cleared after successful ODS load
* **Format**: JSON data flattened into relational tables

### **Layer 2: ODS Tables** (`ods_*`)

* **Purpose**: Operational Data Store - cleaned and normalized data
* **Retention**: Historical data with soft deletes (deleted\_timestamp)
* **Format**: Normalized relational tables with business keys

### **Layer 3: Fact/Dimension Tables** (`fact_*`, `dim_*`)

* **Purpose**: Analytics-ready data marts
* **Retention**: Permanent historical data
* **Format**: Star schema optimized for reporting and analysis

---

## Data Source 1: POMA (Port Operations Management API)

### **What is POMA?**

POMA is Teqplay's **Port Infrastructure Configuration API** that provides static and semi-static data about port facilities, terminals, berths, and geographical areas.

### **Data Ingestion Mode**

* **Batch Processing**: Scheduled periodic extractions (daily/weekly)
* **No Streaming**: Configuration data changes infrequently

### **API Extraction Strategy**

#### **Filtering at API Level**

| Filter Type | Applied? | Filter Logic | Example |
| --- | --- | --- | --- |
| **Country Code** | ✅ Yes | Optional parameter - if provided, only ports in that country are retrieved | `country_code=ID` returns only Indonesian ports |
| **Get All** | ✅ Yes | If no country code provided, retrieves ALL ports globally | No filter = All ports worldwide |

#### **Code Implementation**

pywide760# teqplay/repositories/port.py
if not country\_code:
return api.get\_ports(token=token) # ← GET ALL PORTS
return api.get\_ports(token=token, countryCode=country\_code) # ← FILTERED

### **Data Entities from POMA**

| Entity | Description | Filtering Strategy | Example Data |
| --- | --- | --- | --- |
| **Ports** | Port master data (name, UNLOCODE, country, coordinates) | Country code (optional) | Port of Singapore (SGSIN) |
| **Terminals** | Terminal facilities within ports | Port UNLOCODE (required) | PSA Pasir Panjang Terminal |
| **Berths** | Individual berth positions and specifications | Port UNLOCODE (required) | Berth 1A - Container Berth |
| **Anchorages** | Designated anchorage areas | Port UNLOCODE (required) | Eastern Anchorage Area |
| **Approach Areas** | Port entrance/exit zones | Port UNLOCODE (required) | Singapore Strait Approach |
| **Locks** | Lock facilities for inland waterways | Port UNLOCODE (required) | Panama Canal Locks |

### **Staging Tables (POMA)**

* `stg_port` - Port master data
* `stg_terminal` - Terminal facilities
* `stg_berth` - Berth positions
* `stg_anchorage` - Anchorage areas
* `stg_approach_area` - Approach zones
* `stg_lock` - Lock facilities

### **ODS Tables (POMA)**

* `ods_port` - Normalized port data
* `ods_terminal` - Normalized terminal data
* `ods_berth` - Normalized berth data
* `ods_anchorage` - Normalized anchorage data
* `ods_approach_area` - Normalized approach area data
* `ods_lock` - Normalized lock data
* `ods_port_terminals` - Port-terminal relationships
* `ods_port_berths` - Port-berth relationships
* `ods_port_approach_areas` - Port-approach area relationships
* `ods_port_locks` - Port-lock relationships

### **Example POMA Data Flow**

wide760POMA API (Port Configuration)
↓ [Filter: country\_code=SG]
stg\_port (Raw JSON data - Singapore ports only)
↓
ods\_port (Cleaned & Normalized)
↓
dim\_port (Analytics-ready dimension)

---

## Data Source 2: CSI (Central Ship Information API)

### **What is CSI?**

CSI is Teqplay's **Central Ship Registry API** that provides comprehensive vessel information including ship characteristics, identifiers, and classifications.

### **Data Ingestion Mode**

* **Batch Processing**: Scheduled periodic extractions (daily)
* **No Streaming**: Ship registry data changes infrequently

### **API Extraction Strategy**

#### **Filtering at API Level**

| Filter Type | Applied? | Filter Logic | Example |
| --- | --- | --- | --- |
| **Get All** | ✅ Yes | Retrieves ALL registered ships in the CSI database | No filters - complete ship registry |
| **Download Method** | ✅ Yes | Uses bulk download endpoint for efficiency | Downloads entire registry as JSON file |
| **No Filtering** | ❌ No | No country, flag, or ship type filters applied | Downloads all ships globally |

#### **Code Implementation**

pywide760# teqplay/repositories/ship.py
csi\_api.download\_registered\_ships\_all\_dbo(
to\_dirs=directories\_path,
filename=filename,
resource\_type='json',
token=token,
) # ← NO FILTERING - DOWNLOADS ENTIRE REGISTRY

### **Data Entities from CSI**

| Entity | Description | Filtering Strategy | Example Data |
| --- | --- | --- | --- |
| **Ships** | Complete ship registry (IMO, MMSI, name, type, dimensions) | None - Get ALL ships | Ever Given (IMO: 9811000) |

### **Staging Tables (CSI)**

* `stg_ship` - Raw ship registry data

### **ODS Tables (CSI)**

* `ods_ship` - Normalized ship data with ghost ship and disabled flags

### **Example CSI Data Flow**

wide760CSI API (Ship Registry)
↓ [No Filter - Get ALL ships]
stg\_ship (Raw JSON data - All ships globally)
↓
ods\_ship (Cleaned & Normalized)
↓ [Filter: ghost\_ship\_enabled = false, disabled = false]
dim\_ship (Analytics-ready dimension)

---

## Data Source 3: Vessel Voyage API

### **What is Vessel Voyage API?**

Vessel Voyage API is Teqplay's **Real-time Vessel Movement Tracking API** that provides:

* Port visit events (Statement of Facts - SOF)
* Vessel voyages between ports
* Area occupancy tracking
* Service vessel activities

### **Data Ingestion Modes**

#### **1. Batch Processing**

* **Schedule**: Hourly/Daily based on data type
* **Use Case**: Historical data backfill and regular updates
* **Filtering**: ✅ **ONLY COMPLETED** voyages/visits

#### **2. Streaming (RabbitMQ)**

* **Schedule**: Every 1 minute (near real-time)
* **Use Case**: Operational monitoring and live dashboards
* **Filtering**: ✅ Customer-based UNLOCODE filtering

### **API Extraction Strategy - BATCH MODE**

#### **Filtering at API Level (Batch)**

| Filter Type | Applied? | Filter Logic | Example |
| --- | --- | --- | --- |
| **Completed Only** | ✅ Yes | `finished='true'` - Only retrieves completed voyages/port visits | Excludes ongoing/in-progress visits |
| **Date Range** | ✅ Yes | `start` and `end` parameters - Temporal filtering | `start=2024-01-01&end=2024-01-31` |
| **UNLOCODE** | ✅ Yes | `unlocode` parameter - Port-specific filtering | `unlocode=SGSIN` (Singapore) |
| **Vessel Type** | ✅ Yes | `vesselType` parameter - Filter by vessel category | `vesselType=SEA_VESSEL,BARGE` |

#### **Code Implementation - Vessel Voyages (Batch)**

pywide760# teqplay/repositories/voyage.py
response = VesselVoyageAPI().get\_voyage\_by\_port(
token=token,
destinationPortUnlocodes=unlocode,
start=f'{start\_timestamp.format("YYYY-MM-DDTHH:mm:ss.SSS")}Z',
end=f'{end\_timestamp.format("YYYY-MM-DDTHH:mm:ss.SSS")}Z',
finished='true', # ← ONLY COMPLETED VESSEL VOYAGES
)

#### **Code Implementation - Statement of Facts (Batch)**

pywide760# teqplay/repositories/statement\_of\_fact.py
response = VesselVoyageAPI().get\_sof\_by\_port(
token=token,
encode\_query\_params=False,
view='PTO',
unlocode=unlocode,
finished='true', # ← ONLY COMPLETED PORT VISITS
start=f'{start\_timestamp.format("YYYY-MM-DDTHH:mm:ss.SSS")}Z',
end=f'{end\_timestamp.format("YYYY-MM-DDTHH:mm:ss.SSS")}Z',
vesselType=','.join(vessel\_types) # ← VESSEL TYPE FILTER
)

### **API Extraction Strategy - STREAMING MODE (RabbitMQ)**

#### **What is RabbitMQ Streaming?**

RabbitMQ is a **message broker** that provides real-time data streams from Vessel Voyage API. Instead of polling the API periodically, the system subscribes to message queues and receives updates as they happen.

#### **Streaming Data Types**

1. **Statement of Facts (SOF)** - Port visit events (arrivals, departures, berth movements)
2. **Area Occupancy** - Vessel positions within port areas
3. **Service Vessel** - Support vessel activities (tugs, pilots, bunker vessels)

#### **Filtering at Streaming Level**

| Filter Type | Applied? | Filter Logic | Example |
| --- | --- | --- | --- |
| **Customer-based UNLOCODE** | ✅ Yes | For non-Teqplay customers: Only data matching customer's port code | Customer USCRP only receives USCRP port data |
| **Teqplay Whitelist** | ✅ Yes | For Teqplay: Optional UNLOCODE whitelist via Airflow variable | `DATAFLOW_DATA_INGESTION_STREAMING_UNLOCODES` |
| **Completed Only** | ✅ Yes | `finished='true'` - Only retrieves completed voyages/port visits | Excludes ongoing/in-progress visits |

#### **Code Implementation - Customer Filtering**

pywide760# teqplay/services/streaming/rabbitmq/statement\_of\_fact.py
def \_get\_customer\_data(self, sofs: List[Dict]) -> List[Dict]:
if self.is\_ingesting\_teqplay\_data():
return sofs # ← TEQPLAY: NO FILTERING (or whitelist filtering)
filtered\_sofs = self.\_filter\_sofs\_by\_unlocode(sofs) # ← CUSTOMER: FILTER BY UNLOCODE
return filtered\_sofs

#### **Code Implementation - Whitelist Filtering**

pywide760# teqplay/services/streaming/rabbitmq/statement\_of\_fact.py
def \_filter\_by\_unlocode\_whitelist(self, sofs: List[Dict]) -> List[Dict]:
whitelist = self.manager.get\_streaming\_unlocode()
if whitelist is None:
return sofs # ← NO WHITELIST: Return all SOFs
# ← WHITELIST CONFIGURED: Filter by allowed UNLOCODEs
return [sof for sof in sofs if self.\_extract\_unlocode(sof) in whitelist]

### **Data Entities from Vessel Voyage API**

| Entity | Description | Filtering Strategy |
| --- | --- | --- |
| **Voyages** | Vessel journeys between ports | Batch: `finished='true'` + date range + UNLOCODE |
| **Statement of Facts (SOF)** | Port visit events and timelines | Batch: `finished='true'` + filters<br>Streaming: Customer UNLOCODE |
| **Area Occupancy** | Vessel positions in port areas | Streaming: Customer UNLOCODE |
| **Service Vessel** | Support vessel activities | Streaming: Customer UNLOCODE |

### **Staging Tables (Vessel Voyage)**

* `stg_voyage` - Vessel voyages
* `stg_statement_of_fact` - Port visit events
* `stg_area_occupancy` - Area occupancy tracking
* `stg_service_vessel` - Service vessel activities

### **ODS Tables (Vessel Voyage)**

* `ods_voyage` - Normalized voyage data
* `ods_port_visit` - Port visit master data
* `ods_terminal_visit` - Terminal visit data
* `ods_berth_visit` - Berth visit data
* `ods_anchor` - Anchorage events
* `ods_encounter` - Ship-to-ship encounters (bunkering, STS transfers)
* `ods_area_occupancy` - Area occupancy tracking
* `ods_service_vessel` - Service vessel activities

### **Example Vessel Voyage Data Flow - BATCH MODE**

wide760Vessel Voyage API (Port Visits)
↓ [Filter: finished='true', unlocode=SGSIN, start=2024-01-01, end=2024-01-31]
stg\_statement\_of\_fact (Raw JSON - ONLY COMPLETED visits in Singapore, Jan 2024)
↓
ods\_port\_visit (Cleaned & Normalized)
↓ [Filter: ghost\_ship\_enabled=false, disabled=false, start/end NOT NULL]
fact\_port\_visit (Analytics-ready fact table)

### **Example Vessel Voyage Data Flow - STREAMING MODE**

wide760RabbitMQ Message Broker (Real-time SOF stream)
↓ [Filter: Customer UNLOCODE = USCRP]
stg\_statement\_of\_fact (Raw JSON - ONLY USCRP port data, includes ongoing visits)
↓
ods\_port\_visit (Cleaned & Normalized)
↓ [Filter: ghost\_ship\_enabled=false, disabled=false]
fact\_port\_visit (Analytics-ready fact table - near real-time updates)

---

## Data Filtering at ODS and Fact Layers

While API-level filtering reduces the volume of data ingested, **additional filtering** is applied at the ODS and Fact layers to ensure data quality and analytical relevance.

### **ODS Layer Filtering**

| Filter Type | Applied? | Filter Logic | Purpose |
| --- | --- | --- | --- |
| **Ghost Ships** | ✅ Yes | `ghost_ship_enabled = false` | Exclude test/demo vessels |
| **Disabled Ships** | ✅ Yes | `disabled = false` | Exclude deactivated vessels |
| **Soft Deletes** | ✅ Yes | `deleted_timestamp IS NULL` | Exclude logically deleted records |
| **Valid Identifiers** | ✅ Yes | `ship_imo IS NOT NULL` (sea vessels)<br>`ship_mmsi IS NOT NULL` (barges) | Ensure valid ship identification |
| **Valid Port** | ✅ Yes | `unlocode IS NOT NULL` | Ensure valid port reference |

### **Fact Layer Filtering**

| Filter Type | Applied? | Filter Logic | Purpose |
| --- | --- | --- | --- |
| **Completed Visits** | ✅ Yes | `start_timestamp IS NOT NULL AND end_timestamp IS NOT NULL` | Only analyze completed port visits |
| **Vessel Type** | ✅ Yes | `visit_vessel_type = 'SEA_VESSEL'` or `'BARGE'` | Separate analysis for different vessel types |
| **Batch vs Streaming** | ✅ Yes | Batch: Filter by UNLOCODE<br>Streaming: Filter by visit IDs | Different filtering strategies per mode |

### **Code Implementation - Multi-Level Filtering**

pywide760# teqplay/templates/sql/dml/fact/berth\_visit/prepare\_mooring\_unmooring.sql
WHERE
s.ghost\_ship\_enabled IS false -- ← Exclude ghost ships
AND s.disabled IS false -- ← Exclude disabled ships
AND p.unlocode IS NOT null -- ← Valid port
AND pv.ship\_imo IS NOT null -- ← Valid ship IMO
AND bv.start\_timestamp IS NOT null -- ← Completed visit (start)
AND bv.end\_timestamp IS NOT null -- ← Completed visit (end)
AND bv.deleted\_timestamp IS null -- ← Not soft-deleted
{% if not is\_streaming\_data: %}
AND p.unlocode = %(unlocode)s -- ← BATCH: Filter by port
{% else %}
AND pv.visit\_id = any(%(entry\_ids)s) -- ← STREAMING: Filter by IDs
{% endif %}

---

## Summary: Data Filtering Strategies

### **POMA (Port Infrastructure)**

* **API Level**: Optional country code filter
* **Default**: Get ALL ports globally
* **ODS Level**: No additional filtering
* **Update Frequency**: Weekly/Monthly

### **CSI (Ship Registry)**

* **API Level**: ❌ NO FILTERING - Downloads entire ship registry
* **ODS Level**: Ghost ship and disabled ship flags added
* **Fact Level**: Filter out ghost ships and disabled ships
* **Update Frequency**: Daily

### **Vessel Voyage API - BATCH MODE**

* **API Level**: ✅ **ONLY COMPLETED** (`finished='true'`) + Date range + UNLOCODE + Vessel type
* **ODS Level**: Ghost ships, disabled ships, soft deletes
* **Fact Level**: Completed visits only (start/end timestamps NOT NULL)
* **Update Frequency**: Hourly/Daily

### **Vessel Voyage API - STREAMING MODE (RabbitMQ)**

* **API Level**: ✅ **ONLY COMPLETED** (`finished='true'`)
* **Streaming Level**: ✅ Customer UNLOCODE filtering (non-Teqplay) or Whitelist (Teqplay)
* **ODS Level**: Ghost ships, disabled ships, soft deletes
* **Fact Level**: Completed visits only for most analytics
* **Update Frequency**: Every 1 minute (near real-time)

---

## Key Takeaways

### **1. Data Source Roles**

* **POMA** provides the **"WHERE"** - Port infrastructure and geographical data
* **CSI** provides the **"WHO"** - Ship identification and characteristics
* **Vessel Voyage** provides the **"WHAT & WHEN"** - Actual vessel movements and events

### **2. Filtering Philosophy**

* **API Level**: Reduce data volume at source (completed visits, date ranges, UNLOCODE)
* **ODS Level**: Ensure data quality (ghost ships, disabled ships, soft deletes)
* **Fact Level**: Ensure analytical relevance (completed visits, valid identifiers)

### **3. Batch vs Streaming**

* **Batch Processing**: Used for historical data and infrequent updates

  + ✅ Filters for completed visits only
  + ✅ Date range filtering
  + ✅ Port-specific filtering
* **Streaming (RabbitMQ)**: Used for near real-time operational monitoring

  + ✅ Customer-based UNLOCODE filtering
  + ✅ Filters for completed visits only
  + ✅ 2-minute update frequency

### **4. Data Quality Filters**

All fact tables apply consistent data quality filters:

* `ghost_ship_enabled = false` - Exclude test vessels
* `disabled = false` - Exclude deactivated vessels
* `deleted_timestamp IS NULL` - Exclude soft-deleted records
* `start_timestamp IS NOT NULL AND end_timestamp IS NOT NULL` - Completed visits only

### **5. Data Flow Architecture**

All data flows through **Staging → ODS → Fact/Dimension** layers for:

* Data quality validation
* Business rule application
* Historical tracking with soft deletes
* Consistent analytical reporting

This architecture ensures that analytical reports have access to **complete, accurate, and timely** port performance data.
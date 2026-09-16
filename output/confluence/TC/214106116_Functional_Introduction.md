---
id: confluence:214106116
source: confluence
type: page
space: TC
title: Functional Introduction
author: Yaren Aslan
date: '2025-10-02'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/214106116
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/214106116
---
# Functional Introduction

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/214106116  

## Content

**Introduction:**

PTO is an acronym that stands for Port Turnaround Optimisation. It represents a specialised data processing procedure known as ETL, which stands for Extract, Transform, and Load. The primary objective of the ETL process within PTO is to generate a comprehensive and detailed report for a specific port.

The culmination of the ETL process within PTO is the creation of an extensive port report. This report is a valuable resource that provides a comprehensive overview of port operations, including details on cargo throughput, vessel arrivals and departures, inventory management, and various performance metrics. It offers port authorities, operators, and stakeholders a data-driven perspective on the port's activities and enables them to make informed decisions to optimise operations, allocate resources efficiently, and enhance overall performance.

In summary, Port Turnaround Optimisation (PTO) is a data-driven solution that leverages the ETL process to produce an extensive report for a port.

**ETL - Extract, Transform, and Load:**

ETL, which stands for Extract, Transform, and Load, is a data integration process Within the context of PTO, this process involves the following key steps:

* **Extract:** Data is gathered from multiple sources, including VesselVoyage, Poma, CSI, Platform, PortReporter, and (R)event. This data extraction phase ensures that a wide range of relevant information is collected for analysis.
* **Transform:** Once the data is extracted, it undergoes a transformation phase. During this step, the collected information is processed, cleaned, and standardized. This ensures data accuracy and consistency, making it suitable for further analysis.
* **Load:** After transformation, the refined data is loaded into a centralized database or data warehouse. This consolidated dataset serves as the foundation for generating insightful reports and analytics.

**Technology Stack:**

* **Language:** Kotlin
* **Technology:** The project is built using Spring Boot
* **Database:** The project relies on a relational database management system, specifically PostgreSQL.

**Development Environment Setup Guide:**

* **Get the Source Code:**To start working on the project, developers should clone the source code repository hosted on Bitbucket. The repository can be accessed at the following URL: [https://<Username>@bitbucket.org/teqplay/pto-etl.git](#)
* **Database Access:** The database required for the project is available at the specified host and port: hydra-postgresql.eks-dev.teqplay:5432
* **Configure Application Credentials:** After cloning the source code, developers need to add their credentials to the application.yml file. This file likely contains configuration settings, including database connection details and other environment-specific properties. Developers should ensure that their credentials and environment-specific settings are correctly configured in this file.
* **Start the Project:** Once the source code is cloned and the application is configured with the necessary credentials, developers can initiate the project. This typically involves running the application using a development server or build tool provided by Spring Boot.

**Key Components:**

* **PTO-ETL Process:**

**Step 1 - Updating Static Data:** This step involves updating static data related to ports, terminals, and berths information. This data is retrieved from the POMA API. The purpose of this update is to ensure that the system has the latest information about these elements, which is crucial for accurate analysis and reporting.

**Step 2 - Requesting Vessel Voyage Data:** In this step, the system requests vessel voyage data to retrieve relevant visits. These visits are important for tracking and analyzing vessel activities at specific locations.

**Step 3 - Extracting IMOs:** From the retrieved visits, the system extracts IMOs and requests information about the corresponding ships from the CSI system. This ship information is then stored for further processing.

**Step 4 - Requesting Event Generation:** The system requests the (R)vent engine to start generating events. These events could be related to various aspects of port operations and vessel activities.

**Step 5 - Data Cleaning and Visit Merging:** This step involves cleaning and preparing the data. Additionally, it includes merging visits data.

**Step 6 - Data Transformation:** The final step in the PTO-ETL process is data transformation. This includes combining data, gathering relevant information, and applying transformations to create datasets related to Berth visits and Port visits. These datasets are likely to be used for analysis and reporting. 

* **APMT Report:** The APMT report runs multiple instances of the PTO-ETL process. Each instance is based on specific time frames and requested ports. This component is responsible for generating reports and insights based on the data processed by the PTO-ETL process.
* **Charter Report:** Similar to the APMT report, the Charter report also runs multiple instances of the PTO-ETL process. However, in this case, the report is generated based on received IMOs and ports. The Charter report component is responsible for generating reports and insights related to charter operations based on the processed data.
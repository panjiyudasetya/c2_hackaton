---
id: confluence:440532996
source: confluence
type: page
space: TC
title: 2. Proposal for New Teqplay ETL
author: Panji Y. Wiwaha
date: '2025-04-17'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/440532996
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/440532996
---
# 2. Proposal for New Teqplay ETL

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/440532996  

## Content

Proposal for Developing a Data Warehouse Design with <http://Nats.io> Streaming and Apache Airflow

**Prepared for:** Teqplay  
**Prepared by:**  and    
**Date:** August 21, 2024

### ***1. Executive Summary***

Up till today the majority of Teqplay’s data is unused by customers. The value of maritime data is undeniable. For Teqplay, opening up its data in a contextual and accessible way is a path towards new revenue generation. Shortened time to insights increases Teqplay’s ability to execute and be agile towards a quickly changing data demand in the industry. This proposal outlines a strategy for developing a modern data warehouse design that utilizes streaming data ingestion and Apache Airflow for streamlined ETL (Extract, Transform, Load) workflows. Our solution aims to enhance data accessibility, improve decision-making, and provide a competitive edge through timely insights.

### ***2. Objectives***

* Develop a scalable data warehouse architecture capable of handling real-time data streams.
* Implement tools and technologies for efficient data processing, orchestration, and management.
* Ensure that the data warehouse supports business intelligence and analytics needs across the organization.

### ***3. Scope of Work***

The scope of this project will include:

#### **Data Warehouse Design**

* Identify and define business requirements.
* Develop a conceptual, logical, and physical data model.
* Choose appropriate cloud-base storage solutions

#### **Streaming Data Ingestion**

* Select streaming technologies <http://Nats.io> as a Streaming Data Ingestion source for our data warehouse.
* Design data ingestion pipelines for real-time processing.
* Implement mechanisms for data validation and error handling.
* Subscribe Vessel Voyage events from the Nats Publisher.

#### **ETL Development with Apache Airflow:**

* Set up Apache Airflow for workflow orchestration.
* Define and schedule data extraction, transformation, and loading tasks.
* Implement monitoring and alerting mechanisms for data pipeline failures.

#### **Testing and Deployment:**

* Conduct thorough testing of pipelines and data transformations.
* Deploy the solution in a production environment.
* Provide documentation and training for end-users and administrators.

### ***4. Methodology***

#### **Phase 1: Discovery and Planning**

* Conduct workshops with stakeholders to gather requirements.
* Assess existing data infrastructure.

High-level Designs

#### **Phase 2: Design**

* Create the architectural design of the data warehouse and or datamart.
* Design data models based on user needs.

ETL Module Architecture

Teqplay Architecture DWH/DWM Flow Design

Customer Architecture DWH/DWM Flow Design

#### **Phase 3: Implementation**

* Set up data streaming solutions in python microservices Apps.
* Develop ETL workflows in Apache Airflow.

#### **Phase 4: Testing and Launch**

* Perform user acceptance testing (UAT).
* Launch the data warehouse and provide end-user training.

### ***5. Technology Stack***

* **Data Warehouse:** RDS Postgres, Amazon Redshift
* **Streaming Technologies:** <http://Nats.io>
* **Orchestration Tool:** Apache Airflow
* **Data Processing ETL-Framework:** Python Microservices Apps
* **Visualization Tools:** Power BI

### ***6. Conclusion***

This proposal outlines a comprehensive approach to developing a data warehouse design that leverages streaming capabilities and facilitates efficient data orchestration with Apache Airflow. We are committed to delivering a solution that meets the strategic needs of Teqplay and transforms data into actionable insights.
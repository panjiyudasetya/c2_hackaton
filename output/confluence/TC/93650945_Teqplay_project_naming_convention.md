---
id: confluence:93650945
source: confluence
type: page
space: TC
title: Teqplay project naming convention
author: Darius Wattimena
date: '2022-03-08'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/93650945
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/93650945
---
# Teqplay project naming convention

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/93650945  

## Content

## Rules

* Project repositories, DNS entries, S3 buckets and EC2/EB/EKS instances must always be written in lowercase.
* Any whitespace used in any name must be replaced with a `-` (hyphen).
* The repository name must always match the naming used in the DNS record.

  + This doesn’t apply for backend repositories as the hyphen in `<project_name>-backend` will be removed to follow the following scheme `<project_name>backend.teqplay.nl`.
  + This doesn’t apply to projects with multiple environments (e.g. bunkerplanner).

## Backend

Repository name: `<project_name>-backend`

### Kubernetes

Production:

* Service: `<project_name>`
* Database Service: `db-<project_name>`

Develop:

* Service: `<project_name>-dev`
* Database Service: `db-<project_name>-dev`

### Elastic Beanstalk (EB)

Production: `<project_name>-env`  
Develop: `<project_name>-dev-env`

### EC2 Machine

Production: `<project_name>`  
Develop: `<project_name>-dev`  
EKS Node Group: `eks-<cluster_name>-node`  
Production Database: `db-<database_name>`  
Develop Database: `db-<database_name>-dev`

### DNS

Production: `<project_name>backend.teqplay.nl`  
Develop: `<project_name>backenddev.teqplay.nl`

## Frontend

Repository name: `<project_name>`

### S3 Bucket

Bucket name: `<projectname>.teqplay.nl`

### DNS

Production: `<project_name>.teqplay.nl`  
Develop: `<project_name>dev.teqplay.nl`

## Project Examples:

| **Project** | **Instance** | **Frontend** | | **Backend** | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Repository** | **S3 Bucket / DNS** | **Repository** | **DNS** | **EB / EC2** | **Kubernetes** |
| **PortReporter** | Production | portreporter | portreporter.teqplay.nl | portreporter-backend | portreporterbackend.teqplay.nl | portreporter-env | portreporter |
| Develop | - | portreporterdev.teqplay.nl | - | portreporterbackenddev.teqplay.nl | portreporter-dev-env | portreporter-dev |
| **VesselVoyage** | Production | vesselvoyage | vesselvoyage.teqplay.nl | vesselvoyage-backend | vesselvoyagebackend.teqplay.nl | vesselvoyage-env | vesselvoyage |
| Develop | - | vesselvoyagedev.teqplay.nl | - | vesselvoyagebackenddev.teqplay.nl | vesselvoyage-dev-env | vesselvoyage-dev |
| **CSI** | Production | csi | csi.teqplay.nl | csi-backend | csibackend.teqplay.nl | csi-env | csi |
| Develop | - | csidev.teqplay.nl | - | csibackenddev.teqplay.nl | csi-dev-env | csi-dev |
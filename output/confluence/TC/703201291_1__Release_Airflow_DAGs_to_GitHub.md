---
id: confluence:703201291
source: confluence
type: page
space: TC
title: 1. Release Airflow DAGs to GitHub
author: Panji Y. Wiwaha
date: '2025-04-21'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/703201291
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/703201291
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/569770069/3.+Data+Platform+Teqplay+architecture+overview?atlOrigin=eyJpIjoiYmU5YTZlYzU5Y2QwNDMyMThlZmI1MDUyMTA4Yjk0Y2MiLCJwIjoiYyJ9
---
# 1. Release Airflow DAGs to GitHub

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/703201291  

## Content

# Introduction

DAG is a collection of the tasks we want to run and organize through the Airflow app. In Teqplay, we manage multiple DAG repositories, which are:

1. [**dataflow\_dag\_core**](https://github.com/teqplay/dataflow_dag_core) → It is a repository to run the ETL pipeline used in the [**Teqplay Airflow App**](https://airflow.teqplay.dev/home). This repo aims to generate a report for particular topics based on vessel visitation through any port, terminal, or berth.
2. [**dataflow\_dag\_pocca**](https://github.com/teqplay/dataflow_dag_pocca) → It is a repository to run the ETL pipeline used in the [**Port of Corpus Christy Airflow App**](http://airflowpoccadev.teqplay.dev/home). This repo aims to generate a report for particular topics based on vessel visitation to the Port of Corpus Christy.
3. [**dataflow\_dag\_apmt**](https://github.com/teqplay/dataflow_dag_apmt) → It is a repository to run the ETL pipeline used in the **APMT Terminal Airflow App**. This repo aims to generate a report for particular topics based on vessel visitation to the APMT Terminal.

You may need to read this <https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/569770069/3.+Data+Platform+Teqplay+architecture+overview?atlOrigin=eyJpIjoiYmU5YTZlYzU5Y2QwNDMyMThlZmI1MDUyMTA4Yjk0Y2MiLCJwIjoiYyJ9> to understand why we decided to define the Airflow DAG using a multiple-repositories approach instead of a mono-repository.

# How to create a new GitHub release?

Before creating a new GitHub release, please be aware that:

* Any changes merged to the `develop` branch in the DAG repository will be reflected immediately in the Airflow App on devGreen environment.
* Any changes merged to the `master` branch in the DAG repository will be reflected in the Airflow App on LIVERed environment.

However, it is important for us to track the changes made in each environment at the end of the sprint by following the following steps.

### Step 1 - Setup GitHub Token

* You can create your own GitHub access token by accessing **Developer Settings** and clicking the **Generate new token** button on the **Personal Access Tokens** page.

* Make sure to select all items within the choices panel for repository access.

* Once it is successful, copy the generated access token and keep it in a secure note.
* Copy the `.github_secrets.example` file within the `scripts/` directory and paste it as `.github_secrets` file.

dataflow\_dag\_core
|- scripts
|- .github\_secrets
|- .github\_secrets.example

* Open the `.github_secrets` file, and update the `GITHUB_TOKEN` variable with your personal access token.

GITHUB\_TOKEN='ghp\_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
GITHUB\_ORG='teqplay'
GITHUB\_REPOSITORY='teqplay/dataflow\_dag\_core'

### Step 2 - Create a new GitHub release

* Create a new GitHub Milestone; it is on the **GitHub Issues** tab.

* Include all PRs that you want to release in the created milestone.

### Step 3 - Run a GitHub release script

* Open your terminal.
* Run the release script `./scripts/release.sh`; A command prompt will appear for you to fill in the release details.
* When you fill in the changelog, make sure to include all associated PR numbers,  
  indicated by `#<PR_NUMBER>`, for example:

## [1.3.0] - 2025-04-15
### Added
- Add DAG to clean up and reload visits from Vessel Voyage (#52, #61, #65)
- Add ship id for both ships on ship-to-ship transfers (#67, #69, #70)
- Add anchor duration before visit, during visit, and after visit #66
### Changed
- Replace the wait sensor with a trigger dag run operator (#63, #64, #68)
### Fixed
- Fix failure DAG to calculate terminal's standard deviation #62
- Fix failure DAG to generate data of the ODS voyage #60

* Wait until the release script is done. The script will handle all of the release flow automatically (ie. creating a new tag, pull requests, etc).
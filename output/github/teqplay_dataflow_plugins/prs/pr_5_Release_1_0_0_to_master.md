---
id: github:teqplay/dataflow_plugins:pr:5
source: github
type: pull_request
repo: teqplay/dataflow_plugins
number: 5
title: Release 1.0.0 to master
author: panjiyudasetya
state: closed
date: '2025-03-11'
merged_at: '2025-03-11'
base_branch: master
head_branch: release/1.0.0
url: https://github.com/teqplay/dataflow_plugins/pull/5
labels: []
linked_issues: []
explicit_links:
- jira:PTO-1063
- jira:PTO-1495
- jira:PTO-1849
- jira:PTO-1833
---
# PR #5: Release 1.0.0 to master

**Repo:** teqplay/dataflow_plugins  
**URL:** https://github.com/teqplay/dataflow_plugins/pull/5  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `master` ← `release/1.0.0`  
**Created:** 2025-03-11  
**Merged:** 2025-03-11  

## Description

## [1.0.0] - 2025-03-11
### Added
- Add Teqplay API clients.
- Add common utilities.

## Commits

- `2e6eea97` **panjiyudasetya** (2024-09-13): Update `.gitignore`
- `0d276fb4` **panjiyudasetya** (2024-09-13): Add bitbucket pipelines
- `2333fc34` **panjiyudasetya** (2024-09-13): Add file `.env` example
- `7cd68e91` **panjiyudasetya** (2024-09-13): Add project requirements
- `4498263f` **panjiyudasetya** (2024-09-13): Add vscode settings
- `13a67ca2` **panjiyudasetya** (2024-09-13): Add shell scripts to run linter checks and tests
- `959e8aa2` **panjiyudasetya** (2024-09-13): Move `etl` module to the dataflow plugins repository
- `a264654f` **panjiyudasetya** (2024-09-13): Move the `etl` module tests to the dataflow plugins repository
- `860b29d9` **Panji Yudasetya Wiwaha** (2024-09-13): Merged in PTO-1063-dataflow-plugins (pull request #1)
  PTO-1063 Move the `etl` module into dataflow plugins
  
  Approved-by: Ryan Kharisma Rakhmat
- `7136d441` **panjiyudasetya** (2024-09-17): Set maximum split into one
- `6b779ceb` **Panji Yudasetya Wiwaha** (2024-09-19): Merged in PTO-1063-fix-manage-dot-py (pull request #2)
  PTO-1063 Set maximum split into one
  
  Approved-by: Ryan Kharisma Rakhmat
- `dc90c433` **panjiyudasetya** (2024-09-20): Ignore microseconds from the iso time
- `8ccb1f8a` **Panji Yudasetya Wiwaha** (2024-09-20): Merged in fix/duplicate-time-during-upsert (pull request #3)
  Ignore microseconds from the iso time
  
  Approved-by: Ryan Kharisma Rakhmat
- `e95e0593` **Panji Yudasetya Wiwaha** (2024-12-05): Remove deprecated etl module
- `280603d3` **Panji Yudasetya Wiwaha** (2024-12-05): Add `psycopg` library
- `134d8ced` **Panji Yudasetya Wiwaha** (2024-12-05): Add dataflow utilities
- `da9a2be5` **Panji Yudasetya Wiwaha** (2024-12-05): Add api clients
- `79834e71` **Panji Yudasetya Wiwaha** (2024-12-05): Add tests to the utilities plugin
- `a276ce69` **Panji Yudasetya Wiwaha** (2024-12-05): Add tests to the api clients plugin
- `a04ef985` **Panji Yudasetya Wiwaha** (2024-12-05): Update env file example
- `bdd5459f` **Panji Yudasetya Wiwaha** (2024-12-06): Merged in PTO-1495-part-3 (pull request #6)
  PTO-1495 [Part 3] Add tests to the dataflow plugins
  
  Approved-by: Ryan Kharisma Rakhmat
- `120fa1f2` **panjiyudasetya** (2024-12-06): Rename teqplay api module
- `ee8e0e6f` **Panji Yudasetya Wiwaha** (2024-12-06): Merged in PTO-1495-part-2 (pull request #5)
  PTO-1495 [Part 2] Move API clients and utility functions as from DAG to plugins
  
  Approved-by: Ryan Kharisma Rakhmat
- `686cc06b` **Panji Yudasetya Wiwaha** (2024-12-06): Merged in PTO-1495-part-1 (pull request #4)
  PTO-1495 [Part 1] Remove deprecated ETL module
  
  Approved-by: Ryan Kharisma Rakhmat
- `7f6b2455` **Panji Yudasetya Wiwaha** (2024-12-09): Rename test modules
- `de750a7a` **Panji Yudasetya Wiwaha** (2024-12-09): Update `.gitignore`
- `59f46207` **Panji Yudasetya Wiwaha** (2024-12-09): Add readme file
- `8fe70370` **Panji Yudasetya Wiwaha** (2024-12-09): Setup `pyproject.toml`
- `511863cd` **Panji Yudasetya Wiwaha** (2024-12-09): Merged in add-package-dist (pull request #7)
  PTO-1495 Add configuration to create python package
  
  Approved-by: Ryan Kharisma Rakhmat
- `0c2acdb3` **Panji Yudasetya Wiwaha** (2024-12-12): Add missing requirements on poject toml
- `414c857f` **Panji Yudasetya Wiwaha** (2024-12-12): Update `README.md` file
- `e312df85` **Panji Yudasetya Wiwaha** (2024-12-13): Merged in chore/project-documentations (pull request #8)
  Update project documentations
  
  Approved-by: Ryan Kharisma Rakhmat
- `99230519` **Panji Y. Wiwaha** (2025-02-21): Create Github workflow `config.yml`
- `5377d14d` **Panji Y. Wiwaha** (2025-02-21): Update gh workflows config
- `b5061244` **Panji Y. Wiwaha** (2025-02-21): Merge pull request #1 from teqplay/chore/gh-workflow
  Create Github workflow `config.yml`
- `e9ccb6ed` **Panji Y. Wiwaha** (2025-03-10): Update dev URLs setting for POMA and Vessel Voyage API
- `a9337696` **Panji Y. Wiwaha** (2025-03-10): Update doc-strings
- `3dc307f0` **Panji Y. Wiwaha** (2025-03-10): Update tests
- `46bd47af` **Panji Y. Wiwaha** (2025-03-10): Merge pull request #2 from teqplay/PTO-1849
  PTO-1849 Updates URL settings to ingest data from Teqplay
- `9a25962b` **Panji Y. Wiwaha** (2025-03-10): Add empty changelog file
- `44baf39b` **Panji Y. Wiwaha** (2025-03-10): Plugins version initialization
- `ba050250` **Panji Y. Wiwaha** (2025-03-10): Add shell script to prepare a new release
- `344626d5` **Panji Y. Wiwaha** (2025-03-10): Fix incorrect regex
- `fd9445c6` **Panji Y. Wiwaha** (2025-03-11): Merge pull request #3 from teqplay/PTO-1833-prepare-release-scripts
  PTO-1833 Release preparations
- `fb7dca98` **Panji Y. Wiwaha** (2025-03-11): Bump version 1.0.0

## Reviews

### ryan-kharisma — APPROVED (2025-03-11)

_No comment._

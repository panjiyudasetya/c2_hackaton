---
id: github:teqplay/dataflow_dag_core:pr:748
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 748
title: Release 1.57.0 to master
author: panjiyudasetya
state: closed
date: '2026-08-27'
merged_at: '2026-08-27'
base_branch: master
head_branch: release/1.57.0
url: https://github.com/teqplay/dataflow_dag_core/pull/748
labels: []
linked_issues: []
explicit_links:
- jira:PTO-2930
- jira:PTO-2953
---
# PR #748: Release 1.57.0 to master

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/748  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `master` ← `release/1.57.0`  
**Created:** 2026-08-27  
**Merged:** 2026-08-27  

## Description


## [1.57.0] - 2026-08-27
### Added
- Add Claude data convention review on the project (#745)

### Removed
- Remove FDW left-over experiments (#742) 

### Changed
- Replace all legacy `port_visit_id` generation with `ods_port_visit.visit_id` which is the stable canonical PK (#746)

## Commits

- `ae04d73b` **Panji Y. Wiwaha** (2026-08-19): chore(fdw): remove PostgreSQL Foreign Data Wrapper experiment
  The FDW approach was successfully validated but we decided not to adopt it
  at this stage. This removes all FDW-specific DAGs, task groups, SQL templates,
  QC checks, and related variable keys, leaving only the legacy Python-chunking
  workflow.
- `dccd05bb` **Panji Y. Wiwaha** (2026-08-21): Merge pull request #743 from teqplay/release/1.56.0
  Release 1.56.0 to develop
- `034cba04` **Panji Y. Wiwaha** (2026-08-21): Merge pull request #742 from teqplay/PTO-2930
  PTO-2930 Remove PostgreSQL Foreign Data Wrapper left-over experiment
- `76b3b6be` **Panji Y. Wiwaha** (2026-08-21): chore(claude): enable data convention review on the project
- `d32b2102` **Panji Y. Wiwaha** (2026-08-24): refactor(fact-dml): use visit_id as canonical port visit identifier
  Replace all legacy port_visit_id generation with ods_port_visit.visit_id
  across the fact DML pipeline:
  
  - anchor, bunkering, tug, pilot proceed/proceed_delta: drop ods_port_visit.id
    (generation_id) in favour of ods_port_visit.visit_id
  - ship_to_ship proceed: drop concat(pv.id, '_', pv.visit_id) composite key
  - port_visit prepare_* files: replace composite concat and bpv.id routing keys
    with bpv.visit_id throughout all internal CTEs
  - add_berths_summary, add_terminals_summary, add_shifting_inside_terminals:
    switch all CTE routing keys and UPDATE WHERE conditions to visit_id
  - add_ship_to_ship_summary: filter and join against fact_port_visit.visit_id
    instead of fact_port_visit.port_visit_id
- `a87b7cbb` **Panji Y. Wiwaha** (2026-08-24): refactor(qc): use visit_id as canonical port visit identifier in QC queries
  - anchor, bunkering, tug, pilot components: pv.id → pv.visit_id as port_visit_id
  - pilot/summary_accuracy: fix join on fact_port_visit — was matching on .id
    (generation_id) which breaks post-migration; corrected to .visit_id
  - pilot_components: replace 4 occurrences of pv.id alias; preserve ODS self-join
    ON pv.id = opv.id (intentional generation_id join within ODS layer)
  - port_visit accuracy components (drifting, port_travel, sailing, waiting_time):
    drop concat composite key, switch internal CTE routing keys to bpv.visit_id
  - prepare_ods_encounter_pilot: 6 occurrences updated; ODS self-join preserved
  - port_visit_anchor_overlaps: drop concat composite key
- `bb587eec` **Panji Y. Wiwaha** (2026-08-24): refactor(silver,analytics): reference fact_port_visit by visit_id not port_visit_id
  Retire fact_port_visit.port_visit_id as an external join target; all code
  outside the fact_port_visit DML pipeline now joins on fact_port_visit.visit_id.
  
  - enriched_portcall_performance_monthly (silver MV): base_port_visit CTE now
    selects fpv.visit_id AS port_visit_id and joins tug_wait/boatmen_wait/bunker_wait
    via fpv.visit_id = *.port_visit_id
  - calculate_outlier_flags: selects pv.visit_id AS port_visit_id when populating
    the temp_port_visit_outlier_flags routing table
  - update_port_visit_from_temp: WHERE clause updated to pv.visit_id = t.port_visit_id
- `5762cf56` **Panji Y. Wiwaha** (2026-08-24): Merge pull request #745 from teqplay/chore/claude-plugins
  Enable data convention review on the project
- `65bd2edb` **Panji Y. Wiwaha** (2026-08-27): fix(fact-dml): exclude soft-deleted ships and ports in port_visit DML
  Add missing deleted_timestamp IS null guards to every ods_ship and
  ods_port JOIN across the port_visit prepare queries, ensuring soft-deleted
  infrastructure is consistently excluded at query time.
- `8b2a14bf` **Panji Y. Wiwaha** (2026-08-27): fix(fact-dml): exclude soft-deleted ships and ports in berth_visit and terminal_visit DML
  Add missing deleted_timestamp IS null guards to ods_ship and ods_port
  JOINs across all berth_visit and terminal_visit prepare queries.
- `0f02e321` **Panji Y. Wiwaha** (2026-08-27): fix(fact-dml): exclude soft-deleted ships and ports in pilot DML
  Add missing deleted_timestamp IS null guards to ods_ship (service ship
  aliases s_imo, s_mmsi) and ods_port JOINs across all pilot prepare and
  proceed queries, preserving LEFT JOIN semantics for delta files.
- `4e0f90f5` **Panji Y. Wiwaha** (2026-08-27): fix(fact-dml): exclude soft-deleted ships and ports in anchor, bunkering, tug, ship_to_ship and voyage DML
  Add missing deleted_timestamp IS null guards to ods_ship and ods_port
  JOINs in proceed and proceed_delta queries for the remaining fact DML
  pipelines.
- `db7bd22a` **Panji Y. Wiwaha** (2026-08-27): fix(qc): exclude soft-deleted ships and ports in accuracy QC queries
  Add missing deleted_timestamp IS null guards to ods_ship and ods_port
  JOINs across all accuracy component queries (anchor, berth_visit,
  bunkering, pilot, port_visit, tug).
- `e22f12fb` **Panji Y. Wiwaha** (2026-08-27): fix(qc): exclude soft-deleted ships and ports in completeness, uniqueness and validity QC queries
  Add missing deleted_timestamp IS null guards to ods_ship and ods_port
  JOINs across completeness (berth_visit, encounter, port_visit,
  terminal_visit, tug_event), uniqueness_check (berth_visit, port_visit,
  terminal_visit), and validity (port_visit_anchor_overlaps) queries.
- `ca13763e` **Panji Y. Wiwaha** (2026-08-27): fix(linter): resolved sqlfluff linter error
- `0de2df96` **Panji Y. Wiwaha** (2026-08-27): Merge pull request #746 from teqplay/PTO-2953
  PTO-2953
- `4302e89e` **Panji Y. Wiwaha** (2026-08-27): Bump version 1.57.0

## Reviews

### ryan-kharisma — APPROVED (2026-08-27)

LGTM

## Comments

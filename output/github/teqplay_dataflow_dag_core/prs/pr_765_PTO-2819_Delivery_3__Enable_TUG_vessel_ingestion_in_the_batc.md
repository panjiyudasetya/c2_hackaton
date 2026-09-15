---
id: github:teqplay/dataflow_dag_core:pr:765
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 765
title: 'PTO-2819 Delivery 3: Enable TUG vessel ingestion in the batching pipeline'
author: panjiyudasetya
state: closed
date: '2026-09-08'
merged_at: '2026-09-09'
base_branch: develop
head_branch: PTO-2819-pt3
url: https://github.com/teqplay/dataflow_dag_core/pull/765
labels: []
linked_issues: []
explicit_links:
- jira:PTO-2819
- github:teqplay/dataflow_dag_core:pr:766
---
# PR #765: PTO-2819 Delivery 3: Enable TUG vessel ingestion in the batching pipeline

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/765  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `develop` ← `PTO-2819-pt3`  
**Created:** 2026-09-08  
**Merged:** 2026-09-09  

## Description

### Description

TUG SOFs arrive on the same sea-vessel and barge API endpoints as regular vessels (`?vesselType=SEA_VESSEL|BARGE`). Until this PR the batching path had two problems:

- **SEA_VESSEL path:** TUG records were explicitly discarded by `_is_tug_or_bunker_vessels` in `is_sof_valid`.
- **BARGE path:** TUG records slipped through unfiltered and were stamped `vessel_type='BARGE'` — an active data-quality bug.

No dedicated TUG staging DAG is needed. TUG records already arrive via bleed-through on both existing batch DAGs. The fix is to resolve the correct vessel type at the point of stamping and stop discarding records that are now legitimate.

### What changed

#### `teqplay/services/statement_of_fact.py`

- **`_resolve_vessel_type(sof, default)`** — new method. Reads `ship.categories` from the raw SOF dict and returns `VesselType.TUG` when found, otherwise the service default. BUNKER detection is deferred to a follow-up PR.
- **`_flatten_sofs`** — calls `_resolve_vessel_type` per record instead of stamping `self._vessel_type.value` unconditionally. Fixes the BARGE-path bug as a side effect.
- **`_convert_parquet_records_to_sofs`** — same resolution applied to the Parquet cache path. The `ship` JSON string is parsed once per record solely for category detection; the stored value is unchanged.
- **`_is_sof_completed`** — now reads `vessel_type` from the data dict (stamped upstream by `_resolve_vessel_type`) so TUG records going through the SEA_VESSEL service run are not held to the `slowMovingPeriods` rule.
- **`_clean_sofs`** — passes `vessel_type` from the flattened row into `is_sof_valid` so `_is_sof_completed` has it available.
- **`_is_tug_or_bunker_vessels` → `_is_bunker_vessel`** — narrowed to BUNKER only. TUG is no longer discarded in the SEA_VESSEL filter path.

#### `teqplay/dags/mart/fact_daily_refresh_dag.py`

- Added `refresh_fact_sof__tug` task group after BARGE in the daily refresh chain.

### What was not changed

- No new staging DAG. TUG records are picked up by the existing SEA_VESSEL and BARGE batch DAGs; `ON CONFLICT (entry_id) DO NOTHING` in the staging insert handles any duplicates safely.
- No new ODS or fact stream DAG. `ods_sof__stream` (every 5 min) and `fact_sof__stream` (every 15 min) already have TUG task groups from the prior delivery and will process batched TUG records from the queue on their schedule.
- SEA_VESSEL and BARGE behaviour is unchanged — the `_is_sof_completed` fallback is `self._vessel_type.value` when no per-record `vessel_type` key is present, preserving existing logic exactly.

### Test plan

- [ ] Run `staging_sof__sea_vessel_by_port` for a port known to have TUG traffic. Confirm new rows appear in `stg_statement_of_fact` with `vessel_type = 'TUG'`.
- [ ] Confirm `ods_sof__stream` promotes TUG records to `ods_port_visit` with `visit_vessel_type = 'TUG'`.
- [ ] Confirm `fact_sof__stream` promotes them to facts.
- [ ] Confirm existing SEA_VESSEL and BARGE row counts in staging/ODS/fact are unaffected.
- [ ] Trigger `fact_daily_refresh` manually and confirm the new `refresh_fact_sof__tug` task group runs and completes.

## Commits

- `59a00899` **Panji Y. Wiwaha** (2026-09-08): feat(sof): enable TUG vessel ingestion in batching path
  Resolves the active bug where TUG records leaking through the SEA_VESSEL
  and BARGE endpoints were either discarded or stamped with the wrong
  vessel_type. TUG SOFs now flow through the existing batch DAGs and are
  correctly tagged at every stage.
  
  - Add _resolve_vessel_type to detect TUG from ship.categories and
    override the service-level default stamp
  - Apply resolution in _flatten_sofs (API path) and
    _convert_parquet_records_to_sofs (Parquet cache path)
  - Pass per-record vessel_type into is_sof_valid so _is_sof_completed
    does not apply SEA_VESSEL slowMovingPeriods rules to TUG records
  - Rename _is_tug_or_bunker_vessels to _is_bunker_vessel and narrow it
    to BUNKER only; TUG is no longer discarded in the SEA_VESSEL filter path
  - Extend fact_daily_refresh_dag to include TUG refresh after BARGE
  
  BUNKER ingestion is deferred to a separate PR.
- `7a82a518` **Panji Y. Wiwaha** (2026-09-08): fix(sof): use per-record vessel_type in SOF validity checks and guard null ship
  - is_sof_valid now resolves vessel_type from the per-record key (same as
    _is_sof_completed) so a TUG+BUNKER record stamped as TUG is not rejected
    by the BUNKER filter when the service runs in SEA_VESSEL mode
  - _is_bunker_vessel guards against ship being null/None to avoid AttributeError
  - Updated is_sof_valid docstring to clarify that both checks key off the
    per-record vessel_type, not the service-level self._vessel_type
- `b8a646e8` **Panji Y. Wiwaha** (2026-09-08): test(sof): cover per-record vessel_type override in _is_sof_completed
  Add parametrised test asserting that a SEA_VESSEL service instance honours
  the per-record vessel_type key: TUG- and BUNKER-stamped records bypass the
  slowMovingPeriods requirement, while SEA_VESSEL-stamped records still enforce it.
- `a4066559` **Panji Y. Wiwaha** (2026-09-08): feat(sof): add fact_sof__tug batch DAG and wire into fact orchestrator
  TUG records reach ODS via the SEA_VESSEL ingestion path but were silently
  dropped before fact loading: the SEA_VESSEL fact query requires
  end_timestamp IS NOT NULL (which TUG visits may not have), and the BARGE
  query filters visit_vessel_type = 'BARGE'.
  
  - Add DagID.FACT_SOF_TUG ('fact_sof__tug') to the mart DagID enum
  - Add teqplay/dags/mart/fact_sof/tug_vessel_dag.py, a dedicated batch DAG
    that mirrors the sea_vessel/barge pattern with vessel_type = VesselType.TUG
  - Wire call_fact_sof_tug into fact_transformation_dag.py, running
    unconditionally after call_fact_sof_sea_vessel and before the barge branch
- `d806c467` **Panji Y. Wiwaha** (2026-09-08): fix(sof): extend DML fact templates to handle TUG/BUNKER vessel type correctly
  All three base-query templates (port_visit, berth_visit, terminal_visit) had the
  same two defects when vessel_type = TUG/BUNKER:
  
  1. Vessel-type filter: berth_visit and terminal_visit only had is_barge (true/false),
     so TUG fell into the SEA_VESSEL else-branch which enforced end_timestamp IS NOT NULL,
     silently discarding all open-ended TUG visits. Added an is_tug_bunker elif branch
     (mirrors the existing branch in prepare_base_query.sql) that requires
     visit_vessel_type IN ('TUG', 'BUNKER') and start_timestamp IS NOT NULL only.
  
  2. Batch time range filter: AND pv.end_timestamp > %(start)s applied unconditionally
     to all vessel types. For TUG records with no end_timestamp, NULL > start evaluates
     to NULL (falsy), excluding every open-ended TUG visit. Made the lower-bound check
     conditional: for TUG/BUNKER, AND (pv.end_timestamp > %(start)s OR pv.end_timestamp IS NULL).
- `731a6c08` **Panji Y. Wiwaha** (2026-09-08): fix(sof): extend DML fact templates to handle TUG/BUNKER vessel type correctly
  All 19 DML SQL fact templates now carry three TUG/BUNKER-aware changes:
  
  1. `is_tug_bunker` variable — `{% set is_tug_bunker = vessel_type in ('TUG', 'BUNKER') %}` at the top of every template so TUG/BUNKER records are never mis-routed into the SEA_VESSEL branch.
  
  2. Vessel type filter — added `{% elif is_tug_bunker %}` branch requiring `start_timestamp IS NOT null` and `visit_vessel_type IN ('TUG', 'BUNKER')` but NOT `end_timestamp IS NOT null`, since open-ended TUG visits carry a NULL end. Templates whose unconditional WHERE previously required `end_timestamp IS NOT null` have that guard moved into the SEA_VESSEL else-branch only.
  
  3. Time range lower bound — the `end_timestamp > %(start)s` (or `> '{{ params.start }}'`) filter is now wrapped in `{% if is_tug_bunker %}…OR end_timestamp IS null{% else %}…{% endif %}` so open-ended TUG visits are not silently dropped when `NULL > start` evaluates to NULL.
  
  Pilot encounter/selected prepare files use the simpler guard change: `not is_barge` → `not is_barge and not is_tug_bunker`, since those templates have no batch time range section.
- `fa334d05` **Panji Y. Wiwaha** (2026-09-08): fix(qc): extend QC DML templates to handle TUG/BUNKER vessel type
- `0c0708c9` **Panji Y. Wiwaha** (2026-09-09): feat(qc): wire TUG/BUNKER vessel types into QC DAG pipeline
  Add TUG_VISIT, BUNKER_VISIT, VESSEL_OPERATION__TUG, and VESSEL_OPERATION__BUNKER
  domain constants to Domain model, extend get_vessel_type_from_domain to map them
  to VesselType.TUG/BUNKER, and add TUG/BUNKER task groups to the accuracy,
  completeness, and validity QC DAGs so they are checked when the QC pipeline is
  triggered from start_etl_pipeline.
- `ef818965` **Panji Y. Wiwaha** (2026-09-09): fix(qc): scope TUG/BUNKER vessel_type filter to exact match in QC templates
  Replace IN ('TUG', 'BUNKER') with = '{{ vessel_type }}' in all 38 QC accuracy
  and completeness SQL templates. Previously, any TUG run would include BUNKER
  records in its dataset (and vice versa), producing combined/mislabeled reports
  for both the TUG and BUNKER task groups. The exact-match filter ensures each
  domain group evaluates only its own vessel type population.
- `c7cefa73` **Panji Y. Wiwaha** (2026-09-09): fix(sof): guard post-processing queries against NULL end_timestamp for TUG/BUNKER
  add_berths_summary, add_terminals_summary, and add_zero_fill_to_null_duration all
  scoped their batch UPDATE targets with end_timestamp > %(start)s. For TUG visits
  with no end_timestamp that evaluates to NULL (falsy), silently skipping those rows
  and leaving their derived summary and duration fields unset after insertion.
  
  Read vessel_type from params in each template and apply the same
  is_tug_bunker conditional guard used in the main DML templates:
    TUG/BUNKER: AND (end_timestamp > %(start)s OR end_timestamp IS null)
    others:     AND end_timestamp > %(start)s
- `88694bcb` **Panji Y. Wiwaha** (2026-09-09): fix(sof): guard hard_delete batch scope against NULL end_timestamp for TUG/BUNKER
  The batch DELETE in tug, anchor, bunkering, pilot, and ship_to_ship hard_delete
  templates scopes its target visit_ids via a subquery on fact_port_visit with
  end_timestamp > %(start)s. For TUG visits with no end_timestamp that evaluates
  to NULL, silently excluding those port_visit rows from the subquery and leaving
  any stale fact rows undeleted when source ODS records disappear on a later run.
  
  Add is_tug_bunker to each template and apply the same NULL guard used elsewhere:
    TUG/BUNKER: AND (end_timestamp > %(start)s OR end_timestamp IS null)
    others:     AND end_timestamp > %(start)s
- `b4bdf16d` **Panji Y. Wiwaha** (2026-09-09): fix(sof): scope DML fact vessel_type filter to exact match
  The {% elif is_tug_bunker %} branches used IN ('TUG', 'BUNKER'), causing
  a TUG DAG run to upsert BUNKER port-visit rows that its paired
  hard_delete (scoped to vessel_type = 'TUG') could never clean up.
  Replaced with = '{{ vessel_type }}' across all 18 DML fact templates so
  each domain run only selects its own vessel type.
- `cee87da3` **Panji Y. Wiwaha** (2026-09-09): fix(linter): resolved sqlfluff LT02 issues

## Reviews

### augmentcode[bot] — COMMENTED (2026-09-08)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F765%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-08)

### 🟡 Changes recommended

The updated bunker-category filter can raise at runtime if `ship` is null/None, and the new per-record vessel_type completion behavior needs a targeted unit test to prevent regressions.

*Once you've addressed the issues Copilot identified, you can request another Copilot review.*

<details>
<summary>Pull request overview</summary>

Enables correct TUG vessel handling in the batch statement-of-fact (SOF) ingestion path by resolving per-record vessel type from raw SOF ship categories, preventing TUGs from being discarded (SEA_VESSEL path) or mis-stamped as BARGE (BARGE path), and ensures the daily fact refresh DAG also refreshes SOF-derived metrics for TUG.

**Changes:**
- Added per-record vessel type resolution (`_resolve_vessel_type`) and applied it in both JSON flattening and Parquet-cache conversion paths.
- Updated completion/validation logic to use the per-record stamped `vessel_type` so re-tagged TUG records aren’t held to SEA_VESSEL completion rules.
- Extended `fact_daily_refresh` to run a `refresh_fact_sof__tug` task group after BARGE.
</details>

<details>
<summary>File summaries</summary>

| File | Description |
| ---- | ----------- |
| teqplay/services/statement_of_fact.py | Resolve and propagate per-record vessel type (TUG) through batch/parquet paths and adjust validation/completion accordingly. |
| teqplay/dags/mart/fact_daily_refresh_dag.py | Adds a TUG SOF refresh task group into the daily refresh chain. |
</details>

<details>
<summary>Review details</summary>

- **Files reviewed:** 2/2 changed files
- **Comments generated:** 3
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/dataflow_dag_core/new/develop?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

### panjiyudasetya — COMMENTED (2026-09-08)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-08)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-08)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-08)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-08)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F765%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### augmentcode[bot] — COMMENTED (2026-09-09)

Review completed. 3 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F765%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-09)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-09)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-09)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-09)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F765%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-09)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-09)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F765%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-09)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-09)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F765%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-09)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-09)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### ryan-kharisma — APPROVED (2026-09-09)

LGTM

## Review Comments

### Copilot — 2026-09-08 on `teqplay/services/statement_of_fact.py`

_is_bunker_vessel assumes data['ship'] is a dict and will raise AttributeError if ship is null/None (json.loads('null') -> None). Since SOFStagingData.from_dict uses data.get('ship'), ship can legitimately be missing; this should be handled defensively here.

### Copilot — 2026-09-08 on `teqplay/services/statement_of_fact.py`

This docstring says TUG records “no longer appear as SEA_VESSEL records here”, but is_sof_valid still takes the SEA_VESSEL branch whenever the service instance is configured as SEA_VESSEL (regardless of per-record vessel_type). Consider rewording to emphasize that records are stamped as TUG and completion logic keys off the per-record vessel_type.

### Copilot — 2026-09-08 on `teqplay/services/statement_of_fact.py`

The updated per-record vessel_type override in _is_sof_completed is important new behavior (e.g., SEA_VESSEL service instance processing a record stamped as TUG should bypass slowMovingPeriods). There’s existing unit coverage for _is_sof_completed, but it doesn’t currently assert this re-tagging scenario.

### panjiyudasetya — 2026-09-08 on `teqplay/services/statement_of_fact.py`

Resolved b8a646e

### panjiyudasetya — 2026-09-08 on `teqplay/services/statement_of_fact.py`

Resolved 7a82a51

### panjiyudasetya — 2026-09-08 on `teqplay/services/statement_of_fact.py`

Resolved 7a82a51

### panjiyudasetya — 2026-09-08 on `teqplay/services/statement_of_fact.py`

Resolved by 7a82a51

### panjiyudasetya — 2026-09-09 on `teqplay/dags/quality/accuracy_dag.py`

Resolved ef81896

### panjiyudasetya — 2026-09-09 on `teqplay/templates/sql/quality_control/completeness/encounter/prepare_ods_encounter_pilot.sql`

Resolved ef81896

### panjiyudasetya — 2026-09-09 on `teqplay/dags/mart/fact_daily_refresh_dag.py`

The TUG and BUNKER vessel type is already added in both schema migration and DDL.

### panjiyudasetya — 2026-09-09 on `teqplay/dags/mart/fact_sof/tug_vessel_dag.py`

Resolved c7cefa7

### panjiyudasetya — 2026-09-09 on `teqplay/dags/mart/fact_sof/tug_vessel_dag.py`

Resolved by 88694bc

### panjiyudasetya — 2026-09-09 on `teqplay/templates/sql/dml/fact/tug/proceed.sql`

Resolved b4bdf16

## Comments

### panjiyudasetya — 2026-09-08

augment review

### panjiyudasetya — 2026-09-09

augment review

### panjiyudasetya — 2026-09-09

augment review

### panjiyudasetya — 2026-09-09

augment review

### panjiyudasetya — 2026-09-09

augment review

### panjiyudasetya — 2026-09-09

augment review

### ryan-kharisma — 2026-09-09

just one insight here: we don't need to proceed this tug and bunker in the fact port visit right? please do remove the related fact port visit for this tug and bunker vessel.

### panjiyudasetya — 2026-09-09

Can we do it on this PR https://github.com/teqplay/dataflow_dag_core/pull/766 @ryan-kharisma?

---
id: github:teqplay/dataflow_dag_core:pr:750
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 750
title: PTO-2967 Eliminate deadlocks on fact tables via lock ordering, pool consolidation,
  and retries
author: panjiyudasetya
state: closed
date: '2026-08-31'
merged_at: '2026-09-01'
base_branch: develop
head_branch: PTO-2967
url: https://github.com/teqplay/dataflow_dag_core/pull/750
labels: []
linked_issues: []
explicit_links: []
---
# PR #750: PTO-2967 Eliminate deadlocks on fact tables via lock ordering, pool consolidation, and retries

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/750  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `develop` ← `PTO-2967`  
**Created:** 2026-08-31  
**Merged:** 2026-09-01  

## Description

### Description

Resolves recurring `40P01: deadlock detected` errors on `fact_daily_refresh`, `fact_sof__stream`, and `fact_operational_events` DAGs caused by three concurrent writer paths competing for row and catalog locks on shared fact tables.

### Root causes

**Scenario A — inconsistent row lock ordering**
Five after-proceed UPDATE statements on `fact_port_visit` each acquired row locks independently and in arbitrary order. When a streaming DAG run and a batch or daily-refresh run processed overlapping visit IDs simultaneously, the transactions locked rows in opposite orders and deadlocked.

**Scenario B — index/heap lock inversion between DELETE and INSERT ON CONFLICT DO UPDATE**
Hard-deletion tasks (`DELETE FROM fact_*`) shared `streaming_sql_pool` while their concurrent writers used `fact_sql_pool`. PostgreSQL acquires index locks in reverse order for DELETE vs INSERT ON CONFLICT, which creates a circular dependency when both operations run concurrently without pool-level serialisation.

**Scenario C — PostgreSQL catalog lock contention on concurrent DDL**
`create_temp_tables` and `drop_temp_tables` operators issue DDL against the same DATA_WAREHOUSE schema from concurrent streaming and batch DAG runs. PostgreSQL serialises catalog modifications with schema-level locks, making simultaneous CREATE TABLE and DROP TABLE statements from different runs prone to catalog-level deadlocks even when they target different prefixed tables.

### Changes

#### Fix 1: consistent row lock ordering (SQL templates)

Added `ORDER BY visit_id FOR UPDATE` to the pre-filter CTE in all five after-proceed UPDATE templates under `teqplay/templates/sql/dml/fact/port_visit/`:

- `add_berths_summary.sql`
- `add_terminals_summary.sql`
- `add_shifting_inside_terminals.sql`
- `add_ship_to_ship_summary.sql`
- `add_zero_fill_to_null_duration.sql` (new `locked_rows` CTE with `ORDER BY visit_id FOR UPDATE`, UPDATE rewritten to join against it)

All three writer paths now lock `fact_port_visit` rows in the same ascending `visit_id` order, making a Scenario A deadlock cycle impossible.

#### Fix 2: pool consolidation for hard-deletion operators

Moved deletion operators from `streaming_sql_pool` to `fact_sql_pool` in `teqplay/tasks/fact/sof/deletion_task_groups.py` for every fact table whose write path uses `INSERT ... ON CONFLICT DO UPDATE`:

- `delete_fact_port_visit`
- `delete_fact_ship_to_ship`
- `delete_fact_berth_visit`
- `delete_fact_terminal_visit`
- `delete_fact_anchor`
- `delete_fact_bunkering`
- `delete_fact_pilot`
- `delete_fact_tug`

`delete_fact_stdev_terminal_time` is intentionally left on `streaming_sql_pool` because `fact_stdev_time_terminal_visit` uses a plain DELETE + INSERT pattern with no ON CONFLICT clause, so Scenario B does not apply.

#### Fix 3: retries as a safety net across all affected operators

Added `retries=2, retry_delay=timedelta(seconds=15)` to absorb any residual transient deadlocks:

**`teqplay/tasks/fact/sof/main_task_groups.py`**
- `proceed` task in all three task groups (`load_fact_berth_visit`, `load_fact_terminal_visit`, `load_fact_port_visit`)
- All five after-proceed operators in `load_fact_port_visit` (`add_berths_summary`, `add_terminals_summary`, `add_shifting_inside_terminals`, `add_ship_to_ship_summary`, `add_zero_fill_to_null_duration`)
- `create_temp_tables`, all `prepare_*` tasks, `drop_temp_tables_success`, and `drop_temp_tables_failure` in all three task groups (Scenario C coverage)

**`teqplay/tasks/fact/operational_events/` (anchor, bunkering, pilot, tug)**
- `merge_delta_to_fact`, `delete_orphaned_visits`, `clear_delta_table` in all four event type task groups

### Files changed

| File | Change |
|---|---|
| `teqplay/templates/sql/dml/fact/port_visit/add_berths_summary.sql` | `ORDER BY visit_id FOR UPDATE` |
| `teqplay/templates/sql/dml/fact/port_visit/add_terminals_summary.sql` | `ORDER BY visit_id FOR UPDATE` |
| `teqplay/templates/sql/dml/fact/port_visit/add_shifting_inside_terminals.sql` | `ORDER BY visit_id FOR UPDATE` |
| `teqplay/templates/sql/dml/fact/port_visit/add_ship_to_ship_summary.sql` | `ORDER BY visit_id FOR UPDATE` |
| `teqplay/templates/sql/dml/fact/port_visit/add_zero_fill_to_null_duration.sql` | New `locked_rows` CTE with `ORDER BY visit_id FOR UPDATE` |
| `teqplay/tasks/fact/sof/deletion_task_groups.py` | 8 operators moved to `fact_sql_pool` |
| `teqplay/tasks/fact/sof/main_task_groups.py` | Retries on proceed, prepare, drop, and after-proceed operators |
| `teqplay/tasks/fact/operational_events/anchor_task_groups.py` | Retries on merge, orphan-delete, clear |
| `teqplay/tasks/fact/operational_events/bunkering_task_groups.py` | Retries on merge, orphan-delete, clear |
| `teqplay/tasks/fact/operational_events/pilot_task_groups.py` | Retries on merge, orphan-delete, clear |
| `teqplay/tasks/fact/operational_events/tug_task_groups.py` | Retries on merge, orphan-delete, clear |

### Test plan

- [ ] Deploy to staging and trigger concurrent `fact_sof__stream` and `fact_transformation` runs for the same port; confirm no `40P01` errors
- [ ] Trigger `fact_daily_refresh` during an active streaming run; confirm completion without deadlock
- [ ] Trigger `fact_operational_events` while hard deletion is in-flight; confirm `merge_delta_to_fact` completes or retries successfully
- [ ] Verify QC DAGs (`fact_qc_*`) are unaffected (no changed imports or shared task group references)
- [ ] Confirm row counts on `fact_port_visit`, `fact_anchor`, `fact_bunkering`, `fact_pilot`, `fact_tug` are stable after concurrent runs

## Commits

- `1268582f` **Panji Y. Wiwaha** (2026-08-31): fix(fact-port-visit): lock rows in consistent visit_id order on all after-proceed UPDATEs
  All five after-proceed UPDATE templates for fact_port_visit now acquire
  row locks via ORDER BY visit_id FOR UPDATE before writing. Templates with
  an existing filtered_port_visits CTE have the clause added there; the
  zero-fill template, which previously had no pre-filter CTE, gains a new
  locked_rows CTE with the same batch/stream scope filter.
  
  This removes the circular-wait condition that caused deadlocks when the
  streaming DAG and batch/daily-refresh writers updated overlapping rows in
  different heap-scan orders — mirroring the fix already applied to
  update_port_visit_outlier_flags.sql (incident 2026-08-15).
- `30ad533e` **Panji Y. Wiwaha** (2026-08-31): fix(fact-port-visit): move delete_fact_port_visit to fact_sql_pool
  The streaming delete stream used streaming_sql_pool while the streaming
  update stream used fact_sql_pool. Because the pools are independent,
  DELETE and INSERT...ON CONFLICT DO UPDATE could run concurrently on
  overlapping visit_ids, causing an index/heap lock inversion deadlock.
  
  Moving only delete_fact_port_visit to fact_sql_pool serialises it with
  all UPDATE writers on that table. The other eight tables in the deletion
  chain remain on streaming_sql_pool as they are not contended.
- `426fcacd` **Panji Y. Wiwaha** (2026-08-31): fix(fact-deletions): move streaming-written table deletions to fact_sql_pool
  fact_ship_to_ship_transfers, fact_berth_visit, and fact_terminal_visit are
  all written by the streaming update stream using fact_sql_pool. Having their
  hard deletes on streaming_sql_pool allowed DELETE and INSERT...ON CONFLICT to
  run concurrently on the same rows, creating the same index/heap lock inversion
  deadlock as was present on fact_port_visit.
  
  Batch-only tables (fact_anchor, fact_bunkering, fact_pilot, fact_tug,
  fact_stdev_time_terminal_visit) remain on streaming_sql_pool — they have no
  high-frequency concurrent writers, so the overlap window with a deletion is
  too small to justify the added serialisation.
- `baceca1c` **Panji Y. Wiwaha** (2026-08-31): fix(fact-deletions): move anchor/bunkering/pilot/tug deletions to fact_sql_pool
  These four tables all use INSERT ... ON CONFLICT (id) DO UPDATE in their
  batch load path, which runs on fact_sql_pool. Having their hard deletes on
  streaming_sql_pool allows DELETE and INSERT ON CONFLICT to run concurrently,
  creating the same index/heap lock inversion deadlock (Scenario B) as the
  streaming-written tables fixed previously.
  
  fact_stdev_time_terminal_visit is intentionally left on streaming_sql_pool —
  its load templates use plain DELETE + INSERT with no ON CONFLICT clause, so
  the lock inversion mechanism does not apply.
- `f20db688` **Panji Y. Wiwaha** (2026-08-31): fix(fact-port-visit): add retries on all fact table writers as deadlock safety net
  PostgreSQL raises 40P01 when it detects and resolves a deadlock by aborting
  one transaction. Adding retries=2, retry_delay=15s on all proceed tasks
  (fact_berth_visit, fact_terminal_visit, fact_port_visit) and the five
  after-proceed UPDATE operators on fact_port_visit means an aborted
  transaction self-recovers rather than failing the DAG.
  
  This is a safety net — Fixes 1 and 2 (consistent lock ordering + pool
  consolidation) eliminate the known deadlock conditions structurally. Retries
  cover any edge case not anticipated by those fixes.
  
  update_port_visit_from_temp already carries retries=2, retry_delay=15s from
  incident 2026-08-15 and is unchanged.
- `1026abcc` **Panji Y. Wiwaha** (2026-09-01): fix(fact-operational-events): add retries to delta merge and cleanup operators
  merge_delta_to_fact (DELETE + INSERT ON CONFLICT), delete_orphaned_visits,
  and clear_delta_table now carry retries=2 / retry_delay=15 s across all four
  event types (anchor, bunkering, pilot, tug).
  
  Deadlock window: concurrent hard-deletion on fact_sql_pool can race the
  DELETE + INSERT ON CONFLICT pattern in merge_delta_to_fact; retries absorb
  transient 40P01 errors without surfacing them as DAG failures.
- `c67dbe50` **Panji Y. Wiwaha** (2026-09-01): fix(fact-sof-stream): add retries to prepare and drop-temp-tables operators
  All create_temp_tables, prepare_*, and drop_temp_tables_success/failure
  operators in load_fact_berth_visit, load_fact_terminal_visit, and
  load_fact_port_visit now carry retries=2 / retry_delay=15 s.
  
  These DATA_WAREHOUSE DDL and DML tasks can deadlock under concurrent
  DAG runs (streaming + batch) due to PostgreSQL catalog-level lock
  contention on the same schema. Retries absorb transient 40P01 errors
  without surfacing them as DAG failures.
- `1c9ed8e8` **Panji Y. Wiwaha** (2026-09-01): fix(fact-deletions): lock rows in ascending id order before hard delete to prevent index/heap inversion
  All eight hard_delete.sql templates now wrap their DELETE in a subquery
  that pre-locks the target rows in ascending id order using FOR UPDATE:
  
      DELETE FROM fact_x
      WHERE id IN (
          SELECT id FROM fact_x
          WHERE <filter>
          ORDER BY id
          FOR UPDATE
      );
  
  PostgreSQL's INSERT ... ON CONFLICT DO UPDATE scans the unique index
  (ascending key order) and then locks the heap tuple. Without this fix,
  a concurrent DELETE locks the heap tuple first, then removes the index
  entry, creating a circular lock dependency (index/heap inversion) that
  causes 40P01 errors. Pre-locking in the same ascending order as the
  index eliminates the cycle.
  
  Sharing fact_sql_pool limits total concurrent fact-table DB operations
  (resource management) but does not serialize tasks unless slots=1, so
  the pool assignment alone cannot prevent the inversion. Updated pool
  comments to reflect this accurately.
  
  Affected tables: fact_port_visit, fact_berth_visit, fact_terminal_visit,
  fact_ship_to_ship_transfers, fact_anchor, fact_bunkering, fact_pilot, fact_tug.
- `8a294359` **Panji Y. Wiwaha** (2026-09-01): fix(fact-deletions): use correct ON CONFLICT column in hard_delete lock-ordering subqueries
  The previous commit used `id` as the ordering column in the FOR UPDATE
  subquery for fact_port_visit, fact_berth_visit, and fact_terminal_visit.
  These tables do not have an `id` column as the ON CONFLICT target:
  
    fact_port_visit       -> ON CONFLICT (visit_id)
    fact_berth_visit      -> ON CONFLICT (berth_visit_id)
    fact_terminal_visit   -> ON CONFLICT (terminal_visit_id)
  
  Using the wrong column would cause "column does not exist" errors for
  berth_visit and terminal_visit, and would lock in the wrong order for
  port_visit (mis-aligning with the unique index INSERT ON CONFLICT scans).
  
  Each template now selects and orders by the same column the INSERT ON
  CONFLICT index scan uses, so lock acquisition order is consistent and
  the circular dependency cannot form.

## Reviews

### augmentcode[bot] — COMMENTED (2026-09-01)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F750%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-01)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-01)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F750%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<details>
<summary><b>Items Reviewed</b></summary>

- ✅ Current Task List
</details>


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-01)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-01)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### ryan-kharisma — APPROVED (2026-09-01)

LGTM

## Review Comments

### panjiyudasetya — 2026-09-01 on `teqplay/tasks/fact/sof/deletion_task_groups.py`

Addressed by ddddc12

### panjiyudasetya — 2026-09-01 on `teqplay/templates/sql/dml/fact/berth_visit/hard_delete.sql`

Resolved by 8a29435

## Comments

### panjiyudasetya — 2026-09-01

augment review

### panjiyudasetya — 2026-09-01

augment review

### panjiyudasetya — 2026-09-01

augment review

### panjiyudasetya — 2026-09-01

Tested locally, it's all good, @ryan-kharisma.

<img width="2672" height="1461" alt="image" src="https://github.com/user-attachments/assets/f7acbb35-8715-48a3-b06b-c71fd77fe114" />
<img width="2672" height="1461" alt="image" src="https://github.com/user-attachments/assets/ac2d8aac-bce6-4d2b-aec8-117199f48faa" />


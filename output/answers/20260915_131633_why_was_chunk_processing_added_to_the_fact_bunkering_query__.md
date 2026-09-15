# Why was chunk-processing added to the fact_bunkering query, and what was slow about the original approach?

## Summary

PR #730 ("PTO-2866 Fix slow `fact_bunkering` query and add chunk-processing logs") did **not** introduce chunk-processing itself — chunk processing already existed via the `process_data_in_chunks` helper in `teqplay/tasks/fact/sof/utils.py`. What the PR added was **logging around that existing chunk-processing path**, plus the actual performance fix: adding the missing `deleted_timestamp IS null` predicate so Postgres could use the pre-existing partial indexes instead of full sequential scans (github:teqplay/dataflow_dag_core:pr:730).

## Decisions made

- **Add `deleted_timestamp IS null` to the `ods_encounter`, `ods_berth_visit`, and `ods_terminal_visit` joins in `proceed.sql`** → the partial indexes `idx_encounter_bunkering`, `idx_berth_visit_overlap`, `idx_terminal_visit_overlap` were built *with that predicate*; without it in the query the planner could not prove the index applied and fell back to sequential scans (github:teqplay/dataflow_dag_core:pr:730).
- **Match the predicate already present in `fdw_proceed.sql`** → the correct form already existed elsewhere, so this was aligning `proceed.sql` with the known-good version rather than inventing a new approach (github:teqplay/dataflow_dag_core:pr:730).
- **Apply the identical fix to `quality_control/accuracy/bunkering/bunkering_components.sql`** → that template reconstructs the same `fact_bunkering` shape from ODS tables; keeping it in sync prevents the QC query from silently diverging from the fact-table logic it validates, and from being slow for the same reason (github:teqplay/dataflow_dag_core:pr:730).
- **Add logging inside `process_data_in_chunks` (executed query, total available records, a checkpoint after `cursor.execute()` returns, and chunk progress)** → to make stalled DAG runs diagnosable; this is what allowed the team to determine that a previous "stuck" run was actually a slow query stalled inside the first `fetchmany()`, not a hang on the mart insert (github:teqplay/dataflow_dag_core:pr:730, commit `f731fef4`).

## Rationale

The visible symptom was a `load_fact_bunkering` task that appeared to hang. Because the chunk-processing loop emitted no intermediate output, there was no way to tell whether the task was blocked on the source query or on the downstream mart insert — hence the decision to instrument `process_data_in_chunks` with the query text, a post-`execute()` checkpoint, and per-chunk progress lines. Once instrumented, the stall was localised to the first `fetchmany()`, i.e. to the source query itself (github:teqplay/dataflow_dag_core:pr:730).

The root cause of the slowness was a query/index mismatch rather than data volume. The relevant ODS tables carry *partial* indexes defined with the `deleted_timestamp IS null` predicate. `proceed.sql` omitted that predicate on the three joins, so Postgres could not match the query to the partial indexes and performed full sequential scans: `EXPLAIN ANALYZE` showed roughly **27 seconds spent scanning ~1.3M+ rows to return a 459-row result** (github:teqplay/dataflow_dag_core:pr:730, commit `f731fef4`). Re-adding the predicate — which `fdw_proceed.sql` already had — restores index usage without changing the result set. The QC accuracy template was updated in the same commit specifically to avoid drift between the fact logic and the query that checks it. The author validated the fix by running Airflow locally against the production database (ESALG, Jun 1 – Jul 1 2026) and reported no further "stuck" bunkering fact processing (github:teqplay/dataflow_dag_core:pr:730, comment 2026-07-24). The change shipped in release 1.54.1 (github:teqplay/dataflow_dag_core:pr:731).

## Supporting evidence

- `github:teqplay/dataflow_dag_core:pr:730` — the PR itself: description, root cause, EXPLAIN ANALYZE numbers, commit `f731fef4`, test plan, and the author's local verification comment.
- `github:teqplay/dataflow_dag_core:pr:731` — Release 1.54.1 to develop; confirms `f731fef4` and the merge of #730 shipped in 1.54.1.
- `github:teqplay/dataflow_dag_core:pr:734` — later `fact_bunkering` work (PTO-2867, adding location columns), showing `proceed.sql` / `fdw_proceed.sql` / `proceed_delta.sql` are the templates behind this fact table.
- `github:teqplay/dataflow_dag_core:pr:750` — notes `fact_bunkering` is a batch-only table, useful context for why chunked batch loading applies here.

## Gaps

- **The premise needs correcting**: the evidence does not show chunk-processing being *added*. `process_data_in_chunks` already existed; only logging was added to it. No document explains when or why chunked processing was originally introduced, or what chunk size / `fetchmany` sizing is used.
- **No JIRA ticket PTO-2866 is present** in the evidence, so the original bug report, business impact, and any SLA/timeout constraints are unknown.
- **No post-fix `EXPLAIN ANALYZE` output** is included — the test plan items are unchecked checkboxes, so the confirmed post-fix query time and whether index scans were verified is not documented (only the author's qualitative "no longer see any stuck processing").
- **No review approvals or reviewer discussion** on #730 appear in the evidence beyond the author's own comment addressed to @ryan-kharisma.
- It is unclear whether `proceed_delta.sql` (the delta variant, referenced in pr:734) had the same missing predicate; the PR only mentions `proceed.sql` and the QC template.
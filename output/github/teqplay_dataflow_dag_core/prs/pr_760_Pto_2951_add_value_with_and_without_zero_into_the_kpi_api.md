---
id: github:teqplay/dataflow_dag_core:pr:760
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 760
title: Pto 2951 add value with and without zero into the kpi api
author: ryan-kharisma
state: closed
date: '2026-09-07'
merged_at: '2026-09-10'
base_branch: develop
head_branch: PTO-2951_Add_Value_With_and_Without_Zero_into_the_KPI_API
url: https://github.com/teqplay/dataflow_dag_core/pull/760
labels: []
linked_issues: []
explicit_links: []
---
# PR #760: Pto 2951 add value with and without zero into the kpi api

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/760  
**State:** closed | **Author:** ryan-kharisma  
**Base ← Head:** `develop` ← `PTO-2951_Add_Value_With_and_Without_Zero_into_the_KPI_API`  
**Created:** 2026-09-07  
**Merged:** 2026-09-10  

## Description

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<body><h2 aria-level="5" style="unicode-bidi: plaintext; margin-top: 0px; color: rgb(191, 191, 191); font-family: -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, Roboto, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(25, 26, 27); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">Branch:<span> </span><code style="font-family: monospace; color: rgb(140, 140, 140); background-color: rgb(38, 38, 38); padding: 2px 4px; border-radius: 3px; word-break: break-word; font-size: 0.9em;">PTO-2951_Add_Value_With_and_Without_Zero_into_the_KPI_API</code></h2><p style="white-space: pre-wrap; margin-top: 0.1em; margin-bottom: 0.2em; unicode-bidi: plaintext; color: rgb(191, 191, 191); font-family: -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, Roboto, sans-serif; font-size: 13px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(25, 26, 27); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">Adds a parallel set of <strong><code style="font-family: monospace; color: rgb(140, 140, 140); background-color: rgb(38, 38, 38); padding: 2px 4px; border-radius: 3px; word-break: break-word; font-size: 0.9em;">all_</code> metrics</strong> to 7 of the 9 KPI gold tables, so each existing average/count (which silently excludes zero-duration, ongoing, or missing-timestamp events) gets a companion metric that <em>includes</em> them — without changing the existing metric's value or meaning. <code style="font-family: monospace; color: rgb(140, 140, 140); background-color: rgb(38, 38, 38); padding: 2px 4px; border-radius: 3px; word-break: break-word; font-size: 0.9em;">bunkering_weekly</code> and <code style="font-family: monospace; color: rgb(140, 140, 140); background-color: rgb(38, 38, 38); padding: 2px 4px; border-radius: 3px; word-break: break-word; font-size: 0.9em;">terminal_sailing_duration_monthly</code> were audited and confirmed to need no change (their "excluded" rows are structurally non-applicable, not unmeasured real events).</p>


<p class="p1"><b>Fields + formula, per KPI</b></p>

KPI | New fields | Formula | What gets included that wasn't before
-- | -- | -- | --
kpi_anchorage_duration_monthly | all_avg_duration, all_anchorage_count | all_avg_duration = total / all_anchorage_count | zero-duration events + ongoing (not-yet-departed) anchorages (0h)
kpi_berth_occupancy_monthly | all_visits_count, all_avg_mooring_hours_per_visit | all_avg = jetty_occupied_hours / all_visits_count | visits with no recorded mooring timestamps
kpi_terminal_occupancy_monthly | all_visits_count, all_vessels_served_count, all_avg_vessel_exchange_hours | all_avg_vessel_exchange_hours = total_vessel_exchange_hours / exchange_count (vs. /vessel_exchange_count) | same missing-mooring visits; exchange pairs with no valid operational timestamps
kpi_overall_port_performance_monthly | all_port_visit_count, all_avg_portcall_duration, all_avg_vessel_exchange_hours | all_avg_portcall_duration = all_total_portcall_duration / all_port_visit_count | zero-duration visit-months; same exchange-pair case
kpi_portcall_performance_monthly | all_port_visit_count, all_avg_total_duration_per_visit | same pattern, shares silver source with the KPI above | zero-duration visit-months
kpi_berth_stay_duration_monthly | all_berth_visit_count, all_vessels_served_count, all_avg_berth_stay_per_visit | all_avg = total_berth_stay_hours / all_berth_visit_count | zero-duration visits + ongoing (not-yet-departed) visits
kpi_portcall_duration_monthly | all_port_visit_count, all_avg_tat_per_visit | all_avg_tat_per_visit = turn_around_time_duration / all_port_visit_count | ongoing (not-yet-departed) port visits only (no zero-duration case existed here)


<p class="p3">Every "excluded" row is invisible to the <i>original</i> metric, so existing values/behavior are unchanged. Also fixed 2 latent NULL-into-NOT NULL bugs (a FILTER'd SUM() returns NULL when a group has zero matching rows) in berth_stay_duration_monthly and portcall_performance_monthly.</p>
</body>


<p style="white-space: pre-wrap; margin-top: 0.1em; margin-bottom: 0.2em; unicode-bidi: plaintext; color: rgb(191, 191, 191); font-family: -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, Roboto, sans-serif; font-size: 13px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(25, 26, 27); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">Every "excluded" row is invisible to the <em>original</em> metric, so existing values/behavior are unchanged. Also fixed 2 latent <code style="font-family: monospace; color: rgb(140, 140, 140); background-color: rgb(38, 38, 38); padding: 2px 4px; border-radius: 3px; word-break: break-word; font-size: 0.9em;">NULL</code>-into-<code style="font-family: monospace; color: rgb(140, 140, 140); background-color: rgb(38, 38, 38); padding: 2px 4px; border-radius: 3px; word-break: break-word; font-size: 0.9em;">NOT NULL</code> bugs (a <code style="font-family: monospace; color: rgb(140, 140, 140); background-color: rgb(38, 38, 38); padding: 2px 4px; border-radius: 3px; word-break: break-word; font-size: 0.9em;">FILTER</code>'d <code style="font-family: monospace; color: rgb(140, 140, 140); background-color: rgb(38, 38, 38); padding: 2px 4px; border-radius: 3px; word-break: break-word; font-size: 0.9em;">SUM()</code> returns <code style="font-family: monospace; color: rgb(140, 140, 140); background-color: rgb(38, 38, 38); padding: 2px 4px; border-radius: 3px; word-break: break-word; font-size: 0.9em;">NULL</code> when a group has zero matching rows) in <code style="font-family: monospace; color: rgb(140, 140, 140); background-color: rgb(38, 38, 38); padding: 2px 4px; border-radius: 3px; word-break: break-word; font-size: 0.9em;">berth_stay_duration_monthly</code> and <code style="font-family: monospace; color: rgb(140, 140, 140); background-color: rgb(38, 38, 38); padding: 2px 4px; border-radius: 3px; word-break: break-word; font-size: 0.9em;">portcall_performance_monthly</code>.</p><h3 aria-level="6" style="unicode-bidi: plaintext; color: rgb(191, 191, 191); font-family: -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, Roboto, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(25, 26, 27); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">How to test</h3><ol style="padding-inline-start: 2em; color: rgb(191, 191, 191); font-family: -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, Roboto, sans-serif; font-size: 13px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(25, 26, 27); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><li style="unicode-bidi: plaintext;"><strong>Migrations</strong>: trigger<span> </span><code style="font-family: monospace; color: rgb(140, 140, 140); background-color: rgb(38, 38, 38); padding: 2px 4px; border-radius: 3px; word-break: break-word; font-size: 0.9em;">prepare_database</code><span> </span>(existing deployment mode) — this runs<span> </span><code style="font-family: monospace; color: rgb(140, 140, 140); background-color: rgb(38, 38, 38); padding: 2px 4px; border-radius: 3px; word-break: break-word; font-size: 0.9em;">run_kpi_migrations()</code>, which drops+recreates the 4 affected silver materialized views (column list changes require drop+recreate, not<span> </span><code style="font-family: monospace; color: rgb(140, 140, 140); background-color: rgb(38, 38, 38); padding: 2px 4px; border-radius: 3px; word-break: break-word; font-size: 0.9em;">ALTER</code>) and<span> </span><code style="font-family: monospace; color: rgb(140, 140, 140); background-color: rgb(38, 38, 38); padding: 2px 4px; border-radius: 3px; word-break: break-word; font-size: 0.9em;">ALTER TABLE</code>s the 7 gold tables.</li><li style="unicode-bidi: plaintext;"><strong>Refresh</strong>: trigger<span> </span><code style="font-family: monospace; color: rgb(140, 140, 140); background-color: rgb(38, 38, 38); padding: 2px 4px; border-radius: 3px; word-break: break-word; font-size: 0.9em;">silver__enriched_monthly_refresh</code><span> </span>(views are empty after the drop), then<span> </span><code style="font-family: monospace; color: rgb(140, 140, 140); background-color: rgb(38, 38, 38); padding: 2px 4px; border-radius: 3px; word-break: break-word; font-size: 0.9em;">gold__kpi_monthly_refresh</code>.</li><li style="unicode-bidi: plaintext;"><strong>Verify</strong><span> </span>per KPI — the invariant<span> </span><code style="font-family: monospace; color: rgb(140, 140, 140); background-color: rgb(38, 38, 38); padding: 2px 4px; border-radius: 3px; word-break: break-word; font-size: 0.9em;">all_X &gt;= X</code><span> </span>must hold on every row, and<span> </span><code style="font-family: monospace; color: rgb(140, 140, 140); background-color: rgb(38, 38, 38); padding: 2px 4px; border-radius: 3px; word-break: break-word; font-size: 0.9em;">all_X &gt; X</code><span> </span>on at least some rows if the port has zero-duration/ongoing/missing-timestamp data:<div class="codeBlockWrapper_-a7MRw" style="position: relative; margin: 8px 0px;"><button class="copyButton_CEmTFw copyButton_-a7MRw" title="Copy code" aria-label="Copy code to clipboard" style="color: rgb(191, 191, 191); font-family: -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, Roboto, sans-serif; font-size: 13px; background: none 0% 0% / auto repeat scroll padding-box border-box rgb(18, 19, 20); border-color: rgb(42, 43, 44); border-style: solid; border-width: 1px; border-image: none 100% / 1 / 0 stretch; cursor: pointer; opacity: 0; display: flex; border-radius: 4px; justify-content: center; align-items: center; padding: 4px; transition: opacity 0.15s, background 0.15s; position: absolute; top: 4px; right: 4px;"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true" data-slot="icon" class="copyIcon_CEmTFw"><path fill-rule="evenodd" d="M15.988 3.012A2.25 2.25 0 0 1 18 5.25v6.5A2.25 2.25 0 0 1 15.75 14H13.5v-3.379a3 3 0 0 0-.879-2.121l-3.12-3.121a3 3 0 0 0-1.402-.791 2.252 2.252 0 0 1 1.913-1.576A2.25 2.25 0 0 1 12.25 1h1.5a2.25 2.25 0 0 1 2.238 2.012ZM11.5 3.25a.75.75 0 0 1 .75-.75h1.5a.75.75 0 0 1 .75.75v.25h-3v-.25Z" clip-rule="evenodd"></path><path d="M3.5 6A1.5 1.5 0 0 0 2 7.5v9A1.5 1.5 0 0 0 3.5 18h7a1.5 1.5 0 0 0 1.5-1.5v-5.879a1.5 1.5 0 0 0-.44-1.06L8.44 6.439A1.5 1.5 0 0 0 7.378 6H3.5Z"></path></svg></button><pre style="overflow-x: auto; white-space: pre; box-sizing: border-box; border-radius: 4px; max-width: 100%; margin: 0px; padding: 8px;"><code class="language-sql" style="font-family: monospace; color: rgb(140, 140, 140); background-color: rgb(38, 38, 38); padding: 0px; border-radius: 3px; word-break: break-word; font-size: 0.9em;">SELECT count(*) AS rows,
       count(*) FILTER (WHERE &lt;count_col&gt; &lt;&gt; all_&lt;count_col&gt;) AS diff,
       count(*) FILTER (WHERE all_&lt;count_col&gt; &lt; &lt;count_col&gt;) AS violations  -- must be 0
FROM gold.kpi_&lt;name&gt; WHERE port_unlocode = 'NLRTM';
</code></pre></div></li>
</body></html>

## Commits

- `2228aa4f` **ryan_at_teqplay** (2026-09-03): feat(kpi-anchorage-duration): add all_avg_duration/all_anchorage_count metrics
  Silver enriched view now keeps zero-duration anchorage events instead of
  discarding them, exposing all_avg_duration/all_anchorage_count alongside the
  existing (zero-duration-excluding) metrics. Gold table, DML, QC checks, and
  metric registry updated to match; event-centric filter now gates on
  all_anchorage_count so months with only zero-duration events still get a row.
  Adds migrations for existing deployments (gold ALTER, silver MV drop+recreate).
  
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `730a0909` **ryan_at_teqplay** (2026-09-04): fix all avg in anchorage duration monthly
- `e4279ff8` **ryan_at_teqplay** (2026-09-04): anchorage silver view now counts ongoing (not-yet-departed) events too
- `f425bc51` **ryan_at_teqplay** (2026-09-04): add all_avg_mooring_hours_per_visit/all_visits_count for berth occupancy monthly
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `b2796a23` **ryan_at_teqplay** (2026-09-07): add all_visits_count/all_vessels_served_count/all_avg_vessel_exchange_hours for terminal occupancy monthly
  Reuses the existing has_mooring_data flag and the exchange_count/vessel_exchange_count
  pair already carried by the two source silver views - no Silver DDL changes needed.
  
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `250b17ca` **ryan_at_teqplay** (2026-09-07): add all_avg_portcall_duration/all_port_visit_count/all_avg_vessel_exchange_hours for overall port performance monthly
  Relaxes the silver safety-guard filter (total_portcall_duration > 0) via FILTER instead of
  a blanket WHERE, so zero-duration visit-months can feed all_total_portcall_duration/
  all_port_visit_count in silver.enriched_portcall_performance_monthly without changing the
  existing (filtered) columns' values. Also shared by kpi_portcall_performance_monthly.
  
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `6030b0ee` **ryan_at_teqplay** (2026-09-07): add all_port_visit_count/all_avg_total_duration_per_visit for portcall performance monthly
  Gold-only: silver.enriched_portcall_performance_monthly's all_total_portcall_duration/
  all_port_visit_count columns were already added for kpi_overall_port_performance_monthly.
  Also fixes a NULL-into-NOT-NULL risk: the silver layer's FILTERed SUM() returns NULL (not
  0) for a port/ship_type/vessel_type/month cell where every visit was zero-duration, so the
  7 duration sum columns are now COALESCEd before insert.
  
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `cf13c45f` **ryan_at_teqplay** (2026-09-07): add all_avg_berth_stay_per_visit/all_berth_visit_count/all_vessels_served_count for berth stay duration monthly
  Adds has_stay_data to silver.enriched_berth_visit_monthly_stay: folds in zero-duration
  completed visits (end_timestamp = start_timestamp) and ongoing visits (start_timestamp set,
  end_timestamp still NULL, single row at start month) so they can be counted in the new
  all_ metrics without affecting the existing ones. Also fixes the same NULL-into-NOT-NULL
  risk found in portcall_performance_monthly (COALESCE on the 4 FILTERed duration sums), and
  updates qc_event_centric_validation to gate on all_berth_visit_count instead of
  berth_visit_count so legitimate all-ongoing/zero-duration groups don't false-positive.
  
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `963efa92` **ryan_at_teqplay** (2026-09-07): add all_port_visit_count/all_avg_tat_per_visit for portcall duration monthly
  Adds all_port_visit_count to silver.enriched_portcall_duration_monthly by folding in
  ongoing port visits (eos_entry_timestamp set, eos_exit_timestamp still NULL) as a single
  zero-contribution row per visit at its entry month, counted via has_completed_visit.
  Duration sums stay unconditional (ongoing visits hardcode 0), so no NULL-safety gap here
  unlike berth_stay/portcall_performance. Also updates qc_event_centric_validation to gate
  on all_port_visit_count instead of port_visit_count so legitimate all-ongoing groups
  don't false-positive.
  
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `21579566` **ryan_at_teqplay** (2026-09-07): wire the 5 new KPI all_ metric migrations into run_kpi_migrations()
  Adds migration steps for terminal_occupancy_monthly (gold-only), overall_port_performance_monthly
  + portcall_performance_monthly (shared silver.enriched_portcall_performance_monthly drop+recreate),
  berth_stay_duration_monthly, and portcall_duration_monthly, chained in run_kpi_migrations() so
  existing deployments pick these up via prepare_database.
  
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `21f71422` **ryan_at_teqplay** (2026-09-07): fix linter sqlfluff
- `afb64583` **Ryan Kharisma Rakhmat** (2026-09-09): Potential fix for pull request finding in silver enriched berth visit
  Co-authored-by: Copilot Autofix powered by AI <175728472+Copilot@users.noreply.github.com>
- `5c12a9d7` **Ryan Kharisma Rakhmat** (2026-09-09): Potential fix for pull request finding in mooring fields
  Co-authored-by: Copilot Autofix powered by AI <175728472+Copilot@users.noreply.github.com>
- `f292a89d` **ryan_at_teqplay** (2026-09-09): fix zero-duration events dropped at month boundary in all_* metrics
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `518c9ca5` **ryan_at_teqplay** (2026-09-09): fix dropped ongoing visits, null ship_type, and exchange-hours denominator in all_* metrics
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `37fdbd69` **ryan_at_teqplay** (2026-09-09): fix null ship_type reaching NOT NULL PK in portcall performance view
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `8160e0a2` **ryan_at_teqplay** (2026-09-09): wire berth_exchange_monthly migration and fix null exchange month attribution
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>

## Reviews

### augmentcode[bot] — COMMENTED (2026-09-07)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F760%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-07)

### 🟡 Changes recommended

The Silver logic intended to include zero-duration events has confirmed edge cases that still drop some zero-duration rows (notably at month boundaries), which can make the new `all_*` metrics incorrect.

*Once you've addressed the issues Copilot identified, you can request another Copilot review.*

<details>
<summary>Pull request overview</summary>

This PR extends the KPI “gold” tables and API-facing metric registry with a parallel set of `all_*` metrics that include previously excluded rows (zero-duration events, ongoing events, and/or missing-timestamp events) while preserving existing metric semantics. It also adds migration steps to evolve existing deployments by dropping/recreating affected Silver materialized views and adding new Gold columns.

**Changes:**
- Add “all_*” companion count/average fields across multiple Gold KPI tables, sourced from updated Silver enriched materialized views.
- Update Silver enriched MVs to retain/represent previously excluded events via flags (e.g., `has_mooring_data`, `has_stay_data`) and additional “all” aggregates.
- Wire schema migrations into `run_kpi_migrations()` and register the new metrics in the metric registry task groups.
</details>

<details>
<summary>File summaries</summary>

| File | Description |
| ---- | ----------- |
| teqplay/templates/sql/migration/kpi/silver/portcall_performance_monthly/schema_migration.sql | Drops stale Silver MV so it can be recreated with new `all_*` columns. |
| teqplay/templates/sql/migration/kpi/silver/portcall_duration_monthly/schema_migration.sql | Drops stale Silver MV so it can be recreated with new `all_port_visit_count`. |
| teqplay/templates/sql/migration/kpi/silver/berth_visit_monthly_stay/schema_migration.sql | Drops stale Silver MV so it can be recreated with `has_stay_data` and new rows. |
| teqplay/templates/sql/migration/kpi/silver/berth_visit_monthly_mooring/schema_migration.sql | Drops stale Silver MV so it can be recreated with `has_mooring_data` and new rows. |
| teqplay/templates/sql/migration/kpi/silver/anchorage_duration_monthly/schema_migration.sql | Drops stale Silver MV so it can be recreated with `all_*` anchorage metrics. |
| teqplay/templates/sql/migration/kpi/gold/terminal_occupancy_monthly/schema_migration.sql | Adds `all_*` columns to the Gold terminal occupancy KPI table plus updated column comments. |
| teqplay/templates/sql/migration/kpi/gold/portcall_performance_monthly/schema_migration.sql | Adds `all_*` columns to the Gold portcall performance KPI table plus updated column comments. |
| teqplay/templates/sql/migration/kpi/gold/portcall_duration_monthly/schema_migration.sql | Adds `all_*` columns to the Gold portcall duration KPI table plus updated column comments. |
| teqplay/templates/sql/migration/kpi/gold/overall_port_performance_monthly/schema_migration.sql | Adds `all_*` columns to the Gold overall port performance KPI table plus updated column comments. |
| teqplay/templates/sql/migration/kpi/gold/berth_stay_duration_monthly/schema_migration.sql | Adds `all_*` columns to the Gold berth stay KPI table plus updated column comments. |
| teqplay/templates/sql/migration/kpi/gold/berth_occupancy_monthly/schema_migration.sql | Adds new averages and `all_*` counts/averages to the Gold berth occupancy KPI table. |
| teqplay/templates/sql/migration/kpi/gold/anchorage_duration_monthly/schema_migration.sql | Adds `all_*` anchorage metrics columns to the Gold anchorage KPI table. |
| teqplay/templates/sql/dml/kpi/terminal_occupancy_monthly/load_kpi.sql | Computes and inserts the new `all_*` terminal occupancy fields. |
| teqplay/templates/sql/dml/kpi/portcall_performance_monthly/load_kpi.sql | Computes and inserts `all_*` portcall performance fields and guards NULL sums. |
| teqplay/templates/sql/dml/kpi/portcall_duration_monthly/load_kpi.sql | Computes and inserts `all_*` portcall duration fields. |
| teqplay/templates/sql/dml/kpi/overall_port_performance_monthly/load_kpi.sql | Computes and inserts `all_*` overall port performance fields and filters quay denominators. |
| teqplay/templates/sql/dml/kpi/berth_stay_duration_monthly/load_kpi.sql | Adds `has_stay_data`-filtered “old” metrics and unfiltered `all_*` metrics. |
| teqplay/templates/sql/dml/kpi/berth_occupancy_monthly/load_kpi.sql | Adds `has_mooring_data`-filtered “old” counts and new `avg_*` / `all_*` metrics. |
| teqplay/templates/sql/dml/kpi/anchorage_duration_monthly/load_kpi.sql | Switches event-centric gating to `all_anchorage_count` and inserts `all_*` fields. |
| teqplay/templates/sql/ddl/kpi/silver/enriched_portcall_performance_monthly.sql | Adds `all_total_portcall_duration` / `all_port_visit_count` alongside filtered prior metrics. |
| teqplay/templates/sql/ddl/kpi/silver/enriched_portcall_duration_monthly.sql | Adds ongoing visit representation and `all_port_visit_count`. |
| teqplay/templates/sql/ddl/kpi/silver/enriched_berth_visit_monthly_stay.sql | Adds `has_stay_data` and includes zero-duration/ongoing visits for `all_*` denominators. |
| teqplay/templates/sql/ddl/kpi/silver/enriched_berth_visit_monthly_mooring.sql | Adds `has_mooring_data` and includes missing-mooring visits for `all_*` denominators. |
| teqplay/templates/sql/ddl/kpi/silver/enriched_anchorage_duration_monthly.sql | Adds `all_*` anchorage aggregates and ongoing anchorage representation. |
| teqplay/templates/sql/ddl/kpi/gold/kpi_terminal_occupancy_monthly.sql | Adds `all_*` columns and documentation to the Gold terminal occupancy table DDL. |
| teqplay/templates/sql/ddl/kpi/gold/kpi_portcall_performance_monthly.sql | Adds `all_*` columns and documentation to the Gold portcall performance table DDL. |
| teqplay/templates/sql/ddl/kpi/gold/kpi_portcall_duration_monthly.sql | Adds `all_*` columns and documentation to the Gold portcall duration table DDL. |
| teqplay/templates/sql/ddl/kpi/gold/kpi_overall_port_performance_monthly.sql | Adds `all_*` columns and documentation to the Gold overall port performance table DDL. |
| teqplay/templates/sql/ddl/kpi/gold/kpi_berth_stay_duration_monthly.sql | Adds `all_*` columns and documentation to the Gold berth stay duration table DDL. |
| teqplay/templates/sql/ddl/kpi/gold/kpi_berth_occupancy_monthly.sql | Adds new average and `all_*` columns and documentation to the Gold berth occupancy table DDL. |
| teqplay/templates/sql/ddl/kpi/gold/kpi_anchorage_duration_monthly.sql | Adds `all_*` columns and documentation to the Gold anchorage duration table DDL. |
| teqplay/tasks/prepare_db/migration_task_groups.py | Adds ordered migration operators (drop+recreate Silver MVs; alter Gold tables) into `run_kpi_migrations()`. |
| teqplay/tasks/kpi/terminal_occupancy_monthly_task_groups.py | Registers new terminal occupancy `all_*` metrics in the metric registry. |
| teqplay/tasks/kpi/portcall_performance_monthly_task_groups.py | Registers new portcall performance `all_*` metrics and updates existing metric descriptions. |
| teqplay/tasks/kpi/portcall_duration_monthly_task_groups.py | Updates event-centric QC gating and registers new portcall duration `all_*` metrics. |
| teqplay/tasks/kpi/overall_port_performance_monthly_task_groups.py | Registers new overall port performance `all_*` metrics and updates existing metric descriptions. |
| teqplay/tasks/kpi/berth_stay_duration_monthly_task_groups.py | Updates event-centric QC gating and registers new berth stay `all_*` metrics. |
| teqplay/tasks/kpi/berth_occupancy_monthly_task_groups.py | Registers new berth occupancy average + `all_*` metrics and updates existing metric descriptions. |
| teqplay/tasks/kpi/anchorage_duration_monthly_task_groups.py | Updates event-centric QC gating and registers new anchorage duration `all_*` metrics. |
</details>

<details>
<summary>Review details</summary>

### Suppressed comments (1)

**teqplay/templates/sql/ddl/kpi/silver/enriched_anchorage_duration_monthly.sql:128**
* The generate_series upper-bound subtracts 1 second from end_timestamp. After allowing zero-duration events, this can shift month-boundary timestamps into the previous month (e.g. 2024-02-01 00:00:00 → 2024-01-31 23:59:59), yielding an empty series and dropping those events from all_* counts.
```
    -- Generate series of month boundaries
    -- Note: Subtract 1 second from end_timestamp to prevent generating a row for
    --       boundary months with 0 duration (e.g., end='2024-02-01 00:00:00' should
```

- **Files reviewed:** 39/39 changed files
- **Comments generated:** 3
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/dataflow_dag_core/new/develop?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

### panjiyudasetya — COMMENTED (2026-09-07)

It looks like all existing feedback is quite important to be addressed @ryan-kharisma. Also, please make sure if the DML doesn't produce cartesian products.

### ryan-kharisma — COMMENTED (2026-09-09)

_No comment._

### ryan-kharisma — COMMENTED (2026-09-09)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-09)

Review completed. 3 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F760%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### ryan-kharisma — COMMENTED (2026-09-09)

_No comment._

### ryan-kharisma — COMMENTED (2026-09-09)

_No comment._

### ryan-kharisma — COMMENTED (2026-09-09)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-09)

Review completed. 3 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F760%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### augmentcode[bot] — COMMENTED (2026-09-09)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — APPROVED (2026-09-10)

🚀 🌔

## Review Comments

### Copilot — 2026-09-07 on `teqplay/templates/sql/ddl/kpi/silver/enriched_anchorage_duration_monthly.sql`

This predicate still excludes anchorages where end_timestamp == start_timestamp, so truly zero-duration completed events will never be included in the new “all_*” metrics (despite the PR intent to include zero-duration events).

This issue also appears on line 126 of the same file.

### Copilot — 2026-09-07 on `teqplay/templates/sql/ddl/kpi/silver/enriched_berth_visit_monthly_mooring.sql`

The “missing mooring data” branch still drops berth visits where end_timestamp == start_timestamp. If the goal is for all_visits_count to include *all* visits lacking mooring timestamps, zero-duration visits should be retained too; when doing so, the current “end_timestamp - 1 microsecond” upper bound also needs to avoid shifting exact month-boundary timestamps into the previous month (which can yield an empty generate_series).

### Copilot — 2026-09-07 on `teqplay/templates/sql/ddl/kpi/silver/enriched_berth_visit_monthly_stay.sql`

Now that zero-duration completed visits are included (end_timestamp >= start_timestamp), the “end_timestamp - 1 microsecond” upper bound can shift an end_timestamp that is exactly at a month boundary into the *previous* month. For a zero-duration visit at 2024-02-01 00:00:00, this yields an empty generate_series and drops the visit entirely, so it won’t be counted in the new all_* metrics.

### panjiyudasetya — 2026-09-07 on `teqplay/templates/sql/ddl/kpi/silver/enriched_berth_visit_monthly_stay.sql`

I think this one is quite important to address, @ryan-kharisma.

### ryan-kharisma — 2026-09-09 on `teqplay/templates/sql/ddl/kpi/silver/enriched_portcall_performance_monthly.sql`

already addressed on this f292a89d

### ryan-kharisma — 2026-09-09 on `teqplay/templates/sql/ddl/kpi/silver/enriched_anchorage_duration_monthly.sql`

already addressed on this f292a89d

### ryan-kharisma — 2026-09-09 on `teqplay/templates/sql/ddl/kpi/silver/enriched_berth_visit_monthly_mooring.sql`

addressed at 518c9ca5

### ryan-kharisma — 2026-09-09 on `teqplay/templates/sql/ddl/kpi/silver/enriched_portcall_duration_monthly.sql`

addressed at 518c9ca5

### ryan-kharisma — 2026-09-09 on `teqplay/templates/sql/dml/kpi/terminal_occupancy_monthly/load_kpi.sql`

addressed at 518c9ca5

## Comments

### ryan-kharisma — 2026-09-09

auggie review

### ryan-kharisma — 2026-09-09

auggie review

### ryan-kharisma — 2026-09-09

augment review


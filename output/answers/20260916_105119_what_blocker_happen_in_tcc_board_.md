---
id: file:20260916_105119_what_blocker_happen_in_tcc_board_
source: unknown
explicit_links: []
---
# what blocker happen in TCC board?

## Summary

The evidence contains no Jira issue explicitly flagged with a "Blocked" status or impediment field, so the blockers below are inferred from issue descriptions, bug reports and comments on the TCC board. The dominant blockers are **production instability in VesselVoyage/POMA/CSI processing (stuck queues, deadlocks, OOM, single-pod POMA)**, **bad AIS data (jitter) blocking reliable bunker-encounter detection in SGSIN**, and **a security/vulnerability backlog (Dependabot/DependencyTrack, SOC 2)** that repeatedly had to be triaged. A secondary, process-level blocker is missing tooling/observability — no StopMonitor metrics, no POMA logging, and nightly AisEngine integration tests that always fail.

## Decisions made (decision → reason)

**Production stability**
- Roll back to in-memory state in VesselVoyage and keep the enhanced locking → the move of in-memory state to the database made DB usage much heavier and the new locking introduced side-effects, causing the VesselVoyage queue to get stuck over 12–13 July 2025 and triggering 2 prio-1 calls in 48 hours (jira:TCC-271, jira:TCC-272).
- Fix the locking mechanism so it no longer deadlocks, add try/catch everywhere for blocking threads, and recreate NATS consumers when consumption is unhealthy → the deadlocks/blocked threads were the direct cause of the stuck processing (jira:TCC-273, jira:TCC-276).
- Scale resources back down and remove the extra production node → the Saturday scale-up "seemed to have no effect", so it was not the real fix (jira:TCC-271, jira:TCC-275).
- Document how to scale up processing in the "What to do if …" runbook → the incident showed the team lacked operational guidance (jira:TCC-274).
- Repair ships with incorrect visits/voyages caused by the locking issue, preferably via EventHistory rather than a full recalculation → avoid recalculating more than needed (jira:TCC-287).

**POMA**
- Restore POMA to 2+ pods and re-envision the sync mechanism for multi-pod → POMA had been scaled down to a single pod after a sync issue, and a later operational problem "likely would have resolved itself if multiple pods were running" (jira:TCC-544).
- Add (time-boxed, ~1h) logging to POMA → POMA stopped processing tasks with no clear cause and produced no logs to diagnose it (jira:TCC-543).
- Fix the PROD→DEV Poma sync exception → scheduled sync crashed on a MongoDB duplicate-key bulk-write error on `terminal_temp` (jira:TCC-285).

**Encounters / AIS quality**
- Add a per-ship plausibility (space-dimension) check for AIS positions → existing jitter defences (extrapolation, `canCatchUp`, 15-min finish timer) only hedge in the time dimension, so a 37-minute "teleport" excursion outlasts the timer and chops a bunkering into fragments (jira:TCC-1105).
- Improve bunker encounter detection in SGSIN (short alongside check, heading-based alongside) instead of relying on the normal alongside check → SGSIN has too much bad AIS for the standard check (jira:TCC-1094).
- Drive encounters to a 5% error margin via recalculate → improve → re-validate cycle on SGSIN for 3 months → measured gap versus Ofiniti reference data (jira:TCC-1060, jira:TCC-1128, jira:TCC-1129, jira:TCC-1130).
- Apply the IMO/MMSI mapping to the other side of encounters in VesselVoyage → the mapping was only applied to the subject ship, not the service vessel (jira:TCC-1104).

**Recalculation / revents**
- Make the large-port recalculation process robust so it "can't suddenly decide to stop itself" → treated as a production bug (jira:TCC-1151).
- Alert when a revents recalculation job runs longer than ~24h on Fargate → jobs could run unnoticed (jira:TCC-286).

**Observability / testing**
- Add metrics to StopMonitor → the performance issues could not be investigated without them (jira:TCC-604).
- Make AisEngine integration tests run automatically and report to GitHub → nightly develop-branch tests "always fail (properties seem to be missing from the test)", forcing Darius to run them locally for Obeya metrics (jira:TCC-672).

**Security / SOC 2**
- Define a team process for picking up vulnerabilities and implement it → previously unclear who/when handled them (jira:TCC-312, jira:TCC-319).
- Bump `auth0-js` to v10 and `react-router-dom` to ≥6.30.4 → these actually ship in the browser bundle (login path, router), unlike most Dependabot alerts which are build/test tooling that never reaches the browser (jira:TCC-1131, jira:TCC-1132).
- Update Api and AisEngine dependencies for the tomcat-embed-core / netty-codec-http2 CVEs → both services are publicly exposed (jira:TCC-500).
- Only update dependencies when actually affected → "don't waste time updating dependencies when not needed" (jira:TCC-278).
- Get all applications tagged and present in DependencyTrack → some projects (etapredictor, portmatcher) were missing, so vulnerabilities were invisible (jira:TCC-410, jira:TCC-411).

## Rationale

The recurring theme on the TCC board is that **processing pipelines silently stop or degrade, and the team lacks the observability to know why**. The July 2025 VesselVoyage incident (jira:TCC-271) is the clearest example: an architectural change (in-memory state → database) plus a new locking mechanism produced deadlocks and a stuck queue, escalating to two priority-1 calls in 48 hours. The team's response was deliberately conservative — revert the architectural change, keep only the part that worked, undo the emergency scale-up that had no effect, and add self-healing (NATS consumer recreation) plus a runbook. The same pattern repeats with POMA stopping without logs (jira:TCC-543) and being left on a single pod (jira:TCC-544), CSI Agentic AI failing on timeout/memory with a human running the script locally as a workaround (jira:TCC-540), EventHistory hitting direct-memory OOM on circle queries (jira:TCC-1083), and a suspected VesselVoyage memory leak that remains unassigned (jira:TCC-541).

The second blocker class is **data quality rather than code**. In SGSIN, encounter detection is repeatedly broken by large, sustained bad AIS positions — ships reported kilometres away at impossible speeds and then snapping back — which trip the bunker exit logic and fragment a single bunkering (jira:TCC-1105). The analysis in that ticket is explicit that all existing defences hedge in time, not space, and that there is no plausibility check; that is why the fix is framed as new filtering rather than tuning. This directly blocks the "reliable bunker encounter events" epic and the 5% error-margin target (jira:TCC-1094, jira:TCC-1060).

The third class is **security/compliance debt acting as recurring drag**: a long chain of triage tickets across VesselVoyage, AisEngine, the Teqplay API, frontends and Core Components (jira:TCC-278, jira:TCC-280, jira:TCC-408, jira:TCC-409, jira:TCC-499, jira:TCC-523, jira:TCC-1103, jira:TCC-1183). The team responded by making it a process instead of ad-hoc work (jira:TCC-312), by making DependencyTrack coverage complete and tagged (jira:TCC-410, jira:TCC-411), and by prioritising only the advisories that reach real users (jira:TCC-1131, jira:TCC-1132, jira:TCC-500).

## Supporting evidence

- jira:TCC-271 — VesselVoyage queue stuck 12–13 July 2025, 2 prio-1 calls in 48h; root-cause assumptions and rollback plan.
- jira:TCC-272 / TCC-273 / TCC-274 / TCC-275 / TCC-276 — sub-tasks: in-memory state, deadlock fix, runbook, scale-down, NATS consumer health.
- jira:TCC-287 — ships with broken visits/voyages caused by the locking issue.
- jira:TCC-541 — suspected memory leak in VesselVoyage processing (To Do, unassigned).
- jira:TCC-1083 — EventHistory direct-memory OOM + sorting bug, 500s on `/v1/event/history/circle`.
- jira:TCC-540 — CSI Agentic AI stopped processing ships (timeout/memory); local script as workaround.
- jira:TCC-543 — POMA stopped processing with no logs; add minimal logging.
- jira:TCC-544 — POMA reduced to a single pod; restore HA.
- jira:TCC-285 — Poma PROD→DEV sync fails with Mongo duplicate-key exception.
- jira:TCC-1105 — AIS jitter (large sustained bad positions) breaks SGSIN encounter detection; no plausibility check exists.
- jira:TCC-1094 — SGSIN bunker encounters chopped up / missing hours due to jitter.
- jira:TCC-1060 / TCC-1128 / TCC-1129 / TCC-1130 — drive encounters to 5% error margin vs Ofiniti data.
- jira:TCC-1151 — large-port recalculation stops itself (production bug).
- jira:TCC-1100 — revents produces 0-second voyage between two recalculated visits of the same port.
- jira:TCC-286 — alerting for long-running revents jobs.
- jira:TCC-604 — StopMonitor lacks metrics to investigate performance issues.
- jira:TCC-672 — nightly AisEngine integration tests always fail (missing properties); tests run locally.
- jira:TCC-419 — old (2+ month) visit timestamps differ from VesselVoyage; scope unknown.
- jira:TCC-268 / TCC-374 / TCC-375 / TCC-376 — invalid `fieldType` accepted by CSI API, crashing the frontend.
- jira:TCC-312 / TCC-319 — establishing the vulnerability-handling process.
- jira:TCC-410 / TCC-411 — DependencyTrack coverage gaps (etapredictor, portmatcher missing).
- jira:TCC-500 / TCC-1131 / TCC-1132 / TCC-1103 / TCC-1106 / TCC-1107 / TCC-1183 — CVE remediation and triage backlog.
- confluence:792002660 — VesselVoyage barges blocked by IMO-only identifiers and the Visit–Voyage single-document data model.
- confluence:1277100033 — Spring Boot 4 upgrade guide (context for dependency/version churn).

## Gaps

- **No explicit blocker signal.** None of the retrieved documents contain a Jira "Blocked" status, flag, or impediment field. Everything above is inferred from bug descriptions, incident notes and comments — the board may have had formally flagged blockers that are not in this evidence set.
- **No GitHub or Notion evidence** was returned, so code-level confirmation of fixes (PRs, commits, reverts) is missing.
- **Unresolved items are ambiguous.** TCC-540, TCC-541, TCC-543, TCC-544, TCC-604, TCC-1105, TCC-419, TCC-262, TCC-263, TCC-268 are all still "To Do" and several are unassigned — the evidence does not say whether they are still actively blocking work or simply deprioritised.
- **Root causes not confirmed.** TCC-271 states the cause is an *assumption* pending in-depth analysis; no follow-up analysis document is present. Similarly, TCC-540 does not distinguish between timeout and memory limit, and TCC-541's memory leak is unconfirmed.
- **TCC-560 ("Make sure AIS-filtering works as expected")** has only a template description, so its relationship to the SGSIN jitter blocker is unclear.
- **No sprint/board-level data** (sprint reports, cycle time, blocked-time metrics) is available to say which blockers cost the most delivery time.
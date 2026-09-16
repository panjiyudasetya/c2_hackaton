---
id: file:20260916_104257_tell_me_what_tcc_team_doing_now
source: unknown
explicit_links: []
---
# tell me what TCC team doing now

## Summary

Based on the retrieved TCC-board evidence, the most recently active work (updates dated January 2026 and later) centres on **ETA prediction performance and productisation**, **wrapping up the API test automation project**, and **finishing the AWS SDK migration for CoreComponents** (jira:TCC-619, jira:TCC-490, jira:TCC-492, jira:TCC-478). A large block of platform-stability and data-quality work (VesselVoyage, ShipHistory, AisStream/Kpler migration, Poma V2) was completed during Q4 2025 (jira:TCC-526, jira:TCC-530, jira:TCC-534, jira:TCC-506). Note: the evidence set contains no sprint/board snapshot, so "now" is inferred from the newest `Updated` timestamps rather than from an explicit current-sprint list — treat this as an inference, not a fact.

## Decisions made (as visible in the evidence)

- **Improve ETA prediction performance before re-enabling for all ships/ports** → a metrics-analysis sub-task was run first to decide what to optimise (jira:TCC-619, parent TCC-618, updated 2026-01-19).
- **Create a V0 internal endpoint to replace old platform-based ETA predictions** → so legacy ETA consumers (Teqplay API, Smartfleet) keep working while predictions move to the new predictor; the Teqplay API was adjusted to call it (jira:TCC-490, jira:TCC-491, jira:TCC-492 — these carry the latest update dates in the set, 2026-01 to 2026-06).
- **Support ETA predictions for ships at anchor in a non-destination port** → requested by the PortCallOne team (Richard); judged likely cheap given Rowdey's speed changes, so envisioned for short-term implementation (jira:TCC-531, updated 2026-01-28).
- **Build a standalone Gradle/Java API-test project with nightly runs and GitHub Pages reporting** → to get automated regression coverage of External/Internal API (auth, ship, event) plus visible reporting (jira:TCC-481, jira:TCC-514, jira:TCC-515, jira:TCC-516, jira:TCC-528, jira:TCC-508/509/510), documented in Confluence so others can extend it (jira:TCC-587).
- **Defer CI/CD integration, Voyage tests and infra tests of that framework** → these remain To Do/unassigned (jira:TCC-517, jira:TCC-511, jira:TCC-512).
- **Migrate CoreComponents off the old AWS SDK** → reduce bloated full-SDK dependencies (e.g. revents only needs S3 for AIS loading); inventory done via Dependency Track (jira:TCC-478, jira:TCC-480, jira:TCC-522, closed 2026-01-06).
- **Prioritise VesselVoyage post-processing for ARA region / USCRP** → ~9 million entries meant ~9 days of processing; Obeya decided to prioritise regions with real users because PortReporter customers were waiting (jira:TCC-526).
- **Switch the Spire TCP AIS feed to Kpler, DEV first then PROD** → Spire imposed a hard decommission date of 1 December 2025 (jira:TCC-534).
- **Do not build a shared ship state; keep state per application, move to Redis later** → a shared state breaks when consumers such as EncounterMonitor are catching up (jira:TCC-520).
- **Narrow Core Data Quality metrics to a rolling 2-week window and add ship categories** → the all-time view made it impossible to see the effect of changes, and per-port numbers (e.g. Rotterdam ~80%) were hard to explain (jira:TCC-529, jira:TCC-493).

## Rationale

The thread running through the newest tickets is *making the core data products trustworthy and operable at scale*. ETA predictions are the current focal point: the team is measuring first (jira:TCC-619) before optimising, because the goal is to run predictions again for **all** ships and ports, and because downstream consumers such as PortCallOne were largely falling back to AIS ETAs (jira:TCC-518). The V0 endpoint work (jira:TCC-490/491/492) exists to keep legacy consumers whole during that transition, and the anchorage-ETA request (jira:TCC-531) shows the team taking cheap, high-value PortCallOne feature requests opportunistically.

In parallel, quality engineering has shifted from ad-hoc to automated: the API testing project was built from scratch (Gradle + Java, reporting library, nightly schedule, GitHub Pages) and then documented so the rest of the team can extend it (jira:TCC-481 and children, jira:TCC-587). The deliberate next steps — CI/CD hooks, Voyage tests, infra tests — are still open and unassigned (jira:TCC-517, jira:TCC-511, jira:TCC-512), which suggests capacity was pulled toward ETA and production work instead.

Underneath this sits a steady stream of stability and tech-debt items driven by production pain and external deadlines: memory/OOM issues (jira:TCC-506), a NATS consumer that could hang on drain (jira:TCC-530), caching bugs (jira:TCC-502), the vendor-imposed Spire→Kpler migration (jira:TCC-534), and dependency/vulnerability hygiene (jira:TCC-523, jira:TCC-312/318/319). Decisions here are consistently justified by customer impact (PortReporter, PTO, PortCallOne, Context Mapping team) rather than internal preference.

## Supporting evidence

- jira:TCC-619 — Metrics analysis to decide ETA optimisation targets; newest clearly in-scope work (updated 2026-01-19).
- jira:TCC-490 / jira:TCC-491 / jira:TCC-492 — V0 ETA endpoint plan, implementation, and Teqplay API switch-over (latest update timestamps in the set).
- jira:TCC-531 — Envisioning ETA predictions for ships at anchor, requested by PortCallOne.
- jira:TCC-481 — Parent "Implement API testing" story, Done 2025-12-22.
- jira:TCC-514 / 516 / 515 / 528 / 587 — Gradle+Java setup, reporting library, nightly runs, GitHub Pages reporting, Confluence docs.
- jira:TCC-508 / 509 / 510 — Auth, Ship and Event tests for External/Internal API.
- jira:TCC-517 / 511 / 512 — Still-open testing follow-ups (CI/CD, Voyage tests, infra tests).
- jira:TCC-478 / 480 / 522 — AWS SDK migration across CoreComponents, closed 2026-01-06.
- jira:TCC-526 — ARA/USCRP prioritisation of VesselVoyage post-processing, decided in Obeya.
- jira:TCC-534 — Spire → Kpler AIS feed migration with hard 1-Dec deadline.
- jira:TCC-530 / 506 / 502 / 532 / 524 / 518 / 504 / 503 — Production-issue backlog (TCC-152) handled Oct–Dec 2025.
- jira:TCC-529 / 493 / 513 — Data-quality metric changes and Context Mapping completeness dashboards.
- jira:TCC-520 — Redis / shared ship-state envisioning outcome.
- jira:TCC-523 / 312 / 318 / 319 — SecOps: Dependency Track triage and vulnerability process.
- jira:TCC-464 — "New environment structure for better quality and workflow", To Do, updated 2026-01-14.
- confluence:909639682 — MVP Customer Area Monitoring design (UAB Online request, new CustomerEventPublisher).
- confluence:812417027 — VesselVoyage V1 vs V2 processing performance analysis.
- jira:TCC-206 family (jira:TCC-314, 323, 292, 322 and subtasks) — Poma V2 finalisation and main-port validation fixes.

## Gaps

- **No current-sprint or board-state snapshot.** I inferred "now" from `Updated` dates; there is no sprint name, sprint goal, or "In Progress" status in any retrieved document. Nothing in the set is in an in-progress state — items are either Done or To Do.
- **Inconsistent/odd dates.** jira:TCC-491 and jira:TCC-492 show update dates of 2026-06-19 and 2026-06-23, far beyond the rest of the corpus. I cannot tell whether these are the true "latest" activity or data artefacts.
- **Parent epics not retrieved.** TCC-618 (ETA performance), TCC-426 (Portcall One MVP), TCC-152 (Production Issues), TCC-5 (ETA predictions productized) appear only as parent references — their scope, status and current priority are unknown.
- **No GitHub or Notion evidence.** Only one PR/repo reference appears, indirectly, in a comment (teqplay/teqplay-api-tests branch in jira:TCC-508). There is no code-level or design-doc evidence of what is actively being built right now.
- **No team/capacity information.** Assignee names appear (Darius Wattimena, Michel Wilson, Joost Dambrink, Francisco Jose Muros Muriano, Jamie de Leest, Rowdey Goos, David Hansson), but there is no evidence of who is currently allocated to what.
- **Unclear whether open To Do items are truly queued or dormant** — e.g. jira:TCC-238, jira:TCC-181, jira:TCC-483, jira:TCC-321, jira:TCC-313 are all unassigned with no recent activity.
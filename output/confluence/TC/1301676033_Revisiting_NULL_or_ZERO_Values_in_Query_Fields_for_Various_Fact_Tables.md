---
id: confluence:1301676033
source: confluence
type: page
space: TC
title: Revisiting NULL or ZERO Values in Query Fields for Various Fact Tables
author: Ryan Kharisma Rakhmat
date: '2026-08-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1301676033
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1301676033
---
# Revisiting NULL or ZERO Values in Query Fields for Various Fact Tables

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1301676033  

## Content

Founds that beside the `add zero to fill null durations` there are some `prepare` query that force the null value into 0 by `coalesce` syntax. So I think all of the fields listed here need to revisit again whether we decide it should be`NULL` or `ZERO`.

| **Table Name** | **Group** | **Should be NULL or ZERO ?** |
| --- | --- | --- |
| Fact Berth Visit | mooring (mooring, unmooring and moored duration) | for moored durations is not possible to zero. It should be null if not happening. |
| Fact Terminal Visit | cargo (cargo , non-cargo operation duration) | for barge the null is acceptable if the event is not yet complete. |
| Fact Terminal Visit | terminal moored duration | for moored durations is not possible to zero. It should be null if not happening. |
| Fact Terminal Visit | anchor (terminal anchor duration, anchorage during terminal visit) | in KPI if the data is not complete we set it null and exclude from the average calculations. |
| Fact Terminal Visit | waiting (outside terminal, during terminal) | It should be null if it is not completed. |
| Fact Terminal Visit | slowmoving during terminal visit | It should be null if it is not completed. |
| Fact Terminal Visit | shifting within terminal visit duration | It should be null if it is not completed. |
| Fact Terminal Visit | turn around time | It should be null if it is not completed yet. |
| Fact Port Visit | Sailing (sailing in and out duration) | It should be null if it is not completed. |
| Fact Port Visit | anchor (before, during, after) | before couldn't be null.  during and after should be null if not completed or not happens. |
| Fact Port Visit | slowmoving (arrival, during, inport) | It should be null if it is not completed. |
| Fact Port Visit | shifting (between, inside) | It should be null if it is not completed. |
| Fact Port Visit | Steaming In and Out (port inbound and outbound travel duration) | It should be null if it is not completed. |
| … | … | … |

Action Items

* [ ] Schedule a follow-up session for the week of August 17th
* [ ] Gavin den Hollander to share meeting notes in the channel
* [ ] Team to reflect further on the null vs. zero decisions before the follow-up session
* [ ] Revisit the null/zero discussion with Yaren after their holiday and meeting with Alex
* [ ] Investigate whether outliers should be explicitly excluded from KPI layer calculations

Meeting Context

* The discussion focused on resolving null vs. zero values found in the respects table, where ~30 fields were identified as zero or null

Core Principle: Null vs. Zero

* **Key distinction:** Zero influences averages; null does not — the correct choice depends on whether the absence of an activity is meaningful
* **General rule agreed upon:** If an activity *exists*, the field should have a value (zero or otherwise); if an activity *does not exist or is incomplete*, it should be null
* **Barges special case:** Null is acceptable when an event is not yet finalized (e.g., a start time exists but no end time yet)

Field-by-Field Decisions

* **Mooring duration:** Should *never* be zero or null — it is defined as start and end of berth visit and must always have a value if a berth visit occurred
* **Port turnaround time:** Zero is *not* possible; should be null if the vessel did not go to port
* **Anchor duration:** Zero is acceptable if a vessel visited port but did not anchor; null if no mooring context exists
* **Steaming in/out:** Should be null (not zero) when there is no terminal visit, to avoid skewing calculations
* **Slow moving during terminal:** Same null rule applies
* **Anchor before/during/after:** Null applies for during and after if the visit is incomplete; before may still be populated

KPI Layer Approach

* Proposed approach: expose *multiple values* per KPI metric rather than committing to one representation

  + Average including zeros (counts non-anchoring vessels as zero)
  + Average excluding nulls (only vessels that performed the activity)
  + Count of vessels for each scenario
* This gives end users and applications full flexibility to choose their preferred interpretation
* Outlier detection exists in the Data Mart layer but is *not currently applied* to KPI calculations — flagged as a point to resolve

KPI Validation & Customers

* KPIs are currently developed without a confirmed end user
* Risk noted: end users tend to *trust* data rather than validate it, making it important to get the logic right before exposure
* Suggestion made to validate assumptions with customers once engaged — not just the numbers, but the definitions behind them

Next Steps & Timeline

* Team to “marinate” on the current thinking before making a final decision
* Follow-up meeting to be scheduled for the **week of August 17th**, after Yaren’s holiday
* Yaren has a meeting with Alex upon return that may provide relevant feedback
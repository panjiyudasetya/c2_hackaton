---
id: github:teqplay/vesselvoyage-backend:issue:713
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 713
title: VesselVoyage PTO SOF terminal times can be negative
author: Darius-Wattimena
state: closed
date: '2026-02-17'
url: https://github.com/teqplay/vesselvoyage-backend/issues/713
labels: []
explicit_links: []
---
# Issue #713: VesselVoyage PTO SOF terminal times can be negative

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/713  
**State:** closed | **Author:** Darius-Wattimena  
**Created:** 2026-02-17  
**Closed:** 2026-02-17  

## Description

Description

The terminal times are negative, this shouldn’t be possible. This means the underlying data in the Visit database is having berth stops which are somehow corrupt and have wrong start and end dates.

Those should then result in broken terminal times when requesting the PTO API model. Make sure that the negative berth times are fixed for the below shared visits and fix so negative terminal times are not shared with a negative time.

We should fix the issue, and not mask the problem by not exposing the corrupted data.

CSV containing findings from PTO team => [negative terminal stay (1).csv](https://github.com/user-attachments/files/25362093/negative.terminal.stay.1.csv).

Related slack interaction => https://teqplaydev.slack.com/archives/C04DLAXFVCG/p1769674888939319?thread_ts=1769673503.218199&cid=C04DLAXFVCG.

Dependencies

Initial broken behaviour was reported by Engin and later forwarded by Yaren. When fixed informing the PTO should be done as they need to reimport the data.

Definition of Done

Changes are tested

Changes are deployed on PROD and DATA

PTO team (Yaren) is informed that the fix is available

Definition of Ready

[ ] Follows INVEST principles

[ ] External dependencies identified and resolved or explicitly accepted

[ ] No major open questions remain

[ ] Definition of done defined and understood

[ ] Story points assigned



## Comments

### Darius-Wattimena — 2026-02-17

## Summary

Fixed in PR #714 — merged to `develop` and deployed.

### Root Cause

Corrupt berth stop data in the Visit database where `start.time > end.time` (inverted stops). When the PTO SOF API computed terminal visit durations from these stops, the result was negative.

### Fix

Added validation in the event processing pipeline to prevent inverted stops from being created:

- **`StopStartProcessor`** — When a new stop-start event closes a previous ongoing stop, if the end time would be before the stop's start time, the end is clamped to the start time (zero-duration stop) instead of creating an inverted stop.
- **`StopEndProcessor`** — Same clamping logic when a stop-end event finishes a previous-entry stop.
- Both cases log a warning for observability.

### Tests

6 unit tests added:
- 2 general inverted-stop tests (StopStartProcessor + StopEndProcessor)
- 4 CSV-based tests using real production failure data from the attached CSV (large ~28h inversion, large ~17h inversion, small ~10min inversions)

### Verification on Develop

- ✅ All tests pass
- ✅ Services healthy (`/actuator/health` → UP)
- ✅ Recalculation triggered for affected ship IMO 9983968 (FURE VICTORIA) — all terminal times positive
- ✅ Last 3 finished visits all show correct positive durations (27.77h, 71.46h, 30.55h)

### Remaining Steps

- [ ] **Deploy to Production & Data** — release from `develop` → `master`
- [ ] **Recalculate affected ships** — trigger `POST /v2/recalculate/ship/{shipId}/fullStory` for the ~20 ships from the CSV to repair their existing corrupt stops
- [ ] **Inform PTO team (Yaren)** — notify that the fix is available and data has been corrected

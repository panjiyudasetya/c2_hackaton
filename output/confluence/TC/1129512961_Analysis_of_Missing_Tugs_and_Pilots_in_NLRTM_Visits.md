---
id: confluence:1129512961
source: confluence
type: page
space: TC
title: Analysis of Missing Tugs and Pilots in NLRTM Visits
author: Darius Wattimena
date: '2026-02-16'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1129512961
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1129512961
---
# Analysis of Missing Tugs and Pilots in NLRTM Visits

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1129512961  

## Content

|  |  |
| --- | --- |
| **Analysis Date** |  |
| **Sample** | 50 NLRTM Visits marked as “incomplete SOF“ were analysed  With only 37 Visits of relevant ships, matching the following criteria:   * Only sea vessels were used * Only General Cargo, Bulk Carrier, Container or Tanker |
| **Current “Completeness“ Criteria** | 1. Needs a tug when bigger than `150` meter in length. 2. Needs a pilot when bigger than `75` meter in length.   Otherwise they are marked in the metrics as “complete“. |

# 1. Case Type A – Seagoing NLRTM Visits

**Issue Pattern**

* Missing Tugs
* Missing (Outbound) Pilot

## Primary Example

**Ship 9580974**  
<https://vesselvoyage.teqplay.nl/#/ships/9580974/story/052ec380-bd48-4691-b4d4-33f7f1a2593a.VISIT?mode=period&months=3>

**Observations**

* Outbound pilot wrong because of AIS jitter?
* Tug encounters visible in VesselVoyage → falsely marked missing in metrics

---

## Similar Cases – False “Missing Tugs”

* 9278727  
  <https://vesselvoyage.teqplay.nl/#/ships/9278727/story/310335a0-5a8a-41f5-8c5a-efa2afa2b9d4.VISIT?mode=period&months=3>
* 9304162  
  <https://vesselvoyage.teqplay.nl/#/ships/9304162/story/29865b14-2e0f-438b-a436-321b6cb520a5.VISIT?mode=period&months=3>
* 9214305  
  <https://vesselvoyage.teqplay.nl/#/ships/9214305/story/bb693d0a-a8c2-49cb-ab87-3117614efd5c.VISIT?mode=period&months=3>
* 9742900  
  <https://vesselvoyage.teqplay.nl/#/ships/9742900/story/52db432b-c15f-4a01-b08d-5ca984eaf902.VISIT?mode=period&months=3>
* 9307334  
  <https://vesselvoyage.teqplay.nl/#/ships/9307334/story/a19d8729-1770-446e-b5d7-7c30211df398.VISIT?mode=period&months=3>
* 1014010  
  <https://vesselvoyage.teqplay.nl/#/ships/1014010/story/cb14f21a-96be-4665-aaee-bcc1eee86828.VISIT?mode=period&months=3>
* 9287297  
  <https://vesselvoyage.teqplay.nl/#/ships/9287297/story/14e234d8-b2ca-430b-9fd7-0fecfe8c6c61.VISIT?mode=period&months=3>
* 9568500  
  <https://vesselvoyage.teqplay.nl/#/ships/9568500/story/32a25f4e-555a-4a96-afcf-8a4250581b87.VISIT?mode=period&months=3>
* 9474541  
  <https://vesselvoyage.teqplay.nl/#/ships/9474541/story/03cfc377-7307-4f33-be7c-843242dd67e1.VISIT?mode=period&months=3>
* 9937476  
  <https://vesselvoyage.teqplay.nl/#/ships/9937476/story/8f055f0d-80da-4a59-ac64-086a970d1536.VISIT?mode=period&months=3>
* 9650339  
  <https://vesselvoyage.teqplay.nl/#/ships/9650339/story/317575d2-3b1e-47c1-98aa-4693aa416f84.VISIT?mode=period&months=3>
* 9460796  
  <https://vesselvoyage.teqplay.nl/#/ships/9460796/story/ac4bc0f7-cfbe-4f41-bd54-5463bd631563.VISIT?mode=period&months=3>
* 9350745  
  <https://vesselvoyage.teqplay.nl/#/ships/9350745/story/4d470162-a856-432b-bf89-f12eb0b47d2f.VISIT?mode=period&months=3>

**Pattern**

* Tug encounters visible in timeline
* Metrics engine still flags as missing
* Possible detection window or classification mismatch

---

# 2. Case Type B – NLRTM Inland Visits

**Issue Pattern**

* Missing Tugs
* Missing Pilots

## Primary Example

**Ship 9267467 (75m)**  
<https://vesselvoyage.teqplay.nl/#/ships/9267467/story/daf45153-2816-409e-ad8c-eba6b56d1892.VISIT?mode=period&months=3>

**Observation**

* Inland routing breaks checks, no pilot or fallback at all.

---

## Similar Cases

* 9280926 (110m)  
  <https://vesselvoyage.teqplay.nl/#/ships/9280926/story/7b1cd3a2-9b36-443c-8a7d-f4b7b9fcfba5.VISIT?mode=period&months=3>
* 2329503 (135m)  
  <https://vesselvoyage.teqplay.nl/#/ships/2329503/story/65c6d69c-1296-4a7c-8a4f-26e38411fe9a.VISIT?mode=period&months=3>
* 9432012 (110m)  
  <https://vesselvoyage.teqplay.nl/#/ships/9432012/story/81e08308-5884-497b-8620-c0f56f9b3c00.VISIT?mode=period&months=3>

---

# 3. Case Type C – “Waiting for Departure” Tug Only

**Issue Pattern**

* Tug encounter exists
* Only classified as “waiting for departure”
* Marked as Missing Tug

## Primary Example

**Ship 9467225**  
<https://vesselvoyage.teqplay.nl/#/ships/9467225/story/800cabf7-30a7-4f8a-924c-d750c48b51b0.VISIT?mode=period&months=3>

## Similar Cases

* 9969534  
  <https://vesselvoyage.teqplay.nl/#/ships/9969534/story/84a2f790-c9d4-4d26-80e9-9d4a27957577.VISIT?mode=period&months=3>
* 9351464  
  <https://vesselvoyage.teqplay.nl/#/ships/9351464/story/e1ca63ca-af19-4282-a7a1-0bcba7da195f.VISIT?mode=period&months=3>
* 9057238  
  <https://vesselvoyage.teqplay.nl/#/ships/9057238/story/ce57e7be-b2fa-4ab9-98d4-859729e015ab.VISIT?mode=period&months=3>
* 9934412  
  <https://vesselvoyage.teqplay.nl/#/ships/9934412/story/ce2c997f-7c17-4071-9f25-0837aafbceb5.VISIT?mode=period&months=3>
* 9171101  
  <https://vesselvoyage.teqplay.nl/#/ships/9171101/story/1c25e8f7-665b-4dcb-818a-2413426df916.VISIT?mode=period&months=3>

---

# 4. Case Type D – Anchor-Only EOSP Entry

**Ship 9014078**  
<https://vesselvoyage.teqplay.nl/#/ships/9014078/story/8b25694f-6c9a-47b6-b577-ca67cc3fd603.VISIT?mode=period&months=3>

**Issue Pattern**

* Missing Tugs
* Missing Pilots
* Entered EOSP directly to anchor

**Observations**

* Left port after anchoring

---

# 5. Case Type E – NLRTM → BEANR Transition

**Ship 9283978 (144m)**  
Visit:  
<https://vesselvoyage.teqplay.nl/#/ships/9283978/story/c6cec70b-8934-4042-9434-7bc30355f5ca.VISIT?mode=period&months=3>

Timeline:  
<https://timeline.teqplay.nl/255915986?from=1770175453270&to=1770928749243&URL=https%3A%2F%2Fapi.teqplay.nl%2Fv0&selectedTime=1770224150841>

**Observations**

* Only Boatman used at berth
* Returned to anchor
* Last NLRTM pilot encounter becomes first BEANR encounter?

---

# 6. Case Type F – Inland Visit (No Services Required)

**Ship 9267895 (110m)**  
<https://vesselvoyage.teqplay.nl/#/ships/9267895/story/8ab601ec-e831-4700-a07e-de4bfd878d83.VISIT?mode=period&months=3>

**Observation**

* Visited Moerdijk
* No tugs or pilots required operationally
* Still marked missing

---

# 7. Case Type G – Mixed Detection Failure

**Ship 9213715**  
Visit:  
<https://vesselvoyage.teqplay.nl/#/ships/9213715/story/b12deba6-c158-431e-9565-d60ea468c74a.VISIT?mode=period&months=3>

Timeline:  
<https://timeline.teqplay.nl/245921000?from=1770233275000&to=1771005210000&URL=https%3A%2F%2Fapi.teqplay.nl%2Fv0&selectedTime=1770989926010&selectedEvent=0c7c2ab5-a09d-4b65-8eff-703c76aa2fc0>

**Observations**

* Tug only “waiting for departure”
* Outbound pilot detected but marked missing
* Inbound pilot not detected
* Passed pilot area → fallback logic may not be respected

---

# 8. Case Type H – Small Ships Marked Missing Tug

## Primary Example

**Ship 9566758 (90m tanker)**  
<https://vesselvoyage.teqplay.nl/#/ships/9566758/story/c5d894be-45c4-4a4d-87cf-d5f119a2080f.VISIT?mode=period&months=3>

---

## Similar Small Vessels

* 9367243 (107m)  
  <https://vesselvoyage.teqplay.nl/#/ships/9367243/story/ea8fda46-0e4b-415f-834a-2511195a340e.VISIT?mode=period&months=3>
* 9547570 (99m)  
  <https://vesselvoyage.teqplay.nl/#/ships/9547570/story/3a4afc38-469d-4351-94d4-cbf5c7fc55b5.VISIT?mode=period&months=3>
* 9930014 (89m)  
  <https://vesselvoyage.teqplay.nl/#/ships/9930014/story/07a6eff5-ae31-41ad-ba74-05cc0713f087.VISIT?mode=period&months=3>
* 9410519 (119m)  
  <https://vesselvoyage.teqplay.nl/#/ships/9410519/story/e62bb539-5d7a-4ea5-b7d1-ed769f12e253.VISIT?mode=period&months=3>

---

## Larger Vessels Also Without Tug

* 9320506 (142m)  
  <https://vesselvoyage.teqplay.nl/#/ships/9320506/story/0b38e5ea-132a-484d-85d3-59fa4a3ea91f.VISIT?mode=period&months=3>
* 9349215 (141m)  
  <https://vesselvoyage.teqplay.nl/#/ships/9349215/story/0ff0772f-c480-4af1-b285-50b2a54d516f.VISIT?mode=period&months=3>
* 9970533 (144m)  
  <https://vesselvoyage.teqplay.nl/#/ships/9970533/story/1d89c298-8607-4f90-8eeb-f587371c65e8.VISIT?mode=period&months=3>
* 9809112 (209m)  
  Visit:  
  <https://vesselvoyage.teqplay.nl/#/ships/9809112/story/550861c9-9010-454f-94ff-664d95ec9425.VISIT?mode=period&months=3>   
  Timeline:  
  <https://timeline.teqplay.nl/277574000?from=1770415883000&to=1770683918186&URL=https%3A%2F%2Fapi.teqplay.nl%2Fv0&selectedTime=1770431467808&selectedEvent=137feb78-47f1-4c44-aa17-1816a0aea225>

**Observation**

* Tug expectation appears too rigid
* Likely overly length-driven and not berth-context aware
---
id: confluence:92667905
source: confluence
type: page
space: TC
title: Portreporter Visit structure rules
author: Richard van Klaveren
date: '2022-02-24'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/92667905
explicit_links: []
---
# Portreporter Visit structure rules

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/92667905  

## Content

In portreporter we get visit information from platform and that requires some rules in exceptional cases on how to represent the resulting data.

The basic concept is that there are 3 different types of source for information:

1. **Planned rotation scheme**. This one only holds berth names and indexes
2. **Actual detected rotation scheme**: This one holds the visit ata, atd and berth name
3. **Estimated times:** This one holds the estimated times (eta/etd) at berths received from (mostly) the agent. This one is mapped to the planned rotation scheme based on berth name.

Those 3 inputs are maintained based on additional inputs, so the most up-to-date estimates for each berth are stored (not the older ones) and the most recent planned rotation scheme is stored. All this information is combined via a recalculation structure to the resulting visits taking a couple of rules. Those rules are:

6d467e40-0223-4e30-b653-727f371d1878e2ccddef-65b6-4c3f-8e5f-e7fa02a280cfDECIDEDActuals are first prio, Planning second, estimates third.

* Actuals are first prio, Planning second, estimates third.

If there is an Actual at visitIndex 0 and a planning at visit 0 that are not about the same berth. We will always resolve it to the actual

a6d648d7-1691-441e-a3f5-a5ed8ea80b497bb9d296-b667-4201-9e9d-cae40bf9a158DECIDEDIf there are 2 visits defined and the visit planned second comes in first, we will not change the order of the planning

* If there are 2 visits defined and the visit planned second comes in first, we will not change the order of the planning

This is due to this creating problems if there are duplicate berths. Like which planning item will you replace.

00ed33ac-9ef7-402f-8dda-f6dc05698f6179172f3b-4c26-4155-9ab5-8816fc4063d7DECIDEDWhen a visit is cancelled, keep the eta in the estimates

* When a visit is cancelled, keep the eta in the estimates
e10ebd5b-a939-4bac-89d3-882216528a6dc9eba55b-0bf2-401d-bf0c-dbf5b8f81daaDECIDEDWhen a visit is updated, keep the eta in the estimates

* When a visit is updated, keep the eta in the estimates
cc069a66-bd76-4618-9524-ade3303b07650ac794b2-1acd-4d23-84cb-074e05359572DECIDEDAdd the last eta known by berth name/ berth id to the visit. Even if the eta seems outdated. 

* Add the last eta known by berth name/ berth id to the visit. Even if the eta seems outdated.
2986da10-4c1c-4f73-b89e-ec37a69bb16f0819a929-7d0d-4395-bfc2-5e44827e5479DECIDEDA visit has a unique id by the berth id/berth name

* A visit has a unique id by the berth id/berth name

If the first visit is berth 1 and the third visit it berth 1. The id of the first will be berth 1 and of the third will be berth 1-T1 with T1 incrementing for every duplicate. so third duplicate will be T3

a57d32ac-430c-4b44-95cd-7ada8e3e4867b78c3d13-246b-410d-af6b-a1b7de6f1859DECIDEDIf an ATA event comes in while the previous visit has not received an ATD yet. The previous visit will be assigned the ATA coming in as ATD

* If an ATA event comes in while the previous visit has not received an ATD yet. The previous visit will be assigned the ATA coming in as ATD
cef1ccd0-161f-477b-bb70-a438403ba1fc6f7f18ce-3ea4-4462-ad36-a217bc28193fDECIDEDIf a planned visit is cancelled while the ship already arrived at that berth. Still show the visit40dd52ea-b332-40df-82dd-52f4aae72a85DECIDEDBerth ETA Agent/Berth ETA Vessel/ Nomination ETA Agent will result in an eta updateb26daf62-02cc-461e-84c0-26182239f74bDECIDEDBerth ETD Agent/ Nomination ETD Agent will result in an etd updatee86c4202-a87a-4f0e-838d-5209cb5a3176DECIDEDThe order of the list in the planning matters0c2c7168-de73-431b-8df7-633755c46142DECIDEDThe order of the list in the actuals matterb5d5332d-39f9-4678-8c1f-67aafe294007DECIDEDIf a visit is cancelled that is not the last visit. The order changes along with it. We will have no empty visit spots in the planning list

* If a planned visit is cancelled while the ship already arrived at that berth. Still show the visit
* Berth ETA Agent/Berth ETA Vessel/ Nomination ETA Agent will result in an eta update
* Berth ETD Agent/ Nomination ETD Agent will result in an etd update
* The order of the list in the planning matters
* The order of the list in the actuals matter
* If a visit is cancelled that is not the last visit. The order changes along with it. We will have no empty visit spots in the planning list

This means if there are 3 visits and the 2nd gets cancelled. The third visit will then be the second visit

c224ebf1-e538-4ade-be83-cb7f3473abcbbeadd013-eb56-4f5e-b43d-819c6f5daf8eDECIDEDCancel events never have the location specified, if they do it is ignored

* Cancel events never have the location specified, if they do it is ignored
---
id: confluence:102236161
source: confluence
type: page
space: TC
title: Chorus Functional Design Description
author: Daan Spikker (Unlicensed)
date: '2022-09-23'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/102236161
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/102236161
---
# Chorus Functional Design Description

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/102236161  

## Content

In this document we’ll discuss the principles of Chorus from a functional perspective.

## Bunkering process in Chorus

Disregarding the ADP’s, In the bunkering process, Chorus starts at creating and agreeing upon individual nominations Negotiation process.

### Nominations flow

#### **Create nomination**

A proposed nomination is an intent for bunkering. It is a request from the *customer* to the *supplier*.

Basically “the customer requests a amount *X* LNG for vessel *Y* at Location *Z* at or around time *T.”*

In the nomination the customer is requesting the supplier to get a bunkering activity containing the following:

#### **Initial Nomination (created by customer)**

* Delivery Point
* Contract (optional)
* Receiving vessel ( vessel of customer’s fleet )
* Nominated Quantity
* Additional Services (optional)

  + Gas Up
  + Cool Down

* ETA
* BST
* ETD

The status of the nomination after creating is:  
*‘New Proposal from customer’*

#### **Respond on Nomination**

Supplier can decide to follow-up on the nomination by:

·         Approving proposal (requires additional data)

·         Countering proposal

·         Rejecting proposal (optional reason)

·         Cancelling nomination

#### **Delivery Nomination (edited by supplier)**

* Vendor Reference
* Contract
* Delivery Point
* Receiving vessel ( vessel of customer’s fleet )
* Bunker Vessel
* Nominated Quantity
* Allowed bunkering time
* Additional Services (optional)

  + Gas Up
  + Cool Down
* ETA
* BST
* ETD

#### **Approving of Proposal** Supplier agrees with the conditions given by customer and states *‘bunkering will be executed on conditions agreed upon by bunkervessel X, under contract Y, for an allowed bunkering time T’*. Nomination is identifiable  for Supplier’s internal systems with Vendor Reference.

Supplier needs to add additional fields to nomination that can only be done by supplier and / or are  relevant for supplier:

#### ***Approval Fields***

·         Vendor reference

·         Contract

·         Bunker Vessel

·         Allowed Bunkering Time

#### **Countering Proposal**

Supplier disagrees with the conditions given by customer. He could:

·         Reject proposal (optional reason), giving the customer the option to change the details of the request.

·         Cancel.

·         Countering proposal

o   Change the following details

§  Nominated Quantity

§  Additional Services (on/off)

§  BST

§  *Receiving Vessel – not working now (7 sept 2022)*

§  Location

o   When sending the counterproposal, the supplier should fill in the required *Approval fields.*

Meaning the following fields trigger / not trigger counter proposal:

|  |  |  |  |
| --- | --- | --- | --- |
|  | **to be filled in by Customer** | **to be filled in by Supplier** | **Changing triggers counterproposal** |
| Vendor reference | No | Obligatory | NO |
| Delivery Point | Obligatory | No | YES |
| Contract (optional) | Obligatory | Obligatory | NO |
| Receiving vessel ( vessel of customer’s fleet ) | Optional | Optional | NO |
| Bunker Vessel | No | No | NO |
| Nominated Quantity | Obligatory | Obligatory | YES |
| Additional Services (on/off) (optional) | Obligatory | No | YES |
| Additional Services details | No | No | NO |
| Allowed Bunkering Time | No | Obligatory | YES |
| ETA | Optional | Optional | NO |
| BST | Obligatory | Obligatory | YES |
| ETD | Optional | Optional | NO |

Based on the action performed on the nomination the following statuses apply to a nomination:

* PROPOSED ( From changes by either customer / scheduler )
* ACCEPTED  ( After clicked on accept button )
* REJECTED ( After clicked on reject button )
* COUNTERED
* FINALISED ( After clicking on finalise button ( scheduler ), which is visible after the proposal is currently in accepted state )
* CANCELLED  ( Can this ever be canceled ? )
* COMPLETED ( Can this ever be completed ? )

#### **Dates validation**

* ETA: Must be before BST and before ETD
* BST: Must be after the ETA and must be before the ETD
* ETD: Must be after ETA and after BST

#### **State**

* PROPOSED ( From changes by either customer / scheduler )
* ACCEPTED  ( After clicked on accept button )
* REJECTED ( After clicked on reject button )
* COUNTERED
* CANCELLED (
* COMPLETED

### Supplying Company and corporation

Shell is a supplying corporation, it consists of multiple companies, Shell Western (doing European and American bunkerings), Shell Eastern (Middle east, Asia), and possibly some others.

A nomination that is done in Europe should be handled by Shell Western, one that’s done in Asia by Shell eastern. However, in Chorus this is not automated. AND the customer doesn’t always know.

If a customer creates a nomination (without a contract), the nomination is assigned to the corporation. However the corporation can’t really execute the bunkering, so to accept it, the supplier should assign it to a Shell Company by assigning the matching contract. The contract is exclusively linked to one of the supplying companies, hence determines the supplying company.

### Bunker ships

Bunkerships are part of the corporation, hence they can be used by both Shell Western as Shell eastern or another company within the Shell corporation, IF the bunker ship is in the Shell Corporation. As we will see later, in case of third party companies it can be assigned in another corporation-company combination.

Bunkerships have different attributes of which the following require some explanation:

* Horizon: this is how many days in advance (to bunker start time) the captain sees the (accepted, completed) nomination on his timeline.
* For position report, seagoing / not-seagoing, it defines the type of position report used for this bunker vessel.
* Other properties, defining which things should be logged in position report
* E-mails: recipients of position report.

### Nominations and contracts

* A contract is an agreement between supplying company and customer company that includes:

o   Name contract

o   Supplying company (only one)

o   Customer company (only one)

o   The receiving vessel(s) for which the contract applies

o   The location(s) for which the contract applies

o   The start and end date

o   And contractual process agreements (to be discussed later).

### Assign nomination Screen

* This specific screen identifies nominations that didn’t get assigned with a contract. It allows the supplier (shell) to assign these nominations with a contract.

### Events

Events are other activities on the bunkering vessel that impact scheduling, but are not bunkering activities. Or concretely, if an event is happening, quite likely a bunker activity cannot take place during that time. The following events exist:

* Loading
* Discharge
* LNG Bunkering
* MGO Bunkering (Marine Gas Oil)
* Charter out
* Conditioning
* Maintenance
* Pool
* Tentative
* Waiting
* Travelling

These events have their own properties and uses within the scheduling and planning department at the supplier.

The loading event is of most importance as it defines the properties of the bunker quality, and therefore the eBDN document (electronic bunker delivery notice).

### Annual Delivery Plan:

* An ADP is normally a yearly agreement on the estimated delivery of LNG bunkers between customer and supplier. It generally consists of the location, the frequency, expected amount per month and bunkering and the total amount of LNG volume (or energy?) delivered.
* The (annual) delivery plan in Chorus is actually a dynamic-period delivery plan.
* The supplier can create it based on a set of nominations created.

* In order to create an ADP, it should first have created the nominations in the ADP.
* Then the user creates an ADP and searches for the existing nominations to include.
* When creating the ADP, it is actually more a snapshot of the nominations.
* By generating the PDF from the ADP, the supplier can audit log it’s agreements at a certain time.

**An ADP is created per customer per contract (chorus Phase III).**

 Bulk add/editing & nominations searching

* The feature is used to search for nominations.
* Editing in bulk or adding in bulk is used for the supplier to be able to add one-or-many nominations at once.
* This should be done per customer.
* The editing and creating of nominations should adhere the regular permissions that apply to the regular nomination flow (or the on-behalf nomination flow)

### Sub-companies

* A subcompany is a division between companies within a customer company
* It could be that one company (costa cruises for example) is managed by one user, however to distinguish between the two companies, that could very well do nominations on distinct contracts, the user (customer and/or supplier) can select a subcompany by assigning the contract for the specific subcompany to the nomination.
* Sub-companies are added in the company-admin screen.

### Legal entity

* A legal entity is a way of describing a entity that’s acting on behalf of Shell (but is registered in a different place and acting under a different juridical name). An example of this is Shell Spain. If a bunkeractivity is performend in Barcelona, Spain, the legal entity ShellSpain will be applied. It only shows in the nomination as a label, and on the documents. The nomination falls under Shell Western in this case.

## Position Report

A log book, also known as noon-report per ship. Filled in by captain of bunker vessel.

It’s created by the scheduler or admin of the supplying company.

Captain needs to fill it in by adding a column. Some rows are user-input, others are based on details found in Chorus (vessel details e.g.). Other cells are calculated by combining several cells.

It replaces the excel they’re now using and sending by mail.

The position report can be send by mail as well, in order to let the office know what was the state at time X. These mail recipients are defined in the Configuration>>bunker ships menu.

Some rows are determined by properties of the bunker vessel, such as the number of engines. These are defined in the Configuration>>bunker ships menu.

## MSDS

A link that is added to a nomination, and shown to customer. Link is referring to Material safety data sheet. Can be set in Company configuration screen.

## The Timeline

The timeline supports the scheduler in changing nominations and events.

* In order to edit nominations, the user should open the nomination and perform an action.
* An event can be dragged and dropped (agenda style), it requires the user to confirm the change.
* An export of the timeline gives an excel of the nominations + events with details on the timeline between two given dates.

## Delegations and Third Party Supplier

Already on confluence

**Contracts**

* Just to keep a mental note, if we ever decide to assign `corporationId` for companies outside Shell Corp, we should remember to adjust Contract selection requirement on frontend. Currently, the frontend obliges Shell schedulers to select a contract when creating a new nomination. However, there is no such obligation for the other vendor users (for example: FueLNG or any other 3rd party supplier).  
    
  Frontend distinguishes the vendor companies if they’re under Shell or not by checking the `corporationId`. If it’s `null`, then it means the vendor company is outside of the Shell corp and vice-versa.

**Additional Services**

* As a Customer I can propose **Additional Services** (Cool Down / Gas Up) and changes on these two fields trigger a counter-proposal.
* If `Cool Down` is selected, adding/removing **Arrival Conditions** is also an option for Customer Scheduler and Receiving Vessel Captain. And **DOES NOT** trigger a counter-proposal.

## Task Action overview

As a **Scheduler** i want to be able to see a list of actions that my customers have to perform before a certain deadline. So that i have an overview of status of actions per customer and i don’t have to phone / mail them to remind them to complete their i.e. nominations for this month. The actions can be completed.

I want to be able to define the tasks per customer, give a deadline and define a single or recurring character.

As a **customer** i want to see a list of actions that i have to perform for a certain deadline and see a the actions of the supplier related to me. I want to be able to manually complete the actions assigned to me, or see it when the Scheduler completed the action.

The scheduler defines these action in the configuration>contracts. Here he can set incidental actions, recurring actions (yearly or monthly) for himself or his customer.
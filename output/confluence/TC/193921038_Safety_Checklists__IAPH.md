---
id: confluence:193921038
source: confluence
type: page
space: TC
title: Safety Checklists (IAPH)
author: Leon Joosse (Unlicensed)
date: '2023-07-17'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/193921038
explicit_links: []
---
# Safety Checklists (IAPH)

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/193921038  

## Content

17none

# 1. What is a safety checklist

A safety checklist helps all involved with sticking to agreements and safety measures. The checklist is divided in several parts. Involved parties need to fill in the different parts, and then sign them. These parts are indicated by a letter (A, B, etc). Parts are combined for easier handling, as they roughly belong to the same phase: planning/pre-bunkering, during bunkering and after bunkering.

The safety checklist is a digital copy of the physical safety checklist that bunker and receiving crew need to fill out during the bunkering operation.

A nomination can have 1 safety checklist. The application indicates with a *document status* how far both parties filled in the checklist parts, and who signed them.

## 1.1. IAPH Checklist

Several types of checklists exist, with their combined parts:

* IAPH
* Gothenburg
* TR56

**Quick comparison table**

| **Checklist** | **Parts** | **Fills in via application** | **Fills in via SignRequest** | **Signing in SignRequest** |
| --- | --- | --- | --- | --- |
| IAPH | `AB` `CD` `E` `F` | Bunker captain Receiving captain | - | Bunker captain Receiving captain |

Checklist created by the International Association of Ports and Harbours. This checklist is used in the majority of the ports.

It has the following parts:

* AB

  + A: checklist items on planning
  + B: planned simultaneous operations (simops)
* CD

  + C: checklist items just before bunkering
  + D: data tables on LNG transfer and simops
* E: checklist items after bunkering
* F: a receipt for the terminal where the bunkering takes place (if needed)

Parties involved:

* Receiving party: captain of the receiving ship
* Bunker party, captain of the bunker ship

## 1.2. Digital and paper parts

A small part of the checklist needs to be checked / filled in within the bunker hazard zone. A potential ignition source, like a tablet, cannot be used there. For these parts, we try to facilitate with a printable version of the checklist part. You can recognize those files from the suffix `*-checks.pdf`.

This applies for the repetitive checks (all checklist items having code 'R'), which are collected and saved to a PDF. The bunker crew print out the PDF and fill in the paper in the hazard zone with a pen/pencil, make a picture/scan and upload it to the nomination.

# 2. How to use it

The safety checklist is created by the bunker party and then filled in by the bunker and receiving party. Once completed, a PDF created and digitally signed.

The bunker party can always create a new checklist, by changing the template. The existing checklist is then replaced (throwing away all checked items, entries in data tables, etc).

## 2.1. Creating and filling in the checklist

The bunker party creates the checklist by selecting one of the types. Both receiving and bunker party can start filling in the checklist parts by ticking all checkboxes and populating the data tables. Once completed, a PDF can be created, so all parties can sign.

## 2.2. Creating a PDF

Once both parties are satisfied with filling in the checklist part, the bunker party can create a PDF and assign the signers. The system takes a snapshot of the filled in values and prints them to a PDF. The PDF is attached to the nomination’s document list.

The amount and type of signers differ per checklist type, but in general: (1) bunker party, (2) receiving captain and (3) optionally an external signer.

Assumptions:

1. Both parties are responsible for filling in the checklist correctly, the system allows the user to create a PDF when actually no values are filled in. That is on purpose, as some items may be not applicable to that situation.
2. The system considers the latest (creation date) PDF of that type as the final document, even is those earlier documents are signed. Earlier PDFs are kept for reference.

## 2.3. Signing the PDF

Most safety checklist PDFs must be signed by both the receiving and bunker party. And sometimes by an external signer. External meaning that the signer has no account in Chorus.

Signing is done electronically with SignRequest. This is an online service that accepts a PDF and draws a signature box at the desired place. The signer can then put his signature to sign the document.

The bunker party assigns all signers. All parties sign the document in SignRequest, using the link in the application or email. The system gets events who/when signed. Once all parties signed, we receive the signed copy of the PDF and store it in the database (S3 bucket).

### 2.3.1. Assigning signers

The bunker party assigns the signers. This sets up the document for signing in SignRequest. All assigned parties receive an email with a link that opens the signing page. Logged-in users can also use the ‘Sign’ button at the document, as shown below.

**Note on redirecting the user to SignRequest:**

We could also send the user directly to SignRequest. But there is a problem: when a signer already signed the document and visits the link again, SignRequest shows an non-meaningful error page. Instead, we know the signing status in the application, and thus can show the user a proper ‘You already signed this document’ page.

If the signer has an account in Chorus, he is redirected back to the application. External signers will only see a ‘thanks for signing’ message.

### 2.3.2. External signers

An external signer cannot use the application to check the required checklist items. Instead, we include the checkboxes for the external signer in SignRequest, along with the signature box. This way, the items appear checked for all parties on the final signed PDF.

The signing configuration for the external signer contains a list of checklist items (s)he must tick. SignRequest renders these checkboxes in the correct checklist item rows.

### 2.2.3. Signer and signing status

SignRequest sends events to the back-end, indicating when a signer signed, all signers signed, and some other events. The application uses these events to show the correct *document status*.

Once all signers signed the document, SignRequest sends the PDF including signatures to the back-end. The back-end then replaces the PDF in the database, so the user can download the signed document in the application.

When the last signer signed the document, SignRequest needs some time to process the document. The final `SIGNED` status can take a while (10s of seconds, sometimes minutes) to arrive at the back-end. The system therefore sets a flag (`AWAITING_CALLBACK`) when the user returns from SignRequest, to bridge this time gap for calculating the document status.

# 3. Technical

This part adds technical details which are not covered by earlier sections.

## 3.1. Data model

The `SafetyChecklist` model supports all types: IAPH, Gothenburg and TR56. Some model properties are used for all types, some for a single type. All fields in the `DASafetyChecklist` class are by default for all checklist types, unless indicated otherwise.

Checklists are divided per part, so `checklistA`, `checklistB`, etc. It differs per checklist type which `checklist*` lists are populated.

## 3.2. External signers and checkboxes

In some cases, an external signers needs to check some items. These are stored in the `externalSignerCheckboxes`. The external signer has no user account, so (s)he can only fill it in while signing. The PDF service includes a SignRequest checkbox tag where needed, so that the external signer still has the items checked on the signed version of the document.

## 3.2. System assumptions

1. A nomination can have 0 or 1 safety checklists
2. The safety checklist `_id` always equals the `nomination.eventId`
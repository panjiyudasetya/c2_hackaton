---
id: confluence:139788289
source: confluence
type: page
space: TC
title: Safety Checklists (IAPH, Gothenburg, TR56)
author: Leon Joosse (Unlicensed)
date: '2022-09-13'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/139788289
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/139788289
---
# Safety Checklists (IAPH, Gothenburg, TR56)

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/139788289  

## Content

17none

# 1. What is a safety checklist

A safety checklist helps all involved with sticking to agreements and safety measures. The checklist is divided in several parts. Involved parties need to fill in the different parts, and then sign them. These parts ARE indicated by a letter (A, B, etc). Parts are combined for easier handling, as they roughly belong to the same phase: planning/pre-bunkering, during bunkering and after bunkering.

The safety checklist is a digital copy of the physical safety checklist that bunker and receiving crew need to fill out during the bunkering operation.

A nomination can have 1 safety checklist. The application indicates with a *document status* how far both parties filled in the checklist parts, and who signed them.

## 1.1. Checklist types

Several types of checklists exist, with their combined parts:

* IAPH
* Gothenburg
* TR56

**Quick comparison table**

| **Checklist** | **Parts** | **Fills in via application** | **Fills in via SignRequest** | **Signing in SignRequest** |
| --- | --- | --- | --- | --- |
| IAPH | `AB` `CD` `E` `F` | Bunker party \*\* Receiving captain | - | Bunker party Receiving captain |
| Gothenburg | `AB` `CDEF` `G` | Bunker party \*\* Receiving captain | *Port official \** | Bunker party Receiving captain *Port official \** |
| TR56 | `AB` `CD` `E` | Bunker party \*\* Receiving captain | *Terminal representative \** | Bunker party Receiving captain *Terminal representative \** |

(\*) name and email address can entered at ‘Assign signers’ pop-up, or leave those fields empty to skip this signer)

(\*\*) Bunker party: the nomination’s delivery mode determines which user that is:

* Ship: bunker captain
* Pipe: operator of the pipeline
* Truck/Container: operator of the loading terminal

### 1.1.1. IAPH

Checklist created by the International Association of Ports and Harbours. This checklist is used in the majority of the ports. This checklist is available in Chorus and Fuelboss.

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
* Bunker party, based on the delivery mode:

  + Ship: bunker captain
  + Pipe: operator of the pipeline
  + Truck/Container: operator of the loading terminal (only available in Fuelboss)

### 1.1.2. Gothenburg

Based on the IAPH checklist, tailored to the port of Gothenburg. This checklist is available in Fuelboss.

This safety checklist has an option for a Port Official to sign among the bunker and receiving party. The Port Official has no account, so (s)he can only tick the checkboxes while signing in SignRequest. The PDF template includes these separate checkboxes in SignRequest.

Main difference between IAPH and Gothenburg:

1. Data tables are designed differently
2. Checklist items are divided in a different way across the checklist parts
3. Checkboxes + signing for Port Official

It has the following parts:

* Part AB

  + A1 and A2: checklist items on planning (item A2-4 enables part B2)
  + B1: planned simultaneous operations (simops)
  + B2: checklist for planning when bunkering during low flashpoint (below 30°C) (enabled by item A2-4)
* Part CDEF

  + C: checklist on pre-berthing
  + D: checklist after arrival, but before bunkering
  + E: checklist before bunkering
  + F: data tables on LNG transfer
* Part G: after bunkering

Parties involved:

* Receiving party: captain of the receiving ship
* Bunker party, based on the delivery mode:

  + Ship: bunker captain
  + Pipe: operator of the pipeline
  + Truck/Container: operator of the loading terminal
* Port official (optional)

### 1.1.3. TR56

Based on the IAPH checklist, tailored to the port of Singapore. This checklist is available in Fuelboss.

This safety checklist has an option for a representative of the terminal, where (s)he can tick checkboxes and sign as well. This works the same way as the Port Official in the Gothenburg checklist. The PDF template includes these separate checkboxes in SignRequest.

* AB

  + A: checklist items on planning
  + B: planned simultaneous operations (simops)
* CD

  + C: checklist items just before bunkering
  + D: data tables on LNG transfer and simops
* E: checklist items after bunkering

Parties involved:

* Receiving party: captain of the receiving ship
* Bunker party, based on the delivery mode:

  + Ship: bunker captain
  + Pipe: operator of the pipeline
  + Truck/Container: operator of the loading terminal
* Terminal representative (optional)

## 1.2. Digital and paper parts

A small part of the checklist needs to be checked / filled in within the bunker hazard zone. A potential ignition source, like a tablet, cannot be used there. For these parts, we try to facilitate with a printable version of the checklist part. You can recognize those files from the suffix `*-checks.pdf`.

This applies for the repetitive checks (all checklist items having code 'R'), which are collected and saved to a PDF. The bunker crew print out the PDF and fill in the paper in the hazard zone with a pen/pencil, make a picture/scan and upload it to the nomination.

# 2. How to use it

The safety checklist is created by the bunker party and then filled in by the bunker and receiving party. Once completed, a PDF created and digitally signed.

The bunker party can always create a new checklist, by changing the template. The existing checklist is then replaced (throwing away all checked items, entries in data tables, etc).

## 2.1. Creating and filling in the checklist

The bunker party creates the checklist by selecting one of the types. Both receiving and bunker party can start filling in the checklist parts by ticking all checkboxes and populating the data tables.

Once completed, a PDF can be created, so all parties can sign. The system shows the ‘filling in status’ per party on the safety checklist Overview tab.

## 2.2. Creating a PDF

Once both parties are satisfied with filling in the checklist part, the bunker party can create a PDF and assign the signers. The system takes a snapshot of the filled in values and prints them to a PDF. The PDF is attached to the nomination’s document list.

The amount and type of signers differ per checklist type, but in general: (1) bunker party, (2) receiving captain and (3) optionally an external signer.

Assumptions:

1. Both parties are responsible for filling in the checklist correctly, the system allows the user to create a PDF when actually no values are filled in. That is on purpose, as some items may be not applicable to that situation.
2. The system considers the latest (creation date) PDF of that type as the final document, even is those earlier documents are signed. Earlier PDFs are kept for reference.

*Safety checklist Overview in Fuelboss.*   
*Showing a TR56 safety checklist, showing the ‘Create PDF’ button at part E.*

## 2.3. Signing the PDF

Most safety checklist PDFs must be signed by both the receiving and bunker party. And sometimes by an external signer. External meaning that the signer has no account in Chorus/Fuelboss.

Signing is done electronically with SignRequest. This is an online service that accepts a PDF and draws a signature box at the desired place. The signer can then put his signature to sign the document.

The bunker party assigns all signers. All parties sign the document in SignRequest, using the link in the application or email. The system gets events who/when signed. Once all parties signed, we receive the signed copy of the PDF and store it in the database (S3 bucket).

### 2.3.1. Assigning signers

The bunker party assigns the signers. This sets up the document for signing in SignRequest. All assigned parties receive an email with a link that opens the signing page. Logged-in users can also use the ‘Sign’ button at the document, as shown below.

**Note on redirecting the user to SignRequest:**

We could also send the user directly to SignRequest. But there is a problem: when a signer already signed the document and visits the link again, SignRequest shows an non-meaningful error page. Instead, we know the signing status in the application, and thus can show the user a proper ‘You already signed this document’ page.

If the signer has an account in Chorus/Fuelboss, (s)he is redirected back to the application. External signers will only see a ‘thanks for signing’ message.

### 2.3.2. External signers

An external signer cannot use the application to check the required checklist items. Instead, we include the checkboxes for the external signer in SignRequest, along with the signature box. This way, the items appear checked for all parties on the final signed PDF.

The signing configuration for the external signer contains a list of checklist items (s)he must tick. SignRequest renders these checkboxes in the correct checklist item rows.

### 2.2.3. Signer and signing status

SignRequest sends events to the back-end, indicating when a signer signed, all signers signed, and some other events. The application uses these events to show the correct *document status*.

Once all signers signed the document, SignRequest sends the PDF including signatures to the back-end. The back-end then replaces the PDF in the database, so the user can download the signed document in the application.

When the last signer signed the document, SignRequest needs some time to process the document. The final `SIGNED` status can take a while (10s of seconds, sometimes minutes) to arrive at the back-end. The system therefore sets a flag (`AWAITING_CALLBACK`) when the user returns from SignRequest, to bridge this time gap for calculating the document status.

# 3. Document statuses

Fuelboss shows a *document status* in its nomination overview page. The document status is calculated per part by combining the progress of filling in the checklist and the signing statuses of the PDF.

## 3.1. Available statuses

1. ‘Not started’: neither bunker nor receiving party started filling in the checklist part
2. ‘In progress’ the bunker and/or receiving party started filling in the checklist part
3. ‘Completed’: a PDF was created from the checklist part
4. ‘Pending signatures’: the signers were assigned to the PDF, awaiting their signatures
5. ‘Signed’: all signers signed the PDF

## 3.2. Checklist flow assumptions

The system assumes that the user determines himself when the checklist is filled in ‘enough’. Since the system cannot determine that for the user, it relies on creating the PDF as marking it as ‘Completed’. This resembles reality quite well: when using a paper checklist, both parties start signing when they agree on all checked items and entered data. In other words, one does not alter the checklist content after signing it. And that works perfect for the ‘creating PDF, then signing it’ analogy.

The system allows a user to make changes to the checklist after creating/signing the PDF, such as checking/unchecking items and changing entries in the data tables. The system assumes that the user takes responsibility to create a new PDF and initiate a new signing operation.

# 4. Technical

This part adds technical details which are not covered by earlier sections.

## 4.1. Data model

The `SafetyChecklist` model supports all types: IAPH, Gothenburg and TR56. Some model properties are used for all types, some for a single type. All fields in the `DASafetyChecklist` class are by default for all checklist types, unless indicated otherwise.

Checklists are divided per part, so `checklistA`, `checklistB`, etc. It differs per checklist type which `checklist*` lists are populated.

## 4.2. External signers and checkboxes

In some cases, an external signers needs to check some items. These are stored in the `externalSignerCheckboxes`. The external signer has no user account, so (s)he can only fill it in while signing. The PDF service includes a SignRequest checkbox tag where needed, so that the external signer still has the items checked on the signed version of the document.

## 4.2. System assumptions

1. A nomination can have 0 or 1 safety checklists
2. The safety checklist `_id` always equals the `nomination.eventId`
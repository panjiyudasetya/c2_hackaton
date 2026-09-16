---
id: confluence:773488656
source: confluence
type: page
space: TC
title: PDA Tool / Port Cost Estimator
author: Daan Spikker (Unlicensed)
date: '2026-01-05'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/773488656
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/773488656
---
# PDA Tool / Port Cost Estimator

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/773488656  

## Content

PDA tool is the pro-forma disbursement (PDA) tool and is used by Agency GAC Rotterdam to communicate the PDA to their customers. It should represent an accurate projectino of expected port costs and costs for port services. It is shared through PDF and e-mail with their customers.

Users are the agents at GAC using it on a daily basis to create the PDAs in a PDF and set it to their customers. The PDA is used for Amsterdam and Rotterdam

Use:

* User selects port and searches for a ship in CSI.
* Certain relevant data is populated by CSI (LOA,Length between perpendiculars, DWT, Gross Tonnage). Unavailability of data is not seen as an issue, user can manually add it, and the delivery of data is outside of contract scope.

[Video introducing PDA Tool functional aspects can be found here.](https://drive.google.com/file/d/1icwPReKEoNzPsF4aPbdhmqYoFdtA39o7/view)

### Key functional elements of the tool include:

* **Ship Data Integration:** Users can select a port and search for a ship in CSI (Ship Information System), which populates relevant data like LOA, Length between perpendiculars, DWT, and Gross Tonnage. Users can manually add missing data.
* **Cost Calculation and Management:**

  + **Pilotage and Towage:** Users can specify helicopter pilotage and water depth. The tool calculates additional charges for towage, which can have variable rates based on gas prices and may include discounts.
  + **Mooring and Berthing:** It calculates mooring costs based on mooring type (buoy or jetty) and vessel length, accounting for differences between inbound and outbound movements, including linesmen costs in Amsterdam. It also handles berth shifts.
  + **Port-Specific Tariffs:** The tool automatically applies port-specific tariffs (e.g., Amsterdam vs. Porto), including constant lock fees in Amsterdam.
  + **Discounts and Surcharges:** Discounts and surcharges are applied to the full towage cost for either inbound or outbound.
  + **Fee Maintenance:** Port fees, including tax fees from towage companies, are manually maintained through communication with GAC and official websites, and stored in a properties file with date-specific applicability to manage price changes.
  + **Calculation Page:** The calculation page displays various fees (waste, harbor dues, reporting, custom fees, bird shift entries), allows users to unfold details for each fee, and shows excluded costs for transparency. It also displays zero costs and warnings for missing required values (e.g., draught).
  + **Cost Control:** Users can enable or disable specific costs (e.g., center fees, linesmen) to adjust calculations.
* **Data Persistence:** Calculations are saved to a backend database upon each calculation.( but they’re not retrievable by the user)
* **Testing:** The tool includes unit tests for virtually every calculation case.
* **PDF Export:** Users can export the PDA as a PDF with options for basic, cost parts, and detailed exports (including calculation explanations). The PDF includes static vessel details, customer information, totals, and can incorporate barcodes and company-specific information.
* **PDF Sharing:** Generated PDFs are not stored in the tool but downloaded by the GAC users and then shared with customers.
* **Upcoming Developments:** Changes are planned for the Port of Amsterdam to incorporate sub-port specific port tariffs (e.g., Velsen, Beverwijk) requiring backend updates and frontend adjustments for cargo handling based on specific port locations.

**recordings:**

5th january 2026 - short catch-up on work done in december and next steps to get to 2026 release<https://drive.google.com/file/d/1r3sca46AEEAALS5-AGb7afJD568ub-O7/view?usp=sharing>
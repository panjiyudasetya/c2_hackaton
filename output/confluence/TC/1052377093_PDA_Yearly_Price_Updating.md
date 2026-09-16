---
id: confluence:1052377093
source: confluence
type: page
space: TC
title: PDA Yearly Price Updating
author: Pim van den Toorn (Unlicensed)
date: '2025-12-22'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1052377093
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1052377093
---
# PDA Yearly Price Updating

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1052377093  

## Content

21falsedefaultlisttrue

# 1. The Netherlands

## 1.1. Pilotage - Loodswezen

Loodswezen does all the pilotage in the netherlands, with the cost tables being the same everywhere. Which columns should be used does differ between ports and areas.

### Where to find

Rotterdam - <https://loodswezen.nl/en/rotterdam-rijnmond-region/>

Amsterdam - <https://loodswezen.nl/en/amsterdam-ijmond-region/>

The tables for to/from the sea, shifting, and to/from the rendezvous point are the same everywhere, but check the different regions for which columns should be used. The helicopter costs are also the same.

### When to update

New prices start on the 1st of January, they are posted sometime in December.

### How to update

#### 1. Tariff columns

Check per port if the tariff columns per area have changed, so far they have never, so those aren’t dated yet.

#### 2. Tariff tables

There are three tariff tables, for to/from the sea, for shifting, and for to/from a rendezvous point. These are the same for all regions in the Netherlands.

You can copy these tables per page and paste them into `util/formatPilotage.py` in the project. When you run this, it will print the rows formatted for pasting into the properties. Remember to delete the `≤` on the very first row and column, and replace the `≥196` on the last row/first column with the int max `2147483647`.

#### 3. Helicopter costs

These can be found at the end of part 4 - additional costs, these are the same for all regions in the Netherlands. Here 4.6.1:

## 1.2. Reporting - Teqplay / Intertransis / Dirkzwager

### Where to find

These costs are posted in the `Tariffs of Third Parties` on the Rotterdam seaport tariffs page <https://www.portofrotterdam.com/en/sea-shipping/seaport-dues>, but these are usually posted in January or later. Ask Daan for these prices, the Teqplay ones we have ourselves, the Intertransis and Dirkzwager ones he could request from our partners.

### When to update

New prices start on the 1st of January.

### How to update

Add the new prices to the reporting tables and using the int max for the last row

# 2. Rotterdam

## 2.1. Waste fees

### Where to find

These can be found in the General Terms and Conditions Including Port Tariffs on this page: <https://www.portofrotterdam.com/en/sea-shipping/seaport-dues>. They are in `Annex 1: Port Tariffs`, paragraph 3 `Rates for waste fee for Seagoing Vessels`

### When to update

New prices start on the 1st of January, they are posted sometime in December.

### How to update

Add the starting price, the cost per GT and the max to the table:

NOTE: for 2026 there is a new max for cruise ships is added, implement this change

## 2.2. Port Dues

### Where to find

These can be found in the General Terms and Conditions Including Port Tariffs on this page: <https://www.portofrotterdam.com/en/sea-shipping/seaport-dues>. They are found in `Annex 1: Port Tariffs`.

### When to update

New prices start on the 1st of January, they are posted sometime in December.

### How to update

#### 1. Standard steps

Paragraph `1.2 Rates` has the basic principles, the steps for the calculation and the tables used in these steps. These calculations are laid out step-by-step in the backend, and if they change, this new logic should be added. Add the tables to the property file, some ships have different rates if they are in a type of service:

#### 2. Special rates

Paragraph `1.3 Special rates`. These are currently not in the logic, but these could be nice to add later.

#### 3. Discounts

Paragraph `1.4 Discounts`. These are calculated in the basic rates steps. The efficiency discount table is in the properties, the ESI and Green Award discounts are in the logic.

## 2.3. Buoy, dolphin and public quay dues

### Where to find

These can be found in the General Terms and Conditions Including Port Tariffs on this page: <https://www.portofrotterdam.com/en/sea-shipping/seaport-dues>. They are found in `Annex 1: Port Tariffs`, paragraph 2.

### When to update

New prices start on the 1st of January, they are posted sometime in December.

### How to update

These are the mooring costs with defaults in the frontend, they are not present anywhere in the backend. The defaults in the frontend should be updated.

## 2.4. Towage - Svitzer / Fairplay / Boluda

### Where to find

These costs are posted in the `Tariffs of Third Parties` on the Rotterdam seaport tariffs page <https://www.portofrotterdam.com/en/sea-shipping/seaport-dues>, but these are usually posted in January or later. Ask Daan, he could request these from our partners.

### When to update

New prices start on the 1st of January.

### How to update

Add the new tables to the properties file and make sure the columns are correct, these are different per company.

The costs for shifting is handled in the logic, make sure these are still correct:

## 2.5. Linesmen - KRVE / AJVK

### Where to find

These costs are posted in the `Tariffs of Third Parties` on the Rotterdam seaport tariffs page <https://www.portofrotterdam.com/en/sea-shipping/seaport-dues>, but these are usually posted in January or later. Ask Daan, he could request these from our partners.

### When to update

New prices start on the 1st of January.

### How to update

Add the new tables to the properties, the last line is the additional cost per 5 meters.

# 3. Amsterdam Area

## 3.1. Waste fee

### Where to find

<https://www.portofamsterdam.com/en/shipping/sea-shipping/services-facilities/waste/tariffs-waste-delivery-entitlement>. And maybe also check the “Decision HAP” under “More information” on the bottom, this is where they get the rates from, and this might be updated before the rest of the website.

### When to update

New prices start on April 1st, but they don’t change every year.

### How to update

Add the new costs tot the properties for both cruise ships and other vessels

## 3.2. Towage - Port Towage Amsterdam

### Where to find

<https://www.towageamsterdam.com/tariff-calculator/> → Download tariff sheet

### When to update

New prices start on April 1st, but they may be months late. Daan could maybe get these from a partner.

### How to update

Copy the tables into the properties. In the properties the second and third column are row 1 from the sheet, and the sixth and seventh column are row 5. This is because there used to be more rows in the tariff sheet, but those got merged. Add the assistance on the NS canal (row 3) as well.

## 3.3. Linesmen - Koperen Ploeg / Corps van Vletterlieden

### Where to find

Both their costs are not posted on their websites, Daan has to get these from partners.

These are their website, but they don’t offer much:

<https://www.vletterlieden.nl/> <https://www.dekoperenploeg.nl/>

### When to update

New prices start on January 1st.

### How to update

Add the updated tables to the properties.

# 4. Amsterdam

## 4.1. Port dues

### Where to find

<https://www.portofamsterdam.com/en/shipping/sea-shipping/harbour-dues> → `General terms and Conditions`, at the end the `List of rates`.

### When to update

New prices start on January 1st. At the time of writing, , only the Dutch version of the 2026 prices have been released.

### How to update

`I. Seagoing vessels with cargo, not sailing in scheduled service` has the base tariff for ships not in a service, and the coal/non-petroleum cokes, as this has a special rule noted with the \* below the table:

`II. Seagoing vessels with cargo, sailing in scheduled service` has the tariffs for ships in a service:

`III. Miscellaneous rates for Seagoing vessels` has the no cargo tariffs:

`IV. Environmental discounts and -incentives for seagoing vessels` has the Green Award discount and the ESI incentive, these are in the logic.

## 4.2. Quay dues, buoy dues and dolphin dues

### Where to find

<https://www.portofamsterdam.com/en/shipping/sea-shipping/harbour-dues> → `General terms and Conditions`, the `List of rates`, then at the end the `Rates for quay dues, buoy dues and dolphin dues`

### When to update

New prices start on January 1st. At the time of writing, , only the Dutch version of the 2026 prices have been released.

### How to update

These are the mooring costs with defaults in the frontend, they are not present anywhere in the backend. The defaults in the frontend should be updated.

# 5. Beverwijk

## 5.1. Port dues

### Where to find

<https://lokaleregelgeving.overheid.nl/ZoekResultaat?titel=zeehavengelden&datumrange=op&filter-id--ss-gemeenten=bever&gemeenten=Beverwijk&indeling=>, these are the search results for “zeehavengelden” (Sea port dues) by the Beverwijk municipality. They are only in Dutch.

### When to update

New prices start on January 1st.

### How to update

Add the new rates at the bottom of the page to the properties

# 6. IJmuiden

## 6.1. Port dues

### Where to find

<https://zeehaven.nl/en/shipping/port-dues/>

### When to update

New rates start on March 1st.

### How to update

Add the Sea-going vessel rate, the no-cargo rate, the cruise ship rate, and the ISPS rate to the properties file
---
id: confluence:814972977
source: confluence
type: page
space: TC
title: Vessel Compliance (Navista) - Frontend
author: Fauzan Rifqy
date: '2025-07-31'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/814972977
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/814972977
---
# Vessel Compliance (Navista) - Frontend

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/814972977  

## Content

A modern React + TypeScript web application for managing vessel compliance, terminal clearances, and administrative tasks. The app features robust authentication (Auth0 & NXTPort), role-based dashboards, and a modular, scalable architecture.

## Repository

<https://github.com/teqplay/vesselcompliance>

## Infrastructure

|  |  |
| --- | --- |
| Framework | `typescript` `react` `react-router` |
| Auth | `auth0` |
| Styling | `scss` |
| Tools | `pnpm` `vite` `vitest` `eslint` `prettier` `github-actions` `sentry` |

## Roles

| Feature | Developer | Super User | Terminal | Charterer | Trading Operator | Trader | Vetting |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Dashboard Access** |  |  |  |  |  |  |  |
| Main Dashboard | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Terminal Dashboard | ❌ | ✅\* | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Administrative Features** |  |  |  |  |  |  |  |
| Admin Panel Access | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| User Management | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| View All Users | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Edit User Roles | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Role Assignment Permissions** |  |  |  |  |  |  |  |
| Assign Any Role | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Assign Terminal Roles | ✅ | ✅ | ✅\*\* | ❌ | ❌ | ❌ | ❌ |
| Assign Business Roles | ✅ | ✅ | ❌ | ✅\*\* | ✅\*\* | ✅\*\* | ✅\*\* |
| **Compliance Management** |  |  |  |  |  |  |  |
| View Compliance Records | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Create New Compliance | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Edit Compliance (Standard) | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Edit Compliance (Unrestricted) | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Clearance Management** |  |  |  |  |  |  |  |
| View Terminal Clearances | ✅ | ✅\* | ✅ | ❌ | ❌ | ❌ | ❌ |
| Manage Terminal Clearances | ✅ | ✅\* | ✅ | ❌ | ❌ | ❌ | ❌ |
| Access Clearance by ID | ✅ | ✅\* | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Communication Features** |  |  |  |  |  |  |  |
| Chat/Comments | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Audit Trail Access | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Data Management** |  |  |  |  |  |  |  |
| Filter & Search | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Custom Filters | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Column Configuration | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Export/Download | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

### Legend

* ✅ **Full Access**: Complete access to the feature
* ❌ **No Access**: No access to the feature
* ✅\* **Conditional Access**: Access depends on company type (Terminal company required)
* ✅\*\* **Limited Access**: Access with restrictions based on company type

### Special Notes

#### Super User Terminal Access

* Super Users only get Terminal Dashboard access if their company type is "TERMINAL"
* If not associated with a terminal company, they use the standard Dashboard

#### Role Assignment Restrictions

* **Terminal Companies**: Can only assign `ROLE_TERMINAL_CUSTOMER_SERVICE`
* **Non-Terminal Companies**: Can assign business roles: `ROLE_CHARTERER_OPERATOR`, `ROLE_TRADER`, `ROLE_TRADING_OPERATOR`, `ROLE_VETTING_USER`
* **Developers**: Can assign any role without restrictions

#### Create Compliance Restrictions

* Terminal users and Super Users cannot create new compliance records
* The "Create New" button is hidden for these roles
* This restriction applies to roles: `ROLE_TERMINAL_CUSTOMER_SERVICE`, `ROLE_SUPER_USER`

#### Editing Permissions

* **Standard Editing**: Normal users can edit compliance records with standard validation and restrictions
* **Unrestricted Editing**: Super Users can bypass normal editing limitations and restrictions

---

## Code Practice

Vessel Complience - Code Practice
---
id: confluence:794165251
source: confluence
type: page
space: TC
title: Augment Code Analysis - Comprehensive Explanation of Complex Components in
  Chorus
author: Milzam Abi Karami
date: '2025-07-08'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/794165251
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/794165251
---
# Augment Code Analysis - Comprehensive Explanation of Complex Components in Chorus

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/794165251  

## Content

Date:

12falsenonelisttruenote

**Prompt:**

What are the most complex things inside the repository? can you explain it as well.

**Prompt:**

What are the most complex things inside the repository? can you explain it as well.

## 1. LNG Computation Service

### How It Works

The `LNGComputationService` performs scientific calculations for LNG (Liquefied Natural Gas) properties based on its composition:

1. **Input Data**:

   * LNG composition (percentages of methane, ethane, propane, etc.)
   * Temperature and pressure conditions
   * Reference temperatures for calculations
2. **Core Calculations**:

   * **Density Calculation**: Uses the Klosek-McKinley method to calculate LNG density based on composition and temperature
   * **Calorific Value**: Calculates both gross and net calorific values (energy content) in MJ/kg and MJ/m³
   * **Methane Number**: Uses the PKI (Propane Knock Index) method to calculate methane number, which indicates knock resistance
   * **Wobbe Index**: Calculates this key parameter for gas interchangeability
3. **Vector-Based Approach**:

   * Uses `LNGVector` and `LNGExtendedVector` classes to represent composition
   * Implements vector arithmetic operations for efficient calculations
   * Supports blending calculations when mixing different LNG compositions
4. **Lookup Tables**:

   * Uses interpolation tables for temperature-dependent properties
   * Loads reference data from JSON files (e.g., "calculations/table2-sqrt-bj.json")
5. **Standards Compliance**:

   * Implements calculations according to international standards
   * Supports different reference temperatures (0°C, 15°C, 20°C, 25°C)

## 2. Prompt Negotiation System

### How It Works

The negotiation system manages the lifecycle of bunkering nominations:

1. **Event-Based Architecture**:

   * Uses an event model with `DAPromptBaseEvent` as the base class
   * Specific event types (nomination, counter, acceptance, etc.) extend this base
   * Events form a chain representing the negotiation history
2. **State Machine**:

   * Nominations progress through states: PROPOSED → COUNTERED → ACCEPTED → SCHEDULED → COMPLETED
   * Each state transition has validation rules and triggers side effects
   * `PromptNegotiationService` manages these transitions
3. **Business Rules Engine**:

   * Validates transitions based on user roles, company relationships
   * Implements complex rules about who can counter/accept/reject
   * Handles delegation scenarios where third parties execute bunkering
4. **Notification System**:

   * Triggers notifications on state changes
   * Notifies relevant parties via email
   * Supports different notification templates based on event type
5. **Audit Trail**:

   * Maintains complete history of negotiations
   * Records timestamps and user information for all actions
   * Supports reporting and analytics on negotiation patterns

## 3. EBDN Generation and Parsing

### How It Works

The Electronic Bunker Delivery Note (EBDN) system handles document generation and data extraction:

1. **Data Model**:

   * `DAEBDN` class represents the structured data
   * Contains sections for LNG properties, quantities, signatures
   * Supports both standard and custom fields
2. **Excel Integration**:

   * Uses Apache POI library to read/write Excel files
   * Maps cells to data fields using configuration
   * Handles formula evaluation and cell formatting
3. **Template System**:

   * Configurable templates for different companies
   * Company-specific branding and field layouts
   * Version control for templates
4. **Calculation Engine**:

   * Performs automatic calculations based on input data
   * Calculates derived values (e.g., energy content from volume)
   * Validates data consistency
5. **PDF Generation**:

   * Converts EBDN data to PDF format
   * Supports digital signatures
   * Maintains formatting for legal compliance

## 4. Permission System

### How It Works

The permission system controls access to data and operations:

1. **Multi-Level Model**:

   * **Role-Based**: Basic permissions tied to roles (ADMIN, USER, CAPTAIN, etc.)
   * **Company-Based**: Permissions based on company relationships
   * **Object-Level**: Fine-grained permissions on specific objects
2. **Company Relationships**:

   * Handles parent/child company relationships
   * Supports corporation structures with multiple subsidiaries
   * Implements supplier/customer relationship permissions
3. **Permission Evaluation**:

   * `PermissionEvaluatorImpl` implements Spring Security's PermissionEvaluator
   * Uses method-level security annotations
   * Evaluates complex conditions like "can user from company X see nomination from company Y?"
4. **Delegation Handling**:

   * Special permissions for delegated operations
   * Tracks original and delegated entities
   * Maintains appropriate access control during delegation
5. **Implementation**:

   * Uses Spring Security framework
   * Integrates with Auth0 for authentication
   * Custom authorization rules in `hasPermission()` methods

## 5. PDF Generation

### How It Works

The PDF generation system creates standardized documents:

1. **Template Engine**:

   * Uses Thymeleaf for HTML templates
   * Dynamic content insertion based on data models
   * Conditional sections based on configuration
2. **Rendering Process**:

   * Converts HTML templates to PDF using Flying Saucer
   * Handles precise positioning and pagination
   * Supports embedded images and logos
3. **Document Types**:

   * EBDN (Electronic Bunker Delivery Note)
   * SOF (Statement of Facts)
   * Safety checklists (IAPH, Gothenburg)
   * Quality reports
4. **Customization**:

   * Company-specific branding
   * Configurable sections and fields
   * Multiple language support
5. **Digital Signing**:

   * Integration with SignRequest service
   * Manages signature workflows
   * Tracks signature status

## 6. Company Relationship Model

### How It Works

The company relationship model manages business relationships:

1. **Core Entities**:

   * `DACompany` represents companies in the system
   * `corporationId` links subsidiaries to parent companies
   * Company types (CUSTOMER, VENDOR, BOTH) define basic roles
2. **Hierarchical Structure**:

   * Corporations can have multiple subsidiary companies
   * Permissions cascade through the hierarchy
   * Corporate admins can manage all subsidiaries
3. **Business Relationships**:

   * Tracks supplier/customer relationships
   * Manages contracts between companies
   * Handles delegation relationships
4. **Permission Propagation**:

   * Company administrators can manage their company
   * Corporate administrators can manage all subsidiaries
   * System administrators can manage all companies
5. **Implementation**:

   * MongoDB document structure with references
   * Service layer in `CompanyService` implements business logic
   * Helper methods like `corporationCompanyIds()` to navigate relationships
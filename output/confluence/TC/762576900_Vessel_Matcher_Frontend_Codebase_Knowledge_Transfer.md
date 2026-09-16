---
id: confluence:762576900
source: confluence
type: page
space: TC
title: Vessel Matcher Frontend Codebase Knowledge Transfer
author: Fauzan Rifqy
date: '2025-06-13'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/762576900
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/762576900
---
# Vessel Matcher Frontend Codebase Knowledge Transfer

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/762576900  

## Content

|  |  |
| --- | --- |
| Repo | <https://github.com/teqplay/vesselmatcher> |

## Core Technologies Stack

### Frontend Layer

* React 18.3.1 (UI Framework)
* Apollo Client 3.13.6 (GraphQL State Management)
* React Router 6.14.2 (Navigation)
* SCSS (Styling)
* Mapbox GL 2.15.0 (Maps)
* React Table 7.8.0 (Data Tables)

### Development Tools

* ESLint (Code Quality)
* Prettier (Code Formatting)
* Vitest (Testing)
* TypeScript 5.2.2 (Type Safety)
* Sentry (Error Monitoring)

### Build & Deployment

* Vite 6.2.6 (Build Tool)
* AWS S3 (Static Hosting)
* CloudFront (CDN)
* GitHub Actions (CI/CD)

## Apollo Client Architecture

### GraphQL Integration

* HTTP Link (REST API communication)
* WebSocket Link (Real-time subscriptions)
* Authentication Link (JWT token management)
* InMemoryCache (Client-side caching)
* Split Link (HTTP vs WebSocket routing)

### Authentication

* Auth0 Integration ([teqplay.eu.auth0.com](http://teqplay.eu.auth0.com))
* JWT Token Management
* Automatic Token Refresh
* Environment-specific Client IDs

## Core Component Hierarchy

### App Structure

App
├── AuthProvider (Authentication wrapper)
├── Menu (Navigation)
├── Routes
│ ├── FleetPage (Ship management interface)
│ │ ├── FleetNav (Ship navigation)
│ │ ├── FleetOverview (Ship list/map view)
│ │ ├── FleetTable (Ship data table)
│ │ └── ShipPlanningContainer (Ship planning details)
│ ├── OrdersPage (Cargo order management)
│ │ ├── OrderFilterForm (Search/filter controls)
│ │ └── OrderTable (Order data table)
│ ├── EmailsPage (Email processing interface)
│ │ ├── EmailsPageAll (All emails view)
│ │ ├── EmailsPageIssues (Problem emails)
│ │ └── EmailsPageAdvanced (Advanced search)
│ ├── BrokerPage (Broker cargo interface)
│ ├── LocationsPage (Port/location management)
│ └── StatisticsPage (Analytics dashboard)
├── Popup System
│ ├── EmailDetailsPopup (Email content viewer)
│ ├── OrderDetailsPopup (Order details editor)
│ ├── PortSelectionPopup (Port picker)
│ └── Various confirmation dialogs
└── Global Components
├── LocationMap (Mapbox integration)
├── ShipDetailsTooltip (Ship information)
└── Toast notifications

## Key Data Flows

### Email Processing

Automated parsing of cargo emails with confidence scoring

### Ship-Order Matching

Algorithm matches available ships with cargo orders based on location, capacity, and timing

### Real-time Updates

WebSocket subscriptions for live data synchronization

### Location Intelligence

Geographic calculations for travel distances and route optimization

## Backend Communication

### Base URLs

* Development: [https://backendvesselmatcher.dev.teqplay.com](https://backendvesselmatcher.dev.teqplay.com/)
* Production: [https://backendvesselmatcher.teqplay.nl](https://backendvesselmatcher.teqplay.nl/)
* Localhost: [http://localhost:8080](http://localhost:8080/)

### API Features

* GraphQL API: Single endpoint for all data operations
* WebSocket: Real-time subscriptions for live updates
* Authentication: JWT tokens with Auth0 integration
* Error Handling: Centralized error processing with Sentry integration

## Key Architecture Decisions

### Technology Choices

* Apollo Client over Redux: GraphQL-first approach with built-in caching
* Functional Components: Modern React with hooks throughout
* TypeScript: Full type safety across the codebase
* Vite over Webpack: Faster development and build times

## Development Environment

### Pre-commit Process

* ESLint: Checks for code quality issues and React best practices

### Testing Framework

* Vitest: Modern test runner with Jest compatibility
* jsdom: DOM environment for testing

## Runtime Configuration

// Backend environment detection
const BACKEND\_ENVIRONMENT = localStorage['BACKEND\_ENVIRONMENT'] || 'development'
// API base URLs
const BASE\_URL = {
development: 'https://backendvesselmatcher.dev.teqplay.com',
production: 'https://backendvesselmatcher.teqplay.nl',
localhost: 'http://localhost:8080'
}
// Auth0 configuration
const AUTH0\_DOMAIN = 'teqplay.eu.auth0.com'
const AUTH0\_CLIENT\_ID = BACKEND\_ENVIRONMENT === 'production'
? 'Fzr3K8RBLtvKa4DWtXWd3T2HvMok4Wby'
: 'tnBNFyHOTwndUJ2zAzSq5Kt4eAytF0IJ'

## Entry Point & Authentication

### Authentication Guard

// Authentication check in App component
if (loading || !userAuth || !userProfile) {
return <Login loading={loading} error={error} handleLogin={handleLogin} />
}
// Main application render with providers
return (
<ApolloProvider client={client}>
<UserProfileContext.Provider value={{ userProfile }}>
<ThemeContextProvider companyId={userProfile.companyId} theme={theme} setTheme={setTheme}>
<BrowserRouter>
<div className="app">
<Menu userAuth={userAuth} handleLogout={handleLogout} />
<Routes />
<ToastContainer />
</div>
</BrowserRouter>
</ThemeContextProvider>
</UserProfileContext.Provider>
</ApolloProvider>
)

### Authentication Requirements

* Valid Auth0 JWT token
* User profile loaded
* Company ID assigned

## Route Mapping

### Application Routes

| Path | Component | Description | Access Level |
| --- | --- | --- | --- |
| `/fleet/:shipId?` | FleetPage | Ship management and planning | Authenticated |
| `/orders/:orderId?` | OrdersPage | Cargo order management | Authenticated |
| `/emails/*` | EmailsPageRoute | Email processing interface | Authenticated |
| `/broker` | BrokerPage | Broker cargo interface | Authenticated |
| `/locations/:locationId?` | LocationsPage | Port/location management | Authenticated |
| `/statistics` | StatisticsPage | Analytics dashboard | Authenticated |

### Route Features

* **Dynamic Parameters**: Ship IDs, Order IDs, Email IDs in URLs
* **Nested Routes**: Email sub-routes for different views
* **Default Redirects**: Fallback to /fleet for unknown routes

## Data Models

### Entity Relationships

#### Ship

* MMSI, IMO, Name
* Technical specs (DWT, GT, Speed)
* Holds[] (dimensions)
* LatestVisit
* Profile (visibility settings)

#### Visit

* Ship reference
* Port information
* Arrival/Departure times
* Matches[] (suitable orders)
* UserVisitStatus (user interactions)

#### Order

* Quantity (cargo amount)
* Laycan (loading dates)
* Load/Discharge ports
* Product, rates, commission
* Sources[] (email origins)
* TravelDistance (routing data)

#### Email

* Message metadata
* ParsedOrders[] (extracted cargo)
* ParsedPositions[] (ship positions)
* Score (parsing confidence)
* UserInput (manual corrections)

#### Location

* Names[], Country, UNLOCODE
* Geographic coordinates
* Type (PORT/COUNTRY/REGION)
* Update tracking

## API Integration

### GraphQL Operations

#### Queries

* **ships**: Fleet management data
* **orders**: Cargo order search
* **emails**: Email processing results
* **locations**: Port/location data
* **statistics**: Analytics data

#### Mutations

* **hideShip/showShip**: Fleet visibility
* **updateOrder**: Order modifications
* **updateLocation**: Port data changes
* **User interaction tracking**: Various user actions

#### Subscriptions

* **Real-time email counters**: Live email processing statistics
* **Live order updates**: Ship-cargo matching updates
* **Ship position changes**: Real-time location updates

### API Features

* **Automatic Token Refresh**: Seamless JWT renewal
* **Error Handling**: Centralized GraphQL error processing
* **Optimistic Updates**: Immediate UI feedback
* **WebSocket Fallback**: Graceful degradation for real-time features

## Core Features

### Fleet Management

* **Ship Visibility Control**: Hide/show ships in fleet view
* **Ship Planning**: Match ships with suitable cargo orders
* **Location Tracking**: Latest port visits and positions
* **Capacity Matching**: Algorithm considers ship specifications
* **Distance Calculations**: Travel time and route optimization
* **Interactive Map**: Geographic visualization of ships and ports

### Order Management

* **Advanced Filtering**: Search by ports, dates, cargo type, quantity
* **Real-time Matching**: Live updates of ship-order compatibility
* **Source Tracking**: Link orders back to original emails
* **User Interactions**: Mark orders as read, favorite, or hidden
* **Travel Distance**: Automatic calculation of ballast distances
* **Commission Tracking**: Broker fee management

### Email Processing

* **Automated Parsing**: Rule-based extraction of cargo information
* **Confidence Scoring**: Quality assessment of parsed data
* **Manual Corrections**: User override of automated parsing
* **Issue Detection**: Identification of problematic emails
* **Advanced Search**: Regex and field-specific filtering
* **Real-time Counters**: Live statistics of processing results

### Location Intelligence

* **Port Database**: Comprehensive global port information
* **Geographic Search**: Location-based filtering and matching
* **UNLOCODE Integration**: Standard port code support
* **Custom Locations**: User-defined location management
* **Map Visualization**: Interactive port and ship positioning
* **Distance Calculation**: Multiple routing algorithms

### Analytics & Statistics

* **Processing Metrics**: Email parsing performance statistics
* **Entity Recognition**: Success rates for different data types
* **Trend Analysis**: Historical processing performance
* **Error Tracking**: Identification of common parsing issues
* **Performance Monitoring**: System health and usage metrics

## Advanced Features

### Real-time Capabilities

* **WebSocket Synchronization**: Live updates across all clients
* **Connection Management**: Automatic reconnection and error handling
* **Cache Refresh**: Syncs missed data after reconnection

### Development Features

* **Multi-environment**: Development, staging, and production deployments
* **Theme Support**: Company-specific branding and themes
* **Responsive Design**: Mobile and desktop optimization
* **Keyboard Shortcuts**: Power user navigation features
* **Debug Mode**: Comprehensive logging for troubleshooting

## WebSocket Implementation

### Real-time Data Subscriptions

#### Email Counter Updates

* **Purpose**: Live email processing statistics
* **Data**: Counter changes for parsed emails with issues
* **Usage**: Real-time updates in email issues counter

#### Ship-Order Matches

* **Purpose**: Live cargo order matching for ships
* **Data**: New/updated/deleted order matches
* **Parameters**: Ship ID, port, departure, capacity limits
* **Usage**: Real-time notifications of suitable cargo orders

#### User Visit Status

* **Purpose**: Collaborative user interactions
* **Data**: Read/favorite/hidden order status changes
* **Usage**: Syncs user actions across multiple sessions

### WebSocket Features

* **Automatic Reconnection**: Handles connection drops gracefully
* **JWT Authentication**: Secure token-based authentication
* **Error Notifications**: User-friendly connection status alerts
* **Cache Synchronization**: Refreshes data after reconnection
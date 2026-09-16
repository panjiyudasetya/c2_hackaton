---
id: confluence:815333377
source: confluence
type: page
space: TC
title: SSL App (Alongside Monitor) - Mobile Application
author: Fauzan Rifqy
date: '2025-07-31'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/815333377
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/815333377
---
# SSL App (Alongside Monitor) - Mobile Application

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/815333377  

## Content

A React Native mobile application for Ship Spare Logistics (SSL) that provides real-time monitoring of vessel deliveries, barge tracking, and logistics coordination. The app features Auth0 authentication, interactive maps with Mapbox, and comprehensive delivery management for maritime operations.

## Repository

[GitHub - teqplay/ssl-app](https://github.com/teqplay/ssl-app)

---

## Infrastructure

| Category | Tech Stack |
| --- | --- |
| **Framework** | `react-native` `typescript` `expo-bare-workflow` |
| **Auth** | `auth0` `react-native-auth0` |
| **Maps** | `mapbox-gl` `react-native-mapbox-gl` `maptiler` |
| **Navigation** | `react-navigation` `bottom-tabs` `native-stack` |
| **State** | `react-query` `async-storage` `immer` |
| **Tools** | `npm` `eslint` `prettier` `sentry` `fastlane` |
| **Platforms** | `ios` `android` `xcode` `android-studio` |

---

## Features

| **Feature** | **Description** | **Access** |
| --- | --- | --- |
| **Authentication** |  |  |
| Auth0 Login | Secure authentication with Auth0 integration | ✅ All Users |
| Token Management | Automatic token refresh and storage | ✅ All Users |
| **Map & Tracking** |  |  |
| Interactive Map | Real-time vessel tracking with Mapbox | ✅ All Users |
| Vessel Positioning | Live AIS data with MMSI/IMO tracking | ✅ All Users |
| Berth Visualization | Terminal berths and harbor polygons | ✅ All Users |
| Ship Filtering | Filter by trucks, barges, unassigned | ✅ All Users |
| **Delivery Management** |  |  |
| Barge Overview | Scheduled deliveries by barge | ✅ All Users |
| Truck Overview | Truck-based delivery tracking | ✅ All Users |
| Delivery Status | Real-time delivery progress tracking | ✅ All Users |
| Visit Details | Comprehensive visit information | ✅ All Users |
| **Scheduling** |  |  |
| Date Selection | Multi-date scheduling view | ✅ All Users |
| ETA/ETD Tracking | Estimated and actual times | ✅ All Users |
| Delivery Orders | Sequential delivery numbering | ✅ All Users |
| **Notifications** |  |  |
| Departure Alerts | Warnings for vessels leaving soon | ✅ All Users |
| Completion Status | Visual delivery completion indicators | ✅ All Users |
| **Settings** |  |  |
| User Profile | Account information and logout | ✅ All Users |
| Dark/Light Mode | Automatic theme switching | ✅ All Users |

---

## Special Notes

### Authentication System

* Uses **Auth0** with domain `teqplay.eu.auth0.com` for secure authentication
* Implements automatic token refresh with refresh tokens stored in AsyncStorage
* Backend integration with SSL API service for user session management
* Supports both development and production backend environments

### Map Integration

* **Mapbox GL** integration with custom ship icons (blue, orange, brown, gray)
* **MapTiler** for light/dark themed map styles
* Real-time vessel positioning using AIS data with MMSI and IMO numbers
* Interactive berth polygons showing terminal areas and harbor boundaries
* Custom ship markers with rotation based on course over ground

### Delivery Workflow

* **Barge Deliveries**: Organized by delivering barge with sequential order numbers
* **Truck Deliveries**: Grouped by truck with delivery scheduling
* **Unassigned Visits**: Separate tracking for visits without assigned delivery method
* **Status Tracking**: Visual progress indicators from ETA to delivery completion
* **Departure Warnings**: Alerts when ETD is within 2 hours without delivery

### Data Management

* **React Query** for efficient API data fetching and caching
* **Date Context** for synchronized date selection across all screens
* **Real-time Updates** with automatic refresh functionality
* **Offline Storage** using AsyncStorage for authentication persistence

### Platform Support

* **iOS**: Native iOS app with Xcode project configuration
* **Android**: Native Android app with Gradle build system
* **Expo Bare Workflow**: Ejected from managed Expo for native functionality
* **Fastlane**: Automated deployment for both iOS and Android platforms

### Development Environment

* **Node.js 16+** requirement for development
* **Android SDK 12.0** for Android development
* **Xcode** for iOS development
* **Metro** bundler for React Native development server

### Security & Monitoring

* **Sentry** integration for error tracking and performance monitoring
* **Privacy Policy** compliance with link to privacy policy
* **Secure Token Storage** with encrypted AsyncStorage implementation
* **API Error Handling** with comprehensive error reporting

### Deployment

* **Android**: AAB (Android App Bundle) generation with signed releases
* **iOS**: Archive and upload to App Store Connect with TestFlight
* **Version Management**: Automated version code generation from package.json
* **Environment Configuration**: Separate production and development backends
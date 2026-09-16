---
id: confluence:109477889
source: confluence
type: page
space: TC
title: Port Reporter
author: Richard van Klaveren
date: '2025-06-16'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/109477889
explicit_links: []
---
# Port Reporter

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/109477889  

## Content

* Main Goal(s):

  + Portcall: Providing notifications to users on actual and predicted timestamps around the portcall
  + Smartfleet: Following (smart) fleets of vessels around the globe
* Scope:

  + Portcall: Rotterdam, Amsterdam, Antwerp, Vlissingen, Terneuzen, Ghent, Corpus Christi, Singapore
  + Smartfleet: Global
* Users: 450+

  + Portcall: Agents, Terminals, Shipping line
  + Smartfleet: Terminals, port authorities
* Main Development: 2018 - 2020
* Team involved: Knowledge in team: Joaquin (BE), Damon (FE), David (FE), Richard (PO), Daan (PO)
* Product / project: Product (50 customers)
* Active knowledge required: Yes
* Tech stack: Kotlin, Mongo, RabbitMq, React + Typescript, Cordova

A video with a functional and technical introduction can be found [here](https://www.youtube.com/watch?v=7R_z91RwP8c)

The used slide-deck introducing technical high-level can be found [here](https://docs.google.com/presentation/d/1ZI_V4HQ-7XfccyBA__FZdCSxdBjeqXN9-pM4umXauYw)

Other resources:

* Drive folder: [Teqplay Ops / 1.Products / Port Reporter](https://drive.google.com/drive/folders/1a7kvQLi3jIa4rWT1Cp3W4RJpnCusyi-k)
* Confluence project page: Teqplay Confluence / Port Reporter
* Repository: <https://github.com/teqplay/portreporter-backend>
* Jira Board: [Projects / Port Reporter](https://teqplaybv.atlassian.net/jira/software/c/projects/PRP/boards/25)
* [Teqplay Diagram Architecture](https://app.diagrams.net/#G1X8QOivb0vE43umlODbmq_20WhMRW7K1f#%7B%22pageId%22%3A%22rDCxWZ16RrHVMkRNnX7i%22%7D)

## **Maritime Process supported**

PortReporter supports the **port call lifecycle**, enabling agents, terminals, and shipping companies to coordinate vessel arrivals, cargo operations efficiently. The process starts with charterers arranging for a vessel to call at a port, typically via a local agent. The agent plays a pivotal role, organizing services such as pilots, tugs, and boatmen, and handling financial transactions like disbursement accounts and service payments.

The critical window of three hours before a vessel’s arrival requires precise coordination. PortReporter enhances agent effectiveness by providing real-time notifications and a unified dashboard that helps track multiple port calls simultaneously. The platform enables transparent communication, compliance tracking, and electronic documentation through features like the **Electronic Statement of Facts (ESOF)**. Financial interactions—such as dynamic pricing and weekly invoice dispatches—are streamlined via automated invoicing integrated with the company’s accounting systems. The system also manages differing access levels and subscription models, catering to various stakeholders including agents, terminals, port authorities, and shipping lines.

## **Functional Process of PortReporter**

PortReporter delivers a **robust and feature-rich workflow** tailored to the daily operations of maritime agents and their stakeholders:

* **Vessel Monitoring & Notifications**: Agents monitor vessel status through a dashboard and receive critical updates via phone, email, SMS, and push notifications. A retry mechanism ensures delivery of high-priority alerts, especially during key time windows like pre-arrival.
* **Electronic Documentation & Port Call History**: The tool logs all relevant events during a port call through the ESOF. Additional details such as previous port visits, berth history, and authorization status are available.
* **User Roles & Permissions**: PortReporter supports granular user roles: admins, agency admins, and agents, each with defined capabilities. These roles extend across various company types (agencies, terminals, shipping lines).
* **Subscription Profiles**: Admins configure notification preferences by port event and medium for agents in different operational contexts (e.g., office vs. field). Subscriptions are auto-created during port call registration.
* **Nominations & Charging Logic**: When a shipping company nominates a vessel (e.g., during time charters), PortReporter uses a component called **Scrape Shark** to process nomination emails and allocate responsibility for notifications and charges accordingly.
* **Invoicing Workflow**: Invoices are generated weekly for vessels handled, with logic tied to nominations and port call data. The system supports credits, kickbacks, and tracks payment status through integration with internal accounting software (Exact).

In addition to these specific Portcall related notifications and additional module is integrated allowing the user to monitor fleets of vessels that somehow smartly can be grouped together. Conditions on which they can be grouped together contain:

* Automatically maintained based upon:

  + Vessel characteristics (like cargo type, size, and DWT)
  + Ports where the vessel has departed
  + Ports where the vessel is heading to
* Manually maintained based on manual grouping of vessels (e.g. fleet of competitor)

Smartfleet can be used to see the line-up of vessels for a certain port and period, but also to view what the competition is doing or to close last minutes deal and make sure these vessels do not store goods at competing terminal but at your own terminal.

## **Technical Overview of PortReporter**

PortReporter is a **mature, Spring Boot 3-based microservice application**, operating at the heart of the Teqplay tech ecosystem. Its backend architecture supports scalable and flexible event-driven processing:

* **Data Ingestion**: The system consumes event messages via **RabbitMQ**, including port call updates and smart fleet activity. Events may be processed immediately or scheduled (e.g., pilot boarding alerts set 3 hours in advance).
* **Port Call & Smart Fleet Processing**: Events are matched to port calls or fleets, updating the relevant records and triggering user notifications. MongoDB is used for persistence, chosen for its schema flexibility and rapid development adaptability.
* **Smart Fleet & Vessel Voyage Integration**: PortReporter integrates with other Teqplay modules like Smart Fleet (to manage dynamic vessel groups) and Vessel Voyage (to review ESOFs and port visit data).
* **Nomination Handling via Scrape Shark**: A dedicated service parses incoming nomination emails, linking them to port calls and determining billing and reporting requirements.
* **Component Integration**: The application communicates with shared services like CSI (for vessel data), POMA (port infrastructure), and uses APIs to pull and push data across Teqplay’s ecosystem. Various caching strategies are used (especially for static data from CSI), although the current system lacks cache invalidation controls—highlighted as a future improvement area.
* **Notification Providers**: The notification engine leverages SendGrid, Twilio, and Firebase to deliver multichannel messages.
* **Authentication & Access Control**: Keycloak handles identity and access management, while the admin portal allows impersonation for support and debugging purposes.

**Invoicing & External Integration**: Invoice logic is modular, rule-based, and linked directly to port call data. Final invoices are exported to **Exact**, Teqplay’s financial backend.
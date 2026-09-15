---
id: confluence:180846593
source: confluence
type: page
space: TC
title: Introduction for new developers
author: Fauzan Rifqy
date: '2024-12-18'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/180846593
explicit_links: []
---
# Introduction for new developers

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/180846593  

## Content

The team members are mentioned on the website: <http://teqplay.com/team>.

If anything is unclear don't hesitate to ask any of your colleagues.

## Languages, frameworks, libraries and tools

|  |  |
| --- | --- |
| **Technology Stack** | **Description** |
| Slack | Collaboration and communication platform. |
| Jira | Project management and issue tracking tool. |
| `current` Bitbucket `upcoming` GitHub | Code hosting platforms for version control and collaboration. |
| `legacy` LastPass `current` Bitwarden | Password management solutions for securing credentials. |
| `legacy` CRA (create-react-app) `current` Vite | Frontend development tools for setting up and managing the development environment of web applications |
| React | Frontend framework for building web applications. |
| TypeScript | Programming language providing static typing for JavaScript. |
| `legacy` leaflet `current` mapbox-gl | Library for interactive, customizable maps. |
| Sentry | Error monitoring and performance tracking tool. |
| REST-API | Interface standard for web services communication. |
| Auth0 | Authentication and authorization platform for most new tools. |
| GraphQL | Query language for APIs, used in some experimental projects. |
| Font Awesome | Icon library for scalable vector icons. |
| Sass (.scss files) | CSS preprocessor for styling web applications. |
| `current` CircleCI `upcoming` GitHub Actions | Continuous Integration tools for automated workflows. |
| Cordova | Framework for building mobile applications, used in Port Reporter, Watersport, RiverGuide. |
| React Native | Framework for mobile applications, used in the Alongside Monitor app. |

## Editor

You are free to choose your own editor. Nearly everyone at Teqplay uses VSCode. Recommended plugins for VSCode:

* [Prettier - Code formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
* [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)
* [SCSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=mrmlnc.vscode-scss)
* [TODO Highlight](https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight)
* [Git Blame](https://marketplace.visualstudio.com/items?itemName=waderyan.gitblame)

## DEV / LIVE Environments

We make a distinction between live and dev environments. For experiments we start with only one environment. When we have two we link the dev frontend to a dev backend, the dev frontend will have a separate URL named `<projectname>dev.teqplay.nl`. The live instance will just be the project name and of course link to the live backend.

Examples:

* [portreporter.teqplay.nl](http://portreporter.teqplay.nl) (Linked to the LIVE/production backend)
* [portreporterdev.teqplay.nl](http://portreporterdev.teqplay.nl) (Linked to the development backend)

## Version control / GIT

We have all our repositories inside Bitbucket. We are planning on migrating to Github so it might be the case that by the time you are reading this we have migrated over.

## Deployment

Deployments are done with [CircleCI](http://app.circleci.com/).  
We have a default config defined, that runs the following:

* installs packages
* run linter
* run tests
* builds the code
* after approval via the interface, it will deploy
* master branch will deploy to live, other branches will deploy to dev (default is that dev url will be the develop branch, can be made exceptions for testing purposes)
* message via Slack is shared

No need to deploy every commit, when you move a card in Trello to testing make sure it's deployed to dev. To add the configuration to a project you can follow [this wiki page](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Add%20Circle%20CI%20to%20%22regular%22%20frontend%20projects)

## Error logging - Sentry

We use Sentry to log errors for almost all relevant projects. We have a paid subscription. The way we're using it is mainly captured in [this snippet](https://bitbucket.org/teqplay/workspace/snippets/MKRXRp/sentry-utils)

## Start a new project

We often have have a standard approach on how we setup new projects. But there's often room to expirement with something new, so please don't follow this list blindly:

### Setup base

* [create-react-app](https://create-react-app.dev/docs/adding-typescript/) with typescript to setup a react project
* [Add Sass](https://create-react-app.dev/docs/adding-a-sass-stylesheet/)
* Add eslint and prettier [setup](https://bitbucket.org/teqplay/workspace/snippets/dL5jR5/eslint-config)
* (optional) [Add Sentry](https://bitbucket.org/teqplay/workspace/snippets/MKRXRp/sentry-utils)

### Authentication

* [Add AuthService](https://bitbucket.org/teqplay/workspace/snippets/znp59q/authentication-service). The AuthService will handle request authentication and log in with refresh token if the token is expired.
* [Login screen](https://bitbucket.org/teqplay/port-support/src/master/src/pages/login/) and [auth0 config](https://bitbucket.org/teqplay/workspace/snippets/Gex8KK/auth0-wrapper), we usually copy this from a different project

### Deployment

* [Create AWS bucket, cloudfront and route 53 DNS](https://bitbucket.org/teqplay/teqplay-wiki/wiki/AWS%20host%20front-end%20project)
* [Add CircleCI](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Add%20Circle%20CI%20to%20%22regular%22%20frontend%20projects) config to the project

## Coding standard

--> Add this later in a separate wiki page? The card is on the backlog to do this

## Code sharing (between projects)

* [Bitbucket Snippets](https://bitbucket.org/teqplay/workspace/snippets/)
* [Teqplay-ui library](http://teqplay-ui.teqplay.nl/)
* [Font icon library](https://icons.teqplay.nl/demo.html) Can be updated by uploading svg icons. The files and the readme are in a [repo](https://bitbucket.org/teqplay/teqplay-icon-font)
* [Web-sdk](https://bitbucket.org/teqplay/web-sdk/src/master/) It's a bit older, so not always working with the latest react/leaflet versions.

We are constantly trying to improve code-sharing. Since a lot of applications are similar this is very relevant within Teqplay.

## Backends

For most new projects there's a separate backend created. For some project, the Platform is used ([backend.teqplay.nl](http://backend.teqplay.nl) or [backendpronto.teqplay.nl](http://backendpronto.teqplay.nl)). We want to move away from having one backend for everything, so connecting the platform directly is not highly recommended. Often separate backends will have a connection with the platform.

## Cordova / React Native

One project is built with React Native (SSL app), all other mobile apps are built with Cordova.
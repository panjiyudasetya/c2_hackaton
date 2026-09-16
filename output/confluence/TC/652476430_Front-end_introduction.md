---
id: confluence:652476430
source: confluence
type: page
space: TC
title: Front-end introduction
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652476430
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652476430
---
# Front-end introduction

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652476430  

## Content

The team members are mentioned on the website: <http://teqplay.com/team> If anything is unclear don't hesitate to ask any of your colleagues.

## Languages, frameworks and tools

* Slack
* BitBucket
* Trello
* LastPass (ask Richard for account)
* React (create-react-app)
* Typescript
* Leaflet / Mapbox GL
* Sentry (shared account)
* REST-API
* Auth0 (most new tools use auth0)
* GraphQL (expirement)
* Fontello (our custom icon font, sometimes using fontawsome)
* Sass (.scss files)
* CircleCI (for app deployment)
* Cordova and React Native for mobile applications

## Editor

You're free to choose your own editor. Most front-end'ers use VSCode. Recommended Plugins are also for VSCode:

* Project Snippets
* Prettier - Code formatter
* ESLint
* Jest
* SCSS IntelliSense
* TODO Highlight
* TSLint
* Git Blame
* Typescript Hero

## DEV / LIVE

We make a distinction between live and dev environments. For experiments we start with only one environment. When we have two we link the dev frontend to a dev backend, the dev frontend will have a separate URL named `<projectname>dev.teqplay.nl`. The live instance will just be the project name and of course link to the live backend

## GIT

Repositories should all be in BitBucket, they should have a master and develop branch. Develop

## Deployment

Deployments are done with [CircleCI](http://app.circleci.com/). We have a default config defined, that runs the following: \* installes packages \* run linter \* run tests \* builds the code \* after approval via the interface, it will deploy \* master branch will deploy to live, other branches will deploy to dev (default is that dev url will be the develop branch, can be made exceptions for testing purposes) \* message via Slack is shared

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

One project is built with React Native (SSL app), all other mobile apps are built with Cordova. At this moment Damon and Babette have the most knowledge about this.
---
id: confluence:1044971522
source: confluence
type: page
space: TC
title: Internal / External API test project
author: Francisco Jose Muros Muriano (Unlicensed)
date: '2025-12-12'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1044971522
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1044971522
---
# Internal / External API test project

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1044971522  

## Content

Project can be found here <https://github.com/teqplay/api-tests>

it’s a java project with gradle that uses junit and rest assured in order to run the tests, for reporting, allure reports library is the one applied.

Actual test can be found in src/test/java/nl/teqplay/apitests. Currently they are separated in three folders groups, Auth tests, Event and Ship tests, each one of these folders contains a class for each endpoint of the group

List of planned test can be found here:

<https://docs.google.com/spreadsheets/d/1iRPumbjIVf5u1DBa52EF0Fe60UdW3dpGaolWFXpxDmU/edit?gid=960288592#gid=960288592>

In order to extend this project to create more test for missing endpoints (Infra and Voyages) we can take an existing class as example and just change the body, parameters and endpoint url as needed.

There is a config.properties file in the project used to store all the endpoints used in each test and error messages. it can be found here src/test/resources/config.properties. In order to create a new test we just have to add to the config file the endpoint path that we want to use and use it in the tests

In order to create a request to an endpoint we can do the following:

This is an example of a test, the steps are:

* `GenericApiClient api = new GenericApiClient(env);` Here we use the Environment variable env to make the test run twice, one for internal API and another for external API
* `String token = api.login(env.username, env.password); Here, we get the token by login in the app using the environment client_id and client_secret.`
* `response = api.post(path, body, params, token); this how we call the endpoint, there it uses some parameters:`

  + Path is initialized at the beggining as its going to be re-used all over the tests `String path = ConfigManager.get("event.history.circle");` in this case we load the data from the config file.
  + Body should be an object so rest assured uses the integrated jackson library in order to get the body
  + Params should be an map with the different parameters
  + Token is the actual token that we get in `String token = api.login(env.username, env.password);`
  + With this we get an Response object, that include lot of information as response time, status code, actual response etc. using this response we can build our checks using response.jsonPath()

The general idea with those test are to test one thing per test, if we add lots of checks in one test, it can make harder to detect all the issues at once, and so we dont waste too much time until everything is detected.
---
id: confluence:651493394
source: confluence
type: page
space: TC
title: Use of MTurk from Portcall+
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651493394
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651493394
---
# Use of MTurk from Portcall+

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651493394  

## Content

[This currently is not used anymore, but left here for reference in the future]

## What is MTurk

It is a solution of amazon to let us create jobs for people all around the world to pick up and pay them through amazon. These users can often do simple and quick jobs for a for us small amount of money.

## Why do we use it

We chose to use Mturk when Nxtport decided to create an api but without the agent information which we currently do get by scraping their website. This is to let people manually enter the agent from a site which is hard to scrape.

## How do we use it

We use the api created by Nxtport to fetch the upcoming portcalls. And every time a new portcall is created in our system we create a job called a HIT in MTurk.

This HIT can be picked up by workers of which we currently allow 3 to pick up the same HIT.

After a user filled in the answer, we receive their answer by Simple Notification Service(SNS) which calls an endpoint of portcallplus. We check if the agent is known to us, if it is we accept their answer and change the agent to that in our system.

## Architecture

[The page we ask the workers to check](https://doc-04-2c-docs.googleusercontent.com/docs/securesc/smmasa9lm4mkbj87kivvsm7hi862r73e/j5c79l29sbma1oflh5er73tuohipetom/1641205800000/15315635397882388284/10320788112804505787/1n_MWNP-3oZkjCf2pKKo_cW7kMUh4itNw?e=view&authuser=0&nonce=rp5pbh222gesg&user=10320788112804505787&hash=9at74ns91cae2cheadj34tee5u3ue41t)

## What are known issues

* Currently we check if the agent is known to us by checking all the previous portcalls. This will not work in the following scenarios

1. We delete all the portcalls or all portcalls of an agent. That agent will not be known anymore
2. A new agent has started up but we don't have a portcall with their name yet.
3. An agent company does not exist anymore or changes name
4. The users realizes we only check if it is an existing agent and always answers with the same agent. We will think it is the right agent falsely

* We get the answers by a connection through SNS that calls our endpoint. In the following cases that will go wrong

1. If portcallplus restarts when the answer is coming in. SNS will get a timeout and not send it a second time
2. If portcallplus is not reachable for any other reason like for example dns problems

## Management

To make it possible to have grip over accepting, rejecting and viewing the HITs, we patched a few calls from the amazon api through portcallplus. This is done because Amazon does not provide any kind of tools for HITs created through the api.

Controller: /v1/mturk

**Viewing the status of the HITs**

All HITs as html page

/html/status

All HITs

/list/HITs

All HITs in the reviewable state

/list/reviewableHITs

**Reviewing the answers given**

The answers given to a specific HIT

/answers/{hitId}

Accepting an answer \* The assignmentId is the id of the given answer, retrieveable from /answers/{hitId}

/answers/approve/{assignmentId}

Rejecting an answer

/answers/reject/{assignmentId}

**Workers**

Get all blocked workers

/workers/blocked

Send all workers given in the body a message

/workers/notify

[PortcallPlus Api Reference](https://portcallplus.teqplay.nl/swagger-ui/#/m-turk-controller)

## Api Reference

[API](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_OperationsArticle.html)
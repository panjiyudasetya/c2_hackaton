---
id: confluence:489324545
source: confluence
type: page
space: TC
title: PTO-1187 Investigate Streaming
author: Ryan Kharisma Rakhmat
date: '2024-10-16'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/489324545
explicit_links:
- jira:PTO-1187
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/489324545
---
# PTO-1187 Investigate Streaming

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/489324545  

## Content

Streaming data pipeline need to be integrated also with the Airflow.

Before we start to find [nats.io](http://nats.io) streaming solutions.

Firstly we find the RabbitMq and also Kafka Solutions that already have the plugins ready on airflow.

1. RabbitMQ: <https://pypi.org/project/airflow-provider-rabbitmq/>
2. Kafka: <https://pypi.org/project/airflow-provider-kafka/>

Envision for implementations of the streaming data with airflow will be go through the steps below:

1. Find the [nats.io](http://nats.io) python client

<https://github.com/nats-io/nats.py>

2. Test the python client in local with nats running on docker

Testing locally by running the [nats.io](http://nats.io) server on docker

Create some Producer that stream the messages

Create some Subscriber that subscribe the messages from stream

Create some python client Subscriber that subscribe the messages from stream using python code.

3. Write the new airflow plugins that can be listen to [nats.io](http://nats.io) stream

   1. write some nats plugins on dataflow\_plugins repository
   2. call that new nats plugin from the new dags in dataflow\_dags and we named: “listen\_to\_the\_stream” and set the schedule to continues to always running.
   3. create or make sure the dag that will be triggered exists e.g “ingest\_data\_from\_vesselvoyages\_api” dag after the stream got specific messages "vesselvoyage:change".
   4. test on the development enviroment

references:

<https://betterprogramming.pub/making-async-api-calls-with-airflow-dynamic-task-mapping-d0cbd3066ebb>

<https://medium.com/apache-airflow/apache-kafka-%EF%B8%8F-apache-airflow-a-no-install-click-and-play-demo-of-the-kafka-airflow-provider-6a1df9427c01>
---
id: confluence:136904705
source: confluence
type: page
space: TC
title: NATS stream backup replay
author: Darius Wattimena
date: '2022-08-22'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/136904705
explicit_links: []
---
# NATS stream backup replay

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/136904705  

## Content

# Prerequisites

* Docker
* Kubectl (& optionally Lens)

# Make a backup

* go to the `brokers` namespace and open a shell for `nats-box`
* create a backup (optionally provide `--user` and `--password`)

bashnats stream backup <stream\_name> <directory\_name> --no-consumers

example:

* `<stream_name> = ais-stream:history`
* `<directory_name> = history`

# Copy backup

* get the pod name (using `kubectl get pods -n brokers` for example)
* copy the pod name from `nats-box`
* create a tmp directory on your machine and change directory to it
* run `kubectl cp -n brokers <nats_box_pod_name>:<directory_name> .`

# Restore backup

* move into the directory on your machine which contains your backup, so it shows the following files:

sh$ ls
backup.json stream.tar.s2

* edit the following in the `backup.json`

  + `"num_replicas": 1`
  + `"max_age": 0` (This is needed otherwise NATS will only restore the last hour of messages)
  + `"duplicate_window": 0`
* run in one terminal window

bashdocker run --rm --network host nats -js

* run in another terminal window

bash$ docker run --rm -it --network host -v $(pwd):/backup natsio/nats-box
nats str restore /backup
nats str ls

**If you want to re-restore a backup**

* Delete the old stream `nats str delete <STREAM_NAME>`
* Restore the backup `nats str restore /backup`

# Replay backup

* go to your `application.properties` / `application.yaml` and set:

nats.enabled=true
nats.url=nats://localhost:4222
nats.username=my-replay-user

* go to the lines in your app where you use `.consumerStream(...)` to get a stream and use `.consume(...)` to consume from it
* in `.consume(...)` set `startTime` to `ZonedDateTime.parse(...)` with the start date of the stream
* optionally set `replayAtOriginalSpeed=true` if you’d like to receive the messages spaced in time as they were received initially
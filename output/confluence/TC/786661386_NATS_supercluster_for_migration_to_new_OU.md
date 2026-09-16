---
id: confluence:786661386
source: confluence
type: page
space: TC
title: NATS supercluster for migration to new OU
author: Minh Trang Nguyen (Unlicensed)
date: '2025-07-07'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/786661386
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/786661386
---
# NATS supercluster for migration to new OU

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/786661386  

## Content

**Status: work in process**

The motivation behind deploying a NATS supercluster between two separate Virtual Private Clouds (VPCs) is to streamline the migration of NATS clusters from a root VPC to a VPC within an Organizational Unit (OU). Consequently, comprehensive testing was performed to ascertain the operational characteristics of a NATS supercluster and determine its efficacy in supporting such migration scenarios.

## Test setup

The NATS Helm chart, provided by the NATS team, is accessible at <https://github.com/nats-io/k8s/blob/main/helm/charts/nats/README.md>. For our purposes, the charts have been deployed on a local Kubernetes cluster, distributed across two different namespaces. This local configuration facilitates streamlined debugging and allows for efficient experimentation within defined time constraints.

Each of the two NATS clusters is configured using a distinct set of Helm values.

**NATS cluster a:**

yamlwide760config:
cluster:
enabled: true
port: 6222
replicas: 3
jetstream:
enabled: true
merge:
domain: hub
leafnodes:
enabled: true
port: 7422
gateway:
enabled: true
port: 7222
# merge or patch the gateway config
# https://docs.nats.io/running-a-nats-service/configuration/gateways/gateway#gateway-configuration-block
merge:
name: nats-cluster-a
gateways:
- name: nats-cluster-b
urls:
- nats://nats-cluster-b-headless.testing2.svc.cluster.local:7222
merge:
system\_account: SYS
accounts:
SYS:
users:
- user: test
password: test
test:
users:
- user: demo
password: demo
jetstream: {}
service:
enabled: true
# service port options
# additional boolean field enable to control whether port is exposed in the service
# must be enabled in the config section also
# https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#serviceport-v1-core
ports:
nats:
enabled: true
leafnodes:
enabled: true
websocket:
enabled: true
mqtt:
enabled: true
cluster:
enabled: false
gateway:
enabled: true
monitor:
enabled: false
profiling:
enabled: false
natsBox:
enabled: true

**NATS cluster b:**

yamlwide760config:
cluster:
enabled: true
port: 6222
replicas: 3
jetstream:
enabled: true
merge:
domain: hub
leafnodes:
enabled: true
port: 7422
gateway:
enabled: true
port: 7222
# merge or patch the gateway config
# https://docs.nats.io/running-a-nats-service/configuration/gateways/gateway#gateway-configuration-block
merge:
name: nats-cluster-b
gateways:
- name: nats-cluster-a
urls:
- nats://nats-cluster-a-headless.testing.svc.cluster.local:7222
merge:
system\_account: SYS
accounts:
SYS:
users:
- user: test2
password: test2
test:
users:
- user: demo
password: demo
jetstream: {}
service:
enabled: true
# service port options
# additional boolean field enable to control whether port is exposed in the service
# must be enabled in the config section also
# https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#serviceport-v1-core
ports:
nats:
enabled: true
leafnodes:
enabled: true
websocket:
enabled: true
mqtt:
enabled: true
cluster:
enabled: false
gateway:
enabled: true
monitor:
enabled: false
profiling:
enabled: false
natsBox:
enabled: true

* Both JetStream domains **must share the same name "hub"**; otherwise, the supercluster won't function as intended.

## Install Helm charts

NATS cluster a:

wide760helm upgrade --install nats-cluster-a nats/nats -f values-a.yaml -n testing

NATS cluster b:

wide760helm upgrade --install nats-cluster-b nats/nats -f values-b.yaml -n testing2

## NATS supercluster

After installing the Helm charts, the NATS clusters should be combined to form a single supercluster.

bashwide760nats --user test --password test server report jetstreamwide760╭────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ JetStream Summary │
├───────────────────┬────────────────┬────────┬─────────┬───────────┬──────────┬───────┬────────┬──────┬─────────┬─────────┬─────────┤
│ Server │ Cluster │ Domain │ Streams │ Consumers │ Messages │ Bytes │ Memory │ File │ API Req │ API Err │ Pending │
├───────────────────┼────────────────┼────────┼─────────┼───────────┼──────────┼───────┼────────┼──────┼─────────┼─────────┼─────────┤
│ nats-cluster-a-0\* │ nats-cluster-a │ hub │ 0 │ 0 │ 0 │ 0 B │ 0 B │ 0 B │ 0 │ 0 │ 0 │
│ nats-cluster-a-1 │ nats-cluster-a │ hub │ 0 │ 0 │ 0 │ 0 B │ 0 B │ 0 B │ 0 │ 0 │ 0 │
│ nats-cluster-a-2 │ nats-cluster-a │ hub │ 0 │ 0 │ 0 │ 0 B │ 0 B │ 0 B │ 0 │ 0 │ 0 │
│ nats-cluster-b-0 │ nats-cluster-b │ hub │ 0 │ 0 │ 0 │ 0 B │ 0 B │ 0 B │ 0 │ 0 │ 0 │
│ nats-cluster-b-1 │ nats-cluster-b │ hub │ 0 │ 0 │ 0 │ 0 B │ 0 B │ 0 B │ 0 │ 0 │ 0 │
│ nats-cluster-b-2 │ nats-cluster-b │ hub │ 0 │ 0 │ 0 │ 0 B │ 0 B │ 0 B │ 0 │ 0 │ 0 │
├───────────────────┼────────────────┼────────┼─────────┼───────────┼──────────┼───────┼────────┼──────┼─────────┼─────────┼─────────┤
│ │ │ │ 0 │ 0 │ 0 │ 0 B │ 0 B │ 0 B │ 0 │ 0 │ 0 │
╰───────────────────┴────────────────┴────────┴─────────┴───────────┴──────────┴───────┴────────┴──────┴─────────┴─────────┴─────────╯
╭────────────────────────────────────────────────────────────────────────╮
│ RAFT Meta Group Information │
├──────────────────┬──────────┬────────┬─────────┬────────┬────────┬─────┤
│ Connection Name │ ID │ Leader │ Current │ Online │ Active │ Lag │
├──────────────────┼──────────┼────────┼─────────┼────────┼────────┼─────┤
│ nats-cluster-a-0 │ 7Yz8mSw2 │ yes │ true │ true │ 0s │ 0 │
│ nats-cluster-a-1 │ 2x6ni0z1 │ │ true │ true │ 969ms │ 0 │
│ nats-cluster-a-2 │ DSTslhZF │ │ true │ true │ 969ms │ 0 │
│ nats-cluster-b-0 │ 8SHWVnwb │ │ true │ true │ 970ms │ 0 │
│ nats-cluster-b-1 │ 7EMHrnfe │ │ true │ true │ 969ms │ 0 │
│ nats-cluster-b-2 │ GUa4jknS │ │ true │ true │ 969ms │ 0 │
╰──────────────────┴──────────┴────────┴─────────┴────────┴────────┴─────╯

As the table shows, `nats-cluster-a` currently hosts the leader, which is acceptable for the time being. However, upon completion of the migration, the leader must be relocated to `nats-cluster-b`.

## Creating a stream in nats-cluster-a

To simulate a real-world scenario, we'll create a stream in nats-cluster-a, configured with three replicas. It's important to note that JetStreams are isolated to individual NATS clusters, meaning direct replication of streams between NATS clusters isn't possible.

**Create stream:**

wide760nats --user demo --password demo stream add stream1 --subjects "stream1.>" --storage file --replicas=3 --cluster nats-cluster-a

**Stream report:**

bashwide760nats --user demo --password demo stream report
Obtaining Stream stats
╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Stream Report │
├─────────┬─────────┬──────────────────────────┬───────────┬──────────┬───────┬──────┬─────────┬───────────────────────────────────────────────────────┤
│ Stream │ Storage │ Placement │ Consumers │ Messages │ Bytes │ Lost │ Deleted │ Replicas │
├─────────┼─────────┼──────────────────────────┼───────────┼──────────┼───────┼──────┼─────────┼───────────────────────────────────────────────────────┤
│ stream1 │ File │ cluster: nats-cluster-a │ 0 │ 0 │ 0 B │ 0 │ 0 │ nats-cluster-a-0, nats-cluster-a-1\*, nats-cluster-a-2 │
╰─────────┴─────────┴──────────────────────────┴───────────┴──────────┴───────┴──────┴─────────┴───────────────────────────────────────────────────────╯

A Python script was created to continuously publish messages to this stream, sending one message per second.

**pub.py**

pywide760import asyncio
import logging
import os
from datetime import datetime
from nats.aio.client import Client as NATS
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(\_\_name\_\_)
async def run():
nats\_url = os.environ.get("NATS\_URL")
cluster\_name = os.environ.get("NATS\_CLUSTER\_NAME")
nats = NATS()
await nats.connect(
servers=[nats\_url],
user="demo",
password="demo"
)
js = nats.jetstream()
subject = "stream1.updates"
try:
while True:
now = datetime.now().isoformat()
message = f"{cluster\_name}: published {now}"
ack = await js.publish(subject, message.encode())
logger.info(f"{cluster\_name}: published message: {message} (Stream={ack.stream}, Sequence={ack.seq})")
await asyncio.sleep(1)
except KeyboardInterrupt:
logger.info("Publisher stopped by user.")
finally:
await nats.close()
if \_\_name\_\_ == "\_\_main\_\_":
asyncio.run(run())

**Create a configmap:**

bashwide760kubectl create configmap scriptpublisher --from-file=pub.py=./pub.py --dry-run=client -o yaml > publisher.yaml

cluster-a-pod-publisher.yaml

yamlwide760apiVersion: v1
kind: Pod
metadata:
name: cluster-a-pod-publisher
namespace: testing
spec:
containers:
- name: publisher
image: python:3.12-bookworm
env:
- name: NATS\_URL
value: "nats://nats-cluster-a.testing.svc.cluster.local:4222"
- name: NATS\_CLUSTER\_NAME
value: "cluster-a"
command: ["/bin/sh", "-c"]
args:
- pip install nats-py && python /app/publisher.py
volumeMounts:
- name: script-volume
mountPath: /app/publisher.py
subPath: pub.py
volumes:
- name: script-volume
configMap:
name: scriptpublisherwide760kubectl apply -f cluster-a-pod-publisher.yaml

**Output**

bashwide760kubectl logs cluster-a-pod-publisher
Collecting nats-py
Downloading nats\_py-2.10.0.tar.gz (113 kB)
Installing build dependencies: started
Installing build dependencies: finished with status 'done'
Getting requirements to build wheel: started
Getting requirements to build wheel: finished with status 'done'
Preparing metadata (pyproject.toml): started
Preparing metadata (pyproject.toml): finished with status 'done'
Building wheels for collected packages: nats-py
Building wheel for nats-py (pyproject.toml): started
Building wheel for nats-py (pyproject.toml): finished with status 'done'
Created wheel for nats-py: filename=nats\_py-2.10.0-py3-none-any.whl size=83596 sha256=09b67fd2f8e06345ac7acb3b648eab24600ece0629b9ff6a13fd60caee44a147
Stored in directory: /root/.cache/pip/wheels/d6/bb/e0/05ae3e6fb01be6724f25fb3e8ce98a60dfc13ba29482aec7fc
Successfully built nats-py
Installing collected packages: nats-py
Successfully installed nats-py-2.10.0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
[notice] A new release of pip is available: 25.0.1 -> 25.1.1
[notice] To update, run: pip install --upgrade pip
INFO:\_\_main\_\_:cluster-a: published message: cluster-a: published 2025-07-02T03:35:59.623080 (Stream=stream1, Sequence=1)
INFO:\_\_main\_\_:cluster-a: published message: cluster-a: published 2025-07-02T03:36:00.624715 (Stream=stream1, Sequence=2)
INFO:\_\_main\_\_:cluster-a: published message: cluster-a: published 2025-07-02T03:36:01.626368 (Stream=stream1, Sequence=3)
INFO:\_\_main\_\_:cluster-a: published message: cluster-a: published 2025-07-02T03:36:02.629693 (Stream=stream1, Sequence=4)
INFO:\_\_main\_\_:cluster-a: published message: cluster-a: published 2025-07-02T03:36:03.631349 (Stream=stream1, Sequence=5)
INFO:\_\_main\_\_:cluster-a: published message: cluster-a: published 2025-07-02T03:36:04.632996 (Stream=stream1, Sequence=6)
INFO:\_\_main\_\_:cluster-a: published message: cluster-a: published 2025-07-02T03:36:05.634797 (Stream=stream1, Sequence=7)
INFO:\_\_main\_\_:cluster-a: published message: cluster-a: published 2025-07-02T03:36:06.636543 (Stream=stream1, Sequence=8)
INFO:\_\_main\_\_:cluster-a: published message: cluster-a: published 2025-07-02T03:36:07.638152 (Stream=stream1, Sequence=9)
INFO:\_\_main\_\_:cluster-a: published message: cluster-a: published 2025-07-02T03:36:08.639369 (Stream=stream1, Sequence=10)
INFO:\_\_main\_\_:cluster-a: published message: cluster-a: published 2025-07-02T03:36:09.640890 (Stream=stream1, Sequence=11)
INFO:\_\_main\_\_:cluster-a: published message: cluster-a: published 2025-07-02T03:36:10.642634 (Stream=stream1, Sequence=12)
INFO:\_\_main\_\_:cluster-a: published message: cluster-a: published 2025-07-02T03:36:11.644414 (Stream=stream1, Sequence=13)
INFO:\_\_main\_\_:cluster-a: published message: cluster-a: published 2025-07-02T03:36:12.646261 (Stream=stream1, Sequence=14)
INFO:\_\_main\_\_:cluster-a: published message: cluster-a: published 2025-07-02T03:36:13.647377 (Stream=stream1, Sequence=15)
INFO:\_\_main\_\_:cluster-a: published message: cluster-a: published 2025-07-02T03:36:14.649222 (Stream=stream1, Sequence=16)
INFO:\_\_main\_\_:cluster-a: published message: cluster-a: published 2025-07-02T03:36:15.650992 (Stream=stream1, Sequence=17)
INFO:\_\_main\_\_:cluster-a: published message: cluster-a: published 2025-07-02T03:36:16.652222 (Stream=stream1, Sequence=18)
INFO:\_\_main\_\_:cluster-a: published message: cluster-a: published 2025-07-02T03:36:17.653955 (Stream=stream1, Sequence=19)
INFO:\_\_main\_\_:cluster-a: published message: cluster-a: published 2025-07-02T03:36:18.655360 (Stream=stream1, Sequence=20)
INFO:\_\_main\_\_:cluster-a: published message: cluster-a: published 2025-07-02T03:36:19.656963 (Stream=stream1, Sequence=21)
INFO:\_\_main\_\_:cluster-a: published message: cluster-a: published 2025-07-02T03:36:20.658751 (Stream=stream1, Sequence=22)
INFO:\_\_main\_\_:cluster-a: published message: cluster-a: published 2025-07-02T03:36:21.660503 (Stream=stream1, Sequence=23)
INFO:\_\_main\_\_:cluster-a: published message: cluster-a: published 2025-07-02T03:36:22.662264 (Stream=stream1, Sequence=24)
INFO:\_\_main\_\_:cluster-a: published message: cluster-a: published 2025-07-02T03:36:23.663374 (Stream=stream1, Sequence=25)

## Creating Jetstream KV store in nats-cluster-a

For testing purposes, we created a key-value store via the CLI. The goal was to determine if it's possible to mirror this key-value store to `nats-cluster-b` and then switch to the mirrored store after migration.

**Create the key-value store:**

bashwide760nats --user demo --password demo kv add first\_kv\_store --replicas=3

**Output:**

bashwide760Information for Key-Value Store Bucket first\_kv\_store created 2025-07-02T03:41:37Z
Configuration:
Bucket Name: first\_kv\_store
History Kept: 1
Values Stored: 0
Compressed: false
Backing Store Kind: JetStream
Bucket Size: 0 B
Maximum Bucket Size: unlimited
Maximum Value Size: unlimited
Maximum Age: unlimited
JetStream Stream: KV\_first\_kv\_store
Storage: File
Cluster Information:
Name: nats-cluster-a
Leader: nats-cluster-a-0
Replica: nats-cluster-a-1, current, seen 39ms ago
Replica: nats-cluster-a-2, current, seen 39ms ago

**Create the keys with values:**

bashwide760nats --user demo --password demo kv put first\_kv\_store key1 "value1"
nats --user demo --password demo kv put first\_kv\_store key2 "value2"
nats --user demo --password demo kv put first\_kv\_store key3 "value3"
nats --user demo --password demo kv put first\_kv\_store key4 "value4"
nats --user demo --password demo kv put first\_kv\_store key5 "value5"

**Check the values:**

bashwide760nats --user demo --password demo kv get first\_kv\_store key1
nats --user demo --password demo kv get first\_kv\_store key2
nats --user demo --password demo kv get first\_kv\_store key3
nats --user demo --password demo kv get first\_kv\_store key4
nats --user demo --password demo kv get first\_kv\_store key5

The values were visible in both `nats-cluster-a` and `nats-cluster-b`.

**Stream report nats-cluster-a:**

bashwide760nats --user demo --password demo stream report
Obtaining Stream stats
╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Stream Report │
├───────────────────┬─────────┬──────────────────────────┬───────────┬──────────┬─────────┬──────┬─────────┬───────────────────────────────────────────────────────┤
│ Stream │ Storage │ Placement │ Consumers │ Messages │ Bytes │ Lost │ Deleted │ Replicas │
├───────────────────┼─────────┼──────────────────────────┼───────────┼──────────┼─────────┼──────┼─────────┼───────────────────────────────────────────────────────┤
│ KV\_first\_kv\_store │ File │ │ 0 │ 5 │ 295 B │ 0 │ 0 │ nats-cluster-a-0\*, nats-cluster-a-1, nats-cluster-a-2 │
│ stream1 │ File │ cluster: nats-cluster-a │ 0 │ 98 │ 8.8 KiB │ 0 │ 0 │ nats-cluster-a-0, nats-cluster-a-1\*, nats-cluster-a-2 │
╰───────────────────┴─────────┴──────────────────────────┴───────────┴──────────┴─────────┴──────┴─────────┴───────────────────────────────────────────────────────╯

As the table shows, both the stream and the key-value store were created in `nats-cluster-a` and contain messages.

## Mirroring stream in nats-cluster-b

The strategy involves creating a new stream in `nats-cluster-b` that mirrors the existing stream in `nats-cluster-a`, thereby replicating the data within `nats-cluster-b`. The objective is to ensure data availability in `nats-cluster-b` even after `nats-cluster-a` (the old cluster) is detached from the supercluster. This process is technically known as an active migration.

**Create config file “mirror.json“:**

jsonwide760{
"name": "stream1b",
"subjects": [
"stream1b.\*"
],
"discard": "old",
"duplicate\_window": 120000000000,
"sources": [
{
"name": "stream1"
}
],
"deny\_delete": false,
"sealed": false,
"max\_msg\_size": -1,
"allow\_rollup\_hdrs": false,
"max\_bytes": -1,
"storage": "file",
"allow\_direct": false,
"max\_age": 0,
"max\_consumers": -1,
"max\_msgs\_per\_subject": -1,
"num\_replicas": 3,
"name": "stream1b",
"deny\_purge": false,
"compression": "none",
"max\_msgs": -1,
"retention": "limits",
"mirror\_direct": false
}

Put the content into file `mirror.json` on path `/tmp`.

**Run command in nats-box of nats-cluster-b:**

bashwide760nats --user demo --password demo stream add --config /tmp/mirror.json

The mirror stream should now be created, with its messages successfully replicated to `nats-cluster-b`. Additionally, messages from `stream1b` should also have replicated to `nats-cluster-b` as intended.

wide760nats --user demo --password demo stream report
Obtaining Stream stats
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Stream Report │
├───────────────────┬─────────┬──────────────────────────┬───────────┬──────────┬────────┬──────┬─────────┬───────────────────────────────────────────────────────┤
│ Stream │ Storage │ Placement │ Consumers │ Messages │ Bytes │ Lost │ Deleted │ Replicas │
├───────────────────┼─────────┼──────────────────────────┼───────────┼──────────┼────────┼──────┼─────────┼───────────────────────────────────────────────────────┤
│ KV\_first\_kv\_store │ File │ │ 0 │ 5 │ 295 B │ 0 │ 0 │ nats-cluster-a-0\*, nats-cluster-a-1, nats-cluster-a-2 │
│ stream1 │ File │ cluster: nats-cluster-a │ 0 │ 243 │ 22 KiB │ 0 │ 0 │ nats-cluster-a-0, nats-cluster-a-1\*, nats-cluster-a-2 │
│ stream1b │ File │ │ 0 │ 243 │ 34 KiB │ 0 │ 0 │ nats-cluster-b-0, nats-cluster-b-1\*, nats-cluster-b-2 │
╰───────────────────┴─────────┴──────────────────────────┴───────────┴──────────┴────────┴──────┴─────────┴───────────────────────────────────────────────────────╯
╭────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Replication Report │
├──────────┬────────┬────────────┬───────────────┬────────────────────────┬────────┬─────┬───────┤
│ Stream │ Kind │ API Prefix │ Source Stream │ Filters and Transforms │ Active │ Lag │ Error │
├──────────┼────────┼────────────┼───────────────┼────────────────────────┼────────┼─────┼───────┤
│ stream1b │ Source │ │ stream1 │ │ 873ms │ 0 │ │
╰──────────┴────────┴────────────┴───────────────┴────────────────────────┴────────┴─────┴───────╯

## Mirroring key-value store in nats-cluster-b

bashwide760nats --user demo --password demo kv add first\_kv\_store\_copy \
--mirror first\_kv\_store --replicas 3

**Stream report:**

wide760nats --user demo --password demo stream report
Obtaining Stream stats
╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Stream Report │
├────────────────────────┬─────────┬──────────────────────────┬───────────┬──────────┬────────┬──────┬─────────┬───────────────────────────────────────────────────────┤
│ Stream │ Storage │ Placement │ Consumers │ Messages │ Bytes │ Lost │ Deleted │ Replicas │
├────────────────────────┼─────────┼──────────────────────────┼───────────┼──────────┼────────┼──────┼─────────┼───────────────────────────────────────────────────────┤
│ KV\_first\_kv\_store │ File │ │ 0 │ 5 │ 295 B │ 0 │ 0 │ nats-cluster-a-0\*, nats-cluster-a-1, nats-cluster-a-2 │
│ KV\_first\_kv\_store\_copy │ File │ │ 0 │ 5 │ 295 B │ 0 │ 0 │ nats-cluster-b-0, nats-cluster-b-1, nats-cluster-b-2\* │
│ stream1 │ File │ cluster: nats-cluster-a │ 0 │ 243 │ 22 KiB │ 0 │ 0 │ nats-cluster-a-0, nats-cluster-a-1\*, nats-cluster-a-2 │
│ stream1b │ File │ │ 0 │ 243 │ 34 KiB │ 0 │ 0 │ nats-cluster-b-0, nats-cluster-b-1\*, nats-cluster-b-2 │
╰────────────────────────┴─────────┴──────────────────────────┴───────────┴──────────┴────────┴──────┴─────────┴───────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Replication Report │
├────────────────────────┬────────┬────────────┬───────────────────┬────────────────────────┬────────┬─────┬───────┤
│ Stream │ Kind │ API Prefix │ Source Stream │ Filters and Transforms │ Active │ Lag │ Error │
├────────────────────────┼────────┼────────────┼───────────────────┼────────────────────────┼────────┼─────┼───────┤
│ KV\_first\_kv\_store\_copy │ Mirror │ │ KV\_first\_kv\_store │ │ 912ms │ 0 │ │
│ stream1b │ Source │ │ stream1 │ │ 669ms │ 0 │ │
╰────────────────────────┴────────┴────────────┴───────────────────┴────────────────────────┴────────┴─────┴───────╯

## Migration strategy

With NATS clusters established in two separate environments, we've gained the flexibility to migrate a **publisher (producer)** or **subscriber (consumer)** to the new OU. This migration is facilitated by the ability of these components to access the same streams and accounts, assuming identical account and stream configurations have been imported into `nats-cluster-b`. When all publishers and subscribers are migrated, we can start with the decoupling of the old cluster `nats-cluster-a`.

Next, we will bring down (scaling) the publishers and subscribers in the PVC of the new OU, effectively halting message publication to streams in `nats-cluster-a`.

### Remove stream mirrors

**Save and remove config sources in file /tmp/stream1b\_modified.json:**

wide760nats --user demo --password demo stream info stream1b -j | jq 'del(.config.sources)' > /tmp/stream1b\_modified.json

**Change config of stream1b:**

wide760nats --user demo --password demo stream edit stream1b --config /tmp/stream1b\_modified.json

**Stream report:**

bashwide760nats --user demo --password demo stream report
Obtaining Stream stats
╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Stream Report │
├────────────────────────┬─────────┬──────────────────────────┬───────────┬──────────┬────────┬──────┬─────────┬───────────────────────────────────────────────────────┤
│ Stream │ Storage │ Placement │ Consumers │ Messages │ Bytes │ Lost │ Deleted │ Replicas │
├────────────────────────┼─────────┼──────────────────────────┼───────────┼──────────┼────────┼──────┼─────────┼───────────────────────────────────────────────────────┤
│ KV\_first\_kv\_store │ File │ │ 0 │ 5 │ 295 B │ 0 │ 0 │ nats-cluster-a-0\*, nats-cluster-a-1, nats-cluster-a-2 │
│ KV\_first\_kv\_store\_copy │ File │ │ 0 │ 5 │ 295 B │ 0 │ 0 │ nats-cluster-b-0, nats-cluster-b-1, nats-cluster-b-2\* │
│ stream1 │ File │ cluster: nats-cluster-a │ 0 │ 243 │ 22 KiB │ 0 │ 0 │ nats-cluster-a-0, nats-cluster-a-1\*, nats-cluster-a-2 │
│ stream1b │ File │ │ 0 │ 243 │ 34 KiB │ 0 │ 0 │ nats-cluster-b-0, nats-cluster-b-1\*, nats-cluster-b-2 │
╰────────────────────────┴─────────┴──────────────────────────┴───────────┴──────────┴────────┴──────┴─────────┴───────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Replication Report │
├────────────────────────┬────────┬────────────┬───────────────────┬────────────────────────┬────────┬─────┬───────┤
│ Stream │ Kind │ API Prefix │ Source Stream │ Filters and Transforms │ Active │ Lag │ Error │
├────────────────────────┼────────┼────────────┼───────────────────┼────────────────────────┼────────┼─────┼───────┤
│ KV\_first\_kv\_store\_copy │ Mirror │ │ KV\_first\_kv\_store │ │ 140ms │ 0 │ │
╰────────────────────────┴────────┴────────────┴───────────────────┴────────────────────────┴────────┴─────┴───────╯

As a result of the migration, `stream1b` has become an independent stream residing in `nats-cluster-b`, which was the intended goal.

**Test publishing to stream1b:**

wide760nats --user demo --password demo pub stream1b.updates "Test"
04:44:26 Published 4 bytes to "stream1b.updates"wide760[245] Subject: stream1b.updates Received: 2025-07-02T04:44:26Z
Test

### Remove key-value mirror

As direct un-mirroring of a JetStream key-value store is not supported, migrating its data from `nats-cluster-a` to `nats-cluster-b` requires a custom Python script. This script would be tasked with transferring the data during the period of publisher and subscriber downtime. I've encountered conflicting information from AI applications like ChatGPT regarding the possibility of un-mirroring key-value stores, however, my review of NATS documentation and source code indicates that such a feature is not available.

Using a script could be the way to go, because the amount of data is relatively small.

**Teqplay NATS develop cluster:**

wide760Obtaining Stream stats
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Stream Report │
├───────────────────────────────────────────────┬─────────┬───────────┬───────────┬──────────┬─────────┬──────┬─────────┬─────────────────────────┤
│ Stream │ Storage │ Placement │ Consumers │ Messages │ Bytes │ Lost │ Deleted │ Replicas │
├───────────────────────────────────────────────┼─────────┼───────────┼───────────┼──────────┼─────────┼──────┼─────────┼─────────────────────────┤
│ event-stream │ File │ │ 11 │ 0 │ 0 B │ 0 │ 0 │ nats-0, nats-1\*, nats-2 │
│ KV\_portreporter-monitor-encounter-concurrency │ File │ │ 0 │ 6 │ 588 B │ 0 │ 6 │ nats-0, nats-1, nats-2\* │
│ KV\_portreporter-monitor-pilot-onboard │ File │ │ 0 │ 469 │ 43 KiB │ 0 │ 357 │ nats-0, nats-1\*, nats-2 │
│ KV\_portreporter-monitor-tug-standby │ File │ │ 0 │ 558 │ 68 KiB │ 0 │ 232 │ nats-0, nats-1\*, nats-2 │
│ KV\_portreporter-monitor-tug-waiting │ File │ │ 0 │ 2,051 │ 234 KiB │ 0 │ 703 │ nats-0, nats-1, nats-2\* │
│ KV\_encounter-monitor │ File │ │ 0 │ 5,620 │ 3.8 MiB │ 0 │ 9224 │ nats-0, nats-1, nats-2\* │
│ KV\_anchor-monitor │ File │ │ 0 │ 12,453 │ 4.5 MiB │ 0 │ 547 │ nats-0, nats-1, nats-2\* │
│ KV\_berth-monitor │ File │ │ 0 │ 29,112 │ 19 MiB │ 0 │ 166312 │ nats-0, nats-1, nats-2\* │
│ KV\_stop-monitor-trace │ File │ │ 0 │ 93,772 │ 52 MiB │ 0 │ 162367 │ nats-0, nats-1, nats-2\* │
│ KV\_stop-monitor │ File │ │ 0 │ 343,361 │ 95 MiB │ 0 │ 984345 │ nats-0, nats-1, nats-2\* │
╰───────────────────────────────────────────────┴─────────┴───────────┴───────────┴──────────┴─────────┴──────┴─────────┴──────────────────────

## Decoupling `nats-cluster-a`

Go into nats-box of `nats-cluster-a` and run the command:

bashwide760nats --user test --password test server report jetstream
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ JetStream Summary │
├───────────────────┬────────────────┬────────┬─────────┬───────────┬──────────┬─────────┬────────┬─────────┬─────────┬─────────┬─────────┤
│ Server │ Cluster │ Domain │ Streams │ Consumers │ Messages │ Bytes │ Memory │ File │ API Req │ API Err │ Pending │
├───────────────────┼────────────────┼────────┼─────────┼───────────┼──────────┼─────────┼────────┼─────────┼─────────┼─────────┼─────────┤
│ nats-cluster-a-0\* │ nats-cluster-a │ hub │ 2 │ 0 │ 248 │ 22 KiB │ 0 B │ 22 KiB │ 49 │ 0 │ 0 │
│ nats-cluster-a-1 │ nats-cluster-a │ hub │ 2 │ 0 │ 248 │ 22 KiB │ 0 B │ 22 KiB │ 4 │ 0 │ 0 │
│ nats-cluster-a-2 │ nats-cluster-a │ hub │ 2 │ 0 │ 248 │ 22 KiB │ 0 B │ 22 KiB │ 2 │ 0 │ 0 │
│ nats-cluster-b-0 │ nats-cluster-b │ hub │ 2 │ 0 │ 250 │ 35 KiB │ 0 B │ 35 KiB │ 5 │ 0 │ 0 │
│ nats-cluster-b-1 │ nats-cluster-b │ hub │ 2 │ 0 │ 250 │ 35 KiB │ 0 B │ 35 KiB │ 10 │ 0 │ 0 │
│ nats-cluster-b-2 │ nats-cluster-b │ hub │ 2 │ 0 │ 250 │ 35 KiB │ 0 B │ 35 KiB │ 4 │ 0 │ 0 │
├───────────────────┼────────────────┼────────┼─────────┼───────────┼──────────┼─────────┼────────┼─────────┼─────────┼─────────┼─────────┤
│ │ │ │ 12 │ 0 │ 1,494 │ 170 KiB │ 0 B │ 170 KiB │ 74 │ 0 │ 0 │
╰───────────────────┴────────────────┴────────┴─────────┴───────────┴──────────┴─────────┴────────┴─────────┴─────────┴─────────┴─────────╯
╭────────────────────────────────────────────────────────────────────────╮
│ RAFT Meta Group Information │
├──────────────────┬──────────┬────────┬─────────┬────────┬────────┬─────┤
│ Connection Name │ ID │ Leader │ Current │ Online │ Active │ Lag │
├──────────────────┼──────────┼────────┼─────────┼────────┼────────┼─────┤
│ nats-cluster-a-0 │ 7Yz8mSw2 │ yes │ true │ true │ 0s │ 0 │
│ nats-cluster-a-1 │ 2x6ni0z1 │ │ true │ true │ 970ms │ 0 │
│ nats-cluster-a-2 │ DSTslhZF │ │ true │ true │ 970ms │ 0 │
│ nats-cluster-b-0 │ 8SHWVnwb │ │ true │ true │ 970ms │ 0 │
│ nats-cluster-b-1 │ 7EMHrnfe │ │ true │ true │ 969ms │ 0 │
│ nats-cluster-b-2 │ GUa4jknS │ │ true │ true │ 969ms │ 0 │
╰──────────────────┴──────────┴────────┴─────────┴────────┴────────┴─────╯

Begin by trying to remove all peers in `nats-cluster-a` that are not designated as the leader.

bashwide760nats --user test --password test server cluster peer-remove 2x6ni0z1
nats --user test --password test server cluster peer-remove DSTslhZF

The supercluster is reduced to 4 peers.

bashwide760nats --user test --password test server report jetstream
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ JetStream Summary │
├───────────────────┬────────────────┬────────┬─────────┬───────────┬──────────┬─────────┬────────┬─────────┬─────────┬─────────┬─────────┤
│ Server │ Cluster │ Domain │ Streams │ Consumers │ Messages │ Bytes │ Memory │ File │ API Req │ API Err │ Pending │
├───────────────────┼────────────────┼────────┼─────────┼───────────┼──────────┼─────────┼────────┼─────────┼─────────┼─────────┼─────────┤
│ nats-cluster-a-0\* │ nats-cluster-a │ hub │ 2 │ 0 │ 248 │ 22 KiB │ 0 B │ 22 KiB │ 49 │ 0 │ 0 │
│ nats-cluster-a-1 │ nats-cluster-a │ │ 0 │ 0 │ 0 │ 0 B │ 0 B │ 0 B │ 0 │ 0 │ 0 │
│ nats-cluster-a-2 │ nats-cluster-a │ │ 0 │ 0 │ 0 │ 0 B │ 0 B │ 0 B │ 0 │ 0 │ 0 │
│ nats-cluster-b-0 │ nats-cluster-b │ hub │ 2 │ 0 │ 250 │ 35 KiB │ 0 B │ 35 KiB │ 5 │ 0 │ 0 │
│ nats-cluster-b-1 │ nats-cluster-b │ hub │ 2 │ 0 │ 250 │ 35 KiB │ 0 B │ 35 KiB │ 10 │ 0 │ 0 │
│ nats-cluster-b-2 │ nats-cluster-b │ hub │ 2 │ 0 │ 250 │ 35 KiB │ 0 B │ 35 KiB │ 4 │ 0 │ 0 │
├───────────────────┼────────────────┼────────┼─────────┼───────────┼──────────┼─────────┼────────┼─────────┼─────────┼─────────┼─────────┤
│ │ │ │ 8 │ 0 │ 998 │ 126 KiB │ 0 B │ 126 KiB │ 68 │ 0 │ 0 │
╰───────────────────┴────────────────┴────────┴─────────┴───────────┴──────────┴─────────┴────────┴─────────┴─────────┴─────────┴─────────╯
╭────────────────────────────────────────────────────────────────────────╮
│ RAFT Meta Group Information │
├──────────────────┬──────────┬────────┬─────────┬────────┬────────┬─────┤
│ Connection Name │ ID │ Leader │ Current │ Online │ Active │ Lag │
├──────────────────┼──────────┼────────┼─────────┼────────┼────────┼─────┤
│ nats-cluster-a-0 │ 7Yz8mSw2 │ yes │ true │ true │ 0s │ 0 │
│ nats-cluster-b-0 │ 8SHWVnwb │ │ true │ true │ 313ms │ 0 │
│ nats-cluster-b-1 │ 7EMHrnfe │ │ true │ true │ 313ms │ 0 │
│ nats-cluster-b-2 │ GUa4jknS │ │ true │ true │ 313ms │ 0 │
╰──────────────────┴──────────┴────────┴─────────┴────────┴────────┴─────╯

The next step is making a peer in `nats-cluster-b` the leader.

bashwide760nats --user test --password test server cluster step-down

As a result there’s a new leader.

bashwide760nats --user test --password test server report jetstream
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ JetStream Summary │
├───────────────────┬────────────────┬────────┬─────────┬───────────┬──────────┬─────────┬────────┬─────────┬─────────┬─────────┬─────────┤
│ Server │ Cluster │ Domain │ Streams │ Consumers │ Messages │ Bytes │ Memory │ File │ API Req │ API Err │ Pending │
├───────────────────┼────────────────┼────────┼─────────┼───────────┼──────────┼─────────┼────────┼─────────┼─────────┼─────────┼─────────┤
│ nats-cluster-a-0 │ nats-cluster-a │ hub │ 2 │ 0 │ 248 │ 22 KiB │ 0 B │ 22 KiB │ 49 │ 0 │ 0 │
│ nats-cluster-a-1 │ nats-cluster-a │ │ 0 │ 0 │ 0 │ 0 B │ 0 B │ 0 B │ 0 │ 0 │ 0 │
│ nats-cluster-a-2 │ nats-cluster-a │ │ 0 │ 0 │ 0 │ 0 B │ 0 B │ 0 B │ 0 │ 0 │ 0 │
│ nats-cluster-b-0\* │ nats-cluster-b │ hub │ 2 │ 0 │ 250 │ 35 KiB │ 0 B │ 35 KiB │ 5 │ 0 │ 0 │
│ nats-cluster-b-1 │ nats-cluster-b │ hub │ 2 │ 0 │ 250 │ 35 KiB │ 0 B │ 35 KiB │ 10 │ 0 │ 0 │
│ nats-cluster-b-2 │ nats-cluster-b │ hub │ 2 │ 0 │ 250 │ 35 KiB │ 0 B │ 35 KiB │ 4 │ 0 │ 0 │
├───────────────────┼────────────────┼────────┼─────────┼───────────┼──────────┼─────────┼────────┼─────────┼─────────┼─────────┼─────────┤
│ │ │ │ 8 │ 0 │ 998 │ 126 KiB │ 0 B │ 126 KiB │ 68 │ 0 │ 0 │
╰───────────────────┴────────────────┴────────┴─────────┴───────────┴──────────┴─────────┴────────┴─────────┴─────────┴─────────┴─────────╯
╭────────────────────────────────────────────────────────────────────────╮
│ RAFT Meta Group Information │
├──────────────────┬──────────┬────────┬─────────┬────────┬────────┬─────┤
│ Connection Name │ ID │ Leader │ Current │ Online │ Active │ Lag │
├──────────────────┼──────────┼────────┼─────────┼────────┼────────┼─────┤
│ nats-cluster-a-0 │ 7Yz8mSw2 │ │ true │ true │ 231ms │ 0 │
│ nats-cluster-b-0 │ 8SHWVnwb │ yes │ true │ true │ 0s │ 0 │
│ nats-cluster-b-1 │ 7EMHrnfe │ │ true │ true │ 231ms │ 0 │
│ nats-cluster-b-2 │ GUa4jknS │ │ true │ true │ 231ms │ 0 │
╰──────────────────┴──────────┴────────┴─────────┴────────┴────────┴─────╯

Remove the last peer of `nats-cluster-a`.

wide760nats --user test --password test server cluster peer-remove 7Yz8mSw2

Go to the nats-box of `nats-cluster-b` and check if stream1b is still available.

bashwide760nats --user demo --password demo stream view stream1bwide760[1] Subject: stream1.updates Received: 2025-07-02T04:11:01Z
Nats-Stream-Source: stream1 1 > >
cluster-a: published 2025-07-02T03:35:59.623080
[2] Subject: stream1.updates Received: 2025-07-02T04:11:01Z
Nats-Stream-Source: stream1 2 > >
cluster-a: published 2025-07-02T03:36:00.624715
....

The gateway should be removed from the `nats-cluster-b` ConfigMap. This can be most easily achieved by adjusting the Helm values and subsequently upgrading the NATS cluster.

bashwide760 "gateway": {
"gateways": [
{
"name": "nats-cluster-a",
"urls": [
"nats://nats-cluster-a-headless.v2-testing.svc.cluster.local:7222"
]
}
],
"name": "nats-cluster-b",
"port": 7222
},bashwide760nats --user test2 --password test2 server report jetstream
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ JetStream Summary │
├───────────────────┬────────────────┬────────┬─────────┬───────────┬──────────┬─────────┬────────┬─────────┬─────────┬─────────┬─────────┤
│ Server │ Cluster │ Domain │ Streams │ Consumers │ Messages │ Bytes │ Memory │ File │ API Req │ API Err │ Pending │
├───────────────────┼────────────────┼────────┼─────────┼───────────┼──────────┼─────────┼────────┼─────────┼─────────┼─────────┼─────────┤
│ nats-cluster-b-0 │ nats-cluster-b │ hub │ 2 │ 0 │ 250 │ 35 KiB │ 0 B │ 35 KiB │ 0 │ 0 │ 0 │
│ nats-cluster-b-1 │ nats-cluster-b │ hub │ 2 │ 0 │ 250 │ 35 KiB │ 0 B │ 35 KiB │ 0 │ 0 │ 0 │
│ nats-cluster-b-2\* │ nats-cluster-b │ hub │ 2 │ 0 │ 250 │ 35 KiB │ 0 B │ 35 KiB │ 0 │ 0 │ 0 │
├───────────────────┼────────────────┼────────┼─────────┼───────────┼──────────┼─────────┼────────┼─────────┼─────────┼─────────┼─────────┤
│ │ │ │ 6 │ 0 │ 750 │ 104 KiB │ 0 B │ 104 KiB │ 0 │ 0 │ 0 │
╰───────────────────┴────────────────┴────────┴─────────┴───────────┴──────────┴─────────┴────────┴─────────┴─────────┴─────────┴─────────╯
╭────────────────────────────────────────────────────────────────────────╮
│ RAFT Meta Group Information │
├──────────────────┬──────────┬────────┬─────────┬────────┬────────┬─────┤
│ Connection Name │ ID │ Leader │ Current │ Online │ Active │ Lag │
├──────────────────┼──────────┼────────┼─────────┼────────┼────────┼─────┤
│ nats-cluster-b-0 │ 8SHWVnwb │ │ true │ true │ 160ms │ 0 │
│ nats-cluster-b-1 │ 7EMHrnfe │ │ true │ true │ 160ms │ 0 │
│ nats-cluster-b-2 │ GUa4jknS │ yes │ true │ true │ 0s │ 0 │
╰──────────────────┴──────────┴────────┴─────────┴────────┴────────┴─────╯

The next step is to modify the **publishers and subscribers' ConfigMaps** to reference the new streams. This modification can conveniently occur before the publishers and subscribers are shut down.

Once this is complete, the final steps are to scale up the publishers and subscribers and decommission the old NATS cluster.

## Conclusion

Live data migrations present significant challenges with the NATS supercluster. A key limitation is the inability to directly replicate NATS streams between clusters. Specifically, a stream mirrored from `nats-cluster-a` to `nats-cluster-b` cannot retain its original name. This naming restriction hinders seamless migration. Another critical drawback is that the NATS key-value store, once migrated, cannot be made writable in the target `nats-cluster-b`. Overcoming these limitations for a migration would require unacceptably extensive modifications to the configmaps.

## Plan migrating NATS

The plan to migrate NATS is located at Migrating brokers NATS and RabbitMQ.
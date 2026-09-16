---
id: confluence:794460161
source: confluence
type: page
space: TC
title: Synchronization script small Mongodb databases
author: Minh Trang Nguyen (Unlicensed)
date: '2025-07-09'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/794460161
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/794460161
---
# Synchronization script small Mongodb databases

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/794460161  

## Content

Status: work in progress

## Introduction

This document describes the improved setup for synchronizing two MongoDB databases. The previous cached solution was unstable and has therefore been replaced. The revised setup now consists of a Python script that listens for changes in the source MongoDB database and a separate script that synchronizes this data to the target. This synchronization script only activates when the target MongoDB database is online. All messages are temporarily stored in a local RabbitMQ instance, ensuring reliable delivery.

Python was chosen for its straightforward deployment within the cluster, as it eliminates the need for building a Docker image. While Python can be memory-intensive and its garbage collector may not always be optimal, running the script for a day should be acceptable. However, synchronizing the data as quickly as possible to minimize potential memory impact.

## Change the source database to Replica Set

Changing to Replica Set mode carries some risk. Reverting to standalone mode may not be possible. To mitigate this, take a snapshot of the database before proceeding.

For every MongoDB deployment where you intend to use the sync database tool, add the specified environment variable and restart the deployment.

bashwide760- name: MONGODB\_REPLICA\_SET\_MODE
value: "primary"
- name: MONGODB\_REPLICA\_SET\_NAME
value: "rs0"
- name: MONGODB\_REPLICA\_SET\_KEY
value: "replicakey"

Log in to the MongoDB shell.

bashwide760mongo --username root -password <PASSWORD> --authenticationDatabase admin

Change mode:

bashwide760# Check Replica status
rs.status();
# Change to Replica Set mode
rs.initiate({
\_id: "rs0",
members: [
{ \_id: 0, host: "<MONGODB K8S SERVICE ADDRESS>:27017" }
]
});

The MongoDB host must be accessible via a hostname resolving to its private IP address. `external-dns` handles the automatic creation/update of this private DNS record. You can modify the hostname used in the MongoDB configuration later if needed.

bashwide760rs.conf()
let config = rs.conf();
config.members[0].host = "<MONGODB K8S SERVICE ADDRESS>:27017";
rs.reconfig(config);

## Script listening for changes

For listening, this script must be applied strictly once per namespace.

pywide760import os
import asyncio
import json
import logging
import signal
from motor.motor\_asyncio import AsyncIOMotorClient
from pymongo.errors import PyMongoError
from aio\_pika import connect\_robust, Message, RobustConnection, RobustChannel
from aio\_pika.exceptions import AMQPConnectionError, ChannelClosed
SRC\_MONGO\_USER = os.environ.get("SRC\_MONGO\_USER", "root")
SRC\_MONGO\_PASSWORD = os.environ.get("SRC\_MONGO\_PASSWORD", "develop")
SRC\_MONGO\_HOST = os.environ.get("SRC\_MONGO\_HOST", "localhost")
SRC\_MONGO\_PORT = os.environ.get("SRC\_MONGO\_PORT", "27017")
MONGO\_URI = f"mongodb://{SRC\_MONGO\_USER}:{SRC\_MONGO\_PASSWORD}@{SRC\_MONGO\_HOST}:{SRC\_MONGO\_PORT}"
RABBITMQ\_HOST = os.environ.get("RABBITMQ\_HOST", "localhost")
RABBITMQ\_PORT = int(os.environ.get("RABBITMQ\_PORT", "5672"))
RABBITMQ\_USER = os.environ.get("RABBITMQ\_USER", "waitforchanges")
RABBITMQ\_PASSWORD = os.environ.get("RABBITMQ\_PASSWORD", "admin")
RABBITMQ\_HEARTBEAT = int(os.environ.get("RABBITMQ\_HEARTBEAT", "60"))
RABBITMQ\_VIRTUAL\_HOST = os.environ.get("RABBITMQ\_VIRTUAL\_HOST", "/")
QUEUE\_NAME = "mongodb\_changes"
SKIP\_DBS = {"admin", "config", "local"}
# 30 days in milliseconds
TTL\_MESSAGE\_MS = 2592000000
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(\_\_name\_\_)
shutdown\_event = asyncio.Event()
async def connect\_to\_rabbitmq() -> RobustConnection:
retries = 0
max\_retries = 10
while not shutdown\_event.is\_set():
try:
logger.info(f"Attempting to connect to RabbitMQ ({RABBITMQ\_HOST}:{RABBITMQ\_PORT}) with heartbeat={RABBITMQ\_HEARTBEAT}s...")
connection = await connect\_robust(
host=RABBITMQ\_HOST,
port=RABBITMQ\_PORT,
login=RABBITMQ\_USER,
password=RABBITMQ\_PASSWORD,
virtualhost=RABBITMQ\_VIRTUAL\_HOST,
heartbeat=RABBITMQ\_HEARTBEAT,
timeout=20
)
logger.info("Successfully connected to RabbitMQ.")
return connection
except (AMQPConnectionError, ConnectionRefusedError, asyncio.TimeoutError) as e:
retries += 1
if retries > max\_retries:
logger.error(f"Failed to connect to RabbitMQ after {max\_retries} attempts. Exiting.")
raise e
wait\_time = min(2 \*\* retries, 30)
logger.warning(f"RabbitMQ connection failed: {e}. Retrying in {wait\_time} seconds...")
await asyncio.sleep(wait\_time)
except asyncio.CancelledError:
raise
raise asyncio.CancelledError("Shutdown initiated during RabbitMQ connection attempt.")
async def setup\_rabbitmq\_channel(connection: RobustConnection) -> RobustChannel:
channel = await connection.channel()
await channel.declare\_queue(
QUEUE\_NAME,
durable=True,
arguments={
"x-queue-type": "quorum",
"x-message-ttl": TTL\_MESSAGE\_MS
}
)
logger.info(f"RabbitMQ channel and queue '{QUEUE\_NAME}' declared successfully.")
return channel
async def connect\_to\_mongodb() -> AsyncIOMotorClient:
retries = 0
max\_retries = 10
while not shutdown\_event.is\_set():
try:
logger.info(f"Attempting to connect to MongoDB at {MONGO\_URI}...")
client = AsyncIOMotorClient(MONGO\_URI)
await client.admin.command('ping')
logger.info("Successfully connected to MongoDB.")
return client
except PyMongoError as e:
retries += 1
if retries > max\_retries:
logger.error(f"Failed to connect to MongoDB after {max\_retries} attempts. Exiting.")
raise e
wait\_time = min(2 \*\* retries, 30)
logger.warning(f"MongoDB connection failed: {e}. Retrying in {wait\_time} seconds...")
await asyncio.sleep(wait\_time)
raise asyncio.CancelledError("Shutdown initiated during MongoDB connection attempt.")
async def process\_change\_stream():
mongo\_client: AsyncIOMotorClient = None
rmq\_conn: RobustConnection = None
channel: RobustChannel = None
change\_stream = None
while not shutdown\_event.is\_set():
try:
if not mongo\_client or not rmq\_conn or not channel or rmq\_conn.is\_closed or channel.is\_closed:
if rmq\_conn and not rmq\_conn.is\_closed:
await rmq\_conn.close()
if mongo\_client:
mongo\_client.close()
rmq\_conn = await connect\_to\_rabbitmq()
channel = await setup\_rabbitmq\_channel(rmq\_conn)
mongo\_client = await connect\_to\_mongodb()
logger.info("Starting MongoDB change stream watch.")
change\_stream = mongo\_client.watch(full\_document='updateLookup')
async with change\_stream:
logger.info("Listening for changes across all databases...")
async for change in change\_stream:
if shutdown\_event.is\_set():
logger.info("Shutdown event set, exiting change stream processing.")
break
ns = change.get("ns", {})
db = ns.get("db")
coll = ns.get("coll", "unknown\_collection")
if db in SKIP\_DBS:
continue
event = {
"database": db,
"collection": coll,
"operation\_type": change.get("operationType"),
"full\_document": change.get("fullDocument"),
"update\_description": change.get("updateDescription"),
"document\_key": change.get("documentKey"),
}
logger.info(f"Change detected: {event['operation\_type']} in {db}.{coll}")
try:
payload = json.dumps(event, default=str).encode()
await channel.default\_exchange.publish(
Message(payload),
routing\_key=QUEUE\_NAME
)
logger.debug(f"Message published for {db}.{coll}")
except ChannelClosed as e:
logger.error(f"RabbitMQ channel closed while publishing: {e}. Attempting re-initialization.")
break
except Exception as e:
logger.error(f"Failed to publish message to RabbitMQ: {e}", exc\_info=True)
except PyMongoError as e:
logger.error(f"Error in MongoDB change stream: {e}. Attempting to re-establish change stream...", exc\_info=True)
if mongo\_client:
mongo\_client.close()
await asyncio.sleep(5)
except (AMQPConnectionError, ConnectionRefusedError) as e:
logger.error(f"RabbitMQ connection error: {e}. Attempting to reconnect...", exc\_info=True)
if rmq\_conn and not rmq\_conn.is\_closed:
await rmq\_conn.close()
await asyncio.sleep(5)
except asyncio.CancelledError:
logger.info("Change stream processing task cancelled.")
break
except Exception as e:
logger.error(f"Unexpected error in main processing loop: {e}. Restarting loop...", exc\_info=True)
await asyncio.sleep(10)
finally:
if shutdown\_event.is\_set():
if change\_stream and not change\_stream.closed:
await change\_stream.close()
if rmq\_conn and not rmq\_conn.is\_closed:
await rmq\_conn.close()
if mongo\_client:
mongo\_client.close()
def handle\_signal(signum, frame):
logger.info(f"Signal {signum} received. Initiating graceful shutdown.")
shutdown\_event.set()
async def main():
signal.signal(signal.SIGINT, handle\_signal)
signal.signal(signal.SIGTERM, handle\_signal)
logger.info("Starting MongoDB Change Stream to RabbitMQ Publisher.")
try:
await process\_change\_stream()
except asyncio.CancelledError:
logger.info("Main task cancelled, shutting down.")
except Exception as e:
logger.critical(f"Unhandled exception in main: {e}", exc\_info=True)
finally:
logger.info("Application shutdown complete.")
if \_\_name\_\_ == "\_\_main\_\_":
asyncio.run(main())

Put the code in file `mongodb_changes.py`.

Add this script to a ConfigMap:

bashwide760kubectl create configmap mongodbchanges \
--from-file=mongodb\_changes.py=./mongodb\_changes.py \
--dry-run=client -o yaml | kubectl apply -f -

## Script syncing changes

For synchronization, this script must be applied strictly once per namespace.

pywide760import asyncio
import json
import logging
import os
import signal
from aio\_pika import connect\_robust, IncomingMessage, RobustConnection, RobustChannel, Queue
from aio\_pika.exceptions import AMQPConnectionError
from motor.motor\_asyncio import AsyncIOMotorClient
from pymongo.errors import PyMongoError, ConnectionFailure
TGT\_MONGO\_USER = os.environ.get("TGT\_MONGO\_USER", "root")
TGT\_MONGO\_PASSWORD = os.environ.get("TGT\_MONGO\_PASSWORD", "develop")
TGT\_MONGO\_HOST = os.environ.get("TGT\_MONGO\_HOST", "localhost")
TGT\_MONGO\_PORT = os.environ.get("TGT\_MONGO\_PORT", "27018")
MONGO\_URI = f"mongodb://{TGT\_MONGO\_USER}:{TGT\_MONGO\_PASSWORD}@{TGT\_MONGO\_HOST}:{TGT\_MONGO\_PORT}"
RABBITMQ\_HOST = os.environ.get("RABBITMQ\_HOST", "localhost")
RABBITMQ\_PORT = int(os.environ.get("RABBITMQ\_PORT", "5672"))
RABBITMQ\_USER = os.environ.get("RABBITMQ\_USER", "syncer")
RABBITMQ\_PASSWORD = os.environ.get("RABBITMQ\_PASSWORD", "admin")
RABBITMQ\_HEARTBEAT = int(os.environ.get("RABBITMQ\_HEARTBEAT", "60"))
RABBITMQ\_VIRTUAL\_HOST = os.environ.get("RABBITMQ\_VIRTUAL\_HOST", "/")
QUEUE\_NAME = "mongodb\_changes"
# 30 days in milliseconds
TTL\_MESSAGE\_MS = 2592000000
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(\_\_name\_\_)
shutdown\_event = asyncio.Event()
mongo\_client: AsyncIOMotorClient = None
rmq\_connection: RobustConnection = None
rmq\_channel: RobustChannel = None
rmq\_queue: Queue = None
async def connect\_to\_mongodb() -> AsyncIOMotorClient:
retries = 0
max\_retries = 10
while not shutdown\_event.is\_set():
try:
logger.info(f"Attempting to connect to MongoDB at {MONGO\_URI}...")
client = AsyncIOMotorClient(MONGO\_URI)
await client.admin.command('ping')
logger.info("Successfully connected to MongoDB.")
return client
except (PyMongoError, ConnectionFailure) as e:
retries += 1
if retries > max\_retries:
logger.error(f"Failed to connect to MongoDB after {max\_retries} attempts. Exiting.")
raise e
wait\_time = min(2 \*\* retries, 30) # Exponential backoff, max 30 seconds
logger.warning(f"MongoDB connection failed: {e}. Retrying in {wait\_time} seconds...")
await asyncio.sleep(wait\_time)
except asyncio.CancelledError:
raise
raise asyncio.CancelledError("Shutdown initiated during MongoDB connection attempt.")
async def connect\_to\_rabbitmq() -> RobustConnection:
retries = 0
max\_retries = 10
while not shutdown\_event.is\_set():
try:
logger.info(f"Attempting to connect to RabbitMQ ({RABBITMQ\_HOST}:{RABBITMQ\_PORT}) with heartbeat={RABBITMQ\_HEARTBEAT}s...")
connection = await connect\_robust(
host=RABBITMQ\_HOST,
port=RABBITMQ\_PORT,
login=RABBITMQ\_USER,
password=RABBITMQ\_PASSWORD,
virtualhost=RABBITMQ\_VIRTUAL\_HOST,
heartbeat=RABBITMQ\_HEARTBEAT,
timeout=20
)
logger.info("Successfully connected to RabbitMQ.")
return connection
except (AMQPConnectionError, ConnectionRefusedError, asyncio.TimeoutError) as e:
retries += 1
if retries > max\_retries:
logger.error(f"Failed to connect to RabbitMQ after {max\_retries} attempts. Exiting.")
raise e
wait\_time = min(2 \*\* retries, 30)
logger.warning(f"RabbitMQ connection failed: {e}. Retrying in {wait\_time} seconds...")
await asyncio.sleep(wait\_time)
except asyncio.CancelledError:
raise
raise asyncio.CancelledError("Shutdown initiated during RabbitMQ connection attempt.")
async def setup\_rabbitmq\_queue(connection: RobustConnection) -> tuple[RobustChannel, Queue]:
channel = await connection.channel()
await channel.set\_qos(prefetch\_count=1)
queue = await channel.declare\_queue(
QUEUE\_NAME,
durable=True,
arguments={
"x-queue-type": "quorum",
"x-message-ttl": TTL\_MESSAGE\_MS
}
)
logger.info(f"RabbitMQ channel and queue '{QUEUE\_NAME}' declared successfully.")
return channel, queue
async def on\_message(message: IncomingMessage) -> None:
global mongo\_client
try:
data = json.loads(message.body.decode())
logger.debug(f"Received message: {data}")
operation = data.get("operation\_type")
database = data.get("database")
collection = data.get("collection")
if not database or not collection:
logger.error("Missing database or collection in message. Acknowledging message.")
await message.ack()
return
if not mongo\_client or not await mongo\_client.admin.command('ping'):
logger.warning("MongoDB client not connected or ping failed. Re-attempting connection for this message.")
try:
mongo\_client = await connect\_to\_mongodb()
except Exception as e:
logger.error(f"Failed to re-connect to MongoDB for message processing: {e}. Nacking message.")
await message.nack(requeue=True)
return
db = mongo\_client[database]
coll = db[collection]
if operation == "insert":
full\_document = data.get("full\_document", {})
result = await coll.insert\_one(full\_document)
logger.info(f"Inserted document with \_id: {result.inserted\_id} into {database}.{collection}")
elif operation == "update":
document\_key = data.get("document\_key")
updated\_fields = data.get("update\_description", {}).get("updatedFields", {})
if document\_key and updated\_fields:
result = await coll.update\_one(document\_key, {"$set": updated\_fields})
logger.info(f"Updated {result.modified\_count} document(s) in {database}.{collection}")
else:
logger.error("Missing document\_key or updatedFields for update operation. Acknowledging message.")
elif operation == "replace":
document\_key = data.get("document\_key")
full\_document = data.get("full\_document", {})
if document\_key and full\_document:
result = await coll.replace\_one(document\_key, full\_document)
logger.info(f"Replaced {result.modified\_count} document(s) in {database}.{collection}")
else:
logger.error("Missing document\_key or full\_document for replace operation. Acknowledging message.")
elif operation == "delete":
document\_key = data.get("document\_key")
if document\_key:
result = await coll.delete\_one(document\_key)
logger.info(f"Deleted {result.deleted\_count} document(s) from {database}.{collection}")
else:
logger.error("Missing document\_key for delete operation. Acknowledging message.")
else:
logger.warning(f"Unknown operation\_type: {operation}. Acknowledging message.")
await message.ack()
logger.debug(f"Message acknowledged for {operation} in {database}.{collection}")
except json.JSONDecodeError:
logger.error(f"Invalid JSON received: {message.body.decode()}. Rejecting message without re-queue.")
await message.reject(requeue=False)
except PyMongoError as e:
logger.error(f"MongoDB error processing message: {e}. Nacking message and requeueing.", exc\_info=True)
await message.nack(requeue=True)
except Exception as e:
logger.exception(f"Unexpected error processing message: {e}. Nacking message and requeueing.", exc\_info=True)
await message.nack(requeue=True)
def handle\_signal(signum, frame):
logger.info(f"Signal {signum} received. Initiating graceful shutdown.")
shutdown\_event.set()
async def consumer\_loop():
global mongo\_client, rmq\_connection, rmq\_channel, rmq\_queue
while not shutdown\_event.is\_set():
try:
if not mongo\_client:
mongo\_client = await connect\_to\_mongodb()
if not rmq\_connection or rmq\_connection.is\_closed:
if rmq\_connection and not rmq\_connection.is\_closed:
await rmq\_connection.close()
rmq\_connection = await connect\_to\_rabbitmq()
if not rmq\_channel or rmq\_channel.is\_closed:
if rmq\_channel and not rmq\_channel.is\_closed:
await rmq\_channel.close()
rmq\_channel, rmq\_queue = await setup\_rabbitmq\_queue(rmq\_connection)
logger.info(f"Starting message consumption on queue: {QUEUE\_NAME}")
async with rmq\_queue.iterator() as queue\_iterator:
async for message in queue\_iterator:
if shutdown\_event.is\_set():
logger.info("Shutdown event set, stopping message consumption.")
break
await on\_message(message)
except PyMongoError as e:
logger.error(f"MongoDB connection or operation error: {e}. Re-attempting connections...", exc\_info=True)
if mongo\_client:
mongo\_client.close()
mongo\_client = None
await asyncio.sleep(5)
except AMQPConnectionError as e:
logger.error(f"RabbitMQ connection error: {e}. Re-attempting connections...", exc\_info=True)
if rmq\_connection and not rmq\_connection.is\_closed:
await rmq\_connection.close()
rmq\_connection = None
rmq\_channel = None
rmq\_queue = None
await asyncio.sleep(5)
except asyncio.CancelledError:
logger.info("Consumer loop cancelled.")
break
except Exception as e:
logger.critical(f"Unhandled exception in consumer\_loop: {e}. Restarting loop...", exc\_info=True)
await asyncio.sleep(10)
logger.info("Exiting consumer loop.")
async def main() -> None:
signal.signal(signal.SIGINT, handle\_signal)
signal.signal(signal.SIGTERM, handle\_signal)
logger.info("Starting RabbitMQ to MongoDB Consumer.")
try:
await consumer\_loop()
except asyncio.CancelledError:
logger.info("Main consumer task cancelled, shutting down.")
except Exception as e:
logger.critical(f"Unhandled exception in main: {e}", exc\_info=True)
finally:
logger.info("Closing connections...")
if rmq\_connection and not rmq\_connection.is\_closed:
await rmq\_connection.close()
if mongo\_client:
mongo\_client.close()
logger.info("Application shutdown complete.")
if \_\_name\_\_ == "\_\_main\_\_":
asyncio.run(main())

Put the code in file `mongodb_sync.py`.

Add this script to a ConfigMap:

wide760kubectl create configmap mongodbsync \
--from-file=mongodb\_sync.py=./mongodb\_sync.py \
--dry-run=client -o yaml | kubectl apply -f -

## Deployment sync script

The local RabbitMQ instance uses a PVC to store queue messages. Remember to delete this PVC once the synchronization process is complete.

Some changes are required for each setup:

Change for the source MongoDB host and password.

yamlwide760env:
- name: SRC\_MONGO\_HOST
value: "<MONGO SERVICE>.<NAMESPACE>.svc.cluster.local"
- name: SRC\_MONGO\_PASSWORD
valueFrom:
secretKeyRef:
name: mongodb-secrets
key: mongodb-root-password

Modify the target MongoDB host and password. The host must be a Route 53 address, pointing to the Network Load Balancer.

yamlwide760env:
- name: TGT\_MONGO\_HOST
value: "<ROUTE 53 ADDRESS NETWORK LOAD BALANCER>"
- name: TGT\_MONGO\_PORT
value: "27017"
- name: TGT\_MONGO\_PASSWORD
value: "<PUT HERE THE PASSWORD OF THE TARGET>"

Template deployment:

yamlwide760apiVersion: v1
kind: PersistentVolumeClaim
metadata:
name: pvc-rabbitmq-local
spec:
accessModes:
- ReadWriteOnce
resources:
requests:
storage: 4Gi
---
apiVersion: apps/v1
kind: Deployment
metadata:
name: mongodb-sync-script
spec:
replicas: 1
selector:
matchLabels:
app: mongodb-sync-script
template:
metadata:
labels:
app: mongodb-sync-script
spec:
containers:
- name: rabbitmq
image: bitnami/rabbitmq:4.0.2
volumeMounts:
- name: volume-rabbitmq
mountPath: /opt/bitnami/rabbitmq/.rabbitmq/mnesia
ports:
- containerPort: 5672
- containerPort: 15672
env:
- name: RABBITMQ\_USERNAME
value: localuser
- name: RABBITMQ\_PASSWORD
value: admin
lifecycle:
postStart:
exec:
command:
- /bin/bash
- -c
- |
until rabbitmqctl status; do sleep 5; done
rabbitmqctl add\_user waitforchanges admin
rabbitmqctl set\_user\_tags waitforchanges administrator
rabbitmqctl set\_permissions -p / waitforchanges ".\*" ".\*" ".\*"
rabbitmqctl add\_user syncer admin
rabbitmqctl set\_user\_tags syncer administrator
rabbitmqctl set\_permissions -p / syncer ".\*" ".\*" ".\*"
- name: mongodb-changes
image: python:3.12-bookworm
volumeMounts:
- name: volume-mongodb-changes
mountPath: /app/mongodb\_changes.py
subPath: mongodb\_changes.py
env:
- name: SRC\_MONGO\_HOST
value: "<MONGO SERVICE>.<NAMESPACE>.svc.cluster.local"
- name: SRC\_MONGO\_PASSWORD
valueFrom:
secretKeyRef:
name: mongodb-secrets
key: mongodb-root-password
command: ["/bin/sh", "-c"]
args:
- pip install pymongo && pip install aio\_pika && pip install motor && python /app/mongodb\_changes.py
- name: mongodb-sync
image: python:3.12-bookworm
volumeMounts:
- name: volume-mongodb-sync
mountPath: /app/mongodb\_sync.py
subPath: mongodb\_sync.py
env:
- name: TGT\_MONGO\_HOST
value: "<ROUTE 53 ADDRESS NETWORK LOAD BALANCER>"
- name: TGT\_MONGO\_PORT
value: "27017"
- name: TGT\_MONGO\_PASSWORD
value: "<PUT HERE THE PASSWORD OF THE TARGET>"
command: ["/bin/sh", "-c"]
args:
- pip install pymongo && pip install aio\_pika && pip install motor && python /app/mongodb\_sync.py
volumes:
- name: volume-mongodb-changes
configMap:
name: mongodbchanges
- name: volume-mongodb-sync
configMap:
name: mongodbsync
- name: volume-rabbitmq
persistentVolumeClaim:
claimName: pvc-rabbitmq-local

After successfully modifying the deployment template, apply it.

wide760kubectl apply -f - <<EOF
<DEPLOYMENT MANIFEST HERE>
EOF

## Start migrating

Create a snapshot and restore the snapshot in the new OU. See document.

Migrating to AWS OU (Organisation Unit)

## Example logs

The `mongodb-changes` container's logs should display output similar to the following:

wide760 2025-07-08 16:03:57,185 - INFO - Starting MongoDB Change Stream to RabbitMQ Publisher.
2025-07-08 16:03:57,185 - INFO - Attempting to connect to RabbitMQ (localhost:5672) with heartbeat=60s...
2025-07-08 16:03:57,193 - INFO - Successfully connected to RabbitMQ.
2025-07-08 16:03:57,194 - INFO - RabbitMQ channel and queue 'mongodb\_changes' declared successfully.
2025-07-08 16:03:57,194 - INFO - Attempting to connect to MongoDB at mongodb://root:password@mongodb-source-0.mongodb-source-headless.testing.svc.cluster.local:27017...
2025-07-08 16:03:57,205 - INFO - Successfully connected to MongoDB.
2025-07-08 16:03:57,206 - INFO - Starting MongoDB change stream watch.
2025-07-08 16:03:57,207 - INFO - Listening for changes across all databases... 

The mongodb-sync contains’s logs:

wide760 2025-07-08 16:29:40,084 - INFO - Inserted document with \_id: 686d3d9fd2ed14b1ddf296f8 into develop.example
2025-07-08 16:29:40,102 - INFO - Inserted document with \_id: 686d3d9fd2ed14b1ddf296f9 into develop.example
2025-07-08 16:29:40,119 - INFO - Inserted document with \_id: 686d3d9fd2ed14b1ddf296fa into develop.example
2025-07-08 16:29:40,140 - INFO - Inserted document with \_id: 686d3d9fd2ed14b1ddf296fb into develop.example
2025-07-08 16:29:40,154 - INFO - Inserted document with \_id: 686d3d9fd2ed14b1ddf296fc into develop.example
2025-07-08 16:29:40,173 - INFO - Inserted document with \_id: 686d3d9fd2ed14b1ddf296fd into develop.example
2025-07-08 16:29:40,192 - INFO - Inserted document with \_id: 686d3d9fd2ed14b1ddf296fe into develop.example
2025-07-08 16:29:40,211 - INFO - Inserted document with \_id: 686d3d9fd2ed14b1ddf296ff into develop.example
2025-07-08 16:29:40,231 - INFO - Inserted document with \_id: 686d3d9fd2ed14b1ddf29700 into develop.example
2025-07-08 16:29:40,246 - INFO - Inserted document with \_id: 686d3d9fd2ed14b1ddf29701 into develop.example
2025-07-08 16:29:40,261 - INFO - Inserted document with \_id: 686d3d9fd2ed14b1ddf29702 into develop.example
2025-07-08 16:29:40,281 - INFO - Inserted document with \_id: 686d3d9fd2ed14b1ddf29703 into develop.example
2025-07-08 16:29:40,298 - INFO - Inserted document with \_id: 686d3d9fd2ed14b1ddf29704 into develop.example
2025-07-08 16:29:40,328 - INFO - Inserted document with \_id: 686d3d9fd2ed14b1ddf29705 into develop.example
2025-07-08 16:29:40,347 - INFO - Inserted document with \_id: 686d3d9fd2ed14b1ddf29706 into develop.example
2025-07-08 16:29:40,367 - INFO - Inserted document with \_id: 686d3d9fd2ed14b1ddf29707 into develop.example
2025-07-08 16:29:40,385 - INFO - Inserted document with \_id: 686d3d9fd2ed14b1ddf29708 into develop.example
2025-07-08 16:29:40,424 - INFO - Inserted document with \_id: 686d3d9fd2ed14b1ddf29709 into develop.example
2025-07-08 16:29:40,441 - INFO - Inserted document with \_id: 686d3d9fd2ed14b1ddf2970a into develop.example 

## Total queue messages

To check the number of remaining messages, enter the `rabbitmq` container and run the following command:

bashwide760rabbitmqctl list\_queueswide760Timeout: 60.0 seconds ...
Listing queues for vhost / ...
name messages
mongodb\_changes 3001

## Test results

During testing, database changes were generated by a separate script for one hour. After this period, the target database was enabled to accept connections. The process ran without issues, the queue was fully consumed, and all approximately 120.000 database changes were successfully replicated to the new MongoDB database.
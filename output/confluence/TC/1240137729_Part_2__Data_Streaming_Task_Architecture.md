---
id: confluence:1240137729
source: confluence
type: page
space: TC
title: Part 2. Data Streaming Task Architecture
author: Panji Y. Wiwaha
date: '2026-06-10'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1240137729
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1240137729
---
# Part 2. Data Streaming Task Architecture

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1240137729  

## Content

# **Data Streaming Task with Airflow Triggerer & Deferrable Operators**

## **Why Do We Need the Airflow Triggerer**

### **The Problem in Our Streaming Pipeline**

Our streaming pipelines continuously listen to RabbitMQ message queues. Each pipeline wakes up frequently, checks whether new messages have arrived, and if not, keeps waiting and checks again every few seconds for up to several minutes.

Think of it like an employee whose only job is to sit by a mailbox and check whether a letter has arrived. Most of the time, the mailbox is empty, but the employee is still fully occupied. Therefore, they cannot do any other work while waiting.

In Airflow, each running task occupies a **worker slot**, a reserved unit of compute capacity. Without a smarter approach, every one of these "waiting" tasks would permanently hold a worker slot even while doing absolutely nothing useful. When you have multiple stream types running concurrently, many worker slots get consumed purely by idle waiting, leaving fewer slots available for the actual data processing work that matters.

This is the core problem the Triggerer solves.

## **What Is the Airflow Triggerer**

The **Triggerer** is a separate, lightweight Airflow service introduced in Airflow 2.2. Its only responsibility is to **watch for conditions** on behalf of waiting tasks — so that workers do not have to.

A good real-world analogy: instead of the employee sitting by the mailbox themselves, they hire a **doorbell assistant**. The assistant watches the mailbox in the background. The employee is now free to do other work. When a letter finally arrives, the assistant rings the doorbell, and only then does the employee come back to collect it.

The Triggerer works the same way:

* It runs many small "watchers" (called **Triggers**) simultaneously in the background
* Each watcher periodically checks a condition (e.g., "does the RabbitMQ queue have messages?")
* When the condition is met, it rings the doorbell and notifies Airflow to resume the task on a worker
* Because all watchers run asynchronously inside a single process, the Triggerer can monitor **hundreds of queues at the same time** with very little resource usage

## **Deferrable Operators: Role and Differences**

### **What Is a Normal Operator**

A normal Airflow operator runs a task from start to finish while holding a worker slot the entire time. If the task needs to wait for something, such as a message arriving on a queue, it keeps the worker slot occupied the entire time it waits, even if it is doing nothing productive.

### **What Is a Deferrable Operator**

A deferrable operator is smarter. When it realizes it needs to wait, it:

1. **Pauses itself** and hands the waiting responsibility off to the **Triggerer**
2. **Releases the worker slot** immediately; the worker can run other tasks once released
3. **Sleeps in the background** via a lightweight Trigger in the **Triggerer** process
4. **Resumes on a worker** only when the condition is met (e.g., messages arrived) or the wait times out

Data streaming task operator side-by-side comparison

|  | **Normal Operator** | **Deferrable Operator** |
| --- | --- | --- |
| **When waiting** | Holds a full worker slot — blocked | Releases the worker slot — free for other work |
| **Who does the watching** | The worker itself | The Triggerer, in the background |
| **Resource cost while waiting** | High — a full worker process is reserved | Low — a tiny watcher runs in the Triggerer |
| **Can handle many concurrent waits?** | No — limited by the number of workers | Yes — the Triggerer handles hundreds at once |
| **Resumes how?** | Never pauses — runs continuously | Resumes via a callback once the condition is met |

### **How It Works Step by Step (In Our Pipeline)**

#### **Step 1 — Quick check on arrival**

When the task starts, it quickly peeks at the RabbitMQ queue. If messages are already there, it consumes them immediately — no waiting needed. If the queue is empty, it moves to Step 2.

#### **Step 2 — Hand off to the Triggerer**

The task pauses itself and hands a small Trigger watcher to the Triggerer. The worker slot is released. The Triggerer's watcher quietly checks the queue every 10 seconds.

#### **Step 3 — Doorbell rings**

When the Trigger detects messages in the queue (or the maximum wait time is reached), it sends a signal back to Airflow. Airflow then schedules the task to resume on an available worker.

#### **Step 4 — Resume and consume**

The task wakes up on a worker, reads the signal (messages available, or timed out), and either consumes the messages or finishes cleanly with an empty result.

### **Why the Triggerer Is Mandatory**

A deferrable operator cannot watch for conditions on its own — it has handed that job off. The Triggerer is the process that actually runs those watchers. Without a running Triggerer, any task that defers would pause indefinitely and never resume. The Triggerer is therefore a **required component** whenever deferrable operators are used.

## **Real-World Parallels and Best Practices**

This pattern is widely adopted in production Airflow deployments. A common real-world example is waiting for a file to appear in cloud storage (e.g., Amazon S3). The traditional approach held a worker slot for hours doing nothing but checking. With the deferrable approach, the watcher runs in the Triggerer, and the worker is used only when the file actually needs to be processed.

**Best practices followed in our implementation:**

* **Check before deferring** — The task peeks at the queue first. If messages are already waiting, it skips the Triggerer entirely and consumes immediately. This avoids unnecessary overhead for the common "queue has data" case.
* **Graceful timeout handling** — If no messages arrive within the maximum wait window, the task finishes cleanly with an empty result rather than raising an error, keeping pipeline runs tidy.
* **Survive restarts** — The Trigger saves enough information about itself so that if the Triggerer process restarts, it can reconstruct all active watchers, and nothing is lost.
* **Efficient resource sharing** — Multiple watchers share underlying connections intelligently to avoid overwhelming the RabbitMQ broker with too many simultaneous connections.
* **Lazy loading** — Heavy service dependencies are loaded only when a task actually needs them, not at startup, keeping the system fast to initialize.

## **Technical Implementation**

The deferrable pattern is split across two classes that work together: the **operator** and the **trigger**.

### **The Operator —** `BasicRabbitMQDeferrableOperator`

Extends Airflow's `BaseOperator`. The two key entry points are `execute()` and `execute_complete()`. All other methods are internal helpers.

pywide760class BasicRabbitMQDeferrableOperator(BaseOperator):
def \_\_init\_\_(
self,
\*,
service\_factory: callable = None,
service\_class: type = None,
service\_kwargs: Dict = None,
poke\_interval: int = 10,
timeout: int = 300,
\*\*kwargs,
): ...
def execute(self, context: Context) -> Dict:
"""
Initial execution: Check the queue and decide to defer or consume.
"""
self.\_rmq\_service = self.\_create\_service() # lazy-load via factory
queue\_depth = self.\_peek\_queue\_depth()
if queue\_depth < 1:
self.defer(
trigger=self.\_create\_trigger(), # hand off to Triggerer
method\_name='execute\_complete', # resume callback
)
else:
return self.\_consume\_messages() # consume immediately
def execute\_complete(self, context: Context, event: Dict[str, Any]) -> Dict:
"""
Resume execution after the trigger fires.
"""
if event.get('status') == 'timeout':
return { 'updated\_count': 0, 'deleted\_count': 0, 'ignored\_count': 0}
self.\_rmq\_service = self.\_create\_service()
return self.\_consume\_messages()
def \_create\_service(self): ... # instantiate RMQ service via factory or class
def \_get\_service\_name(self) -> str: ... # return service name for logging
def \_peek\_queue\_depth(self) -> int: ... # passive queue check — no message consumption
def \_create\_trigger(self): ... # build BasicRabb`itMQMessageTrigger with credentials
def \_consume\_messages(self) -> Dict: ... # delegate to `service.consume\_data\_stream()`

### **The Trigger —** `BasicRabbitMQMessageTrigger`

Extends Airflow's `BaseTrigger`. Runs entirely inside the Triggerer process as a lightweight async watcher. The two required methods are `serialize()` and `run()`. All other methods are internal helpers.

pywide760class BasicRabbitMQMessageTrigger(BaseTrigger):
def \_\_init\_\_(
self,
hostname: str,
port: int,
vhost: str,
queue\_name: str,
username: str,
password: str,
poke\_interval: int = 10,
timeout: int = 300,
): ...
def serialize(self) -> tuple[str, dict[str, Any]]:
"""
Serialize trigger state so the Triggerer can reconstruct it after a restart.
"""
return (
'teqplay.triggers.rabbitmq\_trigger.BasicRabbitMQMessageTrigger',
{
'hostname': ...,
'queue\_name': ...,
'poke\_interval': ...,
'timeout': ...
}
)
async def run(self) -> AsyncIterator[TriggerEvent]:
"""
Async generator — polls the queue and yields TriggerEvent when the condition is met.
"""
while True:
if elapsed >= self.timeout:
yield TriggerEvent({'status': 'timeout', ...})
return
queue\_depth = await self.\_check\_queue\_depth\_async()
if queue\_depth > 0:
yield TriggerEvent({'status': 'success', ...})
return
await asyncio.sleep(self.poke\_interval)
async def \_check\_queue\_depth\_async(self) -> int: ... # offloads blocking pika call to thread pool
def \_check\_queue\_depth\_sync(self) -> int: ... # passive queue\_declare via thread-local connection

### **Execution Flow**

The diagram below shows the full lifecycle of a single streaming task run. There are five actors involved:

* **Airflow Scheduler** — decides when to start and resume tasks
* **Worker (1st slot)** — runs `execute()` and is released as soon as it defers
* **Triggerer Process** — a lightweight background process that takes over the waiting, running the polling loop without holding a worker slot
* **Worker (new slot)** — a fresh worker slot allocated only when there are messages to consume; calls `execute_complete()`
* **RabbitMQ Queue** — the external message source being watched

**The key moment to notice is the handoff**: the first worker releases its slot the instant it calls `self.defer()`, and the *Triggerer* takes over from that point.

A second worker is created only after the *Triggerer* confirms that messages have arrived.

## **Conclusion**

The Deferrable Operator pattern is what makes the streaming pipeline efficient at scale. Without it, every streaming task would hold a worker slot open for the entire duration it is waiting, even if that means sitting idle for minutes at a time. With it, the worker is freed the moment there is nothing to do, and only reclaimed when real work needs to be done.

The split between `BasicRabbitMQDeferrableOperator` and `BasicRabbitMQMessageTrigger` reflects a clear division of responsibility: the operator owns the business logic (consume messages, write to staging), and the trigger owns the waiting logic (poll RabbitMQ, fire when ready). This separation makes each class easier to understand, test, and maintain independently.

Together with the Airflow Triggerer process, this pattern allows the pipeline to run at high frequency (for example, every 30 seconds) without exhausting the worker pool, even when the queue is frequently empty.

---

**Shared at:** <placeholder> **|** <date-time>
---
id: confluence:1017118721
source: confluence
type: page
space: TC
title: 'Redis: How to configure a ACL user'
author: Jamie de Leest
date: '2026-02-02'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1017118721
explicit_links:
- jira:SHA-256
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1017118721
---
# Redis: How to configure a ACL user

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1017118721  

## Content

Redis introduced Access Control Lists (ACLs) in Redis 6 to give fine-grained control over what users can access and execute. With ACLs, you can manage users, assign passwords, limit their commands, and restrict key patterns.

---

# **Create an ACL User**

You create users with the `ACL SETUSER` command.

### **Basic syntax**

wide760ACL SETUSER <username> <rule> <rule> ...

## **Example: Create a Read-Only User**

### **Create the user**

wide760ACL SETUSER readonlyuser on >myStrongPassword123 +@read -@write ~\*

Let’s break down what this means:

| Rule | Description |
| --- | --- |
| `on` | Enable the user (users are OFF by default) |
| `>password` | Set login password (use strong passwords!) |
| `+@read` | Allow all read commands (GET, MGET, KEYS, etc.) |
| `-@write` | Deny all write commands |
| `~*` | Allow access to all keys |

If you want to restrict the user to only keys starting with `cache:`:

wide760~cache:\*

---

## Viewing, Editing, and Removing Users

### **List users:**

wide760ACL LIST

### **Show a specific user:**

wide760ACL GETUSER readonlyuser

### **Delete a user:**

wide760ACL DELUSER readonlyuser

---

# **Redis ACL: Complete Rule Reference**

A rule is one of the following types:

* **User state** (`on`, `off`)
* **Password rules** (`>password`, `<password`, `nopass`)
* **Command permissions** (`+cmd`, `-cmd`, `+@category`, `allcommands`)
* **Key access patterns** (`~pattern`, `resetkeys`)
* **Pub/Sub channel patterns** (`&pattern`, `resetchannels`)

---

## **User State Rules**

### `on`

Enables the user. Disabled users cannot authenticate.

### `off`

Disables the user.

---

## **Password Rules**

Redis users can have multiple passwords at the same time.

### `>password`

Adds a new password that **can authenticate**.

Example:

wide760>myStrongPassword

### `<password`

Removes a password from the user.

wide760<myOldPassword

### `#<hash>`

Add this SHA-256 hash value to the list of valid passwords for the user. This hash value will be compared to the hash of a password entered for an ACL user. This allows users to store hashes in the `acl.conf` file rather than storing cleartext passwords. Only SHA-256 hash values are accepted as the password hash must be 64 characters and only contain lowercase hexadecimal characters.

### `!<hash>`

Remove this hash value from the list of valid passwords. This is useful when you do not know the password specified by the hash value but would like to remove the password from the user.

### `nopass`

Allows access **without password**.

⚠️ Extremely unsafe. Almost always disable

### `resetpass`

Removes ALL passwords and ALSO removes `nopass`.

Useful when rotating credentials.

---

## **Command Rules**

Command permissions control what a user may execute.

### **A. Add or remove individual commands**

#### Allow a single command:

wide760+get
+set

#### Deny a single command:

wide760-del

### **B. Command categories**

Redis groups commands into categories like:

| Category | Description |
| --- | --- |
| `@admin` | Config, shutdown, cluster mgmt |
| `@dangerous` | Keys deletion, FLUSHALL, expired debugging |
| `@read` | Read-only commands (GET, MGET, EXISTS) |
| `@write` | Write commands (SET, DEL, INCR) |
| `@keyspace` | Keyspace introspection |
| `@pubsub` | Publish/Subscribe |
| `@fast` | Fast O(1) operations |
| `@slow` | Slow operations (SCAN, SORT) |
| `@connection` | AUTH, PING |
| `@blocking` | BLPOP, BZPOPMIN |
| `@transaction` | MULTI, EXEC |
| `@scripting` | Lua eval |
| `@stream` | XREAD, XADD |
| `@set` | SET operations |
| `@hash`, `@list`, `@zset` | Data type commands |

### Example:

wide760+@read
-@write
+@transaction

### List all categories:

wide760ACL CAT

### List commands in a category:

wide760ACL CAT @write

## **Wildcard command permissions**

You can allow all commands:

wide760allcommands

Or remove all commands:

wide760nocommands

---

## **Key Access Patterns (**`~pattern`**)**

Key access rules determine what *keys* a user may read or write.

Rule syntax:

wide760~<glob-pattern>

Examples:

wide760~app1:\*
~cache:user:\*
~prefix?:value

### Restrict to specific DB index

wide760~db=0:\*
~db=1:user:\*

### Specify Read or Write Access for keys

wide760%R~<pattern> #Read only access
%W~<pattern> #Write only access
%RW~<pattern> #Read and Write access same as ~<pattern>

### Allow ALL keys (dangerous, but common)

wide760~\*
or
allkeys

### Remove all key patterns:

wide760resetkeys

---

## **Pub/Sub Channel Rules (**`&pattern`**)**

Pub/Sub channels have their **own ACL patterns**, separate from key patterns.

Examples:

wide760&orders:\*
&notifications

all channel access

wide760&\*
or
allchannels

Remove all channel patterns:

wide760resetchannels

---

## **Resetting a user**

A redis acl user can be reset with

wide760ACL SETUSER <username> reset

`reset` Performs the following actions: resetpass, resetkeys, resetchannels, allchannels (if acl-pubsub-default is set), off, clearselectors, -@all. The user returns to the same state it had immediately after its creation.

# Our Redis ACL User setup

wide760USER berth-monitor on >PASSWORD +@write +@read +@keyspace +INFO ~berth-monitor:\* resetchannels
USER stop-monitor on >PASSWORD +@write +@read +@keyspace +INFO ~stop-monitor:\* resetchannels
USER anchor-monitor on >PASSWORD +@write +@read +@keyspace +INFO ~anchor-monitor:\* resetchannels
USER portreporter-monitor on >PASSWORD +@write +@read +@keyspace +INFO ~portreporter-monitor:\* resetchannels
USER etapredictor on >PASSWORD +@write +@read +@keyspace +INFO ~etapredictor:\* resetchannels
USER encounter-monitor on >PASSWORD +@write +@read +@keyspace +INFO ~encounter-monitor:\* resetchannels
USER vesselvoyage on >PASSWORD +@read +@keyspace +INFO %R~etapredictor:\* resetchannels allchannels
USER developer on >PASSWORD +@all-@admin -ACL -CONFIG -SHUTDOWN -FLUSHALL -FLUSHDB allkeys 

| User | Read | Write | Keyspace Cmds | Key Access Pattern(s) | Notes |
| --- | --- | --- | --- | --- | --- |
| `berth-monitor` | ✅ | ✅ | ✅ | `berth-monitor:*` | Full RW access to own namespace |
| `stop-monitor` | ✅ | ✅ | ✅ | `stop-monitor:*` | Full RW access to own namespace |
| `anchor-monitor` | ✅ | ✅ | ✅ | `anchor-monitor:*` | Full RW access to own namespace |
| `portreporter-monitor` | ✅ | ✅ | ✅ | `portreporter-monitor:*` | Full RW access to own namespace |
| `etapredictor` | ✅ | ✅ | ✅ | `etapredictor:*` | Full RW access to own namespace |
| `encounter-monitor` | ✅ | ✅ | ✅ | `encounter-monitor:*` | Full RW access to own namespace |
| `vesselvoyage` | ✅ | ❌ | ✅ | **Read-only:** `etapredictor:*` | Can only read ETA predictor data |
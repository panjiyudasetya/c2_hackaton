---
id: jira:TCC-31
source: jira
type: issue
key: TCC-31
project: TCC
board: TCC board
issuetype: Bug
priority: Medium
assignee: Unassigned
labels: []
components: []
title: Make sure berths can be retrieved from Poma with a realistic speed
author: Richard van Klaveren
status: Done
date: '2025-03-03'
url: https://teqplaybv.atlassian.net/browse/TCC-31
explicit_links:
- jira:TCC-152
- jira:TCC-160
- jira:TCC-161
- jira:TCC-32
---
# [TCC-31] Make sure berths can be retrieved from Poma with a realistic speed

**URL:** https://teqplaybv.atlassian.net/browse/TCC-31  
**Type:** Bug | **Status:** Done | **Priority:** Medium  
**Reporter:** Richard van Klaveren | **Assignee:** Unassigned  
**Created:** 2025-03-03 | **Updated:** 2025-06-10  
**Board:** TCC board  
**Parent:** [TCC-152] Production Issues  

## Description

Currently, when all berths are being retrieved from Poma, the retrieval takes up-to 10 seconds, which should b way less. This is blocking other components like EventHistory and Api to update berths and provide relevant answers

## Subtasks

- [TCC-160] Make an assessment what we can do with the monitoring (To Do)
- [TCC-161] Potentially fix an issue on CoreComponents components (To Do)
- [TCC-32] Add monitoring to see what the network input/output is (Done)

## Comments

### Pim van den Toorn — 2025-03-05

Pod side getting berths takes about 1.1 second to send, consistently. The instance itself seems fine, but the up-/downloading is extremely slow.

I tested poma and csi, poma even directly to the pod through port-forwarding in 
Kubernetes: yesterday 4/3 around 1700 the speed was about 2.5-3.5 MB/s, now, around 9:40, the speed is about 2 MB/s.

### Pim van den Toorn — 2025-03-05

Requesting extra cpu doesn’t work

### Darius Wattimena — 2025-03-17

After looking with Pim we found the following:

* [https://repost.aws/questions/QUNu9j1U8YQ_-wyNj26drusQ/network-bandwidth-performance|https://repost.aws/questions/QUNu9j1U8YQ_-wyNj26drusQ/network-bandwidth-performance|smart-link]  Gives quite a detailed answer what “up to 10 Gbits“ actually means. So we get the expected speed it seems?
* We might want to check out {{r5n}}machines as they provide better network performance but same CPU/Memory.

### Pim van den Toorn — 2025-03-18

Darius' link refers to this aws page: [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html|https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html|smart-link] , and the r5 instance speeds: [https://aws.amazon.com/ec2/instance-types/r5/#:~:text=Product%20Details,-R5%20Instances|https://aws.amazon.com/ec2/instance-types/r5/#:~:text=Product%20Details,-R5%20Instances|smart-link] 

The image below describes the max speeds and the baseline speeds of different c5 instances in Gbps. The lowest baseline is 0.75 Gbps, which is 93.75 MBps, far from the 2-5 MBps for getting berths.

There are a few more factors, such as internet bound traffic being limited to 5Gbps. Also the faster loading times we sometimes see might be the burst speed.

I feel like we should be getting more

!image-20250318-085731.png|width=476,height=629,alt="image-20250318-085731.png"!

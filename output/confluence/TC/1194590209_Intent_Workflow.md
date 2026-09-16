---
id: confluence:1194590209
source: confluence
type: page
space: TC
title: Intent Workflow
author: Joost Dambrink
date: '2026-04-22'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1194590209
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1194590209
---
# Intent Workflow

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1194590209  

## Content

This page describes how our team develops features using an AI agent. The workflow covers every stage from writing the initial prompt to merging code with human review, automated quality gates, and full traceability through git at each step.

## Intent Process Format

In the workflow we see steps defined to store information about the process, such as the initial prompt, the generated spec, outcomes and feedback loops. We would like to store this information in a git repository specific for each feature so that we can learn from previous mistakes/wins. The following format should be filled-in for every Intent generated feature:

wide760# Intent: [Feature Name]
## Initial Card Description
```
[Card description here]
```
## Prompt
```
[Your prompt here]
```
## Spec Summary
```
[Your spec here]
```
## Feedback Log
\_Updated each time this intent loops back to Step 1.\_
| Iteration | Reason for loop-back | Changes made |
|-----------|----------------------|--------------|
| 1 | | |
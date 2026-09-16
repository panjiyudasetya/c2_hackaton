---
id: confluence:786530324
source: confluence
type: page
space: TC
title: AI Playbook
author: David Hansson
date: '2026-01-13'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/786530324
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/786530324
---
# AI Playbook

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/786530324  

## Content

## 🌟 Overview

Welcome to the **AI Playbook!**  
This space provides a curated collection of effective prompts, real-world examples, and practical guidelines to help you and your team craft better instructions for AI tools like **ChatGPT**, **GitHub Copilot**, **Augment**, and others.

---

## 📚 Helpful Prompting Resources

* 🔗**How to write better prompts for GitHub Copilot**  
  Official tips and techniques for crafting better GitHub Copilot prompts.  
   <https://github.blog/developer-skills/github/how-to-write-better-prompts-for-github-copilot/?utm_source=chatgpt.com>
* 🔗 **Anthropic Claude – Prompting Claude: Best practices**  
  Guidance directly from Claude’s creators on how to prompt effectively.
* 🔗 **GitHub Copilot – Best practices for using Copilot**  
  Official advice on contextual prompting and code suggestion strategies.  
   <https://docs.github.com/en/copilot/get-started/best-practices-for-using-github-copilot?utm_source=chatgpt.com>
* 🔗 **Augment - How to build your Agent**  
  11 prompting techniques for better AI agents.  
  <https://www.augmentcode.com/blog/how-to-build-your-agent-11-prompting-techniques-for-better-ai-agents>
* 🔗 **OpenAI (ChatGPT) - Best practices for prompt engineering with the OpenAI API**  
  How to give clear and effective instructions to OpenAI models  
  <https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api>

---

## 💡 Tips & Tricks

> **Share techniques that help get better results — e.g. phrasing, context, prompt templates, iteration strategies.**

| **Tip** | **Explanation / Example** | **Added By** |
| --- | --- | --- |
| **Ask the AI to ask you clarifying questions** | Encourage two-way interaction. For example: *“If any part of my request is unclear, ask me questions before starting.”* This helps prevent wrong assumptions and leads to more accurate, context-aware results. | JoostD |
| **Ask what implementations the AI can create before you start coding** | Before diving into code, ask: *“What are the possible implementation strategies for this feature?”* You can then compare its ideas with your own to choose the best approach — saving time and improving design quality. | JoostD |
| **In Augment, use the ‘Enhance Prompt’ functionality for better results** | Augment’s built-in **Enhance Prompt** feature automatically refines your prompt by adding clarity, structure, and intent. Use it before submitting your final request to get more focused, higher-quality outcomes. | JoostD |

---

## ⚠️ Suboptimal Uses of AI

Use this section to collect examples where prompts or workflows didn’t deliver the desired results. Focus on *what went wrong* and *what could be improved*.

| **Suboptimal Use** | **What Happened** | **Why It Didn’t Work** | **Added By / Date** |
| --- | --- | --- | --- |
| *(Add title here)* | *(Briefly describe the situation — what you asked the AI to do and what the outcome was.)* | *(Explain the issue — e.g. vague instructions, missing context, too much complexity, no iteration, etc.)* | *(Name & date)* |
|  |  |  |  |

---

## ✅ Optimal Uses of AI

Showcase use cases, strategies, or habits that consistently lead to good results. Highlight *why they worked* and what others can learn from them.

| **Optimal Use** | **What Worked Well** | **Why It Was Effective** | **Added By / Date** |
| --- | --- | --- | --- |
| In **Augment**, the rules defined in the `.augment/rules/` folder serve as guidelines for the Agent before it starts any implementation.  For example, we can define the **Single Responsibility Principle (SRP)** in a file like `.augment/rules/srp-rule.md` --- type: "always\_apply" --- ## Core Principles ### Functions and Methods - \*\*One clear purpose\*\*: Each function should do one thing and do it well - \*\*Single reason to change\*\*: If a function needs to change, it should be for only one reason - \*\*Descriptive naming\*\*: Function names should clearly indicate their single purpose - \*\*Small and focused\*\*: Keep functions short and focused on their specific task ### Breaking Down Complex Logic - \*\*Extract helper functions\*\*: When a function becomes complex, break it down into smaller, well-defined helper functions - \*\*Avoid multi-step operations\*\*: If a function performs multiple distinct steps, extract each step into its own helper function - \*\*Separate concerns\*\*: Keep data access, business logic, and presentation separate So, when we ask the Agent something like:  *“Create a service to process port data from the POMA API”*  it will automatically ensure that its implementation follows the SRP rule (and any other rules defined in `.augment/rules/`). | The Agent successfully followed one of the **SOLID design principles**, ensuring the implementation produces **high-quality and maintainable code**.  For example: def process\_port\_data(country\_code: str): """ Orchestrate port data processing. """ data = \_fetch\_from\_api(country\_code) validated\_data = \_validate\_data(data) ports = \_transform\_to\_models(validated\_data) \_save\_to\_database(ports) \_send\_notification() Each step in this function has a **single, well-defined responsibility**, resulting in clear, structured, and testable code. | This implementation is effective because it applies the **Single Responsibility Principle (SRP)**.  Ensuring each function focuses on a single task makes the code remain clean, modular, and maintainable, supporting easier testing and future scalability. | Panji |
| Generating Frontend Rules based on agreed Guidelines and integrating them into Augment: Front-end guides   **How to add?** Go to Augment > Settings > Rules & Guidelines Augment AI ruleset for FE guidelines | Consistency ensures behavior, and code patterns across teams and projects | Augment applies the rules, and formats everything correctly | David |

### 🤝 Collaboration Notes

This section outlines how to **collaborate effectively** when adding to or refining this page.

### 🧭 How to Contribute

* **Add your name and date** to every new entry in the tables.
* **Add optimal/suboptimal cases** as examples.
* **Use comments** to help others blocking issues and other discussions.
---
id: confluence:694157313
source: confluence
type: page
space: TC
title: Agentic AI tools market research
author: Nikola Saratlija (Unlicensed)
date: '2025-04-14'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/694157313
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/694157313
---
# Agentic AI tools market research

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/694157313  

## Content

The first step in employing agentic AI at Teqplay is to do a market research to find currently existing AI tools that could be useful.

The AI tools must meet the following criteria:

* **Must have internet access:** Previously, most AI tools were constrained to the information within their training data, meaning they could not give accurate answers to questions that require access to data created past their training period. Most chatbots right now are starting to implement internet access, which gives the LLM access to search engines and to read text on websites, providing current data for context.
* **No code, low code and custom coded:** Any of these paradigms are valid. From a simple chatbot interface, a drag-and-drop interface for building pipelines/workflows and code libraries made only for programmers.
* **Open source or subscription based:** The tool could be both free for use or locked behind a subscription, so long as the tool can perform a task faster and cheaper than a human.
* **Excluding computer-usage:** Some tools like Claude Computer Use give the AI almost full access to a client’s machine, allowing it to open programs, create/save files and execute commands. This usecase is not necessary.

# 1. AI Chatbots

Most people should already be familiar with AI Chatbots like ChatGPT, Claude, Gemini or Perplexity. Recently most AI chatbots have been given internet access which the AI can use to retrieve current information if the query requires data made past their training period, for example articles. Chatbots do this by querying search engines and then opening the top results - inspecting the website’s code structure (DOM) - which they can use for information to answer the prompt. Sometimes even providing the source of the information which the answer is based on which is useful for fact checking.

A simple benchmark was done by asking the chatbot two questions: What is the current ship lineup of the Port of Rotterdam / Port of Paranagua. The chatbot proceded to query Google to look for ship tracking websites like Vesselfinder and then entering the website to fetch the number of vessels and some specific vessels that were currently in port. Technically the AI chatbot answered correctly by accurately returning the data on the website. However the scope of the AI chatbot is limited by what links it finds in the top Google results, meaning the AI can sometimes miss critical data.

AI chatbots can be considered somewhat agentic on the surface but in reality do not display the ability to plan, take initiative, or correct mistakes meaning that even AI chatbots with internet access are not really agentic. On top of that AI chatbots with internet access are limited to accessing static websites that do not have a simple UI. Meaning AI chatbots cannot complete complex tasks like booking a reservation or ordering something online because they do not possess the capability to navigate UI.

# 2. Browser-use Framework

The browser-use framework ([Browser Use](https://browser-use.com/)) allows AI to navigate an internet browser to solve tasks. It does this using both vision capabilities and by scanning the DOM. It has the ability to open tabs and navigate through websites like a human would. It can therefore be seen as a more advanced version of an AI chatbot with internet access because it can navigate through dynamic web content and complex UI. This allows AI to write Google Docs, apply for jobs, book a flight and collect data. This represents a solid step towards agency and autonomy because it is able to solve complex tasks on the internet. However it still lacks concrete planning abilities and error correction.

The Browser-Use framework is open-source and free to use. It is installed as a Python library and requires an LLM API-key. The AI can then be prompted by passing an instruction as a string in the code. It makes use of Playwright to handle the browser context. Browser-use can be configured to use either a fresh browser instance or your own browser, allowing it to access pages that require authentication. This needs to be used with caution of course.

# 3. Manus AI

Manus AI is one of the most solid developments in general purpose, agentic and autonomous AI. It is an AI chatbot that has the ability to solve a wide range of tasks with minimal human intervention, like booking, generating reports and creating software. It is built on top of the browser-use framework allowing Manus to access the internet and perform complex tasks but is even more advanced. What sets it apart is that based on a high-level instruction like “build me a portfolio website“ it will attempt to finish the task end-to-end, handling the planning itself. When given a prompt it will split the task into multiple sub-tasks, like a plan-of-attack. It will proceed to handle each task one-by-one, cross off todos as they get completed. Manus monitors its own outputs and can retry tasks if failed or not meeting expectations. Manus aims to make its decision making and problem solving transparent by printing the actions it does and, if an action requires web access, it shows real-time use of the browser in a side-panel.

Unfortunately Manus AI can be quite slow, especially with tasks requiring internet usage, making it not very scalable. In an experiment Manus AI was tasked to (1) lookup the ship lineup of the Port of Rotterdam an (2) find a 1 bedroom apartment in Rotterdam. Both tasks took about 5 minutes to complete, consuming about 200 credits, approximately 2$. Most of the consumed time and credits were spent on performing operations on the web, like navigation. So if the prompts were to be extended to include multiple sources (for example “lookup the ship lineup of the Port of Rotterdam, Paranagua, Shenzhen and Fujairah“) then Manus would have to search multiple websites which would take a long time

# 4. AI Agent Pipeline Frameworks (AutoGen, Langchain, etc)

An AI agent pipeline is a system where one or more AI agents, powered by LLMs like GPT, work through a series of tasks, possibly using tools, knowledge or even taking to each other to achieve a goal. For example if you have a startup idea you could have (1) a research agent gathering market trends on the internet, (2) a business strategist drafting a plan (3) a coder agent building a prototype and (4) a tester agent reviewing the output. Different tools exist for creating AI agent pipelines, for example AutoGen and Langchain. These kinds of tools differ from the previous examples in that you need to setup the pipeline yourself using Python: (1) what agents exist (2) what roles or tasks they perform (3) how they talk to each other and (4) what tools they use, like an API. This means that this tool will not perform well on general tasks but a pipeline needs to be built and tailored to specific kinds of tasks. A benefit of this is that in theory the result from an AI agent pipeline could be better compared to that of a general AI assistant because the pipeline has been tailored towards a specific kind of task by a human, possibly suiting the domain more.

Many different tools exist for creating AI agent pipelines, like the previously named AutoGen (by Microsoft) and Langchain. But these are lower-level frameworks designed for custom, flexible pipelines. Agents can be configured to use Python functions for file-access, API usage and internet usage. RAG can also be setup. These two tools mainly differ in their style of writing pipelines, but generally do the same thing. Higher-level wrappers of AutoGen/Langchain exist allowing for easier creation of AI agent pipelines, like <https://www.crewai.com/>, <https://agpt.co/> and <https://www.langchain.com/langgraph>.
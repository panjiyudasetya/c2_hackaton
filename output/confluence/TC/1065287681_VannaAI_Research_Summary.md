---
id: confluence:1065287681
source: confluence
type: page
space: TC
title: VannaAI Research Summary
author: Ryan Kharisma Rakhmat
date: '2026-01-12'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1065287681
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1065287681
---
# VannaAI Research Summary

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1065287681  

## Content

# Vanna AI - Maritime Data Analytics Platform

## Documentation Guide

---

## 1. Background

### What is Vanna AI?

Vanna AI is an intelligent **Text-to-SQL** platform that enables users to query databases using natural language. Instead of writing complex SQL queries manually, users can simply ask questions in plain English like *"Show me the top 10 ports by vessel traffic"* and Vanna automatically generates and executes the appropriate SQL query.

### Why We Built This

Traditional data analysis requires:

* SQL expertise to write queries
* Deep understanding of database schemas
* Time-consuming query optimization

**Vanna AI solves these problems by:**

* Allowing non-technical users to access data insights
* Reducing time from question to answer from hours to seconds
* Eliminating SQL syntax errors through AI-powered generation
* Providing immediate visualizations of query results

### Our Implementation

This implementation is specifically designed for **Maritime/Shipping Industry** data analytics, featuring:

| Component | Description |
| --- | --- |
| **Maritime Domain Knowledge** | Pre-trained understanding of ships, ports, voyages, and maritime operations |
| **Multi-LLM Support** | Switch between Google Gemini (cloud) and Ollama (local) LLM support. |
| **PostgreSQL Integration** | Connected to Data Mart with dimension and fact tables |
| **Export Capabilities** | Export results to Excel and charts to images |
| **Web Interface** | Built-in chat UI for interactive querying |

### Technology Stack

wide760┌─────────────────────────────────────────────────────────┐
│ Frontend │
│ Vanna Built-in Web UI (React-based Chat Interface) │
├─────────────────────────────────────────────────────────┤
│ Backend │
│ FastAPI + Vanna Agent + Tool Registry │
├─────────────────────────────────────────────────────────┤
│ AI/ML Layer │
│ Google Gemini / Anthropic Claude LLM Services │
├─────────────────────────────────────────────────────────┤
│ Data Layer │
│ PostgreSQL (Data Warehouse + Data Mart) │
└─────────────────────────────────────────────────────────┘

---

## 2. How to Setup

### Prerequisites

Before starting, ensure you have:

* **Python 3.8+** installed
* **PostgreSQL** database server running (we can use our RDS data warehouse and mart)
* **API Key** for either:

  + Google Gemini API (from [Google AI Studio](https://makersuite.google.com/app/apikey))
  + Anthropic Claude API (from [Anthropic Console](https://console.anthropic.com/))

* **Ollama** local LLLM running (we can use another model e.g Qwen3 or Mistral7 that support `tool`)

### Step-by-Step Installation

#### Step 1: Navigate to Project Directory

bashwide760cd vanna\_ai

#### Step 2: Create Virtual Environment

bashwide760# Create virtual environment
python -m venv venv
# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

#### Step 3: Install Dependencies

bashwide760pip install -r requirements.txt

#### Step 4: Configure Environment Variables

bashwide760# Copy the example environment file
cp .env.example .env
# Edit the .env file with your credentials
nano .env # or use your preferred editor

#### Step 5: Environment Configuration

Edit your `.env` file with the following settings:

envwide760# ===========================================
# LLM Provider Configuration
# ===========================================
# Options: "gemini" or "anthropic"
LLM\_PROVIDER=gemini
# Google Gemini Configuration
GEMINI\_API\_KEY=your\_gemini\_api\_key\_here
GEMINI\_MODEL=gemini-2.5-flash
# Anthropic Claude Configuration (if using Claude)
ANTHROPIC\_API\_KEY=your\_anthropic\_api\_key\_here
ANTHROPIC\_MODEL=claude-sonnet-4-20250514
# ===========================================
# Database Configuration
# ===========================================
# Data Warehouse (source data)
DWH\_HOST=localhost
DWH\_PORT=5432
DWH\_DATABASE=datawarehouse
DWH\_USERNAME=postgres
DWH\_PASSWORD=your\_password
# Data Mart (analytics layer)
MART\_HOST=localhost
MART\_PORT=5432
MART\_DATABASE=datamart
MART\_USERNAME=postgres
MART\_PASSWORD=your\_password
# ===========================================
# Server Configuration
# ===========================================
API\_HOST=0.0.0.0
API\_PORT=8000
API\_DEBUG=False
# ===========================================
# Export Configuration
# ===========================================
EXPORT\_DIR=exports
MAX\_EXPORT\_ROWS=100000
CHART\_WIDTH=1200
CHART\_HEIGHT=600

#### Step 6: Verify Database Connection

Ensure your PostgreSQL databases are accessible:

bashwide760# Test connection to Data Mart
psql -h localhost -p 5432 -U postgres -d datamart -c "SELECT 1;"

---

## 3. How to Run

### Starting the Application

bashwide760# Make sure you're in the vanna\_ai directory
cd vanna\_ai
# Activate virtual environment (if not already active)
source venv/bin/activate
# Start the server
python3 app.py

### Expected Output

wide7602024-01-15 10:30:00 - \_\_main\_\_ - INFO - Initializing Vanna AI Application
2024-01-15 10:30:00 - \_\_main\_\_ - INFO - Using Google Gemini model: gemini-2.5-flash
2024-01-15 10:30:01 - \_\_main\_\_ - INFO - Export directory: exports
2024-01-15 10:30:01 - \_\_main\_\_ - INFO - Maritime domain knowledge loaded
2024-01-15 10:30:01 - \_\_main\_\_ - INFO - All tools registered successfully
2024-01-15 10:30:01 - \_\_main\_\_ - INFO - Maritime system prompt configured
2024-01-15 10:30:01 - \_\_main\_\_ - INFO - Starting Vanna AI Server on 0.0.0.0:8000
Your app is running at:
http://localhost:8000

### Accessing the Application

Open your web browser and navigate to:

wide760http://localhost:8000

---

## 4. How to Use

### Web Interface Overview

The Vanna AI web interface provides an intuitive chat-based experience:

wide760┌─────────────────────────────────────────────────────────────┐
│ 🚢 Vanna AI - Maritime Analytics │
├─────────────────────────────────────────────────────────────┤
│ │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ Chat History │ │
│ │ │ │
│ │ 👤 User: Show me top 5 ports by vessel visits │ │
│ │ │ │
│ │ 🤖 Vanna: Here's the SQL I generated: │ │
│ │ SELECT p.name, COUNT(\*) as visits │ │
│ │ FROM fact\_port\_visit pv │ │
│ │ JOIN dim\_port p ON pv.port\_unlocode = p.unlocode │ │
│ │ GROUP BY p.name ORDER BY visits DESC LIMIT 5; │ │
│ │ │ │
│ │ [📊 Bar Chart] [📋 Data Table] │ │
│ │ │ │
│ └─────────────────────────────────────────────────────┘ │
│ │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ 💬 Type your question here... [→] │ │
│ └─────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘

### Asking Questions

Simply type your question in natural language. The AI understands maritime context automatically.

#### Example Maritime Questions

| Question | What It Does |
| --- | --- |
| "How many ships visited Singapore last month?" | Counts port visits filtered by port and date |
| "Show me container ships with TEU > 10000" | Filters dim\_ship by ship type and capacity |
| "What's the average turnaround time by port?" | Calculates aggregated metrics from fact tables |
| "List all tankers currently at berth" | Joins ship and berth data with status filter |
| "Compare vessel traffic between Rotterdam and Hamburg" | Multi-port comparison with grouping |

#### Question Tips

1. **Be Specific**: "Show top 10 ports" is better than "show ports"
2. **Include Time Ranges**: "in the last 3 months" helps narrow results
3. **Mention Metrics**: "by count", "average", "total" guides aggregation
4. **Use Maritime Terms**: The AI understands IMO, MMSI, TEU, DWT, etc.

### Understanding Results

After asking a question, Vanna provides:

#### 1. Generated SQL Query

sqlwide760SELECT p.name, COUNT(\*) as visit\_count
FROM fact\_port\_visit pv
JOIN dim\_port p ON pv.port\_unlocode = p.unlocode
WHERE pv.arrival\_timestamp >= '2024-01-01'
GROUP BY p.name
ORDER BY visit\_count DESC
LIMIT 10;

#### 2. Data Table

| Port Name | Visit Count |
| --- | --- |
| Singapore | 1,250 |
| Rotterdam | 980 |
| Hamburg | 875 |

#### 3. Visualization

Automatic chart generation based on data type:

* **Bar Chart**: For categorical comparisons
* **Line Chart**: For time series data
* **Pie Chart**: For proportional data
* **Scatter Plot**: For correlations

### Exporting Results

#### Export to Excel

Ask: *"Export this to Excel"* or *"Download as spreadsheet"*

The system will:

1. Generate an `.xlsx` file with formatted columns
2. Save to the `exports/` directory
3. Provide download link

#### Export Charts

Ask: *"Save this chart as image"* or *"Export chart to PNG"*

## 5. Benefits

### For Business Users

| Benefit | Description |
| --- | --- |
| **No SQL Required** | Ask questions in plain English |
| **Instant Insights** | Get answers in seconds, not hours |
| **Self-Service Analytics** | No need to wait for IT or analysts |
| **Visual Results** | Automatic charts make data understandable |
| **Export Ready** | Download results for presentations |

### For Data Teams

| Benefit | Description |
| --- | --- |
| **Reduced Workload** | Fewer ad-hoc query requests |
| **Consistent Queries** | AI generates optimized SQL |
| **Domain Knowledge** | Maritime context is built-in |
| **Audit Trail** | Query history for compliance |
| **Scalable** | Serves multiple users simultaneously |

### For Organizations

| Benefit | Description |
| --- | --- |
| **Faster Decisions** | Data-driven insights on demand |
| **Democratized Data** | Everyone can access analytics |
| **Cost Effective** | Reduces dependency on specialized skills |
| **Flexible LLM Choice** | Switch between Gemini and Claude |
| **Extensible** | Add custom tools and domains |

### Technical Benefits

wide760┌────────────────────────────────────────────────────────────┐
│ Technical Advantages │
├────────────────────────────────────────────────────────────┤
│ │
│ ✅ Modular Architecture │
│ Clean separation of concerns (config, services, tools) │
│ │
│ ✅ Multi-LLM Support │
│ Easy switching between AI providers │
│ │
│ ✅ Domain-Driven Design │
│ Maritime knowledge embedded in system prompts │
│ │
│ ✅ Type-Safe Configuration │
│ Pydantic settings with validation │
│ │
│ ✅ Extensible Tool System │
│ Add custom tools without modifying core code │
│ │
│ ✅ Production Ready │
│ Docker support, logging, error handling │
│ │
└────────────────────────────────────────────────────────────┘

### ROI Comparison

| Metric | Traditional Approach | With Vanna AI |
| --- | --- | --- |
| Time to Answer | 30 min - 2 hours | 5 - 30 seconds |
| SQL Expertise Required | High | None |
| Training Time | Weeks | Minutes |
| Query Errors | Frequent | Minimal |
| Visualization | Separate tool | Built-in |

---

## Quick Reference

### Common Commands

bashwide760# Start server
python3 app.py

### Troubleshooting

| Issue | Solution |
| --- | --- |
| Connection refused | Check if PostgreSQL is running |
| API key error | Verify key in `.env` file |
| No results | Check database has data |
| Slow response | Consider using faster LLM model |

**Benchmarking**

|  |  |  |  |
| --- | --- | --- | --- |
| Models | Location | Question | Time Spent |
| gemini-2.5-flash | Cloud | Show me 5 most busiest port in Europe | Around 2 minutes |
| qwen3:4b | Local | Show me 10 of the most busiest port in US | Around 10 minutes |
| Mistral 7B | Local | Show me top 3 busiest port in the world | Around 3 minutes but the answer is not expected, only show the query |

Another benchmarks question

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Models | Location | Question | Time Spent | Follow up Question | Response |
| gemini-2.5-flash | Cloud | How many ships visited Singapore last month? | Around 1 minutes, but only returning the query and answers is: A total of 102 unique ships visited Singapore last month.  At first iteration not shows the bar chart. | can you find it on our database | Yes, I have already found this information in our database. A total of 102 unique ships visited Singapore last month. With the query and also bar chart is showing to the users. (In approximately one minutes time) |
| qwen3:4b | Local | How many ships visited Rotterdam last month? | Around 4 minutes. But wrong query result: SELECT COUNT(\*) FROM ship\_visits WHERE visit\_date >= DATE\_SUB(CURRENT\_DATE(), INTERVAL 1 MONTH) AND port = 'Rotterdam'; |  |  |
| Mistral 7B | Local | How many ships visited Corpus Christi last month? | Around 2 minutes. But wrong query results :SELECT COUNT(\*) FROM ships WHERE visit\_date >= DATEADD(month, -1, GETDATE()); |  |  |

**screenshots**:

**Architecture Diagram**
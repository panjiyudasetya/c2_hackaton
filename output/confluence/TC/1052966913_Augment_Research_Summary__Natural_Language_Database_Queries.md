---
id: confluence:1052966913
source: confluence
type: page
space: TC
title: 'Augment Research Summary: Natural Language Database Queries'
author: Panji Y. Wiwaha
date: '2025-12-23'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1052966913
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1052966913
---
# Augment Research Summary: Natural Language Database Queries

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1052966913  

## Content

## Background & Problem Statement

### Problem Context

This research explored the use of Augment with Claude Sonnet 4.5 as an alternative approach to natural language database queries, complementing the existing LangChain implementation.

### Limitations with LangChain Implementation

While the LangChain implementation (`langchain_ai/`) was functional and production-ready, several constraints motivated exploring alternatives:

1. **Token Limitations**: LangChain experimentation was constrained by the free-tier token limitations on the Anthropic API, which limited the ability to test and iterate on complex queries extensively.
2. **Complexity Overhead**: The LangChain implementation required:

   * 10+ package dependencies (LangChain, SQLAlchemy, langchain-anthropic, langchain-community, etc.)
   * ~200+ MB installation size
   * Framework-specific concepts and abstractions
   * Approximately 15 minutes of setup time
3. **Different SQL Transparency Approach**: Initially, LangChain didn't show SQL queries by default, but this was later resolved:

   * **Initial state**: SQL queries were hidden, making debugging and auditing difficult
   * **Current state**: SQL transparency now implemented via prompt-based enforcement
   * **Difference**: LangChain uses system prompt instructions vs Augment's rules file approach
   * **Result**: Both implementations now provide equivalent SQL transparency

### Research Motivation

The key gaps that motivated exploring Augment were:

* Need for a simpler, more lightweight alternative with fewer dependencies
* Opportunity to reduce setup complexity and learning curve
* Interest in faster setup and configuration
* Exploration of rules-based enforcement vs prompt-based enforcement for SQL transparency

## Project Goals

### Primary Objectives

1. **Simplicity**: Create a minimal implementation with fewer dependencies and faster setup
2. **Transparency**: Make SQL queries visible by default with context and purpose
3. **User Experience**: Provide professional, clean terminal output with markdown rendering
4. **Ease of Configuration**: Simple setup process with minimal steps
5. **Flexibility**: Enable easy customization without complex configuration

### Specific Capabilities to Achieve

* Natural language to SQL query generation
* Database schema understanding
* Safe query execution (read-only access)
* Interactive CLI with multiple modes (ask, chat, tables, schema)
* Streaming responses
* Rich terminal formatting with markdown support

### Success Criteria

* Setup time under 5 minutes
* Fewer than 6 package dependencies
* Installation size under 100 MB
* SQL queries displayed with context by default
* Clean, professional terminal output
* Comparable or better query accuracy to LangChain
* Easy configuration without complex setup

## Research Outcomes

### **Successfully Implemented Features**

#### **User-Facing Capabilities**

1. **Natural Language Query Processing**

   * Ask questions in plain English about database data
   * Automatic understanding of database structure
   * Claude Sonnet 4.5 generates appropriate SQL queries
   * Results returned in natural language with context
2. **Interactive CLI Modes**

   * **ask**: Single question mode for quick queries
   * **chat**: Interactive conversation mode for multiple questions
   * **tables**: List all available database tables
   * **schema**: View structure of specific tables with sample data
   * **test**: Verify database and API connections
   * **config**: Display current configuration settings
3. **SQL Query Transparency**

   * **Always Visible**: SQL queries displayed by default in every response
   * **Context Provided**: Each query shows its purpose and reasoning
   * **Educational**: Users can learn SQL patterns from the AI
   * **Auditable**: Clear trail of all database access
   * **Example Format**:

     Purpose: Finding top 5 ports by visit count
     SELECT port\_name, COUNT(\*) as visits
     FROM port\_visits
     GROUP BY port\_name
     ORDER BY visits DESC
     LIMIT 5;
4. **Professional Terminal Output**

   * Clean, formatted markdown rendering
   * Color-coded headers and sections
   * Inline formatting (bold, italic, code blocks)
   * Compact display without excessive whitespace
   * Loading spinners during query processing
5. **Configuration System**

   * YAML-based configuration files for easy editing
   * Environment-specific settings (dev, prod)
   * Simple `.env` file for API credentials
   * Database connection settings

#### **Setup and Configuration Experience**

**Installation Process:**

* Install dependencies: `pip install -r requirements.txt` (5 packages, ~50 MB)
* Configure environment: Copy `.env.example` to `.env` and add API key
* Estimated setup time: ~5 minutes

**Configuration Files:**

* `config/config.yaml`: Base configuration settings
* `config/config.dev.yaml`: Development environment overrides
* `config/config.prod.yaml`: Production environment overrides
* `.env`: API credentials and sensitive settings
* `config/auggie_rules.md`: AI behavior rules (SQL transparency, output format)

**What Can Be Configured:**

* Database connection (host, port, database, schema)
* Claude model settings (model name, temperature, max tokens)
* CLI appearance (colors, formatting)
* Logging levels and output locations
* AI behavior rules (SQL display, response format)

### **Demonstrated Capabilities**

**Example Query Flow:**

bashwide760$ python augment\_ai/nlq.py ask "How many tables are in the database?"
✅ Answer:
SQL Queries Executed
Purpose: Getting database schema information to count tables
```sql
SELECT t.table\_name, c.column\_name, c.data\_type, c.is\_nullable
FROM information\_schema.tables t
JOIN information\_schema.columns c ON t.table\_name = c.table\_name
WHERE t.table\_schema = 'public' AND t.table\_type = 'BASE TABLE'
ORDER BY t.table\_name, c.ordinal\_position;
```
Answer
The database contains 18 tables in total...

**Key Features Demonstrated:**

* Natural language understanding
* Automatic schema inspection
* SQL query generation
* Query transparency with context
* Clean markdown formatting
* Professional terminal output

## Advantages of Using Augment for Database Analytics

### 1. Simplicity and Speed

* **Setup Time**: ~5 minutes vs ~15 minutes for LangChain
* **Dependencies**: 5 packages vs 10+ packages
* **Installation Size**: ~50 MB vs ~200+ MB
* **Quick Start**: Minimal configuration needed to get started

### 2. SQL Query Transparency (Rules-Based Enforcement)

* **Always Visible**: SQL queries are displayed by default with context in every response
* **Rules-Based Approach**: Uses `config/auggie_rules.md` file to enforce SQL documentation format
* **Purpose Explained**: Each query shows why it's being run
* **Easy Debugging**: See exactly what queries the AI generates
* **Auditable**: Clear trail of all database access for compliance
* **User Trust**: End users can verify the data source and query logic
* **Educational**: Users learn SQL patterns from the AI's examples

### 3. User Experience

* **Rich Markdown Rendering**: Professional terminal output with colors and formatting
* **Clean Output**: Compact display without excessive whitespace
* **Inline Formatting**: Support for bold, italic, and code blocks
* **Visual Hierarchy**: Color-coded headers for easy reading
* **Streaming Support**: See responses as they're generated (when using `--stream` flag)

### 4. Configuration Flexibility

* **Simple YAML Files**: Easy to understand and modify configuration
* **Environment Support**: Separate settings for dev, prod, and test
* **Layered Settings**: Base config + environment overrides + env vars
* **AI Behavior Rules**: Configure how the AI responds via a markdown rules file
* **Simple Credentials**: API key stored in `.env` file

### 5. Cost Efficiency

* **Smaller Installation**: ~50 MB vs ~200+ MB saves disk space
* **Faster Setup**: Less time spent on installation and configuration
* **Efficient Responses**: A Simpler execution path may use fewer tokens

## Disadvantages of Using Augment for Database Analytics

### 1. Technical Implementation Limitations

**Current Implementation Uses CLI Workaround:**  
The implementation currently uses a CLI subprocess approach rather than the native Python SDK due to technical issues with the SDK (version 0.1.4).

**Impact on User Experience:**

* **No Streaming in Ask Mode**: Responses appear all at once, not word-by-word
* **Slightly Slower**: Additional overhead from subprocess management
* **Timeout Configuration**: Queries have a maximum time limit (180 seconds)

**Note:** These limitations may be temporary if SDK issues are resolved in future versions.

### 2. Limited Ecosystem

* **Newer Framework**: Less mature than LangChain
* **Smaller Community**: Growing but not as large as LangChain
* **Fewer Examples**: Less documentation and community resources
* **Limited Integrations**: Not as many pre-built integrations

### 3. Missing Advanced Features

* **No Connection Pooling**: May impact performance in high-traffic scenarios
* **Basic Query Validation**: Less sophisticated than LangChain's validation
* **No Query Caching**: LangChain offers SQL query caching and optimization
* **Limited Safety Features**: Basic SELECT-only validation

### 4. Production Considerations

* **Less Battle-Tested**: Newer framework with less production usage
* **Fewer Monitoring Tools**: Fewer built-in observability features
* **Scalability Unknowns**: Performance at scale not extensively tested
* **Framework Evolution**: API may change as the framework matures

### 5. Documentation Gaps

* **Good but Not Extensive**: Documentation is good but not as comprehensive as LangChain
* **Fewer Tutorials**: Less community-contributed content
* **Limited Examples**: Fewer real-world implementation examples
* **Smaller Community**: Fewer people to ask for help

## Conclusion

The Augment research successfully demonstrated a simpler alternative to LangChain for natural language database queries. The implementation achieved all primary goals: reduced complexity (5 packages vs 10+), rules-based SQL transparency enforcement, improved user experience with rich markdown rendering, and faster setup (~5 minutes vs ~15 minutes).

**Note on SQL Transparency:** While Augment pioneered the SQL transparency approach in this project using rules-based enforcement, the LangChain implementation later adopted a similar feature using prompt-based enforcement. Both approaches now provide equivalent transparency and auditability, with the main difference being the enforcement mechanism (rules file vs system prompt).

However, the research also revealed some challenges, particularly the current reliance on a CLI subprocess approach (due to SDK technical issues) and the framework's relative immaturity compared to LangChain's established ecosystem.

## Source code

<https://github.com/teqplay/dataflow_ai/tree/develop/augment_ai>
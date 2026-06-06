# CrewAI Multi-Agent Business Research Assistant

## Overview

This project implements a multi-agent AI system using CrewAI that performs business research, analysis, strategic recommendation generation, and quality review.

The solution demonstrates:

* Multi-agent orchestration
* Custom tool integration
* Search fallback handling
* Observability and tracing with Langfuse
* CrewAI execution tracing
* MCP awareness and future extensibility

---

# Architecture

```text
User Topic
    |
    v
Research Specialist
    |
    +--> Search Tool
            |
            +--> Serper
            |
            +--> Tavily (Fallback)
            |
            +--> Graceful Fallback Message
    |
    v
Business Analyst
    |
    +--> File Reader Tool
    |
    v
Strategy Consultant
    |
    +--> Trend Score Tool
    |
    v
Quality Reviewer
    |
    v
Final Executive Report
```

---

# Features

## Multi-Agent Workflow

The system consists of four specialized agents:

### 1. Research Specialist

Responsibilities:

* Market research
* Industry analysis
* Trend identification
* Risk identification

Tool Used:

* Search Tool

---

### 2. Business Analyst

Responsibilities:

* Analyze research findings
* Identify opportunities
* Assess competitive landscape
* Evaluate risks

Tool Used:

* File Reader Tool

---

### 3. Strategy Consultant

Responsibilities:

* Generate recommendations
* Evaluate business relevance
* Assess strategic value

Tool Used:

* Trend Score Tool

---

### 4. Quality Reviewer

Responsibilities:

* Improve clarity
* Improve structure
* Ensure executive readability
* Produce final report

---

# Custom Tools

## Search Tool

File:

```text
tools/search_tool.py
```

Purpose:

* Search the web for current information

Primary Provider:

* Google Serper

Fallback Provider:

* Tavily

Final Fallback:

* Graceful user-facing message

Example:

```text
Serper
    ↓
Tavily
    ↓
Fallback Message
```

---

## File Reader Tool

File:

```text
tools/file_reader_tool.py
```

Purpose:

* Read local files
* Provide contextual information
* Support business analysis

---

## Trend Score Tool

File:

```text
tools/trend_score_tool.py
```

Purpose:

* Generate trend relevance score
* Support strategic recommendations

Example Output:

```text
Topic: Agentic Commerce
Trend Score: 58/100
```

---

# Fallback Strategy

The project implements resilient error handling.

## Search Fallback Flow

```text
User Search
     |
     v
Serper Search
     |
     +--> Success
     |
     +--> Failure
              |
              v
         Tavily Search
              |
              +--> Success
              |
              +--> Failure
                       |
                       v
               Fallback Handler
```

Benefits:

* Increased reliability
* Reduced downtime
* Better user experience

---

# Observability

## Langfuse Integration

The project integrates Langfuse for observability.

Capabilities:

* Trace creation
* Observation logging
* Execution monitoring
* Authentication verification

Configuration:

```env
LANGFUSE_PUBLIC_KEY=
LANGFUSE_SECRET_KEY=
LANGFUSE_HOST=https://cloud.langfuse.com
```

Verification:

```python
langfuse.auth_check()
```

Expected Result:

```text
True
```

---

## CrewAI Tracing

CrewAI tracing is enabled.

Configuration:

```env
CREWAI_TRACING_ENABLED=true
```

Benefits:

* Agent execution tracking
* Task execution tracking
* Tool execution tracking
* Workflow visualization

Example Output:

```text
Trace batch finalized
Crew Execution Completed
```

---

# MCP Awareness

## Current Architecture

The project currently integrates directly with external APIs:

```text
CrewAI Agents
    |
    +--> OpenAI
    +--> Tavily
    +--> Serper
```

---

## Future MCP Architecture

In a production implementation, tools could be exposed through MCP servers.

Example:

```text
CrewAI Agents
      |
      v
   MCP Client
      |
      +--> Search MCP Server
      +--> Research MCP Server
      +--> Trend Analysis MCP Server
      +--> Document Retrieval MCP Server
```

Benefits:

* Standardized tool access
* Dynamic tool discovery
* Improved scalability
* Vendor independence

---

# Installation

## Clone Repository

```bash
git clone https://github.com/shahzadbasir1/crewai_project.git
cd crewai_project
```

## Create Virtual Environment

```bash
py -3.11 -m venv venv
```

Activate:

```powershell
.\venv\Scripts\Activate.ps1
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create:

```text
.env
```

Example:

```env
OPENAI_API_KEY=

SERPER_API_KEY=

TAVILY_API_KEY=

LANGFUSE_PUBLIC_KEY=

LANGFUSE_SECRET_KEY=

LANGFUSE_HOST=https://cloud.langfuse.com

CREWAI_TRACING_ENABLED=true
```

---

# Running the Project

Execute:

```bash
python app.py
```

Example Input:

```text
Agentic Commerce
```

Example Output:

```text
Research Report
Business Analysis
Strategic Recommendations
Final Reviewed Report
```

---

# Project Structure

```text
crewai_project/

├── agents.py
├── tasks.py
├── crew.py
├── app.py

├── tools/
│   ├── search_tool.py
│   ├── file_reader_tool.py
│   └── trend_score_tool.py

├── fallback/
│   └── fallback_handler.py

├── monitoring/
│   ├── langfuse_config.py
│   └── trace_helper.py

├── tests/

├── requirements.txt
├── .env.example
└── README.md
```

---

# Technologies Used

* Python 3.11
* CrewAI
* OpenAI GPT-4o-mini
* Tavily Search
* Google Serper
* Langfuse
* ChromaDB
* Requests
* Pydantic

---

# Sample Workflow

```text
User enters topic
        |
        v
Research Specialist
        |
        v
Search Tool
        |
        v
Business Analyst
        |
        v
File Reader Tool
        |
        v
Strategy Consultant
        |
        v
Trend Score Tool
        |
        v
Quality Reviewer
        |
        v
Final Executive Report
```

---

# Assignment Requirements Coverage

| Requirement            | Status   |
| ---------------------- | -------- |
| Multi-Agent System     | Complete |
| Sequential Workflow    | Complete |
| Custom Tools           | Complete |
| Search Integration     | Complete |
| Fallback Handling      | Complete |
| Langfuse Observability | Complete |
| CrewAI Tracing         | Complete |
| MCP Awareness          | Complete |
| Documentation          | Complete |

---

# Author

Shahzad Basir

Multi-Agent Business Research Assistant built using CrewAI, OpenAI, Tavily, Langfuse, and custom tool integrations.

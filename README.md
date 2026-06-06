# AI Log Summarizer

AI-powered log analysis tool that leverages OpenAI Large Language Models to summarize application logs, identify critical failures, and accelerate root-cause analysis.

## Overview

Troubleshooting large application logs is often time-consuming and error-prone.

AI Log Summarizer automates log analysis by extracting relevant events from telemetry logs and generating concise AI-powered summaries that help engineers quickly understand failures and identify probable root causes.

The project demonstrates practical applications of LLMs in software quality engineering, observability, and incident investigation.

---

## Features

- Analyze application and telemetry logs
- AI-powered log summarization
- Failure pattern identification
- Root-cause analysis assistance
- Prompt-driven log intelligence
- Modular architecture for future extensions

---

## Tech Stack

### Programming Language
- Python

### AI / LLM
- OpenAI API

### Libraries
- OpenAI SDK
- Pydantic
- Python Dotenv
- HTTPX
- tqdm

### Development Tools
- Git
- GitHub

---

## Project Structure

```text
ai-log-summarizer/
│
├── app/
│   ├── llm.py
│   ├── main.py
│   ├── prompts.py
│   └── utils.py
│
├── logs/
│   └── telemetry.txt
│
├── requirements.txt
└── README.md
```

---

## Workflow

```text
Telemetry Log
      │
      ▼
Log Processing
      │
      ▼
Prompt Construction
      │
      ▼
OpenAI LLM Analysis
      │
      ▼
AI Generated Summary
      │
      ▼
Actionable Insights
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/kranjann/ai-log-summarizer.git
cd ai-log-summarizer
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## Run Application

```bash
python app/main.py
```

---

## Sample Use Cases

### Production Incident Analysis

Analyze application logs and identify probable causes of service failures.

### QA Failure Investigation

Summarize automation execution logs and quickly understand failed scenarios.

### Telemetry Review

Extract critical observations from connected vehicle telemetry data.

---

## Future Enhancements

- Multi-file log analysis
- Log anomaly detection
- Severity classification
- Interactive dashboard
- Support for multiple LLM providers
- Automated incident report generation

---

## Author

Krishna Ranjan

Senior QA Engineer | Automation Test Lead

GitHub: https://github.com/kranjann
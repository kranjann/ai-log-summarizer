# AI Log Analyzer - Project Context

## Project Goal

Build a production-style AI-powered log analysis platform while learning LLM engineering concepts from beginner to advanced through hands-on implementation.

The project is intentionally evolving step-by-step to learn:

* Python project architecture
* Git and GitHub workflows
* Prompt Engineering
* Structured Outputs
* Pydantic Validation
* Embeddings
* Semantic Search
* RAG (Retrieval-Augmented Generation)
* Tool Calling
* Agents
* Evaluation
* Observability

---

## Current Status

### Milestone 1 - AI Log Analyzer Foundation ✅

Implemented:

* OpenAI API integration
* Environment variable management with `.env`
* Log file ingestion
* Pathlib-based file handling
* CLI execution via `main.py`
* GitHub repository setup
* GitHub Actions CI pipeline
* Feature branch workflow

Learned:

* Virtual environments
* Python imports
* Pathlib
* Relative vs absolute paths
* Git basics
* Git diff
* Git branching
* CI/CD fundamentals

---

### Milestone 2 - Prompt Engineering V2 ✅

Implemented:

* Dedicated `prompts.py`
* System prompt design
* Severity classification rules
* Consistent output formatting

Prompt Contract:

Summary:
Root Cause:
Severity:
Recommendation:

Learned:

* Role prompting
* Prompt specificity
* Prompt guardrails
* Prompt contracts
* LLM evaluation
* Inference vs evidence

---

### Milestone 3 - Structured JSON Output ✅

Implemented:

* Prompt updated to return JSON
* `json.loads()` parsing
* Python dictionary output

Learned:

* Structured output generation
* JSON parsing
* LLM as a data generator
* Machine-readable outputs

---

### Milestone 4 - Pydantic Validation ✅

Implemented:

* `schemas/log_schema.py`
* `LogAnalysis` Pydantic model
* Validation layer between GPT and application
* Typed domain objects

Current Flow:

Log File
→ Prompt
→ OpenAI
→ JSON String
→ json.loads()
→ LogAnalysis (Pydantic)
→ Application

Learned:

* Data contracts
* Type validation
* Domain models
* Fail-fast principle
* Why model output should never be trusted directly

---

## Current Architecture

ai-log-analyzer/

app/
│
├── main.py
├── llm.py
├── prompts.py
│
└── schemas/
└── log_schema.py

logs/
│
├── telemetry.log
├── mqtt_failure.log
└── application_crash.log

docs/
└── PROJECT_CONTEXT.md

.github/workflows/
└── ci.yml

README.md
requirements.txt

---

## Current Data Model

```python
class LogAnalysis(BaseModel):
    summary: str
    root_cause: str
    severity: str
    recommendations: List[str]
```

---

## Current Test Cases

### telemetry.log

Scenario:

* PostgreSQL timeout
* Connection pool exhausted
* Startup failure

Expected Severity:

Critical

---

### mqtt_failure.log

Scenario:

* TLS handshake failure
* Certificate validation failure
* Authentication rejected
* MQTT connection terminated

Expected Severity:

Critical

---

### application_crash.log

Scenario:

* Java OutOfMemoryError
* Batch processing aborted
* Application terminated

Expected Severity:

Critical

---

## Git Workflow

Preferred Workflow:

1. Create feature branch
2. Commit changes
3. Push branch
4. Open GitHub Pull Request
5. Review changes
6. Merge PR
7. Delete feature branch

Important:

Use GitHub Pull Requests instead of direct local merges whenever practical.

---

## Current Tech Stack

* Python
* OpenAI SDK
* Pydantic
* python-dotenv
* pathlib
* GitHub Actions

---

## AI Engineering Concepts Learned

### Prompt Engineering

* Role prompting
* Output contracts
* Guardrails
* Severity classification

### Structured Outputs

* JSON generation
* JSON parsing
* Machine-readable responses

### Validation

* Pydantic models
* Type checking
* Fail-fast design

### Software Engineering

* Feature branches
* Pull Requests
* CI pipelines
* Incremental development

---

## Upcoming Milestone

### Milestone 5 - Embeddings

Goal:

Teach the system to understand semantic similarity between logs.

Current:

New Log
→ Analyze

Future:

New Log
→ Generate Embedding
→ Search Similar Historical Logs
→ Retrieve Similar Incidents
→ Analyze With Context

Concepts To Learn:

* Embeddings
* Vectors
* Cosine Similarity
* Semantic Search
* Similarity Retrieval

---

## Future Roadmap

### Phase 2

* Embeddings
* Semantic Search
* Historical Incident Retrieval

### Phase 3

* Mini RAG System
* Context Injection
* Retrieval-Augmented Analysis

### Phase 4

* Tool Calling
* Agent Architecture

### Phase 5

* FastAPI
* Docker
* Deployment
* Monitoring

---

## Key Lessons Learned

1. Prompts are contracts.
2. Understanding is different from format compliance.
3. LLM output should be treated as untrusted input.
4. Validate everything.
5. Small PRs are easier to review than large commits.
6. Debug one layer at a time:

   * File ingestion
   * Prompt
   * LLM response
   * JSON parsing
   * Validation

---

## Last Completed Feature

Feature Branch:

feature/structured-output-v1

Result:

Validated `LogAnalysis` Pydantic object returned from GPT output instead of a raw dictionary.

Example Runtime Type:

<class 'schemas.log_schema.LogAnalysis'>

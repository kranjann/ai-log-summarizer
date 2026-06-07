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

# Current Status

## Milestone 1 - AI Log Analyzer Foundation ✅

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
* Git branching
* Pull Requests
* CI/CD fundamentals

---

## Milestone 2 - Prompt Engineering V2 ✅

Implemented:

* Dedicated prompts module
* System prompt design
* Severity classification rules
* Consistent response format

Prompt Contract:

Summary:
Root Cause:
Severity:
Recommendations:

Learned:

* Role prompting
* Prompt specificity
* Prompt guardrails
* Prompt contracts
* LLM evaluation

---

## Milestone 3 - Structured JSON Output ✅

Implemented:

* JSON response generation
* JSON parsing
* Machine-readable output

Learned:

* Structured outputs
* JSON parsing
* LLM data generation patterns

---

## Milestone 4 - Pydantic Validation ✅

Implemented:

* Pydantic schema layer
* LogAnalysis domain model
* Validation between LLM and application

Current Flow:

Log File
→ Prompt
→ OpenAI
→ JSON
→ json.loads()
→ LogAnalysis
→ Application

Data Model:

```python
class LogAnalysis(BaseModel):
    summary: str
    root_cause: str
    severity: str
    recommendations: List[str]
```

Learned:

* Data contracts
* Domain models
* Validation
* Fail-fast design
* Typed application architecture

---

## Milestone 5 - Embedding Foundation ✅

Implemented:

* Embedding service
* OpenAI Embeddings API integration
* Environment configuration reuse
* First vector generation

Current Flow:

Text
→ Embedding Model
→ Vector

Example:

Input:

PostgreSQL connection pool exhausted

Output:

```python
[
    -0.0546,
    -0.0300,
    0.0701,
    ...
]
```

Observed:

* Embedding Type: list
* Embedding Dimensions: 1536

Learned:

* Embeddings
* Vectors
* Semantic representations
* Embedding models vs chat models
* High-dimensional vector spaces

Key Insight:

Different text with similar meaning generates vectors that are close together in semantic space.

Examples:

* PostgreSQL connection pool exhausted
* Unable to acquire database connection

These are semantically similar despite using different words.

---

# Current Architecture

ai-log-analyzer/

app/
│
├── main.py
├── config.py
│
├── services/
│   ├── llm_service.py
│   └── embedding_service.py
│
├── prompts.py
│
└── schemas/
└── log_schema.py

data/
│
└── incidents/

logs/

docs/
│
└── PROJECT_CONTEXT.md

.github/workflows/

README.md
requirements.txt

---

# Historical Incident Dataset

Planned Incident Categories:

* Database failures
* Memory failures
* Authentication failures
* TLS failures
* Kafka issues
* Redis failures
* Disk exhaustion
* API rate limits
* Configuration errors

Purpose:

Provide retrieval candidates for future semantic search and RAG implementation.

---

# Current Test Logs

## telemetry.log

Scenario:

* PostgreSQL timeout
* Connection pool exhausted
* Startup failure

Expected Severity:

Critical

---

## mqtt_failure.log

Scenario:

* TLS handshake failure
* Certificate validation failure
* MQTT authentication rejected

Expected Severity:

Critical

---

## application_crash.log

Scenario:

* Java OutOfMemoryError
* Batch processing failure
* Application terminated

Expected Severity:

Critical

---

# Git Workflow

Preferred Workflow:

1. Create feature branch
2. Commit changes
3. Push branch
4. Open Pull Request
5. Review
6. Merge PR
7. Delete feature branch

Example Branches:

* feature/structured-output-v1
* feature/embedding-foundation
* feature/semantic-search-v1

Important:

Use GitHub Pull Requests instead of direct merges whenever practical.

---

# Current Tech Stack

* Python
* OpenAI SDK
* Pydantic
* python-dotenv
* GitHub Actions

---

# AI Engineering Concepts Learned

## Prompt Engineering

* Role prompting
* Output contracts
* Guardrails
* Classification

## Structured Outputs

* JSON generation
* JSON parsing
* Machine-readable responses

## Validation

* Pydantic models
* Type checking
* Data contracts

## Embeddings

* Vector representations
* Semantic similarity
* Embedding generation
* High-dimensional search foundations

## Software Engineering

* Feature branches
* Pull Requests
* CI pipelines
* Incremental delivery

---

# Upcoming Milestone

## Milestone 6 - Semantic Search

Goal:

Find historical incidents that are semantically similar to a new log.

Future Flow:

New Log
→ Embedding
→ Cosine Similarity
→ Top-K Similar Incidents
→ Ranked Results

Concepts To Learn:

* Cosine Similarity
* Vector Comparison
* Nearest Neighbors
* Top-K Retrieval
* Semantic Search

Deliverable:

Return the most similar incidents for a new log entry.

---

# Future Roadmap

## Phase 2

* Semantic Search
* Historical Incident Retrieval

## Phase 3

* Mini RAG System
* Context Injection
* Retrieval-Augmented Analysis

## Phase 4

* Evaluation Framework
* Prompt Evaluation
* Retrieval Evaluation

## Phase 5

* Tool Calling
* Agent Architecture

## Phase 6

* FastAPI
* Docker
* Deployment
* Monitoring
* Observability

---

# Key Lessons Learned

1. Prompts are contracts.
2. Understanding is different from format compliance.
3. LLM output should be treated as untrusted input.
4. Validate everything.
5. Small PRs are easier to review than large commits.
6. Embeddings encode meaning, not keywords.
7. Similarity is measured mathematically, not linguistically.
8. Debug one layer at a time:

   * File ingestion
   * Prompt
   * LLM response
   * JSON parsing
   * Validation
   * Embedding generation
   * Similarity search

---

# Last Completed Feature

Feature Branch:

feature/embedding-foundation

Result:

Successfully generated OpenAI embeddings and verified semantic vector generation.

Example Runtime Output:

```python
<class 'list'>
1536
[-0.0546, -0.0300, 0.0701, ...]
```

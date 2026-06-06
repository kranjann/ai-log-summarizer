# AI Log Analyzer - Project Context

## Project Goal

Build a production-style AI-powered log analysis platform while learning LLM engineering concepts from beginner to advanced.

The project is intentionally being built incrementally to learn:

* Python project architecture
* Git and GitHub workflows
* Prompt Engineering
* Structured Outputs
* Pydantic
* Embeddings
* RAG
* Tool Calling
* Agents
* Evaluation
* Observability

---

## Current Status

### Completed Milestones

#### Milestone 1 - AI Log Analyzer Foundation

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

* Python imports
* Virtual environments
* Relative vs absolute paths
* Pathlib
* Git basics
* Git diff
* Git branching

---

#### Milestone 2 - Prompt Engineering V2

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
* Prompt contracts
* Guardrails
* LLM evaluation
* Inference vs evidence

---

#### Milestone 3 - JSON Output Parsing

Implemented:

* Prompt updated to return JSON
* `json.loads()` parsing
* Python dictionary output

Current Flow:

Log File
→ Prompt
→ OpenAI
→ JSON
→ Python Dict

Learned:

* Structured data generation
* JSON parsing
* LLM as a data generator
* Importance of machine-readable outputs

---

## Current Architecture

ai-log-analyzer/

app/

* main.py
* llm.py
* prompts.py

logs/

* telemetry.log
* mqtt_failure.log
* application_crash.log

.github/workflows/

* ci.yml

README.md
requirements.txt

---

## Current Log Test Cases

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
* Authentication rejection

Expected Severity:

Critical

---

### application_crash.log

Scenario:

* Java OutOfMemoryError
* Batch processing aborted
* Application termination

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

Avoid direct git merge into main unless explicitly needed.

---

## Current Tech Stack

* Python
* OpenAI SDK
* python-dotenv
* pathlib
* GitHub Actions

---

## Upcoming Milestones

### Next

Structured Output V1

Goals:

* Introduce Pydantic
* Create schemas
* Validate LLM output
* Convert dicts into typed objects

Planned Structure:

app/

schemas/

* log_schema.py

Expected Model:

class LogAnalysis:
summary
root_cause
severity
recommendations

---

### Future

* Embeddings
* Semantic Search
* Mini RAG
* Vector Databases
* Tool Calling
* Agents
* Multi-Agent Systems
* Evaluation Framework
* Observability
* FastAPI
* Docker

---

## Key Lessons Learned

1. Prompts are contracts.
2. Understanding is different from format compliance.
3. LLM output should be treated as data.
4. Validate everything before trusting it.
5. Small PRs are easier to review than large commits.
6. Debug one layer at a time:

   * File ingestion
   * Prompt
   * LLM response
   * Parsing
   * Validation

---

## Last Completed Feature

Prompt V2

Status:

Merged via GitHub Pull Request

Result:

Consistent severity classification across all sample logs.

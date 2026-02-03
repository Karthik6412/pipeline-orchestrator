## Project Spec: Pipeline Orchestrator

**Goal:** Build a config-driven pipeline orchestrator that demonstrates platform engineering principles.

**Requirements:**
1. Read YAML config files
2. Validate config before execution (guardrails)
3. Execute pipeline steps with retry logic
4. Check schema compatibility
5. Output structured JSON logs

**Architecture:**
Control Plane → Validator → Executor → Logger

**Guardrails to implement:**
- Require schema version in config
- Block forbidden paths (/system, /admin, /root)
- Cap retries at 3 max
- Enforce retry policy exists

**Retry logic:**
- Exponential backoff: 1s, 2s, 4s
- Max 3 retries per step
- Step-level failure isolation

**Schema checker:**
- Allow: adding new columns
- Reject: deleting columns, changing types, changing primary keys

**Deliverables:**
- GitHub repo with README
- Working orchestrator.py
- Sample configs (valid + invalid)
- Architecture diagram
- Design decisions documented

**You have 8-12 hours. Build it.**

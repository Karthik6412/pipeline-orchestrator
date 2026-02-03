# Pipeline Orchestrator with Guardrails

A config-driven data pipeline control plane demonstrating failure handling, schema governance, and multi-tenant safety patterns.

## Why This Project

Demonstrates platform engineering principles I applied at Lowe's:
- Control plane validation before execution
- Schema contract enforcement (backward compatibility)
- Failure isolation and retry semantics
- Multi-tenant path restrictions

## Architecture

[Will add diagram]

Control Plane → Validator → Scheduler → Executor → Logger

## Features

- **Config Validation**: Schema version required, forbidden paths blocked
- **Schema Contract Enforcement**: Additive-only changes, no column deletion/PK changes
- **Retry Semantics**: Exponential backoff, max 3 retries per step
- **Step-Level Failure Isolation**: Individual steps fail independently
- **Structured Logging**: JSON logs for observability

## Tech Stack

- Python 3.9+
- Standard library only (no external dependencies except PyYAML)

## Quick Start

[Will add usage instructions]

## Design Decisions

[Will document: why guardrails, why retry caps, why schema contracts]

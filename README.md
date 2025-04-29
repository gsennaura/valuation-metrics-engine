# Valuation Metrics Engine

A simple and modular Python application that calculates the market and auction values of heavy equipment based on provided cost and ratios.

This project was developed as part of a technical challenge.

---

## Overview

Each equipment model has a historical ratio schedule and sale details.  
To compute the value of a given model in a specific year:

```python
market_value = cost * market_ratio
auction_value = cost * auction_ratio
```

- If the requested year is not found, the system uses default ratios (if available).
- Invalid inputs are handled gracefully with specific exceptions.

---

## What This Project Covers

- Clean Architecture principles (modular, testable code)
- Domain logic fully decoupled from infrastructure
- Typed and validated models using Pydantic
- Unit and integration tests using Pytest
- Clear error handling with custom exceptions
- CLI entry point via `main.py`
- Automation with Makefile

---

## Requirements

- Python 3.11 or higher  
- Unix-based system (Linux/macOS) or Windows with Make installed

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/gsennaura/valuation-metrics-engine.git
cd valuation-metrics-engine
```

### 2. Install dependencies and setup virtual environment

```bash
make install
```

### 3. Run the program

```bash
make run
```

---

## Run Tests

To execute all unit and integration tests:

```bash
make test
```

---

## Code Style (Optional)

To run static code analysis using flake8:

```bash
make lint
```

---

## Example

Example console output when running the program:

```console
Model ID: 67352, Year: 2007 -> marketValue=216572.73, auctionValue=123591.11
Model ID: 87964, Year: 2011 -> ModelNotFoundError: Model ID '87964' not found.
```

---

## File Structure

```bash
src/
├── domain/                # Business logic (pure functions)
├── models/                # Pydantic data models and exceptions
├── services/              # Orchestration and data integration
├── tests/                 # Unit and integration tests
api-response.json          # Mocked input dataset
main.py                    # CLI entry point
Makefile                   # Automation commands
requirements.txt           # Project dependencies
.github/                   # PR and commit templates
```

---

## Notes

This challenge was built with a focus on clarity, testability, and modularity — while keeping the scope simple, as requested.
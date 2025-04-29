VENV=.venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip

check-python:
	@command -v python3 > /dev/null || (echo "Python 3.11+ is not installed." && exit 1)

install: check-python
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

test:
	PYTHONPATH=src $(VENV)/bin/pytest -v
	
lint:
	$(VENV)/bin/flake8 src/

run:
	PYTHONPATH=src $(PYTHON) main.py

clean:
	rm -rf $(VENV) .pytest_cache __pycache__ */__pycache__ .mypy_cache .coverage

.PHONY: check-python install test lint run clean

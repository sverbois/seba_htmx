.PHONY: help  # List phony targets
help:
	@cat "Makefile" | grep '^.PHONY:' | sed -e "s/^.PHONY:/- make/"

.PHONY: install  # Install development environment
install: venv/bin/pip
	venv/bin/pip install -r requirements.txt

.PHONY: start  # Start component
start:
	venv/bin/uvicorn src.main:app --reload

.PHONY: clean  # Clean development environment
clean:
	rm -rf venv

venv/bin/pip:
	python3.12 -m venv venv
	venv/bin/pip install --upgrade pip

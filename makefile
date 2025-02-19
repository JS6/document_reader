.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: setup_env
setup_env: ## create the env
	if [ ! -d ".venv" ]; then \
		python3.11 -m venv .venv && \
		chmod -R 755 .venv; \
	fi
	. .venv/bin/activate && \
	pip install -r requirements.txt && \
	python setup.py install && \
	python -m spacy download en_core_web_sm && \
	pip install pre-commit

.PHONY: pre-commit
pre-commit: ## Run pre-commit checks
	pre-commit run --all-files

help:
	@echo "make"
	@echo "    install"
	@echo "        Install all requirements for running the bot."
	@echo "    install-dev"
	@echo "        Install all requirements for development."
	@echo "    clean"
	@echo "        Remove Python/build artifacts."
	@echo "    formatter"
	@echo "        Apply black formatting to code."
	@echo "    lint"
	@echo "        Lint code with flake8, and check if black formatter should be applied."
	@echo "    types"
	@echo "        Check for type errors using pytype."
	@echo "    test-actions"
	@echo "        Run custom action unit tests"

install:
	python -m pip install --upgrade "pip<20"
	pip install -r requirements.txt
	python -m spacy download en_core_web_md
	python -m spacy link en_core_web_md en 
	pip install -e .

install-dev:
	python -m pip install --upgrade "pip<20"
	pip install -r requirements-dev.txt
	python -m spacy download en_core_web_md
	python -m spacy link en_core_web_md en 
	pip install -e .

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
	rm -rf build/
	rm -rf .pytype/
	rm -rf dist/
	rm -rf docs/_build

formatter:
	black --verbose --config pyproject.toml actions tests

lint:
	flake8 actions tests
	black --check --verbose --config pyproject.toml actions tests

types:
	pytype --keep-going actions tests

test-actions:
	pytest . -vv

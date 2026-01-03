.PHONY: help install install-dev test test-verbose lint type-check clean build dist upload-test upload docs

help:
	@echo "Available commands:"
	@echo "  make install       - Install package in development mode"
	@echo "  make install-dev   - Install with development dependencies"
	@echo "  make test          - Run tests"
	@echo "  make test-verbose  - Run tests with verbose output"
	@echo "  make lint         - Run linting checks"
	@echo "  make type-check    - Run type checking"
	@echo "  make clean         - Clean build artifacts"
	@echo "  make build         - Build distribution packages"
	@echo "  make dist          - Build and check distribution"
	@echo "  make upload-test   - Upload to TestPyPI"
	@echo "  make upload        - Upload to PyPI"
	@echo "  make docs          - Generate documentation"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"
	pip install -r requirements-dev.txt

test:
	python -m unittest discover -s tests -p "test_*.py" -v

test-verbose:
	python -m unittest discover -s tests -p "test_*.py" -v -b

lint:
	flake8 numwordify/ tests/ --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 numwordify/ tests/ --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

type-check:
	mypy numwordify/ --ignore-missing-imports

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	find . -type d -name __pycache__ -exec rm -r {} +
	find . -type f -name "*.pyc" -delete

build:
	python -m build

dist: clean build
	twine check dist/*

upload-test: dist
	twine upload --repository testpypi dist/*

upload: dist
	twine upload dist/*

docs:
	@echo "Documentation is in README.md"
	@echo "For API docs, see README.md or run: python -c 'import numwordify; help(numwordify)'"



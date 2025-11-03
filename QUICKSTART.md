# Quick Start Guide

## Installation (Development)

```bash
cd /Users/mohamadabukhashabeh/PycharmProjects/python-packages/num2words
pip install -e .
```

## Basic Usage

```python
from num2words import num2words

# English
print(num2words(42))
# Output: "forty-two"

# Arabic
print(num2words(42, lang='ar'))
# Output: "اثنان وأربعون"

# Ordinal
print(num2words(1, to='ordinal'))
# Output: "first"

# Decimal
print(num2words(123.45))
# Output: "one hundred twenty-three point forty-five"
```

## Running Tests

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## Building for Distribution

```bash
# Install build tools
pip install build twine

# Build package
python -m build

# This creates:
# - dist/num2words-0.1.0.tar.gz
# - dist/num2words-0.1.0-py3-none-any.whl
```

## Project Structure

```
num2words/
├── num2words/              # Main package
│   ├── __init__.py
│   ├── converter.py        # Main converter interface
│   └── languages/          # Language implementations
│       ├── __init__.py
│       ├── base.py         # Base converter class
│       ├── english.py      # English converter
│       └── arabic.py       # Arabic converter
├── tests/                  # Test suite
│   ├── test_english.py
│   ├── test_arabic.py
│   └── test_integration.py
├── examples/               # Framework examples
│   ├── django_example.py
│   ├── fastapi_example.py
│   └── flask_example.py
├── setup.py                # Setup script
├── pyproject.toml          # Modern Python packaging
├── README.md               # Documentation
├── LICENSE                 # MIT License
└── requirements.txt        # Dependencies (none!)

```

## Features

- **Zero Dependencies** - Pure Python, no external libraries
- **Lightweight** - Small package size
- **Performant** - Fast conversion algorithms
- **Multi-language** - English and Arabic support
- **Framework Agnostic** - Works with Django, FastAPI, Flask, etc.
- **Well Tested** - Comprehensive test suite
- **PyPI Ready** - Ready for distribution  


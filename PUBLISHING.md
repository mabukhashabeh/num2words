# Publishing to PyPI

This guide explains how to publish the `num2words` package to PyPI.

## Prerequisites

1. Create accounts on:
   - [PyPI](https://pypi.org/account/register/)
   - [TestPyPI](https://test.pypi.org/account/register/) (for testing)

2. Install build tools:
```bash
pip install build twine
```

## Steps to Publish

### 1. Update Version

Update the version in:
- `pyproject.toml` (version field)
- `setup.py` (version field)
- `num2words/__init__.py` (__version__)

### 2. Build the Package

```bash
cd num2words
python -m build
```

This creates:
- `dist/num2words-0.1.0.tar.gz` (source distribution)
- `dist/num2words-0.1.0-py3-none-any.whl` (wheel)

### 3. Test on TestPyPI (Recommended)

```bash
# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Test installation
pip install --index-url https://test.pypi.org/simple/ num2words
```

### 4. Publish to PyPI

```bash
# Upload to PyPI
twine upload dist/*
```

### 5. Verify Installation

```bash
pip install num2words
python -c "from num2words import num2words; print(num2words(42))"
```

## Updating the Package

1. Update version number
2. Update CHANGELOG.md
3. Build: `python -m build`
4. Upload: `twine upload dist/*`

## Notes

- Never upload the same version twice to PyPI
- Always test on TestPyPI first
- Keep credentials secure (use `~/.pypirc` or environment variables)


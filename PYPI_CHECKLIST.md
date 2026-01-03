# PyPI Publishing Checklist

This checklist ensures the package meets all PyPI requirements for professional packages.

## Pre-Publishing Checklist

### Code Quality
- [x] All tests pass (39 tests)
- [x] Type hints added throughout codebase
- [x] Comprehensive edge case handling (infinity, NaN, very large numbers)
- [x] Error handling for invalid inputs
- [x] Code follows PEP 8 style guidelines
- [x] No linter errors

### Documentation
- [x] README.md with comprehensive documentation
- [x] API reference documentation
- [x] Usage examples for all frameworks (Django, FastAPI, Flask)
- [x] CHANGELOG.md with version history
- [x] CONTRIBUTING.md for contributors
- [x] CODE_OF_CONDUCT.md
- [x] SECURITY.md for vulnerability reporting
- [x] AUTHORS.md with maintainer information
- [x] LICENSE file (MIT)

### Package Configuration
- [x] setup.py configured correctly
- [x] pyproject.toml with all metadata
- [x] setup.cfg for additional configuration
- [x] __version__ in __init__.py matches version in setup files
- [x] Author information correct in all files
- [x] GitHub URLs correct
- [x] Python version requirements specified (>=3.7)
- [x] Classifiers appropriate for package

### Testing Infrastructure
- [x] Comprehensive test suite (39 tests covering edge cases)
- [x] Tests for English conversion
- [x] Tests for Arabic conversion
- [x] Tests for edge cases (infinity, NaN, very large numbers, etc.)
- [x] Integration tests
- [x] CI/CD workflow (.github/workflows/ci.yml)
- [x] Publish workflow (.github/workflows/publish.yml)
- [x] tox.ini for multi-version testing
- [x] Makefile for common tasks

### Build Configuration
- [x] MANIFEST.in includes all necessary files
- [x] .gitignore excludes build artifacts
- [x] Requirements files (requirements.txt, requirements-dev.txt)
- [x] .pypirc.example for publishing credentials

### Code Features
- [x] Zero external dependencies
- [x] Type hints throughout
- [x] Comprehensive error handling
- [x] Edge case handling (infinity, NaN, very large numbers)
- [x] Support for English and Arabic
- [x] Cardinal and ordinal number support
- [x] Decimal number support
- [x] Negative number support
- [x] Gender support for Arabic

## Publishing Steps

1. **Update Version**
   - Update version in pyproject.toml
   - Update version in setup.py
   - Update __version__ in numwordify/__init__.py
   - Update CHANGELOG.md

2. **Run Tests**
   ```bash
   make test
   python -m unittest discover -s tests -v
   ```

3. **Lint and Type Check**
   ```bash
   make lint
   make type-check
   ```

4. **Build Package**
   ```bash
   make build
   # or
   python -m build
   ```

5. **Check Package**
   ```bash
   twine check dist/*
   ```

6. **Test on TestPyPI**
   ```bash
   make upload-test
   # or
   twine upload --repository testpypi dist/*
   ```

7. **Install from TestPyPI and Test**
   ```bash
   pip install --index-url https://test.pypi.org/simple/ numwordify
   python -c "from numwordify import num2words; print(num2words(42))"
   ```

8. **Publish to PyPI**
   ```bash
   make upload
   # or
   twine upload dist/*
   ```

9. **Verify Installation**
   ```bash
   pip install numwordify
   python -c "from numwordify import num2words; print(num2words(42))"
   ```

## Post-Publishing

- [ ] Create GitHub release
- [ ] Update documentation if needed
- [ ] Announce on social media/forums (optional)

## Notes

- Never upload the same version twice to PyPI
- Always test on TestPyPI first
- Keep API tokens secure (use environment variables or .pypirc)
- Follow semantic versioning (MAJOR.MINOR.PATCH)



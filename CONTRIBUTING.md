# Contributing to num2words

Thank you for your interest in contributing to num2words! This document provides guidelines and instructions for contributing.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Install the package in development mode:
   ```bash
   pip install -e .
   pip install -r requirements-dev.txt
   ```

## Development Setup

```bash
# Clone the repository
git clone https://github.com/mabukhashabeh/num2words.git
cd num2words

# Install in development mode
make install-dev

# Run tests
make test
```

## Code Style

- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Keep functions focused and small
- Add docstrings to all public functions and classes
- Maximum line length: 127 characters

## Testing

- Write tests for all new features
- Ensure all tests pass before submitting
- Run tests with: `make test` or `python -m unittest discover -s tests -v`
- Aim for high test coverage

## Submitting Changes

1. Create a feature branch from `main` or `develop`
2. Make your changes
3. Add tests for new functionality
4. Ensure all tests pass
5. Update documentation if needed
6. Submit a pull request with a clear description

## Pull Request Guidelines

- Provide a clear description of changes
- Reference any related issues
- Ensure CI checks pass
- Request review from maintainers

## Adding New Languages

To add support for a new language:

1. Create a new converter class in `num2words/languages/`
2. Inherit from `BaseConverter`
3. Implement the `convert` method
4. Add language codes to `NumberConverter._converters`
5. Add comprehensive tests
6. Update documentation

## Reporting Issues

When reporting issues, please include:
- Python version
- Package version
- Steps to reproduce
- Expected vs actual behavior
- Error messages if any

## License

By contributing, you agree that your contributions will be licensed under the MIT License.


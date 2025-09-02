# Contributing to SEL_RDB

We welcome contributions to SEL_RDB! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Create a new branch for your feature or bug fix
4. Make your changes
5. Test your changes
6. Submit a pull request

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/SEL_Rdb.git
   cd SEL_Rdb
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the package in development mode:
   ```bash
   pip install -e ".[dev]"
   ```

## Code Standards

### Python Style

We follow PEP 8 style guidelines. Key points:
- Use 4 spaces for indentation
- Limit lines to 79 characters
- Use descriptive variable and function names
- Write docstrings for all public functions and classes

### Documentation

- Update documentation when adding new features
- Write clear, concise docstrings
- Provide usage examples for new functionality
- Keep README.md and docs/ up to date

## Testing

### Running Tests

To run the existing test suite:

```bash
python test_package.py
```

### Adding Tests

When adding new features:
1. Write tests for your new functionality
2. Ensure all existing tests still pass
3. Add test cases to `test_package.py` or create new test files as appropriate

## Submitting Changes

### Pull Request Process

1. Ensure your code follows the style guidelines
2. Update documentation as needed
3. Add tests for new functionality
4. Verify all tests pass
5. Create a pull request with a clear description of changes

### Commit Messages

- Use clear, descriptive commit messages
- Follow the format: "Brief summary (fixes #123)"
- Reference issue numbers when applicable

## Reporting Issues

### Bug Reports

When reporting bugs, please include:
- Version of SEL_RDB you're using
- Python version
- Operating system
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Any error messages

### Feature Requests

For feature requests, please describe:
- The problem you're trying to solve
- How the feature would work
- Examples of usage
- Any alternative solutions you've considered

## Areas for Contribution

### Code Improvements

- Enhance error handling and reporting
- Improve performance of file processing
- Add support for additional RDB file formats
- Expand logic extraction capabilities

### Documentation

- Improve existing documentation
- Add more usage examples
- Create tutorials
- Translate documentation

### Testing

- Expand test coverage
- Add integration tests
- Create test fixtures for different RDB file types

## Community

### Code of Conduct

Please be respectful and professional in all interactions. We are committed to providing a welcoming environment for all contributors.

### Getting Help

If you need help with contributing:
1. Check the documentation
2. Search existing issues
3. Open a new issue with your question

Thank you for contributing to SEL_RDB!
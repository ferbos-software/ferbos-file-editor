# Contributing to Ferbos File Editor

Thank you for your interest in contributing to Ferbos File Editor! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow

## Development Setup

### Prerequisites

- Python 3.11 or higher
- Git
- Home Assistant development environment (optional, for full testing)

### Installation

1. **Fork and clone the repository**:
   ```bash
   git clone https://github.com/your-username/ferbos-file-editor.git
   cd ferbos-file-editor
   ```

2. **Install development dependencies**:
   ```bash
   pip install -r requirements-dev.txt
   ```

3. **Verify setup**:
   ```bash
   ruff --version
   pytest --version
   ```

## Development Workflow

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 2. Make Your Changes

- Write clean, readable code
- Follow existing code style
- Add tests for new functionality
- Update documentation if needed

### 3. Run Local Checks

Before committing, ensure:

```bash
# Format code
ruff format custom_components/ferbos_file_editor/

# Check linting
ruff check custom_components/ferbos_file_editor/

# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=custom_components/ferbos_file_editor --cov-report=term
```

### 4. Commit Your Changes

Write clear, descriptive commit messages:

```bash
git add .
git commit -m "Add feature: description of what you added"
```

**Commit message guidelines**:
- Use imperative mood ("Add feature" not "Added feature")
- Keep first line under 50 characters
- Add detailed description if needed

### 5. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

## Pull Request Process

### PR Requirements

1. **Description**: Clearly describe what the PR does and why
2. **Tests**: Include tests for new functionality
3. **Documentation**: Update README or docs if needed
4. **CI Passes**: All CI checks must pass
5. **No Conflicts**: Branch must be up to date with `main`

### PR Review Process

1. **CI Runs Automatically**: GitHub Actions will run all checks
2. **Peer Review**: At least 2 team members must approve
3. **Address Feedback**: Make requested changes
4. **Approval**: Once approved and CI passes, PR can be merged

### PR Checklist

Before submitting, ensure:

- [ ] Code follows existing style (run `ruff format` and `ruff check`)
- [ ] Tests are added/updated and passing
- [ ] Documentation is updated if needed
- [ ] No merge conflicts with `main`
- [ ] Commit messages are clear and descriptive
- [ ] All CI checks pass

## Code Style

### Python Style

- Follow PEP 8 (enforced by Ruff)
- Use type hints where appropriate
- Keep functions focused and small
- Add docstrings for public functions/classes

### Formatting

We use Ruff for formatting. Run:

```bash
ruff format custom_components/ferbos_file_editor/
```

### Linting

We use Ruff for linting. Run:

```bash
ruff check custom_components/ferbos_file_editor/
```

## Testing

### Writing Tests

- Place unit tests in `tests/test_*.py`
- Place integration tests in `tests/integration/`
- Use descriptive test names
- Follow pytest conventions

### Test Structure

```python
@pytest.mark.unit
class TestMyFunction:
    """Test my_function."""
    
    @pytest.mark.asyncio
    async def test_my_function_success(self):
        """Test successful case."""
        # Test code here
        assert result == expected
```

### Running Tests

```bash
# All tests
pytest tests/ -v

# Unit tests only
pytest tests/ -v -m unit

# Integration tests only
pytest tests/ -v -m integration

# Smoke tests
pytest tests/ -v -m smoke

# With coverage
pytest tests/ -v --cov=custom_components/ferbos_file_editor
```

## Peer Review Guidelines

### For Reviewers

**What to Review**:
- Code quality and style
- Test coverage
- Functionality correctness
- Security considerations
- Documentation updates

**Review Checklist**:
- [ ] Code is readable and well-structured
- [ ] Tests are comprehensive
- [ ] No obvious bugs or security issues
- [ ] Documentation is clear
- [ ] CI checks pass

**Providing Feedback**:
- Be constructive and specific
- Suggest improvements, not just point out issues
- Approve when ready, or request changes with clear reasons

### For Authors

**Responding to Reviews**:
- Address all feedback
- Ask questions if something is unclear
- Update the PR with changes
- Mark conversations as resolved when addressed

## Branch Protection

The `main` branch is protected with the following rules:

- ✅ Requires pull request before merging
- ✅ Requires 2 approvals minimum
- ✅ Requires all CI checks to pass
- ✅ Requires branch to be up to date

See [CI_SETUP.md](CI_SETUP.md) for detailed branch protection configuration.

## Getting Help

- **Issues**: Open an issue for bugs or feature requests
- **Discussions**: Use GitHub Discussions for questions
- **Documentation**: Check README.md and CI_SETUP.md

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Thank You!

Your contributions make this project better. We appreciate your time and effort!


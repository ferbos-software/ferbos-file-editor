# CI/CD Setup Guide

This document describes the Continuous Integration (CI) pipeline setup and branch protection requirements for the Ferbos File Editor integration.

## CI Pipeline Overview

The CI pipeline runs automatically on:
- Every push to `main` or `master` branch
- Every pull request targeting `main` or `master` branch

## CI Jobs

### 1. Lint Job
- **Purpose**: Code quality and style checking
- **Tools**: Ruff (linter and formatter)
- **Location**: `.github/workflows/ci.yml` → `lint` job
- **Checks**:
  - Code linting with `ruff check`
  - Code formatting with `ruff format --check`

### 2. Test Job
- **Purpose**: Unit test execution
- **Tools**: pytest with coverage
- **Location**: `.github/workflows/ci.yml` → `test` job
- **Checks**:
  - All unit tests in `tests/` directory
  - Code coverage reporting
  - Coverage uploaded to Codecov (optional)

### 3. Integration Job
- **Purpose**: Integration and smoke tests
- **Tools**: pytest with integration markers
- **Location**: `.github/workflows/ci.yml` → `integration` job
- **Checks**:
  - Smoke tests for basic functionality
  - Integration tests for WebSocket API

### 4. Validate Job
- **Purpose**: Validate integration structure
- **Location**: `.github/workflows/ci.yml` → `validate` job
- **Checks**:
  - `manifest.json` is valid JSON
  - `hacs.json` is valid JSON
  - Required files are present

## Branch Protection Rules

To enforce peer review and CI requirements, configure branch protection rules in GitHub:

### Required Settings

1. **Navigate to**: Repository Settings → Branches → Add rule
2. **Branch name pattern**: `main` (or `master`)
3. **Enable the following**:
   - ✅ Require a pull request before merging
   - ✅ Require approvals: **2** (minimum)
   - ✅ Dismiss stale pull request approvals when new commits are pushed
   - ✅ Require status checks to pass before merging
     - Select all CI jobs: `lint`, `test`, `integration`, `validate`
   - ✅ Require branches to be up to date before merging
   - ✅ Do not allow bypassing the above settings

### Optional Settings

- Require conversation resolution before merging
- Require signed commits
- Require linear history

## Peer Review Process

### For Developers

1. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** and commit:
   ```bash
   git add .
   git commit -m "Description of changes"
   ```

3. **Push and create a Pull Request**:
   ```bash
   git push origin feature/your-feature-name
   ```
   Then create a PR on GitHub targeting `main`.

4. **Wait for CI to pass**: All CI jobs must pass (green checkmarks).

5. **Address review feedback**: Make requested changes and push updates.

6. **Get approvals**: Wait for 2 peer approvals from the dev team.

7. **Merge**: Once approved and CI passes, the PR can be merged.

### For Reviewers

1. **Review the code**:
   - Check code quality and style
   - Verify tests are included
   - Ensure functionality is correct
   - Check for security issues

2. **Approve or request changes**:
   - Approve if the PR is ready
   - Request changes if improvements are needed

3. **Verify CI status**: Ensure all CI checks pass before approving.

## Artifacts

### PR Approvals
- Documented in the PR conversation
- Visible in the PR's "Reviewers" section
- Required: 2 approvals minimum

### CI Logs
- Accessible from the "Actions" tab in GitHub
- Each CI run provides detailed logs
- Download artifacts if needed

## Local Development

### Running Tests Locally

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run linting
ruff check custom_components/ferbos_file_editor/
ruff format custom_components/ferbos_file_editor/

# Run unit tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=custom_components/ferbos_file_editor --cov-report=term

# Run integration tests
pytest tests/integration/ -v -m integration
```

### Pre-commit Checks

Before pushing, ensure:
- ✅ All tests pass locally
- ✅ Linting passes (`ruff check`)
- ✅ Code is formatted (`ruff format`)
- ✅ No merge conflicts with `main`

## Troubleshooting

### CI Fails on Linting
- Run `ruff check` locally and fix issues
- Run `ruff format` to auto-format code

### CI Fails on Tests
- Run `pytest tests/ -v` locally to see failures
- Ensure all tests pass before pushing

### PR Not Merging
- Check that all CI jobs are green
- Verify you have 2 approvals
- Ensure branch is up to date with `main`

## Responsibilities

- **Developers**: Create PRs, address feedback, ensure CI passes
- **Repository Maintainers**: Review PRs, approve changes, merge when ready
- **CI System**: Automatically run tests and checks on every PR

## References

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Branch Protection Rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [pytest Documentation](https://docs.pytest.org/)


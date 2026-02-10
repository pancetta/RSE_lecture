# Local CI Testing Guide

This guide explains how to run CI checks locally **before** committing and pushing code, preventing CI failures.

## Why Local CI Checks Matter

The GitHub Actions CI runs several checks on every commit:
1. **Syntax validation** - Checks Python code for syntax errors
2. **Linting (flake8)** - Checks code style and quality
3. **Notebook conversion** - Converts `.py` files to `.ipynb`
4. **Notebook execution** - Runs all notebooks to verify they work

**Running these checks locally BEFORE committing prevents CI failures and wasted time.**

## Quick Start

### Option 1: Use the Automated Script (Recommended)

Run the complete CI check suite:

```bash
# From repository root
bash scripts/local_ci_check.sh
```

This runs ALL the same checks as GitHub Actions CI.

### Option 2: Use Make Targets

```bash
# Run complete local CI check
make ci-local

# Or just run linting
make lint
```

## Manual Step-by-Step Process

If you prefer to run checks individually:

### 1. Check Python Syntax

```bash
# Check the conversion script
python -m py_compile convert_to_notebooks.py

# Check all lecture files
for lecture_file in lecture_*/lecture_*.py; do
    echo "Checking: $lecture_file"
    python -m py_compile "$lecture_file"
done
```

### 2. Run Flake8 Linting

**Critical errors first** (these will always fail CI):

```bash
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
```

**Full linting check** (checks all style rules):

```bash
flake8 . --count --statistics
```

### 3. Convert Notebooks

```bash
python convert_to_notebooks.py
```

### 4. Verify Notebooks

```bash
for lecture_file in lecture_*/lecture_*.py; do
    notebook_file="${lecture_file%.py}.ipynb"
    test -f "$notebook_file" && echo "✓ $notebook_file" || echo "✗ Missing: $notebook_file"
done
```

## Common Flake8 Errors and Fixes

### E501: Line too long

**Error:** `E501 line too long (131 > 127 characters)`

**Fix:** Break long lines at natural points:

```python
# BAD
logger.warning(f"Station {station_id} rejected: quality {data['quality']:.2f} below threshold {quality_threshold:.2f}")

# GOOD
logger.warning(
    f"Station {station_id} rejected: quality {data['quality']:.2f} "
    f"below threshold {quality_threshold:.2f}")
```

### E128: Continuation line under-indented

**Error:** `E128 continuation line under-indented for visual indent`

**Fix:** Align continuation lines properly:

```python
# BAD
cov = sum((temps_i[k] - mean_i) * (temps_j[k] - mean_j) 
         for k in range(len(temps_i)))

# GOOD
cov = sum((temps_i[k] - mean_i) * (temps_j[k] - mean_j)
          for k in range(len(temps_i)))
```

### W504: Line break after binary operator

**Error:** `W504 line break after binary operator`

**Fix:** Put operator at the start of the next line:

```python
# BAD
cov = sum((si['temps'][k] - si['mean']) * 
         (sj['temps'][k] - sj['mean'])
         for k in range(si['n']))

# GOOD
cov = sum((si['temps'][k] - si['mean']) *
          (sj['temps'][k] - sj['mean'])
          for k in range(si['n']))
```

## Flake8 Configuration

The repository uses `.flake8` configuration file with these settings:

- **Max line length:** 127 characters
- **Max complexity:** 10
- **Ignored errors:** E402, W293, W291, E302, E305, F401, F841, E226, F541 (common in notebooks)

See `.flake8` file for complete configuration.

## Pre-Commit Workflow

**Recommended workflow before every commit:**

1. Make your changes to lecture files
2. Run local CI checks:
   ```bash
   make ci-local
   ```
3. Fix any issues found
4. Run CI checks again to confirm
5. Commit and push (CI should pass!)

## Troubleshooting

### "flake8: command not found"

Install the development environment:

```bash
make install-dev
# or
micromamba env create -f environment-dev.yml -y
micromamba activate rse_lecture
```

### "No module named 'jupytext'"

Install development dependencies:

```bash
micromamba activate rse_lecture
micromamba install jupytext -c conda-forge
```

### Script won't run on Windows

Use Git Bash or WSL, or run the manual commands in PowerShell.

## Integration with Git Hooks (Optional)

To automatically run checks before every commit, create `.git/hooks/pre-commit`:

```bash
#!/bin/bash
# Auto-run CI checks before commit

echo "Running pre-commit CI checks..."
if bash scripts/local_ci_check.sh; then
    echo "✓ Pre-commit checks passed"
    exit 0
else
    echo "✗ Pre-commit checks failed"
    echo "Fix the issues above before committing"
    exit 1
fi
```

Make it executable:

```bash
chmod +x .git/hooks/pre-commit
```

Now checks run automatically before every `git commit`.

## Summary

**Always run `make ci-local` before committing to avoid CI failures!**

This saves time and keeps the CI green. 🟢

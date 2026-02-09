# Dependency Management Guide

This document describes how dependencies are managed in the RSE Lecture repository and how to handle dependency updates.

## Overview

The repository uses a **conda-only dependency management approach**:

1. **GitHub Actions**: Automatically tracked and updated by Dependabot
2. **Conda packages**: Monitored by a custom GitHub Actions workflow, manually updated

## Dependency Files

### Conda Environment Files (Single Source of Truth)

These are the **only** dependency specifications in the repository:

- **`environment.yml`** - Base dependencies for all lectures
- **`environment-dev.yml`** - Development environment (includes testing tools)
- **`lecture_0X/environment.yml`** - Lecture-specific additional dependencies

**Format**: Conda environment YAML format
**Package Manager**: micromamba or conda/mamba
**Usage**: Single source of truth for all Python and system dependencies

## Automated Dependency Tracking

### 1. Dependabot (GitHub Actions Only)

**What it does:**
- Monitors `.github/workflows/*.yml` files for GitHub Actions version updates
- Creates pull requests automatically when newer versions are available
- Runs **weekly on Mondays at 09:00 UTC**

**Configuration:** `.github/dependabot.yml`

**How to handle Dependabot PRs:**

1. Review the PR created by Dependabot
2. Check that CI tests pass
3. Review the changelog for breaking changes
4. Merge if tests pass and changes look safe
5. Close if the update is incompatible

### 2. Weekly Conda Dependency Check

**What it does:**
- Runs a GitHub Actions workflow every Monday at 09:00 UTC
- Reviews all conda environment.yml files
- Creates/updates a GitHub issue with dependency status
- Provides manual review reminders

**Configuration:** `.github/workflows/dependency-check.yml`

**How to handle the weekly issue:**

1. Review the issue created by the workflow
2. Check conda-forge for available updates to packages
3. Decide which dependencies to update
4. Follow the update process below

## Updating Dependencies

### Updating Conda/Python Dependencies

When you need to update a Python package dependency:

1. **Edit the environment.yml file:**
   ```bash
   # Example: Update numpy in base environment
   vim environment.yml
   # Change: numpy>=1.21.0
   # To:     numpy>=1.24.0
   ```

2. **Test the changes locally:**
   ```bash
   # Remove old environment
   micromamba env remove -n rse_lecture
   
   # Create fresh environment with new dependencies
   make install-dev
   micromamba activate rse_lecture
   
   # Test conversion and execution
   python convert_to_notebooks.py
   make build-website
   
   # Or run specific lecture tests
   make install-lecture4
   ```

3. **Run CI checks locally (recommended):**
   ```bash
   # Lint
   flake8 . --count --statistics
   
   # Syntax check
   python -m py_compile convert_to_notebooks.py
   
   # Test notebooks execute
   for notebook in lecture_*/*.ipynb; do
     jupyter nbconvert --to notebook --execute --inplace "$notebook"
   done
   ```

4. **Commit environment.yml:**
   ```bash
   git add environment.yml
   # Or for lecture-specific:
   git add lecture_04/environment.yml
   
   git commit -m "deps: update numpy to 1.24.0"
   git push
   ```

5. **Wait for CI to validate:**
   - CI runs on: Ubuntu, macOS 15, macOS 26, Windows
   - Must pass on all platforms before merge

### Updating GitHub Actions

Dependabot automatically creates PRs for GitHub Actions updates. Simply:

1. Review the Dependabot PR
2. Check CI passes
3. Merge if safe

## Version Pinning Strategy

### When to use `>=` (minimum version):
- For core dependencies where we want users to get latest compatible versions
- When the API is stable and backwards compatible
- Example: `numpy>=1.21.0`

### When to use `==` (exact version):
- When you need reproducible builds
- When a specific version is required for compatibility
- For production/deployment environments
- Example: `numpy==1.24.3`

### When to use `~=` (compatible release):
- When you want patch updates but not minor version changes
- Example: `numpy~=1.24.0` (allows 1.24.x but not 1.25.0)

### Current strategy:
- **Development**: Use `>=` for flexibility and forward compatibility
- **Known working versions**: Tested in CI, versions are recorded in git history
- **Security updates**: Applied promptly when vulnerabilities found
- **Conda-only**: Single package manager ensures consistent resolution across platforms

## Troubleshooting

### Dependency conflict errors

If you encounter conflicts when installing:

```bash
micromamba install ... 
# Error: Conflicts with package X
```

**Solutions:**
1. Check which package is causing the conflict
2. Try updating both packages to compatible versions
3. Consult conda-forge for compatibility matrices
4. Consider using different packages if incompatible

### CI failures after dependency update

If CI fails after updating dependencies:

1. **Check the error logs:**
   - Syntax errors → Fix code compatibility
   - Import errors → Missing dependency or incompatible version
   - Test failures → API changes in updated package

2. **Test locally on multiple platforms:**
   - Use Docker for Linux testing
   - Test on actual macOS/Windows if possible

3. **Rollback if needed:**
   ```bash
   git revert <commit-hash>
   ```

## Best Practices

1. **Test before merging**: Always run CI tests on all platforms
2. **Update regularly**: Review dependencies weekly via automated issues
3. **Document changes**: Note why specific versions were chosen in commit messages
4. **Security first**: Apply security updates promptly
5. **Conda-only**: Keep all dependencies in environment.yml files for consistency

## Useful Commands

```bash
# Check dependency versions in current environment
micromamba list

# Search for available versions
micromamba search numpy

# Show package info
micromamba info numpy

# Export exact current environment (with all resolved versions)
micromamba env export > environment-frozen.yml

# Compare environment files
diff environment.yml environment-frozen.yml
```

## Related Files

- `.github/dependabot.yml` - Dependabot configuration (GitHub Actions only)
- `.github/workflows/dependency-check.yml` - Weekly conda dependency checker
- `.github/workflows/ci.yml` - CI pipeline that tests dependencies
- `Makefile` - Build targets for installing environments

## Getting Help

- **Conda issues**: Check [conda-forge](https://conda-forge.org/)
- **Package compatibility**: Review package documentation and changelogs
- **CI failures**: Check GitHub Actions logs
- **Questions**: Open an issue in the repository

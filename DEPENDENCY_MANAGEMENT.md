# Dependency Management Guide

This document describes how dependencies are managed in the RSE Lecture repository and how to handle dependency updates.

## Overview

The repository uses a **hybrid dependency tracking approach**:

1. **GitHub Actions**: Automatically tracked and updated by Dependabot
2. **Conda/Python packages**: Monitored by a custom GitHub Actions workflow, manually updated

## Dependency Files

### Conda Environment Files (Source of Truth)

These are the authoritative dependency specifications:

- **`environment.yml`** - Base dependencies for all lectures
- **`environment-dev.yml`** - Development environment (includes testing tools)
- **`lecture_0X/environment.yml`** - Lecture-specific additional dependencies

**Format**: Conda environment YAML format
**Usage**: Primary source for creating conda/micromamba environments

### Requirements Files (Auto-Generated)

These files are automatically generated from environment.yml files:

- **`requirements.txt`** - Mirrors base environment.yml
- **`requirements-dev.txt`** - Mirrors dev environment.yml  
- **`lecture_0X/requirements.txt`** - Mirrors lecture-specific environment.yml

**Format**: pip requirements format
**Usage**: Reference only; may be used by Dependabot in the future
**Maintenance**: Run `make sync-requirements` after editing any environment.yml file

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

2. **Sync the requirements.txt files:**
   ```bash
   make sync-requirements
   ```

3. **Test the changes locally:**
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

4. **Run CI checks locally (recommended):**
   ```bash
   # Lint
   flake8 . --count --statistics
   
   # Syntax check
   python -m py_compile convert_to_notebooks.py sync_requirements.py
   
   # Test notebooks execute
   for notebook in lecture_*/*.ipynb; do
     jupyter nbconvert --to notebook --execute --inplace "$notebook"
   done
   ```

5. **Commit both environment.yml and requirements.txt:**
   ```bash
   git add environment.yml requirements.txt
   # Or for lecture-specific:
   git add lecture_04/environment.yml lecture_04/requirements.txt
   
   git commit -m "deps: update numpy to 1.24.0"
   git push
   ```

6. **Wait for CI to validate:**
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
- **Development**: Use `>=` for flexibility
- **Known working versions**: Tested in CI, versions are recorded
- **Security updates**: Applied promptly when vulnerabilities found

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

### Sync script errors

If `make sync-requirements` fails:

1. **Check environment.yml syntax:**
   ```bash
   python -c "import yaml; yaml.safe_load(open('environment.yml'))"
   ```

2. **Check for special conda syntax:**
   - The script only handles simple dependencies
   - Complex conda-specific features may not translate to pip

## Best Practices

1. **Test before merging**: Always run CI tests on all platforms
2. **Update regularly**: Review dependencies weekly via automated issues
3. **Document changes**: Note why specific versions were chosen
4. **Security first**: Apply security updates promptly
5. **Keep in sync**: Always run `make sync-requirements` after editing environment.yml
6. **Commit together**: environment.yml and requirements.txt should be committed together

## Useful Commands

```bash
# Sync requirements from environments
make sync-requirements

# Check dependency versions in current environment
micromamba list

# Search for available versions
micromamba search numpy

# Show package info
micromamba info numpy

# Export exact current environment
micromamba env export > environment-frozen.yml
```

## Related Files

- `.github/dependabot.yml` - Dependabot configuration
- `.github/workflows/dependency-check.yml` - Conda dependency checker
- `.github/workflows/ci.yml` - CI pipeline that tests dependencies
- `sync_requirements.py` - Script to sync requirements.txt files
- `Makefile` - Build targets including `sync-requirements`

## Getting Help

- **Conda issues**: Check [conda-forge](https://conda-forge.org/)
- **Package compatibility**: Review package documentation and changelogs
- **CI failures**: Check GitHub Actions logs
- **Questions**: Open an issue in the repository

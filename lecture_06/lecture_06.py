# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Lecture 6: Automation and Continuous Integration
# 
# ## Overview
# This lecture teaches you how to automate testing and ensure code quality through
# Continuous Integration (CI). We'll continue our temperature conversion story,
# setting up automated testing that would have prevented the research disaster
# from Lecture 5.
# 
# **Duration**: ~90 minutes
# 
# ## Learning Objectives
# - Understand what Continuous Integration (CI) is and why it matters
# - Set up automated testing with GitHub Actions
# - Configure CI workflows for GitLab
# - Build reproducible research pipelines
# - Automate code quality checks
# - Prevent bugs from reaching production/publication

# %% [markdown]
# ## Part 1: The Missing Piece - Automation
# 
# ### Recap: The Temperature Conversion Disaster
# 
# In Lecture 5, we learned about the climate research team that published incorrect results
# due to a bug in their temperature conversion code. We wrote tests to catch such bugs.
# 
# But there's still a problem: **tests only help if you actually run them!**
# 
# ### The Human Factor
# 
# Even with a comprehensive test suite, bugs can slip through:
# 
# - Developer forgets to run tests before committing
# - Tests run on one person's machine but not others
# - New team member doesn't know tests exist
# - Tests pass on your computer but fail on colleague's setup
# - Someone commits code late at night without testing
# - Tests exist but aren't part of the workflow
# 
# ### Enter: Continuous Integration
# 
# **Continuous Integration (CI)** automates testing every time code changes.
# 
# **How it works:**
# 1. Developer pushes code to repository (e.g., GitHub, GitLab)
# 2. CI system automatically detects the change
# 3. CI system runs all tests in a clean environment
# 4. Results are reported back (pass/fail)
# 5. Bugs are caught before they can cause harm
# 
# **Benefits:**
# - **Catch bugs early**: Before they reach main branch
# - **Consistent environment**: Same for everyone
# - **No excuses**: Tests always run
# - **Confidence**: Know code works before merging
# - **Documentation**: CI config shows how to run tests

# %% [markdown]
# ## Part 2: Introduction to GitHub Actions
# 
# ### What is GitHub Actions?
# 
# **GitHub Actions** is GitHub's built-in CI/CD platform. It's:
# - Free for public repositories
# - Free for private repos (with limits)
# - Integrated directly into GitHub
# - Uses simple YAML configuration
# - Supports multiple operating systems
# - Has a huge marketplace of pre-built actions
# 
# ### Key Concepts
# 
# - **Workflow**: Automated process (e.g., "run tests")
# - **Job**: Set of steps that run together
# - **Step**: Individual task (e.g., "install Python")
# - **Action**: Reusable unit of code
# - **Runner**: Virtual machine that executes jobs
# - **Trigger**: Event that starts workflow (e.g., push, pull request)

# %% [markdown]
# ## Part 3: Creating Your First GitHub Actions Workflow
# 
# ### Workflow File Structure
# 
# GitHub Actions workflows are defined in YAML files stored in `.github/workflows/`.
# 
# **Directory structure:**
# ```
# my_project/
# ├── .github/
# │   └── workflows/
# │       └── tests.yml       # CI workflow
# ├── src/
# │   └── temperature.py
# ├── tests/
# │   └── test_temperature.py
# └── README.md
# ```

# %% [markdown]
# ### Basic Workflow Example
# 
# Let's create a workflow that runs our temperature conversion tests:

# %%
# This represents: .github/workflows/tests.yml

basic_workflow = '''
name: Test Suite

# When to run this workflow
on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

# What to do
jobs:
  test:
    name: Run Tests
    runs-on: ubuntu-latest
    
    steps:
      # Step 1: Get the code
      - name: Check out repository
        uses: actions/checkout@v4
      
      # Step 2: Set up Python
      - name: Set up Python 3.11
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      
      # Step 3: Install dependencies
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest pytest-cov
          pip install -r requirements.txt
      
      # Step 4: Run tests
      - name: Run tests with coverage
        run: |
          pytest --cov=src --cov-report=term-missing tests/
'''

print("GitHub Actions Workflow:")
print("=" * 70)
print(basic_workflow)

# %% [markdown]
# ### Understanding the Workflow
# 
# **Triggers (`on`):**
# - `push`: Run when code is pushed to main or develop branches
# - `pull_request`: Run when PR is opened/updated targeting main
# 
# **Jobs (`jobs`):**
# - `runs-on: ubuntu-latest`: Use Ubuntu Linux virtual machine
# - Could also use `windows-latest` or `macos-latest`
# 
# **Steps:**
# - `uses`: Pre-built action from GitHub marketplace
# - `run`: Shell command to execute
# - Each step runs in sequence
# 
# **Why this prevents disasters:**
# - Tests run automatically on every push
# - Can't merge PR with failing tests
# - Same environment for all developers
# - Catches bugs before they reach main branch

# %% [markdown]
# ## Part 4: Advanced GitHub Actions Features
# 
# ### Testing on Multiple Python Versions

# %%
multi_python_workflow = '''
name: Test Suite

on: [push, pull_request]

jobs:
  test:
    name: Test Python ${{ matrix.python-version }}
    runs-on: ubuntu-latest
    
    strategy:
      matrix:
        python-version: ["3.8", "3.9", "3.10", "3.11", "3.12"]
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest pytest-cov
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
      
      - name: Run tests
        run: pytest --cov=src tests/
'''

print("Multi-Python Version Testing:")
print("=" * 70)
print(multi_python_workflow)
print("\n✓ This runs tests on 5 different Python versions!")
print("✓ Ensures compatibility across Python versions")

# %% [markdown]
# ### Testing on Multiple Operating Systems

# %%
multi_os_workflow = '''
name: Cross-Platform Tests

on: [push, pull_request]

jobs:
  test:
    name: Test on ${{ matrix.os }}
    runs-on: ${{ matrix.os }}
    
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        python-version: ["3.11"]
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest pytest-cov
          pip install -r requirements.txt
      
      - name: Run tests
        run: pytest --cov=src tests/
'''

print("Cross-Platform Testing:")
print("=" * 70)
print(multi_os_workflow)
print("\n✓ Tests on Linux, Windows, and macOS")
print("✓ Catches platform-specific bugs")

# %% [markdown]
# ### Code Quality Checks

# %%
quality_workflow = '''
name: Code Quality

on: [push, pull_request]

jobs:
  lint:
    name: Lint with flake8
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      
      - name: Install linting tools
        run: |
          python -m pip install --upgrade pip
          pip install flake8 black
      
      - name: Check code style with black
        run: black --check src/ tests/
      
      - name: Lint with flake8
        run: |
          # Stop build if there are Python syntax errors or undefined names
          flake8 src/ tests/ --count --select=E9,F63,F7,F82 --show-source --statistics
          # Exit-zero treats all errors as warnings
          flake8 src/ tests/ --count --exit-zero --max-complexity=10 --max-line-length=100 --statistics
  
  test:
    name: Run tests
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest pytest-cov
          pip install -r requirements.txt
      
      - name: Run tests with coverage
        run: |
          pytest --cov=src --cov-report=xml --cov-report=term tests/
      
      - name: Check coverage threshold
        run: |
          coverage report --fail-under=80
'''

print("Code Quality Workflow:")
print("=" * 70)
print(quality_workflow)
print("\n✓ Checks code formatting with black")
print("✓ Lints code with flake8")
print("✓ Ensures 80% test coverage")
print("✓ Fails build if quality standards not met")

# %% [markdown]
# ## Part 5: Complete Example - Temperature Project CI
# 
# ### Full Production-Ready Workflow

# %%
complete_workflow = '''
name: Temperature Module CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  # Job 1: Code Quality Checks
  quality:
    name: Code Quality
    runs-on: ubuntu-latest
    
    steps:
      - name: Check out code
        uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      
      - name: Install tools
        run: |
          python -m pip install --upgrade pip
          pip install flake8 black isort
      
      - name: Check import sorting
        run: isort --check-only src/ tests/
      
      - name: Check code formatting
        run: black --check src/ tests/
      
      - name: Lint code
        run: flake8 src/ tests/ --max-line-length=100
  
  # Job 2: Run Tests
  test:
    name: Test Suite
    runs-on: ${{ matrix.os }}
    
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        python-version: ["3.9", "3.10", "3.11", "3.12"]
    
    steps:
      - name: Check out code
        uses: actions/checkout@v4
      
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest pytest-cov
          pip install -r requirements.txt
      
      - name: Run unit tests
        run: |
          pytest tests/ -v --cov=src --cov-report=xml --cov-report=term-missing
      
      - name: Upload coverage to Codecov
        if: matrix.os == 'ubuntu-latest' && matrix.python-version == '3.11'
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml
          fail_ci_if_error: true
  
  # Job 3: Build and validate package
  build:
    name: Build Package
    runs-on: ubuntu-latest
    needs: [quality, test]
    
    steps:
      - name: Check out code
        uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      
      - name: Install build tools
        run: |
          python -m pip install --upgrade pip
          pip install build twine
      
      - name: Build package
        run: python -m build
      
      - name: Check package
        run: twine check dist/*
'''

print("Complete Production CI Workflow:")
print("=" * 70)
print(complete_workflow)
print("\n✅ Multiple jobs running in parallel")
print("✅ Tests on 4 Python versions × 3 operating systems = 12 configurations")
print("✅ Code quality enforced")
print("✅ Coverage tracking with Codecov")
print("✅ Package build validation")

# %% [markdown]
# ## Part 6: GitHub Actions for Research Projects
# 
# ### Research-Specific Workflow

# %%
research_workflow = '''
name: Research Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
  schedule:
    # Run nightly at 2 AM UTC
    - cron: '0 2 * * *'

jobs:
  test-analysis:
    name: Test Analysis Code
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      
      - name: Install scientific stack
        run: |
          python -m pip install --upgrade pip
          pip install pytest numpy pandas matplotlib scipy
      
      - name: Run analysis tests
        run: pytest tests/test_analysis.py -v
  
  test-notebooks:
    name: Test Jupyter Notebooks
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install jupyter nbconvert nbformat numpy pandas matplotlib
      
      - name: Execute notebooks
        run: |
          jupyter nbconvert --to notebook --execute \
            notebooks/*.ipynb --output-dir=/tmp/executed_notebooks/
  
  validate-data:
    name: Validate Data Quality
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      
      - name: Install dependencies
        run: |
          pip install pandas great-expectations
      
      - name: Run data validation
        run: python scripts/validate_data.py
  
  reproducibility-check:
    name: Reproducibility Check
    runs-on: ubuntu-latest
    needs: [test-analysis, test-notebooks]
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      
      - name: Run full analysis pipeline
        run: bash scripts/run_analysis.sh
      
      - name: Compare with expected results
        run: python scripts/compare_results.py
      
      - name: Archive results
        uses: actions/upload-artifact@v3
        with:
          name: analysis-results
          path: results/
'''

print("Research-Specific CI Workflow:")
print("=" * 70)
print(research_workflow)
print("\n✅ Tests analysis code")
print("✅ Executes and validates Jupyter notebooks")
print("✅ Validates data quality")
print("✅ Checks reproducibility of results")
print("✅ Runs nightly to catch data issues")
print("✅ Archives results for comparison")

# %% [markdown]
# ## Part 7: GitLab CI/CD
# 
# ### Introduction to GitLab CI
# 
# **GitLab CI** is GitLab's built-in CI/CD platform. It's similar to GitHub Actions but:
# - Uses `.gitlab-ci.yml` instead of `.github/workflows/*.yml`
# - Different syntax and structure
# - Can be self-hosted (important for sensitive research data)
# - Free for public and private repositories
# 
# ### Why Learn Both?
# 
# - Many universities host GitLab internally
# - Some research institutions require on-premise hosting
# - Some projects use GitHub, others use GitLab
# - Concepts transfer between platforms

# %% [markdown]
# ### GitLab CI File Structure
# 
# GitLab CI workflows are defined in a single `.gitlab-ci.yml` file at the repository root.
# 
# **Directory structure:**
# ```
# my_project/
# ├── .gitlab-ci.yml      # CI configuration
# ├── src/
# │   └── temperature.py
# ├── tests/
# │   └── test_temperature.py
# └── README.md
# ```

# %% [markdown]
# ### Basic GitLab CI Example

# %%
gitlab_basic = '''
# GitLab CI configuration for temperature module

# Define pipeline stages
stages:
  - test
  - quality
  - build

# Default settings for all jobs
default:
  image: python:3.11
  before_script:
    - python -m pip install --upgrade pip
    - pip install pytest pytest-cov

# Job: Run tests
test:
  stage: test
  script:
    - pip install -r requirements.txt
    - pytest --cov=src --cov-report=term tests/
  coverage: '/(?i)total.*? (100(?:\\.0+)?\\%|[1-9]?\\d(?:\\.\\d+)?\\%)$/'

# Job: Code quality check
lint:
  stage: quality
  before_script:
    - pip install flake8 black
  script:
    - black --check src/ tests/
    - flake8 src/ tests/ --max-line-length=100

# Job: Build package
build:
  stage: build
  before_script:
    - pip install build
  script:
    - python -m build
  artifacts:
    paths:
      - dist/
'''

print("GitLab CI Configuration:")
print("=" * 70)
print(gitlab_basic)

# %% [markdown]
# ### Key Differences: GitLab vs GitHub Actions
# 
# | Feature | GitHub Actions | GitLab CI |
# |---------|---------------|-----------|
# | Config file | `.github/workflows/*.yml` | `.gitlab-ci.yml` |
# | Structure | Workflows → Jobs → Steps | Stages → Jobs |
# | Docker | Optional | Default |
# | Marketplace | Yes (actions) | No (but has includes) |
# | Self-hosted | Yes (runners) | Yes (runners) |
# | Matrix builds | Built-in | Via parallel keyword |

# %% [markdown]
# ### Advanced GitLab CI Features

# %%
gitlab_advanced = '''
# Advanced GitLab CI configuration

stages:
  - quality
  - test
  - deploy

# Variables available to all jobs
variables:
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"

# Cache pip packages
cache:
  paths:
    - .cache/pip

# Template for Python jobs
.python-job:
  image: python:3.11
  before_script:
    - python -m pip install --upgrade pip
    - pip install pytest pytest-cov

# Code quality job
code-quality:
  extends: .python-job
  stage: quality
  before_script:
    - pip install flake8 black isort
  script:
    - isort --check-only src/ tests/
    - black --check src/ tests/
    - flake8 src/ tests/ --max-line-length=100
  allow_failure: false

# Test on multiple Python versions
.test-template:
  extends: .python-job
  stage: test
  script:
    - pip install -r requirements.txt
    - pytest --cov=src --cov-report=term --cov-report=xml tests/
  coverage: '/(?i)total.*? (100(?:\\.0+)?\\%|[1-9]?\\d(?:\\.\\d+)?\\%)$/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage.xml

# Matrix: Test on Python 3.9, 3.10, 3.11, 3.12
test-python-3.9:
  extends: .test-template
  image: python:3.9

test-python-3.10:
  extends: .test-template
  image: python:3.10

test-python-3.11:
  extends: .test-template
  image: python:3.11

test-python-3.12:
  extends: .test-template
  image: python:3.12

# Deploy documentation (only on main branch)
pages:
  stage: deploy
  image: python:3.11
  script:
    - pip install sphinx sphinx-rtd-theme
    - cd docs && make html
    - mv _build/html ../public
  artifacts:
    paths:
      - public
  only:
    - main
'''

print("Advanced GitLab CI Configuration:")
print("=" * 70)
print(gitlab_advanced)
print("\n✅ Job templates (.python-job)")
print("✅ Caching for faster builds")
print("✅ Multiple Python versions")
print("✅ Coverage reports")
print("✅ Conditional deployment")

# %% [markdown]
# ### Research-Specific GitLab CI

# %%
gitlab_research = '''
# GitLab CI for research projects

stages:
  - quality
  - test
  - analysis
  - report

variables:
  DATA_DIR: "/data/shared"  # Mount point for research data

# Quality checks
code-quality:
  stage: quality
  image: python:3.11
  script:
    - pip install flake8
    - flake8 src/ --max-line-length=100

# Unit tests
unit-tests:
  stage: test
  image: python:3.11
  script:
    - pip install pytest pytest-cov numpy pandas
    - pytest tests/unit/ -v --cov=src
  coverage: '/TOTAL.*? (100(?:\\.0+)?\\%|[1-9]?\\d(?:\\.\\d+)?\\%)$/'

# Integration tests (may need real data)
integration-tests:
  stage: test
  image: python:3.11
  script:
    - pip install pytest numpy pandas scipy matplotlib
    - pytest tests/integration/ -v
  only:
    - main
    - develop

# Run full analysis pipeline
run-analysis:
  stage: analysis
  image: python:3.11
  script:
    - pip install -r requirements.txt
    - python scripts/run_analysis.py --data-dir $DATA_DIR
  artifacts:
    paths:
      - results/
    expire_in: 30 days
  only:
    - main

# Generate report
generate-report:
  stage: report
  image: python:3.11
  dependencies:
    - run-analysis
  script:
    - pip install jupyter nbconvert
    - jupyter nbconvert --to html --execute notebooks/report.ipynb
  artifacts:
    paths:
      - notebooks/report.html
    expire_in: 1 year
  only:
    - main

# Nightly reproducibility check
nightly-check:
  stage: analysis
  image: python:3.11
  script:
    - pip install -r requirements.txt
    - python scripts/run_analysis.py --data-dir $DATA_DIR
    - python scripts/compare_with_baseline.py
  only:
    - schedules
'''

print("Research-Specific GitLab CI:")
print("=" * 70)
print(gitlab_research)
print("\n✅ Separate unit and integration tests")
print("✅ Full analysis pipeline")
print("✅ Automated report generation")
print("✅ Scheduled reproducibility checks")
print("✅ Artifact preservation")

# %% [markdown]
# ## Part 8: CI Best Practices for Research
# 
# ### 1. Start Simple, Add Gradually
# 
# **Phase 1: Basic testing**
# ```yaml
# - Run pytest on every push
# ```
# 
# **Phase 2: Add quality checks**
# ```yaml
# - Add linting
# - Add coverage requirements
# ```
# 
# **Phase 3: Multi-platform**
# ```yaml
# - Test on different OS
# - Test on different Python versions
# ```
# 
# **Phase 4: Advanced**
# ```yaml
# - Test notebooks
# - Validate data
# - Check reproducibility
# ```

# %% [markdown]
# ### 2. Make Tests Fast
# 
# Slow tests discourage running CI frequently.
# 
# **Strategies:**
# - Use small test datasets
# - Mock expensive operations
# - Run heavy tests only on main branch
# - Use parallel execution
# - Cache dependencies
# 
# **Example timing:**

# %%
test_timing_example = '''
# Fast tests (run on every commit)
fast-tests:
  stage: test
  script:
    - pytest tests/unit/ -v  # < 1 minute
  
# Slow tests (run only on main/PR)
integration-tests:
  stage: test
  script:
    - pytest tests/integration/ -v  # 5-10 minutes
  only:
    - main
    - merge_requests

# Very slow tests (run nightly)
full-analysis:
  stage: test
  script:
    - bash scripts/run_full_analysis.sh  # 1+ hours
  only:
    - schedules
'''

print("Test Timing Strategy:")
print("=" * 70)
print(test_timing_example)

# %% [markdown]
# ### 3. Protect Important Branches
# 
# **GitHub:**
# 1. Settings → Branches → Branch protection rules
# 2. Require status checks to pass before merging
# 3. Require pull request reviews
# 4. Require branches to be up to date
# 
# **GitLab:**
# 1. Settings → Repository → Protected branches
# 2. Allowed to merge: Maintainers
# 3. Require CI to pass
# 4. Require approval from code owners
# 
# This ensures:
# ✅ No untested code reaches main  
# ✅ All changes reviewed  
# ✅ Tests pass before merge  
# ✅ Main branch always in good state  

# %% [markdown]
# ### 4. Use Status Badges
# 
# Show CI status in your README:
# 
# **GitHub Actions:**
# ```markdown
# ![Tests](https://github.com/username/repo/workflows/Tests/badge.svg)
# ```
# 
# **GitLab CI:**
# ```markdown
# ![Pipeline](https://gitlab.com/username/repo/badges/main/pipeline.svg)
# ![Coverage](https://gitlab.com/username/repo/badges/main/coverage.svg)
# ```
# 
# Benefits:
# - Immediate visibility of project health
# - Shows you care about quality
# - Builds trust in your research code

# %% [markdown]
# ### 5. Monitor and Maintain
# 
# CI requires ongoing maintenance:
# 
# - **Update dependencies**: Keep actions/images current
# - **Fix flaky tests**: Tests that randomly fail
# - **Optimize speed**: As test suite grows
# - **Review failures**: Don't ignore failing tests
# - **Update for new Python versions**: As they release

# %% [markdown]
# ## Part 9: Putting It All Together - Complete Example
# 
# ### The Temperature Project - Fully Automated
# 
# Let's see how CI would have prevented our Lecture 5 disaster:

# %%
complete_example = '''
# GitHub Actions workflow: .github/workflows/ci.yml
name: Temperature Module CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    name: Test Suite
    runs-on: ubuntu-latest
    
    steps:
      - name: Check out code
        uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest pytest-cov
      
      - name: Run tests
        run: |
          pytest tests/ -v --cov=src --cov-report=term-missing
      
      - name: Ensure minimum coverage
        run: |
          coverage report --fail-under=80

# Requirements file: requirements.txt
# (empty for this simple project)

# Test file: tests/test_temperature.py
"""
import pytest

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

class TestTemperatureConversion:
    def test_celsius_to_fahrenheit_freezing(self):
        assert celsius_to_fahrenheit(0) == 32
    
    def test_celsius_to_fahrenheit_boiling(self):
        assert celsius_to_fahrenheit(100) == 212
    
    def test_fahrenheit_to_celsius_freezing(self):
        assert fahrenheit_to_celsius(32) == 0
    
    def test_fahrenheit_to_celsius_boiling(self):
        assert fahrenheit_to_celsius(212) == 100
    
    def test_roundtrip_conversion(self):
        for temp in [-40, 0, 37, 100]:
            f = celsius_to_fahrenheit(temp)
            c = fahrenheit_to_celsius(f)
            assert abs(c - temp) < 0.01
"""
'''

print("Complete Automated Temperature Project:")
print("=" * 70)
print(complete_example)
print("\n✅ Tests run automatically on every push")
print("✅ Tests run on every pull request")
print("✅ Requires 80% coverage")
print("✅ Any bug in conversion would be caught immediately")
print("✅ Could NOT publish with broken code")

# %% [markdown]
# ### How CI Prevents Disasters
# 
# **Without CI (Lecture 5 scenario):**
# 1. Developer writes buggy `fahrenheit_to_celsius`
# 2. Forgets to write/run tests
# 3. Commits and pushes code
# 4. Bug makes it to production
# 5. Incorrect results published
# 6. Paper retracted months later
# 
# **With CI:**
# 1. Developer writes buggy `fahrenheit_to_celsius`
# 2. Pushes code to GitHub
# 3. CI automatically runs tests
# 4. Tests FAIL (bug detected!)
# 5. Pull request blocked from merging
# 6. Developer fixes bug before it causes harm
# 
# **Result:** Crisis averted! ✅

# %% [markdown]
# ## Part 10: Setting Up CI for Your Research Project
# 
# ### Step-by-Step Guide
# 
# **For GitHub:**
# 
# 1. **Create workflow file:**
#    ```bash
#    mkdir -p .github/workflows
#    touch .github/workflows/tests.yml
#    ```
# 
# 2. **Add basic workflow** (from examples above)
# 
# 3. **Add test requirements** to `requirements.txt`
# 
# 4. **Commit and push:**
#    ```bash
#    git add .github/workflows/tests.yml
#    git commit -m "Add CI workflow"
#    git push
#    ```
# 
# 5. **Check workflow runs:**
#    - Go to GitHub → Actions tab
#    - See workflow running
#    - View results
# 
# 6. **Enable branch protection:**
#    - Settings → Branches
#    - Add rule for `main`
#    - Require status checks
# 
# **For GitLab:**
# 
# 1. **Create CI file:**
#    ```bash
#    touch .gitlab-ci.yml
#    ```
# 
# 2. **Add configuration** (from examples above)
# 
# 3. **Commit and push:**
#    ```bash
#    git add .gitlab-ci.yml
#    git commit -m "Add GitLab CI"
#    git push
#    ```
# 
# 4. **Check pipeline:**
#    - Go to CI/CD → Pipelines
#    - View pipeline execution
# 
# 5. **Protect branches:**
#    - Settings → Repository → Protected branches

# %% [markdown]
# ### Common Issues and Solutions

# %%
common_issues = '''
# Issue 1: Tests pass locally but fail in CI
Cause: Different environment
Solution: Use same Python version, pin dependencies

# Issue 2: Slow CI runs
Cause: Installing heavy dependencies
Solution: Use caching, split into fast/slow tests

# Issue 3: Flaky tests
Cause: Tests depend on random values, timing, or external services
Solution: Set random seeds, mock external calls, increase timeouts

# Issue 4: Merge conflicts in workflow files
Cause: Multiple people editing CI config
Solution: Keep workflow simple, use templates, communicate

# Issue 5: Secrets in logs
Cause: Printing environment variables
Solution: Use GitHub/GitLab secrets, mask sensitive data

# Issue 6: Coverage dropping
Cause: New code not tested
Solution: Enforce coverage threshold, review PRs carefully
'''

print("Common CI Issues and Solutions:")
print("=" * 70)
print(common_issues)

# %% [markdown]
# ## Summary: What We Learned
# 
# ### From Testing to Automation
# 
# **Lecture 5 taught us:**
# - Why testing is critical
# - How to write tests with pytest
# - Test-driven development
# - Measuring coverage
# 
# **Lecture 6 added:**
# - Automating tests with CI
# - GitHub Actions configuration
# - GitLab CI configuration
# - Research-specific pipelines
# - Best practices for CI
# 
# ### The Complete Picture
# 
# ```
# Developer writes code
#        ↓
# Writes tests (TDD)
#        ↓
# Commits and pushes
#        ↓
# CI automatically runs tests
#        ↓
# Tests pass → Code can merge
# Tests fail → Bug caught, fix required
#        ↓
# Code merged to main
#        ↓
# CI runs full analysis
#        ↓
# Results validated
#        ↓
# Research published with confidence!
# ```

# %% [markdown]
# ### Key Takeaways
# 
# ✅ **CI automates testing** - No human intervention needed  
# ✅ **Catches bugs early** - Before they cause problems  
# ✅ **Consistent environment** - Same for everyone  
# ✅ **Builds confidence** - Know your code works  
# ✅ **Enables collaboration** - Safe to accept contributions  
# ✅ **Prevents disasters** - Like our temperature conversion story  
# ✅ **Works for research** - Can test data, notebooks, pipelines  
# ✅ **Platform agnostic** - GitHub, GitLab, others all support CI  
# 
# ### Best Practices Checklist
# 
# - ✅ Set up CI from day 1 of project
# - ✅ Run tests on every push and pull request
# - ✅ Test on multiple Python versions (if applicable)
# - ✅ Test on multiple OS (if cross-platform)
# - ✅ Enforce code quality (linting, formatting)
# - ✅ Require minimum test coverage
# - ✅ Protect main branch - require passing tests
# - ✅ Add status badges to README
# - ✅ Keep tests fast
# - ✅ Monitor and maintain CI configuration

# %% [markdown]
# ### Resources
# 
# **GitHub Actions:**
# - [GitHub Actions Documentation](https://docs.github.com/en/actions)
# - [GitHub Actions Marketplace](https://github.com/marketplace?type=actions)
# - [Awesome Actions](https://github.com/sdras/awesome-actions)
# 
# **GitLab CI:**
# - [GitLab CI/CD Documentation](https://docs.gitlab.com/ee/ci/)
# - [GitLab CI/CD Examples](https://docs.gitlab.com/ee/ci/examples/)
# 
# **Testing:**
# - [pytest Documentation](https://docs.pytest.org/)
# - [pytest-cov Documentation](https://pytest-cov.readthedocs.io/)
# - [Codecov](https://codecov.io/) - Coverage tracking service
# 
# **Research Software:**
# - [The Turing Way - Testing](https://the-turing-way.netlify.app/reproducible-research/testing.html)
# - [Best Practices for Scientific Computing](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745)

# %% [markdown]
# ### Final Thoughts
# 
# Remember our cautionary tale from Lecture 5?
# 
# The climate research team's paper was retracted because:
# - ❌ No tests were written
# - ❌ No CI to run tests automatically
# - ❌ Bug went undetected for months
# - ❌ Results published without validation
# 
# With what you learned in Lectures 5 and 6:
# - ✅ Tests would have caught the bug
# - ✅ CI would have prevented merging
# - ✅ Bug would never reach publication
# - ✅ Research would be trustworthy
# 
# **Your research deserves better than to become a cautionary tale.**
# 
# **Test your code. Automate your testing. Publish with confidence.**
# 
# ### Next Steps in Your RSE Journey
# 
# You now have the foundation to:
# 1. Write reliable, tested research software
# 2. Set up automated quality checks
# 3. Collaborate safely with confidence
# 4. Publish reproducible research
# 
# Continue learning:
# - Advanced testing strategies (mocking, fixtures, parametrization)
# - Deployment and packaging
# - Documentation generation
# - Performance optimization
# - Reproducible environments (Docker, conda)
# 
# Most importantly: **Apply what you've learned to your research!**

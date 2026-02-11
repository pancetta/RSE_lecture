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
# 
# ## Quick Access
# 
# Scan the QR codes below for quick access to course materials:
# 
# <div style="display: flex; gap: 20px; align-items: flex-start;">
#   <div style="text-align: center;">
#     <img src="../course_qr_code.png" alt="Course Website QR Code" width="150"/>
#     <p><strong>Course Website</strong></p>
#   </div>
#   <div style="text-align: center;">
#     <img src="lecture_06_qr_code.png" alt="This Lecture QR Code" width="150"/>
#     <p><strong>This Lecture</strong></p>
#   </div>
# </div>
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
# This seems obvious, but it's the Achilles' heel of testing. You can have a perfect test suite 
# with 100% coverage, but if someone forgets to run the tests before committing code, bugs still 
# slip through. Manual processes fail eventually—someone gets busy, forgets, or assumes their 
# small change "couldn't possibly break anything."
# 
# ### The Human Factor
# 
# Even with a comprehensive test suite, bugs can slip through when testing isn't automated:
# 
# - **Developer forgets to run tests before committing**: Happens more often than you'd think
# - **Tests run on one person's machine but not others**: "Works on my machine" syndrome
# - **New team member doesn't know tests exist**: No documentation or onboarding
# - **Tests pass on your computer but fail on colleague's setup**: Environment differences
# - **Someone commits code late at night without testing**: Tired developer, honest mistake
# - **Tests exist but aren't part of the workflow**: No one remembers to run them regularly
# 
# **The fundamental problem**: Relying on humans to remember manual steps doesn't scale. We're 
# forgetful, we get busy, we take shortcuts. The solution is to remove humans from the loop—
# automate testing so it happens every time, without exception.
# 
# ### Enter: Continuous Integration
# 
# **Continuous Integration (CI)** automates testing every time code changes. It's a practice where 
# developers integrate their work frequently (daily or more), and each integration is verified by 
# an automated build and test process. This catches problems early, when they're easiest to fix.
# 
# **How it works:**
# 1. Developer pushes code to repository (e.g., GitHub, GitLab)
# 2. CI system automatically detects the change—no human intervention needed
# 3. CI system runs all tests in a clean, reproducible environment
# 4. Results are reported back (pass/fail) within minutes
# 5. Bugs are caught before they can cause harm or reach other developers
# 
# **Benefits:**
# - **Catch bugs early**: Before they reach main branch and affect others
# - **Consistent environment**: Same for everyone—no more "works on my machine"
# - **No excuses**: Tests always run—can't forget or skip them
# - **Confidence**: Know code works before merging—sleep better at night
# - **Documentation**: CI config shows exactly how to run tests—reproducible by anyone
# - **Faster feedback**: Know within minutes if your change broke something

# %%
# Visualize the CI Pipeline workflow
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

fig, ax = plt.subplots(figsize=(14, 7))
ax.set_xlim(0, 14)
ax.set_ylim(0, 8)
ax.axis('off')

# Title
ax.text(7, 7.5, 'Continuous Integration Pipeline', ha='center',
        fontsize=16, fontweight='bold')

# Step 1: Developer pushes code
dev_box = FancyBboxPatch((0.5, 4.5), 2, 2,
                         boxstyle="round,pad=0.1",
                         edgecolor='#1976d2', linewidth=2,
                         facecolor='#e3f2fd')
ax.add_patch(dev_box)
ax.text(1.5, 5.8, '👨‍💻 Developer', ha='center', fontsize=11, fontweight='bold')
ax.text(1.5, 5.3, 'Pushes Code', ha='center', fontsize=10)
ax.text(1.5, 4.9, 'to GitHub', ha='center', fontsize=9, style='italic')

# Step 2: CI Triggered
trigger_circle = Circle((4.5, 5.5), 0.4, color='#ff9800', zorder=3)
ax.add_patch(trigger_circle)
ax.text(4.5, 5.5, '⚡', ha='center', va='center', fontsize=20)
ax.text(4.5, 4.3, 'Trigger', ha='center', fontsize=9, fontweight='bold')
ax.text(4.5, 3.9, 'Automatic', ha='center', fontsize=8, style='italic')

# Step 3: CI System runs tests
ci_box = FancyBboxPatch((6, 4), 3, 3,
                        boxstyle="round,pad=0.1",
                        edgecolor='#388e3c', linewidth=3,
                        facecolor='#e8f5e9')
ax.add_patch(ci_box)
ax.text(7.5, 6.5, '🤖 CI System', ha='center', fontsize=11, fontweight='bold')
ax.text(7.5, 6, 'Clean Environment', ha='center', fontsize=9, color='#555')

# Sub-steps within CI
substeps = [
    {'y': 5.4, 'text': '1. Checkout code', 'icon': '📥'},
    {'y': 4.9, 'text': '2. Install dependencies', 'icon': '📦'},
    {'y': 4.4, 'text': '3. Run all tests', 'icon': '🧪'},
]
for step in substeps:
    ax.text(6.3, step['y'], step['icon'], ha='left', fontsize=10)
    ax.text(6.7, step['y'], step['text'], ha='left', va='center', fontsize=8)

# Step 4: Results
pass_box = FancyBboxPatch((10.5, 5.5), 2.2, 1.2,
                          boxstyle="round,pad=0.08",
                          edgecolor='#2e7d32', linewidth=2,
                          facecolor='#c8e6c9')
ax.add_patch(pass_box)
ax.text(11.6, 6.3, '✅ PASS', ha='center', fontsize=11,
        fontweight='bold', color='#1b5e20')
ax.text(11.6, 5.9, 'Tests succeeded', ha='center', fontsize=8)

fail_box = FancyBboxPatch((10.5, 3.5), 2.2, 1.2,
                          boxstyle="round,pad=0.08",
                          edgecolor='#c62828', linewidth=2,
                          facecolor='#ffcdd2')
ax.add_patch(fail_box)
ax.text(11.6, 4.3, '❌ FAIL', ha='center', fontsize=11,
        fontweight='bold', color='#b71c1c')
ax.text(11.6, 3.9, 'Tests failed', ha='center', fontsize=8)

# Arrows
# Developer to Trigger
arrow1 = FancyArrowPatch((2.5, 5.5), (4.0, 5.5),
                         arrowstyle='->', mutation_scale=20,
                         linewidth=2, color='#333')
ax.add_patch(arrow1)
ax.text(3.25, 5.8, 'git push', ha='center', fontsize=8,
        style='italic', color='#666')

# Trigger to CI
arrow2 = FancyArrowPatch((5.0, 5.5), (6.0, 5.5),
                         arrowstyle='->', mutation_scale=20,
                         linewidth=2, color='#333')
ax.add_patch(arrow2)

# CI to Pass
arrow3 = FancyArrowPatch((9.0, 6.0), (10.5, 6.1),
                         arrowstyle='->', mutation_scale=20,
                         linewidth=2, color='#2e7d32')
ax.add_patch(arrow3)

# CI to Fail
arrow4 = FancyArrowPatch((9.0, 5.0), (10.5, 4.1),
                         arrowstyle='->', mutation_scale=20,
                         linewidth=2, color='#c62828')
ax.add_patch(arrow4)

# Feedback loop
feedback_arrow = FancyArrowPatch((10.5, 3.5), (2.5, 4.5),
                                 arrowstyle='->', mutation_scale=15,
                                 linewidth=1.5, color='#c62828',
                                 linestyle='dashed',
                                 connectionstyle="arc3,rad=-.3")
ax.add_patch(feedback_arrow)
ax.text(6, 2.5, 'Fix bugs & push again', ha='center', fontsize=9,
        style='italic', color='#c62828')

# Timeline annotation
ax.text(7, 1.5, '⏱️ Entire process: 2-5 minutes (fully automated)',
        ha='center', fontsize=10, color='#1976d2',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#e3f2fd',
                  edgecolor='#1976d2', linewidth=2))

# Benefits box
ax.text(7, 0.5, '✨ No manual testing • Consistent results • Immediate feedback',
        ha='center', fontsize=9, color='#555',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#f5f5f5',
                  edgecolor='#999'))

plt.tight_layout()
plt.show()

# %% [markdown]
# The diagram above shows the complete CI workflow:
# 
# 1. **Developer pushes code** → Commits and pushes changes to GitHub
# 2. **CI automatically triggers** → No manual intervention needed
# 3. **CI system runs tests** → In a clean, reproducible environment
#    - Checks out code
#    - Installs dependencies
#    - Runs entire test suite
# 4. **Results reported** → Pass ✅ or Fail ❌
# 5. **Feedback loop** → If tests fail, fix and repeat
# 
# The entire process takes just minutes and happens automatically every time code
# changes. This ensures bugs are caught immediately, before they can affect others!
# 
# **Research context**: For research software, CI is crucial for reproducibility. Your CI configuration 
# documents exactly how to build and test your code, making it easy for reviewers and other researchers 
# to verify your results. Many journals now require CI badges showing tests pass.

# %% [markdown]
# ## Part 2: Introduction to GitHub Actions
# 
# ### What is GitHub Actions?
# 
# **GitHub Actions** is GitHub's built-in CI/CD platform. Unlike earlier CI systems that required 
# separate services (like Travis CI or CircleCI), GitHub Actions is integrated directly into GitHub, 
# making it incredibly convenient.
# 
# **GitHub Actions** is:
# - **Free for public repositories**: Unlimited minutes for open-source projects
# - **Free for private repos (with limits)**: 2000 minutes/month on free tier
# - **Integrated directly into GitHub**: No third-party accounts needed
# - **Uses simple YAML configuration**: Human-readable, version-controlled with your code
# - **Supports multiple operating systems**: Linux, Windows, macOS—test on all platforms
# - **Has a huge marketplace of pre-built actions**: Don't reinvent the wheel
# 
# **When to use GitHub Actions vs. other CI systems**: For most projects hosted on GitHub, GitHub 
# Actions is the easiest choice. Use alternatives like GitLab CI if you're on GitLab, Jenkins for 
# self-hosted enterprise systems, or CircleCI/Travis if you need features GitHub Actions doesn't 
# provide yet.
# 
# ### Key Concepts
# 
# Understanding these terms helps you read and write GitHub Actions workflows:
# 
# - **Workflow**: An automated process (e.g., "run tests")—the whole CI pipeline
# - **Job**: Set of steps that run together on the same machine—can run multiple jobs in parallel
# - **Step**: Individual task (e.g., "install Python")—the smallest unit of work
# - **Action**: Reusable unit of code—like a function you can call in your workflow
# - **Runner**: Virtual machine that executes jobs—GitHub provides these, or you can host your own
# - **Trigger**: Event that starts workflow (e.g., push, pull request)—defines when CI runs
# 
# **Mental model**: Think of a workflow as a script, jobs as functions in that script (that can run 
# in parallel), and steps as individual commands. Triggers are like "when should this script run?" 
# and runners are the computers that execute it.

# %% [markdown]
# <div style="background-color: #f3e5f5; border-left: 5px solid #9c27b0; padding: 15px; margin: 10px 0; border-radius: 5px;">
#     <h4 style="color: #7b1fa2; margin-top: 0;">💡 Try It Yourself</h4>
#     <p>CI/CD transforms how you work—automation prevents disasters!</p>
#     <ul>
#         <li><strong>Set up your first workflow:</strong> Create a
#         .github/workflows/tests.yml file for one of your projects that runs pytest on
#         every push—watch it catch bugs automatically.</li>
#         <li><strong>Add multiple triggers:</strong> Configure your workflow to run on push,
#         pull_request, and schedule (daily at midnight)—ensure your code stays healthy even
#         when you're not actively developing.</li>
#         <li><strong>Experiment with matrix testing:</strong> Test your code across Python
#         3.8, 3.9, 3.10, 3.11, and multiple operating systems (Ubuntu, macOS,
#         Windows)—discover platform-specific bugs before users do.</li>
#     </ul>
# </div>

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
# Let's break down each part of the workflow to understand what it does and why:
# 
# **Triggers (`on`):**
# - `push`: Run when code is pushed to main or develop branches—catches bugs in merged code
# - `pull_request`: Run when PR is opened/updated targeting main—prevents bugs from being merged
# 
# **Jobs (`jobs`):**
# - `runs-on: ubuntu-latest`: Use Ubuntu Linux virtual machine—most common, fastest
# - Could also use `windows-latest` or `macos-latest`—useful for cross-platform testing
# 
# **Steps:**
# - `uses`: Pre-built action from GitHub marketplace—tested, maintained code you can trust
# - `run`: Shell command to execute—anything you'd type in terminal
# - Each step runs in sequence—if one fails, the job fails
# 
# **Why this prevents disasters:**
# - Tests run automatically on every push—no way to forget
# - Can't merge PR with failing tests—GitHub shows red X, reviewers see it
# - Same environment for all developers—no "works on my machine" excuses
# - Catches bugs before they reach main branch—main stays stable and deployable
# 
# **Common pitfall**: Forgetting to make tests a required check before merging. In your repository 
# settings, enable "Require status checks to pass before merging" to enforce that CI must pass.

# %% [markdown]
# <div style="background-color: #f3e5f5; border-left: 5px solid #9c27b0; padding: 15px; margin: 10px 0; border-radius: 5px;">
#     <h4 style="color: #7b1fa2; margin-top: 0;">💡 Try It Yourself</h4>
#     <p>Advanced workflows unlock professional development practices!</p>
#     <ul>
#         <li><strong>Add linting and formatting checks:</strong> Extend your workflow to
#         run flake8, black, and mypy—enforce code quality standards automatically and never
#         merge poorly formatted code again.</li>
#         <li><strong>Build a deployment pipeline:</strong> Add steps that build documentation with Sphinx, run performance
#         benchmarks, and deploy to GitHub Pages—automate your entire release process.</li>
#         <li><strong>Set up status badges:</strong> Add workflow status badges to your README that show build status, test
#         coverage, and documentation status—make quality visible at a glance.</li>
#     </ul>
# </div>

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
# <div style="background-color: #f3e5f5; border-left: 5px solid #9c27b0; padding: 15px; margin: 10px 0; border-radius: 5px;">
#     <h4 style="color: #7b1fa2; margin-top: 0;">💡 Try It Yourself</h4>
#     <p>Optimize your CI pipeline for speed and reliability—every second counts!</p>
#     <ul>
#         <li><strong>Measure and optimize runtime:</strong> Add timing to each workflow
#         step, identify the slowest parts, and optimize them—try caching dependencies,
#         running jobs in parallel, or using faster test selection strategies.</li>
#         <li><strong>Implement smart caching:</strong> Cache pip packages, pre-built
#         dependencies, and test databases across runs—reduce a 5-minute build to 30 seconds
#         by reusing previous work.</li>
#         <li><strong>Handle flaky tests:</strong> Identify tests that randomly fail, add
#         retries with proper delays, or refactor them to be deterministic—build a CI
#         pipeline you can trust 100% of the time.</li>
#     </ul>
# </div>

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

# %% [markdown]
# ## Acknowledgements and References
# 
# This lecture synthesizes best practices from CI/CD documentation and research software engineering:
# 
# ### Primary Sources
# 
# - **Research Software Engineering with Python** by The Alan Turing Institute  
#   <https://alan-turing-institute.github.io/rse-course/html/>  
#   Continuous integration concepts, workflow patterns, and automation strategies adapted from this course.
# 
# - **Research Software Engineering with Python** by Damien Irving, Kate Hertweck,
#   Luke Johnston, Joel Ostblom, Charlotte Wickham, and Greg Wilson (2022)
#   <https://third-bit.com/py-rse/>
#   Chapter on "Continuous Integration" provided foundational CI/CD concepts for
#   research workflows.
# 
# ### Platform Documentation
# 
# - **GitHub Actions Documentation**  
#   <https://docs.github.com/en/actions>  
#   Official GitHub Actions reference for workflow syntax and features.
#   - Workflow Syntax: <https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions>
#   - Events that trigger workflows: <https://docs.github.com/en/actions/reference/events-that-trigger-workflows>
#   - GitHub Actions Marketplace: <https://github.com/marketplace?type=actions>
# 
# - **GitLab CI/CD Documentation**  
#   <https://docs.gitlab.com/ee/ci/>  
#   Official GitLab CI/CD reference for pipeline configuration.
#   - CI/CD YAML syntax: <https://docs.gitlab.com/ee/ci/yaml/>
#   - GitLab CI/CD examples: <https://docs.gitlab.com/ee/ci/examples/>
#   - Auto DevOps: <https://docs.gitlab.com/ee/topics/autodevops/>
# 
# ### Testing Integration
# 
# - **pytest Documentation**  
#   <https://docs.pytest.org/>  
#   For running tests in CI environments.
# 
# - **pytest-cov Plugin**  
#   <https://pytest-cov.readthedocs.io/>  
#   For coverage reporting in CI pipelines.
# 
# ### Additional CI/CD Resources
# 
# - **Travis CI Documentation**  
#   <https://docs.travis-ci.com/>  
#   Alternative CI platform (referenced for comparison).
# 
# - **CircleCI Documentation**  
#   <https://circleci.com/docs/>  
#   Alternative CI platform (referenced for comparison).
# 
# ### Best Practices Sources
# 
# - **The Twelve-Factor App**  
#   <https://12factor.net/>  
#   Methodology for building software-as-a-service, influencing CI/CD best practices.
# 
# - **Software Carpentry**  
#   Automation principles for scientific computing.
# 
# ### Notes
# 
# All workflow examples and configurations are original creations for this course, following official
# documentation and community best practices. The lecture builds on the testing concepts from Lecture 5,
# showing how to automate them through CI/CD pipelines on GitHub and GitLab platforms.

# %% [markdown]
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

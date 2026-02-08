# Lecture 3: Documentation and Code Quality

## Overview
This lecture focuses on writing good documentation, maintaining code quality, and using tools to automate quality checks.

## Topics Covered
- The importance of documentation
- Types of documentation (docstrings, README, tutorials, API docs)
- Code quality metrics
- Automated quality tools (linters, formatters, type checkers)

## Files
- `lecture_03.py` - Main lecture content in Jupytext format

## Running the Lecture

1. Create and activate the base environment:
```bash
cd /path/to/RSE_lecture
make install
micromamba activate rse_lecture
```

Or manually:
```bash
micromamba env create -f environment.yml
micromamba activate rse_lecture
```

**Note:** Lecture 3 uses only the base environment with no additional dependencies.

2. Convert to notebook and run:
```bash
cd lecture_03
jupytext --to notebook lecture_03.py
jupyter notebook lecture_03.ipynb
```

Or from the main repository directory:
```bash
make convert
jupyter notebook
```

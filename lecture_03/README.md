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

### Using micromamba (Recommended)

1. Create and activate the environment for this lecture:
```bash
cd /path/to/RSE_lecture
micromamba env create -f lecture_03/environment.yml
micromamba activate rse_lecture_03
```

Or use the Makefile:
```bash
make install-lecture3
micromamba activate rse_lecture_03
```

2. Convert to notebook and run:
```bash
cd lecture_03
jupytext --to notebook lecture_03.py
jupyter notebook lecture_03.ipynb
```

### Using pip

Convert to notebook:
```bash
jupytext --to notebook lecture_03.py
jupyter notebook lecture_03.ipynb
```

Or from the main repository directory:
```bash
make convert
jupyter notebook
```
